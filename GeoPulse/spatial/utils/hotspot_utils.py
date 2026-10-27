def validate_latitude(latitude):
    """
    Check whether latitude is valid.

    Valid latitude:
        -90 to +90
    """

    if latitude is None:
        return False

    return -90 <= latitude <= 90


def validate_longitude(longitude):
    """
    Check whether longitude is valid.

    Valid longitude:
        -180 to +180
    """

    if longitude is None:
        return False

    return -180 <= longitude <= 180


def create_grid_id(latitude, longitude, grid_size=1000):
    """
    Create a deterministic grid ID from latitude and longitude.
    """

    if not validate_latitude(latitude):
        raise ValueError("Invalid latitude")

    if not validate_longitude(longitude):
        raise ValueError("Invalid longitude")

    grid_lat = int(latitude * grid_size)
    grid_lon = int(longitude * grid_size)

    return f"G_{grid_lat}_{grid_lon}"


def classify_density(point_count, max_count):
    """
    Classify point density.

    HIGH:
        >= 66% of maximum

    MEDIUM:
        >= 33% of maximum

    LOW:
        below 33%
    """

    if point_count < 0:
        raise ValueError("Point count cannot be negative")

    if max_count <= 0:
        return "LOW"

    if point_count >= max_count * 0.66:
        return "HIGH"

    if point_count >= max_count * 0.33:
        return "MEDIUM"

    return "LOW"