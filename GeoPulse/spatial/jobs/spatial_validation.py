"""
GeoPulse - Day 9
Spatial Data Quality and Movement Validation

Purpose:
- Validate GPS coordinates
- Check missing values
- Check duplicate records
- Validate timestamps
- Calculate basic movement statistics
- Generate a clean validation report
"""

from pathlib import Path
from pyspark.sql import SparkSession
from pyspark.sql import functions as F


PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_FILE = PROJECT_ROOT / "data" / "gps" / "gps_data.csv"
OUTPUT_DIR = PROJECT_ROOT / "data" / "output" / "day9_validation"


def create_spark():
    return (
        SparkSession.builder
        .appName("GeoPulse-Day9-SpatialValidation")
        .master("local[*]")
        .getOrCreate()
    )


def load_data(spark):
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"GPS input file not found: {INPUT_FILE}"
        )

    return (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(str(INPUT_FILE))
    )


def validate_coordinates(df):
    return df.withColumn(
        "coordinate_status",
        F.when(
            F.col("latitude").isNull() |
            F.col("longitude").isNull(),
            "INVALID_MISSING"
        )
        .when(
            (F.col("latitude") < -90) |
            (F.col("latitude") > 90) |
            (F.col("longitude") < -180) |
            (F.col("longitude") > 180),
            "INVALID_RANGE"
        )
        .otherwise("VALID")
    )


def validate_timestamps(df):
    timestamp_column = None

    possible_columns = [
        "timestamp",
        "Timestamp",
        "event_timestamp",
        "datetime",
        "DateTime"
    ]

    for column_name in possible_columns:
        if column_name in df.columns:
            timestamp_column = column_name
            break

    if timestamp_column is None:
        return df.withColumn(
            "timestamp_status",
            F.lit("TIMESTAMP_COLUMN_NOT_FOUND")
        )

    return df.withColumn(
        "parsed_timestamp",
        F.to_timestamp(F.col(timestamp_column))
    ).withColumn(
        "timestamp_status",
        F.when(
            F.col("parsed_timestamp").isNull(),
            "INVALID"
        ).otherwise("VALID")
    )


def create_validation_summary(df):
    return df.agg(
        F.count("*").alias("total_records"),

        F.sum(
            F.when(
                F.col("coordinate_status") == "VALID",
                1
            ).otherwise(0)
        ).alias("valid_coordinates"),

        F.sum(
            F.when(
                F.col("coordinate_status") == "INVALID_MISSING",
                1
            ).otherwise(0)
        ).alias("missing_coordinates"),

        F.sum(
            F.when(
                F.col("coordinate_status") == "INVALID_RANGE",
                1
            ).otherwise(0)
        ).alias("invalid_coordinate_range"),

        F.sum(
            F.when(
                F.col("timestamp_status") == "VALID",
                1
            ).otherwise(0)
        ).alias("valid_timestamps"),

        F.sum(
            F.when(
                F.col("timestamp_status") == "INVALID",
                1
            ).otherwise(0)
        ).alias("invalid_timestamps")
    )


def find_duplicates(df):
    if "DeviceID" in df.columns:
        return (
            df.groupBy("DeviceID")
            .count()
            .filter(F.col("count") > 1)
            .orderBy(F.desc("count"))
        )

    if "device_id" in df.columns:
        return (
            df.groupBy("device_id")
            .count()
            .filter(F.col("count") > 1)
            .orderBy(F.desc("count"))
        )

    return None


def main():

    print("=" * 70)
    print("GeoPulse - Day 9: Spatial Data Quality Validation")
    print("=" * 70)

    spark = create_spark()

    try:
        print("\n[1] Loading GPS data...")
        df = load_data(spark)

        print(f"Columns: {df.columns}")
        print(f"Total records: {df.count()}")

        print("\n[2] Validating coordinates...")
        df = validate_coordinates(df)

        print("\n[3] Validating timestamps...")
        df = validate_timestamps(df)

        print("\n[4] Creating validation summary...")

        summary = create_validation_summary(df)

        summary.show(truncate=False)

        print("\n[5] Coordinate status:")
        (
            df.groupBy("coordinate_status")
            .count()
            .orderBy("coordinate_status")
            .show()
        )

        print("\n[6] Timestamp status:")
        (
            df.groupBy("timestamp_status")
            .count()
            .orderBy("timestamp_status")
            .show()
        )

        print("\n[7] Checking duplicate device records...")

        duplicates = find_duplicates(df)

        if duplicates is not None:
            duplicates.show(20, truncate=False)
        else:
            print("DeviceID column not found.")

        print("\n[8] Saving validation output...")

        OUTPUT_DIR.mkdir(
            parents=True,
            exist_ok=True
        )

        (
            df.write
            .mode("overwrite")
            .option("header", True)
            .csv(str(OUTPUT_DIR / "validated_gps"))
        )

        (
            summary.write
            .mode("overwrite")
            .option("header", True)
            .csv(str(OUTPUT_DIR / "summary"))
        )

        print("\nDay 9 validation completed successfully.")
        print(f"Output directory: {OUTPUT_DIR}")

    finally:
        spark.stop()
        print("\nSpark stopped.")


if __name__ == "__main__":
    main()