# GeoPulse — Spatial Processing Environment

## Day 1 — Setup Spatial Processing Environment

**Member:** Member 2
**Commit:** `feat: setup spatial processing environment`

---

## 1. Objective

Set up the spatial processing environment required for the GeoPulse project.

The environment uses:

* Python
* PySpark
* Apache Spark
* Apache Sedona
* Hadoop/WinUtils for Windows
* GeoTools wrapper

The purpose of this setup is to provide the foundation for processing and analyzing geospatial data in the GeoPulse project.

---

## 2. Day 1 Tasks

The following tasks were completed:

* [x] Create spatial processing directory
* [x] Create `spatial/jobs/`
* [x] Create `spatial/utils/`
* [x] Set up Python environment
* [x] Install and configure PySpark
* [x] Configure Apache Spark
* [x] Configure Hadoop for Windows
* [x] Configure `HADOOP_HOME`
* [x] Configure `hadoop.home.dir`
* [x] Configure `winutils.exe`
* [x] Add Hadoop to PATH
* [x] Install/configure Apache Sedona
* [x] Configure GeoTools wrapper
* [x] Create a Sedona test program
* [x] Verify Spark startup
* [x] Verify Apache Sedona startup
* [x] Verify a spatial geometry operation
* [x] Commit Day 1 implementation to Git

---

## 3. Project Structure

The spatial processing structure is:

```text
GeoPulse/
└── spatial/
    ├── jobs/
    │   └── test_sedona.py
    │
    └── utils/
```

### `spatial/jobs/`

Contains executable Spark/Sedona jobs.

The Day 1 validation program is:

```text
test_sedona.py
```

### `spatial/utils/`

Contains utility modules that will be used by future spatial-processing jobs.

---

## 4. Environment

### Operating System

Windows

### Python

Python 3.12

Python executable:

```text
C:\Users\Shree\AppData\Local\Programs\Python\Python312\python.exe
```

### Apache Spark

```text
Spark 3.5.6
```

### PySpark

```text
PySpark 3.5.6
```

### Apache Sedona

```text
Apache Sedona 1.9.1
```

### GeoTools Wrapper

```text
GeoTools Wrapper 1.9.1-33.5
```

### Hadoop Runtime

The PySpark installation uses Hadoop 3.3.4 runtime libraries.

---

## 5. Windows Hadoop Configuration

Spark on Windows required Hadoop configuration.

The following directory was created:

```text
C:\hadoop\bin
```

The required executable was configured as:

```text
C:\hadoop\bin\winutils.exe
```

Environment variables were configured:

```text
HADOOP_HOME=C:\hadoop
hadoop.home.dir=C:\hadoop
```

The Hadoop binary directory was also added to the PATH:

```text
C:\hadoop\bin
```

This allows Spark to start correctly on Windows.

---

## 6. PySpark Configuration

PySpark was installed and verified.

The Spark environment was tested using:

```powershell
python test_sedona.py
```

Spark successfully started with:

```text
Spark version: 3.5.6
```

---

## 7. Apache Sedona Configuration

Apache Sedona dependencies were successfully resolved.

Dependencies used:

```text
org.apache.sedona#sedona-spark-shaded-3.5_2.12;1.9.1
```

and:

```text
org.datasyslab#geotools-wrapper;1.9.1-33.5
```

The dependencies were successfully retrieved and loaded by Spark.

---

## 8. Sedona Validation

The spatial environment was tested using:

```powershell
cd "C:\Users\Shree\OneDrive\Desktop\Infotact_18_project_no_2\GeoPulse\spatial\jobs"

python test_sedona.py
```

The test successfully produced:

```text
======================================
GeoPulse Spatial Environment READY!
Spark version: 3.5.6
Apache Sedona started successfully!
======================================
```

A spatial point was also successfully processed:

```text
POINT (77.5946 12.9716)
```

This confirms that Spark and Apache Sedona are working together.

---

## 9. Validation Result

The following components were successfully validated:

| Component                   | Status |
| --------------------------- | ------ |
| Python                      | PASS   |
| PySpark                     | PASS   |
| Apache Spark                | PASS   |
| Hadoop configuration        | PASS   |
| WinUtils                    | PASS   |
| Apache Sedona               | PASS   |
| GeoTools wrapper            | PASS   |
| Spatial geometry processing | PASS   |

---

## 10. Warnings

During execution, Spark displayed:

```text
WARN NativeCodeLoader: Unable to load native-hadoop library for your platform...
```

This is a common Windows Spark warning and did not prevent the application from running.

Spark also displayed a temporary-directory cleanup warning involving:

```text
geotools-wrapper-1.9.1-33.5.jar
```

The warning occurred during Spark shutdown after the spatial operation had already completed successfully.

Therefore, these warnings did not affect the Day 1 validation.

---

## 11. Git Commit

The completed Day 1 work was committed using:

```powershell
git add spatial
git commit -m "feat: setup spatial processing environment"
```

Commit message:

```text
feat: setup spatial processing environment
```

To verify the latest commit:

```powershell
git log -1 --oneline
```

---

## 12. Definition of Done

Day 1 is considered complete when:

* Python is available.
* PySpark is installed.
* Spark starts successfully.
* Hadoop/WinUtils is configured.
* Apache Sedona loads successfully.
* GeoTools wrapper loads successfully.
* A spatial geometry operation executes successfully.
* Required `spatial/jobs` and `spatial/utils` directories exist.
* Changes are committed to Git.

All Day 1 requirements have been completed.

---

## 13. Result

**Member 2 — Day 1: COMPLETE**

The GeoPulse project now has a functional Spark + Apache Sedona spatial-processing environment that can be used for the next stages of development.

---

## 14. Next Step

Proceed to:

```text
Member 2 — Day 2
```

The Day 2 implementation should build on this verified spatial-processing environment.

# GeoPulse — Day 2: Spatial GPS Data Schema

## 1. Overview

GeoPulse is a **Hyper-Local Retail Mobility Analytics** project that uses anonymous GPS mobility data to understand customer movement and retail activity.

The Spatial Engineering module is responsible for preparing GPS data for geographic and spatial analysis.

Day 2 focuses on creating a **standardized GPS data schema** that will be used in the later stages of the GeoPulse spatial processing pipeline.

---

## 2. Day 2 Objective

The main objective of Day 2 is to:

* Define a standard GPS data structure.
* Create a PySpark schema for GPS records.
* Prepare sample GPS mobility data.
* Define the coordinate reference system.
* Document GPS fields and data types.
* Establish basic GPS data-quality requirements.
* Prepare the data for future Apache Sedona processing.

---

## 3. Day 2 Scope

### Included in Day 2

* GPS schema definition
* Sample GPS dataset
* Coordinate system documentation
* GPS field definitions
* Data-quality rules
* Schema validation

### Not Included in Day 2

The following tasks will be implemented on later days:

* Spatial geometry creation
* Apache Sedona spatial processing
* Store catchment areas
* 500-meter catchment analysis
* GPS-to-store spatial joins
* Movement arcs
* Spatial aggregation
* Spatial optimization

---

## 4. Folder Structure

```text
spatial/
└── schemas/
    ├── __init__.py
    ├── gps_schema.py
    ├── sample_gps.csv
    └── README.md
```

---

## 5. GPS Data Schema

The GeoPulse GPS dataset contains four primary fields.

| Field       | Data Type | Required | Description                        |
| ----------- | --------- | -------- | ---------------------------------- |
| `device_id` | String    | Yes      | Anonymous mobile device identifier |
| `latitude`  | Double    | Yes      | Geographic latitude                |
| `longitude` | Double    | Yes      | Geographic longitude               |
| `timestamp` | Timestamp | Yes      | Date and time of GPS observation   |

---

## 6. Field Description

### 6.1 device_id

The `device_id` identifies an anonymous mobile device.

Example:

```text
device_001
device_002
device_003
```

The identifier is used to track movement patterns without storing personal identity information.

---

### 6.2 latitude

The `latitude` represents the north-south geographic position of a GPS observation.

Valid geographic range:

```text
-90 to +90
```

Example:

```text
19.9975
```

---

### 6.3 longitude

The `longitude` represents the east-west geographic position of a GPS observation.

Valid geographic range:

```text
-180 to +180
```

Example:

```text
73.7898
```

---

### 6.4 timestamp

The `timestamp` represents the date and time at which the GPS observation was recorded.

Example:

```text
2026-09-24 09:00:00
```

The timestamp will later support:

* Time-based movement analysis
* Hourly footfall analysis
* Visit identification
* Movement sequence analysis
* Temporal aggregation

---

## 7. Coordinate Reference System

The sample GPS coordinates use:

```text
WGS 84
EPSG:4326
```

WGS 84 is a geographic coordinate reference system commonly used for GPS latitude and longitude data.

Example:

```text
Latitude  = 19.9975
Longitude = 73.7898
```

The coordinates are stored as latitude and longitude values at this stage.

---

## 8. PySpark Schema

The schema is implemented using PySpark `StructType` and `StructField`.

```python
from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    DoubleType,
    TimestampType
)

GPS_SCHEMA = StructType([
    StructField("device_id", StringType(), False),
    StructField("latitude", DoubleType(), False),
    StructField("longitude", DoubleType(), False),
    StructField("timestamp", TimestampType(), False)
])
```

