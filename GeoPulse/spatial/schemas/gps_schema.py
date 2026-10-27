"""
GeoPulse GPS Data Schema

Defines the standard PySpark schema for GPS mobility data.
Supports baseline coordinates and optional receiver telemetry.
"""

from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    DoubleType,
    TimestampType
)

GPS_SCHEMA = StructType([
    StructField("device_id", StringType(), nullable=False),
    StructField("latitude", DoubleType(), nullable=False),
    StructField("longitude", DoubleType(), nullable=False),
    StructField("timestamp", TimestampType(), nullable=False),
    StructField("accuracy", DoubleType(), nullable=True)
])