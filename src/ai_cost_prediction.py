import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Sample cost data (replace with real billing data)
data = {
    "month": list(range(1, 13)),
    "cost": [100, 120, 140, 160, 180, 200, 220, 240, 260, 280, 300, 320]
}

df = pd.DataFrame(data)

# Train ML model
X = df[["month"]]
y = df["cost"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

# Predict next 3 months
future_months = np.array([[13], [14], [15]])
predictions = model.predict(future_months)

print("Predicted Costs for Next 3 Months:", predictions)
