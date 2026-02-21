def generate_ai_report(company_summary, analysis_summary, risk_summary):
    """
    Generate executive-level financial report (FREE AI Logic - No API)
    """

    company_name = company_summary.get("Company Name", "The company")
    sector = company_summary.get("Sector", "Unknown Sector")
    pe_ratio = company_summary.get("P/E Ratio", "N/A")

    trend = analysis_summary.get("Trend Direction", "Unknown")
    volatility = analysis_summary.get("Volatility (%)", 0)
    latest_price = analysis_summary.get("Latest Price", "N/A")

    risk_level = risk_summary.get("Risk Level", "Unknown")
    outlook = risk_summary.get("Strategic Outlook", "")

    # Executive Summary
    executive_summary = f"""
    Executive Summary:
    {company_name} operates in the {sector} sector and is currently trading at {latest_price}.
    The stock shows a {trend.lower()} with a volatility of approximately {volatility}%, 
    indicating a {risk_level.lower()} profile.
    """

    # Performance Analysis
    performance_analysis = f"""
    Performance Analysis:
    The technical indicators suggest that the stock is experiencing a {trend.lower()} trend.
    Moving average analysis indicates momentum alignment with current price action,
    which is a key signal used in institutional financial analysis.
    """

    # Risk Commentary
    risk_commentary = f"""
    Risk Commentary:
    Based on the observed volatility levels ({volatility}%) and trend direction,
    the stock is categorized under {risk_level}. {outlook}
    """

    # Strategic Recommendation (Consulting-style)
    if "Low Risk" in risk_level and "Uptrend" in trend:
        recommendation = """
        Strategic Recommendation:
        The stock demonstrates stable growth characteristics with controlled volatility.
        Suitable for long-term investment consideration from a risk-adjusted perspective.
        """
    elif "High Risk" in risk_level:
        recommendation = """
        Strategic Recommendation:
        Elevated volatility and risk signals suggest cautious monitoring.
        Recommended for high-risk tolerance portfolios only.
        """
    else:
        recommendation = """
        Strategic Recommendation:
        Mixed technical and risk signals observed.
        A balanced and cautious investment approach is recommended.
        """

    final_report = (
        executive_summary
        + performance_analysis
        + risk_commentary
        + recommendation
    )

    return final_report