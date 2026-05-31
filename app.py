
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Demand Forecasting Dashboard")

df = pd.read_csv("sales_sample.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Sales Trend")

fig, ax = plt.subplots(figsize=(10,5))
ax.plot(df['date'], df['quantity'])
ax.set_title('Demand Trend')
ax.set_xlabel('Date')
ax.set_ylabel('Quantity Sold')

st.pyplot(fig)

st.subheader("Summary Metrics")

st.write("Total Quantity Sold:", df['quantity'].sum())
st.write("Average Quantity Sold:", df['quantity'].mean())
st.write("Maximum Quantity Sold:", df['quantity'].max())
import streamlit as st

st.write(df.columns)
import streamlit as st
import pandas as pd

df = pd.read_csv("sales_sample.csv")  # or your file name

st.write("Column Names:")
st.write(list(df.columns))

st.dataframe(df.head())
