# pages/3_Technical_Analysis.py

import streamlit as st
import plotly.graph_objects as go

st.markdown("📈 **Technical Analysis**")

if "data" not in st.session_state:
    st.warning("Please go back to Home and select a ticker first.")
else:
    df = st.session_state.data

    # — 1) Candlestick + 20-day SMA + Bollinger Bands —
    fig = go.Figure()
    fig.add_trace(go.Candlestick(
        x=df.index,
        open=df["Open"],
        high=df["High"],
        low=df["Low"],
        close=df["Close"],
        name="Price"
    ))
    sma20 = df["Close"].rolling(20).mean()
    fig.add_trace(go.Scatter(
        x=df.index,
        y=sma20,
        name="20-day SMA"
    ))
    upper = sma20 + 2 * df["Close"].rolling(20).std()
    lower = sma20 - 2 * df["Close"].rolling(20).std()
    fig.add_trace(go.Scatter(
        x=df.index,
        y=upper,
        name="BB Upper",
        line={"dash": "dash"}
    ))
    fig.add_trace(go.Scatter(
        x=df.index,
        y=lower,
        name="BB Lower",
        line={"dash": "dash"}
    ))
    st.plotly_chart(fig, use_container_width=True)

    # — 2) RSI (14-day) —
    delta = df["Close"].diff()
    up, down = delta.clip(lower=0), -delta.clip(upper=0)
    rs = up.rolling(14).mean() / down.rolling(14).mean()
    rsi = 100 - (100 / (1 + rs))
    rsi_fig = go.Figure(go.Scatter(x=df.index, y=rsi, name="RSI"))
    rsi_fig.add_hline(70, line_dash="dot")
    rsi_fig.add_hline(30, line_dash="dot")
    st.plotly_chart(rsi_fig, use_container_width=True)

    # — 3) On-Balance Volume (OBV) —
    direction = df["Close"].diff().apply(lambda x: 1 if x > 0 else (-1 if x < 0 else 0))
    obv = (df["Volume"] * direction).cumsum()
    obv_fig = go.Figure(go.Scatter(x=df.index, y=obv, name="On-Balance Volume"))
    st.plotly_chart(obv_fig, use_container_width=True)
