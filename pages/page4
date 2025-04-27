import streamlit as st
import joblib
import numpy as np
import pandas as pd
import plotly.graph_objects as go

@st.cache_resource
def load_models():
    fund_model = joblib.load("model/fund_model.pkl")
    tech_model = joblib.load("model/tech_model.pkl")
    return fund_model, tech_model

def main():
    st.title("🤖 Model & Score Explanation")

    # Inputs (same as scoring page)
    ticker = st.text_input("Enter Stock Ticker", "AAPL").upper()
    fund_weight = st.slider("Fundamental Weight (%)", 0, 100, 50)
    tech_weight = 100 - fund_weight
    st.write(f"**Fundamental Weight:** {fund_weight}% | **Technical Weight:** {tech_weight}%")

    if st.button("Explain Model & Scores"):
        st.info("Running models and extracting explanations…")

        fund_model, tech_model = load_models()

        # define feature names exactly as in training
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
        # simulate dummy feature rows
        df_f = pd.DataFrame([np.random.rand(len(fund_num_cols))], columns=fund_num_cols)
        df_f['gics_sector_x'] = 'Information Technology'
        df_t = pd.DataFrame([np.random.rand(len(tech_num_cols))], columns=tech_num_cols)
        df_t['gics_sector_x'] = 'Information Technology'

        # predict
        fund_score = fund_model.predict(df_f)[0]
        tech_score = tech_model.predict(df_t)[0]
        final_score = (fund_score * fund_weight/100) + (tech_score * tech_weight/100)
        final_score = min(max(final_score, 0), 10)

        # show breakdown
        st.subheader("Score Breakdown")
        st.write(f"- Technical Score: **{tech_score:.2f} / 10**")
        st.write(f"- Fundamental Score: **{fund_score:.2f} / 10**")
        st.write(f"- **Combined Final Score: {final_score:.2f} / 10**")

        # feature importances
        st.subheader("Feature Importances")

        # Fundamental model importances
        if hasattr(fund_model, "feature_importances_"):
            imp = fund_model.feature_importances_
            df_imp = pd.DataFrame({
                "feature": fund_num_cols,
                "importance": imp[: len(fund_num_cols)]
            }).sort_values("importance", ascending=False)
            fig = go.Figure(go.Bar(
                x=df_imp["importance"],
                y=df_imp["feature"],
                orientation="h",
                text=df_imp["importance"].map(lambda v: f"{v:.3f}"),
                textposition="auto"
            ))
            fig.update_layout(title="Fundamental Model Feature Importances", yaxis_title="", margin=dict(l=150))
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.write("Fundamental model does not expose `feature_importances_`.")

        # Technical model importances
        if hasattr(tech_model, "feature_importances_"):
            imp = tech_model.feature_importances_
            df_imp = pd.DataFrame({
                "feature": tech_num_cols,
                "importance": imp[: len(tech_num_cols)]
            }).sort_values("importance", ascending=False)
            fig = go.Figure(go.Bar(
                x=df_imp["importance"],
                y=df_imp["feature"],
                orientation="h",
                text=df_imp["importance"].map(lambda v: f"{v:.3f}"),
                textposition="auto"
            ))
            fig.update_layout(title="Technical Model Feature Importances", yaxis_title="", margin=dict(l=150))
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.write("Technical model does not expose `feature_importances_`.")

if __name__ == "__main__":
    main()
