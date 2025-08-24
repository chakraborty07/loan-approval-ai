import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import os

# ========== Step 1: Load dataset ==========
# If you already have a dataset, replace this with your CSV path
# Example: data = pd.read_csv("data/loan_data.csv")

# For demo purposes, let's create a sample dataset
data = pd.DataFrame({
    "Gender": ["Male", "Female", "Male", "Male", "Female", "Female", "Male", "Female"],
    "Married": ["Yes", "No", "Yes", "No", "Yes", "No", "Yes", "Yes"],
    "Education": ["Graduate", "Not Graduate", "Graduate", "Graduate", "Not Graduate", "Graduate", "Graduate", "Not Graduate"],
    "Self_Employed": ["No", "Yes", "No", "No", "Yes", "No", "No", "Yes"],
    "ApplicantIncome": [5000, 3000, 4000, 6000, 2500, 3500, 8000, 2000],
    "LoanAmount": [200, 100, 150, 250, 80, 120, 300, 90],
    "Credit_History": [1, 0, 1, 1, 0, 1, 1, 0],
    "Loan_Status": ["Y", "N", "Y", "Y", "N", "Y", "Y", "N"]
})

print("Sample Data:")
print(data.head())

# ========== Step 2: Encode categorical features ==========
le = LabelEncoder()
for col in ["Gender", "Married", "Education", "Self_Employed", "Loan_Status"]:
    data[col] = le.fit_transform(data[col])

# ========== Step 3: Split data ==========
X = data.drop("Loan_Status", axis=1)
y = data["Loan_Status"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ========== Step 4: Scale numeric values ==========
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# ========== Step 5: Train model ==========
model = LogisticRegression()
model.fit(X_train, y_train)

# ========== Step 6: Evaluate ==========
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"✅ Model trained with accuracy: {accuracy:.2f}")

# ========== Step 7: Save model ==========
os.makedirs("artifacts", exist_ok=True)
joblib.dump(model, "artifacts/loan_model.pkl")
joblib.dump(scaler, "artifacts/scaler.pkl")

print("🎉 Model and scaler saved in artifacts/ folder")
