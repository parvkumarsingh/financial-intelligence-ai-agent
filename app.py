import streamlit as st
import matplotlib.pyplot as plt

from tools.data_tool import fetch_stock_data
from tools.analysis_tool import perform_technical_analysis
from tools.risk_tool import evaluate_risk
from tools.llm_tool import generate_ai_report


# =========================
# Page Configuration
# =========================
st.set_page_config(
    page_title="Financial Intelligence AI Agent",
    page_icon="📊",
    layout="wide"
)

# =========================
# Title
# =========================
st.title("Financial Intelligence AI Agent")
st.subheader("AI-Powered Stock Analysis Dashboard (Consulting Style)")


# =========================
# Format Guide
# =========================
st.info(
    "💡 Format Guide:\n"
    "- US Stocks: AAPL, TSLA, MSFT\n"
    "- Indian NSE Stocks: TCS.NS, RELIANCE.NS"
)

# =========================
# User Input
# =========================
ticker = st.text_input("Enter Stock Ticker")


# =========================
# Analyze Button
# =========================
if st.button("🔍 Analyze Stock"):

    if not ticker.strip():
        st.warning("Please enter a stock ticker.")
        st.stop()

    with st.spinner("Fetching financial data and generating AI insights..."):

        ticker = ticker.strip().upper()

        # -----------------------------------
        # Smart Exchange Fallback Logic
        # -----------------------------------
        if "." not in ticker:
            hist_test, _ = fetch_stock_data(ticker)

            if hist_test is None or hist_test.empty:
                ticker = ticker + ".NS"

        # -----------------------------------
        # Step 1: Fetch Data
        # -----------------------------------
        hist_data, company_summary = fetch_stock_data(ticker)

        # -----------------------------------
        # Validation Check
        # -----------------------------------
        if hist_data is None or hist_data.empty:
            st.error(
                "Invalid stock ticker or no data found.\n\n"
                "👉 US Stocks: AAPL, TSLA\n"
                "👉 Indian Stocks: TCS.NS, RELIANCE.NS"
            )
            st.stop()

        st.success(f"Data successfully loaded for {ticker}")

        # -----------------------------------
        # Step 2: Technical Analysis
        # -----------------------------------

        analyzed_df, analysis_summary = perform_technical_analysis(hist_data)

        if analyzed_df is None or analyzed_df.empty:
            st.error("Unable to perform technical analysis due to insufficient data.")
            st.stop()

        # -----------------------------------
        # Step 3: Risk Evaluation
        # -----------------------------------
        risk_summary = evaluate_risk(analysis_summary)

        # -----------------------------------
        # Step 4: AI Executive Report
        # -----------------------------------
        ai_report = generate_ai_report(
            company_summary,
            analysis_summary,
            risk_summary
        )

        # ================================
        # DISPLAY SECTION
        # ================================

        # Company Summary
        st.markdown("## 🏢 Company Summary")
        for key, value in company_summary.items():
            st.write(f"**{key}:** {value}")
        
        # Technical Analysis Summary
        st.markdown("## 📊 Technical Analysis Summary")
        for key, value in analysis_summary.items():
            st.write(f"**{key}:** {value}")

        # Compact Charts ("2 in one row")
        st.markdown("## 📈 Stock Charts")

        col1, col2 = st.columns(2)

        with col1:
            fig1, ax1 = plt.subplots(figsize=(5, 3))
            ax1.plot(analyzed_df.index, analyzed_df["Close"])
            ax1.set_title("Price Trend (1Year)")
            ax1.tick_params(axis='x', rotation=45)
            st.pyplot(fig1)

        with col2:
            fig2, ax2 = plt.subplots(figsize=(5, 3))
            ax2.plot(analyzed_df.index, analyzed_df["Close"], label="Close")
            ax2.plot(analyzed_df.index, analyzed_df["MA_20"], label="20 MA")
            ax2.plot(analyzed_df.index, analyzed_df["MA_50"], label="50 MA")
            ax2.legend()
            ax2.set_title("Moving Average")
            ax2.tick_params(axis='x', rotation=45)
            st.pyplot(fig2)

        # Risk Summary
        st.markdown("## ⚠ Risk Assessment")
        for key, value in risk_summary.items():
            st.write(f"**{key}:** {value}")

        # AI Executive Report
        st.markdown("## 🧠 AI Executive Report")
        st.write(ai_report)