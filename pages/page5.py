import streamlit as st

def main():
    st.title("📚 Documentation & Assumptions")

    st.markdown("""
### How It Works
- **Fundamental Data**: WRDS Compustat (Jan 2015 – Dec 2024; 8,612 rows) – uses financial metrics like current assets, net income, liabilities, etc.
- **Technical Data**: Real-time prices & indicators from Yahoo Finance (monthly return, volatility, moving averages, etc.; 26,105 rows)
- **Models**: Two separate scikit-learn pipelines  
  - Fundamental model predicts a Piotroski F-score  
  - Technical model predicts a Sharpe ratio  

These are combined via user-chosen weights into a final **0–10 Investment Rating**.

### What the Investment Rating Means
- **1–3 → Risky Investment** 🔴  
  Higher risk, consider selling or avoiding.
- **4–5 → Moderate Investment** 🟡  
  Balanced risk, hold or monitor closely.
- **6–10 → Safer Investment** 🟢  
  Lower risk, consider buying.

### Limitations
- **Historical Lag**: Fundamentals update quarterly; may not reflect real-time events.  
- **Market Noise**: Technical indicators can give false signals in volatile markets.  
- **Model Assumptions**: Random Forest and rule-based logic assume stationarity and may not adapt to regime shifts.

---
**Disclaimer:**  
This tool is provided **“as-is”** for educational purposes. Always conduct your own due diligence and consult a financial advisor before making investment decisions.
""")

if __name__ == "__main__":
    main()

