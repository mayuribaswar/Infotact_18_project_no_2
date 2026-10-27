"""
GeoPulse - Day 12
Hotspot Reporting and Summary Module

This module reads hotspot analysis results, validates the data,
calculates hotspot statistics, classifies hotspots, and generates
a final summary CSV report.
"""

from pathlib import Path
import sys

import pandas as pd


# -------------------------------------------------------------------
# Project paths
# -------------------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_FILE = PROJECT_ROOT / "data" / "processed" / "hotspot_results.csv"
OUTPUT_FILE = PROJECT_ROOT / "data" / "processed" / "hotspot_summary.csv"


# -------------------------------------------------------------------
# Logging helper
# -------------------------------------------------------------------

def log(message: str) -> None:
    """Display a formatted log message."""
    print(f"[GeoPulse] {message}")


# -------------------------------------------------------------------
# Load hotspot data
# -------------------------------------------------------------------

def load_hotspot_data(file_path: Path) -> pd.DataFrame:
    """Load hotspot results from CSV."""

    log(f"Loading hotspot data from: {file_path}")

    if not file_path.exists():
        raise FileNotFoundError(
            f"Hotspot results file not found: {file_path}"
        )

    df = pd.read_csv(file_path)

    if df.empty:
        raise ValueError("Hotspot results file is empty.")

    log(f"Loaded {len(df)} hotspot records.")

    return df


# -------------------------------------------------------------------
# Column detection
# -------------------------------------------------------------------

def find_column(df: pd.DataFrame, possible_names: list[str]) -> str | None:
    """
    Find a column using several possible column names.

    This makes the reporting module more flexible if the
    hotspot analysis output uses slightly different names.
    """

    normalized = {
        column.lower().strip().replace(" ", "_"): column
        for column in df.columns
    }

    for name in possible_names:
        key = name.lower().strip().replace(" ", "_")

        if key in normalized:
            return normalized[key]

    return None


# -------------------------------------------------------------------
# Validate hotspot data
# -------------------------------------------------------------------

def validate_hotspot_data(df: pd.DataFrame) -> None:
    """Validate required hotspot information."""

    log("Validating hotspot columns...")

    if len(df.columns) == 0:
        raise ValueError("No columns found in hotspot results.")

    log(f"Available columns: {list(df.columns)}")


# -------------------------------------------------------------------
# Normalize risk level
# -------------------------------------------------------------------

def normalize_risk_level(value) -> str:
    """
    Convert different possible risk representations into:
    HIGH, MEDIUM, or LOW.
    """

    if pd.isna(value):
        return "LOW"

    text = str(value).strip().upper()

    if text in {"HIGH", "H", "3", "HIGH RISK"}:
        return "HIGH"

    if text in {"MEDIUM", "MED", "M", "2", "MEDIUM RISK"}:
        return "MEDIUM"

    if text in {"LOW", "L", "1", "LOW RISK"}:
        return "LOW"

    return "LOW"


# -------------------------------------------------------------------
# Classify hotspots
# -------------------------------------------------------------------

def classify_hotspots(df: pd.DataFrame) -> pd.DataFrame:
    """Add a standardized risk level column."""

    log("Classifying hotspots...")

    risk_column = find_column(
        df,
        [
            "risk_level",
            "risk",
            "risk_category",
            "severity",
            "classification",
        ],
    )

    if risk_column:
        df["risk_level"] = df[risk_column].apply(normalize_risk_level)

    else:
        score_column = find_column(
            df,
            [
                "hotspot_score",
                "score",
                "hotspot_score_value",
                "density",
            ],
        )

        if score_column:
            scores = pd.to_numeric(
                df[score_column],
                errors="coerce"
            ).fillna(0)

            high_threshold = scores.quantile(0.75)
            medium_threshold = scores.quantile(0.40)

            def classify(score):
                if score >= high_threshold:
                    return "HIGH"

                if score >= medium_threshold:
                    return "MEDIUM"

                return "LOW"

            df["risk_level"] = scores.apply(classify)

        else:
            df["risk_level"] = "LOW"

    return df


# -------------------------------------------------------------------
# Calculate hotspot score
# -------------------------------------------------------------------

def calculate_hotspot_score(df: pd.DataFrame) -> pd.DataFrame:
    """
    Ensure a hotspot_score column exists.
    """

    score_column = find_column(
        df,
        [
            "hotspot_score",
            "score",
            "hotspot_score_value",
        ],
    )

    if score_column:
        df["hotspot_score"] = pd.to_numeric(
            df[score_column],
            errors="coerce"
        ).fillna(0)

    else:
        event_column = find_column(
            df,
            [
                "event_count",
                "events",
                "count",
                "point_count",
                "num_events",
            ],
        )

        if event_column:
            df["hotspot_score"] = pd.to_numeric(
                df[event_column],
                errors="coerce"
            ).fillna(0)

        else:
            df["hotspot_score"] = 0

    return df


# -------------------------------------------------------------------
# Calculate event count
# -------------------------------------------------------------------

def calculate_event_count(df: pd.DataFrame) -> pd.DataFrame:
    """Ensure event_count column exists."""

    event_column = find_column(
        df,
        [
            "event_count",
            "events",
            "count",
            "point_count",
            "num_events",
        ],
    )

    if event_column:
        df["event_count"] = pd.to_numeric(
            df[event_column],
            errors="coerce"
        ).fillna(0)

    else:
        df["event_count"] = 0

    return df