The schema ensures that GPS data follows a consistent structure when loaded into PySpark.

---

## 9. Schema Data Types

### StringType

Used for:

```text
device_id
```

Example:

```text
device_001
```

### DoubleType

Used for:

```text
latitude
longitude
```

Example:

```text
19.9975
73.7898
```

### TimestampType

Used for:

```text
timestamp
```

Example:

```text
2026-09-24 09:00:00
```

---

## 10. Required Fields

All four fields are required.

In the PySpark schema, the final parameter is set to `False`:

```python
StructField("device_id", StringType(), False)
```

This means the field is not expected to contain null values.

The same rule applies to:

```text
latitude
longitude
timestamp
```

---

## 11. Sample Dataset

The `sample_gps.csv` file contains sample GPS mobility records.

The dataset contains:

* 10 anonymous devices
* 100 GPS observations
* Multiple timestamps
* Latitude values
* Longitude values
* Different movement paths

Example:

```csv
device_id,latitude,longitude,timestamp
device_001,19.9975,73.7898,2026-09-24 09:00:00
device_001,19.9978,73.7902,2026-09-24 09:05:00
device_001,19.9981,73.7907,2026-09-24 09:10:00
```

The sample data is intended for development and testing.

---

## 12. GPS Data Flow

The GPS data will be processed through the following stages:

```text
Sample / Mock GPS Data
        |
        v
GPS Data Schema
        |
        v
Coordinate Validation
        |
        v
Spatial Point Geometry
        |
        v
Apache Sedona Processing
        |
        v
Spatial Analysis
        |
        v
Retail Mobility Insights
```

Day 2 implements the **GPS Data Schema** stage.

---

## 13. Data Quality Rules

The following basic validation rules are defined for GPS data.

### Latitude Validation

```text
-90 <= latitude <= 90
```

Values outside this range are invalid.

### Longitude Validation

```text
-180 <= longitude <= 180
```

Values outside this range are invalid.

### Device ID Validation

`device_id` should:

* Exist
* Not be null
* Identify an anonymous device

### Timestamp Validation

`timestamp` should:

* Exist
* Not be null
* Contain a valid date and time

---

## 14. Privacy

GeoPulse uses anonymous device identifiers for mobility analysis.

The GPS dataset should not contain personally identifiable information such as:

* Name
* Phone number
* Email address
* Personal address
* Other direct personal identifiers

The `device_id` is intended only for anonymous movement analysis.

---

## 15. Future Spatial Processing

The schema created on Day 2 will be used by the Spatial Engineering module in later tasks.

### Geometry Creation

Latitude and longitude will later be converted into spatial Point geometry.

```text
latitude + longitude
        |
        v
Spatial Point
```

Apache Sedona will be used for spatial operations.

---

### Catchment Analysis

Store locations will later be used to create geographic catchment areas.

A planned analysis will evaluate a **500-meter store catchment**.

The meter-based distance calculation must account for the coordinate system rather than treating latitude/longitude degrees as meters.

---

### Spatial Join

GPS points will later be compared with store catchment geometries to identify GPS observations that fall within store areas.

```text
GPS Points
     +
Store Catchments
     |
     v
Spatial Join
     |
     v
Store-associated GPS observations
```

---

### Movement Analysis

GPS observations will later be ordered by device and timestamp to analyze movement between locations.

---

## 16. Validation

The GPS schema can be tested using:

```powershell
python -c "from spatial.schemas.gps_schema import GPS_SCHEMA; print(GPS_SCHEMA.simpleString())"
```

Expected output:

```text
struct<device_id:string,latitude:double,longitude:double,timestamp:timestamp>
```

---

## 17. Sample Dataset Validation

To check the number of lines in the sample CSV:

```powershell
(Get-Content "spatial\schemas\sample_gps.csv").Count
```

For 100 GPS records plus one header row, the expected result is:

```text
101
```

---

## 18. Day 2 Deliverables

The following files are created:

```text
spatial/schemas/__init__.py
spatial/schemas/gps_schema.py
spatial/schemas/sample_gps.csv
spatial/schemas/README.md
```

---

## 19. Technologies Used

| Technology         | Purpose                           |
| ------------------ | --------------------------------- |
| Python             | Schema implementation             |
| PySpark            | Data schema and processing        |
| CSV                | Sample GPS dataset                |
| WGS 84 / EPSG:4326 | GPS coordinate reference system   |
| Apache Sedona      | Planned future spatial processing |

---

## 20. Git Commit

Day 2 Git commit:

```text
feat: create spatial GPS data schema
```

Push command:

```powershell
git add spatial/schemas
git commit -m "feat: create spatial GPS data schema"
git push origin sakshi
```

---

## 21. Day 2 Completion

### Completed

* [x] Created spatial schema directory
* [x] Created PySpark GPS schema
* [x] Defined GPS fields
* [x] Defined GPS data types
* [x] Created sample GPS dataset
* [x] Added 100 sample GPS records
* [x] Documented WGS 84 / EPSG:4326
* [x] Defined basic data-quality rules
* [x] Added privacy considerations
* [x] Added schema validation
* [x] Documented future spatial processing

### Status

**Day 2 — Completed**

**Team Member:** Member 2 — Spatial Engineering

**Module:** Spatial GPS Data Schema

**Next Task:** Day 3 — Geographic Boundary / Coordinate Validation

# GeoPulse Spatial Jobs

This directory contains PySpark and Apache Sedona jobs used for
processing GPS mobility data.

---

# Day 3 – Geographic Boundary Validation

## Objective

The objective of Day 3 is to validate GPS coordinates before
performing further spatial analytics.

GPS records outside the configured geographic boundary are marked
as invalid.

This validation helps ensure that only GPS points belonging to the
selected geographic area are used in later spatial processing.

---

# Geographic Boundary

The current prototype uses the following geographic bounding box:

```text
Minimum Latitude  = 19.98
Maximum Latitude  = 20.02

Minimum Longitude = 73.77
Maximum Longitude = 73.81
```

A GPS coordinate is considered valid when it satisfies both
latitude and longitude conditions.

```text
19.98 <= latitude <= 20.02
```

AND

```text
73.77 <= longitude <= 73.81
```

> **Note:** This bounding box is a prototype geographic boundary
> for development and testing. It is not an official administrative
> or municipal boundary.

---

# Day 3 Validation Flow

```text
                 GPS CSV Data
                      |
                      v
              PySpark DataFrame
                      |
                      v
            Coordinate Validation
                      |
             +--------+--------+
             |                 |
             v                 v
          VALID             INVALID
             |                 |
             |                 |
             +--------+--------+
                      |
                      v
              Validation Result
```

---

# Validation Rules

## 1. Latitude Validation

The latitude must be within:

```text
19.98 to 20.02
```

If latitude is smaller than `19.98` or greater than `20.02`,
the record is marked as invalid.

---

## 2. Longitude Validation

The longitude must be within:

```text
73.77 to 73.81
```

If longitude is smaller than `73.77` or greater than `73.81`,
the record is marked as invalid.

---

## 3. Complete Coordinate Validation

A GPS record is valid only when both conditions are satisfied:

```text
Latitude  -> inside boundary
Longitude -> inside boundary
```

Otherwise:

```text
boundary_status = INVALID
```

---

# Validation Output Columns

The validation process adds two new columns to the GPS data.

## boundary_status

Possible values:

```text
VALID
INVALID
```

### VALID

The latitude and longitude are inside the configured boundary.

### INVALID

The GPS coordinate is outside the configured boundary or contains
missing coordinates.

---

# validation_reason

The validation process provides a reason for each validation result.

Possible values:

```text
WITHIN_BOUNDARY
OUTSIDE_LATITUDE
OUTSIDE_LONGITUDE
MISSING_COORDINATES
```

## WITHIN_BOUNDARY

The GPS coordinate is completely inside the configured boundary.

## OUTSIDE_LATITUDE

The latitude is outside the permitted latitude range.

## OUTSIDE_LONGITUDE

The longitude is outside the permitted longitude range.

## MISSING_COORDINATES

Latitude or longitude is missing.

---

# Project Files

## boundary_validation.py

Main Day 3 PySpark job.

Responsibilities:

* Load GPS data.
* Apply the GPS schema.
* Validate latitude.
* Validate longitude.
* Generate `boundary_status`.
* Generate `validation_reason`.
* Display valid records.
* Display invalid records.
* Display validation statistics.

---

## boundary.py

Contains the geographic boundary configuration.

It defines:

```text
MIN_LATITUDE
MAX_LATITUDE
MIN_LONGITUDE
MAX_LONGITUDE
```

It also provides a utility function:

```python
is_inside_boundary(latitude, longitude)
```

---

## gps_schema.py

Defines the structure of GPS records.

Current schema:

```text
device_id
latitude
longitude
timestamp
accuracy
```

---

## gps_ingestion.py

Loads the GPS CSV file into a PySpark DataFrame using the
predefined GPS schema.

Input:

```text
data/sample_gps.csv
```

---

## test_sedona.py

Tests:

* PySpark initialization.
* Apache Sedona initialization.
* Creation of a sample GPS DataFrame.

---

# Input Data

The Day 3 validation job reads:

```text
data/sample_gps.csv
```

The input contains the following fields:

```text
device_id
latitude
longitude
timestamp
accuracy
```

Example:

