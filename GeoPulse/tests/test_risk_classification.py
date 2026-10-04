"""
GeoPulse - Day 11 Tests
Tests for hotspot risk classification.
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col


def create_test_spark():
    """Create Spark session for testing."""

    return (
        SparkSession.builder
        .appName("GeoPulse-Day11-Tests")
        .master("local[2]")
        .getOrCreate()
    )


def classify_risk(score):
    """Return risk level based on hotspot score."""

    if score >= 0.70:
        return "HIGH"

    if score >= 0.40:
        return "MEDIUM"

    return "LOW"


def test_high_risk():
    """Score >= 0.70 should be HIGH."""

    assert classify_risk(0.70) == "HIGH"
    assert classify_risk(0.90) == "HIGH"
    assert classify_risk(1.00) == "HIGH"


def test_medium_risk():
    """Score between 0.40 and 0.70 should be MEDIUM."""

    assert classify_risk(0.40) == "MEDIUM"
    assert classify_risk(0.55) == "MEDIUM"
    assert classify_risk(0.69) == "MEDIUM"


def test_low_risk():
    """Score below 0.40 should be LOW."""

    assert classify_risk(0.00) == "LOW"
    assert classify_risk(0.20) == "LOW"
    assert classify_risk(0.39) == "LOW"


def test_boundary_values():
    """Test classification boundary values."""

    assert classify_risk(0.3999) == "LOW"
    assert classify_risk(0.40) == "MEDIUM"
    assert classify_risk(0.6999) == "MEDIUM"
    assert classify_risk(0.70) == "HIGH"


def test_spark_dataframe():

    spark = create_test_spark()

    try:

        data = [
            ("19998_73790", 0.91, 1250),
            ("19997_73790", 0.84, 1087),
            ("19997_73789", 0.62, 745),
            ("20005_73798", 0.48, 521),
            ("20000_73793", 0.21, 189),
        ]

        df = spark.createDataFrame(
            data,
            [
                "grid_id",
                "hotspot_score",
                "event_count",
            ],
        )

        assert df.count() == 5

        high = df.filter(
            col("hotspot_score") >= 0.70
        ).count()

        medium = df.filter(
            (col("hotspot_score") >= 0.40)
            & (col("hotspot_score") < 0.70)
        ).count()

        low = df.filter(
            col("hotspot_score") < 0.40
        ).count()

        assert high == 2
        assert medium == 2
        assert low == 1

    finally:
        spark.stop()