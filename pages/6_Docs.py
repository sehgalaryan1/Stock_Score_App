import streamlit as st

st.markdown("📚 **Documentation / How It Works**")

st.write("""
**Inputs:**  
- Ticker, fundamental vs technical weight  

**Data sources:**  
- Fundamentals: your combined CSV (Compustat 2000–2024)  
- Technicals: Yahoo Finance via yfinance  

**Models:**  
- **Fundamental**: RandomForest pipeline w/ scaling & one-hot  
- **Technical**: RandomForest pipeline w/ scaling & one-hot  

**Score calculation:**  
