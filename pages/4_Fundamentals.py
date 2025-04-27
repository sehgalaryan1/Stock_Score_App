import streamlit as st
import pandas as pd
import altair as alt
from feature_engineering import fund_num_cols, fund_cat_cols

st.markdown("🧾 **Fundamental Metrics**")

if "combined" not in st.session_state:
    st.warning("Please go back to Home and select a ticker first.")
else:
    df = st.session_state.combined

    # Raw fundamental data
    with st.expander("Show raw fundamental data"):
        st.dataframe(df[fund_num_cols + fund_cat_cols], use_container_width=True)

    # Example comparison vs. industry (mock data—replace with real averages)
    df_ratios = pd.DataFrame({
        "Metric": ["ROE","Debt/Equity","EPS Growth","P/E Ratio"],
        "Company": df[["net_income","total_liabilities","dividends_per_share_quarter","price_low_quarter"]]
                       .mean().round(1).tolist(),
        "Industry Avg": [15, 1.2, 8, 20]
    })

    chart = alt.Chart(df_ratios).transform_fold(
        ["Company","Industry Avg"],
        as_=["Type","Value"]
    ).mark_bar().encode(
        x="Metric:N", y="Value:Q", color="Type:N"
    )
    st.altair_chart(chart, use_container_width=True)
