import streamlit as st
import page1    # Stock Input & Score page
import page2    # Technical Analysis page
import page3    # Fundamental Analysis page
import page4    # Model & Rating Explanation page
import page5    # Limitations & Next Steps page
import urllib.parse

st.set_page_config(
    page_title="Stock Advisory Tool",
    page_icon="📊",
    layout="wide"
)

# Initialize page in session state
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Callback to navigate
def navigate_to(page_name):
    st.session_state.page = page_name

# Sidebar nav, bound to session_state.page
st.sidebar.title("🔗 Navigation")
st.sidebar.radio(
    "Go to",
    [
        "Home",
        "Stock Input & Score",
        "Technical Analysis",
        "Fundamental Analysis",
        "Model & Rating Explanation",
        "Limitations & Next Steps",
    ],
    key="page",
)

# Main routing
if st.session_state.page == "Home":
    st.title("📊 Welcome to the Stock Advisory Tool")
    st.markdown("""
---
## 👥 Team Members
- Raskirt Bhatia  
- Aryan Sehgal  
- Hyunjin Yu  


---
### Introduction  
Investing doesn’t have to be overwhelming. Our tool brings together a company’s long-term financial health and short-term market momentum in one simple dashboard.

---
### What This App Does  
- **Fundamental Analysis**: Deep dive into company financials  
- **Technical Analysis**: Price action and momentum indicators  

…and delivers a clear **1–10 Investment Rating** so you can decide at a glance.

---
### Behind the Ratings 
1. Historical financials from WRDS Compustat (Jan 2015 – Dec 2024)  
2. Live price and indicator data via Yahoo Finance  
3. Blend of Random Forest Regressor 

---
### Quick Start
1. Go to **Stock Input & Score**  
2. Enter ticker & set fundamentals/technicals balance  
3. Click **Compute Investment Rating**  
4. Explore detailed charts, ratios, and explanations on other pages
""")

    # 👉 Call-to-action button
    st.button("Start Now", on_click=navigate_to, args=("Stock Input & Score",))

elif st.session_state.page == "Stock Input & Score":
    page1.main()

elif st.session_state.page == "Technical Analysis":
    page2.main()

elif st.session_state.page == "Fundamental Analysis":
    page3.main()

elif st.session_state.page == "Model & Rating Explanation":
    page4.main()

elif st.session_state.page == "Limitations & Next Steps":
    page5.main()

# QR Code fixed at bottom-left of sidebar
url = "https://stockscoreapp-4jbsnyaykawmponh76wn3s.streamlit.app/"
encoded_url = urllib.parse.quote(url, safe='')
qr_api = f"https://api.qrserver.com/v1/create-qr-code/?data={encoded_url}&size=150x150"

st.sidebar.markdown(
    f"""
    <div style="
        position: fixed;
        bottom: 20px;
        left: 10px;
        width: 150px;
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
