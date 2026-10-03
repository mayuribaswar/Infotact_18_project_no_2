"""
jobs/pipeline.py - Day 10: End-to-End GeoPulse Pipeline Runner
Orchestrates ingestion, spatial validation, movement calculation, 
hotspot clustering, and final artifact export.
"""

import sys
import logging
from pathlib import Path
from pyspark.sql import SparkSession
from sedona.register import SedonaRegistrator

# Import existing project modules
from jobs.gps_ingestion import ingest_gps_data
from jobs.spatial_validation import validate_spatial_data
from jobs.boundary_validation import filter_by_boundary
from jobs.movement_analysis import calculate_movement_metrics
from jobs.hotspot_analysis import detect_hotspots
from jobs.hotspot_visualization import generate_hotspot_map

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger("GeoPulsePipeline")


def create_sedona_session(app_name: str = "GeoPulse-Pipeline") -> SparkSession:
    """Initializes SparkSession with Apache Sedona registration."""
    spark = (
        SparkSession.builder.appName(app_name)
        .config("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
        .config("spark.kryo.registrator", "org.apache.sedona.core.serde.SedonaKryoRegistrator")
        .config("spark.sql.extensions", "org.apache.sedona.viz.sql.SedonaVizExtensions")
        .getOrCreate()
    )
    SedonaRegistrator.registerAll(spark)
    return spark


def run_pipeline(
    raw_data_path: str,
    boundary_geojson_path: str,
    output_dir: str
):
    """Executes the complete GeoPulse processing flow."""
    spark = create_sedona_session()
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    try:
        # Step 1: Ingestion
        logger.info("Step 1/5: Ingesting raw GPS data from %s", raw_data_path)
        raw_df = ingest_gps_data(spark, raw_data_path)

        # Step 2: Coordinate & Boundary Validation
        logger.info("Step 2/5: Filtering valid geometries and boundary clipping")
        valid_df = validate_spatial_data(raw_df)
        bounded_df = filter_by_boundary(valid_df, boundary_geojson_path)

        # Step 3: Movement & Trajectory Analysis
        logger.info("Step 3/5: Calculating speed, dwell times, and trajectories")
        movement_df = calculate_movement_metrics(bounded_df)
        movement_df.write.mode("overwrite").parquet(str(output_path / "movement_metrics.parquet"))

        # Step 4: Hotspot Clustering
        logger.info("Step 4/5: Running spatial aggregation for retail hotspots")
        hotspot_df = detect_hotspots(movement_df)
        hotspot_df.write.mode("overwrite").parquet(str(output_path / "hotspots.parquet"))

        # Step 5: Visualization & Map Export
        logger.info("Step 5/5: Generating HTML map visualization")
        map_path = str(output_path / "hotspot_map.html")
        generate_hotspot_map(hotspot_df, output_html_path=map_path)
        
        logger.info("Pipeline completed successfully! Artifacts written to %s", output_dir)

    except Exception as e:
        logger.error("Pipeline run failed: %s", str(e), exc_info=True)
        sys.exit(1)
    finally:
        spark.stop()


if __name__ == "__main__":
    # Default file paths
    RAW_PATH = "data/raw_gps_pings.csv"
    BOUNDARY_PATH = "data/store_boundaries.geojson"
    OUTPUT_PATH = "data/output"

    run_pipeline(RAW_PATH, BOUNDARY_PATH, OUTPUT_PATH)