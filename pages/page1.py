import streamlit as st
import joblib
import numpy as np
import pandas as pd
import yfinance as yf

@st.cache_data
def load_ticker_list():
    tickers = [
        'MSFT', 'NVDA', 'GOOG', 'GOOGL', 'AMZN', 'META', 'AAPL','BRK.B', 'AVGO', 'TSLA',
        'WMT', 'LLY', 'JPM', 'V', 'UNH', 'MA', 'XOM', 'COST', 'NFLX', 'PG',
        'ORCL', 'JNJ', 'HD', 'ABBV', 'KO', 'TMUS', 'BAC', 'PM', 'CRM', 'CVX',
        'PLTR', 'CSCO', 'MCD', 'IBM', 'ABT', 'LIN', 'WFC', 'GE', 'MRK', 'T',
        'PEP', 'VZ', 'AXP', 'ACN', 'MS', 'ISRG', 'RTX', 'NOW', 'TMO', 'INTU',
        'PGR', 'AMGN', 'GS', 'UBER', 'AMD', 'DIS', 'QCOM', 'BKNG', 'ADBE', 'SPGI',
        'TJX', 'CAT', 'SCHW', 'BSX', 'NEE', 'BLK', 'TXN', 'DHR', 'SYK', 'UNP',
        'GILD', 'CMCSA', 'VRTX', 'HON', 'PFE', 'DE', 'LOW', 'ADP', 'C', 'FI',
        'AMAT', 'BA', 'PANW', 'MMC', 'CB', 'LMT', 'ETN', 'COP', 'MDT', 'AMT',
        'BMY', 'SO', 'ELV', 'BX', 'CRWD', 'MO', 'WELL', 'SBUX', 'CME', 'DUK',
        'WM', 'KKR', 'ANET', 'ICE', 'PLD', 'CI', 'KLAC', 'GEV', 'ADI', 'LRCX',
        'CVS', 'MCK', 'MDLZ', 'INTC', 'AJG', 'SHW', 'CTAS', 'HCA', 'UPS', 'AON',
        'NKE', 'ORLY', 'APH', 'MU', 'MCO', 'TT', 'EQIX', 'RSG', 'CL', 'TDG',
        'NOC', 'FTNT', 'DASH', 'GD', 'PH', 'MMM', 'APO', 'CDNS', 'ABNB', 'MSI',
        'WMB', 'ITW', 'ECL', 'ZTS', 'CMG', 'SNPS', 'CEG', 'COF', 'WDAY', 'NEM',
        'IBKR', 'WSO', 'RYAN', 'RBA', 'EME', 'CASY', 'FNF', 'GWRE', 'SFM', 'DOCU',
        'BJ', 'CSL', 'WMG', 'BURL', 'DKS', 'DUOL', 'RS', 'USFD', 'EQH', 'CHWY',
        'CNH', 'PSTG', 'UNM', 'RPM', 'GLPI', 'AMH', 'CG', 'GGG', 'WPC', 'DT',
        'UTHR', 'PPC', 'FIX', 'ELS', 'ACM', 'SGI', 'COKE', 'MORN', 'RGLD', 'CW',
        'RGA', 'FLEX', 'GME', 'PFGC', 'OC', 'ILMN', 'RNR', 'WLK', 'ACI', 'BMRN',
        'THC', 'XPO', 'KNSL', 'SCI', 'LAMR', 'CLH', 'WTRG', 'CART', 'OHI', 'ENTG',
        'TXRH', 'HLI', 'NLY', 'AFG', 'PEN', 'EWBC', 'AVTR', 'RBC', 'PCTY', 'H',
        'EHC', 'AR', 'ITT', 'JLL', 'EXEL', 'CAVA', 'WWD', 'MUSA', 'LECO', 'PAG',
        'MANH', 'GMED', 'DOCS', 'ALLY', 'CCK', 'CNM', 'DTM', 'BRBR', 'CELH',
        'NBIX', 'BWXT', 'ATR', 'TOL', 'MTZ', 'X', 'CACI', 'ORI', 'SEIC', 'MEDP',
        'JEF', 'FHN', 'OGE', 'FYBR', 'SF', 'PR', 'CUBE', 'SAIA', 'COHR', 'CRS',
        'AIT', 'SNX', 'ARMK', 'CHE', 'PRI', 'SSB', 'CIEN', 'G', 'BLD', 'OVV',
        'INGR', 'NVT', 'ADC', 'HRB', 'MASI', 'EGP', 'CR', 'MLI', 'PLNT', 'WMS',
        'DBX', 'VNOM', 'APPF', 'RRC', 'TTEK', 'AM', 'NYT', 'CBSH', 'HLNE', 'BERY',
        'FND', 'NNN', 'LAD', 'BRX', 'HALO', 'DCI', 'CHDN', 'GPK', 'WBS', 'EXP',
        'EXLS', 'CORT', 'COOP', 'EAT', 'TGTX', 'SPXC', 'CRVL', 'LRN', 'VIRT',
        'TFX', 'EPRT', 'AWI', 'CWEN', 'TRNO', 'BWA', 'CRK', 'STEP', 'ACIW',
        'CWE.A', 'BMI', 'MMSI', 'QRVO', 'GKOS', 'CTRE', 'BCPC', 'JXN', 'ADMA',
        'GPI', 'IDCC', 'MOG.A', 'LNC', 'RHP', 'KTOS', 'JBTM', 'CSWI', 'SPSC',
        'ZWS', 'RHI', 'KRYS', 'AL', 'CALM', 'SKY', 'FMC', 'ETSY', 'ITRI', 'MSGS',
        'FSS', 'ALKS', 'MTH', 'RDN', 'AMTM', 'ESI', 'IBP', 'URBN', 'WSC', 'PECO',
        'GTES', 'DY', 'ABG', 'INSP', 'MARA', 'BOX', 'GEO', 'NSIT', 'TDS', 'RUSHA',
        'SANM', 'GSHD', 'CE', 'PLMR', 'AROC', 'BGC', 'MP', 'AGO', 'ITGR', 'FELE',
        'FIZZ', 'PBH', 'PIPR', 'ATGE', 'CNR', 'AVAV', 'ESE', 'MRP', 'MGY', 'RDNT',
        'MC', 'SNDR', 'MWA', 'FRPT', 'CVCO', 'SNDK', 'SEE', 'SNEX', 'CNS', 'SMPL',
        'SFBS', 'ACA', 'KAI', 'YOU', 'SLG', 'SKT', 'GOLF', 'ABCB', 'MAC', 'BCC',
        'BANF', 'SHAK', 'LUMN', 'SKYW', 'MDU', 'ICUI', 'DORM', 'VRRM', 'AEIS',
        'GVA', 'AX', 'GFF', 'IPAR', 'AVA', 'OTTR', 'CNK', 'MGEE', 'PLXS', 'MATX',
        'MPW', 'SITM', 'OSIS', 'UNF', 'BRC', 'KFY', 'SWI', 'FUN', 'SXT', 'BXMT',
        'CRC', 'CPK', 'NPO', 'PJT', 'AWR', 'KTB', 'CWT', 'WDFC', 'FTDR', 'HIW',
        'TMDX', 'FBP', 'PRVA', 'UCB', 'ABM', 'FULT'
    ]
    # drop any duplicates, keep original order
    return list(dict.fromkeys(tickers))

