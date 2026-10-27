"""
GeoPulse - Day 11
Hotspot Insight & Risk Classification

Purpose:
    Classify spatial grids into HIGH, MEDIUM, or LOW risk
    based on hotspot scores and event activity.

Input:
    data/output/hotspot_results.csv

Outputs:
    data/output/risk_classification.csv
    data/output/hotspot_insights.txt
"""

from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    when,
    count,
    countDistinct,
    avg,
    round as spark_round,
)


# -------------------------------------------------------------------
# Paths
# -------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_FILE = PROJECT_ROOT / "data" / "output" / "hotspot_results.csv"
OUTPUT_DIR = PROJECT_ROOT / "data" / "output"

RISK_OUTPUT = OUTPUT_DIR / "risk_classification.csv"
INSIGHT_OUTPUT = OUTPUT_DIR / "hotspot_insights.txt"


# -------------------------------------------------------------------
# Spark Session
# -------------------------------------------------------------------

def create_spark_session():
    """Create and return Spark session."""

    return (
        SparkSession.builder
        .appName("GeoPulse-Day11-RiskClassification")
        .master("local[*]")
        .getOrCreate()
    )


# -------------------------------------------------------------------
# Load Data
# -------------------------------------------------------------------

def load_hotspot_data(spark):
    """Load hotspot result CSV."""

    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Input file not found: {INPUT_FILE}"
        )

    print(f"[1] Loading hotspot data...")
    print(f"    File: {INPUT_FILE}")

    df = (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(str(INPUT_FILE))
    )

    print(f"    Rows loaded: {df.count()}")

    return df


# -------------------------------------------------------------------
# Detect Columns
# -------------------------------------------------------------------

def find_column(df, possible_names):
    """
    Find the first matching column from possible column names.
    Matching is case-insensitive.
    """

    columns = {column.lower(): column for column in df.columns}

    for name in possible_names:
        if name.lower() in columns:
            return columns[name.lower()]

    return None


# -------------------------------------------------------------------
# Prepare Data
# -------------------------------------------------------------------

def prepare_data(df):
    """Prepare hotspot data for classification."""

    print("[2] Preparing hotspot data...")

    grid_column = find_column(
        df,
        [
            "grid_id",
            "grid",
            "cell_id",
            "cell",
            "geohash",
        ],
    )

    score_column = find_column(
        df,
        [
            "hotspot_score",
            "hotspot",
            "score",
            "density",
            "hotspot_density",
        ],
    )

    event_column = find_column(
        df,
        [
            "event_count",
            "events",
            "count",
            "activity_count",
        ],
    )

    user_column = find_column(
        df,
        [
            "user_id",
            "vehicle_id",
            "device_id",
            "user",
        ],
    )

    # ---------------------------------------------------------------
    # Grid ID
    # ---------------------------------------------------------------

    if grid_column is None:
        raise ValueError(
            "Could not find a grid identifier column."
        )

    prepared = df.withColumn(
        "grid_id",
        col(grid_column).cast("string")
    )

    # ---------------------------------------------------------------
    # Hotspot score
    # ---------------------------------------------------------------

    if score_column is not None:
        prepared = prepared.withColumn(
            "hotspot_score",
            col(score_column).cast("double")
        )
    else:
        print(
            "    Warning: hotspot score column not found."
        )

        prepared = prepared.withColumn(
            "hotspot_score",
            col("grid_id").isNotNull().cast("double")
        )

    # ---------------------------------------------------------------
    # Event count
    # ---------------------------------------------------------------

    if event_column is not None:
        prepared = prepared.withColumn(
            "event_count",
            col(event_column).cast("double")
        )
    else:
        prepared = prepared.withColumn(
            "event_count",
            col("hotspot_score")
        )

    # ---------------------------------------------------------------
    # User count
    # ---------------------------------------------------------------

    if user_column is not None:
        prepared = prepared.withColumn(
            "unique_users",
            col(user_column).cast("string")
        )
    else:
        prepared = prepared.withColumn(
            "unique_users",
            col("grid_id")
        )

    return prepared


# -------------------------------------------------------------------
# Aggregate Grid Statistics
# -------------------------------------------------------------------

def calculate_grid_statistics(df):
    """Calculate statistics for every spatial grid."""

    print("[3] Calculating grid statistics...")

    stats = (
        df.groupBy("grid_id")
        .agg(
            spark_round(avg("hotspot_score"), 4).alias(
                "hotspot_score"
            ),
            spark_round(avg("event_count"), 2).alias(
                "event_count"
            ),
            countDistinct("unique_users").alias(
                "unique_users"
            ),
        )
    )

    return stats


