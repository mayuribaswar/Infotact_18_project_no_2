"""
Geographic boundary configuration for GeoPulse.

This module contains the prototype geographic boundary
used to validate GPS coordinates.
"""

MIN_LATITUDE = 19.98
MAX_LATITUDE = 20.02

MIN_LONGITUDE = 73.77
MAX_LONGITUDE = 73.81


def is_inside_boundary(latitude, longitude):
    """
    Check whether a GPS coordinate is inside
    the configured geographic boundary.

    Parameters
    ----------
    latitude : float
        GPS latitude.

    longitude : float
        GPS longitude.

    Returns
    -------
    bool
        True if the point is inside the boundary,
        otherwise False.
    """

    if latitude is None or longitude is None:
        return False

    return (
        MIN_LATITUDE <= latitude <= MAX_LATITUDE
        and
        MIN_LONGITUDE <= longitude <= MAX_LONGITUDE
    )