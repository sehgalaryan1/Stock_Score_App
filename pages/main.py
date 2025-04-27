import streamlit as st

st.set_page_config(page_title="Stock Advisory Tool", page_icon="📊", layout="wide")

st.title("📊 Welcome to the Stock Advisory Tool")

st.markdown("""
---
### 📚 Introduction
Investing is both an art and a science — and we’re here to make it smarter and simpler for you.

In today’s fast-moving markets, successful investing requires more than just watching the headlines.
It demands a balanced view of a company’s **long-term financial health** and its **short-term market momentum**.

That's why we built this tool — a data-driven platform that helps you make informed investment decisions in just a few clicks.

---
### 🔍 What This App Does
Our tool combines:
- 📚 **Fundamental Analysis** (financial ratios like ROE, profit margin, debt levels)
- 📈 **Technical Analysis** (price momentum, volatility, technical patterns)

to generate a **1–10 investment rating**.

---
### 🧠 How It Works
- Pulls historical financial data (WRDS Compustat 2000–2024)
- Fetches real-time stock price and technical indicators (Yahoo Finance)
- Blends rule-based logic and machine learning (Logistic Regression, Decision Trees)

---
### 📈 Why It Matters
Our app helps you cut through the noise by showing:
- How strong a company fundamentally is
- How the market currently feels about it

---
### 🚀 Get Started
1. Enter a stock ticker
2. Review your investment rating
3. Explore detailed analysis pages
4. Adjust fundamental vs. technical weightings

---
### 🔗 Navigate Using Sidebar
Use the sidebar 👉 to explore different analysis pages.
""")
