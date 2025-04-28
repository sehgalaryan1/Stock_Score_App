import streamlit as st

def main():
    st.title("📚 Limitations & Next Steps")

    st.markdown("""
### Limitations
- **Historical Lag**: Fundamentals update quarterly; may not reflect very recent events.  
- **Market Noise**: Technical indicators can mislead during volatile swings.  
- **Model Assumptions**: Random Forest and rule-based logic assume stationarity; may not capture sudden regime changes.

---
**Disclaimer:**  
This tool is provided **“as-is”** for educational purposes. Always conduct your own due diligence and consult a financial advisor before making investment decisions.

---
### Next Steps
- **Enrich Data Sources**  
  Integrate additional fundamentals from WRDS Compustat and real-time news sentiment.  
- **Advanced Technical Metrics**  
  Add indicators like Bollinger Bands, MACD crossovers, On-Balance Volume heatmaps.  
- **Explainability**  
  Surface SHAP values or LIME explanations so users can see which features drove each score.  
- **Backtesting Module**  
  Enable users to backtest the rating strategy on historical data.  
- **Multi-Ticker Comparison**  
  Let users compare ratings across a watchlist of stocks side by side.  
- **Alerts & Notifications**  
  Build email or Slack alerts when a stock’s rating crosses a user-defined threshold.   
- **Export & Reporting**  
  Allow PDF/CSV export of scores and charts for easy sharing and record-keeping.  

---
""")

if __name__ == "__main__":
    main()
