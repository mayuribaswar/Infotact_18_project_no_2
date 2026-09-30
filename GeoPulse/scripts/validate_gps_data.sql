-- ============================================
-- GeoPulse - GPS Data Validation
-- ============================================

USE DATABASE GEOPULSE;
USE SCHEMA RAW;


-- 1. Total records
SELECT COUNT(*) AS total_records
FROM GPS_RAW;


-- 2. NULL device IDs
SELECT COUNT(*) AS null_device_ids
FROM GPS_RAW
WHERE device_id IS NULL;


-- 3. NULL timestamps
SELECT COUNT(*) AS null_timestamps
FROM GPS_RAW
WHERE timestamp IS NULL;


-- 4. NULL latitude
SELECT COUNT(*) AS null_latitudes
FROM GPS_RAW
WHERE latitude IS NULL;


-- 5. NULL longitude
SELECT COUNT(*) AS null_longitudes
FROM GPS_RAW
WHERE longitude IS NULL;


-- 6. Invalid latitude
SELECT COUNT(*) AS invalid_latitudes
FROM GPS_RAW
WHERE latitude NOT BETWEEN -90 AND 90;


-- 7. Invalid longitude
SELECT COUNT(*) AS invalid_longitudes
FROM GPS_RAW
WHERE longitude NOT BETWEEN -180 AND 180;


-- 8. Negative speed
SELECT COUNT(*) AS negative_speeds
FROM GPS_RAW
WHERE speed < 0;


-- 9. Negative accuracy
SELECT COUNT(*) AS negative_accuracy
FROM GPS_RAW
WHERE accuracy < 0;


-- 10. Duplicate GPS records
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


-- 11. Show invalid GPS records
SELECT *
FROM GPS_RAW
WHERE latitude IS NULL
   OR longitude IS NULL
   OR latitude NOT BETWEEN -90 AND 90
   OR longitude NOT BETWEEN -180 AND 180
   OR speed < 0;


-- 12. GPS range summary
SELECT
    MIN(latitude) AS min_latitude,
    MAX(latitude) AS max_latitude,
    MIN(longitude) AS min_longitude,
    MAX(longitude) AS max_longitude,
    MIN(speed) AS min_speed,
    MAX(speed) AS max_speed
FROM GPS_RAW;


-- 13. Unique devices
SELECT COUNT(DISTINCT device_id) AS unique_devices
FROM GPS_RAW;


-- 14. Final validation summary
SELECT
    COUNT(*) AS total_records,
    COUNT_IF(device_id IS NULL) AS null_device_ids,
    COUNT_IF(timestamp IS NULL) AS null_timestamps,
    COUNT_IF(latitude IS NULL) AS null_latitudes,
    COUNT_IF(longitude IS NULL) AS null_longitudes,
    COUNT_IF(latitude NOT BETWEEN -90 AND 90)
        AS invalid_latitudes,
    COUNT_IF(longitude NOT BETWEEN -180 AND 180)
        AS invalid_longitudes,
    COUNT_IF(speed < 0)
        AS negative_speeds,
    COUNT_IF(accuracy < 0)
        AS negative_accuracy
FROM GPS_RAW;