{{ config(
    materialized='view',
    schema='STAGING',
    tags=['staging', 'gps', 'geopulse']
) }}

WITH source_data AS (

    SELECT
        device_id,
        latitude,
        longitude,
        timestamp AS event_timestamp,
        accuracy,
        speed,
        altitude,
        battery_level,
        device_type
    FROM {{ source('raw', 'RAW_GPS_POINTS') }}

),

cleaned_data AS (

    SELECT
        TRIM(device_id) AS device_id,

        TRY_TO_DECIMAL(latitude, 10, 7) AS latitude,

        TRY_TO_DECIMAL(longitude, 10, 7) AS longitude,

        TRY_TO_TIMESTAMP_NTZ(event_timestamp) AS event_timestamp,

        TRY_TO_DECIMAL(accuracy, 10, 2) AS accuracy_meters,

        TRY_TO_DECIMAL(speed, 10, 2) AS speed_kmh,

        TRY_TO_DECIMAL(altitude, 10, 2) AS altitude_meters,

        TRY_TO_NUMBER(battery_level) AS battery_level,

        UPPER(TRIM(device_type)) AS device_type

    FROM source_data

),

validated_data AS (

    SELECT
        device_id,
        latitude,
        longitude,
        event_timestamp,
        accuracy_meters,
        speed_kmh,
        altitude_meters,
        battery_level,
        device_type,

        /* Validate latitude */
        CASE
            WHEN latitude BETWEEN -90 AND 90
            THEN TRUE
            ELSE FALSE
        END AS is_valid_latitude,

        /* Validate longitude */
        CASE
            WHEN longitude BETWEEN -180 AND 180
            THEN TRUE
            ELSE FALSE
        END AS is_valid_longitude,

        /* Validate GPS accuracy */
        CASE
            WHEN accuracy_meters IS NULL
                OR accuracy_meters >= 0
            THEN TRUE
            ELSE FALSE
        END AS is_valid_accuracy,

        /* Validate timestamp */
        CASE
            WHEN event_timestamp IS NOT NULL
            THEN TRUE
            ELSE FALSE
        END AS is_valid_timestamp,

        /* Validate device */
        CASE
            WHEN device_id IS NOT NULL
                AND device_id != ''
            THEN TRUE
            ELSE FALSE
        END AS is_valid_device

    FROM cleaned_data

),

filtered_data AS (

    SELECT *
    FROM validated_data

    WHERE is_valid_latitude = TRUE
      AND is_valid_longitude = TRUE
      AND is_valid_timestamp = TRUE
      AND is_valid_device = TRUE

),

deduplicated_data AS (

    SELECT
        *,
        ROW_NUMBER() OVER (
            PARTITION BY
                device_id,
                latitude,
                longitude,
                event_timestamp
            ORDER BY event_timestamp
        ) AS record_rank

    FROM filtered_data

),

final_data AS (

    SELECT
        device_id,

        latitude,

        longitude,

        event_timestamp,

        DATE(event_timestamp) AS event_date,

        EXTRACT(
            HOUR FROM event_timestamp
        ) AS event_hour,

        EXTRACT(
            MINUTE FROM event_timestamp
        ) AS event_minute,

        DAYOFWEEK(event_timestamp) AS day_of_week,

        DAYNAME(event_timestamp) AS day_name,

        MONTH(event_timestamp) AS event_month,

        YEAR(event_timestamp) AS event_year,

        accuracy_meters,

        speed_kmh,

        altitude_meters,

        battery_level,

        device_type,

        /* Quality classification */

        CASE
            WHEN accuracy_meters IS NULL
                THEN 'UNKNOWN'

            WHEN accuracy_meters <= 10
                THEN 'HIGH'

            WHEN accuracy_meters <= 50
                THEN 'MEDIUM'

            ELSE 'LOW'
        END AS gps_quality,

        /* Time-of-day classification */

        CASE
            WHEN event_hour BETWEEN 6 AND 11
                THEN 'MORNING'

            WHEN event_hour BETWEEN 12 AND 16
                THEN 'AFTERNOON'

            WHEN event_hour BETWEEN 17 AND 21
                THEN 'EVENING'

            ELSE 'NIGHT'
        END AS time_period,

        /* Speed classification */

        CASE
            WHEN speed_kmh IS NULL
                THEN 'UNKNOWN'

            WHEN speed_kmh = 0
                THEN 'STATIONARY'

            WHEN speed_kmh < 5
                THEN 'WALKING'

            WHEN speed_kmh < 20
                THEN 'CYCLING'

            WHEN speed_kmh < 60
                THEN 'DRIVING'

            ELSE 'HIGH_SPEED'
        END AS movement_type,

        /* Data quality flag */

        CASE
            WHEN accuracy_meters IS NULL
                THEN 'REVIEW'

            WHEN accuracy_meters <= 50
                THEN 'VALID'

            ELSE 'LOW_ACCURACY'
        END AS data_quality,

        CURRENT_TIMESTAMP() AS dbt_processed_at

    FROM deduplicated_data

    WHERE record_rank = 1

)

SELECT
    device_id,
    latitude,
    longitude,
    event_timestamp,

    event_date,
    event_hour,
    event_minute,
    day_of_week,
    day_name,
    event_month,
    event_year,

    accuracy_meters,
    gps_quality,

    speed_kmh,
    movement_type,

    altitude_meters,
    battery_level,
    device_type,

    time_period,
    data_quality,

    dbt_processed_at

FROM final_data
