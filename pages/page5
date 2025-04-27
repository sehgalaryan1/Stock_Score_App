import streamlit as st

def main():
    st.title("📚 Documentation & Assumptions")

    st.markdown("""
### How It Works
- **Fundamental Data**: WRDS Compustat (2000–2024) – uses financial metrics like current assets, net income, liabilities, etc.
- **Technical Data**: Real-time prices & indicators from Yahoo Finance (monthly return, volatility, moving averages, etc.)
- **Models**: Two separate scikit-learn pipelines
  - Fundamental model predicts a Piotroski F-score  
  - Technical model predicts a Sharpe ratio  
  These are combined via user-chosen weights into a final 0–10 risk score.

### Inputs & Targets
- **Fundamental Features**:  
  `current_assets, total_assets, common_equity_total, … , dividends_per_share_quarter, price_low_quarter`  
- **Technical Features**:  
  `monthly_return, month_trading_volume, stdev, avg_ret_6m, avg_ret_12m, vol_6m, vol_12m`  
- **Categorical**:  
  `gics_sector_x`  
- **Targets**:  
  - Fundamental → `f_score` (Piotroski)  
  - Technical → `sharpe_ratio`

### What the Score Means
- **0–3** → Low attractiveness (⚠️ consider selling)  
- **4–6** → Neutral/hold (🟡 watch closely)  
- **7–10** → High attractiveness (🟢 consider buying)  

### Limitations
- **Historical Lag**: Fundamentals update quarterly; may not reflect real-time events.  
- **Market Noise**: Technical indicators can give false signals in volatile markets.  
- **Model Assumptions**: Logistic regression and tree-based methods assume stationarity and may not adapt to regime shifts.

---
**Disclaimer:**  
This tool is provided **“as-is”** for educational purposes. Always conduct your own due diligence and consult a financial advisor before making investment decisions.
""")

if __name__ == "__main__":
    main()
