import streamlit as st
import page1    # Stock Input & Score page
import page2    # Technical Analysis page
import page3    # Fundamental Analysis page
import page4    # Model & Rating Explanation page
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
    "Model & Rating Explanation",
    "Documentation & Assumptions",
])

# --- Page Routing ---
if choice == "Home":
    st.title("📊 Welcome to the Stock Advisory Tool")
    st.markdown("""
---
## 👥 Team Members
- Aryan Sehgal  
- Hyunjin Yu  
- Raskirt Bhatia  

---
### 📚 Introduction  
Investing doesn’t have to be overwhelming. Our tool brings together a company’s long-term financial health and short-term market momentum in one simple dashboard.

---
### 🔍 What This App Does  
We combine:
- **Fundamental Analysis**: Deep dive into company financials  
- **Technical Analysis**: Price action and momentum indicators  

…and deliver a clear **1–10 Investment Rating** so you can decide at a glance.

---
### 🧠 How It Works  
- We pull historical financials from WRDS Compustat (Jan 2015 – Dec 2024).  
- We fetch live price and indicator data via Yahoo Finance.  
- We blend a **Random Forest Regressor** with **rule-based logic** for a balanced view.

---
### 📈 Why It Matters  
Markets move fast. This app helps you:
- See if a company is financially solid  
- Understand how the market feels right now  
- Make data-driven decisions, not guesses

---
### 🚀 Quick Start
1. Go to **Stock Input & Score** in the sidebar.  
2. Enter your ticker and pick the balance between fundamentals vs. technicals.  
3. Click **Compute Investment Rating** to get your 1–10 score.  
4. Explore other pages for detailed charts, ratios, and model insights.

Use the sidebar to hop between pages whenever you like!
""")

elif choice == "Stock Input & Score":
    page1.main()

elif choice == "Technical Analysis":
    page2.main()

elif choice == "Fundamental Analysis":
    page3.main()

elif choice == "Model & Rating Explanation":
    page4.main()

elif choice == "Documentation & Assumptions":
    page5.main()