# -------------------------------------------------------------------
# Risk Classification
# -------------------------------------------------------------------

def classify_risk(df):
    """
    Classify each grid.

    HIGH:
        hotspot score >= 0.70

    MEDIUM:
        hotspot score >= 0.40 and < 0.70

    LOW:
        hotspot score < 0.40
    """

    print("[4] Classifying risk levels...")

    classified = df.withColumn(
        "risk_level",
        when(
            col("hotspot_score") >= 0.70,
            "HIGH"
        )
        .when(
            col("hotspot_score") >= 0.40,
            "MEDIUM"
        )
        .otherwise("LOW")
    )

    return classified


# -------------------------------------------------------------------
# Save CSV
# -------------------------------------------------------------------

def save_risk_results(df):
    """Save risk classification results."""

    print("[5] Saving risk classification...")

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    pandas_df = df.orderBy(
        col("hotspot_score").desc()
    ).toPandas()

    pandas_df.to_csv(
        RISK_OUTPUT,
        index=False
    )

    print(f"    Output: {RISK_OUTPUT}")


# -------------------------------------------------------------------
# Generate Insights
# -------------------------------------------------------------------

def generate_insights(df):
    """Generate a text-based hotspot insight report."""

    print("[6] Generating hotspot insights...")

    total_grids = df.count()

    high_count = df.filter(
        col("risk_level") == "HIGH"
    ).count()

    medium_count = df.filter(
        col("risk_level") == "MEDIUM"
    ).count()

    low_count = df.filter(
        col("risk_level") == "LOW"
    ).count()

    highest = (
        df.orderBy(
            col("hotspot_score").desc()
        )
        .limit(5)
        .collect()
    )

    average_score = (
        df.select(
            spark_round(
                avg("hotspot_score"),
                4
            ).alias("average_score")
        )
        .collect()[0]["average_score"]
    )

    lines = []

    lines.append("=" * 70)
    lines.append("GeoPulse - Day 11 Hotspot Insights")
    lines.append("=" * 70)
    lines.append("")

    lines.append(f"Total spatial grids analyzed : {total_grids}")
    lines.append(f"Average hotspot score        : {average_score}")
    lines.append("")

    lines.append("Risk Distribution")
    lines.append("-" * 30)
    lines.append(f"HIGH grids   : {high_count}")
    lines.append(f"MEDIUM grids : {medium_count}")
    lines.append(f"LOW grids    : {low_count}")
    lines.append("")

    lines.append("Top Hotspot Grids")
    lines.append("-" * 30)

    for index, row in enumerate(highest, start=1):
        lines.append(
            f"{index}. Grid: {row['grid_id']} | "
            f"Score: {row['hotspot_score']} | "
            f"Events: {row['event_count']} | "
            f"Users: {row['unique_users']} | "
            f"Risk: {row['risk_level']}"
        )

    lines.append("")
    lines.append("Interpretation")
    lines.append("-" * 30)

    if high_count > 0:
        lines.append(
            "High-risk grids require priority monitoring "
            "because they show strong spatial activity."
        )
    else:
        lines.append(
            "No high-risk grids were detected."
        )

    if medium_count > 0:
        lines.append(
            "Medium-risk grids should be monitored for "
            "increasing activity."
        )

    if low_count > 0:
        lines.append(
            "Low-risk grids currently show comparatively "
            "lower hotspot activity."
        )

    lines.append("")
    lines.append("=" * 70)

    INSIGHT_OUTPUT.write_text(
        "\n".join(lines),
        encoding="utf-8"
    )

    print(f"    Output: {INSIGHT_OUTPUT}")


# -------------------------------------------------------------------
# Main
# -------------------------------------------------------------------

def main():

    print("=" * 70)
    print("GeoPulse - Day 11: Hotspot Insight & Risk Classification")
    print("=" * 70)

    spark = create_spark_session()

    try:

        df = load_hotspot_data(spark)

        df = prepare_data(df)

        stats = calculate_grid_statistics(df)

        classified = classify_risk(stats)

        print("")
        print("[7] Risk classification preview:")
        classified.orderBy(
            col("hotspot_score").desc()
        ).show(
            10,
            truncate=False
        )

        save_risk_results(classified)

        generate_insights(classified)

        print("")
        print("=" * 70)
        print("Day 11 completed successfully!")
        print("=" * 70)

    finally:
        spark.stop()


if __name__ == "__main__":
    main()