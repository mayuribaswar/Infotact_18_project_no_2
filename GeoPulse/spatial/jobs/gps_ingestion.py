"""Loads sample GPS records into PySpark using the defined schema."""
from pathlib import Path
from pyspark.sql import SparkSession
from spatial.schemas.gps_schema import GPS_SCHEMA

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = PROJECT_ROOT / "data" / "sample_gps.csv"


def main():
    spark = SparkSession.builder.appName("GeoPulse-Ingestion").master("local[*]").getOrCreate()
    try:
        df = spark.read.option("header", True).schema(GPS_SCHEMA).csv(str(DATA_PATH))
        print("=== GPS Data Sample ===")
        df.show(5, truncate=False)
        print(f"Total Loaded Records: {df.count()}")
    finally:
        spark.stop()


if __name__ == "__main__":
    main()