# StockScore: A Multi-Page Streamlit App for Stock Analysis

An interactive, multi-page Streamlit dashboard that combines fundamental and technical analysis to dynamically rate stocks using live Yahoo Finance data and pre-trained machine learning models.

---

## 🚀 Live App  
[Launch StockScore App](https://stockscoreapp-4jbsnyaykawmponh76wn3s.streamlit.app/)  

---

## 👥 Team Members
- Raskirt Bhatia
- Aryan Sehgal
- Hyunjin Yu 

---

## 📝 Project Description
StockScore lets you enter any stock ticker and choose a weight (%) for **fundamental analysis**; the remaining weight is applied to **technical analysis**. The app fetches live data from Yahoo Finance, runs two separate ML pipelines, and delivers a combined **1–10 Investment Rating** (higher = safer).

---

## 🗂 App Structure
1. **Home Page** (`main.py`)  
   Introduction and sidebar navigation overview.  
2. **Page 1: Stock Input & Rating** (`page1.py`)  
   Enter a ticker, set fundamental vs. technical weight, and compute a live-data Investment Rating.  
3. **Page 2: Technical Analysis** (`page2.py`)  
   Simple closing-price chart (last 6 months) via Streamlit’s built-in `st.line_chart`.  
4. **Page 3: Fundamental Analysis** (`page3.py`)  
   Key financial ratios (ROE, Debt-to-Equity, EPS growth, P/E, Profit Margin) in a table and bar chart.  
5. **Page 4: Model & Rating Explanation** (`page4.py`)  
   Runs the same live inputs through both ML pipelines, shows individual model scores, combined rating, and feature importances.  
6. **Page 5: Documentation & Assumptions** (`page5.py`)  
   Detailed description of data sources, features, model targets, rating interpretation, and limitations.  

---

## 🤖 Machine Learning Models
- **Fundamental Model** (`model/fund_model.pkl`)  
  Predicts a stock rating based on key financial indicators.  
- **Technical Model** (`model/tech_model.pkl`)  
  Predicts a stock rating based on price-momentum and volume metrics.
- **Scaler** (`model/minmax_scaler.pkl`)
Converts the raw model predictions (Fundamental F-score and Technical Sharpe ratio) into a normalized rating between 1 and 10 for easier comparison across stocks.

A final combined rating (1–10) is generated based on the user-assigned weightages.

---

## 📁 Folder Structure
```bash
/pages/
  main.py
  page1.py
  page2.py
  page3.py
  page4.py
  page5.py

/model/
  fund_model.pkl
  tech_model.pkl
  minmax_scaler.pkl

/data/
  … (All datasets used for model training and evaluation)

/notebook/
  … (Jupyter notebook)

README.md  
requirements.txt


