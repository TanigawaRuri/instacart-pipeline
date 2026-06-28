SELECT DISTINCT op.product_id
FROM {{ ref('stg_order_products') }} op
LEFT JOIN {{ ref('stg_products') }} p
    ON op.product_id = p.product_id
WHERE p.product_id IS NULL