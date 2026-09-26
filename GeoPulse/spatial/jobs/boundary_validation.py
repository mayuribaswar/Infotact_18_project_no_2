"""
GeoPulse Geographic Boundary Validation

This job loads GPS records using PySpark and validates
whether each GPS coordinate belongs to the configured
geographic boundary.
"""

from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    when,
    lit
)

from spatial.schemas.gps_schema import GPS_SCHEMA
from spatial.utils.boundary import (
    MIN_LATITUDE,
    MAX_LATITUDE,
    MIN_LONGITUDE,
    MAX_LONGITUDE
)


def create_spark_session():
    """Create and configure Spark session."""

    return (
        SparkSession.builder
        .appName("GeoPulse-Boundary-Validation")
        .master("local[*]")
        .getOrCreate()
    )


def load_gps_data(spark, file_path):
    """Load GPS CSV data using the predefined schema."""

    return (
        spark.read
        .option("header", True)
        .schema(GPS_SCHEMA)
        .csv(file_path)
    )


def validate_coordinates(gps_df):
    """
    Validate latitude and longitude values.

    A record is valid when:
        MIN_LATITUDE <= latitude <= MAX_LATITUDE
        MIN_LONGITUDE <= longitude <= MAX_LONGITUDE
    """

    validated_df = gps_df.withColumn(
        "boundary_status",
        when(
            col("latitude").isNull()
            | col("longitude").isNull(),
            lit("INVALID")
        )
        .when(
            (col("latitude") >= MIN_LATITUDE)
            & (col("latitude") <= MAX_LATITUDE)
            & (col("longitude") >= MIN_LONGITUDE)
            & (col("longitude") <= MAX_LONGITUDE),
            lit("VALID")
        )
        .otherwise(lit("INVALID"))
    )

    return validated_df


def main():

    project_root = Path(__file__).resolve().parents[2]

    input_file = project_root / "data" / "sample_gps.csv"

    spark = create_spark_session()

    try:

        print("=" * 70)
        print("GeoPulse - Geographic Boundary Validation")
        print("=" * 70)

        print("\nConfigured Geographic Boundary:")
        print(f"Latitude : {MIN_LATITUDE} to {MAX_LATITUDE}")
        print(f"Longitude: {MIN_LONGITUDE} to {MAX_LONGITUDE}")

        gps_df = load_gps_data(
            spark,
            str(input_file)
        )

        print("\nTotal GPS Records:")
        print(gps_df.count())

        validated_df = validate_coordinates(gps_df)

        print("\n=== Validation Results ===")

        validated_df.select(
            "device_id",
            "latitude",
            "longitude",
            "timestamp",
            "boundary_status"
        ).show(
            50,
            truncate=False
        )

        print("\n=== Boundary Status Count ===")

        (
            validated_df
            .groupBy("boundary_status")
            .count()
            .orderBy("boundary_status")
            .show()
        )

        print("\n=== Valid GPS Records ===")

        (
            validated_df
            .filter(col("boundary_status") == "VALID")
            .show(
                50,
                truncate=False
            )
        )

        print("\n=== Invalid GPS Records ===")

        (
            validated_df
            .filter(col("boundary_status") == "INVALID")
            .show(
                50,
                truncate=False
            )
        )

        print("\nBoundary validation completed successfully.")

    finally:
        spark.stop()


if __name__ == "__main__":
    main()