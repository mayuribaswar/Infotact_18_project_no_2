{{ config(
    materialized='view',
    schema='STAGING'
) }}

WITH source_data AS (

    SELECT
        store_id,
        store_name,
        latitude,
        longitude,
        store_type
    FROM {{ source('raw', 'stores') }}

),

cleaned_data AS (

    SELECT
        TRIM(store_id) AS store_id,

        TRIM(store_name) AS store_name,

        CAST(latitude AS FLOAT) AS latitude,

        CAST(longitude AS FLOAT) AS longitude,

        TRIM(store_type) AS store_type

    FROM source_data

    WHERE store_id IS NOT NULL
      AND store_name IS NOT NULL
      AND latitude IS NOT NULL
      AND longitude IS NOT NULL

),

validated_data AS (

    SELECT
        store_id,
        store_name,
        latitude,
        longitude,
        store_type,

        CASE
            WHEN latitude BETWEEN -90 AND 90
             AND longitude BETWEEN -180 AND 180
            THEN TRUE
            ELSE FALSE
        END AS is_valid_coordinate

    FROM cleaned_data

)

SELECT
    store_id,
    store_name,
    latitude,
    longitude,
    store_type,
    is_valid_coordinate

FROM validated_data

WHERE is_valid_coordinate = TRUE
