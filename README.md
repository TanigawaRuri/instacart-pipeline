# 🛒 Instacart Data Pipeline

## Overview
End-to-end data pipeline built with Snowflake, dbt, Airflow, and Streamlit
using the Instacart Market Basket Analysis dataset (3.2M orders, 15M order-product rows).

## Architecture
<img width="850" height="723" alt="lineage graph" src="https://github.com/user-attachments/assets/bb213460-0a5f-493a-a1b2-abcbb0b6e651" />

## Tech Stack
| Layer | Tool |
|-------|------|
| Data Warehouse | Snowflake |
| Transformation | dbt 1.11 |
| Orchestration | Apache Airflow 2.9 |
| Dashboard | Streamlit |
| Language | Python, SQL |

## Data Model

### Staging (Views)
Raw data cleaning and column renaming
- `stg_orders` — order metadata
- `stg_order_products` — order-product mapping
- `stg_products` — product master
- `stg_aisles` — aisle master
- `stg_departments` — department master

### Intermediate (Views)
Multi-table JOIN for reuse across marts
- `int_order_items` — orders + products + departments + aisles

### Marts (Tables)

**Dimensions**
- `dim_product` — product attributes
- `dim_aisle` — aisle attributes
- `dim_department` — department attributes

**Facts**
- `fact_orders` — order-level fact table
- `fact_order_items` — order-product fact table

**Metrics**
- `mart_customer_retention` — customer reorder behavior
- `mart_product_performance` — product reorder metrics
- `mart_basket_analysis` — basket size and composition
- `mart_hourly_patterns` — order timing heatmap

## Data Quality
- **41 dbt tests** — unique, not_null, relationships, accepted_values
- **4 custom singular tests**
  - `duplicate_order_detection` — same user + order_number combination
  - `orphan_products` — order_products without matching product
  - `null_product_names` — empty or null product names
  - `invalid_aisle_ids` — aisle_id not in stg_aisles

## Pipeline Orchestration
Airflow DAG runs daily:

## Dashboard
🔗 [Live Dashboard](https://instacart-pipeline-wryewkn48dzooxbb6wqv6d.streamlit.app/)

## Limitations
- No timestamp columns in source data → `active_months` metric omitted
- `days_since_prior_order` used as proxy for order interval analysis