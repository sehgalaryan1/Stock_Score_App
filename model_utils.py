# model_utils.py
import joblib
import streamlit as st
from pathlib import Path

@st.cache_resource
def load_models():
    """Load and cache the two sklearn pipelines from model/."""
    base = Path(__file__).parent / "model"
    fund = joblib.load(base / "fund_model.pkl")
    tech = joblib.load(base / "tech_model.pkl")
    return fund, tech
