from pathlib import Path
import pandas as pd


DATA_FILE = Path("data/snowflake/gps_data_prepared.csv")
SQL_FILE = Path("data/snowflake/load_gps_data.sql")


def generate_load_sql():
    print("Preparing Snowflake ingestion SQL...")

    if not DATA_FILE.exists():
        print("Prepared GPS file not found.")
        print("Run prepare_gps_data.py first.")
        return

    df = pd.read_csv(DATA_FILE)

    print(f"Records ready for ingestion: {len(df)}")

    sql = """
USE DATABASE GEOPULSE;
USE SCHEMA RAW;

CREATE TABLE IF NOT EXISTS GPS_DATA (
    GPS_ID INTEGER,
    USER_ID VARCHAR(50),
    LATITUDE FLOAT,
    LONGITUDE FLOAT,
    TIMESTAMP TIMESTAMP_NTZ,
    SPEED_KMH FLOAT,
    ACCURACY_M FLOAT
);

"""

    for _, row in df.iterrows():
        sql += f"""INSERT INTO GPS_DATA
(GPS_ID, USER_ID, LATITUDE, LONGITUDE, TIMESTAMP, SPEED_KMH, ACCURACY_M)
VALUES (
    {int(row['gps_id'])},
    '{row['user_id']}',
    {row['latitude']},
    {row['longitude']},
    '{row['timestamp']}',
    {row['speed_kmh']},
    {row['accuracy_m']}
);

"""

    SQL_FILE.write_text(sql, encoding="utf-8")

    print(f"SQL file created: {SQL_FILE}")
    print("GPS data is ready for Snowflake ingestion.")


if __name__ == "__main__":
    generate_load_sql()