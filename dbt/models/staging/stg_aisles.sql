SELECT
aisle_id,
aisle
FROM {{ source('raw', 'aisles')}}
