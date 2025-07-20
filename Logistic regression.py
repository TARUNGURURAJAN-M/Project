import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, accuracy_score
import joblib

# Step 1: Load cleaned data
df = pd.read_csv("cleaned_data.csv")

# Step 2: Select features and target
features = ['budget', 'revenue', 'runtime', 'vote_average', 'vote_count', 'popularity']
X = df[features]
y = df['success']

# Step 3: Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 4: Split data
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Step 5: Train Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 6: Make predictions
y_pred = model.predict(X_test)

# Step 7: Evaluate model
print("✅ Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Step 8: Save the model and scaler
joblib.dump(model, "success_prediction_model.pkl")
joblib.dump(scaler, "scaler.pkl")

# Step 9: Predict on full dataset and save to CSV
df['predicted_success'] = model.predict(X_scaled)
df.to_csv("data_with_predictions.csv", index=False)
print("📁 data_with_predictions.csv and model files saved.")
