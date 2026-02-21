from tools.data_tool import fetch_stock_data
from tools.analysis_tool import perform_technical_analysis
from tools.risk_tool import evaluate_risk
from tools.llm_tool import generate_ai_report

def main():
    ticker = input("Enter Stock Ticker (Example: AAPL, TSLA, TCS.NS): ")

    print("\nFetching financial data...\n")
    hist_data, company_summary = fetch_stock_data(ticker)

    print("===== COMPANY SUMMARY =====")
    for key, value in company_summary.items():
        print(f"{key}: {value}")

    print("\nPerforming technical analysis...\n")
    analyzed_df, analysis_summary = perform_technical_analysis(hist_data)

    print("===== TECHNICAL ANALYSIS =====")
    for key, value in analysis_summary.items():
        print(f"{key}: {value}")

    print("\nEvaluating risk and strategic outlook...\n")
    risk_summary = evaluate_risk(analysis_summary)

    print("===== RISK & STRATEGIC INSIGHT =====")
    for key, value in risk_summary.items():
        print(f"{key}: {value}")

    print("\nGenerating AI Executive Report (Corporate Level)...\n")
    ai_report = generate_ai_report(
        company_summary,
        analysis_summary,
        risk_summary
    )

    print("===== AI EXECUTIVE REPORT =====")
    print(ai_report)

if __name__ == "__main__":
    main()