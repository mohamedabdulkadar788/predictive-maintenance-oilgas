import streamlit as st
import pandas as pd
import pickle

# Load model and features
with open('rf_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('features.pkl', 'rb') as f:
    features = pickle.load(f)

# App title
st.title("🛠️ Predictive Maintenance - Oil & Gas Industry")
st.write("Upload your sensor data CSV to predict machine failure.")

# Upload CSV
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    try:
        input_df = pd.read_csv(uploaded_file)

        # Show uploaded data
        st.subheader("📊 Uploaded Sensor Data")
        st.dataframe(input_df.head())

        # Check columns
        if all(f in input_df.columns for f in features):
            input_data = input_df[features]

            # Predict button
            if st.button("Predict"):
                preds = model.predict(input_data)

                # Show results
                st.subheader("📢 Prediction Results")
                results_df = pd.DataFrame({
                    'Prediction': ['Failure' if p == 1 else 'Normal' for p in preds]
                })
                st.dataframe(results_df)

                st.success("✅ Prediction complete!")

        else:
            st.error("Uploaded file must contain these columns:\n" + ", ".join(features))

    except Exception as e:
        st.error(f"Error reading file: {e}")
