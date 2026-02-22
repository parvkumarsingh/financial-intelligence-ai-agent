def evaluate_risk(analysis_summary):
    """
    Evaluate stock risk level based on volatility and trend
    Corporate-style risk classification logic
    """

    volatility = analysis_summary["Volatility (%)"]
    trend = analysis_summary["Trend"]

    # Risk Classification based on volatility
    if volatility < 1:
        risk_level = "Low Risk 🟢"
    elif 1 <= volatility < 2.5:
        risk_level = "Medium Risk 🟡"
    else:
        risk_level = "High Risk 🔴"

    # Strategic Insight (Consultant-style logic)
    if trend == "Uptrend 📈" and risk_level == "Low Risk 🟢":
        outlook = "Stable growth potential with low volatility."
    elif trend == "Uptrend 📈" and risk_level != "Low Risk 🟢":
        outlook = "Growth trend present but accompanied by moderate/high volatility."
    elif trend == "Downtrend 📉" and risk_level == "High Risk 🔴":
        outlook = "Downward trend with high volatility indicates elevated investment risk."
    else:
        outlook = "Mixed signals observed; cautious monitoring recommended."

    risk_summary = {
        "Risk Level": risk_level,
        "Strategic Outlook": outlook
    }

    return risk_summary