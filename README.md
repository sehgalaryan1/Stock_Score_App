StockScore: A Multi-Page Streamlit App for Stock Analysis
An interactive, multi-page Streamlit dashboard that combines fundamental and technical analysis to dynamically rate stocks using live Yahoo Finance data and machine learning models.

Live App
👉 Launch StockScore App

Team Members
Aryan Sehgal

Raskirt Bhatia

Hyunjin Yu

Project Description
StockScore allows users to input a stock ticker and assign a weight (%) to fundamental analysis. The remaining weight is automatically assigned to technical analysis. The app retrieves real-time data from Yahoo Finance and provides a comprehensive breakdown across multiple pages:

App Structure
Home Page (main.py): Introduction and navigation overview.

Page 1 (page1.py): Stock input form, selection of fundamental weight, and quick score summary.

Page 2 (page2.py): In-depth technical analysis (moving averages, RSI, MACD, etc.).

Page 3 (page3.py): In-depth fundamental analysis (financial ratios, earnings, balance sheet).

Page 4 (page4.py): ML models’ predictions and combined final score.

Page 5 (page5.py): Documentation, assumptions, and limitations of the project.

The app uses two machine learning models:

Fundamental Model: Predicts a stock rating based on key financial indicators.

Technical Model: Predicts a stock rating based on technical chart patterns and momentum indicators.

A combined final rating (1-10) is then calculated based on the user-assigned weightages.

Folder Structure
/pages/ — Contains all the page scripts (main.py, page1.py, ..., page5.py).

/model/ — Contains .pkl files for the trained ML models.

/data/ — Contains the datasets used for model training and evaluation.

Key Features
Live stock data fetching using Yahoo Finance.

User-controlled weightage between technical and fundamental analysis.

Two ML models providing independent and combined stock scores.

Documentation and assumptions clearly laid out within the app.

Multi-page architecture with Streamlit session state management.

Requirements
All necessary libraries are listed in the requirements.txt file. Some key libraries:

streamlit

yfinance

scikit-learn

pandas

numpy

matplotlib

seaborn
