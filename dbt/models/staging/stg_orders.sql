SELECT 
order_id,
user_id,
order_number,
order_dow as order_day_of_week,
order_hour_of_day as order_hour,
days_since_prior_order
FROM {{ source('raw', 'orders') }}