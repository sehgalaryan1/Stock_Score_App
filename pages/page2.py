import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick  # <- 퍼센트 표시용

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

        # 날짜 포맷 정리
        df = df.reset_index()
        df["Date"] = pd.to_datetime(df["Date"])
        df.set_index("Date", inplace=True)

        # --- Closing Price Chart (6 months only) ---
        st.subheader(f"📈 {ticker} Closing Price (Last 6 Months)")
        df_6m = df.last('6M')
        st.line_chart(df_6m["Close"])

        # --- Monthly Return Line Chart (2 years) ---
        st.subheader(f"📊 {ticker} Monthly Returns (Last 2 Years)")

        try:
            # 1. Calculate daily return
            daily_ret = df["Close"].pct_change().dropna()

            # 2. Resample to monthly returns
            monthly_returns = daily_ret.resample('M').sum()

            if not monthly_returns.empty:
                # 📈 Matplotlib 커스텀 차트 그리기
                fig, ax = plt.subplots()
                ax.plot(monthly_returns.index, monthly_returns.values, marker='o')
                ax.set_ylabel('Monthly Return (%)')
                ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))  # 1.0 = 100%
                ax.set_title(f"{ticker} Monthly Returns (Last 2 Years)")
                plt.xticks(rotation=45)
                plt.grid(True)
                st.pyplot(fig)

            else:
                st.write("No monthly returns data available.")

        except Exception as e:
            st.error(f"Error calculating monthly returns: {e}")

if __name__ == "__main__":
    main()
#--------------------------------------------------------
# import streamlit as st
# import yfinance as yf
# import pandas as pd
# import numpy as np

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

#         # 날짜 포맷 정리
#         df = df.reset_index()
#         df["Date"] = pd.to_datetime(df["Date"])  # 꼭 datetime 포맷 유지
#         df.set_index("Date", inplace=True)

#         # --- Closing Price Chart ---
#         st.subheader(f"📈 {ticker} Closing Price (Last 6 Months)")
#         st.line_chart(df["Close"])

#         # --- Calculate and Show Monthly Return (Last Month) ---
#         st.subheader("📊 Monthly Return (Last Month)")

#         try:
#             # 1. Calculate daily return
#             daily_ret = df["Close"].pct_change().dropna()

#             # 2. Resample to monthly returns
#             monthly_returns = daily_ret.resample('M').sum()

#             # 3. Safe display
#             if not monthly_returns.empty:
#                 monthly_return_last = monthly_returns.iloc[-1].item()
#                 st.metric(label="Monthly Return", value=f"{monthly_return_last:.2%}")
#             else:
#                 st.metric(label="Monthly Return", value="N/A")

#         except Exception as e:
#             st.error(f"Error calculating monthly return: {e}")

# if __name__ == "__main__":
#     main()
# --------------------------------------------------------------------------------------------

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
