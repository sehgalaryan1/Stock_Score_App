import streamlit as st

def main():
    st.title("🤖 Model & Rating Explanation")

    # --- How It Works Section ---
    st.header("How It Works")
    st.markdown("""
- **Model Training Data**: WRDS Compustat (Jan 2015 – Dec 2024) containing 26K rows and using fundamental metrics like current assets, net income, liabilities, etc. and technical metrics like return, volume, volatility, etc. 
- **Real time App Data**: Real-time technnical & fundamental indicators from Yahoo Finance. 
- **Models**: Two separate scikit-learn pipelines utilizing Random Forest Regressor. 
- **Companies for Model Training**: Top 150 companies from each of the S&P 400, S&P 500, S&P 600 indices.
    """)

    st.divider()

    # --- Inputs & Targets Section ---
    st.header("📚 Inputs & Targets")
    st.markdown("""
- **Fundamental Features** (18 numeric + 1 categorical):  
  `current_assets, total_assets, common_equity_total, … , dividends_per_share_quarter, price_low_quarter, gics_sector_x`

- **Technical Features** (7 numeric + 1 categorical):  
  `monthly_return, month_trading_volume, stdev, avg_ret_6m, avg_ret_12m, vol_6m, vol_12m, gics_sector_x`

- **Target Variables**:
    - Fundamental → `f_score` (Piotroski) 
    - Technical → `sharpe_ratio`
    
- **Rating**:
    - MinMax Scaler scales the fundamental and technical scores into two seperate ratings ranging from 1-10.
    - The final score is computed as a weighted average of the fundamental and technical ratings, using the user’s specified weightings. 
    """)

    st.divider()

    # --- Investment Rating Meaning Section ---
    st.header("What the Investment Rating Means")
    st.markdown("""
- **1–3 → Risky Investment** 🔴  
  Higher risk, consider selling or avoiding.

- **3–6 → Moderate Investment** 🟡  
  Balanced risk, hold or monitor closely.

- **6–10 → Safer Investment** 🟢  
  Lower risk, consider buying.
    """)

if __name__ == "__main__":
    main()
