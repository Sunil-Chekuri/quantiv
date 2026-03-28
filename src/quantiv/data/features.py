import pandas as pd


def create_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["returns"] = df["Close"].pct_change()
    df["ma_5"] = df["Close"].rolling(window=5).mean()
    df["ma_10"] = df["Close"].rolling(window=10).mean()
    df["volume_change"] = df["Volume"].pct_change()

    df["target"] = df["Close"].shift(-1)

    return df.dropna()