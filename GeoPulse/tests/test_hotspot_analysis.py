import pytest

from spatial.utils.hotspot_utils import (
    validate_latitude,
    validate_longitude,
    create_grid_id,
    classify_density
)


def test_valid_latitude():
    assert validate_latitude(19.9975) is True


def test_invalid_latitude():
    assert validate_latitude(100) is False


def test_valid_longitude():
    assert validate_longitude(73.7898) is True


def test_invalid_longitude():
    assert validate_longitude(200) is False


def test_grid_id_creation():
    grid_id = create_grid_id(
        19.9975,
        73.7898
    )

    assert grid_id.startswith("G_")


def test_high_density():
    result = classify_density(
        point_count=100,
        max_count=100
    )

    assert result == "HIGH"


def test_medium_density():
    result = classify_density(
        point_count=50,
        max_count=100
    )

    assert result == "MEDIUM"


def test_low_density():
    result = classify_density(
        point_count=10,
        max_count=100
    )

    assert result == "LOW"


def test_zero_max_count():
    result = classify_density(
        point_count=10,
        max_count=0
    )

    assert result == "LOW"


def test_negative_point_count():
    with pytest.raises(ValueError):
        classify_density(
            point_count=-1,
            max_count=100
        )