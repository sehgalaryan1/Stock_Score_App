import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# Cache ticker list for dropdown
@st.cache_data
# ticker_list.py

def load_ticker_list():
    tickers = [
        'AAPL', 'MSFT', 'NVDA', 'GOOG', 'GOOGL', 'AMZN', 'META', 'BRK.B', 'AVGO', 'TSLA',
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
    return tickers

@st.cache_data
def fetch_ticker_info(ticker):
    tk = yf.Ticker(ticker)
    info = tk.info or {}
    qf   = tk.quarterly_financials   # DataFrame: cols are quarters
    return info, qf

def compute_metrics(info, qf):
    """Return a dict of your ratios plus YoY changes where available."""
    # core ratios from info
    roe   = info.get('returnOnEquity', np.nan)*100
    roa   = info.get('returnOnAssets',  np.nan)*100
    de    = info.get('debtToEquity',    np.nan)
    pm    = info.get('profitMargins',   np.nan)*100
    pe    = info.get('trailingPE',      np.nan)
    eps_q = info.get('earningsQuarterlyGrowth', np.nan)*100
    
    return {
      'Return on Equity (%)': roe,
      'Return on Assets (%)': roa,
      'Debt-to-Equity':       de,
      'Profit Margin (%)':    pm,
      'P/E Ratio':            pe,
      'EPS Growth QoQ (%)':   eps_q,
      # could add more YoY computations here if we get the raw values in qf…
    }

def industry_averages(universe, industry, metric_keys):
    """Loop the ticker universe, grab each ticker that matches `industry`, compute average per metric."""
    rows = []
    for tk in universe:
        info, qf = fetch_ticker_info(tk)
        if info.get('industry') == industry:
            rows.append(compute_metrics(info, qf))
    df_ind = pd.DataFrame(rows)
    return df_ind.mean()

# —————— Streamlit page ——————

def main():
    st.title("🧾 Fundamental Analysis")

    # 1) ticker
    tickers = load_ticker_list()
    ticker  = st.selectbox(
      "Select or Type a Stock Ticker",
      options=tickers,
      index=tickers.index("AAPL"),
      help="Start typing…"
    )

    if st.button("Fetch Fundamentals"):
        st.info(f"Loading {ticker}…")
        info, qf = fetch_ticker_info(ticker)
        sector   = info.get("sector","N/A")
        industry = info.get("industry","N/A")
        st.write(f"**Sector:** {sector}   |   **Industry:** {industry}")

        # 2) compute your company metrics
        comp = compute_metrics(info, qf)

        # 3) compute industry averages
        ind_avg = industry_averages(tickers, industry, list(comp.keys()))

        # 4) put it all in a DataFrame, reindex from 1…
        df = (
          pd.DataFrame.from_dict({
            'Company': comp,
            'Industry Avg': ind_avg
          })
          .reset_index()
          .rename(columns={'index':'Metric'})
        )
        df.index = df.index + 1

        # 5) add YoY/QoQ change column (for EPS Growth we have it, others can be blank or computed)
        df['Change vs Prev Qtr'] = ''
        df.loc[df['Metric']=="EPS Growth QoQ (%)", 'Change vs Prev Qtr'] = df.loc[df['Metric']=="EPS Growth QoQ (%)","Company"].astype(float)

        # 6) display with conditional formatting
        def color_row(val, indval):
            return ['background-color: lightgreen' if v>iv else 'background-color: salmon'
                    for v, iv in zip(val, indval)]

        styled = (
          df.style
            .format({ 'Company': "{:,.2f}", 'Industry Avg': "{:,.2f}" })
            .apply(lambda row: color_row([row['Company']], [row['Industry Avg']]), axis=1, subset=['Company'])
        )
        st.table(styled)

        # 7) bar chart with industry avg overlay
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=df['Metric'], y=df['Company'],
            name=ticker
        ))
        fig.add_trace(go.Bar(
            x=df['Metric'], y=df['Industry Avg'],
            name=f"{industry} Avg"
        ))
        fig.update_layout(
            barmode='group',
            title=f"{ticker} vs {industry} Averages",
            xaxis_tickangle=-45,
            margin=dict(t=50, b=150)
        )
        st.plotly_chart(fig, use_container_width=True)

if __name__=="__main__":
    main()