```text
device_001,19.9975,73.7898,2026-09-26 08:00:00,5.2
```

---

# Sample Validation

Example of a valid coordinate:

```text
Latitude  = 19.9975
Longitude = 73.7898
```

Since:

```text
19.98 <= 19.9975 <= 20.02
```

and:

```text
73.77 <= 73.7898 <= 73.81
```

the record is:

```text
VALID
```

with:

```text
WITHIN_BOUNDARY
```

---

# Example Invalid Latitude

Example:

```text
Latitude  = 19.9768
Longitude = 73.7882
```

The latitude is below:

```text
19.98
```

Therefore:

```text
boundary_status = INVALID
validation_reason = OUTSIDE_LATITUDE
```

---

# Example Invalid Longitude

Example:

```text
Latitude  = 19.9929
Longitude = 73.8199
```

The longitude is greater than:

```text
73.81
```

Therefore:

```text
boundary_status = INVALID
validation_reason = OUTSIDE_LONGITUDE
```

---

# Day 3 Sample Dataset Result

The sample dataset contains:

```text
Total GPS Records = 30
```

Expected validation result:

```text
VALID   = 25
INVALID = 5
```

---

# Invalid Records

The following records are intentionally outside the prototype
boundary.

| Device ID  | Latitude | Longitude | Reason            |
| ---------- | -------: | --------: | ----------------- |
| device_021 |  19.9768 |   73.7882 | OUTSIDE_LATITUDE  |
| device_022 |  19.9939 |   73.7519 | OUTSIDE_LONGITUDE |
| device_024 |  20.0272 |   73.7968 | OUTSIDE_LATITUDE  |
| device_026 |  19.9556 |   73.7871 | OUTSIDE_LATITUDE  |
| device_028 |  19.9929 |   73.8199 | OUTSIDE_LONGITUDE |

---

# Running the Jobs

All commands should be executed from the GeoPulse project root.

Example:

```text
GeoPulse/
```

---

## 1. Activate Virtual Environment

PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

---

## 2. Test Apache Sedona

Run:

```powershell
.\.venv\Scripts\python.exe -m spatial.jobs.test_sedona
```

Expected message:

```text
Sedona initialization successful!
```

---

## 3. Test GPS Ingestion

Run:

```powershell
.\.venv\Scripts\python.exe -m spatial.jobs.gps_ingestion
```

The job displays:

* GPS records
* DataFrame schema
* Record count

---

## 4. Run Boundary Validation

Run:

```powershell
.\.venv\Scripts\python.exe -m spatial.jobs.boundary_validation
```

The job displays:

```text
Configured Geographic Boundary
Total GPS Records
Validation Results
Boundary Status Count
Valid GPS Records
Invalid GPS Records
```

---

# Expected Console Output

The beginning of the output should look similar to:

```text
======================================================================
GeoPulse - Geographic Boundary Validation
======================================================================

Configured Geographic Boundary:
Latitude : 19.98 to 20.02
Longitude: 73.77 to 73.81

Total GPS Records:
30
```

The validation status should contain:

```text
VALID
INVALID
```

The final message should be:

```text
Boundary validation completed successfully.
```

---

# Python Module Execution

The jobs should be executed using Python module mode.

Correct:

```powershell
.\.venv\Scripts\python.exe -m spatial.jobs.boundary_validation
```

Avoid directly running:

```powershell
python spatial\jobs\boundary_validation.py
```

Module execution is used so that the `spatial` package imports work
correctly from the GeoPulse project root.

---

# Day 3 Technical Stack

The Day 3 implementation uses:

```text
Python
PySpark
Apache Spark
Apache Sedona
CSV
```

PySpark is used for distributed-style DataFrame processing.

Apache Sedona is included as the project's spatial processing
framework and will be used more extensively in later spatial tasks.

---

# Day 3 Implementation

The processing flow is:

```text
CSV
 |
 v
PySpark CSV Reader
 |
 v
GPS Schema
 |
 v
GPS DataFrame
 |
 v
Latitude Validation
 |
 v
Longitude Validation
 |
 v
boundary_status
 |
 v
validation_reason
 |
 v
Valid / Invalid Records
```

---

# Quality Checks

Day 3 includes the following checks:

* GPS CSV can be loaded.
* GPS schema matches the input data.
* Latitude values are checked.
* Longitude values are checked.
* Missing coordinates are handled.
* Valid records are identified.
* Invalid records are identified.
* Validation reasons are generated.
* Total records are counted.
* Valid/invalid counts are displayed.

---

# Day 3 Deliverables

The following files are part of the Day 3 implementation:

```text
spatial/
│
├── jobs/
│   ├── boundary_validation.py
│   └── README.md
│
├── schemas/
│   └── gps_schema.py
│
└── utils/
    └── boundary.py
```

The existing Day 2 files remain part of the project:

```text
spatial/jobs/gps_ingestion.py
spatial/jobs/test_sedona.py
data/sample_gps.csv
```

---

# Day 3 Commit

Git commit message:

```text
feat: add geographic boundary validation
```

Commands:

```powershell
git add spatial data README.md
```

```powershell
git commit -m "feat: add geographic boundary validation"
```

```powershell
git push origin sakshi
```

---

# Day 3 Completion Criteria

Day 3 is considered complete when:

```text
[✓] Geographic boundary configured
[✓] GPS schema defined
[✓] GPS data loaded successfully
[✓] Latitude validation implemented
[✓] Longitude validation implemented
[✓] VALID / INVALID status implemented
[✓] Validation reason implemented
[✓] Missing coordinates handled
[✓] Sample data tested
[✓] 30 records processed
[✓] 25 valid records identified
[✓] 5 invalid records identified
[✓] Sedona test successful
[✓] Documentation completed
[✓] Git commit created
[✓] Changes pushed to sakshi branch
```

---

# Future Spatial Enhancements

The current Day 3 implementation uses a simple rectangular
bounding box.

Future versions can use:

```text
Actual geographic polygons
City boundaries
Administrative boundaries
GeoJSON
Shapefiles
Apache Sedona spatial functions
```

These can provide more accurate geographic validation than a
simple latitude/longitude bounding box.

---

# Next Task

The next Member 2 spatial engineering task is:

```text
Day 4 – Spatial Distance and Movement Calculation
```

The next stage will use validated GPS records to calculate:

* Distance between consecutive GPS points.
* Movement between locations.
* Device-level movement.
* Total distance travelled.
* Movement-related metrics.

# GeoPulse

## Geospatial Mobility Analytics Platform

GeoPulse is a geospatial data processing and mobility analytics project designed to analyze movement data, detect spatial patterns, validate geographic boundaries, and identify important mobility insights using modern big-data and geospatial technologies.

The project uses Python, Apache Spark, Apache Sedona, and spatial data processing techniques to build a scalable geospatial analytics pipeline.

---

# Project Objectives

The main objectives of GeoPulse are:

- Process large-scale geospatial mobility data.
- Perform spatial data validation.
- Analyze movement and location patterns.
- Detect invalid geographic coordinates.
- Perform point-in-polygon analysis.
- Validate whether movement points fall inside defined boundaries.
- Prepare clean spatial datasets for further analytics.
- Build a scalable spatial-processing environment using Apache Spark and Apache Sedona.
- Generate analytical outputs that can later be used for dashboards and visualization.

---

# Technology Stack

## Programming Language

- Python 3.12+

## Big Data Processing

- Apache Spark
- PySpark

## Geospatial Processing

- Apache Sedona
- Spatial SQL
- GeoPandas
- Shapely

## Data Processing

- Pandas
- CSV
- JSON

## Testing

- Pytest

## Development Tools

- Visual Studio Code
- PowerShell
- Git
- GitHub
- Python Virtual Environment

---

# Project Structure

