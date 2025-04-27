import streamlit as st
import yfinance as yf
import plotly.express as px

def main():
    st.title("📈 Technical Analysis (Simple)")

    ticker = st.text_input("Enter Stock Ticker", "AAPL").upper()
    if not ticker:
        return

    if st.button("Fetch Price Chart"):
        with st.spinner(f"Loading 6 months of daily data for {ticker}…"):
            try:
                df = yf.download(ticker, period="6mo", interval="1d", progress=False)
            except Exception as e:
                st.error(f"Error fetching data: {e}")
                return

        if df is None or df.empty:
            st.error("No data found. Check the ticker and try again.")
            return

        # Use the DataFrame index directly for the x‐axis
        fig = px.line(
            x=df.index,
            y=df["Close"],
            labels={"x": "Date", "y": "Close Price"},
            title=f"{ticker} Closing Price (Last 6 Months)"
        )
        st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
