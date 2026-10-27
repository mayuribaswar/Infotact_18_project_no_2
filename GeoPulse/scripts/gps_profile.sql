USE DATABASE GEOPULSE;
USE SCHEMA RAW;


-- GPS dataset overview
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


-- Speed statistics
SELECT
    MIN(speed) AS minimum_speed,
    MAX(speed) AS maximum_speed,
    AVG(speed) AS average_speed,
    MEDIAN(speed) AS median_speed
FROM GPS_RAW;


-- Accuracy statistics
SELECT
    MIN(accuracy) AS minimum_accuracy,
    MAX(accuracy) AS maximum_accuracy,
    AVG(accuracy) AS average_accuracy,
    MEDIAN(accuracy) AS median_accuracy
FROM GPS_RAW;