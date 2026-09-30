"""
GeoPulse - Day 7
Spatial Hotspot Analysis

This job:
1. Creates sample GPS data
2. Validates latitude and longitude
3. Creates Sedona Point geometry
4. Assigns GPS points to spatial grid cells
5. Calculates hotspot statistics
6. Classifies grid cells as LOW, MEDIUM, or HIGH density

Windows-safe version:
- Sample data is created using Spark SQL VALUES
- Avoids Python createDataFrame() worker startup
- Apache Sedona is initialized through SedonaContext
"""

import sys

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from sedona.spark import SedonaContext


# ============================================================
# 1. CREATE SPARK SESSION
# ============================================================

def create_spark_session():
    """
    Create Spark session with Apache Sedona dependencies.
    """

    python_executable = sys.executable

    print("\nPython executable:")
    print(python_executable)

    spark = (
        SparkSession.builder
        .appName("GeoPulse-Hotspot-Analysis")
        .master("local[*]")

        # ----------------------------------------------------
        # Apache Sedona
        # ----------------------------------------------------
        .config(
            "spark.jars.packages",
            "org.apache.sedona:sedona-spark-3.5_2.12:1.7.2,"
            "org.datasyslab:geotools-wrapper:1.7.2-28.5"
        )

        # ----------------------------------------------------
        # Sedona serializer
        # ----------------------------------------------------
        .config(
            "spark.serializer",
            "org.apache.spark.serializer.KryoSerializer"
        )

        .config(
            "spark.kryo.registrator",
            "org.apache.sedona.core.serde.SedonaKryoRegistrator"
        )

        # ----------------------------------------------------
        # Python configuration
        # ----------------------------------------------------
        .config(
            "spark.pyspark.python",
            python_executable
        )

        .config(
            "spark.pyspark.driver.python",
            python_executable
        )

        # ----------------------------------------------------
        # Run locally with one executor
        # ----------------------------------------------------
        .config(
            "spark.executor.instances",
            "1"
        )

        .config(
            "spark.python.worker.reuse",
            "false"
        )

        .getOrCreate()
    )

    # Initialize Sedona
    spark = SedonaContext.create(spark)

    return spark


# ============================================================
# 2. CREATE SAMPLE GPS DATA
# ============================================================

def create_sample_data(spark):
    """
    Create sample GPS data using Spark SQL.

    IMPORTANT:
    We intentionally do NOT use spark.createDataFrame()
    because that can start a Python worker on Windows.

    Spark SQL VALUES creates the DataFrame directly
    on the JVM side.
    """

    query = """
        SELECT
            device_id,
            CAST(latitude AS DOUBLE) AS latitude,
            CAST(longitude AS DOUBLE) AS longitude
        FROM VALUES
            ('D001', 19.9975, 73.7898),
            ('D001', 19.9978, 73.7901),
            ('D001', 19.9980, 73.7903),

            ('D002', 19.9976, 73.7899),
            ('D002', 19.9979, 73.7902),

            ('D003', 19.9981, 73.7904),
            ('D003', 19.9983, 73.7906),

            ('D004', 19.9977, 73.7900),

            ('D005', 20.0000, 73.7930),

            ('D006', 20.0050, 73.7980)

        AS gps_data(
            device_id,
            latitude,
            longitude
        )
    """

    df = spark.sql(query)

    return df


# ============================================================
# 3. VALIDATE COORDINATES
# ============================================================

def validate_coordinates(df):
    """
    Validate latitude and longitude.

    Latitude:
        -90 <= latitude <= 90

    Longitude:
        -180 <= longitude <= 180
    """

    df = df.filter(
        F.col("latitude").isNotNull()
        & F.col("longitude").isNotNull()
        & F.col("latitude").between(-90, 90)
        & F.col("longitude").between(-180, 180)
    )

    return df


# ============================================================
# 4. CREATE SEDONA POINT GEOMETRY
# ============================================================

def create_geometry(df):
    """
    Create Sedona Point geometry.

    ST_Point(
        longitude,
        latitude
    )

    Longitude comes first.
    Latitude comes second.
    """

    df = df.withColumn(
        "geometry",
        F.expr(
            """
            ST_Point(
                CAST(longitude AS DOUBLE),
                CAST(latitude AS DOUBLE)
            )
            """
        )
    )

    return df


# ============================================================
# 5. CREATE SPATIAL GRID
# ============================================================

def create_grid(df, grid_size=1000):
    """
    Assign every GPS point to a spatial grid cell.

    grid_size = 1000 gives approximately
    three decimal places of grid precision.
    """

    df = (
        df
        .withColumn(
            "grid_lat",
            F.floor(
                F.col("latitude") * grid_size
            )
        )
        .withColumn(
            "grid_lon",
            F.floor(
                F.col("longitude") * grid_size
            )
        )
        .withColumn(
            "grid_id",
            F.concat_ws(
                "_",
                F.col("grid_lat"),
                F.col("grid_lon")
            )
        )
    )

    return df


