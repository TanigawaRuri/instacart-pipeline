SELECT 
    user_id as customer_id,
    count(distinct(order_id)) as total_orders,
    avg(days_since_prior_order) as avg_days_between_orders,
    count(product_id) as total_products_bought,
    AVG(reordered) as reorder_rate
FROM {{ ref('int_order_items')}}
GROUP BY user_id