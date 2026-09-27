import pandas as pd
import pytest

from spatial.jobs.movement_analysis import (
    haversine_distance,
    classify_movement,
    is_abnormal_speed,
    analyze_movement,
    create_device_summary,
)


def test_haversine_same_point():
    distance = haversine_distance(19.9975, 73.7898, 19.9975, 73.7898)
    assert distance == pytest.approx(0.0)


def test_stationary_classification():
    assert classify_movement(1.5) == "STATIONARY"


def test_moving_classification():
    assert classify_movement(20) == "MOVING"


def test_fast_moving_classification():
    assert classify_movement(60) == "FAST_MOVING"


def test_unknown_classification():
    assert classify_movement(float("nan")) == "UNKNOWN"


def test_normal_speed():
    assert is_abnormal_speed(80) is False


def test_abnormal_speed():
    assert is_abnormal_speed(150) is True


def test_analyze_movement():
    data = pd.DataFrame(
        {
            "device_id": ["D001", "D001", "D001"],
            "latitude": [19.9975, 19.9985, 20.0000],
            "longitude": [73.7898, 73.7910, 73.7930],
            "timestamp": [
                "2026-09-27 08:00:00",
                "2026-09-27 08:05:00",
                "2026-09-27 08:10:00",
            ],
        }
    )

    result = analyze_movement(data)

    assert len(result) == 3
    assert result.iloc[0]["distance_km"] == 0.0
    assert result.iloc[1]["distance_km"] > 0
    assert result.iloc[2]["distance_km"] > 0
    assert result.iloc[1]["time_difference_seconds"] == 300
    assert result.iloc[1]["speed_kmh"] > 0
    assert (
        result.iloc[2]["cumulative_distance_km"]
        >= result.iloc[1]["cumulative_distance_km"]
    )


def test_device_summary():
    data = pd.DataFrame(
        {
            "device_id": ["D001", "D001", "D002"],
            "distance_km": [0.0, 1.5, 2.0],
            "speed_kmh": [0.0, 18.0, 24.0],
            "abnormal_speed": [False, False, False],
        }
    )

    summary = create_device_summary(data)
    assert len(summary) == 2

    d001 = summary[summary["device_id"] == "D001"].iloc[0]
    assert d001["total_distance_km"] == pytest.approx(1.5)
    assert d001["gps_points"] == 2
    assert d001["abnormal_speed_count"] == 0