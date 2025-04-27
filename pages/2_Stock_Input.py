import streamlit as st
from model_utils         import load_models
from feature_engineering import make_tech_features, make_fund_features

st.markdown("🔍 **Stock Input & Score**")

if "data" not in st.session_state or "combined" not in st.session_state:
    st.warning("Please go back to Home and select a ticker first.")
else:
    df_price    = st.session_state.data
    df_combined = st.session_state.combined
    fw, tw      = st.session_state.fund_weight, st.session_state.tech_weight

    # Build features
    X_tech = make_tech_features(df_price)
    X_fund = make_fund_features(df_combined)

    # Load models
    fund_model, tech_model = load_models()

    # Predict
    tech_preds = tech_model.predict(X_tech)
    fund_preds = fund_model.predict(X_fund)

    # Latest scores
    tech_score = float(tech_preds[-1])
    fund_score = float(fund_preds[-1])

    # Combine
    final_score = round(fw * fund_score + tw * tech_score, 1)
    emoji       = "🟢" if final_score >= 7 else "🟡" if final_score >= 4 else "🔴"

    # Display
    st.metric("Investment Rating (0–10)", f"{final_score} {emoji}")
    st.write("**Sub-scores:**")
    st.write(f"- Fundamental: {fund_score:.1f} / 10  ({int(fw*100)}%)")
    st.write(f"- Technical:  {tech_score:.1f} / 10  ({int(tw*100)}%)")

    with st.expander("Show raw price data"):
        st.dataframe(df_price, use_container_width=True)

# 3) Store weightings as decimals
st.session_state.fund_weight = fund_weight / 100.0
st.session_state.tech_weight = tech_weight  / 100.0
