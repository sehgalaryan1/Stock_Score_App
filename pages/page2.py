import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

def main():
    st.title("📈 Technical Analysis")

    # 1) Ticker input
    ticker = st.text_input("Enter Stock Ticker", "AAPL").upper()
    if not ticker:
        st.warning("Please enter a ticker symbol.")
        return

    # 2) Fetch data when button is clicked
    if st.button("Fetch Technicals"):
        with st.spinner(f"Loading 1 year of daily data for {ticker}…"):
            try:
                df = yf.download(ticker, period="1y", interval="1d", progress=False)
            except Exception as e:
                st.error(f"Error fetching data: {e}")
                return

        if df is None or df.empty:
            st.error("No data found. Check the ticker and try again.")
            return

        # 3) Ensure enough rows for rolling calculations
        if len(df) < 2:
            st.error("Not enough data to compute indicators.")
            return

        # 4) Compute indicators with min_periods=1 so output length matches df
        df["SMA_20"] = df["Close"].rolling(window=20, min_periods=1).mean()
        std20 = df["Close"].rolling(window=20, min_periods=1).std()
        # Now std20 has the same length & index as df
        df["BB_up"] = df["SMA_20"] + 2 * std20
        df["BB_dn"] = df["SMA_20"] - 2 * std20

        # RSI
        delta = df["Close"].diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        avg_gain = gain.rolling(window=14, min_periods=1).mean()
        avg_loss = loss.rolling(window=14, min_periods=1).mean()
        rs = avg_gain / avg_loss.replace(0, pd.NA)
        df["RSI"] = 100 - (100 / (1 + rs))

        # OBV
        df["OBV"] = (df["Volume"] * ((df["Close"].diff() > 0).map({True: 1, False: -1}))).cumsum()

        # 5) Candlestick + SMA + BB chart
        fig1 = go.Figure(
            data=[
                go.Candlestick(
                    x=df.index, open=df["Open"], high=df["High"],
                    low=df["Low"], close=df["Close"], name="Price"
                ),
                go.Scatter(x=df.index, y=df["SMA_20"], name="SMA 20"),
                go.Scatter(x=df.index, y=df["BB_up"], name="BB Upper"),
                go.Scatter(x=df.index, y=df["BB_dn"], name="BB Lower"),
            ]
        )
        fig1.update_layout(
            title=f"{ticker} Price & Bollinger Bands",
            xaxis_rangeslider_visible=False
        )
        st.plotly_chart(fig1, use_container_width=True)

        # 6) RSI chart with 70/30 lines
        fig2 = go.Figure(go.Scatter(x=df.index, y=df["RSI"], name="RSI"))
        fig2.update_layout(
            title=f"{ticker} RSI (14)",
            yaxis=dict(range=[0, 100]),
            shapes=[
                dict(type="line", x0=df.index.min(), x1=df.index.max(),
                     y0=70, y1=70, line=dict(dash="dash")),
                dict(type="line", x0=df.index.min(), x1=df.index.max(),
                     y0=30, y1=30, line=dict(dash="dash")),
            ]
        )
        st.plotly_chart(fig2, use_container_width=True)

        # 7) OBV line chart
        fig3 = go.Figure(go.Scatter(x=df.index, y=df["OBV"], name="On-Balance Volume"))
        fig3.update_layout(title=f"{ticker} On-Balance Volume")
        st.plotly_chart(fig3, use_container_width=True)

if __name__ == "__main__":
    main()