# -------------------------------------------------------------------
# Create hotspot summary
# -------------------------------------------------------------------

def create_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Create the final standardized hotspot summary."""

    log("Creating hotspot summary...")

    df = calculate_event_count(df)
    df = calculate_hotspot_score(df)
    df = classify_hotspots(df)

    summary_columns = []

    # Grid ID
    grid_column = find_column(
        df,
        [
            "grid_id",
            "grid",
            "cell_id",
            "spatial_grid",
        ],
    )

    if grid_column:
        df["grid_id"] = df[grid_column].astype(str)
        summary_columns.append("grid_id")

    # Coordinates
    latitude_column = find_column(
        df,
        [
            "latitude",
            "lat",
            "center_latitude",
            "grid_lat",
        ],
    )

    longitude_column = find_column(
        df,
        [
            "longitude",
            "lon",
            "lng",
            "center_longitude",
            "grid_longitude",
        ],
    )

    if latitude_column:
        df["latitude"] = pd.to_numeric(
            df[latitude_column],
            errors="coerce"
        )
        summary_columns.append("latitude")

    if longitude_column:
        df["longitude"] = pd.to_numeric(
            df[longitude_column],
            errors="coerce"
        )
        summary_columns.append("longitude")

    summary_columns.extend(
        [
            "risk_level",
            "event_count",
            "hotspot_score",
        ]
    )

    summary = df[summary_columns].copy()

    summary = summary.sort_values(
        by="hotspot_score",
        ascending=False
    )

    summary = summary.reset_index(drop=True)

    return summary


# -------------------------------------------------------------------
# Generate statistics
# -------------------------------------------------------------------

def generate_statistics(df: pd.DataFrame) -> dict:
    """Generate overall hotspot statistics."""

    total_hotspots = len(df)

    high_count = int(
        (df["risk_level"] == "HIGH").sum()
    )

    medium_count = int(
        (df["risk_level"] == "MEDIUM").sum()
    )

    low_count = int(
        (df["risk_level"] == "LOW").sum()
    )

    total_events = float(
        df["event_count"].sum()
    )

    average_score = float(
        df["hotspot_score"].mean()
    ) if total_hotspots else 0.0

    maximum_score = float(
        df["hotspot_score"].max()
    ) if total_hotspots else 0.0

    return {
        "total_hotspots": total_hotspots,
        "high_risk_hotspots": high_count,
        "medium_risk_hotspots": medium_count,
        "low_risk_hotspots": low_count,
        "total_events": total_events,
        "average_hotspot_score": round(
            average_score,
            2
        ),
        "maximum_hotspot_score": round(
            maximum_score,
            2
        ),
    }


# -------------------------------------------------------------------
# Print statistics
# -------------------------------------------------------------------

def print_statistics(statistics: dict) -> None:
    """Print hotspot statistics."""

    print()
    print("=" * 60)
    print("GeoPulse - Day 12 Hotspot Statistics")
    print("=" * 60)

    print(
        f"Total hotspots          : "
        f"{statistics['total_hotspots']}"
    )

    print(
        f"High-risk hotspots      : "
        f"{statistics['high_risk_hotspots']}"
    )

    print(
        f"Medium-risk hotspots    : "
        f"{statistics['medium_risk_hotspots']}"
    )

    print(
        f"Low-risk hotspots       : "
        f"{statistics['low_risk_hotspots']}"
    )

    print(
        f"Total events            : "
        f"{statistics['total_events']}"
    )

    print(
        f"Average hotspot score   : "
        f"{statistics['average_hotspot_score']}"
    )

    print(
        f"Maximum hotspot score   : "
        f"{statistics['maximum_hotspot_score']}"
    )

    print("=" * 60)


# -------------------------------------------------------------------
# Save report
# -------------------------------------------------------------------

def save_report(
    summary: pd.DataFrame,
    output_path: Path
) -> None:
    """Save final hotspot summary CSV."""

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    summary.to_csv(
        output_path,
        index=False
    )

    log(f"Final report saved to: {output_path}")


# -------------------------------------------------------------------
# Main
# -------------------------------------------------------------------

def main() -> int:

    print("=" * 70)
    print("GeoPulse - Day 12: Hotspot Reporting")
    print("=" * 70)

    try:
        # Step 1
        df = load_hotspot_data(INPUT_FILE)

        # Step 2
        validate_hotspot_data(df)

        # Step 3
        summary = create_summary(df)

        # Step 4
        statistics = generate_statistics(summary)

        # Step 5
        print_statistics(statistics)

        # Step 6
        save_report(summary, OUTPUT_FILE)

        print()
        print("Day 12 completed successfully.")
        print("Hotspot summary report generated.")
        print("=" * 70)

        return 0

    except FileNotFoundError as error:
        print(f"\nERROR: {error}")
        return 1

    except ValueError as error:
        print(f"\nERROR: {error}")
        return 1

    except Exception as error:
        print(f"\nUNEXPECTED ERROR: {error}")
        return 1


if __name__ == "__main__":
    sys.exit(main())