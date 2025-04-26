# pages/2_Stock_Input.py

import streamlit as st
from model_utils import load_models
from feature_engineering import make_tech_features, make_fund_features

st.markdown("🔍 **Stock Input & Score**")

# Check that both price history and combined feature data are loaded
if "data" not in st.session_state or "combined" not in st.session_state:
    st.warning("Please go back to Home and select a ticker first.")
else:
    df_price    = st.session_state.data
    df_combined = st.session_state.combined
    fw          = st.session_state.fund_weight
    tw          = st.session_state.tech_weight

    # 1) Build feature matrices exactly as in your notebook
    X_tech = make_tech_features(df_price)
    X_fund = make_fund_features(df_combined)

    # 2) Load the trained pipelines
    fund_model, tech_model = load_models()

    # 3) Predict sub-scores
    tech_preds = tech_model.predict(X_tech)
    fund_preds = fund_model.predict(X_fund)

    # 4) Use the most recent prediction from each
    tech_score = float(tech_preds[-1])
    fund_score = float(fund_preds[-1])

    # 5) Combine by user’s weights
    final_score = round(fw * fund_score + tw * tech_score, 1)
    emoji       = "🟢" if final_score >= 7 else "🟡" if final_score >= 4 else "🔴"

    # 6) Display the results
    st.metric("Investment Rating (0–10)", f"{final_score} {emoji}")
    st.write("**Sub-scores:**")
    st.write(f"- Fundamental: {fund_score:.1f} / 10  ({int(fw*100)}%)")
    st.write(f"- Technical:  {tech_score:.1f} / 10  ({int(tw*100)}%)")

    # 7) Raw data expander
    with st.expander("Show raw price data"):
        st.dataframe(df_price, use_container_width=True)

