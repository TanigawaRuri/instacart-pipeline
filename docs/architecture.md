┌─────────────────────────────────────────────────────────┐

│                     Data Sources                         │

│              Instacart CSV (Kaggle)                      │

│     orders / order_products / products / aisles /        │

│                    departments                           │

└─────────────────────┬───────────────────────────────────┘

│ Python scripts/load_csv.py

▼

┌─────────────────────────────────────────────────────────┐

│                  Snowflake RAW Schema                    │

│   ORDERS / ORDER_PRODUCTS / PRODUCTS / AISLES /          │

│                  DEPARTMENTS                             │

└─────────────────────┬───────────────────────────────────┘

│ dbt

▼

┌─────────────────────────────────────────────────────────┐

│               dbt Staging Layer (Views)                  │

│   stg_orders / stg_order_products / stg_products /       │

│              stg_aisles / stg_departments                │

└─────────────────────┬───────────────────────────────────┘

│ dbt

▼

┌─────────────────────────────────────────────────────────┐

│            dbt Intermediate Layer (Views)                │

│                  int_order_items                         │

│        (orders + products + aisles + departments)        │

└──────┬──────────────┬──────────────┬────────────────────┘

│              │              │

▼              ▼              ▼

┌────────────┐ ┌────────────┐ ┌────────────────────────────┐

│ Dimensions │ │   Facts    │ │         Metrics             │

│ dim_product│ │fact_orders │ │ mart_customer_retention     │

│ dim_aisle  │ │fact_order_ │ │ mart_product_performance    │

│ dim_depart │ │   items    │ │ mart_basket_analysis        │

└────────────┘ └────────────┘ │ mart_hourly_patterns        │

└────────────────────────────┘

│

│ Apache Airflow (@daily)

│ dbt run → dbt test → dbt docs

▼

┌─────────────────────────────────────────────────────────┐

│                  Streamlit Dashboard                     │

│   Customer Retention / Product Performance /             │

│         Basket Analysis / Hourly Patterns                │

└─────────────────────────────────────────────────────────┘
## Component Details

| Component | Role |
|-----------|------|
| Snowflake | Cloud Data Warehouse |
| dbt | Transformation + Testing + Documentation |
| Airflow | Orchestration (daily batch) |
| Streamlit | Business Intelligence Dashboard |

## Data Flow
1. CSV files loaded into Snowflake RAW schema via Python
2. dbt staging models clean and rename raw columns
3. dbt intermediate model joins staging tables
4. dbt mart models aggregate metrics for business use
5. Airflow DAG orchestrates daily pipeline execution
6. Streamlit reads from mart tables for visualization
