WITH basket AS (
    SELECT 
        order_id,
        COUNT(product_id) as basket_size,
        COUNT(DISTINCT(department_id)) as unique_departments,
        AVG(reordered) as cnt_in_basket
    FROM {{ ref('int_order_items')}}
    GROUP BY order_id
)

SELECT 
    AVG(basket_size) as avg_basket_size,
    AVG(unique_departments) as avg_unique_departments,
    AVG(cnt_in_basket) as avg_in_basket
FROM basket