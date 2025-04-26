# model_utils.py
import streamlit as st
import joblib, requests
from io import BytesIO

@st.cache_resource
def load_models():
    """Fetch model files from cloud storage and return (fund_model, tech_model)."""
    # Replace with the HTTPS URLs for your uploaded .pkl files:
    fund_url = "https://storage.googleapis.com/bucket-ba780/fund_model.pkl"
    tech_url = "https://storage.googleapis.com/bucket-ba780/tech_model.pkl"

    # Download into memory
    fund_resp = requests.get(fund_url)
    tech_resp = requests.get(tech_url)
    fund_resp.raise_for_status()
    tech_resp.raise_for_status()

    # Load into sklearn pipelines
    fund_model = joblib.load(BytesIO(fund_resp.content))
    tech_model = joblib.load(BytesIO(tech_resp.content))

    return fund_model, tech_model
