"""
GeoPulse GPS Data Schema

Defines the standard PySpark schema for raw GPS mobility data.
"""

from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    DoubleType,
    TimestampType
)


GPS_SCHEMA = StructType([
    StructField(
        "device_id",
        StringType(),
        False
    ),
    StructField(
        "latitude",
        DoubleType(),
        False
    ),
    StructField(
        "longitude",
        DoubleType(),
        False
    ),
    StructField(
        "timestamp",
        TimestampType(),
        False
    )
])