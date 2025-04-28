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

    if st.button("Show Technical Metrics"):
        with st.spinner(f"Loading 2 years of data for {ticker}…"):
            df = yf.download(ticker, period="2y", interval="1d", progress=False)

        if df is None or df.empty:
            st.error("No data found. Check the ticker and try again.")
            return

        df = df.reset_index()
        df["Date"] = pd.to_datetime(df["Date"])
        df.set_index("Date", inplace=True)

        # ---- Main Section Title ----
        st.markdown(f"## 📊 {ticker} Technical Metrics (Last 2 Years)")

        # --- Monthly Return ---
        try:
            daily_ret = df["Close"].pct_change().dropna()
            monthly_returns = daily_ret.resample('M').sum()

            st.markdown("### 🔷 Monthly Return")
            if not monthly_returns.empty:
                fig = go.Figure(go.Scatter(x=monthly_returns.index, y=monthly_returns.values, mode='lines'))
                fig.update_layout(showlegend=False, margin=dict(t=10, b=10), height=300)
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.write("No monthly returns data available.")
        except Exception as e:
            st.error(f"Error calculating monthly returns: {e}")

        # --- Monthly Trading Volume ---
        try:
            monthly_volume = df['Volume'].resample('M').sum()

            st.markdown("### 🔷 Monthly Trading Volume")
            if not monthly_volume.empty:
                fig = go.Figure(go.Scatter(x=monthly_volume.index, y=monthly_volume.values, mode='lines'))
                fig.update_layout(showlegend=False, margin=dict(t=10, b=10), height=300)
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.write("No monthly volume data available.")
        except Exception as e:
            st.error(f"Error calculating monthly volume: {e}")

        # --- 30-Day Rolling Volatility ---
        try:
            daily_ret = df["Close"].pct_change().dropna()
            rolling_volatility = daily_ret.rolling(window=30).std()

            st.markdown("### 🔷 30-Day Rolling Volatility")
            if not rolling_volatility.empty:
                fig = go.Figure(go.Scatter(x=rolling_volatility.index, y=rolling_volatility.values, mode='lines'))
                fig.update_layout(showlegend=False, margin=dict(t=10, b=10), height=300)
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.write("No volatility data available.")
        except Exception as e:
            st.error(f"Error calculating volatility: {e}")

        # --- 30-Day Rolling Sharpe Ratio ---
        try:
            daily_ret = df["Close"].pct_change().dropna()
            rolling_mean = daily_ret.rolling(window=30).mean()
            rolling_std = daily_ret.rolling(window=30).std()
            rolling_sharpe = rolling_mean / rolling_std

            st.markdown("### 🔷 30-Day Rolling Sharpe Ratio")
            if not rolling_sharpe.empty:
                fig = go.Figure(go.Scatter(x=rolling_sharpe.index, y=rolling_sharpe.values, mode='lines'))
                fig.update_layout(showlegend=False, margin=dict(t=10, b=10), height=300)
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.write("No Sharpe Ratio data available.")
        except Exception as e:
            st.error(f"Error calculating Sharpe Ratio: {e}")

if __name__ == "__main__":
    main()
# import streamlit as st
# import yfinance as yf
# import pandas as pd
# import plotly.graph_objects as go

# def main():
#     st.title("🧾 Fundamental Analysis")

#     # 1) Ticker input
#     ticker = st.text_input("Enter Stock Ticker", "AAPL").upper()
#     if not ticker:
#         return

#     # 2) Fetch fundamentals
#     if st.button("Fetch Fundamentals"):
#         with st.spinner(f"Loading fundamentals for {ticker}…"):
#             tk = yf.Ticker(ticker)
#             info = tk.info

#         # 3) Extract metrics (multiplying decimals to % where appropriate)
#         metrics = {
#             'Return on Equity (ROE %)': info.get('returnOnEquity', 0) * 100,
#             'Debt-to-Equity Ratio': info.get('debtToEquity', None),
#             'EPS Growth (QoQ %)': info.get('earningsQuarterlyGrowth', 0) * 100,
#             'PE Ratio': info.get('trailingPE', None),
#             'Profit Margin (%)': info.get('profitMargins', 0) * 100
#         }

#         # 4) Build DataFrame
#         df = pd.DataFrame.from_dict(metrics, orient='index', columns=['Value'])
#         df.index.name = 'Metric'
#         df = df.reset_index()

#         # 5) Display table
#         st.table(df.style.format({'Value': "{:,.2f}"}))

#         # 6) Bar chart
#         fig = go.Figure(go.Bar(
#             x=df['Metric'],
#             y=df['Value'],
#             text=df['Value'].map(lambda v: f"{v:,.1f}"),
#             textposition='auto'
#         ))
#         fig.update_layout(
#             title=f"{ticker} Key Financial Ratios",
#             yaxis_title="Value",
#             xaxis_tickangle=-45,
#             margin=dict(t=50, b=150)
#         )
#         st.plotly_chart(fig, use_container_width=True)

# if __name__ == "__main__":
#     main()
