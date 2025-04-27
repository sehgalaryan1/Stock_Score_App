import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

def main():
    st.title("📈 Technical Analysis")

    # 1) Ticker input
    ticker = st.text_input("Enter Stock Ticker", "AAPL").upper()
    if not ticker:
        return

    # 2) Fetch data
    if st.button("Fetch Technicals"):
        with st.spinner(f"Loading {ticker} data…"):
            df = yf.download(ticker, period="1y", interval="1d")
        if df.empty:
            st.error("No data found. Check ticker symbol.")
            return

        # 3) Compute indicators
        df["SMA_20"] = df["Close"].rolling(20).mean()
        df["EMA_50"] = df["Close"].ewm(span=50, adjust=False).mean()
        std20 = df["Close"].rolling(20).std()
        df["BB_up"] = df["SMA_20"] + 2 * std20
        df["BB_dn"] = df["SMA_20"] - 2 * std20

        # RSI
        delta = df["Close"].diff()
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        avg_gain = gain.rolling(14).mean()
        avg_loss = loss.rolling(14).mean()
        rs = avg_gain / avg_loss
        df["RSI"] = 100 - (100 / (1 + rs))

        # OBV
        df["OBV"] = (df["Volume"] * ((df["Close"].diff() > 0) * 2 - 1)).cumsum()

        # 4) Candlestick + SMA + Bollinger
        fig1 = go.Figure(
            data=[
                go.Candlestick(
                    x=df.index,
                    open=df["Open"], high=df["High"],
                    low=df["Low"], close=df["Close"],
                    name="Price"
                ),
                go.Scatter(x=df.index, y=df["SMA_20"], name="SMA 20"),
                go.Scatter(x=df.index, y=df["BB_up"], name="BB Upper"),
                go.Scatter(x=df.index, y=df["BB_dn"], name="BB Lower"),
            ]
        )
        fig1.update_layout(title=f"{ticker} Price & Bollinger Bands", xaxis_rangeslider_visible=False)
        st.plotly_chart(fig1, use_container_width=True)

        # 5) RSI chart
        fig2 = go.Figure(go.Scatter(x=df.index, y=df["RSI"], name="RSI"))
        fig2.update_layout(title=f"{ticker} RSI (14)", yaxis=dict(range=[0, 100]), shapes=[
            dict(type="line", x0=df.index.min(), x1=df.index.max(), y0=70, y1=70, line=dict(dash="dash")),
            dict(type="line", x0=df.index.min(), x1=df.index.max(), y0=30, y1=30, line=dict(dash="dash")),
        ])
        st.plotly_chart(fig2, use_container_width=True)

        # 6) OBV chart
        fig3 = go.Figure(go.Scatter(x=df.index, y=df["OBV"], name="On-Balance Volume"))
        fig3.update_layout(title=f"{ticker} On-Balance Volume")
        st.plotly_chart(fig3, use_container_width=True)

if __name__ == "__main__":
    main()
   
