# 🛒 Instacart Data Pipeline

## Overview
End-to-end data pipeline built with Snowflake, dbt, Airflow, and Streamlit
using the Instacart Market Basket Analysis dataset (3.2M orders).

## Architecture
<img width="850" height="723" alt="lineage graph" src="https://github.com/user-attachments/assets/bb213460-0a5f-493a-a1b2-abcbb0b6e651" />

raw data → Snowflake → dbt (staging/intermediate/mart) → Airflow → Streamlit

## Tech Stack
| Layer | Tool |
|-------|------|
| Data Warehouse | Snowflake |
| Transformation | dbt |
| Orchestration | Apache Airflow |
| Dashboard | Streamlit |

## Data Model
### Staging
- stg_orders, stg_order_products, stg_products, stg_aisles, stg_departments

### Intermediate
- int_order_items (JOIN layer)

### Marts
- mart_customer_retention
- mart_product_performance
- mart_basket_analysis
- mart_hourly_patterns

## Data Quality
- 41 dbt tests (unique, not_null, relationships, accepted_values)
- 4 custom singular tests (duplicate detection, orphan products, null checks)

## Dashboard
https://instacart-pipeline-wryewkn48dzooxbb6wqv6d.streamlit.app/

## Limitations
- No timestamp columns in source data → active_months metric omitted
