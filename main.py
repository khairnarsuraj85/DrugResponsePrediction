# backend/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import pandas as pd

app = FastAPI()

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, set specific domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model and scaler
with open("drug_prediction_model2.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

drug_names = ["Erlotinib", "Rapamycin", "Sunitinib", "PHA-665752", "MG-132",
              "Paclitaxel", "Cyclopamine", "AZ628", "Sorafenib", "Tozasertib",
              "Imatinib", "NVP-TAE684", "Crizotinib", "Tipifarnib", "Cabozantinib"]

class InputData(BaseModel):
    MIN_CONC: float
    MAX_CONC: float
    LN_IC50: float
    AA_POSITION: str

@app.post("/predict")
def predict(data: InputData):
    df = pd.DataFrame([{
        "MIN_CONC": data.MIN_CONC,
        "MAX_CONC": data.MAX_CONC,
        "LN_IC50": data.LN_IC50,
        "AA_POSITION": data.AA_POSITION
    }])
    dummy_df = pd.get_dummies(df, columns=['AA_POSITION'], drop_first=True)
    expected_columns = scaler.feature_names_in_
    dummy_df = dummy_df.reindex(columns=expected_columns, fill_value=0)
    input_scaled = scaler.transform(dummy_df)
    prediction = model.predict(input_scaled)
    drug_index = prediction[0]
    return {
        "predicted_drug": drug_names[drug_index],
        "sensitivity": "Sensitive" if drug_index == 1 else "Resistant"
    }
