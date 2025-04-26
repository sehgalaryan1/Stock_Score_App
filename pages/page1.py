import streamlit as st
import numpy as np

st.markdown("🔍 **Stock Input & Score**")

if 'data' not in st.session_state:
    st.warning("Go back to Home and pick a ticker.")
else:
    df = st.session_state.data
    fw = st.session_state.fund_weight    # e.g. 0.6
    tw = st.session_state.tech_weight     # e.g. 0.4

    # — Technical score (normalize avg daily % change into 0–10) —
    raw = df['Close'].pct_change().mean() * 100 + 5
    # ensure it's a Python float and clip between 0 and 10
    tech_score = round(float(np.clip(raw, 0, 10)), 1)

    # — Fundamental score (swap in your real ML output here) —
    fund_score = 7.3

    # — Combined weighted score —
    final_score = round(fw * fund_score + tw * tech_score, 1)
    color = "🟢" if final_score >= 7 else "🟡" if final_score >= 4 else "🔴"

    st.metric("Investment Rating (0–10)", f"{final_score} {color}")
    st.write("**Sub-scores:**")
    st.write(f"- Fundamental: {fund_score} / 10  ({int(fw*100)}%)")
    st.write(f"- Technical:  {tech_score} / 10  ({int(tw*100)}%)")

    with st.expander("Show raw price data"):
        st.dataframe(df, use_container_width=True)
