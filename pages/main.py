import streamlit as st
import page1    # Stock Input & Score page
import page2    # Technical Analysis page
import page3    # Fundamental Analysis page
import page4    # Model & Rating Explanation page
import page5    # Limitations & Next Steps page

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
    "Limitations & Next Steps",
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
### Introduction  
Investing doesn’t have to be overwhelming. Our tool brings together a company’s long-term financial health and short-term market momentum in one simple dashboard.

---
### What This App Does  
- **Fundamental Analysis**: Deep dive into company financials  
- **Technical Analysis**: Price action and momentum indicators  

…and delivers a clear **1–10 Investment Rating** so you can decide at a glance.

---
### How It Works  
1. Historical financials from WRDS Compustat (Jan 2015 – Dec 2024)  
2. Live price and indicator data via Yahoo Finance  
3. Blend of Random Forest Regressor + rule-based logic

---
### Quick Start
1. Go to **Stock Input & Score**  
2. Enter ticker & set fundamentals/technicals balance  
3. Click **Compute Investment Rating**  
4. Explore detailed charts, ratios, and explanations on other pages
""")

elif choice == "Stock Input & Score":
    page1.main()

elif choice == "Technical Analysis":
    page2.main()

elif choice == "Fundamental Analysis":
    page3.main()

elif choice == "Model & Rating Explanation":
    page4.main()

elif choice == "Limitations & Next Steps":
    page5.main()

# --- QR Code fixed at bottom-left of sidebar ---
url = "https://your-website.com"
qr_api = f"https://api.qrserver.com/v1/create-qr-code/?data={url}&size=200x200"

st.sidebar.markdown(
    f"""
    <div style="
        position: fixed;
        bottom: 20px;
        left: 10px;
        width: 200px;
        text-align: left;
        ">
      <img src="{qr_api}" alt="QR code" style="width:100%; height:auto;"/>
      <p style="
        font-size: 12px;
        margin: 4px 0 0 0;
      ">Scan to visit our site</p>
    </div>
    """,
    unsafe_allow_html=True,
)
