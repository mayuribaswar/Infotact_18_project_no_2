from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    avg,
    col,
    count,
    floor,
    round,
    countDistinct,
    when,
)
from sedona.spark import SedonaContext


# ============================================================
# GeoPulse - Day 7: Spatial Hotspot Analysis
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[2]

DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = DATA_DIR / "output"

GPS_FILE = DATA_DIR / "gps" / "gps_data.csv"
OUTPUT_FILE = OUTPUT_DIR / "hotspot_results.csv"


def create_spark_session():
    print("[0] Starting Spark + Sedona...\n")

    print("Python executable:")
    import sys
    print(sys.executable)

    spark = (
        SparkSession.builder
        .appName("GeoPulse-Day7-HotspotAnalysis")
        .master("local[*]")
        .config(
            "spark.jars.packages",
            "org.apache.sedona:sedona-spark-3.5_2.12:1.7.2,"
            "org.datasyslab:geotools-wrapper:1.7.2-28.5"
        )
        .config(
            "spark.serializer",
            "org.apache.spark.serializer.KryoSerializer"
        )
        .config(
            "spark.kryo.registrator",
            "org.apache.sedona.core.serde.SedonaKryoRegistrator"
        )
        .getOrCreate()
    )

    SedonaContext.create(spark)

    spark.sparkContext.setLogLevel("WARN")

    print("Spark + Sedona started successfully.\n")

    return spark


def load_gps_data(spark):
    print("[1] Loading GPS data...")

    if not GPS_FILE.exists():
        raise FileNotFoundError(
            f"GPS input file not found: {GPS_FILE}"
        )

    df = (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(str(GPS_FILE))
    )

    df = df.select(
        "device_id",
        "latitude",
        "longitude"
    )

    print("GPS data loaded successfully.")

    df.show(truncate=False)

    return df


def validate_coordinates(df):
    print("\n[2] Validating coordinates...")

    valid_df = df.filter(
        col("latitude").between(-90, 90)
        & col("longitude").between(-180, 180)
    )

    print("Valid coordinates:")

    valid_df.show(truncate=False)

    return valid_df


def create_geometry(df):
    print("\n[3] Creating Sedona Point geometry...")

    geometry_df = df.withColumn(
        "geometry",
        # ST_Point expects longitude first, latitude second
        __import__("pyspark.sql.functions").sql.functions.expr(
            "ST_Point(CAST(longitude AS DECIMAL(24,20)), "
            "CAST(latitude AS DECIMAL(24,20)))"
        )
    )

    print("Sedona geometry created successfully.")

    geometry_df.show(truncate=False)

    return geometry_df


def create_spatial_grid(df):
    print("\n[4] Creating spatial grid...")

    grid_df = (
        df
        .withColumn(
            "grid_lat",
            floor(col("latitude") * 1000)
        )
        .withColumn(
            "grid_lon",
            floor(col("longitude") * 1000)
        )
        .withColumn(
            "grid_id",
            __import__("pyspark.sql.functions").sql.functions.concat(
                col("grid_lat"),
                __import__("pyspark.sql.functions").sql.functions.lit("_"),
                col("grid_lon")
            )
        )
    )

    print("Spatial grid created successfully.")

    grid_df.select(
        "device_id",
        "latitude",
        "longitude",
        "grid_lat",
        "grid_lon",
        "grid_id"
    ).show(truncate=False)

    return grid_df


def calculate_hotspot_statistics(df):
    print("\n[5] Calculating hotspot statistics...")

    hotspot_df = (
        df.groupBy("grid_id")
        .agg(
            count("*").alias("point_count"),
            countDistinct("device_id").alias("unique_devices"),
            round(
                avg(col("point_count"))
                if False
                else count("*") / countDistinct("device_id"),
                2
            ).alias("avg_points_per_device")
        )
    )

    print("Hotspot statistics:")

    hotspot_df.show(truncate=False)

    return hotspot_df


def classify_hotspots(df):
    print("\n[6] Classifying hotspot density...")

    classified_df = df.withColumn(
        "density",
        when(col("point_count") >= 2, "HIGH")
        .otherwise("MEDIUM")
    )

    return classified_df


def save_results(df):
    print("\n[7] Saving hotspot results...")

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    # Convert the small final result to Pandas
    # and save as one CSV file.
    pandas_df = df.toPandas()

    pandas_df.to_csv(
        OUTPUT_FILE,
        index=False
    )

    print(f"Hotspot results saved to:")
    print(OUTPUT_FILE)

    print(f"Total hotspot records: {len(pandas_df)}")


def main():
    print("=" * 70)
    print("GeoPulse - Day 7: Spatial Hotspot Analysis")
    print("=" * 70)

    spark = None

    try:
        spark = create_spark_session()

        gps_df = load_gps_data(spark)

        valid_df = validate_coordinates(gps_df)

        geometry_df = create_geometry(valid_df)

        grid_df = create_spatial_grid(geometry_df)

        hotspot_df = calculate_hotspot_statistics(
            grid_df
        )

        final_df = classify_hotspots(
            hotspot_df
        )

        print("\n[8] FINAL HOTSPOT ANALYSIS")
        print("=" * 70)

        final_df.show(
            truncate=False
        )

        save_results(final_df)

        print("=" * 70)
        print("Day 7 Hotspot Analysis completed successfully!")
        print("=" * 70)

    finally:
        if spark is not None:
            print("\nStopping Spark...")
            spark.stop()
            print("Spark stopped.")


if __name__ == "__main__":
    main()