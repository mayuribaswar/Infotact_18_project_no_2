from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# GeoPulse - Day 8: Spatial Hotspot Visualization
# ============================================================

BASE_DIR = Path(__file__).resolve().parents[2]

DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = DATA_DIR / "output"

INPUT_FILE = OUTPUT_DIR / "hotspot_results.csv"
CSV_OUTPUT = OUTPUT_DIR / "hotspot_visualized.csv"
IMAGE_OUTPUT = OUTPUT_DIR / "hotspot_map.png"


REQUIRED_COLUMNS = {
    "grid_id",
    "point_count",
    "unique_devices",
    "avg_points_per_device",
    "density",
}


def load_hotspot_data():
    print("[1] Loading Day 7 hotspot results...")

    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Day 7 output file not found: {INPUT_FILE}\n"
            "Run Day 7 first."
        )

    df = pd.read_csv(INPUT_FILE)

    print("Hotspot data loaded successfully.")
    print(f"Records: {len(df)}")

    return df


def validate_data(df):
    print("\n[2] Validating hotspot data...")

    missing_columns = REQUIRED_COLUMNS - set(df.columns)

    if missing_columns:
        raise ValueError(
            f"Missing columns: {sorted(missing_columns)}"
        )

    if df.empty:
        raise ValueError(
            "Hotspot data is empty."
        )

    print("Required columns are present.")

    print("\nInput data:")
    print(df)


def add_coordinates(df):
    print("\n[3] Extracting grid coordinates...")

    # grid_id format:
    # 19998_73790

    grid_values = df["grid_id"].astype(str).str.split(
        "_",
        expand=True
    )

    df["grid_lat"] = grid_values[0].astype(float)
    df["grid_lon"] = grid_values[1].astype(float)

    # Convert grid values back to approximate coordinates.
    df["latitude"] = df["grid_lat"] / 1000
    df["longitude"] = df["grid_lon"] / 1000

    return df


def create_visualization(df):
    print("\n[4] Creating hotspot visualization...")

    plt.figure(figsize=(10, 7))

    for classification in ["LOW", "MEDIUM", "HIGH"]:

        subset = df[
            df["density"] == classification
        ]

        if not subset.empty:
            plt.scatter(
                subset["longitude"],
                subset["latitude"],
                label=classification,
                s=100,
                alpha=0.7
            )

    plt.xlabel("Longitude")
    plt.ylabel("Latitude")

    plt.title(
        "GeoPulse Spatial Hotspot Visualization"
    )

    plt.legend()

    plt.grid(True)

    plt.tight_layout()

    plt.savefig(
        IMAGE_OUTPUT,
        dpi=150
    )

    plt.close()

    print(
        f"Visualization saved to: {IMAGE_OUTPUT}"
    )


def save_visualized_data(df):
    print("\n[5] Saving visualization data...")

    output_columns = [
        "latitude",
        "longitude",
        "grid_id",
        "point_count",
        "unique_devices",
        "avg_points_per_device",
        "density",
    ]

    result = df[output_columns]

    result.to_csv(
        CSV_OUTPUT,
        index=False
    )

    print(
        f"CSV saved to: {CSV_OUTPUT}"
    )


def main():

    print("=" * 70)
    print("GeoPulse - Day 8: Spatial Hotspot Visualization")
    print("=" * 70)

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    df = load_hotspot_data()

    validate_data(df)

    df = add_coordinates(df)

    create_visualization(df)

    save_visualized_data(df)

    print("\n" + "=" * 70)
    print("Day 8 Spatial Visualization completed successfully!")
    print("=" * 70)


if __name__ == "__main__":
    main()