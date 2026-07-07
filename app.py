import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="UAC System Capacity Dashboard",
    layout="wide"
)

st.title("UAC System Capacity & Care Load Dashboard")

# -------------------------------------------------
# Load Dataset
# -------------------------------------------------
df = pd.read_csv("final_uac_analysis.csv")

# -------------------------------------------------
# Convert Date
# -------------------------------------------------
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Remove empty dates
df = df.dropna(subset=["Date"])

# Sort by date
df = df.sort_values("Date")

# -------------------------------------------------
# KPI Summary
# -------------------------------------------------
st.header("KPI Summary")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Average System Load",
    f"{df['Total System Load'].mean():,.2f}"
)

col2.metric(
    "Maximum System Load",
    f"{df['Total System Load'].max():,.0f}"
)

col3.metric(
    "Average Net Intake",
    f"{df['Net Intake Pressure'].mean():,.2f}"
)

# -------------------------------------------------
# Total System Load
# -------------------------------------------------
st.subheader("Total System Load")

fig1, ax1 = plt.subplots(figsize=(12,5))

ax1.plot(
    df["Date"],
    df["Total System Load"],
    color="blue",
    linewidth=2
)

ax1.set_xlabel("Date")
ax1.set_ylabel("Total System Load")
ax1.grid(True)

st.pyplot(fig1)

# -------------------------------------------------
# Net Intake Pressure
# -------------------------------------------------
st.subheader("Net Intake Pressure")

fig2, ax2 = plt.subplots(figsize=(12,5))

ax2.plot(
    df["Date"],
    df["Net Intake Pressure"],
    color="green"
)

ax2.axhline(0, linestyle="--", color="red")

ax2.set_xlabel("Date")
ax2.set_ylabel("Net Intake Pressure")
ax2.grid(True)

st.pyplot(fig2)

# -------------------------------------------------
# 7-Day Average Load
# -------------------------------------------------
st.subheader("7-Day Average Load")

fig3, ax3 = plt.subplots(figsize=(12,5))

ax3.plot(
    df["Date"],
    df["7-Day Avg Load"],
    color="orange",
    linewidth=2
)

ax3.set_xlabel("Date")
ax3.set_ylabel("7-Day Average Load")
ax3.grid(True)

st.pyplot(fig3)

# -------------------------------------------------
# CBP vs HHS Care Load
# -------------------------------------------------
st.subheader("CBP vs HHS Care Load")

fig4, ax4 = plt.subplots(figsize=(12,5))

ax4.plot(
    df["Date"],
    df["Children in CBP custody"],
    label="CBP Custody",
    linewidth=2
)

ax4.plot(
    df["Date"],
    df["Children in HHS Care"],
    label="HHS Care",
    linewidth=2
)

ax4.set_xlabel("Date")
ax4.set_ylabel("Children")
ax4.legend()
ax4.grid(True)

st.pyplot(fig4)

# -------------------------------------------------
# Dataset Preview
# -------------------------------------------------
st.subheader("Dataset Preview")

st.dataframe(df)

# -------------------------------------------------
# Download Button
# -------------------------------------------------
csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Processed Dataset",
    data=csv,
    file_name="final_uac_analysis.csv",
    mime="text/csv"
)