@st.cache_resource
def load_models():
    fund_model = joblib.load("model/fund_model.pkl")
    tech_model = joblib.load("model/tech_model.pkl")
    scaler     = joblib.load("model/minmax_scaler.pkl")
    return fund_model, tech_model, scaler

def main():
    st.title("🔍 Stock Input & Rating")

    # ticker selector
    tickers = load_ticker_list()
    ticker  = st.selectbox(
        "Select Stock Ticker",
        options=tickers,
        index=tickers.index("MSFT"),
        help="Start typing to filter…"
    )

    # weights
    fund_w = st.slider("Fundamental Weight (%)", 0, 100, 50)
    tech_w = 100 - fund_w
    st.markdown(f"**Fund:** {fund_w}%   |   **Tech:** {tech_w}%")

    if st.button("🧮 Compute Investment Rating"):
        st.info("Fetching live data…")

        # fundamentals
        tk = yf.Ticker(ticker)
        try:
            info = tk.info
        except Exception as e:
            st.error(f"Could not fetch fundamentals: {e}")
            return

        sector   = info.get("sector",   "N/A")
        industry = info.get("industry", "N/A")
        st.write(f"**Sector:** {sector}   |   **Industry:** {industry}")

        # build df_f
        fund_num_cols = [
            'current_assets','total_assets','common_equity_total',
            'current_debt','long_term_debt','depreciation_amortization',
            'preferred_dividends','current_liabilities','total_liabilities',
            'net_income','pretax_income','total_revenue',
            'total_income_taxes','interest_expense_total',
            'capital_expenditures','net_cash_flow_operating_activities',
            'dividends_per_share_quarter','price_low_quarter'
        ]
        fund_cat_cols = ['gics_sector_x']
        fund_data = {
            'current_assets':                   info.get('currentAssets', np.nan),
            'total_assets':                     info.get('totalAssets', np.nan),
            'common_equity_total':              info.get('totalStockholderEquity', np.nan),
            'current_debt':                     info.get('currentDebt', np.nan),
            'long_term_debt':                   info.get('longTermDebt', np.nan),
            'depreciation_amortization':        info.get('depreciationAndAmortization', np.nan),
            'preferred_dividends':              info.get('preferredStockDividend', np.nan),
            'current_liabilities':              info.get('currentLiabilities', np.nan),
            'total_liabilities':                info.get('totalLiab', np.nan) or info.get('totalLiabilities', np.nan),
            'net_income':                       info.get('netIncomeToCommon', np.nan),
            'pretax_income':                    info.get('pretaxIncome', np.nan),
            'total_revenue':                    info.get('totalRevenue', np.nan),
            'total_income_taxes':               info.get('incomeTaxExpense', np.nan),
            'interest_expense_total':           info.get('interestExpense', np.nan),
            'capital_expenditures':             info.get('capitalExpenditures', np.nan),
            'net_cash_flow_operating_activities': info.get('operatingCashflow', np.nan),
            'dividends_per_share_quarter':      info.get('dividendRate', np.nan),
            'price_low_quarter':                info.get('fiftyTwoWeekLow', np.nan),
            'gics_sector_x':                    sector
        }
        df_f = pd.DataFrame([fund_data], columns=fund_num_cols + fund_cat_cols)

        # technicals (monthly resample)
        hist = yf.download(ticker, period="3y", interval="1d", progress=False)
        if hist.empty:
            st.error("No price history found.")
            return
        monthly_close  = hist["Close"].resample("M").last()
        monthly_vol    = hist["Volume"].resample("M").sum()
        monthly_ret    = monthly_close.pct_change() * 100
        avg_ret_6m     = monthly_ret.rolling(6,  min_periods=1).mean()
        avg_ret_12m    = monthly_ret.rolling(12, min_periods=1).mean()
        vol_6m         = monthly_ret.rolling(6,  min_periods=1).std()
        vol_12m        = monthly_ret.rolling(12, min_periods=1).std()

        tech_data = {
            'monthly_return':      monthly_ret.iloc[-1],
            'month_trading_volume': monthly_vol.iloc[-1],
            'stdev':               monthly_ret.std(),
            'avg_ret_6m':          avg_ret_6m.iloc[-1],
            'avg_ret_12m':         avg_ret_12m.iloc[-1],
            'vol_6m':              vol_6m.iloc[-1],
            'vol_12m':             vol_12m.iloc[-1],
            'gics_sector_x':       sector
        }
        df_t = pd.DataFrame([tech_data])

        # predict & scale
        fund_model, tech_model, scaler = load_models()
        raw_tech = tech_model.predict(df_t)[0]
        raw_fund = fund_model.predict(df_f)[0]
        tech_score, fund_score = scaler.transform([[raw_tech, raw_fund]])[0]
        combined_score = (fund_score * fund_w/100) + (tech_score * tech_w/100)
        combined_score = np.clip(combined_score, 0, 10)

        # display
        c1, c2, c3 = st.columns(3)
        c1.metric("Technical Score",   f"{tech_score:.2f} / 10")
        c2.metric("Fundamental Score", f"{fund_score:.2f} / 10")
        c3.metric("Combined Score",    f"{combined_score:.2f} / 10")

        # traffic-light
        if combined_score < 4:
            st.write("🔴 **Risky**")
        elif combined_score < 6:
            st.write("🟡 **Moderate**")
        else:
            st.write("🟢 **Safer**")

if __name__ == "__main__":
    main()
