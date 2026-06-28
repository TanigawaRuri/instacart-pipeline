SELECT
    op.order_id,
    o.user_id,
    o.order_number,
    o.order_day_of_week,
    o.order_hour,
    o.days_since_prior_order,
    op.product_id,
    op.add_to_cart_order,
    op.reordered,
    p.product_name,
    p.department_id,
    p.aisle_id
FROM {{ ref('stg_order_products')}} op 
LEFT JOIN {{ ref('stg_orders')}} o
    ON op.order_id = o.order_id
LEFT JOIN {{ ref('stg_products')}} p
    ON op.product_id = p.product_id