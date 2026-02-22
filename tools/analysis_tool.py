import pandas as pd
import numpy as np

def perform_technical_analysis(hist_data):

    # Safety Check
    if hist_data is None or hist_data.empty or len(hist_data) < 50:
        return None, None
    
    df = hist_data.copy()

    # Proper validation
    if hist_data is None or hist_data.empty:
        return None, None

    # Make a copy (safe practice)
    df = hist_data.copy()

    # Calculate Daily Returns
    df["Daily Return"] = df["Close"].pct_change()

    # Moving Averages
    df["MA_20"] = df["Close"].rolling(window=20).mean()
    df["MA_50"] = df["Close"].rolling(window=50).mean()

    # Volatility
    volatility = df["Daily Return"].std() * 100

    # Trend Direction
    latest_price = df["Close"].iloc[-1]
    ma_20_latest = df["MA_20"].iloc[-1]

    trend = "Bullish" if latest_price > ma_20_latest else "Bearish"

    summary = {
        "Latest Close": latest_price,
        "20 Day MA": ma_20_latest,
        "50 Day MA": df["MA_50"].iloc[-1],
        "Volatility (%)": round(volatility, 2),
        "Trend": trend
    }

    return df, summary