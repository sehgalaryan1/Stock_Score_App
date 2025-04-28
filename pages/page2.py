import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np

# Cache ticker list for dropdown
@st.cache_data
def load_ticker_list():
    tickers = [
        'AAPL', 'MSFT', 'NVDA', 'GOOG', 'GOOGL', 'AMZN', 'META', 'BRK.B', 'AVGO', 'TSLA'
        # add more tickers as needed
    ]
    return list(dict.fromkeys(tickers))


def main():
    st.title("📈 Technical Analysis")

    # ticker selector with dropdown + filter
    tickers = load_ticker_list()
    ticker = st.selectbox(
        "Select Stock Ticker", options=tickers, index=tickers.index('AAPL'), help="Start typing to filter…"
    )

    if st.button("Show Technical Metrics"):
        with st.spinner(f"Loading 2 years of data for {ticker}…"):
            df = yf.download(ticker, period="2y", interval="1d", progress=False)

        if df is None or df.empty:
            st.error("No data found. Check the ticker and try again.")
            return

        # Date formatting
        df = df.reset_index()
        df["Date"] = pd.to_datetime(df["Date"])
        df.set_index("Date", inplace=True)

        # --- Monthly Return Line Chart (2 years) ---
        st.subheader(f"📊 {ticker} Monthly Returns (Last 2 Years)")
        try:
            daily_ret = df["Close"].pct_change().dropna()
            monthly_returns = daily_ret.resample('M').sum()
            if not monthly_returns.empty:
                st.line_chart(monthly_returns)
            else:
                st.write("No monthly returns data available.")
        except Exception as e:
            st.error(f"Error calculating monthly returns: {e}")

        # --- Monthly Trading Volume Chart (2 years) ---
        st.subheader(f"📊 {ticker} Monthly Trading Volume (Last 2 Years)")
        try:
            monthly_volume = df['Volume'].resample('M').sum()
            if not monthly_volume.empty:
                st.line_chart(monthly_volume)
            else:
                st.write("No monthly volume data available.")
        except Exception as e:
            st.error(f"Error calculating monthly volume: {e}")

        # --- 30-Day Rolling Volatility Chart (2 years) ---
        st.subheader(f"📊 {ticker} 30-Day Rolling Volatility (Last 2 Years)")
        try:
            daily_ret = df["Close"].pct_change().dropna()
            rolling_volatility = daily_ret.rolling(window=30).std()
            if not rolling_volatility.empty:
                st.line_chart(rolling_volatility)
            else:
                st.write("No volatility data available.")
        except Exception as e:
            st.error(f"Error calculating volatility: {e}")

        # --- 30-Day Rolling Sharpe Ratio Chart (2 years) ---
        st.subheader(f"📊 {ticker} 30-Day Rolling Sharpe Ratio (Last 2 Years)")
        try:
            daily_ret = df["Close"].pct_change().dropna()
            rolling_mean = daily_ret.rolling(window=30).mean()
            rolling_std = daily_ret.rolling(window=30).std()
            rolling_sharpe = rolling_mean / rolling_std
            if not rolling_sharpe.empty:
                st.line_chart(rolling_sharpe)
            else:
                st.write("No Sharpe Ratio data available.")
        except Exception as e:
            st.error(f"Error calculating Sharpe Ratio: {e}")

if __name__ == "__main__":
    main()