```text
GeoPulse/
│
├── spatial/
│   ├── __init__.py
│   │
│   ├── jobs/
│   │   ├── __init__.py
│   │   ├── test_sedona.py
│   │   ├── boundary_validation.py
│   │   └── movement_analysis.py
│   │
│   ├── data/
│   │   ├── raw/
│   │   ├── processed/
│   │   └── sample/
│   │
│   ├── schemas/
│   │   └── spatial_schema.py
│   │
│   └── utils/
│       ├── __init__.py
│       └── spatial_utils.py
│
├── tests/
│   ├── __init__.py
│   └── test_spatial_processing.py
│
├── requirements.txt
├── README.md
└── .gitignore

# GeoPulse — Day 5

## Member 2: GPS Data Preparation for Snowflake Ingestion

### 📌 Overview

Day 5 focuses on preparing GPS and movement data for ingestion into **Snowflake**.

The objective is to clean, validate, organize, and prepare GPS records so they can be loaded into the `GEOPULSE.RAW` schema created by Member 1.

---

## 🎯 Day 5 Objective

The main objectives are:

* Prepare GPS data for Snowflake ingestion.
* Create a structured GPS CSV dataset.
* Validate GPS coordinates.
* Remove duplicate records.
* Validate speed and GPS accuracy values.
* Convert timestamps into a standard format.
* Sort GPS records by user and timestamp.
* Generate Snowflake table and ingestion SQL.
* Keep the data ready for the next stages of the GeoPulse pipeline.

---

## 📁 Project Structure

```text
GeoPulse/
│
├── data/
│   └── snowflake/
│       ├── gps_data.csv
│       ├── gps_data_prepared.csv
│       └── load_gps_data.sql
│
├── spatial/
│   └── ingestion/
│       ├── __init__.py
│       ├── prepare_gps_data.py
│       └── snowflake_loader.py
│
└── README.md
```

---

## 📊 GPS Dataset

The GPS dataset contains the following fields:

| Column       | Description            |
| ------------ | ---------------------- |
| `gps_id`     | Unique GPS record ID   |
| `user_id`    | User/device identifier |
| `latitude`   | GPS latitude           |
| `longitude`  | GPS longitude          |
| `timestamp`  | GPS record timestamp   |
| `speed_kmh`  | Movement speed in km/h |
| `accuracy_m` | GPS accuracy in meters |

---

## 🧹 Data Preparation

The `prepare_gps_data.py` script performs the following operations:

### 1. Load GPS Data

The script reads:

```text
data/snowflake/gps_data.csv
```

using Pandas.

### 2. Remove Duplicate Records

Duplicate GPS records are removed using:

```python
df.drop_duplicates()
```

### 3. Validate Coordinates

Latitude must be between:

```text
-90 and 90
```

Longitude must be between:

```text
-180 and 180
```

Invalid coordinates are removed.

### 4. Validate Speed

Speed values must be greater than or equal to zero.

### 5. Validate GPS Accuracy

Accuracy values must be greater than zero.

### 6. Convert Timestamp

GPS timestamps are converted into a standard Pandas datetime format.

### 7. Sort Records

Records are sorted using:

```text
user_id
timestamp
```

This makes the data suitable for movement analysis.

---

## ❄️ Snowflake Preparation

The `snowflake_loader.py` script prepares SQL for loading the cleaned GPS data into:

```text
GEOPULSE
   └── RAW
       └── GPS_DATA
```

The generated Snowflake table contains:

```sql
GPS_ID INTEGER
USER_ID VARCHAR(50)
LATITUDE FLOAT
LONGITUDE FLOAT
TIMESTAMP TIMESTAMP_NTZ
SPEED_KMH FLOAT
ACCURACY_M FLOAT
```

The generated SQL file is:

```text
data/snowflake/load_gps_data.sql
```

---

## ▶️ How to Run

### Step 1 — Activate Virtual Environment

From the GeoPulse root directory:

```powershell
.venv\Scripts\Activate.ps1
```

### Step 2 — Prepare GPS Data

Run:

```powershell
python -m spatial.ingestion.prepare_gps_data
```

Expected output:

```text
Loading GPS data...
Initial rows: 20
Prepared rows: 20
Saved file: data\snowflake\gps_data_prepared.csv
```

### Step 3 — Generate Snowflake SQL

Run:

```powershell
python -m spatial.ingestion.snowflake_loader
```

Expected output:

```text
Preparing Snowflake ingestion SQL...
Records ready for ingestion: 20
SQL file created: data\snowflake\load_gps_data.sql
GPS data is ready for Snowflake ingestion.
```

---

## 🔍 Data Validation

The prepared dataset is checked for:

* Duplicate records
* Missing values
* Invalid latitude
* Invalid longitude
* Negative speed
* Invalid GPS accuracy
* Incorrect timestamp format

The validation summary is displayed by the preparation script.

---

## 🔄 Data Flow

```text
Raw GPS CSV
     │
     ▼
prepare_gps_data.py
     │
     ├── Remove duplicates
     ├── Validate coordinates
     ├── Validate speed
     ├── Validate accuracy
     ├── Convert timestamps
     └── Sort records
     │
     ▼
gps_data_prepared.csv
     │
     ▼
snowflake_loader.py
     │
     ▼
load_gps_data.sql
     │
     ▼
GEOPULSE.RAW.GPS_DATA
```

---

## 👥 Team Integration

### Member 1

Creates the Snowflake structure:

```text
GEOPULSE
├── RAW
├── STAGING
└── ANALYTICS
```

### Member 2

Prepares GPS data and generates the ingestion SQL.

### Member 3

Configures the dbt connection with Snowflake.

### Member 4

Creates the Snowflake API service for retrieving data.

---

## 📦 Day 5 Deliverables

* [x] GPS sample dataset
* [x] GPS data preparation script
* [x] Data validation
* [x] Duplicate removal
* [x] Timestamp conversion
* [x] Prepared GPS dataset
* [x] Snowflake table definition
* [x] Snowflake ingestion SQL
* [x] Local execution test

---

## 🧪 Testing

The following commands were used to test the Day 5 implementation:

```powershell
python -m spatial.ingestion.prepare_gps_data
```

```powershell
python -m spatial.ingestion.snowflake_loader
```

Both scripts should complete successfully without errors.

---

## 🚀 Git Commit

Day 5 commit:

```text
feat: prepare GPS data for Snowflake ingestion
```

Push the changes:

```powershell
git add data/snowflake spatial/ingestion
git commit -m "feat: prepare GPS data for Snowflake ingestion"
git push origin sakshi
```

---

## 🎯 Day 5 Result

At the end of Day 5, GPS data is cleaned, validated, structured, and ready to be ingested into the **GeoPulse Snowflake RAW layer**.

This creates the foundation for the next stages of the GeoPulse data pipeline, including **dbt transformations, analytics, and API-based data retrieval**.

# 🌍 GeoPulse — Day 6

## Snowflake GPS Data Validation & Data Quality

### 📅 Day

**Day 6**

### 👤 Member

**Member 2**

### 🎯 Objective

The main objective of Day 6 is to prepare the **GPS data for reliable processing in Snowflake** by creating the RAW GPS table and performing different data validation and data quality checks.

The validation process checks for:

* Missing values
* Invalid GPS coordinates
* Duplicate records
* Invalid speed values
* Invalid GPS accuracy
* Timestamp issues
* Device-level data quality
* GPS data ranges
* Outliers and unusual values

---

# 🏗️ Day 6 Architecture

```text
GPS CSV Data
     │
     ▼
┌─────────────────────┐
│ Snowflake RAW Layer │
│      GPS_RAW        │
└──────────┬──────────┘
           │
           ▼
┌──────────────────────────┐
│     Data Validation      │
│                          │
│ • NULL checks            │
│ • Coordinate validation  │
│ • Duplicate detection    │
│ • Speed validation       │
│ • Accuracy validation    │
│ • Timestamp checks       │
└──────────┬───────────────┘
           │
           ▼
┌──────────────────────────┐
│    Data Quality Checks   │
│                          │
│ • Outlier detection      │
│ • Device profiling       │
│ • Date analysis          │
│ • Hour analysis          │
└──────────┬───────────────┘
           │
           ▼
      STAGING Layer
```

---

# 📁 Day 6 Files

```text
snowflake/
└── scripts/
    ├── create_tables.sql
    ├── validate_gps_data.sql
    ├── data_quality_checks.sql
    └── gps_profile.sql
```

---

# 🗄️ Snowflake Database Structure

```text
GEOPULSE
│
├── RAW
│   └── GPS_RAW
│
├── STAGING
│
└── ANALYTICS
```

Day 6 mainly works with:

```text
GEOPULSE.RAW.GPS_RAW
```

---

# 📊 GPS_RAW Table

The RAW table contains the original GPS information.

| Column      | Data Type | Description           |
| ----------- | --------- | --------------------- |
| `device_id` | VARCHAR   | GPS device identifier |
| `timestamp` | TIMESTAMP | GPS record time       |
| `latitude`  | FLOAT     | Latitude coordinate   |
| `longitude` | FLOAT     | Longitude coordinate  |
| `speed`     | FLOAT     | Device speed          |
| `accuracy`  | FLOAT     | GPS accuracy          |

---

# 1️⃣ Create RAW Table

File:

```text
create_tables.sql
```

The table is created inside:

```text
GEOPULSE.RAW
```

Example:

```sql
CREATE TABLE IF NOT EXISTS GPS_RAW (
    device_id VARCHAR(50),
    timestamp TIMESTAMP,
    latitude FLOAT,
    longitude FLOAT,
    speed FLOAT,
    accuracy FLOAT
);
```

---

# 2️⃣ Data Validation

File:

```text
validate_gps_data.sql
```

The validation script checks the quality of incoming GPS records.

## NULL Checks

Checks for missing:

```text
device_id
timestamp
latitude
longitude
speed
accuracy
```

Example:

```sql
SELECT COUNT(*) AS null_latitudes
FROM GPS_RAW
WHERE latitude IS NULL;
```

---

# 🌐 3️⃣ Latitude Validation

Valid latitude range:

```text
-90 to +90
```

Query:

```sql
SELECT *
FROM GPS_RAW
WHERE latitude IS NOT NULL
  AND latitude NOT BETWEEN -90 AND 90;
```

Records returned by this query contain invalid latitude values.

---

# 🌐 4️⃣ Longitude Validation

Valid longitude range:

```text
-180 to +180
```

Query:

```sql
SELECT *
FROM GPS_RAW
WHERE longitude IS NOT NULL
  AND longitude NOT BETWEEN -180 AND 180;
