import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Construct full path to the CSV
csv_path = os.path.join(os.path.dirname(__file__), "fusion_dataset.csv")

# Check if file exists and is non-empty
if not os.path.exists(csv_path) or os.stat(csv_path).st_size == 0:
    print("❌ fusion_dataset.csv is missing or empty. Please generate or log data first.")
    exit()

# Load dataset
df = pd.read_csv(csv_path, names=["timestamp", "gesture", "brain_state", "action_triggered"])

# Encode categorical data
df['gesture_code'] = df['gesture'].astype('category').cat.codes
df['brain_code'] = df['brain_state'].astype('category').cat.codes

X = df[['gesture_code', 'brain_code']]
y = df['action_triggered']

# Avoid error if dataset is still empty after loading
if X.empty or y.empty:
    print("❌ Loaded dataset is empty after preprocessing. Check CSV contents.")
    exit()

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train and save model
model = RandomForestClassifier()
model.fit(X_train, y_train)
joblib.dump(model, os.path.join(os.path.dirname(__file__), "fusion_model.joblib"))

print("✅ Model trained and saved.")
