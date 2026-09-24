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
