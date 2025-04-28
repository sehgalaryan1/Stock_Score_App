import streamlit as st

def main():
    st.title("Limitations & Next Steps")

    # Limitations section
    st.header("Limitations")
    st.markdown("""
- **Historical Lag**  
  Fundamentals update quarterly; may not reflect very recent events.
- **Market Noise**  
  Technical indicators can mislead during volatile swings.
- **Model Assumptions**  
  Random Forest and rule-based logic assume stationarity; may not capture sudden regime changes.
    """)

    # Next Steps section
    st.header("Next Steps")
    st.markdown("""
1. **Enrich Data Sources**  
   Integrate additional fundamentals from WRDS and real-time news sentiment.  
2. **Advanced Metrics**  
   Add Bollinger Bands, MACD crossovers, OBV heatmaps.  
3. **Explainability**  
   Surface SHAP or LIME explanations for each score.  
4. **Backtesting Module**  
   Let users backtest the rating strategy on historical data.  
5. **Multi-Ticker View**  
   Compare ratings across a watchlist side by side.  
6. **Alerts & Notifications**  
   Email or Slack alerts when ratings cross your thresholds.  
7. **Export & Reporting**  
   PDF/CSV export of scores and charts for easy sharing.
    """)

    st.markdown("---")
    st.markdown(
        "<span style='color:gray;'>**Disclaimer:** This tool is provided “as-is” for educational purposes. Always conduct your own due diligence and consult a financial advisor before making investment decisions.</span>",
        unsafe_allow_html=Tr

