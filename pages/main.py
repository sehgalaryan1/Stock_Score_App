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

    # — Replace date inputs with weight slider —
    fund_weight = st.slider("Fundamental Weight (%)", min_value=0, max_value=100, value=50)
    tech_weight = 100 - fund_weight
    st.write(f"Technical Weight: **{tech_weight}%**")

# ── MAIN CONTENT (Home / Intro) ──
st.markdown("📊", unsafe_allow_html=True)
st.title("Welcome to the Stock Advisory Tool")
# … your intro copy here …

# Echo selection & weights
st.write(f"You’ve selected **{ticker_symbol}** with **{fund_weight}% Fundamental** and **{tech_weight}% Technical** weightings.")

# ── FETCH & STORE DATA ──
df = yf.download(ticker_symbol)
if df.empty:
    st.error("No data found. Check your ticker.")
    st.stop()

# Save everything to session_state for downstream pages
st.session_state.data        = df
st.session_state.fund_weight = fund_weight / 100.0
st.session_state.tech_weight = tech_weight / 100.0
