import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker):
    """
    Fetch historical stock data and basic company information
    """
    # Create stock object
    stock = yf.Ticker(ticker)

    # Get 1 year historical data
    hist_data = stock.history(period="1y")

    # Get company info
    info = stock.info

    # Extract important financial details
    financial_summary = {
        "Company Name": info.get("longName", "N/A"),
        "Sector": info.get("sector", "N/A"),
        "Market Cap": info.get("marketCap", "N/A"),
        "P/E Ratio": info.get("trailingPE", "N/A"),
        "Current Price": info.get("currentPrice", "N/A")
    }

    return hist_data, financial_summary