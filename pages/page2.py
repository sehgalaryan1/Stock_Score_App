import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

def main():
    st.title("📈 Technical Analysis")

    ticker = st.text_input("Enter Stock Ticker", "AAPL").upper()
    if not ticker:
        st.warning("Please enter a ticker symbol.")
        return

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
        if len(df) < 2:
            st.error("Not enough data to compute indicators.")
            return

        # --- Compute rolling stats in a separate DataFrame ---
        sma20 = df["Close"].rolling(window=20, min_periods=1).mean()
        std20 = df["Close"].rolling(window=20, min_periods=1).std().fillna(0)

        tech_inds = pd.DataFrame({
            "SMA_20": sma20,
            "BB_up": sma20 + 2 * std20,
            "BB_dn": sma20 - 2 * std20
        }, index=df.index)

        # RSI (14)
        delta = df["Close"].diff().fillna(0)
        gain = delta.clip(lower=0)
        loss = (-delta).clip(lower=0)
        avg_gain = gain.rolling(window=14, min_periods=1).mean()
        avg_loss = loss.rolling(window=14, min_periods=1).mean().replace(0, pd.NA)
        rs = avg_gain / avg_loss
        tech_inds["RSI"] = 100 - (100 / (1 + rs))

        # OBV
        signal = delta.apply(lambda x: 1 if x > 0 else -1)
        tech_inds["OBV"] = (df["Volume"] * signal).cumsum()

        # --- Join indicators back to price DF ---
        df = df.join(tech_inds)

        # --- Plot 1: Candlestick + SMA + BB ---
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
        fig1.update_layout(title=f"{ticker} Price & Bollinger Bands", xaxis_rangeslider_visible=False)
        st.plotly_chart(fig1, use_container_width=True)

        # --- Plot 2: RSI with thresholds ---
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

        # --- Plot 3: OBV line chart ---
        fig3 = go.Figure(go.Scatter(x=df.index, y=df["OBV"], name="On-Balance Volume"))
        fig3.update_layout(title=f"{ticker} On-Balance Volume")
        st.plotly_chart(fig3, use_container_width=True)

if __name__ == "__main__":
    main()
    
