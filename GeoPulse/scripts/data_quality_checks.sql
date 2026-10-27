USE DATABASE GEOPULSE;
USE SCHEMA RAW;


-- 1. Check zero-speed records
SELECT COUNT(*) AS stopped_records
FROM GPS_RAW
WHERE speed = 0;


-- 2. Check unusually high speed
SELECT *
FROM GPS_RAW
WHERE speed > 120
ORDER BY speed DESC;


-- 3. Check poor GPS accuracy
SELECT *
FROM GPS_RAW
WHERE accuracy > 100
ORDER BY accuracy DESC;


-- 4. Check same device records
SELECT
    device_id,
    COUNT(*) AS total_records
FROM GPS_RAW
GROUP BY device_id
ORDER BY total_records DESC;


-- 5. Check earliest and latest timestamp
SELECT
    MIN(timestamp) AS earliest_timestamp,
    MAX(timestamp) AS latest_timestamp
FROM GPS_RAW;


-- 6. Check records by date
SELECT
    DATE(timestamp) AS record_date,
    COUNT(*) AS record_count
FROM GPS_RAW
GROUP BY DATE(timestamp)
ORDER BY record_date;


-- 7. Check records by hour
SELECT
    EXTRACT(HOUR FROM timestamp) AS record_hour,
    COUNT(*) AS record_count
FROM GPS_RAW
GROUP BY EXTRACT(HOUR FROM timestamp)
ORDER BY record_hour;


-- 8. Check devices with very few records
SELECT
    device_id,
    COUNT(*) AS record_count
FROM GPS_RAW
GROUP BY device_id
HAVING COUNT(*) < 5
ORDER BY record_count;


-- 9. Check devices with many records
SELECT
    device_id,
    COUNT(*) AS record_count
FROM GPS_RAW
GROUP BY device_id
HAVING COUNT(*) > 1000
ORDER BY record_count DESC;