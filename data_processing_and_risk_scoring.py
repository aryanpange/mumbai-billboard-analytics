import pandas as pd
import numpy as np
from datetime import datetime

# --- Configuration ---
INPUT_CSV_PATH = 'billboard_data_enriched.csv'
OUTPUT_CSV_PATH = 'billboard_data_cleaned.csv'
CURRENT_DATE = pd.to_datetime('2025-09-02')
AUDIT_AGE_THRESHOLD_YEARS = 2

# --- 1. Data Loading ---
print("Step 1: Loading data...")
try:
    df = pd.read_csv(INPUT_CSV_PATH, engine='python', on_bad_lines='skip')
    print(f"Successfully loaded {len(df)} rows.")
except FileNotFoundError:
    print(f"Error: {INPUT_CSV_PATH} not found.")
    exit()

# --- 2. Data Cleaning ---
print("Step 2: Cleaning and preprocessing...")
df['Last_Audit_Date'] = pd.to_datetime(df['Last_Audit_Date'], errors='coerce')
df['Permit_Status'] = df['Permit_Status'].fillna('Unknown')
df['Client_ID'] = df['Client_ID'].fillna('')
df['Client_Name'] = df['Client_Name'].fillna('')

# --- 3. Feature Engineering ---
print("Step 3: Engineering features...")
df['cpi_inr'] = df.apply(lambda row: row['Monthly_Rate_INR'] / row['Monthly_Impressions_Est'] if row['Monthly_Impressions_Est'] > 0 else 0, axis=1)
cpi_95th_percentile = df['cpi_inr'].quantile(0.95)
df['rate_normalized'] = (df['Monthly_Rate_INR'] - df['Monthly_Rate_INR'].min()) / (df['Monthly_Rate_INR'].max() - df['Monthly_Rate_INR'].min())
df['impressions_normalized'] = (df['Monthly_Impressions_Est'] - df['Monthly_Impressions_Est'].min()) / (df['Monthly_Impressions_Est'].max() - df['Monthly_Impressions_Est'].min())
df['gap_ratio'] = df['rate_normalized'] - df['impressions_normalized']

# --- 4. Risk Scoring Logic ---
print("Step 4: Applying risk scoring logic...")
def calculate_risk_score(row):
    score = 0
    if row['Permit_Status'] == 'Expired': score += 3
    if row['gap_ratio'] > 0.5: score += 2
    if row['cpi_inr'] > cpi_95th_percentile: score += 2
    if pd.notna(row['Last_Audit_Date']) and (CURRENT_DATE - row['Last_Audit_Date']).days > 365 * AUDIT_AGE_THRESHOLD_YEARS: score += 1
    if row['Permit_Status'] in ['Pending', 'Unknown']: score += 1
    return score

def get_risk_tier(score):
    if score >= 4: return 'High Risk'
    elif score == 3: return 'Medium Risk'
    elif score in [1, 2]: return 'Low Risk'
    else: return 'No Apparent Risk'

df['Risk_Score'] = df.apply(calculate_risk_score, axis=1)
df['Risk_Tier'] = df['Risk_Score'].apply(get_risk_tier)

# --- 5. Finalizing and Saving Output ---
print(f"Step 5: Saving the cleaned data...")
final_columns = [
    'Billboard_ID', 'Location_Name', 'Borough', 'Location_Type', 'Billboard_Type',
    'Width_ft', 'Height_ft', 'Monthly_Impressions_Est', 'Monthly_Rate_INR',
    'cpi_inr', 'gap_ratio', 'Permit_Status', 'Last_Audit_Date',
    'Risk_Score', 'Risk_Tier', 'Client_ID', 'Client_Name', 'Client_Industry'
]
df_final = df[final_columns]
df_final.to_csv(OUTPUT_CSV_PATH, index=False)

print(f"\nSUCCESS: Created {OUTPUT_CSV_PATH}")
print("Columns saved:", list(df_final.columns))