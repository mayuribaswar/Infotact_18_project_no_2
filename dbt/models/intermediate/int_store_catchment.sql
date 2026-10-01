{{ config(
    materialized='table'
) }}

WITH catchment_data AS (

    SELECT
        store_id,
        store_name,
        latitude,
        longitude,
        store_type,
        catchment_radius_meters,
        catchment_geometry,
        created_at

    FROM {{ ref('stg_stores') }}

),

catchment_analytics AS (

    SELECT
        store_id,
        store_name,
        store_type,
        latitude,
        longitude,

        -- Standard catchment radius
        COALESCE(
            catchment_radius_meters,
            500
        ) AS catchment_radius_meters,

        catchment_geometry,
        created_at

    FROM catchment_data

    WHERE store_id IS NOT NULL
      AND latitude IS NOT NULL
      AND longitude IS NOT NULL

)

SELECT
    store_id,
    store_name,
    store_type,
    latitude,
    longitude,
    catchment_radius_meters,
    catchment_geometry,
    created_at

FROM catchment_analytics
