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

        # Simple line chart of Close price
        fig = px.line(
            df.reset_index(),
            x="Date",
            y="Close",
            title=f"{ticker} Closing Price (6 mo)"
        )
        st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
