import streamlit as st
import yfinance as yf
import plotly.graph_objects as go

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

        # Build a go.Figure directly
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=df.index,
            y=df["Close"],
            mode="lines",
            name="Close Price"
        ))
        fig.update_layout(
            title=f"{ticker} Closing Price (Last 6 Months)",
            xaxis_title="Date",
            yaxis_title="Close Price",
            margin=dict(t=50, b=50)
        )

        st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
