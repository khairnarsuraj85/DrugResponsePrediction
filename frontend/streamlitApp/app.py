import streamlit as st
import pandas as pd
import pickle

# Load the trained model and scaler
with open('drug_prediction_model2.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# List of drug names corresponding to model's output
drug_names = ["Erlotinib", "Rapamycin", "Sunitinib", "PHA-665752", "MG-132", "Paclitaxel", "Cyclopamine", "AZ628", "Sorafenib", "Tozasertib",
              "Imatinib", "NVP-TAE684", "Crizotinib","Tipifarnib", "Cabozantinib" ]  # Update with actual drug names

# Title of the app
st.title("Drug Response Prediction App")

# User input for features
st.header("Input Features")
feature_1 = st.number_input("MIN_CONC:", step=0.01)
feature_2 = st.number_input("MAX_CONC:", step=0.01)
feature_3 = st.number_input("LN_IC50:", step=0.01)

# AA Position options
aa_position = st.selectbox("AA Position:", 
    options=["p.A1004S", "p.A1004V", "p.A1004fs*16", "p.A1045V", "p.A1049T", 
              "p.A1052V", "p.A1068V", "p.A1078S", "p.A108V"])  # Include all relevant options

# Create a DataFrame for input features
input_data = pd.DataFrame({
    'MIN_CONC': [feature_1],
    'MAX_CONC': [feature_2],
    'LN_IC50': [feature_3],
    'AA_POSITION': [aa_position]
})

# Creating dummy variables to match the training set
dummy_df = pd.get_dummies(input_data, columns=['AA_POSITION'], drop_first=True)

# List all columns from the scaler's fitted DataFrame (these should match your training set)
expected_columns = scaler.feature_names_in_

# Ensure the input DataFrame has the same columns as the training set
dummy_df = dummy_df.reindex(columns=expected_columns, fill_value=0)

# Scale the input data
input_data_scaled = scaler.transform(dummy_df)

# Make predictions
if st.button("Predict"):
    # Make prediction
    prediction_index = model.predict(input_data_scaled)

    # Get predicted drug name and sensitivity
    predicted_drug_name = drug_names[prediction_index[0]]  # Assuming prediction_index is an array
    drug_sensitivity = "Sensitive" if prediction_index[0] == 1 else "Resistant"

    # Display the prediction result
    st.success(f"The predicted drug is **{predicted_drug_name}**, which is **{drug_sensitivity}**.")
    st.write(f"Concentrations - MIN_CONC: {feature_1}, MAX_CONC: {feature_2}, LN_IC50: {feature_3}")





