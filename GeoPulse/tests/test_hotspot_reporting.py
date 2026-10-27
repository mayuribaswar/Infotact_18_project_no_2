"""
GeoPulse - Day 12
Tests for hotspot reporting module.
"""

import pandas as pd

from spatial.jobs.hotspot_reporting import (
    calculate_event_count,
    calculate_hotspot_score,
    classify_hotspots,
    create_summary,
    generate_statistics,
    normalize_risk_level,
)


def test_normalize_risk_level():

    assert normalize_risk_level("HIGH") == "HIGH"
    assert normalize_risk_level("high") == "HIGH"
    assert normalize_risk_level("MEDIUM") == "MEDIUM"
    assert normalize_risk_level("LOW") == "LOW"


def test_calculate_event_count():

    df = pd.DataFrame(
        {
            "grid_id": ["A", "B"],
            "event_count": [10, 20],
        }
    )

    result = calculate_event_count(df)

    assert "event_count" in result.columns
    assert result["event_count"].sum() == 30


def test_calculate_hotspot_score():

    df = pd.DataFrame(
        {
            "grid_id": ["A", "B"],
            "hotspot_score": [5.5, 10.5],
        }
    )

    result = calculate_hotspot_score(df)

    assert "hotspot_score" in result.columns
    assert result["hotspot_score"].max() == 10.5


def test_classify_hotspots():

    df = pd.DataFrame(
        {
            "grid_id": ["A", "B", "C"],
            "risk_level": [
                "HIGH",
                "MEDIUM",
                "LOW",
            ],
        }
    )

    result = classify_hotspots(df)

    assert list(result["risk_level"]) == [
        "HIGH",
        "MEDIUM",
        "LOW",
    ]


def test_create_summary():

    df = pd.DataFrame(
        {
            "grid_id": ["A", "B"],
            "latitude": [19.99, 20.00],
            "longitude": [73.78, 73.79],
            "risk_level": ["HIGH", "LOW"],
            "event_count": [100, 20],
            "hotspot_score": [50, 10],
        }
    )

    result = create_summary(df)

    assert len(result) == 2
    assert "grid_id" in result.columns
    assert "risk_level" in result.columns
    assert "event_count" in result.columns
    assert "hotspot_score" in result.columns


def test_generate_statistics():

    df = pd.DataFrame(
        {
            "grid_id": ["A", "B", "C"],
            "risk_level": [
                "HIGH",
                "MEDIUM",
                "LOW",
            ],
            "event_count": [100, 50, 20],
            "hotspot_score": [50, 25, 10],
        }
    )

    statistics = generate_statistics(df)

    assert statistics["total_hotspots"] == 3
    assert statistics["high_risk_hotspots"] == 1
    assert statistics["medium_risk_hotspots"] == 1
    assert statistics["low_risk_hotspots"] == 1
    assert statistics["total_events"] == 170
    assert statistics["maximum_hotspot_score"] == 50