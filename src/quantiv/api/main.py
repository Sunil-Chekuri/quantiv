from datetime import date
from fastapi import FastAPI
from quantiv.pipeline.pipeline import run_pipeline
from quantiv.utils.logger import setup_logger

app = FastAPI()

logger = setup_logger()


@app.get("/")
def home():
    logger.info("Health check called")
    return {"message": "Quantiv API running"}


@app.get("/predict")
def predict(
    ticker: str,
    start: date,
    end: date
):

    logger.info(
        f"Prediction request: ticker={ticker}, start={start}, end={end}"
    )

    results = run_pipeline(
        ticker,
        str(start),
        str(end)
    )

    response = {
        model: {
            "RMSE": float(results[model]["RMSE"]),
            "MAPE": float(results[model]["MAPE"]),
            "predicted_next_price": float(
                results[model]["last_prediction"]
            )
        }
        for model in results
    }

    logger.info("Prediction completed")

    return {
        "ticker": ticker,
        "start": start,
        "end": end,
        "results": response
    }