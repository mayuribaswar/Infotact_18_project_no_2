"""
GeoPulse - Day 9
Spatial Data Quality Validation

Purpose:
1. Automatically locate GPS input CSV files.
2. Validate latitude and longitude.
3. Validate timestamps.
4. Detect missing values.
5. Detect duplicate records.
6. Generate validation summary.
7. Save validated data and summary.

Technology:
- Python
- PySpark
- Apache Spark
"""

from pathlib import Path
from pyspark.sql import SparkSession
from pyspark.sql import functions as F


# ============================================================
# PROJECT PATHS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"

OUTPUT_DIR = DATA_DIR / "output" / "day9_validation"


# ============================================================
# SPARK SESSION
# ============================================================

def create_spark():
    """
    Create and configure Spark session.
    """

    return (
        SparkSession.builder
        .appName("GeoPulse-Day9-Spatial-Validation")
        .master("local[*]")
        .getOrCreate()
    )


# ============================================================
# FIND GPS INPUT FILE
# ============================================================

def find_gps_file():
    """
    Search the data directory recursively for CSV files.

    This avoids depending on one fixed file name such as
    data/gps/gps_data.csv.
    """

    if not DATA_DIR.exists():
        raise FileNotFoundError(
            f"Data directory not found: {DATA_DIR}"
        )

    csv_files = list(DATA_DIR.rglob("*.csv"))

    if not csv_files:
        raise FileNotFoundError(
            f"No CSV files found inside: {DATA_DIR}"
        )

    print("\nAvailable CSV files:")

    for index, file in enumerate(csv_files, start=1):
        print(f"[{index}] {file}")

    # Prefer files whose names indicate GPS/location data
    preferred_files = [
        file for file in csv_files
        if any(
            keyword in file.name.lower()
            for keyword in [
                "gps",
                "location",
                "mobility",
                "ping",
                "movement",
                "device"
            ]
        )
    ]

    if preferred_files:
        selected_file = preferred_files[0]
    else:
        selected_file = csv_files[0]

    print(f"\nSelected GPS input file:")
    print(selected_file)

    return selected_file


# ============================================================
# LOAD DATA
# ============================================================

def load_data(spark):
    """
    Load GPS CSV data into Spark DataFrame.
    """

    input_file = find_gps_file()

    df = (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .option("mode", "PERMISSIVE")
        .csv(str(input_file))
    )

    return df, input_file


# ============================================================
# FIND COLUMN
# ============================================================

def find_column(df, possible_names):
    """
    Find a column from a list of possible column names.
    Matching is case-insensitive.
    """

    columns_lower = {
        column.lower(): column
        for column in df.columns
    }

    for name in possible_names:

        if name.lower() in columns_lower:
            return columns_lower[name.lower()]

    return None


# ============================================================
# VALIDATE COORDINATES
# ============================================================

def validate_coordinates(df):
    """
    Validate latitude and longitude values.
    """

    latitude_column = find_column(
        df,
        [
            "latitude",
            "lat",
            "Latitude",
            "LAT"
        ]
    )

    longitude_column = find_column(
        df,
        [
            "longitude",
            "lon",
            "lng",
            "Longitude",
            "LONG",
            "LON"
        ]
    )

    print("\nCoordinate columns:")

    print(f"Latitude : {latitude_column}")
    print(f"Longitude: {longitude_column}")

    if latitude_column is None or longitude_column is None:

        print(
            "\nLatitude/Longitude columns were not found."
        )

        return (
            df
            .withColumn(
                "coordinate_status",
                F.lit("COLUMN_NOT_FOUND")
            )
        )

    df = df.withColumn(
        "latitude_numeric",
        F.col(latitude_column).cast("double")
    )

    df = df.withColumn(
        "longitude_numeric",
        F.col(longitude_column).cast("double")
    )

    df = df.withColumn(
        "coordinate_status",
        F.when(
            F.col("latitude_numeric").isNull()
            | F.col("longitude_numeric").isNull(),
            "INVALID_MISSING"
        )
        .when(
            (F.col("latitude_numeric") < -90)
            | (F.col("latitude_numeric") > 90)
            | (F.col("longitude_numeric") < -180)
            | (F.col("longitude_numeric") > 180),
            "INVALID_RANGE"
        )
        .otherwise("VALID")
    )

    return df


