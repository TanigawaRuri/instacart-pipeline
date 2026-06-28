# Data Dictionary

## Staging Layer

### stg_orders
| Column | Type | Description |
|--------|------|-------------|
| order_id | INTEGER | Unique order identifier |
| user_id | INTEGER | Unique user identifier |
| order_number | INTEGER | Sequence of orders per user |
| order_day_of_week | INTEGER | Day of week (0=Sunday, 6=Saturday) |
| order_hour | INTEGER | Hour of day (0-23) |
| days_since_prior_order | FLOAT | Days since previous order |

### stg_order_products
| Column | Type | Description |
|--------|------|-------------|
| order_id | INTEGER | Foreign key to stg_orders |
| product_id | INTEGER | Foreign key to stg_products |
| add_to_cart_order | INTEGER | Sequence within basket |
| reordered | INTEGER | 1 if repeat purchase, 0 if first time |

### stg_products
| Column | Type | Description |
|--------|------|-------------|
| product_id | INTEGER | Unique product identifier |
| product_name | VARCHAR | Product display name |
| aisle_id | INTEGER | Foreign key to stg_aisles |
| department_id | INTEGER | Foreign key to stg_departments |

### stg_aisles
| Column | Type | Description |
|--------|------|-------------|
| aisle_id | INTEGER | Unique aisle identifier |
| aisle | VARCHAR | Aisle name |

### stg_departments
| Column | Type | Description |
|--------|------|-------------|
| department_id | INTEGER | Unique department identifier |
| department | VARCHAR | Department name |

## Intermediate Layer

### int_order_items
| Column | Type | Description |
|--------|------|-------------|
| order_id | INTEGER | Unique order identifier |
| user_id | INTEGER | Unique user identifier |
| order_number | INTEGER | Sequence of orders per user |
| order_day_of_week | INTEGER | Day of week |
| order_hour | INTEGER | Hour of day |
| days_since_prior_order | FLOAT | Days since previous order |
| product_id | INTEGER | Unique product identifier |
| add_to_cart_order | INTEGER | Sequence within basket |
| reordered | INTEGER | Repeat purchase flag |
| product_name | VARCHAR | Product display name |
| department_id | INTEGER | Department identifier |
| aisle_id | INTEGER | Aisle identifier |

## Marts Layer

### fact_orders
| Column | Type | Description |
|--------|------|-------------|
| order_id | INTEGER | Unique order identifier (PK) |
| user_id | INTEGER | User identifier |
| order_number | INTEGER | Sequence of orders per user |
| order_day_of_week | INTEGER | Day of week |
| order_hour | INTEGER | Hour of day |
| days_since_prior_order | FLOAT | Days since previous order |

### fact_order_items
| Column | Type | Description |
|--------|------|-------------|
| order_id | INTEGER | Foreign key to fact_orders |
| product_id | INTEGER | Foreign key to dim_product |
| add_to_cart_order | INTEGER | Sequence within basket |
| reordered | INTEGER | Repeat purchase flag |

### dim_product
| Column | Type | Description |
|--------|------|-------------|
| product_id | INTEGER | Unique product identifier (PK) |
| product_name | VARCHAR | Product display name |
| aisle_id | INTEGER | Foreign key to dim_aisle |
| department_id | INTEGER | Foreign key to dim_department |

### mart_customer_retention
| Column | Type | Description |
|--------|------|-------------|
| customer_id | INTEGER | Unique user identifier |
| total_orders | INTEGER | Total distinct orders |
| avg_days_between_orders | FLOAT | Average order interval in days |
| total_products_bought | INTEGER | Total products purchased |
| reorder_rate | FLOAT | Proportion of reordered items |

### mart_product_performance
| Column | Type | Description |
|--------|------|-------------|
| product_id | INTEGER | Unique product identifier |
| department_id | INTEGER | Department identifier |
| aisle_id | INTEGER | Aisle identifier |
| total_reorders | INTEGER | Total reorder count |
| reorder_rate | FLOAT | Proportion of reordered purchases |
| unique_customers | INTEGER | Distinct customers who bought |
| avg_cart_position | FLOAT | Average add-to-cart sequence |

### mart_basket_analysis
| Column | Type | Description |
|--------|------|-------------|
| avg_basket_size | FLOAT | Average items per order |
| avg_unique_departments | FLOAT | Average departments per order |
| avg_reorder_ratio | FLOAT | Average reorder proportion per order |

### mart_hourly_patterns
| Column | Type | Description |
|--------|------|-------------|
| order_day_of_week | INTEGER | Day of week (0=Sunday) |
| order_hour | INTEGER | Hour of day (0-23) |
| order_count | INTEGER | Distinct orders in this slot |
| total_items | INTEGER | Total items ordered in this slot |
