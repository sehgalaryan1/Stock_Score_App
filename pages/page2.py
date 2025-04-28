import streamlit as st
import yfinance as yf
import pandas as pd

# Cache ticker list for dropdown
@st.cache_data
def load_ticker_list():
    # … your list of tickers …
    return tickers

def main():
    st.title("📈 Technical Analysis")

    tickers = load_ticker_list()
    ticker = st.selectbox(
        "Select Stock Ticker",
        options=tickers,
        index=tickers.index('AAPL'),
        help="Start typing to filter…"
    )

    if st.button("Show Technical Metrics"):
        with st.spinner(f"Loading 2 years of data for {ticker}…"):
            df = yf.download(ticker, period="2y", interval="1d", progress=False)

        if df is None or df.empty:
            st.error("No data found. Check the ticker and try again.")
            return

        df = df.reset_index()
        df["Date"] = pd.to_datetime(df["Date"])
        df.set_index("Date", inplace=True)

        # ——— Big Title ———
        st.header(f"📊 {ticker} (Last 2 Years)")

        # ——— Monthly Returns ———
        st.subheader("Monthly Returns")
        try:
            monthly_returns = df["Close"].pct_change().dropna().resample('M').sum()
            if not monthly_returns.empty:
                st.line_chart(monthly_returns)
            else:
                st.write("No monthly returns data available.")
        except Exception as e:
            st.error(f"Error calculating monthly returns: {e}")

        # ——— Monthly Volume ———
        st.subheader("Monthly Trading Volume")
        try:
            monthly_volume = df['Volume'].resample('M').sum()
            if not monthly_volume.empty:
                st.line_chart(monthly_volume)
            else:
                st.write("No monthly volume data available.")
        except Exception as e:
            st.error(f"Error calculating monthly volume: {e}")

        # ——— 30-Day Rolling Volatility ———
        st.subheader("30-Day Rolling Volatility")
        try:
            vol = df["Close"].pct_change().dropna().rolling(window=30).std()
            if not vol.empty:
                st.line_chart(vol)
            else:
                st.write("No volatility data available.")
        except Exception as e:
            st.error(f"Error calculating volatility: {e}")

        # ——— 30-Day Rolling Sharpe Ratio ———
        st.subheader("30-Day Rolling Sharpe Ratio")
        try:
            ret = df["Close"].pct_change().dropna()
            sr = ret.rolling(window=30).mean() / ret.rolling(window=30).std()
            if not sr.empty:
                st.line_chart(sr)
            else:
                st.write("No Sharpe Ratio data available.")
        except Exception as e:
            st.error(f"Error calculating Sharpe Ratio: {e}")

if __name__ == "__main__":
    main()
