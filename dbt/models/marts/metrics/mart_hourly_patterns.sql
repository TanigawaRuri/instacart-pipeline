SELECT 
    ORDER_DAY_OF_WEEK,
    ORDER_HOUR,
    COUNT(DISTINCT(order_id)) as order_count,
    COUNT(PRODUCT_ID) as total_items
FROM {{ ref('int_order_items')}}
GROUP BY ORDER_HOUR, ORDER_DAY_OF_WEEK