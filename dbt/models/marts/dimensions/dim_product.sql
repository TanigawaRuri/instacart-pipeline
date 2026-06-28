SELECT 
product_id,
product_name,
department_id,
aisle_id
FROM {{ ref('stg_products')}}