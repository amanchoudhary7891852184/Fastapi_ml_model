import numpy as np
import joblib

# Load trained model & scaler
model = joblib.load("kidney_stone_best_model.pkl")
scaler = joblib.load("scaler.pkl")

def predict_stone(data):
    input_array = np.array([[  
        data.gravity,
        data.ph,
        data.osmo,
        data.cond,
        data.urea,
        data.calc
    ]])

    input_scaled = scaler.transform(input_array)
    prediction = model.predict(input_scaled)[0]

    return int(prediction)
