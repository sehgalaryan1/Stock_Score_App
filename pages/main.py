import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load models
@st.cache_resource
def load_models():
    fund_model = joblib.load('model/fund_model.pkl')
    tech_model = joblib.load('model/tech_model.pkl')
    return fund_model, tech_model

fund_model, tech_model = load_models()

# App Title
st.title('📈 Stock Investment Risk Scorer')

# Input Section
ticker = st.text_input('Enter Stock Ticker (e.g., AAPL)', 'AAPL')
fund_weight = st.slider('Select Fundamental Weight (%)', 0, 100, 50)
tech_weight = 100 - fund_weight

st.write(f"**Fundamental Weight:** {fund_weight}%")
st.write(f"**Technical Weight:** {tech_weight}%")

# When the button is clicked
if st.button('🔍 Score Investment Risk'):
    st.info('Fetching features and running models...')

    # --- Define expected feature columns based on your models ---
    fund_num_cols = [
        'current_assets', 'total_assets', 'common_equity_total',
        'current_debt', 'long_term_debt', 'depreciation_amortization',
        'preferred_dividends', 'current_liabilities', 'total_liabilities',
        'net_income', 'pretax_income', 'total_revenue',
        'total_income_taxes', 'interest_expense_total',
        'capital_expenditures', 'net_cash_flow_operating_activities',
        'dividends_per_share_quarter', 'price_low_quarter'
    ]
    fund_cat_cols = ['gics_sector_x']

    tech_num_cols = [
        'monthly_return', 'month_trading_volume', 'stdev',
        'avg_ret_6m', 'avg_ret_12m', 'vol_6m', 'vol_12m'
    ]
    tech_cat_cols = ['gics_sector_x']

    # --- Simulate feature input ---
    dummy_fund_features = pd.DataFrame([np.random.rand(len(fund_num_cols))], columns=fund_num_cols)
    dummy_fund_features['gics_sector_x'] = 'Information Technology'  # Dummy sector

    dummy_tech_features = pd.DataFrame([np.random.rand(len(tech_num_cols))], columns=tech_num_cols)
    dummy_tech_features['gics_sector_x'] = 'Information Technology'  # Dummy sector

    # --- Predict ---
    fund_score = fund_model.predict(dummy_fund_features)[0]
    tech_score = tech_model.predict(dummy_tech_features)[0]

    # --- Combine Scores ---
    final_score = (fund_score * fund_weight/100) + (tech_score * tech_weight/100)
    final_score = min(max(final_score, 0), 10)  # Clip between 0 and 10

    # --- Display the Score ---
    st.success(f"🎯 Investment Risk Score: **{final_score:.2f} / 10**")

    # --- Categorize Risk ---
    if final_score < 3:
        st.write("🟢 **Low Risk** - Safer Investment")
    elif final_score < 7:
        st.write("🟡 **Medium Risk** - Caution Advised")
    else:
        st.write("🔴 **High Risk** - Risky Investment")

    # --- Optional: Add a Gauge Chart ---
    try:
        import plotly.graph_objects as go
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=final_score,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "Investment Risk Score (0-10)"},
            gauge={
                'axis': {'range': [0, 10]},
                'bar': {'color': "darkblue"},
                'steps': [
                    {'range': [0, 3], 'color': 'green'},
                    {'range': [3, 7], 'color': 'yellow'},
                    {'range': [7, 10], 'color': 'red'}
                ],
            }
        ))
        st.plotly_chart(fig)
    except ImportError:
        st.warning('Plotly not installed. Install with `pip install plotly` to see the gauge chart.')
