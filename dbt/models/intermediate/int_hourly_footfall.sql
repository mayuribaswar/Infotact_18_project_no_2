WITH hourly_data AS (

    SELECT
        device_id,
        DATE_TRUNC('hour', timestamp) AS visit_hour,
        latitude,
        longitude

    FROM {{ ref('stg_gps_points') }}

)

SELECT
    visit_hour,
    COUNT(DISTINCT device_id) AS unique_visitors,
    COUNT(*) AS total_gps_points

FROM hourly_data

GROUP BY visit_hour
ORDER BY visit_hour;
