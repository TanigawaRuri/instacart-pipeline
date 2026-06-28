SELECT product_id
FROM {{ ref('stg_products') }}
WHERE product_name IS NULL
   OR TRIM(product_name) = ''