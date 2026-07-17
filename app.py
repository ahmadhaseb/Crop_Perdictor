import streamlit as st
import pandas as pd
import numpy as np
import joblib

# ==============================
# Page Configuration
# ==============================
st.set_page_config(
    page_title="AI Crop Recommendation System",
    page_icon="🌱",
    layout="centered"
)

# ==============================
# Load Trained Model
# ==============================
model = joblib.load("crop_model.pkl")

# ==============================
# Crop Information
# ==============================
crop_info = {
    "rice": {
        "season": "Kharif",
        "description": "Rice is one of the major food crops grown in warm and humid climates.",
        "temperature": "20°C - 35°C",
        "rainfall": "100 - 200 mm",
        "tips": "Maintain proper irrigation and balanced fertilizer."
    },

    "wheat": {
        "season": "Rabi",
        "description": "Wheat is Pakistan's major winter crop.",
        "temperature": "15°C - 25°C",
        "rainfall": "50 - 100 mm",
        "tips": "Use certified seed and irrigate at critical stages."
    },

    "maize": {
        "season": "Spring / Kharif",
        "description": "Maize is widely grown for food and livestock feed.",
        "temperature": "18°C - 30°C",
        "rainfall": "60 - 120 mm",
        "tips": "Ensure proper spacing and nitrogen fertilizer."
    },

    "cotton": {
        "season": "Kharif",
        "description": "Cotton is Pakistan's important cash crop.",
        "temperature": "21°C - 35°C",
        "rainfall": "50 - 100 mm",
        "tips": "Avoid waterlogging and control pests."
    },

    "banana": {
        "season": "Throughout the Year",
        "description": "Banana grows best in tropical climates.",
        "temperature": "25°C - 35°C",
        "rainfall": "100 - 250 mm",
        "tips": "Provide regular irrigation and organic manure."
    },

    "mango": {
        "season": "Spring",
        "description": "Mango is known as the king of fruits.",
        "temperature": "24°C - 35°C",
        "rainfall": "75 - 150 mm",
        "tips": "Avoid excess irrigation during flowering."
    }
}

# ==============================
# Sidebar
# ==============================
st.sidebar.title("🌾 AI Crop Recommendation")

st.sidebar.info("""
This application recommends the best crop
based on soil nutrients and weather conditions.

Technology Used

• Python

• Scikit-Learn

• Streamlit

• Machine Learning
""")

# ==============================
# Main Title
# ==============================
st.title("🌱 AI Crop Recommendation System")

st.write("""
Enter the required soil nutrients and weather information.
The Machine Learning model will recommend the most suitable crop.
""")

st.divider()

# ==============================
# User Inputs
# ==============================
st.subheader("📝 Enter Soil & Weather Information")

N = st.number_input("Nitrogen (N)", 0.0, 200.0, 90.0)

P = st.number_input("Phosphorus (P)", 0.0, 200.0, 42.0)

K = st.number_input("Potassium (K)", 0.0, 200.0, 43.0)

temperature = st.number_input("Temperature (°C)", value=25.0)

humidity = st.slider("Humidity (%)", 0.0, 100.0, 80.0)

ph = st.number_input("Soil pH", 0.0, 14.0, 6.5)

rainfall = st.number_input("Rainfall (mm)", value=200.0)

st.divider()

# ==============================
# Prediction
# ==============================
if st.button("🌾 Recommend Crop"):

    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])

    prediction = model.predict(input_data)

    crop = prediction[0]

    st.subheader("📋 Input Summary")

    summary = pd.DataFrame({
        "Parameter":[
            "Nitrogen",
            "Phosphorus",
            "Potassium",
            "Temperature",
            "Humidity",
            "Soil pH",
            "Rainfall"
        ],

        "Value":[
            N,
            P,
            K,
            temperature,
            humidity,
            ph,
            rainfall
        ]
    })

    st.table(summary)

    st.success(f"🌾 Recommended Crop : {crop.title()}")

    if crop.lower() in crop_info:

        st.subheader("📖 Crop Details")

        st.write("### 🌱 Description")
        st.write(crop_info[crop.lower()]["description"])

        st.write("### 📅 Best Season")
        st.write(crop_info[crop.lower()]["season"])

        st.write("### 🌡 Suitable Temperature")
        st.write(crop_info[crop.lower()]["temperature"])

        st.write("### 🌧 Suitable Rainfall")
        st.write(crop_info[crop.lower()]["rainfall"])

        st.write("### 💡 Growing Tips")
        st.info(crop_info[crop.lower()]["tips"])

    else:
        st.warning("Detailed information for this crop is not available.")

    st.balloons()

st.divider()

st.markdown("---")

st.caption("👨‍💻 Developed by Haseeb Ahmad")
