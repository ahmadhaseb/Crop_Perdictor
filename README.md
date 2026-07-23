# 🌾 Crop Recommendation System

A Machine Learning-based Crop Recommendation System developed using **Python, Scikit-learn, FastAPI, and Streamlit**. The system recommends the most suitable crop based on soil nutrients and environmental conditions using a **Random Forest Classifier**.

---

## 📖 Project Overview

The Crop Recommendation System helps farmers make informed decisions by predicting the most suitable crop based on soil nutrients and weather conditions. It uses a trained Machine Learning model to analyze user inputs and provide accurate crop recommendations.

The project includes a **FastAPI backend** for prediction and a **Streamlit frontend** for an interactive user interface.

---

## ✨ Features

- 🌱 Crop Recommendation
- 🤖 Machine Learning Prediction
- 🌐 FastAPI REST API
- 💻 Streamlit User Interface
- 📊 User Input Summary
- ⚡ Real-Time Prediction
- 📱 Responsive and Easy-to-Use Interface

---

## 🛠 Technologies Used

- Python
- Scikit-learn
- Streamlit
- FastAPI
- Pandas
- NumPy
- Joblib
- Requests
- Uvicorn

---

## 🤖 Machine Learning Model

### Algorithm

- Random Forest Classifier

### Input Features

- Nitrogen (N)
- Phosphorus (P)
- Potassium (K)
- Temperature
- Humidity
- pH
- Rainfall

### Output

- Recommended Crop

---

## 📂 Dataset

The model is trained using the **Crop Recommendation Dataset**.

### Features

- Nitrogen
- Phosphorus
- Potassium
- Temperature
- Humidity
- pH
- Rainfall

### Target

- Crop Label

---

## 📁 Project Structure

```text
Crop-Recommendation-System/
│
├── app.py
├── crop_model.pkl
├── requirements.txt
├── README.md
└── Crop_recommendation.csv
```

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/ahmadhaseb/Crop-Recommendation-System.git
```

### Move to Project Directory

```bash
cd Crop-Recommendation-System
```

### Install Required Libraries

```bash
pip install -r requirements.txt
```

---

## ▶ Run FastAPI Backend

```bash
python -m uvicorn api:app --reload
```

API Documentation

```
http://127.0.0.1:8000/docs
```

---

## ▶ Run Streamlit Frontend

```bash
python -m streamlit run app.py
```

---

## 📊 Application Workflow

1. Launch the Streamlit application.
2. Enter soil nutrient values and environmental conditions.
3. Click the **Predict Crop** button.
4. Streamlit sends the request to the FastAPI backend.
5. The Random Forest Classifier predicts the most suitable crop.
6. The recommended crop is displayed along with the input summary.

---

## 🎯 Future Improvements

- Fertilizer Recommendation
- Weather API Integration
- Soil Health Analysis
- Crop Yield Prediction
- Multi-language Support
- Cloud Deployment
- Farmer Dashboard

---

## 👨‍💻 Developer

**Haseeb Ahmad**

BS Software Engineering

Machine Learning & AI Enthusiast

---

## 📄 License

This project is developed for educational and learning purposes.
