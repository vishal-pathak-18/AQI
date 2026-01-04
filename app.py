import streamlit as st
import pandas as pd

# --------------------------------------------------
# Page configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Air Quality Index Dashboard",
    layout="wide"
)

# --------------------------------------------------
# Title
# --------------------------------------------------
st.title("🌍 Air Quality Index (AQI) Dashboard")

# --------------------------------------------------
# Load data
# --------------------------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("AQI-and-Lat-Long-of-Countries (1).csv")
    return df

df = load_data()

# --------------------------------------------------
# Dataset preview
# --------------------------------------------------
st.subheader("📄 Dataset Preview")
st.dataframe(df.head())

# --------------------------------------------------
# Descriptive statistics
# --------------------------------------------------
st.subheader("📊 Descriptive Statistics")
st.write(df.describe())

# --------------------------------------------------
# Sidebar filters
# --------------------------------------------------
st.sidebar.header("🔎 Filters")

aqi_min = int(df["AQI Value"].min())
aqi_max = int(df["AQI Value"].max())

aqi_range = st.sidebar.slider(
    "Select AQI Range",
    aqi_min,
    aqi_max,
    (aqi_min, aqi_max)
)

filtered_df = df[
    (df["AQI Value"] >= aqi_range[0]) &
    (df["AQI Value"] <= aqi_range[1])
]

# --------------------------------------------------
# Filtered data
# --------------------------------------------------
st.subheader("📑 Filtered Data")
st.dataframe(filtered_df)

# --------------------------------------------------
# Map visualization
# --------------------------------------------------
st.subheader("🗺️ AQI Locations on Map")

map_df = filtered_df.rename(
    columns={
        "lat": "latitude",
        "lng": "longitude"
    }
)

st.map(map_df)

# --------------------------------------------------
# AQI Distribution (Streamlit native chart)
# --------------------------------------------------
st.subheader("📈 AQI Distribution")

aqi_counts = filtered_df["AQI Value"].value_counts().sort_index()
st.line_chart(aqi_counts)

# --------------------------------------------------
# Footer
# --------------------------------------------------
st.markdown("---")
st.markdown("✅ Built using **Streamlit + Pandas** (Cloud Safe)")
