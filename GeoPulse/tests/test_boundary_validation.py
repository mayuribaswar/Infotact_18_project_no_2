import csv
import json
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]

# Dynamically locate files whether placed in data/ or spatial/data/
DATA_FILE = (
    ROOT_DIR / "data" / "gaps.csv"
    if (ROOT_DIR / "data" / "gaps.csv").exists()
    else ROOT_DIR / "spatial" / "data" / "gaps.csv"
)

BOUNDARY_FILE = (
    ROOT_DIR / "data" / "city_boundary.geojson"
    if (ROOT_DIR / "data" / "city_boundary.geojson").exists()
    else ROOT_DIR / "spatial" / "data" / "city_boundary.geojson"
)


def load_gaps():
    with open(DATA_FILE, "r", encoding="utf-8-sig", newline="") as file:
        return list(csv.DictReader(file))


def test_input_files_exist():
    assert DATA_FILE.exists(), f"gaps.csv not found at {DATA_FILE}"
    assert BOUNDARY_FILE.exists(), f"city_boundary.geojson not found at {BOUNDARY_FILE}"


def test_gaps_csv_has_required_columns():
    rows = load_gaps()
    assert len(rows) > 0
    required_columns = {
        "gap_id",
        "location_name",
        "latitude",
        "longitude",
        "gap_type",
        "severity",
    }
    assert required_columns.issubset(rows[0].keys())


def test_gaps_csv_not_empty():
    assert len(load_gaps()) > 0


def test_coordinates_are_valid():
    for row in load_gaps():
        lat = float(row["latitude"])
        lon = float(row["longitude"])
        assert -90.0 <= lat <= 90.0
        assert -180.0 <= lon <= 180.0


def test_gap_ids_are_unique():
    rows = load_gaps()
    gap_ids = [row["gap_id"] for row in rows]
    assert len(gap_ids) == len(set(gap_ids))


def test_expected_test_points_exist():
    rows = load_gaps()
    gap_ids = {row["gap_id"] for row in rows}
    assert "G015" in gap_ids
    assert "G016" in gap_ids


def test_boundary_geojson_is_valid():
    with open(BOUNDARY_FILE, "r", encoding="utf-8") as file:
        boundary = json.load(file)
    assert boundary["type"] == "FeatureCollection"
    assert len(boundary["features"]) > 0