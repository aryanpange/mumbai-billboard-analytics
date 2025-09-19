import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

# --- Configuration ---
INPUT_CSV_PATH = 'billboard_data_cleaned.csv'
# --- THIS IS THE CORRECTED LINE ---
OUTPUT_CSV_PATH = 'billboard_analysis_final.csv'

# --- 1. Data Loading ---
print("Step 1: Loading the cleaned data...")
try:
    df = pd.read_csv(INPUT_CSV_PATH)
    print(f"Successfully loaded {len(df)} rows from {INPUT_CSV_PATH}.")
except FileNotFoundError:
    print(f"Error: The file {INPUT_CSV_PATH} was not found. Please run the previous script first.")
    exit()

# --- 2. Feature Selection for ML Model ---
print("Step 2: Selecting numerical features for anomaly detection...")

features_for_ml = [
    'Monthly_Impressions_Est',
    'Monthly_Rate_INR',
    'cpi_inr',
    'gap_ratio',
    'Width_ft',
    'Height_ft'
]
df_ml = df[features_for_ml].copy()
df_ml.fillna(df_ml.median(), inplace=True)

print(f"Features selected for ML: {features_for_ml}")

# --- 3. Data Scaling ---
print("Step 3: Scaling the data...")
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df_ml)
print("Data successfully scaled.")

# --- 4. Training the Isolation Forest Model ---
print("Step 4: Training the Isolation Forest model...")
model = IsolationForest(n_estimators=100, contamination='auto', random_state=42)
model.fit(X_scaled)
print("Model training complete.")

# --- 5. Predicting Anomalies and Finalizing Output ---
print("Step 5: Predicting anomalies and saving the final dataset...")
predictions = model.predict(X_scaled)
df['ML_Anomaly_Flag'] = [1 if p == -1 else 0 for p in predictions]

anomaly_count = df['ML_Anomaly_Flag'].sum()
print(f"The model identified {anomaly_count} potential anomalies.")

print("\nSample of ML-flagged anomalies:")
print(df[df['ML_Anomaly_Flag'] == 1][['Billboard_ID', 'Risk_Tier', 'ML_Anomaly_Flag']].head())

# Save the final, fully-analyzed dataset
df.to_csv(OUTPUT_CSV_PATH, index=False)

print(f"\nProcessing complete. The final dataset with ML flags is saved to {OUTPUT_CSV_PATH}.")

