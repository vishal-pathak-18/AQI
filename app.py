import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(page_title="Air Quality Dashboard", layout="wide")

# Title
st.title("🌍 Air Quality Index (AQI) Dashboard")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("AQI-and-Lat-Long-of-Countries (1).csv")
    return df

df = load_data()

# Show raw data
st.subheader("📄 Dataset Preview")
st.dataframe(df.head())

# Basic statistics
st.subheader("📊 Descriptive Statistics")
st.write(df.describe())

# Sidebar filters
st.sidebar.header("Filters")

aqi_range = st.sidebar.slider(
    "Select AQI Value Range",
    int(df["AQI Value"].min()),
    int(df["AQI Value"].max()),
    (0, 150)
)

filtered_df = df[
    (df["AQI Value"] >= aqi_range[0]) &
    (df["AQI Value"] <= aqi_range[1])
]

st.subheader("Filtered Data")
st.dataframe(filtered_df)

# Map visualization
st.subheader("🗺️ AQI Locations on Map")

map_df = filtered_df.rename(
    columns={"lat": "latitude", "lng": "longitude"}
)

st.map(map_df)

# AQI distribution plot
st.subheader("📈 AQI Distribution")

fig, ax = plt.subplots()
ax.hist(filtered_df["AQI Value"], bins=20)
ax.set_xlabel("AQI Value")
ax.set_ylabel("Frequency")

st.pyplot(fig)
