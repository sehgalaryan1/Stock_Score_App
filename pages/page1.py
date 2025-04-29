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

        # build df_f
        fund_data = {
            'current_assets': info.get('currentAssets', np.nan),
            'total_assets':   info.get('totalAssets', np.nan),
            # …all your other fundamental fields…
        }
        df_f = pd.DataFrame([fund_data])

        # technicals
        hist = yf.download(ticker, period="3y", interval="1d", progress=False)
        if hist.empty:
            st.error("No price history found.")
            return
        monthly_close = hist["Close"].resample("M").last()
        monthly_ret   = monthly_close.pct_change() * 100
        tech_data = {
            'monthly_return': monthly_ret.iloc[-1],
            # …etc…
        }
        df_t = pd.DataFrame([tech_data])

        # predict & scale
        fund_model, tech_model, scaler = load_models()
        raw_tech = tech_model.predict(df_t)[0]
        raw_fund = fund_model.predict(df_f)[0]
        tech_score, fund_score = scaler.transform([[raw_tech, raw_fund]])[0]
        combined_score = np.clip(
            fund_score * fund_w/100 + tech_score * tech_w/100,
            0, 10
        )

        # display metrics
        c1, c2, c3 = st.columns(3)
        c1.metric("Technical Score",   f"{tech_score:.2f} / 10")
        c2.metric("Fundamental Score", f"{fund_score:.2f} / 10")
        c3.metric("Combined Score",    f"{combined_score:.2f} / 10")

        # traffic light
        if combined_score < 4:
            st.write("🔴 **Risky**")
        elif combined_score < 6:
            st.write("🟡 **Moderate**")
        else:
            st.write("🟢 **Safer**")

if __name__ == "__main__":
    main()
