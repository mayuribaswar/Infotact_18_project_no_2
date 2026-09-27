
import os
import shutil
import tempfile

from pyspark.sql import SparkSession
from sedona.spark import SedonaContext


# Project-local Spark temporary directory
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

SPARK_TEMP_DIR = os.path.join(PROJECT_ROOT, "spark_temp")

os.makedirs(SPARK_TEMP_DIR, exist_ok=True)


def run_test():
    print("Starting GeoPulse Spatial Environment...")

    spark = (
        SparkSession.builder
        .appName("GeoPulse-Sedona-Test")
        .master("local[*]")
        .config("spark.local.dir", SPARK_TEMP_DIR)
        .config(
            "spark.jars.packages",
            "org.apache.sedona:sedona-spark-shaded-3.5_2.12:1.8.0,"
            "org.datasyslab:geotools-wrapper:1.8.0-33.1"
        )
        .config(
            "spark.serializer",
            "org.apache.spark.serializer.KryoSerializer"
        )
        .config(
            "spark.kryo.registrator",
            "org.apache.sedona.core.serde.SedonaKryoRegistrator"
        )
        .config("spark.driver.memory", "2g")
        .config("spark.executor.memory", "2g")
        .getOrCreate()
    )

    spark.sparkContext.setLogLevel("WARN")

    try:
        print("Creating Sedona context...")

        SedonaContext.create(spark)

        print("========================================")
        print("GeoPulse Sedona Test")
        print("========================================")
        print("Spark Version:", spark.version)

        print("Testing Sedona spatial function...")

        result = spark.sql("""
            SELECT ST_Point(77.5946, 12.9716) AS geom
        """)

        result.show(truncate=False)

        print("========================================")
        print("Sedona spatial function test: SUCCESS")
        print("GeoPulse Spatial Environment: READY")
        print("========================================")

    finally:
        print("Stopping Spark...")
        spark.stop()


if __name__ == "__main__":
    run_test()

