from sklearn.model_selection import train_test_split

from quantiv.data.loader import load_stock_data
from quantiv.data.features import create_features
from quantiv.models.regression import train_models


def run_pipeline(ticker: str, start: str, end: str):
    df = load_stock_data(ticker, start, end)
    df = create_features(df)

    features = ["returns", "ma_5", "ma_10", "volume_change"]
    X = df[features]
    y = df["target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, shuffle=False
    )

    results = train_models(X_train, y_train, X_test, y_test)

    return results