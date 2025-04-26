import streamlit as st

# ——— Introduction ———
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

st.markdown("🚀 **Get Started Now**")
st.write("""
Use the side-bar to navigate:  
1. 🔍 Stock Input & Score  
2. 📈 Technical Analysis  
3. 🧾 Fundamentals  
4. 🤖 Model Insights  
5. 📚 Docs / About
""")
# Sidebar inputs for ticker symbol and dates
ticker_symbol = st.sidebar.text_input("Enter Stock Ticker (e.g., AAPL, MSFT)", value="MSFT")

# Print update onb which ticker and dates
st.write(f"You have selected *{ticker_symbol}*.")
# st.markdown(''':red[Now click on] :blue-background[Page 1, 2 or 3] to the left to view analyses.''')

# Access the stock data for the given tocker using the yfinance "download" function
# Temporarily store data in "df" dataframe
df = yf.download(ticker_symbol)
if df.empty:
   st.error("No data found. Please check the ticker symbol or date range.")
   st.stop()


#  Note: The stock info dataframe (df) is stored in a StreamLit "session state" that allows the data to be shared across
#        the mutiple pages (ie, main.py, page1.py, page2.py and page4.py)
st.session_state.data = df
