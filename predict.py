import pickle
import pandas as pd
import numpy as np

# 1️⃣ Load the model and features
with open('rf_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('features.pkl', 'rb') as f:
    features = pickle.load(f)
    
    
# input_df = pd.read_csv('new_sensor_data.csv')[features]


# 2️⃣ Example new data (from user or sensor)
# You can replace this with reading from CSV later
new_data = {
    'sensor_2': [150.0],
    'sensor_3': [16.3],
    'sensor_4': [410.1],
    'sensor_7': [22.5],
    'sensor_8': [85.0],
    'sensor_11': [42.0],
    'sensor_15': [375.3],
    'sensor_17': [39.1],
    'sensor_20': [12.6],
    'sensor_21': [0.03]
}

# 3️⃣ Convert to DataFrame
input_df = pd.DataFrame(new_data)

# 4️⃣ Make prediction
prediction = model.predict(input_df)[0]

# 5️⃣ Show result
if prediction == 1:
    print("!!!Beware, Machine is at risk of FAILURE")
else:
    print("[OK Fine!] Machine is operating NORMALLY")
