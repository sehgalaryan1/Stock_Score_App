# pages/page2.py
import streamlit as st
import yfinance as yf
from yfinance.exceptions import YFRateLimitError
import pandas as pd
import time

@st.cache_data
def load_ticker_list():
    tickers = [
        'MSFT', 'NVDA', 'GOOG', 'GOOGL', 'AMZN', 'META', 'AAPL', 'BRK.B', 'AVGO', 'TSLA',
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


def safe_history(ticker, retries=3, delay=3):
    """Try yf.Ticker(ticker).history with retries on rate limits."""
    for i in range(retries):
        try:
            return yf.Ticker(ticker).history(period="2y", interval="1d")
        except YFRateLimitError:
            time.sleep(delay * (i + 1))
        except Exception:
            break
    return pd.DataFrame()

def main():
    st.title("📈 Technical Analysis")

    tickers = load_ticker_list()
    ticker = st.selectbox(
        "Select or Type a Stock Ticker",
        options=tickers,
        index=tickers.index('MSFT'),
        help="Start typing to filter…"
    )

    if st.button("Show Technical Metrics"):
        with st.spinner(f"Loading data for {ticker}…"):
            yf_ticker = ticker.replace('.', '-')  # BRK.B → BRK-B
            df = safe_history(yf_ticker)

            # Fallback mock for MSFT if still empty
            if df.empty and ticker == "MSFT":
                st.warning("⚠️ Using mock data for MSFT due to rate limits.")
                df = pd.DataFrame({
                    "Date": pd.date_range(end=pd.Timestamp.today(), periods=60),
                    "Close": pd.Series([280 + i*0.5 for i in range(60)]),
                    "Volume": pd.Series([1e7] * 60)
                }).set_index("Date")

        if df is None or df.empty:
            st.error("No data found. Check the ticker and try again.")
            return

        df = df.reset_index()
        df["Date"] = pd.to_datetime(df["Date"])
        df.set_index("Date", inplace=True)

        # Annualized 2-year Sharpe Ratio
        try:
            daily_ret = df["Close"].pct_change().dropna()
            monthly_ret = (1 + daily_ret).resample("M").prod() - 1
            sharpe = float(monthly_ret.mean() / monthly_ret.std() * (12 ** 0.5))
            st.subheader(f"Sharpe Ratio: {sharpe:.2f}")
        except Exception as e:
            st.error(f"Error computing Sharpe Ratio: {e}")

        # Monthly Returns
        st.subheader("Monthly Returns")
        try:
            monthly_returns = df["Close"].pct_change().dropna().resample('M').sum()
            if not monthly_returns.empty:
                st.line_chart(monthly_returns)
            else:
                st.write("No monthly returns data available.")
        except Exception as e:
            st.error(f"Error calculating monthly returns: {e}")

        # Monthly Trading Volume
        st.subheader("Monthly Trading Volume")
        try:
            monthly_volume = df['Volume'].resample('M').sum()
            if not monthly_volume.empty:
                st.line_chart(monthly_volume)
            else:
                st.write("No monthly volume data available.")
        except Exception as e:
            st.error(f"Error calculating monthly volume: {e}")

        # 30-Day Rolling Volatility
        st.subheader("30-Day Rolling Volatility")
        try:
            vol = df["Close"].pct_change().dropna().rolling(window=30).std()
            if not vol.empty:
                st.line_chart(vol)
            else:
                st.write("No volatility data available.")
        except Exception as e:
            st.error(f"Error calculating volatility: {e}")

        # 30-Day Rolling Sharpe Ratio
        st.subheader("30-Day Rolling Sharpe Ratio")
        try:
            ret = df["Close"].pct_change().dropna()
            sr = (ret.rolling(window=30).mean() / ret.rolling(window=30).std()) * (12 ** 0.5)
            if not sr.empty:
                st.line_chart(sr)
            else:
                st.write("No Sharpe Ratio data available.")
        except Exception as e:
            st.error(f"Error calculating Sharpe Ratio: {e}")

if __name__ == "__main__":
    main()
