Mumbai Billboard Advertising Analytics & Fraud Detection
🚩 Project Overview
This project simulates a real-world scenario where a marketing team needs to optimize their billboard advertising spend in the Mumbai Metropolitan Region (MMR). The goal is to move beyond simple performance metrics and develop a robust system for identifying potentially fraudulent or poor-value billboards, ultimately providing actionable insights through an interactive Power BI dashboard.
The project addresses a critical business problem: How can we ensure our advertising budget is not wasted on overpriced, underperforming, or non-compliant billboards?
🛠️ Tools & Technologies
Data Processing & Analysis: Python (Pandas, NumPy)
Machine Learning: Scikit-learn (Isolation Forest for anomaly detection)
Data Visualization & Dashboarding: Power BI
Version Control: Git & GitHub
📂 Project Structure
This project follows a complete, end-to-end data analysis workflow:
Data Engineering & Feature Creation:
A synthetic dataset of 500 billboards across the MMR was generated, including location, pricing, estimated impressions, and permit status.
Derived metrics like Cost Per Impression (CPI) and a custom "Gap Ratio" (normalized price vs. impressions) were engineered to quantify value.
Rule-Based Risk Scoring (Business Logic):
A tiered risk scoring system was developed to flag billboards based on clear business rules:
High Risk (+3 pts): Expired permit.
Medium Risk (+2 pts): Disproportionately high price (Gap Ratio > 50%) or CPI in the top 5th percentile.
Low Risk (+1 pt): Outdated impression audit (>2 years) or pending/unknown permit status.
Billboards were categorized into 'High', 'Medium', 'Low', and 'No Apparent Risk' tiers.
Machine Learning Anomaly Detection:
An Isolation Forest model was trained on numerical features (price, impressions, CPI, dimensions) to identify "unknown unknowns"—billboards with unusual combinations of attributes that the rule-based system might miss.
This provides a secondary layer of validation, flagging billboards that are statistically different from the norm.
Interactive Dashboarding in Power BI:
A comprehensive, 3-page Power BI report was built to translate the complex analysis into actionable business insights for different stakeholders.
📊 Power BI Dashboard Highlights
The final report consists of three tailored pages:
Page 1: Executive Overview
A high-level summary for leadership to understand overall performance and risk exposure in under 30 seconds.
Key KPIs: Total Monthly Revenue, Booked Billboards Count, Number of High-Risk Billboards, and Total Revenue at Risk.
Visuals: Risk tier breakdown and revenue contribution by borough.
(Insert a screenshot of your Executive Overview dashboard here)
Page 2: Risk Investigation Deep Dive
An interactive tool for analysts to investigate why billboards are flagged.
Features: Interactive slicers for Risk Tier, Borough, and Permit Status.
Visuals: A scatter plot to visually identify overpriced outliers and a detailed table for drilling down into specific billboard data.
(Insert a screenshot of your Risk Investigation dashboard here)
Page 3: Market & Inventory Analysis
A strategic view for the marketing team to plan future campaigns.
Insights: Compares performance of Digital vs. Static billboards.
Visuals: Identifies top spending client industries and provides a matrix comparing average cost and impressions across all boroughs.
🚀 How to Use
Clone the repository.
Ensure you have Python and the required libraries (pandas, scikit-learn) installed.
Run the Python scripts in order:
python data_processing_and_risk_scoring.py to generate the cleaned dataset.
python ml_anomaly_detection.py to add the ML anomaly flags.
Open the billboard_report.pbix file in Power BI Desktop.
Click "Refresh" to load the final billboard_analysis_final.csv data.
