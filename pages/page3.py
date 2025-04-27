import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

def main():
    st.title("🧾 Fundamental Analysis")

    # 1) Ticker input
    ticker = st.text_input("Enter Stock Ticker", "AAPL").upper()
    if not ticker:
        return

    # 2) Fetch fundamentals
    if st.button("Fetch Fundamentals"):
        with st.spinner(f"Loading fundamentals for {ticker}…"):
            tk = yf.Ticker(ticker)
            info = tk.info

        # 3) Extract metrics (multiplying decimals to % where appropriate)
        metrics = {
            'Return on Equity (ROE %)': info.get('returnOnEquity', 0) * 100,
            'Debt-to-Equity Ratio': info.get('debtToEquity', None),
            'EPS Growth (QoQ %)': info.get('earningsQuarterlyGrowth', 0) * 100,
            'PE Ratio': info.get('trailingPE', None),
            'Profit Margin (%)': info.get('profitMargins', 0) * 100
        }

        # 4) Build DataFrame
        df = pd.DataFrame.from_dict(metrics, orient='index', columns=['Value'])
        df.index.name = 'Metric'
        df = df.reset_index()

        # 5) Display table
        st.table(df.style.format({'Value': "{:,.2f}"}))

        # 6) Bar chart
        fig = go.Figure(go.Bar(
            x=df['Metric'],
            y=df['Value'],
            text=df['Value'].map(lambda v: f"{v:,.1f}"),
            textposition='auto'
        ))
        fig.update_layout(
            title=f"{ticker} Key Financial Ratios",
            yaxis_title="Value",
            xaxis_tickangle=-45,
            margin=dict(t=50, b=150)
        )
        st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()
   
