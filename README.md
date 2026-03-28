# quantiv


A modular stock prediction pipeline built using **FastAPI**, **scikit-learn**, and modern Python dependency management with **uv**.

This project demonstrates how to move from experimental scripts to a structured, production-style system with clear separation of concerns: data ingestion, feature engineering, model training, and API serving.

---

## Features

- REST API for stock price prediction
- Multiple regression models:
  - Linear Regression
  - Ridge Regression
  - Lasso Regression
  - Random Forest
- Modular architecture (data → features → models → pipeline → API)
- Logging support for observability
- Dependency management using `pyproject.toml` and `uv`
- Time-series aware train/test split
- Easily extendable for backtesting and additional models

---


---

## Tech Stack

- Python
- FastAPI
- scikit-learn
- pandas
- numpy
- yfinance
- uv (dependency management)
- logging

---

## How It Works

The pipeline follows a structured workflow:

1. Fetch historical stock data
2. Generate features
3. Train regression models
4. Evaluate model performance
5. Serve predictions via REST API

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Sunil-Chekuri/quantiv.git
cd quantiv

Install dependencies using uv:
```bash
uv sync


## Running the API

Start the FastAPI server:

uv run uvicorn quantiv.api.main:app --reload

The API will be available at:

http://127.0.0.1:8000

Interactive API documentation:

http://127.0.0.1:8000/docs
