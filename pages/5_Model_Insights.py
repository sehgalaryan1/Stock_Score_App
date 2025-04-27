import streamlit as st
import pandas as pd
from model_utils         import load_models
from feature_engineering import make_tech_features, make_fund_features

st.markdown("🤖 **Model Insights**")

if "data" not in st.session_state or "combined" not in st.session_state:
    st.warning("Please go back to Home and select a ticker first.")
else:
    df_price    = st.session_state.data
    df_combined = st.session_state.combined

    # Load models
    fund_model, tech_model = load_models()

    # Generate full prediction series
    tech_preds = tech_model.predict(make_tech_features(df_price))
    fund_preds = fund_model.predict(make_fund_features(df_combined))

    # Create a DataFrame for plotting
    df_insights = pd.DataFrame({
        "Date": df_price.index[-len(tech_preds):],
        "Technical Score": tech_preds,
        "Fundamental Score": fund_preds
    }).set_index("Date")

    st.line_chart(df_insights)
    st.write("Above: how each sub-score has evolved over time.")
