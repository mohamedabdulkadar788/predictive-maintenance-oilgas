import streamlit as st
import pandas as pd

# Feature columns you are using
features = ['sensor_2', 'sensor_3', 'sensor_4', 'sensor_7', 'sensor_8',
            'sensor_11', 'sensor_15', 'sensor_17', 'sensor_20', 'sensor_21']

# Title
st.title("🔧 Predictive Maintenance App - Upload Your Sensor Data")

# File uploader
uploaded_file = st.file_uploader("📤 Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("📋 Raw Data Preview")
    st.dataframe(df)

    # Check if required columns exist
    required_columns = features + ['label']
    missing = [col for col in required_columns if col not in df.columns]

    if missing:
        st.error(f"Missing columns in uploaded file: {missing}")
    else:
        X = df[features]
        y = df['label']

        st.success("✅ Features and label successfully extracted!")

        st.subheader("🧪 Input Features (X)")
        st.dataframe(X)

        st.subheader("🎯 Target (label)")
        st.write(y.value_counts())
