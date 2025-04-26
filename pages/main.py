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
    fund_weight   = st.slider("Fundamental Weight (%)", 0, 100, 50)
    tech_weight   = 100 - fund_weight
    st.markdown(f"**Technical Weight:** {tech_weight}%")

# ── MAIN PAGE (Home / Introduction) ──
st.markdown("📊", unsafe_allow_html=True)
st.title("Welcome to the Stock Advisory Tool")
st.write("""
**Investing is both an art and a science — and we’re here to make it smarter and simpler for you.**

In today’s fast-moving markets, successful investing requires more than just watching the headlines.  
It demands a balanced view of a company’s long-term financial health and its short-term market momentum.  
That’s why we built the Stock Advisory Tool — a data-driven platform that helps you make more informed  
investment decisions with just a few clicks.
""")

st.markdown("🔍 **What This App Does**")
st.write("""
- **Fundamental analysis:** deep dives into company financials  
- **Technical analysis:** price movements & market trends  

Enter a ticker and see a **1–10 investment rating** based on:  
1. Historical ratios (ROE, profit margin, debt levels)  
2. Recent market behavior (momentum, volatility, patterns)
""")

st.markdown("🧠 **How It Works**")
st.write("""
1. WRDS Compustat (2000–2024) for fundamentals  
2. Yahoo Finance API for real-time prices & indicators  
3. Hybrid scoring: rule-based logic + ML (logistic regression, decision trees)
""")

st.markdown("📈 **Why It Matters**")
st.write("""
- **What the company is** (fundamentally strong or weak)  
- **How the market feels** (rising or falling)  

Drill into ratios, indicators, and industry comparisons—all behind one clear rating.
""")

st.markdown("🚀 **Get Started**")
st.write(f"You’ve selected **{ticker_symbol}**, with **{fund_weight}% Fundamental** and **{tech_weight}% Technical** weightings.")

# ── FETCH & STORE DATA ──
# 1) Load price history for technical features & charts
df_price = yf.download(ticker_symbol)
if df_price.empty:
    st.error("No price data found. Check your ticker.")
    st.stop()
st.session_state.data = df_price

# 2) Load combined feature dataset for fundamentals & engineered tech features
try:
    all_combined = pd.read_csv("data/combined.csv", parse_dates=["tech_date"])
    df_combined = all_combined[all_combined["ticker"] == ticker_symbol]
    if df_combined.empty:
        st.warning("No fundamental data found for this ticker in combined.csv.")
    else:
        st.session_state.combined = df_combined
except FileNotFoundError:
    st.error("Could not find data/combined.csv; please upload it to the data/ folder.")
    st.stop()

# 3) Store weightings as decimals
st.session_state.fund_weight = fund_weight / 100.0
st.session_state.tech_weight = tech_weight  / 100.0
