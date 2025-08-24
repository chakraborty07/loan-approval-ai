from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import joblib
import numpy as np
import os

app = FastAPI()

# Load model and scaler
model_path = os.path.join("artifacts", "loan_model.pkl")
scaler_path = os.path.join("artifacts", "scaler.pkl")

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

@app.get("/", response_class=HTMLResponse)
def form():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Loan Approval Prediction</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(to right, #667eea, #764ba2);
                color: #fff;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                background: rgba(0,0,0,0.6);
                padding: 30px;
                border-radius: 15px;
                box-shadow: 0px 4px 15px rgba(0,0,0,0.3);
                width: 400px;
                text-align: center;
            }
            input, button {
                width: 90%;
                padding: 10px;
                margin: 10px 0;
                border: none;
                border-radius: 8px;
            }
            input {
                background: #f1f1f1;
            }
            button {
                background: #667eea;
                color: white;
                font-weight: bold;
                cursor: pointer;
                transition: 0.3s;
            }
            button:hover {
                background: #5a67d8;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>🏦 Loan Approval Prediction</h2>
            <form action="/predict" method="post">
                <input type="number" step="any" name="ApplicantIncome" placeholder="Applicant Income" required><br>
                <input type="number" step="any" name="CoapplicantIncome" placeholder="Coapplicant Income" required><br>
                <input type="number" step="any" name="LoanAmount" placeholder="Loan Amount" required><br>
                <input type="number" step="any" name="Loan_Amount_Term" placeholder="Loan Term (months)" required><br>
                <input type="number" name="Credit_History" placeholder="Credit History (0 or 1)" required><br>
                <button type="submit">🔍 Predict</button>
            </form>
        </div>
    </body>
    </html>
    """

@app.post("/predict")
def predict(ApplicantIncome: float = Form(...), 
            CoapplicantIncome: float = Form(...),
            LoanAmount: float = Form(...),
            Loan_Amount_Term: float = Form(...),
            Credit_History: int = Form(...)):

    features = np.array([[ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History]])
    features = scaler.transform(features)
    prediction = model.predict(features)

    result = "✅ Loan Approved" if prediction[0] == 1 else "❌ Loan Rejected"

    return f"""
    <html>
        <head><title>Result</title></head>
        <body style="font-family: Arial; text-align:center; background:#f0f0f0; padding:50px;">
            <h1>{result}</h1>
            <a href="/">🔙 Back</a>
        </body>
    </html>
    """
