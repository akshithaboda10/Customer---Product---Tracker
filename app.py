import streamlit as st
import pandas as pd

# Title of the Dashboard
st.title("🛒 Customer Product Tracker")

# Load CSV data
df = pd.read_csv("VSD_purchases.csv")
st.write("Column Names:", df.columns.tolist())


# Show raw data
st.subheader("📄 Raw Purchase Data")
st.dataframe(df)

# Summary
st.subheader("📊 Summary")

# Unique customers
st.write(f"Total Customers: {df['Customer Name'].nunique()}")

# Total quantity sold
st.write(f"Total Quantity Sold: {df['Quantity'].sum()}")

# Most common tyre size
most_common_tyre = df['Tyre Size'].mode()[0]
st.write(f"Most Popular Tyre Size: {most_common_tyre}")
