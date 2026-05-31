
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Demand Forecasting Dashboard")

df = pd.read_csv("sales.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Sales Trend")

fig, ax = plt.subplots()
ax.plot(df['Date'], df['Sales'])
plt.xticks(rotation=45)

st.pyplot(fig)

st.subheader("Summary Metrics")

st.write("Total Sales:", df['Sales'].sum())
st.write("Average Sales:", df['Sales'].mean())
st.write("Maximum Sales:", df['Sales'].max())