# ============================================================
# VALIDATE TIMESTAMP
# ============================================================

def validate_timestamp(df):
    """
    Detect and validate timestamp column.
    """

    timestamp_column = find_column(
        df,
        [
            "timestamp",
            "Timestamp",
            "datetime",
            "DateTime",
            "event_timestamp",
            "event_time",
            "time",
            "date_time"
        ]
    )

    print("\nTimestamp column:")

    print(timestamp_column)

    if timestamp_column is None:

        return df.withColumn(
            "timestamp_status",
            F.lit("COLUMN_NOT_FOUND")
        )

    df = df.withColumn(
        "parsed_timestamp",
        F.to_timestamp(
            F.col(timestamp_column)
        )
    )

    df = df.withColumn(
        "timestamp_status",
        F.when(
            F.col("parsed_timestamp").isNull(),
            "INVALID"
        )
        .otherwise("VALID")
    )

    return df


# ============================================================
# DATA QUALITY SUMMARY
# ============================================================

def create_quality_summary(df):
    """
    Generate overall data-quality statistics.
    """

    total_records = df.count()

    valid_coordinates = (
        df.filter(
            F.col("coordinate_status") == "VALID"
        ).count()
    )

    invalid_coordinates = (
        df.filter(
            F.col("coordinate_status") != "VALID"
        ).count()
    )

    valid_timestamps = (
        df.filter(
            F.col("timestamp_status") == "VALID"
        ).count()
    )

    invalid_timestamps = (
        df.filter(
            F.col("timestamp_status") == "INVALID"
        ).count()
    )

    summary_data = [
        (
            total_records,
            valid_coordinates,
            invalid_coordinates,
            valid_timestamps,
            invalid_timestamps
        )
    ]

    summary = df.sparkSession.createDataFrame(
        summary_data,
        [
            "total_records",
            "valid_coordinates",
            "invalid_coordinates",
            "valid_timestamps",
            "invalid_timestamps"
        ]
    )

    return summary


# ============================================================
# DUPLICATE ANALYSIS
# ============================================================

def analyze_duplicates(df):
    """
    Detect duplicate records.

    If DeviceID exists, analyze repeated device records.
    Otherwise, check complete-row duplicates.
    """

    device_column = find_column(
        df,
        [
            "DeviceID",
            "device_id",
            "deviceid",
            "Device_Id"
        ]
    )

    if device_column:

        print(
            f"\nDuplicate analysis using: {device_column}"
        )

        duplicates = (
            df.groupBy(device_column)
            .count()
            .filter(F.col("count") > 1)
            .orderBy(F.desc("count"))
        )

    else:

        print(
            "\nDeviceID column not found."
        )

        print(
            "Checking duplicate complete records..."
        )

        duplicates = (
            df.groupBy(df.columns)
            .count()
            .filter(F.col("count") > 1)
            .orderBy(F.desc("count"))
        )

    return duplicates


# ============================================================
# NULL ANALYSIS
# ============================================================

def analyze_nulls(df):
    """
    Calculate NULL count for every column.
    """

    expressions = []

    for column in df.columns:

        expressions.append(
            F.sum(
                F.when(
                    F.col(column).isNull(),
                    1
                ).otherwise(0)
            ).alias(column)
        )

    return df.agg(*expressions)


# ============================================================
# COORDINATE STATUS REPORT
# ============================================================

def coordinate_report(df):

    print("\nCoordinate Validation Report")
    print("-" * 50)

    (
        df.groupBy("coordinate_status")
        .count()
        .orderBy("coordinate_status")
        .show(
            truncate=False
        )
    )


# ============================================================
# TIMESTAMP STATUS REPORT
# ============================================================

def timestamp_report(df):

    print("\nTimestamp Validation Report")
    print("-" * 50)

    (
        df.groupBy("timestamp_status")
        .count()
        .orderBy("timestamp_status")
        .show(
            truncate=False
        )
    )


# ============================================================
# SHOW DATA INFORMATION
# ============================================================

