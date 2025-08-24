Got it 👍
The issue is happening because in your `README.md` the **project structure code block** isn’t closed properly with triple backticks (\`\`\`) — so GitHub is treating everything after it as plain text.

Let me give you the **perfectly structured version** 👇
Copy this **exactly as it is** and paste into your `README.md` (don’t change spacing or backticks):

````markdown
# 💳 Loan Approval Prediction AI  

This project is a **Loan Approval Prediction System** built using **Machine Learning** and deployed with **FastAPI**.  
It predicts whether a loan application should be approved or not based on applicant details.  

---

## 🚀 Features  
- 📊 Machine Learning model trained on loan dataset  
- ⚡ FastAPI backend for serving predictions  
- 🔗 REST API endpoints for integration  
- 📂 Organized project structure for easy scalability  

---

## 📂 Project Structure  

```bash
loan_approval_ai/
│── app/
│   └── main.py          # FastAPI web app
│── artifacts/
│   ├── loan_model.pkl   # Trained ML model
│   └── scaler.pkl       # Standard scaler for preprocessing
│── data/
│   └── loan.csv         # Dataset
│── train_model.py       # Script to train the ML model
│── requirements.txt     # Project dependencies
└── README.md            # Project documentation
````

---

## ⚙️ Installation & Setup

Clone the repository:

```bash
git clone https://github.com/your-username/loan_approval_ai.git
cd loan_approval_ai
```

Create & activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### Train the model

```bash
python train_model.py
```

This will generate `loan_model.pkl` and `scaler.pkl` in the `artifacts/` folder.

### Run the web app

```bash
uvicorn app.main:app --reload
```

Visit 👉 [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

---

## 🌐 User Interface Preview

The app provides a simple web form 📝 where you can input:

* 👨 Applicant Income
* 👩‍👦 Co-applicant Income
* 🏠 Loan Amount
* ⏳ Loan Term
* 👔 Credit History
* 👨‍👩‍👧 Marital Status
* 🎓 Education
* 👩 Gender

Then the AI model will tell you if the **loan is Approved ✅** or **Rejected ❌**.

---

## 🛠️ Tech Stack

* **Python 3.10+** 🐍
* **FastAPI** ⚡ (Backend Framework)
* **Scikit-Learn** 📊 (Machine Learning)
* **Pandas & NumPy** 🔢 (Data Handling)
* **Uvicorn** 🚀 (ASGI Server)

---

## 📊 Machine Learning Model

We use a **Logistic Regression** model for binary classification.
📌 Steps involved:

1. Data Preprocessing 🔧
2. Feature Scaling 📏
3. Model Training 🏋️
4. Evaluation & Prediction 🎯

---

## 📌 Future Improvements

* ✅ Better UI with Tailwind / Bootstrap
* ✅ Deploy on **Heroku / Render**
* ✅ Use advanced ML models (Random Forest, XGBoost)
* ✅ Add database for loan applications

---

## 👨‍💻 Author

Developed with ❤️ by **Ananya Chakraborty**

---

## ⭐ Show your support

If you like this project, please **star ⭐ the repo** and share it with others!
