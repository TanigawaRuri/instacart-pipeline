SELECT
order_id,
product_id,
add_to_cart_order,
reordered
FROM {{ source('raw', 'order_products')}}