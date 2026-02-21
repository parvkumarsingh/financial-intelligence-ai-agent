import pandas as pd
import numpy as np

def perform_technical_analysis(hist_data):
    """
    Perform financial analysis:
    - Daily Returns
    - Moving Averages
    - Volatility
    - Trend Direction
    """

    # Make a copy of data (safe practice)
    df = hist_data.copy()

    # Calculate Daily Returns
    df["Daily Return"] = df["Close"].pct_change()

    # Calculate Moving Averages
    df["MA_20"] = df["Close"].rolling(window=20).mean()
    df["MA_50"] = df["Close"].rolling(window=50).mean()

    # Calculate Volatility (Risk Indicator)
    volatility = df["Daily Return"].std() * 100  # in %

    # Determine Trend Direction
    latest_price = df["Close"].iloc[-1]
    ma_20_latest = df["MA_20"].iloc[-1]

    if latest_price > ma_20_latest:
        trend = "Uptrend 📈"
    else:
        trend = "Downtrend 📉"

    analysis_summary = {
        "Latest Price": round(latest_price, 2),
        "20-Day Moving Average": round(ma_20_latest, 2),
        "Volatility (%)": round(volatility, 2),
        "Trend Direction": trend
    }

    return df, analysis_summary