# feature_engineering.py
import pandas as pd

# exactly the lists you used when training
num_cols_tech = [
    "monthly_return","month_trading_volume","stdev",
    "avg_ret_6m","avg_ret_12m","vol_6m","vol_12m"
]
cat_cols = ["gics_sector_x"]

fund_num_cols = [
    "current_assets","total_assets","common_equity_total","current_debt",
    "long_term_debt","depreciation_amortization","preferred_dividends",
    "current_liabilities","total_liabilities","net_income","pretax_income",
    "total_revenue","total_income_taxes","interest_expense_total",
    "capital_expenditures","net_cash_flow_operating_activities",
    "dividends_per_share_quarter","price_low_quarter"
]
fund_cat_cols = ["gics_sector_x"]

def make_tech_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["monthly_return"]       = df["Close"].pct_change()
    df["month_trading_volume"] = df["Volume"].resample("M").sum()
    df["stdev"]                = df["monthly_return"].rolling(12).std()
    df["avg_ret_6m"]           = df["monthly_return"].rolling(6).mean()
    df["avg_ret_12m"]          = df["monthly_return"].rolling(12).mean()
    df["vol_6m"]               = df["monthly_return"].rolling(6).std()
    df["vol_12m"]              = df["monthly_return"].rolling(12).std()
    return df[num_cols_tech + cat_cols].dropna()

def make_fund_features(df: pd.DataFrame) -> pd.DataFrame:
    # df already has all the Compustat columns + 'gics_sector_x'
    return df[fund_num_cols + fund_cat_cols].dropna()
