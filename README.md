# 💊 Drug Response Prediction

Predict the **most suitable drug** and its **sensitivity (Sensitive/Resistant)** from features like concentration and mutation data.

---

## 📌 Overview

This project uses a **RandomForestClassifier** model to predict drug response based on given inputs.  
It offers:
- **FastAPI backend** for predictions
- **Frontend** (HTML/CSS/JS) for browser-based interaction
- **Streamlit app** for quick local testing

---

## ✨ Features

- 🔮 Predict drug type and sensitivity (Sensitive/Resistant)
- ⚡ REST API powered by FastAPI
- 🖥️ Simple HTML/CSS/JS frontend to consume API
- 🚀 Streamlit-based quick test interface
- 🧱 Saved model (`.pkl`) and scaler for reproducible results

---

## 📂 Project Structure

```plaintext
├── backend/  
│   ├── main.py # FastAPI app (uvicorn entrypoint: main:app)  
│   ├── drug_prediction_model2.pkl # Trained ML model (RandomForestClassifier)  
│   └── scaler.pkl # StandardScaler for preprocessing  
├── frontend/  
│   ├── index.html # UI  
│   ├── styles.css # Styles  
│   └── script.js # Calls the FastAPI endpoint  
├── streamlitApp/  
│   └── app.py # Streamlit interface for local testing  
├── dataset.csv # Training dataset (example/optional)  
├── Algo.ipynb # Training notebook  
├── DrugResponsePrediction.ipynb # Alternate training/testing notebook  
├── .gitignore  
└── README.md # You are here ✅  
