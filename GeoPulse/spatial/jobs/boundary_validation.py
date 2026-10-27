"""
GeoPulse Geographic Boundary Validation

PySpark pipeline to validate mobility observations against
geographical bounds and annotate rejection causes.
"""

from pathlib import Path
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when, lit

from spatial.schemas.gps_schema import GPS_SCHEMA
from spatial.utils.boundary import (
    MIN_LATITUDE,
    MAX_LATITUDE,
    MIN_LONGITUDE,
    MAX_LONGITUDE
)


def create_spark_session() -> SparkSession:
    """Configure and initialize PySpark Session."""
    return (
        SparkSession.builder
        .appName("GeoPulse-Boundary-Validation")
        .master("local[*]")
        .config("spark.sql.session.timeZone", "UTC")
        .getOrCreate()
    )


def load_gps_data(spark: SparkSession, file_path: str):
    """Load GPS CSV data using standard GPS schema."""
    return (
        spark.read
        .option("header", True)
        .schema(GPS_SCHEMA)
        .csv(file_path)
    )


def validate_coordinates(gps_df):
    """
    Validate coordinates against configured bounding boundaries.
    Generates both validation_reason and boundary_status columns.
    """
    return (
        gps_df
        .withColumn(
            "validation_reason",
            when(
                col("latitude").isNull() | col("longitude").isNull(),
                lit("MISSING_COORDINATES")
            )
            .when(
                (col("latitude") < MIN_LATITUDE) | (col("latitude") > MAX_LATITUDE),
                lit("OUTSIDE_LATITUDE")
            )
            .when(
                (col("longitude") < MIN_LONGITUDE) | (col("longitude") > MAX_LONGITUDE),
                lit("OUTSIDE_LONGITUDE")
            )
            .otherwise(lit("WITHIN_BOUNDARY"))
        )
        .withColumn(
            "boundary_status",
            when(col("validation_reason") == "WITHIN_BOUNDARY", lit("VALID"))
            .otherwise(lit("INVALID"))
        )
    )


def main():
    project_root = Path(__file__).resolve().parents[2]
    input_file = project_root / "data" / "sample_gps.csv"

    spark = create_spark_session()
    try:
        print("=" * 70)
        print("GeoPulse - Geographic Boundary Validation")
        print("=" * 70)
        print(f"Bounding Lat : {MIN_LATITUDE} to {MAX_LATITUDE}")
        print(f"Bounding Lon : {MIN_LONGITUDE} to {MAX_LONGITUDE}\n")

        gps_df = load_gps_data(spark, str(input_file))
        total_records = gps_df.count()
        print(f"Total Ingested GPS Records: {total_records}")

        validated_df = validate_coordinates(gps_df).cache()

        print("\n=== Sample Validation Breakdown ===")
        validated_df.select(
            "device_id", "latitude", "longitude", "timestamp", "boundary_status", "validation_reason"
        ).show(15, truncate=False)

        print("\n=== Validation Status Counts ===")
        validated_df.groupBy("boundary_status", "validation_reason").count().show()

        valid_count = validated_df.filter(col("boundary_status") == "VALID").count()
        invalid_count = validated_df.filter(col("boundary_status") == "INVALID").count()
        print(f"Summary: {valid_count} Valid Records | {invalid_count} Invalid Records")

    finally:
        spark.stop()


if __name__ == "__main__":
    main()