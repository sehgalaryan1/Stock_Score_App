# StockScore: A Multi-Page Streamlit App for Stock Analysis

An interactive, multi-page Streamlit dashboard that combines fundamental and technical analysis to dynamically rate stocks using live Yahoo Finance data and machine learning models.

---

## 🚀 Live App  
[Launch StockScore App](#)  

---

## 👥 Team Members
- Aryan Sehgal  
- Raskirt Bhatia  
- Hyunjin Yu  

---

## 📝 Project Description
StockScore allows users to input a stock ticker and assign a weight (%) to fundamental analysis. The remaining weight is automatically assigned to technical analysis. The app retrieves real-time data from Yahoo Finance and provides a comprehensive breakdown across multiple pages.

---

## 🗂 App Structure
1. **Home Page** (`main.py`)  
   Introduction and navigation overview.  
2. **Page 1** (`page1.py`)  
   Stock input form, selection of fundamental weight, and quick score summary.  
3. **Page 2** (`page2.py`)  
   In-depth technical analysis (moving averages, RSI, MACD, etc.).  
4. **Page 3** (`page3.py`)  
   In-depth fundamental analysis (financial ratios, earnings, balance sheet).  
5. **Page 4** (`page4.py`)  
   ML models’ predictions and combined final score.  
6. **Page 5** (`page5.py`)  
   Documentation, assumptions, and limitations of the project.  

---

## 🤖 Machine Learning Models
The app uses two separate ML models:

- **Fundamental Model**  
  Predicts a stock rating based on key financial indicators.  
- **Technical Model**  
  Predicts a stock rating based on technical chart patterns and momentum indicators.  

A final combined rating (on a scale from 1 to 10) is generated based on the user-assigned weightages.

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
  fundamental_model.pkl
  technical_model.pkl

/data/
  … (All datasets used for model training and evaluation)

README.md
requirements.txt