def show_data_information(df):

    print("\nDataset Schema")
    print("-" * 50)

    df.printSchema()

    print("\nSample Records")
    print("-" * 50)

    df.show(
        10,
        truncate=False
    )


# ============================================================
# SAVE OUTPUT
# ============================================================

def save_outputs(
    df,
    summary,
    null_report,
    duplicates
):

    OUTPUT_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    print("\nSaving Day 9 outputs...")

    # Validated GPS data
    (
        df.write
        .mode("overwrite")
        .option("header", True)
        .csv(
            str(
                OUTPUT_DIR / "validated_gps"
            )
        )
    )

    # Quality summary
    (
        summary.write
        .mode("overwrite")
        .option("header", True)
        .csv(
            str(
                OUTPUT_DIR / "quality_summary"
            )
        )
    )

    # NULL report
    (
        null_report.write
        .mode("overwrite")
        .option("header", True)
        .csv(
            str(
                OUTPUT_DIR / "null_report"
            )
        )
    )

    # Duplicate report
    if duplicates is not None:

        (
            duplicates.write
            .mode("overwrite")
            .option("header", True)
            .csv(
                str(
                    OUTPUT_DIR / "duplicates"
                )
            )
        )

    print(
        f"\nOutputs saved to:\n{OUTPUT_DIR}"
    )


# ============================================================
# MAIN
# ============================================================

def main():

    print("=" * 70)

    print(
        "GeoPulse - Day 9: "
        "Spatial Data Quality Validation"
    )

    print("=" * 70)

    spark = create_spark()

    try:

        # ----------------------------------------------------
        # 1. LOAD DATA
        # ----------------------------------------------------

        print("\n[1] Loading GPS data...")

        df, input_file = load_data(
            spark
        )

        print(
            f"\nInput file:\n{input_file}"
        )

        print(
            f"\nTotal records: {df.count()}"
        )

        print(
            f"Total columns: {len(df.columns)}"
        )

        # ----------------------------------------------------
        # 2. SHOW DATA
        # ----------------------------------------------------

        print(
            "\n[2] Inspecting dataset..."
        )

        show_data_information(
            df
        )

        # ----------------------------------------------------
        # 3. COORDINATE VALIDATION
        # ----------------------------------------------------

        print(
            "\n[3] Validating coordinates..."
        )

        df = validate_coordinates(
            df
        )

        coordinate_report(
            df
        )

        # ----------------------------------------------------
        # 4. TIMESTAMP VALIDATION
        # ----------------------------------------------------

        print(
            "\n[4] Validating timestamps..."
        )

        df = validate_timestamp(
            df
        )

        timestamp_report(
            df
        )

        # ----------------------------------------------------
        # 5. QUALITY SUMMARY
        # ----------------------------------------------------

        print(
            "\n[5] Creating quality summary..."
        )

        summary = create_quality_summary(
            df
        )

        summary.show(
            truncate=False
        )

        # ----------------------------------------------------
        # 6. NULL ANALYSIS
        # ----------------------------------------------------

        print(
            "\n[6] Checking NULL values..."
        )

        null_report = analyze_nulls(
            df
        )

        null_report.show(
            truncate=False
        )

        # ----------------------------------------------------
        # 7. DUPLICATE ANALYSIS
        # ----------------------------------------------------

        print(
            "\n[7] Checking duplicate records..."
        )

        duplicates = analyze_duplicates(
            df
        )

        duplicates.show(
            20,
            truncate=False
        )

        # ----------------------------------------------------
        # 8. SAVE OUTPUTS
        # ----------------------------------------------------

        print(
            "\n[8] Saving validation results..."
        )

        save_outputs(
            df,
            summary,
            null_report,
            duplicates
        )

        # ----------------------------------------------------
        # FINAL RESULT
        # ----------------------------------------------------

        print("\n" + "=" * 70)

        print(
            "DAY 9 SPATIAL VALIDATION COMPLETED SUCCESSFULLY"
        )

        print("=" * 70)

    except Exception as error:

        print(
            "\nDay 9 validation failed."
        )

        print(
            f"Error: {error}"
        )

        raise

    finally:

        spark.stop()

        print(
            "\nSpark stopped."
        )


# ============================================================
# ENTRY POINT
# ============================================================

if __name__ == "__main__":
    main()
