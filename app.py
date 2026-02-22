import streamlit as st


import matplotlib.pyplot as plt

import plotly.graph_objects as go
from tools.data_tool import fetch_stock_data
from tools.analysis_tool import perform_technical_analysis
from tools.risk_tool import evaluate_risk
from tools.llm_tool import generate_ai_report

# -------------------------------
# Global State Variables
# -------------------------------
analyzed_df = None
analysis_summary = None
risk_summary = None
ai_report = None

# =========================
# Page Configuration
# =========================
st.set_page_config(
    page_title="Financial Intelligence AI Agent",
    page_icon="📊",
    layout="wide"
)
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
}
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}
.glass-card {
    background: rgba(255, 255, 255, 0.07);
    backdrop-filter: blur(12px);
    border-radius: 20px;
    padding: 20px;
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
}
.metric-card {
    background: linear-gradient(135deg, #00F5A0, #00D9F5);
    border-radius: 16px;
    padding: 18px;
    color: black;
    text-align: center;
    font-weight: bold;
}
.section-title {
    font-size: 28px;
    font-weight: 700;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)
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
        
        st.markdown("## 📊 Key Metrics")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("💰 Current Price", f"{analysis_summary['Latest Close']:.2f}")
        col2.metric("📈 20D MA", f"{analysis_summary['20 Day MA']:.2f}")
        col3.metric("📉 50D MA", f"{analysis_summary['50 Day MA']:.2f}")
        col4.metric("⚡️ Volatility", f"{analysis_summary['Volatility (%)']:.2f}%")
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


        # Company Summary
        st.markdown("## 🏢 Company Summary")
        for key, value in company_summary.items():
            st.write(f"**{key}:** {value}")
        
        # Technical Analysis Summary
        st.markdown("## 📊 Technical Analysis Summary")
        for key, value in analysis_summary.items():
            st.write(f"**{key}:** {value}")

    st.markdown("## 📊 Advanced Price Action")

    fig = go.Figure(data=[go.Candlestick(
        x=analyzed_df.index,
        open=analyzed_df['Open'],
        high=analyzed_df['High'],
        low=analyzed_df['Low'],
        close=analyzed_df['Close']
    )])

    # Optional: Add moving averages
    fig.add_trace(go.Scatter(
        x=analyzed_df.index,
        y=analyzed_df["MA_20"],
        mode="lines",
        name="20D MA"
    ))

    fig.add_trace(go.Scatter(
        x=analyzed_df.index,
        y=analyzed_df["MA_50"],
        mode="lines",
        name="50D MA"
    ))

    fig.update_layout(
        template="plotly_dark",
        height=550,
        xaxis_rangeslider_visible=False
    )

    st.plotly_chart(fig, use_container_width=True)

# ==============================
# RSI Indicator
# ==============================

st.markdown("### 📉 RSI Indicator")

delta = analyzed_df['Close'].diff()
gain = delta.clip(lower=0)
loss = -delta.clip(upper=0)

avg_gain = gain.rolling(14).mean()
avg_loss = loss.rolling(14).mean()

rs = avg_gain / avg_loss
analyzed_df['RSI'] = 100 - (100 / (1 + rs))

import plotly.graph_objects as go

fig_rsi = go.Figure()

fig_rsi.add_trace(go.Scatter(
    x=analyzed_df.index,
    y=analyzed_df['RSI'],
    mode='lines',
    name='RSI'
))

fig_rsi.update_layout(
    template="plotly_dark",
    height=250,
    yaxis=dict(range=[0, 100])
)

st.plotly_chart(fig_rsi, use_container_width=True)

# ==============================
# MACD Indicator
# ==============================

st.markdown("### 📊 MACD Indicator")

ema12 = analyzed_df['Close'].ewm(span=12, adjust=False).mean()
ema26 = analyzed_df['Close'].ewm(span=26, adjust=False).mean()

analyzed_df['MACD'] = ema12 - ema26
analyzed_df['Signal'] = analyzed_df['MACD'].ewm(span=9, adjust=False).mean()

fig_macd = go.Figure()

fig_macd.add_trace(go.Scatter(
    x=analyzed_df.index,
    y=analyzed_df['MACD'],
    mode='lines',
    name='MACD'
))

fig_macd.add_trace(go.Scatter(
    x=analyzed_df.index,
    y=analyzed_df['Signal'],
    mode='lines',
    name='Signal Line'
))

fig_macd.update_layout(
    template="plotly_dark",
    height=250
)

st.plotly_chart(fig_macd, use_container_width=True)

            
# Risk Summary

st.markdown("## ⚠ Risk Assessment")
for key, value in risk_summary.items():
    st.write(f"**{key}:** {value}")

if "Buy" in ai_report:
    border_color = "rgba(0,255,150,0.6)"
elif "Sell" in ai_report:
    border_color = "rgba(255,80,80,0.6)"
else:
    border_color = "rgba(255,200,0,0.6)"

st.markdown("## 🧠 AI Executive Analysis")

st.markdown(f"""
<div style="
    background: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 15px;
    border: 1px solid {border_color};
    box-shadow: 0 0 25px {border_color}; 
">
{ai_report}
</div>
""", unsafe_allow_html=True)

# AI Sentiment Gauge

st.markdown("### 🧠 AI Sentiment Score")

if analysis_summary["Trend"] == "Bullish":
    sentiment_score = 80
elif analysis_summary["Trend"] == "Bearish":
    sentiment_score = 30
else:
    sentiment_score = 50

fig_gauge = go.Figure(go.Indicator(
    mode="gauge+number",
    value=sentiment_score,
    title={'text': "AI Confidence Level"},
    gauge={
        'axis': {'range': [0, 100]},
        'bar': {'color': "lime"},
        'steps': [
            {'range': [0, 40], 'color': "red"},
            {'range': [40, 70], 'color': "orange"},
            {'range': [70, 100], 'color': "green"},
        ],
    }
))

fig_gauge.update_layout(template="plotly_dark", height=300)

st.plotly_chart(fig_gauge, use_container_width=True)