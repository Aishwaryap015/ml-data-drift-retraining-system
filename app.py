import streamlit as st
import pandas as pd
import joblib

st.title("📊 Data Drift Monitoring Dashboard")

# Load data
train = pd.read_csv("data/train.csv")
new_data = pd.read_csv("data/new_data.csv")

st.subheader("Training Data Preview")
st.write(train.head())

st.subheader("New Incoming Data Preview")
st.write(new_data.head())

# Load model
model = joblib.load("models/model.pkl")

st.subheader("Model Prediction Sample")

preds = model.predict(new_data.drop("target", axis=1))
st.write(preds[:10])

st.success("System Running Successfully 🚀")