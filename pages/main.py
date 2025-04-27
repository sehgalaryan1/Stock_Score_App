# pages/main.py
import streamlit as st
import pandas as pd
import yfinance as yf

# ── Sidebar controls ──
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
    fund_weight   = st.slider("Fundamental Weight (%)", 0, 100, 50)
    tech_weight   = 100 - fund_weight
    st.markdown(f"**Technical Weight:** {tech_weight}%")

# ── Main page content ──
st.markdown("📊", unsafe_allow_html=True)
st.title("Welcome to the Stock Advisory Tool")
st.write("""
**Investing is both an art and a science — and we’re here to make it smarter and simpler for you.**

In today’s fast-moving markets, successful investing requires more than just watching the headlines.  
It demands a balanced view of a company’s long-term financial health and its short-term market momentum.  
That’s why we built the Stock Advisory Tool — a data-driven platform that helps you make more informed  
investment decisions with just a few clicks.
""")

st.markdown("🚀 **Get Started**")
st.write(f"You’ve selected **{ticker_symbol}**, with **{fund_weight}% Fundamental** and **{tech_weight}% Technical** weightings.")

# ── Fetch & store data in session_state ──
# 1) Price history for technical pages
df_price = yf.download(ticker_symbol)
if df_price.empty:
    st.error("No price data found. Check your ticker.")
    st.stop()
st.session_state.data = df_price

# 2) Combined feature set for fundamentals & modeling
try:
    combined = pd.read_csv("data/combined.csv", parse_dates=["tech_date"])
    df_comb  = combined[combined["ticker"] == ticker_symbol]
    if df_comb.empty:
        st.warning("No fundamental data for this ticker in combined.csv.")
    else:
        st.session_state.combined = df_comb
except FileNotFoundError:
    st.error("Missing data/combined.csv – please upload it.")
    st.stop()

# 3) Save weightings
st.session_state.fund_weight = fund_weight / 100.0
st.session_state.tech_weight = tech_weight  / 100.0
