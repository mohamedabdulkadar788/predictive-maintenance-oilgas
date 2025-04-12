import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader("Upload your CSV file now ", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    # Show the column names for debugging
    st.write("Columns in the uploaded file:", df.columns)
    
    required_columns = ['sensor_2', 'sensor_3', 'sensor_4', 'sensor_7', 'sensor_8', 
                        'sensor_11', 'sensor_15', 'sensor_17', 'sensor_20', 'sensor_21', 'label']
    
    missing_columns = [col for col in required_columns if col not in df.columns]
    
    if missing_columns:
        st.error(f"Missing columns in uploaded file: {missing_columns}")
    else:
        st.write("All required columns are present!")
        # Continue with further logic here (e.g., predictions, data analysis, etc.)