```

---

# 🚗 5️⃣ Speed Validation

Speed should not be negative.

```sql
SELECT *
FROM GPS_RAW
WHERE speed < 0;
```

The query identifies invalid speed records.

---

# 📡 6️⃣ Accuracy Validation

GPS accuracy should not be negative.

```sql
SELECT *
FROM GPS_RAW
WHERE accuracy < 0;
```

Very large accuracy values can also be investigated as possible low-quality GPS readings.

---

# 🔁 7️⃣ Duplicate Detection

Duplicate GPS records are identified using:

```text
device_id
timestamp
latitude
longitude
```

Query:

```sql
SELECT
    device_id,
    timestamp,
    latitude,
    longitude,
    COUNT(*) AS duplicate_count
FROM GPS_RAW
GROUP BY
    device_id,
    timestamp,
    latitude,
    longitude
HAVING COUNT(*) > 1
ORDER BY duplicate_count DESC;
```

---

# ⏱️ 8️⃣ Timestamp Analysis

The dataset is checked for the earliest and latest GPS records.

```sql
SELECT
    MIN(timestamp) AS earliest_timestamp,
    MAX(timestamp) AS latest_timestamp
FROM GPS_RAW;
```

This helps understand the time period covered by the dataset.

---

# 📱 9️⃣ Device Profiling

The number of records generated by each device can be checked.

```sql
SELECT
    device_id,
    COUNT(*) AS record_count
FROM GPS_RAW
GROUP BY device_id
ORDER BY record_count DESC;
```

This helps identify devices with unusually low or high numbers of records.

---

# 📅 🔟 Records by Date

```sql
SELECT
    DATE(timestamp) AS record_date,
    COUNT(*) AS record_count
FROM GPS_RAW
GROUP BY DATE(timestamp)
ORDER BY record_date;
```

This helps understand daily GPS data volume.

---

# 🕐 1️⃣1️⃣ Records by Hour

```sql
SELECT
    EXTRACT(HOUR FROM timestamp) AS record_hour,
    COUNT(*) AS record_count
FROM GPS_RAW
GROUP BY EXTRACT(HOUR FROM timestamp)
ORDER BY record_hour;
```

This helps analyze when GPS data is being generated.

---

# 📈 1️⃣2️⃣ GPS Data Profiling

File:

```text
gps_profile.sql
```

The profile provides:

* Total records
* Unique devices
* First GPS record
* Last GPS record
* Minimum latitude
* Maximum latitude
* Minimum longitude
* Maximum longitude
* Minimum speed
* Maximum speed
* Average speed
* Average accuracy

Example:

```sql
SELECT
    COUNT(*) AS total_records,
    COUNT(DISTINCT device_id) AS unique_devices,
    MIN(timestamp) AS first_record,
    MAX(timestamp) AS last_record,
    MIN(latitude) AS min_latitude,
    MAX(latitude) AS max_latitude,
    MIN(longitude) AS min_longitude,
    MAX(longitude) AS max_longitude,
    MIN(speed) AS min_speed,
    MAX(speed) AS max_speed,
    AVG(speed) AS average_speed,
    AVG(accuracy) AS average_accuracy
FROM GPS_RAW;
```

---

# 🧪 Final Data Quality Report

The final validation summary provides a quick overview of the dataset.

```sql
SELECT
    COUNT(*) AS total_records,
    COUNT_IF(device_id IS NULL) AS missing_device_id,
    COUNT_IF(timestamp IS NULL) AS missing_timestamp,
    COUNT_IF(latitude IS NULL) AS missing_latitude,
    COUNT_IF(longitude IS NULL) AS missing_longitude,
    COUNT_IF(latitude NOT BETWEEN -90 AND 90)
        AS invalid_latitude,
    COUNT_IF(longitude NOT BETWEEN -180 AND 180)
        AS invalid_longitude,
    COUNT_IF(speed < 0)
        AS invalid_speed,
    COUNT_IF(accuracy < 0)
        AS invalid_accuracy,
    COUNT(DISTINCT device_id)
        AS unique_devices
FROM GPS_RAW;
```

---

# 🧠 Concepts Learned

During Day 6, the following concepts were covered:

### SQL

* `SELECT`
* `COUNT`
* `COUNT_IF`
* `COUNT(DISTINCT)`
* `MIN`
* `MAX`
* `AVG`
* `MEDIAN`
* `GROUP BY`
* `HAVING`
* `ORDER BY`
* `WHERE`
* `BETWEEN`
* `EXTRACT`
* `DATE`

### Data Engineering

* Data validation
* Data profiling
* Data quality
* Duplicate detection
* NULL detection
* Range validation
* Outlier identification
* Raw data processing
* Snowflake RAW layer

---

# 🔄 Day 6 Data Flow

```text
Raw GPS Data
     ↓
GPS_RAW
     ↓
NULL Validation
     ↓
Coordinate Validation
     ↓
Speed Validation
     ↓
Accuracy Validation
     ↓
Duplicate Detection
     ↓
Timestamp Analysis
     ↓
Device Profiling
     ↓
Data Quality Report
     ↓
STAGING
```

---

# ✅ Day 6 Checklist

* [x] Create Snowflake RAW table
* [x] Create GPS_RAW structure
* [x] Check total records
* [x] Check NULL values
* [x] Validate latitude
* [x] Validate longitude
* [x] Validate speed
* [x] Validate accuracy
* [x] Detect duplicate records
* [x] Analyze timestamps
* [x] Analyze devices
* [x] Analyze records by date
* [x] Analyze records by hour
* [x] Create GPS data profile
* [x] Create final data quality report

---

# 🚀 Git Commit

After completing Day 6:

```bash
git add snowflake/scripts
git commit -m "feat: add GPS data quality and validation checks"
git push origin sakshi
```

---

# 📌 Day 6 Outcome

By the end of Day 6, the GeoPulse project has a structured **Snowflake RAW GPS layer** with validation and profiling queries.

The validated data is now ready to move toward the **STAGING layer** for cleaning and transformation.

**Next:** Day 7 will focus on **cleaning and transforming GPS data in the STAGING layer**.

# GeoPulse — Day 7: Spatial Hotspot Analysis

## 📌 Overview

Day 7 focuses on **Spatial Hotspot Analysis** in the GeoPulse project.

The objective is to identify geographic areas where a large number of movement events are concentrated. Hotspot analysis helps detect locations with unusually high activity and provides useful spatial insights from movement data.

The implementation uses **PySpark** for distributed data processing and **Apache Sedona** for spatial operations.

---

## 🎯 Day 7 Objectives

* Load processed movement data using Spark.
* Create spatial points from latitude and longitude.
* Divide the geographic area into spatial grid cells.
* Count movement events inside each grid cell.
* Calculate hotspot statistics.
* Identify high-activity spatial regions.
* Save the hotspot analysis results for further processing or visualization.

---

## 🛠️ Technologies Used

* Python 3.12.10
* Apache Spark 3.5.6
* Apache Sedona
* PySpark
* GeoPandas / spatial libraries where required
* PyTest
* Windows 11
* VS Code
* Git & GitHub

---

## 📂 Project Structure

```text
GeoPulse/
│
├── spatial/
│   ├── __init__.py
│   │
│   ├── jobs/
│   │   ├── __init__.py
│   │   ├── boundary_validation.py
│   │   ├── movement_analysis.py
│   │   └── hotspot_analysis.py
│   │
│   ├── utils/
│   │   └── ...
│   │
│   └── tests/
│       └── ...
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── output/
│
├── configs/
│   └── ...
│
├── .venv/
├── requirements.txt
├── README.md
└── ...
```

---

# 🔥 Hotspot Analysis

## What is a Spatial Hotspot?

A **spatial hotspot** is a geographic area where the concentration of events is significantly higher than surrounding areas.

For example:

```text
Low Activity       Medium Activity       High Activity

   🟢                    🟡                    🔴
   🟢                    🟡                    🔴
   🟢                    🟡                    🔴
```

In GeoPulse, movement events are grouped into spatial regions and the number of events in each region is calculated.

A region with a high number of movement events can be considered a **high-activity area**.

---

# 🧠 Day 7 Processing Flow

```text
Movement Data
      │
      ▼
Load Data using Spark
      │
      ▼
Validate Latitude / Longitude
      │
      ▼
Create Spatial Points
      │
      ▼
Create Spatial Grid
      │
      ▼
Assign Events to Grid Cells
      │
      ▼
Count Events per Grid Cell
      │
      ▼
Calculate Hotspot Statistics
      │
      ▼
Identify High-Activity Areas
      │
      ▼
