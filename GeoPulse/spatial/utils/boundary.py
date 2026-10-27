"""
Geographic boundary configuration and point-in-polygon utilities for GeoPulse.
"""

import json
from pathlib import Path
from typing import Optional
from shapely.geometry import shape, Point

# Bounding box prototype limits
MIN_LATITUDE = 19.98
MAX_LATITUDE = 20.02
MIN_LONGITUDE = 73.77
MAX_LONGITUDE = 73.81


def is_inside_boundary(latitude: Optional[float], longitude: Optional[float]) -> bool:
    """Check whether coordinates fall inside the configured bounding box."""
    if latitude is None or longitude is None:
        return False
    return (
        MIN_LATITUDE <= latitude <= MAX_LATITUDE
        and MIN_LONGITUDE <= longitude <= MAX_LONGITUDE
    )


def is_inside_geojson_polygon(latitude: float, longitude: float, geojson_path: Path) -> bool:
    """Check whether coordinates fall inside a GeoJSON polygon boundary."""
    if latitude is None or longitude is None or not geojson_path.exists():
        return False

    with open(geojson_path, "r", encoding="utf-8") as f:
        geo_data = json.load(f)

    # Longitude is X, Latitude is Y
    pt = Point(longitude, latitude)
    for feature in geo_data.get("features", []):
        poly = shape(feature["geometry"])
        if poly.contains(pt):
            return True
    return False