
import streamlit as st
import joblib
import pandas as pd

MODEL_PATH = "best_model.joblib"
model = joblib.load(MODEL_PATH)

st.title("🏠 House Price Predictor")
st.write("Model: rf")

st.header("Manual input")
inputs = {}
# numeric input
for c in ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']:
    inputs[c] = st.number_input(c, value=0.0)

input_df = pd.DataFrame([inputs])

if st.button("Predict"):
    pred = model.predict(input_df)[0]
    st.success(f"Predicted Price: {pred:,.2f}")
