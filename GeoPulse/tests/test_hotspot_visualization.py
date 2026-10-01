from pathlib import Path

import pandas as pd
import pytest

from spatial.jobs.hotspot_visualization import (
    REQUIRED_COLUMNS,
    classify_hotspot,
)


def test_required_columns():
    columns = {
        "latitude",
        "longitude",
        "grid_id",
        "point_count",
        "density",
    }

    assert REQUIRED_COLUMNS == columns


def test_high_classification():
    result = classify_hotspot(90, 30, 70)
    assert result == "HIGH"


def test_medium_classification():
    result = classify_hotspot(50, 30, 70)
    assert result == "MEDIUM"


def test_low_classification():
    result = classify_hotspot(10, 30, 70)
    assert result == "LOW"


def test_classification_values():
    valid_values = {"LOW", "MEDIUM", "HIGH"}

    sample = pd.DataFrame({
        "density": [10, 50, 90]
    })

    low = sample["density"].quantile(0.33)
    high = sample["density"].quantile(0.66)

    classifications = sample["density"].apply(
        lambda value: classify_hotspot(
            value,
            low,
            high
        )
    )

    assert set(classifications).issubset(valid_values)


def test_latitude_longitude_range():
    df = pd.DataFrame({
        "latitude": [18.52, 19.07, 20.01],
        "longitude": [73.85, 72.87, 73.78],
    })

    assert df["latitude"].between(-90, 90).all()
    assert df["longitude"].between(-180, 180).all()