import streamlit as st

st.markdown("🔍 **Stock Input & Score**")

if 'data' not in st.session_state:
    st.warning("Go back to Home and pick a ticker.")
else:
    df = st.session_state.data
    fw = st.session_state.fund_weight    # e.g. 0.6
    tw = st.session_state.tech_weight     # e.g. 0.4

    # — Placeholder scoring logic — replace with your real models —
    # Technical: normalize 1–10 from avg daily % change
    tech_raw = df['Close'].pct_change().mean() * 100
    tech_score = round(max(0, min(10, tech_raw + 5)), 1)

    # Fundamental: dummy for now (swap your ML model output here)
    fund_score = 7.3

    # Combined weighted score
    final_score = round(fw * fund_score + tw * tech_score, 1)
    color = "🟢" if final_score >= 7 else "🟡" if final_score >= 4 else "🔴"

    st.metric("Investment Rating (0–10)", f"{final_score} {color}")
    st.write("**Sub-scores:**")
    st.write(f"- Fundamental: {fund_score} / 10  ({int(fw*100)}%)")
    st.write(f"- Technical:  {tech_score} / 10  ({int(tw*100)}%)")

    with st.expander("Show raw price data"):
        st.dataframe(df, use_container_width=True)
