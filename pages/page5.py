import streamlit as st

def main():
    st.title("📚 Limitations & Next Steps")

    # Limitations section
    st.header("Limitations")
    st.markdown("""
1. **Historical Lag**  
  Fundamentals update quarterly; may not reflect very recent events.
2. **Market Noise**  
  Technical indicators can mislead during volatile swings.
3. **Model Assumptions**  
  Random Forest and rule-based logic assume stationarity; may not capture sudden regime changes.
    """)

    # Next Steps section
    st.header("Next Steps")
    st.markdown("""
- **Enrich Data Sources**  
   Integrate additional fundamentals from WRDS and real-time news sentiment.  
- **Advanced Metrics**  
   Add Bollinger Bands, MACD crossovers, OBV heatmaps.  
- **Explainability**  
   Surface SHAP or LIME explanations for each score.  
- **Backtesting Module**  
   Let users backtest the rating strategy on historical data.  
- **Multi-Ticker View**  
   Compare ratings across a watchlist side by side.  
- **Alerts & Notifications**  
   Email or Slack alerts when ratings cross your thresholds.  
- **Export & Reporting**  
   PDF/CSV export of scores and charts for easy sharing.
    """)

    st.markdown("---")

    # New Methodology Files section
    st.header("📁 Methodology Files from GitHub")
    st.markdown("""
View the core notebooks and code used in building this application:

[https://github.com/sehgalaryan1/Stock_Score_App](https://github.com/sehgalaryan1/Stock_Score_App)
    """)

    st.markdown("---")
    st.markdown(
        "<span style='color:gray;'>**Disclaimer:** This tool is provided “as-is” for educational purposes. Always conduct your own due diligence and consult a financial advisor before making investment decisions.</span>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()

