import streamlit as st
import joblib
import numpy as np
import pandas as pd
import yfinance as yf

@st.cache_data
def load_ticker_list():
    tickers = [
        'MSFT', 'NVDA', 'GOOG', 'GOOGL', 'AMZN', 'META', 'AAPL','BRK.B', 'AVGO', 'TSLA',
        # …etc…
    ]
    # drop duplicates, keep original order
    return list(dict.fromkeys(tickers))

@st.cache_resource
def load_models():
    fund_model = joblib.load("model/fund_model.pkl")
    tech_model = joblib.load("model/tech_model.pkl")
    scaler     = joblib.load("model/minmax_scaler.pkl")
    return fund_model, tech_model, scaler

def main():
    st.title("Stock Input & Rating")

    # ticker selector
    tickers = load_ticker_list()
    ticker  = st.selectbox(
        "Select Stock Ticker",
        options=tickers,
        index=tickers.index("MSFT"),
        help="Start typing to filter…"
    )

    # weights
    fund_w = st.slider("Fundamental Weight (%)", 0, 100, 50)
    tech_w = 100 - fund_w
    st.markdown(f"**Fund:** {fund_w}%   |   **Tech:** {tech_w}%")

    if st.button("Compute Investment Rating"):
        st.info("Fetching live data…")

        # --- fetch fundamentals + logo ---
        tk = yf.Ticker(ticker)
        try:
            info = tk.info
        except Exception as e:
            st.error(f"Could not fetch fundamentals: {e}")
            return

        # logo
        logo_url = info.get("logo_url")
        if logo_url:
            st.image(logo_url, width=100)

        # sector / industry
        sector   = info.get("sector",   "N/A")
        industry = info.get("industry", "N/A")
        st.write(f"**Sector:** {sector}   |   **Industry:** {industry}")

        # --- build df_f (fundamentals) ---
        fund_data = {
            'current_assets':                   info.get('currentAssets', np.nan),
            'total_assets':                     info.get('totalAssets', np.nan),
            'common_equity_total':              info.get('totalStockholderEquity', np.nan),
            'current_debt':                     info.get('currentDebt', np.nan),
            'long_term_debt':                   info.get('longTermDebt', np.nan),
            'depreciation_amortization':        info.get('depreciationAndAmortization', np.nan),
            'preferred_dividends':              info.get('preferredStockDividend', np.nan),
            'current_liabilities':              info.get('currentLiabilities', np.nan),
            'total_liabilities':                info.get('totalLiab', np.nan) or info.get('totalLiabilities', np.nan),
            'net_income':                       info.get('netIncomeToCommon', np.nan),
            'pretax_income':                    info.get('pretaxIncome', np.nan),
            'total_revenue':                    info.get('totalRevenue', np.nan),
            'total_income_taxes':               info.get('incomeTaxExpense', np.nan),
            'interest_expense_total':           info.get('interestExpense', np.nan),
            'capital_expenditures':             info.get('capitalExpenditures', np.nan),
            'net_cash_flow_operating_activities': info.get('operatingCashflow', np.nan),
            'dividends_per_share_quarter':      info.get('dividendRate', np.nan),
            'price_low_quarter':                info.get('fiftyTwoWeekLow', np.nan),
            'gics_sector_x':                    sector
        }
        df_f = pd.DataFrame([fund_data])

        # --- build df_t (technicals) with ALL expected cols ---
        hist = yf.download(ticker, period="3y", interval="1d", progress=False)
        if hist.empty:
            st.error("No price history found.")
            return
