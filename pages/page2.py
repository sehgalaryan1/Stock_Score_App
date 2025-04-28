import streamlit as st
import yfinance as yf
import pandas as pd

def main():
    st.title("📈 Technical Analysis")

    ticker = st.text_input("Enter Stock Ticker", "AAPL").upper()
    if not ticker:
        st.warning("Please enter a ticker symbol.")
        return

    if st.button("Show Technical Metrics"):
        with st.spinner(f"Loading 1 year of data for {ticker}…"):
            hist = yf.download(ticker, period="1y", interval="1d", progress=False)

        if hist is None or hist.empty:
            st.error("No data found. Check the ticker and try again.")
            return

        # Daily returns
        daily_ret = hist['Close'].pct_change().dropna()

        # --- Calculate Metrics ---
        monthly_return = daily_ret.resample('M').sum()
        if not monthly_return.empty:
            monthly_return = monthly_return.iloc[-1]
        else:
            monthly_return = np.nan  # 마지막 1개월 누적 수익률
        month_trading_volume = hist['Volume'].resample('M').sum().iloc[-1]  # 마지막 1개월 거래량
        stdev = daily_ret.std()  # 전체 1년 수익률 변동성 (σ)
        avg_ret_6m = daily_ret.rolling(window=126, min_periods=1).mean().iloc[-1]  # 최근 6개월 평균 수익률
        vol_6m = daily_ret.rolling(window=126, min_periods=1).std().iloc[-1]  # 최근 6개월 수익률 변동성

        # --- Display Metrics ---
        st.subheader(f"📊 Key Technical Metrics for {ticker}")
        metrics = {
    "Monthly Return (Last Month)": f"{monthly_return:.2%}" if pd.notna(monthly_return) else "N/A",
    "Monthly Trading Volume": f"{month_trading_volume:,.0f}" if month_trading_volume is not None and not pd.isna(month_trading_volume) else "N/A",
    "Standard Deviation (1Y)": f"{stdev:.2%}" if stdev is not None and not pd.isna(stdev) else "N/A",
    "Average Return (6M)": f"{avg_ret_6m:.2%}" if avg_ret_6m is not None and not pd.isna(avg_ret_6m) else "N/A",
    "Volatility (6M)": f"{vol_6m:.2%}" if vol_6m is not None and not pd.isna(vol_6m) else "N/A",
}
        
        for key, value in metrics.items():
            st.write(f"- **{key}**: {value}")

        st.divider()

        # --- Optional: Closing Price Chart ---
        st.subheader(f"📈 {ticker} Closing Price (Last 6 Months)")
        df_plot = hist[-126:].copy()
        df_plot = df_plot.reset_index()
        df_plot["Date"] = df_plot["Date"].dt.date
        df_plot.set_index("Date", inplace=True)
        st.line_chart(df_plot["Close"])

if __name__ == "__main__":
    main()


# import streamlit as st
# import yfinance as yf

# def main():
#     st.title("📈 Technical Analysis")

#     ticker = st.text_input("Enter Stock Ticker", "AAPL").upper()
#     if not ticker:
#         st.warning("Please enter a ticker symbol.")
#         return

#     if st.button("Show Closing Price Chart"):
#         with st.spinner(f"Loading 6 months of data for {ticker}…"):
#             df = yf.download(ticker, period="6mo", interval="1d", progress=False)

#         if df is None or df.empty:
#             st.error("No data found. Check the ticker and try again.")
#             return

#         # Make Date just the day (drop the timestamp) for a cleaner x-axis
#         df = df.reset_index()
#         df["Date"] = df["Date"].dt.date
#         df.set_index("Date", inplace=True)

#         st.subheader(f"{ticker} Closing Price (Last 6 Months)")
#         st.line_chart(df["Close"])

# if __name__ == "__main__":
#     main()
