"""
GeoPulse - Day 4: GPS Movement and Trajectory Analysis

Reads validated GPS records, calculates distance and velocity between consecutive
points, classifies motion, and generates per-device summary metrics.
"""

from pathlib import Path
import math
from typing import Optional
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[2]
INPUT_FILE = PROJECT_ROOT / "data" / "cleaned_gps.csv"
OUTPUT_FILE = PROJECT_ROOT / "data" / "movement_analysis.csv"


def haversine_distance(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Calculate distance between two GPS coordinates in kilometers."""
    earth_radius_km = 6371.0

    lat1_rad, lon1_rad = math.radians(float(lat1)), math.radians(float(lon1))
    lat2_rad, lon2_rad = math.radians(float(lat2)), math.radians(float(lon2))

    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    a = math.sin(dlat / 2.0) ** 2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2.0) ** 2
    c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))
    return earth_radius_km * c


def classify_movement(speed_kmh: Optional[float]) -> str:
    """Classify movement based on calculated speed in km/h."""
    if pd.isna(speed_kmh):
        return "UNKNOWN"
    if speed_kmh < 3.0:
        return "STATIONARY"
    elif speed_kmh <= 40.0:
        return "MOVING"
    return "FAST_MOVING"


def is_abnormal_speed(speed_kmh: Optional[float], max_speed_kmh: float = 120.0) -> bool:
    """Determine whether recorded speed exceeds acceptable velocity thresholds."""
    if pd.isna(speed_kmh):
        return False
    return speed_kmh > max_speed_kmh


def analyze_movement(df: pd.DataFrame) -> pd.DataFrame:
    """Calculate point-to-point distance, delta-time, speed, and cumulative distance."""
    df = df.copy()
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df = df.sort_values(by=["device_id", "timestamp"]).reset_index(drop=True)

    df["prev_lat"] = df.groupby("device_id")["latitude"].shift(1)
    df["prev_lon"] = df.groupby("device_id")["longitude"].shift(1)
    df["prev_time"] = df.groupby("device_id")["timestamp"].shift(1)

    distances = []
    time_diff_seconds = []
    speeds = []

    for _, row in df.iterrows():
        if pd.isna(row["prev_lat"]) or pd.isna(row["prev_time"]):
            distances.append(0.0)
            time_diff_seconds.append(None)
            speeds.append(0.0)
        else:
            dist = haversine_distance(row["prev_lat"], row["prev_lon"], row["latitude"], row["longitude"])
            t_diff = (row["timestamp"] - row["prev_time"]).total_seconds()
            speed = (dist / (t_diff / 3600.0)) if t_diff > 0 else 0.0

            distances.append(round(dist, 4))
            time_diff_seconds.append(t_diff)
            speeds.append(round(speed, 2))

    df["time_difference_seconds"] = time_diff_seconds
    df["time_difference_minutes"] = [
        round(t / 60.0, 2) if t is not None else None for t in time_diff_seconds
    ]
    df["distance_km"] = distances
    df["speed_kmh"] = speeds
    df["movement_status"] = df["speed_kmh"].apply(classify_movement)
    df["abnormal_speed"] = df["speed_kmh"].apply(is_abnormal_speed)
    df["cumulative_distance_km"] = df.groupby("device_id")["distance_km"].cumsum().round(4)

    return df.drop(columns=["prev_lat", "prev_lon", "prev_time"])


def create_device_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Create per-device movement aggregate summary."""
    summary = df.groupby("device_id").agg(
        gps_points=("device_id", "count"),
        total_distance_km=("distance_km", "sum"),
        avg_speed_kmh=("speed_kmh", "mean"),
        max_speed_kmh=("speed_kmh", "max"),
        abnormal_speed_count=("abnormal_speed", "sum"),
    ).reset_index()

    summary["total_distance_km"] = summary["total_distance_km"].round(4)
    summary["avg_speed_kmh"] = summary["avg_speed_kmh"].round(2)
    return summary


def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(f"Input file not found at: {INPUT_FILE}")

    raw_df = pd.read_csv(INPUT_FILE)
    movement_df = analyze_movement(raw_df)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    movement_df.to_csv(OUTPUT_FILE, index=False)

    print("=" * 60)
    print("GeoPulse - Day 4 Trajectory Processing Complete")
    print("=" * 60)
    print(f"Saved: {OUTPUT_FILE} ({len(movement_df)} records)")

    summary = create_device_summary(movement_df)
    print("\nDevice Summary:")
    print(summary.to_string(index=False))


if __name__ == "__main__":
    main()