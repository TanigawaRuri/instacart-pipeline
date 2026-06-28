import streamlit as st
import snowflake.connector
import pandas as pd
import plotly.express as px
from cryptography.hazmat.primitives.serialization import load_der_private_key
import base64

st.set_page_config(
    page_title="Instacart Analytics",
    page_icon="🛒",
    layout="wide"
)

@st.cache_resource
def get_connection():
    private_key_bytes = base64.b64decode(st.secrets["snowflake"]["private_key"])
    private_key = load_der_private_key(private_key_bytes, password=None)
    
    return snowflake.connector.connect(
        account=st.secrets["snowflake"]["account"],
        user=st.secrets["snowflake"]["user"],
        private_key=private_key,
        database=st.secrets["snowflake"]["database"],
        warehouse=st.secrets["snowflake"]["warehouse"],
        role=st.secrets["snowflake"]["role"]
    )

@st.cache_data
def load_data(query):
    conn = get_connection()
    return pd.read_sql(query, conn)

st.title("🛒 Instacart Analytics Dashboard")
st.markdown("---")

st.header("1. Customer Retention")
df_customer = load_data("SELECT * FROM INSTACART.MARTS.MART_CUSTOMER_RETENTION")

col1, col2, col3 = st.columns(3)
col1.metric("Total Customers", f"{len(df_customer):,}")
col2.metric("Avg Orders per Customer", f"{df_customer['TOTAL_ORDERS'].mean():.1f}")
col3.metric("Avg Reorder Rate", f"{df_customer['REORDER_RATE'].mean():.1%}")

fig1 = px.histogram(df_customer, x="TOTAL_ORDERS", nbins=50,
                    title="Distribution of Orders per Customer")
st.plotly_chart(fig1, use_container_width=True)

st.header("2. Product Performance")
df_product = load_data("""
    SELECT p.PRODUCT_NAME, m.TOTAL_REORDERS, m.REORDER_RATE, m.UNIQUE_CUSTOMERS
    FROM INSTACART.MARTS.MART_PRODUCT_PERFORMANCE m
    JOIN INSTACART.MARTS.DIM_PRODUCT p ON m.PRODUCT_ID = p.PRODUCT_ID
    ORDER BY m.TOTAL_REORDERS DESC
    LIMIT 20
""")

fig2 = px.bar(df_product, x="PRODUCT_NAME", y="TOTAL_REORDERS",
              title="Top 20 Products by Reorders",
              color="REORDER_RATE", color_continuous_scale="Blues")
fig2.update_xaxes(tickangle=45)
st.plotly_chart(fig2, use_container_width=True)

st.header("3. Basket Analysis")
df_basket = load_data("SELECT * FROM INSTACART.MARTS.MART_BASKET_ANALYSIS")

col1, col2, col3 = st.columns(3)
col1.metric("Avg Basket Size", f"{df_basket['AVG_BASKET_SIZE'].values[0]:.1f} items")
col2.metric("Avg Unique Departments", f"{df_basket['AVG_UNIQUE_DEPARTMENTS'].values[0]:.1f}")
col3.metric("Avg Reorder Ratio", f"{df_basket['AVG_IN_BASKET'].values[0]:.1%}")

st.header("4. Hourly Patterns")
df_hourly = load_data("SELECT * FROM INSTACART.MARTS.MART_HOURLY_PATTERNS ORDER BY ORDER_DAY_OF_WEEK, ORDER_HOUR")

day_map = {0: "Sun", 1: "Mon", 2: "Tue", 3: "Wed", 4: "Thu", 5: "Fri", 6: "Sat"}
df_hourly["DAY"] = df_hourly["ORDER_DAY_OF_WEEK"].map(day_map)

fig4 = px.density_heatmap(df_hourly, x="ORDER_HOUR", y="DAY",
                           z="ORDER_COUNT", title="Order Heatmap by Day & Hour",
                           color_continuous_scale="Blues")
st.plotly_chart(fig4, use_container_width=True)