Save Hotspot Results
```

---

# 📊 Spatial Grid Concept

The geographic area is divided into smaller grid cells.

Example:

```text
+------+------+------+------+
| Cell | Cell | Cell | Cell |
|  A1  |  A2  |  A3  |  A4  |
+------+------+------+------+
| Cell | Cell | Cell | Cell |
|  B1  |  B2  |  B3  |  B4  |
+------+------+------+------+
| Cell | Cell | Cell | Cell |
|  C1  |  C2  |  C3  |  C4  |
+------+------+------+------+
```

Each movement event is assigned to a grid cell based on its geographic coordinates.

The number of events in each cell is then calculated.

---

# 📍 Input Data

The hotspot analysis uses movement/location data containing geographic information such as:

* Latitude
* Longitude
* Event ID
* Timestamp
* Movement information
* Other processed spatial attributes

Invalid geographic coordinates are filtered before spatial processing.

Valid latitude range:

```text
-90 to 90
```

Valid longitude range:

```text
-180 to 180
```

---

# ⚙️ Implementation

The Day 7 job can be executed using:

```powershell
python -u -m spatial.jobs.hotspot_analysis
```

The `-m` option runs the Python module from the project package.

---

# 🚀 Running Day 7

## 1. Open the project directory

```powershell
cd "C:\Users\Shree\OneDrive\Desktop\Infotact_18_project_no_2\GeoPulse"
```

---

## 2. Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

After activation, the terminal should show:

```text
(.venv)
```

---

## 3. Verify Python

```powershell
python --version
```

Expected:

```text
Python 3.12.10
```

---

## 4. Run Hotspot Analysis

```powershell
python -u -m spatial.jobs.hotspot_analysis
```

---

# 🔍 Expected Processing

The job should perform the following operations:

### Step 1 — Start Spark

A Spark session is initialized for distributed processing.

### Step 2 — Initialize Apache Sedona

Sedona is used for spatial data processing and geographic operations.

### Step 3 — Load Movement Data

The processed movement dataset is loaded into a Spark DataFrame.

### Step 4 — Validate Coordinates

Latitude and longitude values are checked to ensure they contain valid geographic coordinates.

### Step 5 — Create Spatial Data

Coordinates are converted into spatial point representations.

### Step 6 — Generate Spatial Grid

The geographic area is divided into grid cells.

### Step 7 — Aggregate Events

Movement events are grouped according to their grid cells.

### Step 8 — Calculate Hotspot Statistics

Event density/activity is calculated for each spatial region.

### Step 9 — Identify Hotspots

Grid cells with comparatively high activity are identified as hotspot areas.

### Step 10 — Save Results

The generated hotspot results are written to the configured output location.

---

# 📈 Example Output

A conceptual hotspot result can look like:

| Grid Cell | Event Count | Activity Level |
| --------- | ----------: | -------------- |
| G001      |        1250 | High           |
| G002      |         820 | Medium         |
| G003      |         310 | Low            |
| G004      |        1475 | High           |

The exact values depend on the dataset used by the GeoPulse pipeline.

---

# 🧪 Validation

The Day 7 implementation should be checked for:

* Successful Spark initialization
* Successful Sedona initialization
* Correct input data loading
* Valid latitude and longitude values
* Correct spatial point creation
* Correct grid assignment
* Correct event aggregation
* Correct hotspot calculation
* Successful output generation

---

# 🛡️ Error Handling

The job should handle common problems such as:

* Missing input files
* Empty datasets
* Invalid coordinates
* Null latitude/longitude values
* Spark initialization errors
* Sedona configuration errors
* Invalid data types
* Output directory problems

Meaningful error messages should be displayed when processing fails.

---

# 💡 Why Hotspot Analysis is Useful

Spatial hotspot analysis can be used to understand:

* High-traffic areas
* Frequently visited locations
* Movement concentration
* Geographic activity patterns
* Potential congestion zones
* Frequently occurring spatial events
* Regional movement behavior

This makes hotspot analysis an important component of a geospatial analytics pipeline.

---

# 🔗 Relation with Previous GeoPulse Tasks

The GeoPulse pipeline progressively builds spatial intelligence.

```text
Day 3
Boundary Validation
       │
       ▼
Day 4
Movement Analysis
       │
       ▼
Day 7
Spatial Hotspot Analysis
       │
       ▼
Spatial Insights
```

The outputs from previous spatial processing stages can be used as inputs for hotspot analysis.

---

# 🧰 Environment

| Component        | Version    |
| ---------------- | ---------- |
| Operating System | Windows 11 |
| Python           | 3.12.10    |
| PySpark          | 3.5.6      |
| Apache Spark     | 3.5.6      |
| Java             | 21.0.12    |
| PyTest           | 9.1.1      |
| Environment      | `.venv`    |

---

# 📌 Important Command

Run the Day 7 task from the **GeoPulse root directory**:

```powershell
python -u -m spatial.jobs.hotspot_analysis
```

Do not run the file by directly using:

```powershell
python hotspot_analysis.py
```

when the implementation depends on the project package structure.

---

# ✅ Day 7 Completion Checklist

* [x] Spark environment configured
* [x] Sedona environment configured
* [x] Hotspot analysis module created
* [x] Spatial data processing implemented
* [x] Spatial grid processing implemented
* [x] Hotspot aggregation implemented
* [x] Output processing implemented
* [x] Day 7 job executed successfully
* [ ] Final visualization/dashboard integration

---

# 🎯 Day 7 Outcome

By completing Day 7, GeoPulse can process geographic movement data and determine areas with concentrated spatial activity.

The generated hotspot information can later be used for:

* Spatial visualization
* Maps
* Dashboards
* Geographic pattern analysis
* Advanced spatial analytics

---

## Day 8 – Spatial Hotspot Visualization

### Objective

The objective of Day 8 was to convert the spatial hotspot analysis results into a structured and visual format.

### Work Completed

- Read the hotspot analysis output generated in Day 7.
- Validated the required spatial columns.
- Classified locations into LOW, MEDIUM, and HIGH hotspot categories.
- Generated a structured CSV output.
- Created a scatter-based spatial visualization.
- Added automated tests for hotspot classification and coordinate validation.

### Input

The visualization process uses the hotspot analysis output containing:

- Latitude
- Longitude
- Grid ID
- Point Count
- Density

### Hotspot Classification

The density values are divided into three categories:

- LOW – lower-density spatial areas
- MEDIUM – moderate-density spatial areas
- HIGH – higher-density spatial areas

### Output

The process generates:

`data/output/hotspot_visualized.csv`

The output contains:

- latitude
- longitude
- grid_id
- point_count
- density
- classification

A spatial visualization is also generated:

`data/output/hotspot_map.png`

### Testing

Automated tests were added to verify:

- Required columns
- Hotspot classification
- Valid classification values
- Latitude range
- Longitude range

### Technologies Used

- Python
- Pandas
- Matplotlib
- Pytest
- PySpark / Apache Sedona from previous spatial processing stages

### Day 8 Outcome

The hotspot results generated during spatial analysis are now available as both structured data and a visual representation, making high-density spatial areas easier to identify and analyze.
# GeoPulse - Day 9
## Spatial Data Quality Validation

### Overview

Day 9 focuses on validating the quality and consistency of the spatial GPS data used in the GeoPulse project.

The objective is to identify invalid coordinates, missing values, incorrect timestamps, and duplicate records before performing further spatial analysis.

---

## Objectives

The main objectives of Day 9 are:

1. Load the GPS mobility dataset.
2. Inspect the structure and schema of the data.
3. Validate latitude and longitude values.
4. Validate timestamp information.
5. Identify missing values.
6. Detect duplicate records.
7. Generate a data-quality summary.
8. Save the validation results for further analysis.

---

## Technologies Used

- Python 3.12.10
- Apache Spark
- PySpark 3.5.6
- Apache Sedona
- Pandas
- Git and GitHub

---

## Project Structure

```text
GeoPulse/
│
├── data/
│   ├── gps/
│   ├── polygons/
│   └── output/
│       └── day9_validation/
│
├── spatial/
│   ├── jobs/
│   │   ├── boundary_validation.py
│   │   ├── movement_analysis.py
│   │   └── spatial_validation.py
│   │
│   └── utils/
│
├── tests/
│
├── README.md
└── requirements.txt
# GeoPulse: Day 10 - End-to-End Pipeline Orchestration & Warehouse Integration

## Overview
Day 10 finalizes the GeoPulse mobility analytics platform by connecting all previously isolated modules into a single, automated, production-ready execution pipeline (`jobs/pipeline.py`). It orchestrates GPS ingestion, spatial validation, movement calculation, hotspot clustering, and final artifact generation.

---

## Complete Project Structure

