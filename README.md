# Mumbai Billboard Advertising Analytics & Fraud Detection

🚩 **Project Overview**  
This project simulates a real-world scenario where a marketing team needs to optimize their billboard advertising spend in the Mumbai Metropolitan Region (MMR). The goal is to move beyond simple performance metrics and develop a robust system for identifying potentially fraudulent or poor-value billboards, ultimately providing actionable insights through an interactive Power BI dashboard.

The project addresses a critical business problem:  
**How can we ensure our advertising budget is not wasted on overpriced, underperforming, or non-compliant billboards?**

---

## 🛠️ Tools & Technologies
- **Data Processing & Analysis:** Python (Pandas, NumPy)  
- **Machine Learning:** Scikit-learn (Isolation Forest for anomaly detection)  
- **Data Visualization & Dashboarding:** Power BI  
- **Version Control:** Git & GitHub  

---

## 📂 Project Structure
This project follows a complete, end-to-end data analysis workflow:

1. **Data Engineering & Feature Creation**
   - Synthetic dataset of 500 billboards across MMR, including location, pricing, impressions, and permit status.
   - Derived metrics like Cost Per Impression (CPI) and Gap Ratio.

2. **Rule-Based Risk Scoring (Business Logic)**
   - High Risk: Expired permits.  
   - Medium Risk: Overpriced (Gap Ratio > 50%) or very high CPI.  
   - Low Risk: Outdated audits or pending permits.  
   - Risk tiers assigned as: High / Medium / Low / No Apparent Risk.  

3. **Machine Learning Anomaly Detection**
   - Isolation Forest flags statistically unusual billboards.  
   - Secondary validation layer to catch hidden fraud/misinformation.  

4. **Interactive Dashboarding in Power BI**
   - Final business-ready dashboards with actionable insights.  

---

## 📊 Power BI Dashboard Highlights  

### 1️⃣ Executive Overview  
A high-level summary for leadership to understand overall performance and risk exposure in under 30 seconds.  

![Executive Dashboard](https://github.com/aryanpange/mumbai-billboard-analytics/blob/main/dashboard-overview.png?raw=true)  

---

### 2️⃣ Risk Investigation Deep Dive  
Interactive view for analysts to explore why billboards were flagged.  

![Risk Investigation Dashboard](https://github.com/aryanpange/mumbai-billboard-analytics/blob/main/dashboard-investigation.png?raw=true)  

---

### 3️⃣ Market & Inventory Analysis  
Strategic page for the marketing team to compare Digital vs. Static boards and analyze borough-level trends.  

![Market Analysis Dashboard](https://github.com/aryanpange/mumbai-billboard-analytics/blob/main/dashboard-market-analysis.png?raw=true)  

---

## 🚀 How to Use
1. Clone this repository.  
2. Install Python and dependencies (`pandas`, `scikit-learn`).  
3. Run preprocessing + ML scripts:
   ```bash
   python data_processing_and_risk_scoring.py  
   python ml_anomaly_detection.py  
