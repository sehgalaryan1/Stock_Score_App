import os, sys
# Insert the project root (one level up from pages/) into sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from model_utils import load_models
from feature_engineering import make_tech_features, make_fund_features

st.markdown("🔍 **Stock Input & Score**")

if "data" not in st.session_state or "combined" not in st.session_state:
    st.warning("Please go back to Home and select a ticker first.")
else:
    df_price    = st.session_state.data
    df_combined = st.session_state.combined
    fw, tw      = st.session_state.fund_weight, st.session_state.tech_weight

    X_tech = make_tech_features(df_price)
    X_fund = make_fund_features(df_combined)

    fund_model, tech_model = load_models()
    tech_preds = tech_model.predict(X_tech)
    fund_preds = fund_model.predict(X_fund)

    tech_score = float(tech_preds[-1])
    fund_score = float(fund_preds[-1])
    final_score = round(fw * fund_score + tw * tech_score, 1)
    emoji       = "🟢" if final_score >= 7 else "🟡" if final_score >= 4 else "🔴"

    st.metric("Investment Rating (0–10)", f"{final_score} {emoji}")
    st.write("**Sub-scores:**")
    st.write(f"- Fundamental: {fund_score:.1f} / 10  ({int(fw*100)}%)")
    st.write(f"- Technical:  {tech_score:.1f} / 10  ({int(tw*100)}%)")

    with st.expander("Show raw price data"):
        st.dataframe(df_price, use_container_width=True)
