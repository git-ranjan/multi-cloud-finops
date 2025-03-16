import requests
import json
import numpy as np
import pandas as pd
from fastapi import FastAPI
from sklearn.ensemble import IsolationForest

app = FastAPI()

# Simulated function to fetch cloud cost data (replace with actual API calls)
def fetch_cost_data():
    return pd.DataFrame({
        'timestamp': pd.date_range(start='2024-01-01', periods=30, freq='D'),
        'aws_cost': np.random.randint(100, 500, size=30),
        'gcp_cost': np.random.randint(50, 400, size=30),
        'azure_cost': np.random.randint(80, 450, size=30)
    })

# Train Isolation Forest model for anomaly detection
def train_model(data):
    model = IsolationForest(contamination=0.1, random_state=42)
    data['total_cost'] = data[['aws_cost', 'gcp_cost', 'azure_cost']].sum(axis=1)
    model.fit(data[['total_cost']])
    data['anomaly'] = model.predict(data[['total_cost']])
    return data

@app.get("/detect-anomalies")
def detect_anomalies():
    cost_data = fetch_cost_data()
    analyzed_data = train_model(cost_data)
    anomalies = analyzed_data[analyzed_data['anomaly'] == -1]
    return anomalies.to_dict(orient='records')

@app.get("/optimize-cost")
def optimize_cost():
    # Placeholder for cloud cost optimization logic
    return {"message": "Cost optimization triggered!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
