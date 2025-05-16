import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import joblib

df = pd.read_csv('system/threat_humter_data.csv')
df = df[['length', 'proto']]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

model = IsolationForest(contamination=0.05, random_state=42)
model.fit(X_scaled)

joblib.dump(model, 'model/model.joblib')
joblib.dump(scaler, 'model/scaler.joblib')
print("Model and scaler saved.")