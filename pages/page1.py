import streamlit as st
from model_utils import load_models
from feature_engineering import make_tech_features, make_fund_features

st.markdown("🔍 **Stock Input & Score**")

if "data" not in st.session_state or "combined" not in st.session_state:
    st.warning("Go back to Home, select a ticker, and wait for data to load.")
else:
    # 1) Grab price & combined feature data
    df_price    = st.session_state.data
    df_combined = st.session_state.combined

    # 2) User’s weightings (0–1)
    fw = st.session_state.fund_weight
    tw = st.session_state.tech_weight

    # 3) Build feature matrices exactly as in your notebook
    X_tech = make_tech_features(df_price)
    X_fund = make_fund_features(df_combined)

    # 4) Load the trained pipelines
    fund_model, tech_model = load_models()

    # 5) Predict sub‐scores
    tech_preds = tech_model.predict(X_tech)
    fund_preds = fund_model.predict(X_fund)

    # 6) Take the most recent prediction from each
    tech_score = float(tech_preds[-1])
    fund_score = float(fund_preds[-1])

    # 7) Weighted combination
    final_score = round(fw * fund_score + tw * tech_score, 1)
    color = "🟢" if final_score >= 7 else "🟡" if final_score >= 4 else "🔴"

    # 8) Display
    st.metric("Investment Rating (0–10)", f"{final_score} {color}")
    st.write("**Sub-scores:**")
    st.write(f"- Fundamental: {fund_score:.1f} / 10  ({int(fw*100)}%)")
    st.write(f"- Technical:  {tech_score:.1f} / 10  ({int(tw*100)}%)")

    # 9) Optional: peek at the raw data
    with st.expander("Show raw price data"):
        st.dataframe(df_price, use_container_width=True)
