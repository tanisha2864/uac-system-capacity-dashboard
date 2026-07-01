import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# TITLE
st.title("Factory-to-Customer Shipping Route Efficiency Dashboard")

# LOAD DATA
df = pd.read_csv("Nassau Candy Distributor.csv")

# KPI SECTION
st.subheader("KPI Summary")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average Lead Time",
    round(df['Lead Time'].mean(),2)
)

col2.metric(
    "Maximum Lead Time",
    round(df['Lead Time'].max(),2)
)

col3.metric(
    "Total Routes",
    df['Route'].nunique()
)

# LEAD TIME DISTRIBUTION
st.subheader("Lead Time Distribution")

fig, ax = plt.subplots(figsize=(10,5))

ax.hist(df['Lead Time'])

ax.grid(True)

st.pyplot(fig)

# TOP DELAY ROUTES
st.subheader("Top Delay Routes")

top_routes = (
    df.groupby('Route')['Delay']
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

fig, ax = plt.subplots(figsize=(12,5))

ax.bar(
    top_routes.index,
    top_routes.values
)

plt.xticks(rotation=90)

ax.set_ylabel("Delay Percentage")

st.pyplot(fig)

# DATA PREVIEW
st.subheader("Dataset Preview")

st.dataframe(df.head(20))
