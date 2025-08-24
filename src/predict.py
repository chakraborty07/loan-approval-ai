import joblib
import numpy as np

# Load trained model and scaler
model = joblib.load("artifacts/loan_model.pkl")
scaler = joblib.load("artifacts/scaler.pkl")

# Function to predict loan approval
def predict_loan(gender, married, education, self_employed, applicant_income, loan_amount, credit_history):
    # Encode categorical variables (same encoding as train.py)
    gender = 1 if gender.lower() == "male" else 0
    married = 1 if married.lower() == "yes" else 0
    education = 1 if education.lower() == "graduate" else 0
    self_employed = 1 if self_employed.lower() == "yes" else 0
    credit_history = int(credit_history)

    # Create feature array
    features = np.array([[gender, married, education, self_employed, applicant_income, loan_amount, credit_history]])

    # Scale numeric values
    features = scaler.transform(features)

    # Make prediction
    prediction = model.predict(features)[0]

    return "✅ Loan Approved" if prediction == 1 else "❌ Loan Not Approved"


if __name__ == "__main__":
    # Example test case
    result = predict_loan(
        gender="Male",
        married="Yes",
        education="Graduate",
        self_employed="No",
        applicant_income=4000,
        loan_amount=150,
        credit_history=1
    )
    print(result)
