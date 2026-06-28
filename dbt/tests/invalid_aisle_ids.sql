SELECT DISTINCT p.aisle_id
FROM {{ ref('stg_products') }} p
LEFT JOIN {{ ref('stg_aisles') }} a
    ON p.aisle_id = a.aisle_id
WHERE a.aisle_id IS NULL