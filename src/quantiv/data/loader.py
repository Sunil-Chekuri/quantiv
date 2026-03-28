import yfinance as yf
import pandas as pd


def load_stock_data(ticker: str, start: str, end: str) -> pd.DataFrame:
    return yf.download(ticker, start=start, end=end)