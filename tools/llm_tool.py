def generate_ai_report(company_summary, analysis_summary, risk_summary):
    """
    Generate executive-level financial report (FREE AI Logic - No API)
    """

    # -------------------------------
    # Extract Key Data
    # -------------------------------
    company_name = company_summary.get("Company Name", "The company")
    sector = company_summary.get("Sector", "Unknown Sector")

    trend = analysis_summary.get("Trend", "Unknown")
    volatility = analysis_summary.get("Volatility (%)", 0)
    latest_price = analysis_summary.get("Latest Close", "N/A")

    risk_level = risk_summary.get("Risk Level", "Unknown")

    # -------------------------------
    # AI Decision Engine
    # -------------------------------
    if trend.lower() == "bullish" and "low" in risk_level.lower():
        recommendation = "Buy"
        confidence = 80
    elif trend.lower() == "bearish":
        recommendation = "Sell"
        confidence = 35
    else:
        recommendation = "Hold"
        confidence = 55

    # -------------------------------
    # AI Executive Report
    # -------------------------------
    ai_report = f"""
## 📊 Investment Verdict

**{company_name}** is currently in a **{trend}** phase within the **{sector}** sector.

- Latest Price: {latest_price}
- Volatility: {volatility}%
- Risk Classification: {risk_level}

---

### ✅ Strengths
- Technical trend alignment supports current momentum.
- Volatility profile indicates structured price behavior.
- Risk framework suggests controlled exposure.

### ⚠️ Risks
- Market sentiment shifts could impact direction.
- Sector rotation risk remains relevant.
- Broader macroeconomic conditions may influence volatility.

---

## 🎯 Final Recommendation
### **{recommendation}**

### 🔎 Confidence Score
**{confidence}%**
"""

    return ai_report