```text
GeoPulse/
└── spatial/
    ├── data/
    │   ├── raw_gps_pings.csv
    │   ├── store_boundaries.geojson
    │   └── output/
    │       ├── movement_metrics.parquet/
    │       ├── hotspots.parquet/
    │       └── hotspot_map.html
    ├── jobs/
    │   ├── __init__.py
    │   ├── gps_ingestion.py
    │   ├── spatial_validation.py
    │   ├── boundary_validation.py
    │   ├── movement_analysis.py
    │   ├── hotspot_analysis.py
    │   ├── hotspot_visualization.py
    │   ├── test_sedona.py
    │   └── pipeline.py
    ├── schemas/
    │   └── __init__.py
    ├── tests/
    │   ├── __init__.py
    │   ├── test_boundary_validation.py
    │   ├── test_hotspot_analysis.py
    │   ├── test_hotspot_visualization.py
    │   └── test_movement_analysis.py
    ├── utils/
    │   └── __init__.py
    ├── requirements-spatial.txt
    └── README.md
    # Day 10 - Spatial Hotspot Analysis

## Objective

The objective of Day 10 is to identify geographic areas containing a high concentration of GPS events.

Day 10 uses the validated GPS data generated during Day 9 and performs grid-based spatial aggregation and hotspot classification.

---

## Input Data

Day 10 uses the validated GPS data from Day 9:

```text
data/output/day9_validation/validated_gps/
```

Only records containing valid latitude and longitude values are processed.

---

## Tasks Performed

Day 10 performs the following tasks:

1. Load validated GPS data.
2. Detect latitude and longitude columns.
3. Convert latitude and longitude to numeric values.
4. Remove records with missing coordinates.
5. Create spatial grid cells.
6. Assign each GPS point to a grid.
7. Count GPS events in each grid.
8. Calculate spatial statistics.
9. Calculate density thresholds.
10. Classify grids as HIGH, MEDIUM or LOW.
11. Rank grids based on event count.
12. Identify the top hotspot grids.
13. Save the results.

---

## Spatial Grid Generation

A grid precision of `1000` is used.

The grid coordinates are calculated using:

```text
grid_lat = floor(latitude * 1000)
grid_lon = floor(longitude * 1000)
```

A unique grid identifier is created using:

```text
grid_id = grid_lat_grid_lon
```

For example:

```text
latitude  = 19.9975
longitude = 73.7898
```

can produce:

```text
grid_lat = 19997
grid_lon = 73789
grid_id  = 19997_73789
```

The same calculation is applied consistently to all GPS records.

---

## Grid Event Aggregation

GPS records are grouped by:

```text
grid_id
grid_lat
grid_lon
```

The number of GPS events in each grid is calculated as:

```text
event_count
```

Example:

| grid_id     | grid_lat | grid_lon | event_count |
| ----------- | -------: | -------: | ----------: |
| 19998_73790 |    19998 |    73790 |        1250 |
| 19997_73790 |    19997 |    73790 |        1135 |
| 19997_73789 |    19997 |    73789 |         978 |

The actual values are generated from the input dataset.

---

## Hotspot Classification

The grid cells are classified according to their event density using percentile-based thresholds.

### HIGH

Grid event count is at or above the 90th percentile.

### MEDIUM

Grid event count is at or above the 70th percentile but below the 90th percentile.

### LOW

Grid event count is below the 70th percentile.

This approach allows the classification to adapt to the distribution of the dataset.

---

## Hotspot Ranking

Each grid is assigned a rank based on its event count.

The grid with the highest number of events receives:

```text
hotspot_rank = 1
```

The grids are sorted in descending order of `event_count`.

---

## Statistics Generated

Day 10 calculates the following statistics:

* Total validated records
* Usable spatial records
* Total spatial grids
* Total grid events
* Minimum events per grid
* Maximum events per grid
* Average events per grid
* Medium-density threshold
* High-density threshold

---

## Output Structure

Day 10 generates the following output:

```text
data/
└── output/
    └── day10_hotspots/
        ├── grid_counts/
        ├── hotspot_results/
        └── hotspot_summary/
```

---

## Output Description

### `grid_counts/`

Contains the number of GPS events in each spatial grid.

Fields:

```text
grid_id
grid_lat
grid_lon
event_count
```

---

### `hotspot_results/`

Contains the complete hotspot analysis.

Fields:

```text
grid_id
grid_lat
grid_lon
event_count
density_level
hotspot_rank
```

---

### `hotspot_summary/`

Contains overall hotspot statistics.

Fields:

```text
metric
value
```

---

## Project File

The Day 10 Python implementation is:

```text
spatial/jobs/hotspot_analysis.py
```

---

## How to Run

From the GeoPulse project root directory:

```powershell
python -m spatial.jobs.hotspot_analysis
```

---

## Expected Console Output

```text
======================================================================
GeoPulse - Day 10: Spatial Hotspot Analysis
======================================================================

[1] Starting Spark session...

[2] Locating Day 9 validated GPS data...

[3] Loading validated GPS data...

[4] Detecting coordinate columns...

[5] Preparing spatial coordinates...

[6] Removing records with missing coordinates...

[7] Creating spatial grid...

[8] Counting GPS events per grid...

[9] Saving grid counts...

[10] Calculating hotspot statistics...

[11] Calculating density thresholds...

[12] Classifying spatial density...

[13] Ranking hotspot grids...

[14] Saving hotspot results...

[15] Creating hotspot summary...

======================================================================
HOTSPOT ANALYSIS SUMMARY
======================================================================

Total validated records : XXXXX
Usable spatial records  : XXXXX
Total spatial grids     : XXXXX
Minimum events/grid     : XX
Maximum events/grid     : XXXX
Average events/grid     : XXX

Top hotspot grids:

    1. <grid_id> - XXXX events - HIGH
    2. <grid_id> - XXXX events - HIGH
    3. <grid_id> - XXXX events - HIGH

======================================================================
Day 10 hotspot analysis completed successfully.
======================================================================
```

The actual values are generated automatically from the dataset.

---

## Validation Checklist

```text
[✓] Day 9 validated GPS data loaded
[✓] Latitude detected
[✓] Longitude detected
[✓] Missing coordinates removed
[✓] Spatial grid generated
[✓] GPS points assigned to grids
[✓] Events counted per grid
[✓] Spatial statistics calculated
[✓] Density thresholds calculated
[✓] HIGH/MEDIUM/LOW classification performed
[✓] Hotspots ranked
[✓] Grid counts saved
[✓] Hotspot results saved
[✓] Hotspot summary saved
```

---

## Git Commands

Check the changes:

```powershell
git status
```

Add Day 10 files:

```powershell
git add README.md spatial/jobs/hotspot_analysis.py
```

Commit:

```powershell
git commit -m "Day 10 spatial hotspot analysis"
```

Push to the `sakshi` branch:

```powershell
git push origin sakshi
```

---

## Day 10 Deliverables

```text
1. spatial/jobs/hotspot_analysis.py
2. Grid count results
3. Hotspot analysis results
4. Hotspot summary
5. Updated README.md
```

---

## Day 10 Completion

Day 10 completes the grid-based spatial hotspot analysis of the validated GPS dataset.
The resulting hotspot information can be used in subsequent days for spatial visualization and advanced spatial analysis.

# GeoPulse — Day 11

## Hotspot Insight & Risk Classification

### 📌 Overview

Day 11 of the **GeoPulse** project focuses on converting hotspot detection results into meaningful **risk classifications and business insights**.

The system analyzes spatial hotspot scores and activity levels and classifies geographical grids into three categories:

* **HIGH** — Strong hotspot activity
* **MEDIUM** — Moderate hotspot activity
* **LOW** — Lower hotspot activity

This step transforms the previous spatial-analysis results into an easier-to-understand risk assessment.

---

## 🎯 Objectives

The main objectives of Day 11 are:

1. Load the hotspot results generated in previous stages.
2. Calculate statistics for each geographical grid.
3. Analyze hotspot scores and event activity.
4. Classify each grid into HIGH, MEDIUM, or LOW risk.
5. Generate a structured CSV containing the classifications.
6. Generate a text-based hotspot insight report.
7. Add automated tests for the risk-classification logic.

---

## 🏗️ Day 11 Architecture

```text
GPS / Spatial Data
        │
        ▼
Hotspot Detection
        │
        ▼
hotspot_results.csv
        │
        ▼
Grid Statistics
        │
        ├── Hotspot Score
        ├── Event Count
        └── Unique Users
        │
        ▼
Risk Classification
        │
        ├── HIGH
        ├── MEDIUM
        └── LOW
        │
        ├───────────────┐
        ▼               ▼
CSV Output        Insight Report
```

---

## 📂 Files Added

```text
GeoPulse/
│
├── spatial/
│   └── jobs/
│       └── risk_classification.py
│
├── tests/
│   └── test_risk_classification.py
│
└── data/
    └── output/
        ├── risk_classification.csv
        └── hotspot_insights.txt
```

---

## 📥 Input

Day 11 uses the hotspot output generated during the previous spatial-analysis stages.

### Input file

```text
data/output/hotspot_results.csv
```

The input contains geographical grid information and hotspot-related metrics.

Depending on the previous processing stage, the file may contain columns such as:

```text
grid_id
hotspot_score
event_count
user_id
vehicle_id
device_id
```

The Day 11 script automatically looks for commonly used column names.

---

## ⚙️ Risk Classification Logic

Each geographical grid is assigned a risk level according to its hotspot score.

### 🔴 HIGH Risk

```text
hotspot_score >= 0.70
```

These grids have strong hotspot activity and should receive priority monitoring.

### 🟠 MEDIUM Risk

```text
0.40 <= hotspot_score < 0.70
```

These grids show moderate activity and should be monitored for possible increases.

### 🟢 LOW Risk

```text
hotspot_score < 0.40
```

These grids currently show comparatively lower hotspot activity.

---

## 📊 Grid Statistics

For every grid, the system calculates:

### 1. Hotspot Score

Represents the strength or density of hotspot activity.

### 2. Event Count

Represents the amount of detected activity within the grid.

### 3. Unique Users

Represents the number of distinct users, vehicles, or devices associated with the grid when such information is available.

---

## 📤 Output 1 — Risk Classification CSV

The following file is generated:

```text
data/output/risk_classification.csv
```

Example:

```csv
grid_id,hotspot_score,event_count,unique_users,risk_level
19998_73790,0.91,1250,1250,HIGH
19997_73790,0.84,1087,1087,HIGH
19997_73789,0.62,745,745,MEDIUM
20005_73798,0.48,521,521,MEDIUM
20000_73793,0.21,189,189,LOW
```

The actual values depend on the project's input data.

---

## 📤 Output 2 — Hotspot Insights

The following report is generated:

```text
data/output/hotspot_insights.txt
```

It contains:

* Total grids analyzed
* Average hotspot score
* Number of HIGH-risk grids
* Number of MEDIUM-risk grids
* Number of LOW-risk grids
* Top hotspot grids
* Event counts
* User counts
* Risk interpretation

---

## 🧪 Testing

Day 11 includes automated tests:

```text
tests/test_risk_classification.py
```

The tests verify:

* HIGH-risk classification
* MEDIUM-risk classification
* LOW-risk classification
* Boundary values
* Spark DataFrame processing

---

## ▶️ How to Run

### Step 1 — Open the project

```powershell
cd "C:\Users\Shree\OneDrive\Desktop\Infotact_18_project_no_2\GeoPulse"
```

### Step 2 — Run Day 11

```powershell
python -m spatial.jobs.risk_classification
```

### Step 3 — Run tests

```powershell
pytest tests/test_risk_classification.py -v
```

---

## ✅ Expected Result

After successful execution:

```text
Day 11 completed successfully!
```

The following files should be available:

```text
data/output/risk_classification.csv
data/output/hotspot_insights.txt
```

---

## 🔍 Example Risk Distribution

For example, if five grids are analyzed:

```text
HIGH     : 2 grids
MEDIUM   : 2 grids
LOW      : 1 grid
```

The exact distribution depends on the hotspot data.

---

## 💡 Business Interpretation

The risk classification makes the GeoPulse results easier to understand.

### HIGH Risk

High-risk areas can be prioritized for:

* Traffic monitoring
* Safety monitoring
* Resource allocation
* Further spatial investigation
* Real-time alerts

### MEDIUM Risk

Medium-risk areas can be monitored for:

* Increasing activity
* Repeated events
* Emerging hotspots
* Changes in spatial patterns

### LOW Risk

Low-risk areas can be treated as comparatively stable areas while continuing normal monitoring.

---

## 🛠️ Technologies Used

* Python 3.12.10
* Apache Spark
* PySpark 3.5.6
* Pandas
* Pytest
* CSV
* Spatial Data Processing

---

## 📈 GeoPulse Pipeline Progress

```text
Day 1
Project Setup
     ↓
