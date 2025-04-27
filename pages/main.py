import streamlit as st
import page1    # Stock Input & Score page
import page2    # Technical Analysis page
import page3    # Fundamental Analysis page
import page4    # Model & Score Explanation page
import page5    # Documentation & Assumptions page

st.set_page_config(
    page_title="Stock Advisory Tool",
    page_icon="📊",
    layout="wide"
)

# --- Sidebar Navigation ---
st.sidebar.title("🔗 Navigation")
choice = st.sidebar.radio("Go to", [
    "Home",
    "Stock Input & Score",
    "Technical Analysis",
    "Fundamental Analysis",
    "Model & Score Explanation",
    "Documentation & Assumptions",
])

# --- Page Routing ---
if choice == "Home":
    st.title("📊 Welcome to the Stock Advisory Tool")
    st.markdown("""
---
### 📚 Introduction  
Investing is both an art and a science — and we’re here to make it smarter and simpler for you.

In today’s fast-moving markets, successful investing requires more than just watching the headlines.  
It demands a balanced view of a company’s **long-term financial health** and its **short-term market momentum**.

That’s why we built the **Stock Advisory Tool** — a data-driven platform that helps you make more informed investment decisions with just a few clicks.

---
### 🔍 What This App Does  
Our tool combines the power of:
- 📚 **Fundamental Analysis** (deep dives into company financials)  
- 📈 **Technical Analysis** (studying price movements and market trends)  

to generate a **1–10 investment rating** based on:
1. **Historical financial strength** (key ratios like ROE, profit margin, debt levels)  
2. **Recent market behavior** (momentum, volatility, technical patterns)

---
### 🧠 How It Works  
- We pull historical financial data from WRDS Compustat (2000–2024) to assess fundamentals.  
- We fetch real-time price and indicator data via the Yahoo Finance API to capture market sentiment.  
- A hybrid ML system (logistic regression, decision trees, rule-based logic) blends these into a final risk score.

---
### 📈 Why It Matters  
Investment decisions are never black and white. Our app cuts through the noise by showing:
- **What** the company is (fundamentally strong or weak)  
- **How** the market feels about it (rising or falling)  

You can also drill into detailed ratios and charts for deeper context.

---
### 🚀 Get Started Now  
1. Enter a stock ticker  
2. Review the 1–10 investment rating  
3. Adjust fundamental vs. technical weightings to match your style  

Use the **sidebar** to navigate to any section!
""")

elif choice == "Stock Input & Score":
    page1.main()

elif choice == "Technical Analysis":
    page2.main()

elif choice == "Fundamental Analysis":
    page3.main()

elif choice == "Model & Score Explanation":
    page4.main()

elif choice == "Documentation & Assumptions":
    page5.main()

