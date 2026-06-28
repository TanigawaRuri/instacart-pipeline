SELECT
    user_id,
    order_number,
    COUNT(*) as cnt
FROM {{ ref('stg_orders') }}
GROUP BY user_id, order_number
HAVING cnt > 1