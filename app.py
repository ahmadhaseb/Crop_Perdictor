import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("crop_model.pkl")

# Page Configuration
st.set_page_config(
    page_title="Crop Recommendation System",
    page_icon="🌱",
    layout="centered"
)

# Title
st.title("🌱 Crop Recommendation System")
st.write("Enter the soil and weather details to get the recommended crop.")

# User Inputs
N = st.number_input("Nitrogen (N)", min_value=0.0, max_value=200.0, value=90.0)
P = st.number_input("Phosphorus (P)", min_value=0.0, max_value=200.0, value=42.0)
K = st.number_input("Potassium (K)", min_value=0.0, max_value=200.0, value=43.0)

temperature = st.number_input("Temperature (°C)", value=25.0)
humidity = st.slider("Humidity (%)", 0.0, 100.0, 80.0)
ph = st.number_input("Soil pH", min_value=0.0, max_value=14.0, value=6.5)
rainfall = st.number_input("Rainfall (mm)", value=200.0)

# Prediction Button
if st.button("🌾 Recommend Crop"):

    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])

    prediction = model.predict(input_data)

    st.success(f"✅ Recommended Crop: **{prediction[0]}**")
