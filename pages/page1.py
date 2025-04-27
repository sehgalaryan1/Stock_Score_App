import streamlit as st
import joblib
import numpy as np
import pandas as pd

@st.cache_resource
def load_models():
    fund_model = joblib.load("model/fund_model.pkl")
    tech_model = joblib.load("model/tech_model.pkl")
    return fund_model, tech_model

def main():
    fund_model, tech_model = load_models()

    st.title("🔍 Stock Input & Score")

    # 1) Ticker & weight inputs
    ticker = st.text_input("Enter Stock Ticker (e.g., AAPL)", "AAPL")
    fund_weight = st.slider("Fundamental Weight (%)", 0, 100, 50)
    tech_weight = 100 - fund_weight
    st.write(f"**Fundamental:** {fund_weight}% | **Technical:** {tech_weight}%")

    # 2) Run prediction
    if st.button("🔍 Score Investment Risk"):
        st.info("Fetching features and running models...")

        # — feature definitions (must match your training)
        fund_num_cols = [
            'current_assets','total_assets','common_equity_total',
            'current_debt','long_term_debt','depreciation_amortization',
            'preferred_dividends','current_liabilities','total_liabilities',
            'net_income','pretax_income','total_revenue',
            'total_income_taxes','interest_expense_total',
            'capital_expenditures','net_cash_flow_operating_activities',
            'dividends_per_share_quarter','price_low_quarter'
        ]
        tech_num_cols = [
            'monthly_return','month_trading_volume','stdev',
            'avg_ret_6m','avg_ret_12m','vol_6m','vol_12m'
        ]

        # — simulate inputs (replace with real data later)
        df_f = pd.DataFrame([np.random.rand(len(fund_num_cols))], columns=fund_num_cols)
        df_f['gics_sector_x'] = 'Information Technology'
        df_t = pd.DataFrame([np.random.rand(len(tech_num_cols))], columns=tech_num_cols)
        df_t['gics_sector_x'] = 'Information Technology'

        # — make predictions
        fund_score = fund_model.predict(df_f)[0]
        tech_score = tech_model.predict(df_t)[0]

        # — combine & clip to 0–10
        final_score = (fund_score * fund_weight/100) + (tech_score * tech_weight/100)
        final_score = min(max(final_score, 0), 10)

        st.success(f"🎯 Investment Risk Score: **{final_score:.2f} / 10**")

        # — risk category
        if final_score < 3:
            st.write("🟢 **Low Risk**")
        elif final_score < 7:
            st.write("🟡 **Medium Risk**")
        else:
            st.write("🔴 **High Risk**")

        # — optional gauge chart
        try:
            import plotly.graph_objects as go
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=final_score,
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': "Risk Score (0–10)"},
                gauge={
                    'axis': {'range': [0, 10]},
                    'steps': [
                        {'range': [0, 3], 'color': 'green'},
                        {'range': [3, 7], 'color': 'yellow'},
                        {'range': [7, 10], 'color': 'red'}
                    ],
                }
            ))
            st.plotly_chart(fig, use_container_width=True)
        except ImportError:
            st.warning("Install `plotly` (`pip install plotly`) to see the gauge chart.")

if __name__ == "__main__":
    main()
  
