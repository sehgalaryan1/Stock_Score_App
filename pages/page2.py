import streamlit as st
import yfinance as yf

def main():
    st.title("📈 Technical Analysis")

    ticker = st.text_input("Enter Stock Ticker", "AAPL").upper()
    if not ticker:
        st.warning("Please enter a ticker symbol.")
        return

    if st.button("Show Closing Price Chart"):
        with st.spinner(f"Loading 6 months of data for {ticker}…"):
            df = yf.download(ticker, period="6mo", interval="1d", progress=False)

        if df is None or df.empty:
            st.error("No data found. Check the ticker and try again.")
            return

        # Make Date just the day (drop the timestamp) for a cleaner x-axis
        df = df.reset_index()
        df["Date"] = df["Date"].dt.date
        df.set_index("Date", inplace=True)

        st.subheader(f"{ticker} Closing Price (Last 6 Months)")
        st.line_chart(df["Close"])

if __name__ == "__main__":
    main()
