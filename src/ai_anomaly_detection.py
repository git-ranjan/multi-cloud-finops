import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest

# Load cloud billing data
df = pd.read_csv("data/cloud_billing.csv")

# Selecting relevant features
features = df[['aws_cost', 'gcp_cost', 'azure_cost']]

# Train an Isolation Forest model
model = IsolationForest(contamination=0.05, random_state=42)
df['anomaly'] = model.fit_predict(features)

# Identify anomalies
anomalies = df[df['anomaly'] == -1]

# Save anomalies report
anomalies.to_csv("output/cost_anomalies.csv", index=False)
print("✅ Anomaly Detection Completed. Results saved to output/cost_anomalies.csv.")
