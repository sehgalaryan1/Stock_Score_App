import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np

def main():
    st.title("📈 Technical Analysis")

    ticker = st.text_input("Enter Stock Ticker", "AAPL").upper()

    if not ticker:
        st.warning("Please enter a ticker symbol.")
        return

    if st.button("Show Technical Metrics"):
        with st.spinner(f"Fetching data for {ticker}…"):
            hist = yf.download(ticker, period="1y", interval="1d", progress=False)

        if hist is None or hist.empty:
            st.error("No data found. Check the ticker and try again.")
            return

        # --- Calculate daily return ---
        daily_ret = hist['Close'].pct_change().dropna()

        # --- Monthly Return (Last Month) ---
        monthly_returns = daily_ret.resample('M').sum()
        monthly_return = monthly_returns.iloc[-1] if not monthly_returns.empty else np.nan

        # --- Monthly Trading Volume (Last Month) ---
        monthly_volumes = hist['Volume'].resample('M').sum()
        month_trading_volume = monthly_volumes.iloc[-1] if not monthly_volumes.empty else np.nan

        # --- Standard Deviation (1y) ---
        stdev = daily_ret.std()

        # --- 6 Month Avg Return ---
        avg_ret_6m = daily_ret.rolling(window=126, min_periods=1).mean().iloc[-1]

        # --- 6 Month Volatility (Std Dev) ---
        vol_6m = daily_ret.rolling(window=126, min_periods=1).std().iloc[-1]

        # --- Display Key Metrics ---
        st.subheader(f"📊 Key Technical Metrics for {ticker}")

        metrics = {
            "Monthly Return (Last Month)": f"{monthly_return:.2%}" if not pd.isna(monthly_return) else "N/A",
            "Monthly Trading Volume (Last Month)": f"{month_trading_volume:,.0f}" if not pd.isna(month_trading_volume) else "N/A",
            "Annualized Volatility (1Y)": f"{stdev:.2%}" if not pd.isna(stdev) else "N/A",
            "Average Return (6M)": f"{avg_ret_6m:.2%}" if not pd.isna(avg_ret_6m) else "N/A",
            "Volatility (6M)": f"{vol_6m:.2%}" if not pd.isna(vol_6m) else "N/A",
        }

        st.table(pd.DataFrame(metrics.items(), columns=["Metric", "Value"]))

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
