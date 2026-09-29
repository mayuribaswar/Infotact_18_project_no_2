-- ============================================
-- GeoPulse - Snowflake RAW Table
-- ============================================

USE DATABASE GEOPULSE;
USE SCHEMA RAW;

CREATE TABLE IF NOT EXISTS GPS_RAW (
    device_id VARCHAR(50),
    timestamp TIMESTAMP,
    latitude FLOAT,
    longitude FLOAT,
    speed FLOAT,
    accuracy FLOAT
);