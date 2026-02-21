import streamlit as st
import matplotlib.pyplot as plt

from tools.data_tool import fetch_stock_data
from tools.analysis_tool import perform_technical_analysis
from tools.risk_tool import evaluate_risk
from tools.llm_tool import generate_ai_report

# Page Configuration
st.set_page_config(
    page_title="Corporate Financial AI Agent",
    page_icon="📊",
    layout="wide"
)

# Title
st.title("Financial Intelligence AI Agent")
st.subheader("AI-Powered Stock Analysis Dashboard (Consulting Style)")

# User Input
ticker = st.text_input(
    "Enter Stock Ticker (Example: AAPL, TSLA, TCS.NS, RELIANCE.NS):",
    "AAPL"
)

# Analyze Button
if st.button("🔍 Analyze Stock"):

    with st.spinner("Fetching financial data and generating AI insights..."):

        # Step 1: Fetch Data
        hist_data, company_summary = fetch_stock_data(ticker)

        # Step 2: Technical Analysis
        analyzed_df, analysis_summary = perform_technical_analysis(hist_data)

        # Step 3: Risk Evaluation
        risk_summary = evaluate_risk(analysis_summary)

        # Step 4: AI Report (Free Logic)
        ai_report = generate_ai_report(
            company_summary,
            analysis_summary,
            risk_summary
        )

    # Layout in columns
    col1, col2 = st.columns(2)

    # Company Summary
    with col1:
        st.markdown("## 🏢 Company Summary")
        for key, value in company_summary.items():
            st.write(f"**{key}:** {value}")

    # Technical Analysis
    with col2:
        st.markdown("## 📈 Technical Analysis")
        for key, value in analysis_summary.items():
            st.write(f"**{key}:** {value}")

    # Risk Section
    st.markdown("## ⚠ Risk & Strategic Insight")
    for key, value in risk_summary.items():
        st.write(f"**{key}:** {value}")

    # Price Chart
    st.markdown("## 📊 Stock Price Trend (1 Year)")
    fig, ax = plt.subplots()
    ax.plot(analyzed_df.index, analyzed_df["Close"])
    ax.set_xlabel("Date")
    ax.set_ylabel("Stock Price")
    ax.set_title(f"{ticker} Price Trend")
    st.pyplot(fig)

    # Moving Average Chart
    st.markdown("## 📉 Moving Average Analysis")
    fig2, ax2 = plt.subplots()
    ax2.plot(analyzed_df.index, analyzed_df["Close"], label="Close Price")
    ax2.plot(analyzed_df.index, analyzed_df["MA_20"], label="20-Day MA")
    ax2.plot(analyzed_df.index, analyzed_df["MA_50"], label="50-Day MA")
    ax2.legend()
    ax2.set_title("Moving Average Comparison")
    st.pyplot(fig2)

    # AI Executive Report
    st.markdown("## 🧠 AI Executive Report (Corporate Level)")
    st.write(ai_report)