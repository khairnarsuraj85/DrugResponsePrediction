
# 💊 Drug Response Prediction

This project predicts the most suitable drug and its sensitivity (Sensitive/Resistant) based on given concentration and mutation data.  
It consists of:
- **Machine Learning Model** (trained on drug response dataset)
- **FastAPI Backend** for prediction API
- **Frontend (HTML/CSS/JS)** for web-based interaction
- **Streamlit App** for quick testing

---

## 📌 Features
- Predict drug type and sensitivity using user inputs.
- FastAPI-based backend for REST API predictions.
- Frontend UI for easy interaction.
- Streamlit app for quick testing without a browser.
- Scaler & model loading for reproducible results.

---

## 📂 Project Structure

Drug-Response-Prediction/
│
├── backend/
│ ├── main.py # FastAPI backend API
│ ├── drug_prediction_model2.pkl # Saved ML model
│ ├── scaler.pkl # Saved scaler for feature normalization
│
├── frontend/
│ ├── index.html # Main HTML UI
│ ├── styles.css # Styling
│ ├── script.js # JS for API calls
│ └── streamlitApp/
│ └── app.py # Streamlit-based UI
│
├── dataset.csv # Dataset used for training
├── Algo.ipynb # Model training notebook
├── DrugResponsePrediction.ipynb # Alternative training/testing notebook
├── .gitignore
└── README.md # Project documentation


---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/Drug-Response-Prediction.git
cd Drug-Response-Prediction

📦 Backend Setup (FastAPI)
Install dependencies

From the project root, run:

pip install fastapi uvicorn pandas scikit-learn pydantic

🚀 Running the Backend
cd backend
uvicorn main:app --reload


The backend will start at:
http://127.0.0.1:8000

🌐 Frontend Setup

No installation required.
Just open frontend/index.html in your browser after the backend is running.

🖥 Running the Streamlit App

From frontend/streamlitApp/:

streamlit run app.py


The app will be available at http://localhost:8501

📊 Input Parameters
Parameter	Type	Description
MIN_CONC	float	Minimum concentration of the drug
MAX_CONC	float	Maximum concentration of the drug
LN_IC50	float	Log IC50 value
AA_POSITION	string	Mutation/amino acid position
📦 API Endpoint

POST /predict
Request Body:

{
  "MIN_CONC": 0.1,
  "MAX_CONC": 5.0,
  "LN_IC50": 2.3,
  "AA_POSITION": "p.A1004S"
}


Response:

{
  "predicted_drug": "Erlotinib",
  "sensitivity": "Sensitive"
}

🧠 Model

Trained using RandomForestClassifier in Algo.ipynb.

Features scaled using StandardScaler.

Saved as drug_prediction_model2.pkl and scaler.pkl.

📜 License

This project is open-source and free to use for educational purposes.

👨‍💻 Author

Suraj Khairnar
Final-year Computer Engineering student passionate about AI, ML, and real-world applications.


---

If you want, I can now make this **README automatically detect and list backend dependencies from your `main.py` & notebooks** so you never miss a package when someone installs it.  
Should I prepare that next?