# ============================================================
# 6. CALCULATE HOTSPOTS
# ============================================================

def calculate_hotspots(df):
    """
    Calculate hotspot statistics for every grid cell.

    Metrics:
        point_count
        unique_devices
        avg_points_per_device
    """

    hotspot_df = (
        df
        .groupBy("grid_id")
        .agg(
            F.count("*").alias("point_count"),

            F.countDistinct(
                "device_id"
            ).alias("unique_devices")
        )
        .withColumn(
            "avg_points_per_device",
            F.round(
                F.col("point_count")
                / F.col("unique_devices"),
                2
            )
        )
    )

    return hotspot_df


# ============================================================
# 7. CLASSIFY DENSITY
# ============================================================

def classify_density(df):
    """
    Classify each grid cell as:

        HIGH
        MEDIUM
        LOW

    based on point density.
    """

    max_row = (
        df
        .select(
            F.max("point_count").alias("max_count")
        )
        .first()
    )

    max_count = max_row["max_count"]

    if max_count is None:
        return df.withColumn(
            "density",
            F.lit("LOW")
        )

    high_threshold = max_count * 0.66
    medium_threshold = max_count * 0.33

    df = df.withColumn(
        "density",
        F.when(
            F.col("point_count") >= high_threshold,
            F.lit("HIGH")
        )
        .when(
            F.col("point_count") >= medium_threshold,
            F.lit("MEDIUM")
        )
        .otherwise(
            F.lit("LOW")
        )
    )

    return df


# ============================================================
# 8. MAIN
# ============================================================

def main():

    print("=" * 70)
    print("GeoPulse - Day 7: Spatial Hotspot Analysis")
    print("=" * 70)

    spark = None

    try:

        # ----------------------------------------------------
        # Start Spark
        # ----------------------------------------------------
        print("\n[0] Starting Spark + Sedona...")

        spark = create_spark_session()

        print("Spark + Sedona started successfully.")

        # ----------------------------------------------------
        # Stage 1
        # ----------------------------------------------------
        print("\n[1] Loading GPS data...")

        df = create_sample_data(spark)

        print("GPS data loaded successfully.")

        df.show(
            truncate=False
        )

        # ----------------------------------------------------
        # Stage 2
        # ----------------------------------------------------
        print("\n[2] Validating coordinates...")

        df = validate_coordinates(df)

        print("Valid coordinates:")

        df.show(
            truncate=False
        )

        # ----------------------------------------------------
        # Stage 3
        # ----------------------------------------------------
        print("\n[3] Creating Sedona Point geometry...")

        df = create_geometry(df)

        print("Sedona geometry created successfully.")

        df.select(
            "device_id",
            "latitude",
            "longitude",
            "geometry"
        ).show(
            truncate=False
        )

        # ----------------------------------------------------
        # Stage 4
        # ----------------------------------------------------
        print("\n[4] Creating spatial grid...")

        df = create_grid(
            df,
            grid_size=1000
        )

        print("Spatial grid created successfully.")

        df.select(
            "device_id",
            "latitude",
            "longitude",
            "grid_lat",
            "grid_lon",
            "grid_id"
        ).show(
            truncate=False
        )

        # ----------------------------------------------------
        # Stage 5
        # ----------------------------------------------------
        print("\n[5] Calculating hotspot statistics...")

        hotspot_df = calculate_hotspots(df)

        print("Hotspot statistics:")

        hotspot_df.show(
            truncate=False
        )

        # ----------------------------------------------------
        # Stage 6
        # ----------------------------------------------------
        print("\n[6] Classifying hotspot density...")

        final_df = classify_density(
            hotspot_df
        )

        # ----------------------------------------------------
        # Stage 7
        # ----------------------------------------------------
        print("\n[7] FINAL HOTSPOT ANALYSIS")
        print("=" * 70)

        final_df = final_df.orderBy(
            F.desc("point_count")
        )

        final_df.show(
            truncate=False
        )

        # ----------------------------------------------------
        # Summary
        # ----------------------------------------------------
        print("=" * 70)
        print("Day 7 Hotspot Analysis completed successfully!")
        print("=" * 70)

    except Exception as e:

        print("\n" + "=" * 70)
        print("ERROR")
        print("=" * 70)

        print("Error Type:")
        print(type(e).__name__)

        print("\nError Message:")
        print(str(e))

        raise

    finally:

        if spark is not None:

            print("\nStopping Spark...")

            try:
                spark.stop()
            except Exception as stop_error:
                print(
                    "Warning while stopping Spark:",
                    str(stop_error)
                )

            print("Spark stopped.")


# ============================================================
# 9. ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()