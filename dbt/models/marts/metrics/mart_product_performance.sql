-- mart_product_performance.sql
SELECT
    product_id,
    department_id,
    aisle_id,
    SUM(reordered) as total_reorders,
    AVG(reordered) as reorder_rate,
    COUNT(DISTINCT user_id) as unique_customers,
    AVG(add_to_cart_order) as avg_cart_position
FROM {{ ref('int_order_items') }}
GROUP BY product_id, department_id, aisle_id