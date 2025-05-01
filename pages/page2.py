# pages/page2.py
import streamlit as st
import yfinance as yf
import pandas as pd

@st.cache_data
def load_ticker_list():
    tickers = [
        'MSFT', 'NVDA', 'GOOG', 'GOOGL', 'AMZN', 'META', 'AAPL', 'BRK.B', 'AVGO', 'TSLA',
        # (rest of your full ticker list remains unchanged)
        'WDFC', 'FTDR', 'HIW', 'TMDX', 'FBP', 'PRVA', 'UCB', 'ABM', 'FULT'
    ]
    return tickers

def main():
    st.title("📈 Technical Analysis")

    tickers = load_ticker_list()
    ticker = st.selectbox(
        "Select or Type a Stock Ticker",
        options=tickers,
        index=tickers.index('MSFT'),
        help="Start typing to filter…"
    )

    if st.button("Show Technical Metrics"):
        with st.spinner(f"Loading data for {ticker}…"):
            yf_ticker = ticker.replace('.', '-')  # Convert BRK.B → BRK-B
            df = yf.Ticker(yf_ticker).history(period="2y", interval="1d")

        if df is None or df.empty:
            st.error("No data found. Check the ticker and try again.")
            return

        df = df.reset_index()
        df["Date"] = pd.to_datetime(df["Date"])
        df.set_index("Date", inplace=True)

        # Annualized 2-year Sharpe Ratio
        try:
            daily_ret = df["Close"].pct_change().dropna()
            monthly_ret = (1 + daily_ret).resample("M").prod() - 1
            sharpe = float(monthly_ret.mean() / monthly_ret.std() * (12 ** 0.5))
            st.subheader(f"Sharpe Ratio: {sharpe:.2f}")
        except Exception as e:
            st.error(f"Error computing Sharpe Ratio: {e}")

        # Monthly Returns
        st.subheader("Monthly Returns")
        try:
            monthly_returns = df["Close"].pct_change().dropna().resample('M').sum()
            if not monthly_returns.empty:
                st.line_chart(monthly_returns)
            else:
                st.write("No monthly returns data available.")
        except Exception as e:
            st.error(f"Error calculating monthly returns: {e}")

        # Monthly Trading Volume
        st.subheader("Monthly Trading Volume")
        try:
            monthly_volume = df['Volume'].resample('M').sum()
            if not monthly_volume.empty:
                st.line_chart(monthly_volume)
            else:
                st.write("No monthly volume data available.")
        except Exception as e:
            st.error(f"Error calculating monthly volume: {e}")

        # 30-Day Rolling Volatility
        st.subheader("30-Day Rolling Volatility")
        try:
            vol = df["Close"].pct_change().dropna().rolling(window=30).std()
            if not vol.empty:
                st.line_chart(vol)
            else:
                st.write("No volatility data available.")
        except Exception as e:
            st.error(f"Error calculating volatility: {e}")

        # 30-Day Rolling Sharpe Ratio
        st.subheader("30-Day Rolling Sharpe Ratio")
        try:
            ret = df["Close"].pct_change().dropna()
            sr = (ret.rolling(window=30).mean() / ret.rolling(window=30).std()) * (12 ** 0.5)
            if not sr.empty:
                st.line_chart(sr)
            else:
                st.write("No Sharpe Ratio data available.")
        except Exception as e:
            st.error(f"Error calculating Sharpe Ratio: {e}")

if __name__ == "__main__":
    main()
