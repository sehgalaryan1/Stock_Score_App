# main.py
import streamlit as st
import pandas as pd
import yfinance as yf

# ── SIDEBAR ──
with st.sidebar:
    st.header("📊 Investment Advisory App")
    st.markdown("""
    **Navigate:**  
    - 🏠 Home  
    - 🔍 Stock Input & Score  
    - 📈 Technical Analysis  
    - 🧾 Fundamentals  
    - 🤖 Model Insights  
    - 📚 Docs  
    """)

    st.subheader("🔍 Stock Input & Score")
    ticker_symbol = st.text_input("Ticker (e.g. AAPL)", value="MSFT")
    start_date    = st.date_input("Start Date",  pd.to_datetime("2024-01-01"))
    end_date      = st.date_input("End Date",    pd.to_datetime("2024-12-31"))

# ── MAIN CONTENT (Home / Intro) ──
st.markdown("📊", unsafe_allow_html=True)
st.title("Welcome to the Stock Advisory Tool")

st.write("""
**Investing is both an art and a science — and we’re here to make it smarter and simpler for you.**

In today’s fast-moving markets, successful investing requires more than just watching the headlines.  
It demands a balanced view of a company’s long-term financial health and its short-term market momentum.  
That’s why we built the Stock Advisory Tool — a data-driven platform that helps you make more informed  
investment decisions with just a few clicks.
""")

st.markdown("🧠 **How It Works**")
st.write("""
1. WRDS Compustat (2000–2024) for fundamentals  
2. Yahoo Finance API for real-time prices & indicators  
3. Hybrid scoring: rule-based logic + ML (logistic regression, decision trees)
""")

st.markdown("🚀 **Get Started**")
st.write(f"You’ve selected **{ticker_symbol}** from **{start_date}** to **{end_date}**.  ")

# ── FETCH & STORE DATA ──
df = yf.download(ticker_symbol, start=start_date, end=end_date)
if df.empty:
    st.error("No data found. Check your ticker or date range.")
    st.stop()
st.session_state.data = df
