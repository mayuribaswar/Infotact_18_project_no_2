import pandas as pd
from pathlib import Path


INPUT_FILE = Path("data/snowflake/gps_data.csv")
OUTPUT_FILE = Path("data/snowflake/gps_data_prepared.csv")


def prepare_gps_data():
    print("Loading GPS data...")

    df = pd.read_csv(INPUT_FILE)

    print(f"Initial rows: {len(df)}")

    # Remove duplicate records
    df = df.drop_duplicates()

    # Convert timestamp
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    # Remove invalid latitude/longitude
    df = df[
        df["latitude"].between(-90, 90)
        & df["longitude"].between(-180, 180)
    ]

    # Remove invalid speed values
    df = df[df["speed_kmh"] >= 0]

    # Remove invalid accuracy values
    df = df[df["accuracy_m"] > 0]

    # Sort records
    df = df.sort_values(["user_id", "timestamp"])

    # Reset index
    df = df.reset_index(drop=True)

    # Save prepared dataset
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_FILE, index=False)

    print(f"Prepared rows: {len(df)}")
    print(f"Saved file: {OUTPUT_FILE}")

    print("\nData preview:")
    print(df.head())

    print("\nValidation summary:")
    print(df.isnull().sum())


if __name__ == "__main__":
    prepare_gps_data()