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
