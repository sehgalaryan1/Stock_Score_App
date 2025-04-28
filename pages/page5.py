import streamlit as st

def main():
    st.title("📚 Limitations & Next Steps")

    st.markdown("""

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

