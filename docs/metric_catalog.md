# Metric Catalog

## Customer Metrics

| Metric | Formula | Model | Description |
|--------|---------|-------|-------------|
| total_orders | COUNT(DISTINCT order_id) | mart_customer_retention | Total orders per customer |
| avg_days_between_orders | AVG(days_since_prior_order) | mart_customer_retention | Average order interval |
| total_products_bought | COUNT(product_id) | mart_customer_retention | Lifetime products purchased |
| reorder_rate | AVG(reordered) | mart_customer_retention | Proportion of reordered items |

## Product Metrics

| Metric | Formula | Model | Description |
|--------|---------|-------|-------------|
| total_reorders | SUM(reordered) | mart_product_performance | Total reorder count |
| reorder_rate | AVG(reordered) | mart_product_performance | Reorder proportion |
| unique_customers | COUNT(DISTINCT user_id) | mart_product_performance | Distinct buyers |
| avg_cart_position | AVG(add_to_cart_order) | mart_product_performance | Average basket sequence |

## Basket Metrics

| Metric | Formula | Model | Description |
|--------|---------|-------|-------------|
| avg_basket_size | AVG(COUNT(product_id) per order) | mart_basket_analysis | Average items per order |
| avg_unique_departments | AVG(COUNT(DISTINCT department_id) per order) | mart_basket_analysis | Category diversity per order |
| avg_reorder_ratio | AVG(AVG(reordered) per order) | mart_basket_analysis | Reorder proportion per basket |

## Hourly Metrics

| Metric | Formula | Model | Description |
|--------|---------|-------|-------------|
| order_count | COUNT(DISTINCT order_id) | mart_hourly_patterns | Orders per time slot |
| total_items | COUNT(product_id) | mart_hourly_patterns | Items per time slot |

## Limitations
- No absolute timestamps → date-based metrics unavailable
- days_since_prior_order is self-reported → may contain nulls for first orders
