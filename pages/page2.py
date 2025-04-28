import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np  # numpy import 추가

def main():
    st.title("📈 Technical Analysis")

    ticker = st.text_input("Enter Stock Ticker", "AAPL").upper()
    if not ticker:
        st.warning("Please enter a ticker symbol.")
        return

    if st.button("Show Closing Price Chart"):
        with st.spinner(f"Loading 6 months of data for {ticker}…"):
            df = yf.download(ticker, period="6mo", interval="1d", progress=False)

        if df is None or df.empty:
            st.error("No data found. Check the ticker and try again.")
            return

        # 날짜 포맷 정리
        df = df.reset_index()
        df["Date"] = pd.to_datetime(df["Date"]).dt.date
        df.set_index("Date", inplace=True)

        # --- Closing Price Chart ---
        st.subheader(f"📈 {ticker} Closing Price (Last 6 Months)")
        st.line_chart(df["Close"])

        # --- Calculate and Show Monthly Return (Last Month) ---
        st.subheader("📊 Monthly Return (Last Month)")

        try:
            # 1. Calculate daily return
            daily_ret = df["Close"].pct_change().dropna()

            # 2. Resample to monthly return (마지막 한 달 수익률)
            daily_ret.index = pd.to_datetime(daily_ret.index)  # resample하려면 datetime 인덱스 필요
            monthly_returns = daily_ret.resample('M').sum()

            if not monthly_returns.empty:
                monthly_return_last = monthly_returns.iloc[-1]
            else:
                monthly_return_last = np.nan

            # 3. Safe display
            if not pd.isna(monthly_return_last):
                st.metric(label="Monthly Return", value=f"{monthly_return_last:.2%}")
            else:
                st.metric(label="Monthly Return", value="N/A")

        except Exception as e:
            st.error(f"Error calculating monthly return: {e}")

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
