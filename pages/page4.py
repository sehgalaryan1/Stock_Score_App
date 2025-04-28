import streamlit as st
import joblib
import numpy as np
import pandas as pd
import yfinance as yf

# Cache machine-learning models and scaler
@st.cache_resource
def load_models():
    fund_model = joblib.load("model/fund_model.pkl")
    tech_model = joblib.load("model/tech_model.pkl")
    scaler     = joblib.load("model/minmax_scaler.pkl")
    return fund_model, tech_model, scaler

# Cache fundamental info for 1 hour\ n@st.cache_data(ttl=3600)
def get_info(ticker):
    tk = yf.Ticker(ticker)
    return tk.info

# Cache price history for 1 hour\ n@st.cache_data(ttl=3600)
def get_history(ticker):
    return yf.download(ticker, period="1y", interval="1d", progress=False)


def main():
    st.title("🤖 Model & Rating Explanation")

    # --- Live Example: always on top ---
    st.header("🔍 Live Example: Run Models on a Ticker")
    ticker = st.text_input("Enter Stock Ticker", "AAPL").upper()
    fund_weight = st.slider("Fundamental Weight (%)", 0, 100, 50)
    tech_weight = 100 - fund_weight
    st.write(f"**Fundamental:** {fund_weight}%   |   **Technical:** {tech_weight}%")

    if st.button("Run Analysis"):
        # --- Fetch and process data & run models in one spinner ---
        with st.spinner("Fetching data and running models…"):
            try:
                info = get_info(ticker)
            except Exception as e:
                st.error(f"Could not fetch fundamentals: {e}")
                return

            hist = get_history(ticker)
            if hist is None or hist.empty:
                st.error("No price history found.")
                return
            daily_ret = hist['Close'].pct_change().dropna()

            # Prepare feature DataFrames
            fund_num_cols = [
                'current_assets','total_assets','common_equity_total',
                'current_debt','long_term_debt','depreciation_amortization',
                'preferred_dividends','current_liabilities','total_liabilities',
                'net_income','pretax_income','total_revenue',
                'total_income_taxes','interest_expense_total',
                'capital_expenditures','net_cash_flow_operating_activities',
                'dividends_per_share_quarter','price_low_quarter'
            ]
            fund_cat_cols = ['gics_sector_x']
            fund_data = {
                'current_assets': info.get('currentAssets', np.nan),
                'total_assets': info.get('totalAssets', np.nan),
                'common_equity_total': info.get('totalStockholderEquity', np.nan),
                'current_debt': info.get('currentDebt', np.nan),
                'long_term_debt': info.get('longTermDebt', np.nan),
                'depreciation_amortization': info.get('depreciationAndAmortization', np.nan),
                'preferred_dividends': info.get('preferredStockDividend', np.nan),
                'current_liabilities': info.get('currentLiabilities', np.nan),
                'total_liabilities': info.get('totalLiab', np.nan) or info.get('totalLiabilities', np.nan),
                'net_income': info.get('netIncomeToCommon', np.nan),
                'pretax_income': info.get('pretaxIncome', np.nan),
                'total_revenue': info.get('totalRevenue', np.nan),
                'total_income_taxes': info.get('incomeTaxExpense', np.nan),
                'interest_expense_total': info.get('interestExpense', np.nan),
                'capital_expenditures': info.get('capitalExpenditures', np.nan),
                'net_cash_flow_operating_activities': info.get('operatingCashflow', np.nan),
                'dividends_per_share_quarter': info.get('dividendRate', np.nan),
                'price_low_quarter': info.get('fiftyTwoWeekLow', np.nan),
                'gics_sector_x': info.get('sector', 'Unknown')
            }
            df_f = pd.DataFrame([fund_data], columns=fund_num_cols + fund_cat_cols)

            tech_num_cols = [
                'monthly_return','month_trading_volume','stdev',
                'avg_ret_6m','avg_ret_12m','vol_6m','vol_12m'
            ]
            tech_cat_cols = ['gics_sector_x']
            tech_data = {
                'monthly_return': daily_ret.resample('M').sum().iloc[-1],
                'month_trading_volume': hist['Volume'].resample('M').sum().iloc[-1],
                'stdev': daily_ret.std(),
                'avg_ret_6m': daily_ret.rolling(window=126, min_periods=1).mean().iloc[-1],
                'avg_ret_12m': daily_ret.rolling(window=252, min_periods=1).mean().iloc[-1],
                'vol_6m': daily_ret.rolling(window=126, min_periods=1).std().iloc[-1],
                'vol_12m': daily_ret.rolling(window=252, min_periods=1).std().iloc[-1],
                'gics_sector_x': info.get('sector', 'Unknown')
            }
            df_t = pd.DataFrame([tech_data], columns=tech_num_cols + tech_cat_cols)

            # Run predictions
            fund_model, tech_model, scaler = load_models()
            raw_tech = tech_model.predict(df_t)[0]
            raw_fund = fund_model.predict(df_f)[0]
            tech_score, fund_score = scaler.transform([[raw_tech, raw_fund]])[0]
            final_score = np.clip(
                (fund_score * fund_weight/100) + (tech_score * tech_weight/100),
                0, 10
            )

        # --- Display breakdown immediately ---
        st.subheader("📈 Rating Breakdown")
        st.write(f"- Fundamental Score: **{fund_score:.2f} / 10**")
        st.write(f"- Technical Score: **{tech_score:.2f} / 10**")
        st.write(f"- **Combined Investment Rating: {final_score:.2f} / 10**")

        # --- Explanatory Sections below breakdown ---
        st.divider()
        st.header("How It Works")
        st.markdown("""
- **Fundamental Data**: WRDS Compustat (Jan 2015 – Dec 2024) containing 8,612 rows and using financial metrics like current assets, net income, liabilities, etc.
- **Technical Data**: Real-time prices & indicators from Yahoo Finance (monthly return, volatility, moving averages, etc.) containing 26,105 rows.
- **Models**: Two separate scikit-learn pipelines:
    - Fundamental model predicts a Piotroski F-score
    - Technical model predicts a Sharpe ratio

These are combined via user-chosen weights into a final **1–10 Investment Rating**.
        """)
        st.divider()
        st.header("📚 Inputs & Targets")
        st.markdown("""
- **Fundamental Features** (18 numeric + 1 categorical):  
  current_assets, total_assets, common_equity_total, … , dividends_per_share_quarter, price_low_quarter, gics_sector_x

- **Technical Features** (7 numeric + 1 categorical):  
  monthly_return, month_trading_volume, stdev, avg_ret_6m, avg_ret_12m, vol_6m, vol_12m, gics_sector_x

- **Targets**:
    - Fundamental → f_score (Piotroski)
    - Technical → sharpe_ratio
        """)
        st.divider()
        st.header("What the Investment Rating Means")
        st.markdown("""
- **1–3 → Risky Investment** 🔴  
  Higher risk, consider selling or avoiding.

- **3–6 → Moderate Investment** 🟡  
  Balanced risk, hold or monitor closely.

- **6–10 → Safer Investment** 🟢  
  Lower risk, consider buying.
        """)

if __name__ == "__main__":
    main()