Day 2–6
Data Processing & Spatial Analysis
     ↓
Day 7
Hotspot Detection
     ↓
Day 8
Visualization
     ↓
Day 9
Spatial Data Quality Validation
     ↓
Day 10
Analysis / Visualization
     ↓
Day 11
Hotspot Insight & Risk Classification
```

---

## 🎯 Day 11 Deliverables

| Deliverable            | Status |
| ---------------------- | ------ |
| Hotspot data loading   | ✅      |
| Grid statistics        | ✅      |
| Hotspot score analysis | ✅      |
| Risk classification    | ✅      |
| CSV generation         | ✅      |
| Insight report         | ✅      |
| Automated tests        | ✅      |
| Documentation          | ✅      |

---

## 📝 Conclusion

Day 11 extends GeoPulse from spatial hotspot detection to **actionable risk analysis**.

The system now identifies geographical areas with different levels of hotspot activity and produces structured outputs that can be used for further visualization, reporting, monitoring, and decision-making.

**GeoPulse Day 11 — Hotspot Insight & Risk Classification completed.**

# GeoPulse - Day 12: Hotspot Reporting and Summary

## Overview

Day 12 focuses on building the **Hotspot Reporting and Summary Module** for the GeoPulse spatial analytics project.

The purpose of this module is to take the hotspot results generated during the previous hotspot analysis stages, validate and standardize the data, classify hotspots according to their risk level, calculate important statistics, and generate a clean summary report.

---

## Day 12 Objectives

The main objectives of Day 12 are:

* Load hotspot analysis results.
* Validate the hotspot data.
* Identify important columns automatically.
* Standardize hotspot risk levels.
* Calculate hotspot scores.
* Calculate event counts.
* Classify hotspots into:

  * HIGH
  * MEDIUM
  * LOW
* Generate hotspot statistics.
* Create a final CSV summary report.
* Add automated tests for the reporting module.
* Handle missing files and invalid data safely.

---

## Project Structure

```text
GeoPulse/
│
├── data/
│   ├── raw/
│   │
│   └── processed/
│       ├── hotspot_results.csv
│       └── hotspot_summary.csv
│
├── spatial/
│   └── jobs/
│       ├── hotspot_analysis.py
│       ├── spatial_validation.py
│       └── hotspot_reporting.py
│
├── tests/
│   └── test_hotspot_reporting.py
│
└── README.md
```

---

## Input File

The Day 12 module reads the hotspot analysis output from:

```text
data/processed/hotspot_results.csv
```

This file contains the hotspot information generated during the previous analysis stages.

Possible information includes:

* Grid ID
* Latitude
* Longitude
* Event count
* Hotspot score
* Risk level

---

## Main Python Module

The main Day 12 module is:

```text
spatial/jobs/hotspot_reporting.py
```

It performs the complete reporting workflow.

### Workflow

```text
Hotspot Results
       |
       v
Load CSV
       |
       v
Validate Data
       |
       v
Calculate Event Count
       |
       v
Calculate Hotspot Score
       |
       v
Classify Risk Level
       |
       v
Generate Statistics
       |
       v
Create Summary
       |
       v
Save CSV Report
```

---

## Risk Classification

Hotspots are categorized into three risk levels:

| Risk Level | Meaning                                  |
| ---------- | ---------------------------------------- |
| HIGH       | High concentration or high hotspot score |
| MEDIUM     | Moderate concentration or hotspot score  |
| LOW        | Lower concentration or hotspot score     |

The module also supports existing risk-level values from the input file.

---

## Generated Statistics

The reporting module calculates:

* Total number of hotspots
* Number of high-risk hotspots
* Number of medium-risk hotspots
* Number of low-risk hotspots
* Total number of events
* Average hotspot score
* Maximum hotspot score

Example:

```text
============================================================
GeoPulse - Day 12 Hotspot Statistics
============================================================
Total hotspots          : 5
High-risk hotspots      : 3
Medium-risk hotspots    : 2
Low-risk hotspots       : 0
Total events            : 53600
Average hotspot score   : 10720.00
Maximum hotspot score   : 18500.00
============================================================
```

The actual values depend on the hotspot results generated by the project.

---

## Output File

The final report is automatically generated at:

```text
data/processed/hotspot_summary.csv
```

The summary contains standardized information such as:

```text
grid_id
latitude
longitude
risk_level
event_count
hotspot_score
```

The rows are sorted by hotspot score in descending order so that the strongest hotspots appear first.

---

## Running the Day 12 Module

Open PowerShell in the GeoPulse project root directory.

Run:

```powershell
python -m spatial.jobs.hotspot_reporting
```

Expected workflow:

```text
======================================================================
GeoPulse - Day 12: Hotspot Reporting
======================================================================
[GeoPulse] Loading hotspot data...
[GeoPulse] Validating hotspot columns...
[GeoPulse] Creating hotspot summary...
[GeoPulse] Classifying hotspots...
[GeoPulse] Final report saved...
Day 12 completed successfully.
======================================================================
```

---

## Running Tests

The Day 12 module contains automated unit tests.

Run:

```powershell
pytest tests/test_hotspot_reporting.py -v
```

The tests verify:

* Risk-level normalization
* Event-count calculation
* Hotspot-score calculation
* Risk classification
* Summary generation
* Statistics generation

Expected result:

```text
6 passed
```

---

## Error Handling

The module handles common problems such as:

### Missing input file

If:

```text
data/processed/hotspot_results.csv
```

does not exist, the program displays an error instead of crashing unexpectedly.

### Empty input file

If the CSV contains no records, the program reports that the file is empty.

### Missing columns

The module attempts to identify equivalent column names such as:

```text
event_count
events
count
point_count
```

and:

```text
hotspot_score
score
density
```

This makes the reporting module more flexible.

---

## Technologies Used

* Python 3.12
* Pandas
* Pytest
* CSV
* Git & GitHub

---

## Day 12 Deliverables

The following files are added or generated during Day 12:

```text
spatial/jobs/hotspot_reporting.py
tests/test_hotspot_reporting.py
data/processed/hotspot_summary.csv
```

---

## Validation

Before committing the Day 12 work, run:

```powershell
python -m spatial.jobs.hotspot_reporting
```

Then run:

```powershell
pytest tests/test_hotspot_reporting.py -v
```

Finally check:

```powershell
git status
```

---

## Git Commands

```powershell
git add spatial/jobs/hotspot_reporting.py tests/test_hotspot_reporting.py data/processed/hotspot_summary.csv README.md
```

Commit:

```powershell
git commit -m "Add Day 12 hotspot reporting and summary module"
```

Push:

```powershell
git push origin sakshi
```

---

## Day 12 Completion Criteria

Day 12 is considered complete when:

* [x] Hotspot results can be loaded.
* [x] Input data is validated.
* [x] Event counts are calculated.
* [x] Hotspot scores are calculated.
* [x] Risk levels are classified.
* [x] Hotspot statistics are generated.
* [x] Summary CSV is generated.
* [x] Unit tests are added.
* [x] Tests pass successfully.
* [x] Changes are committed and pushed to the `sakshi` branch.

---

## Conclusion

Day 12 extends the GeoPulse spatial analytics pipeline by converting hotspot analysis results into a structured and easy-to-understand report.

The generated `hotspot_summary.csv` provides a standardized dataset that can be used in the upcoming visualization, dashboard, and final reporting stages of GeoPulse.
