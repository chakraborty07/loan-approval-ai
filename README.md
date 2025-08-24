```markdown
# 🤖 Loan Approval Prediction using AI
Welcome to the **Loan Approval Prediction System** 🎉  
This project uses **Machine Learning** 🧠 and **FastAPI** ⚡ to predict whether a loan application should be **approved ✅** or **rejected ❌** based on applicant details.  

## 📂 Project Structure
```

loan\_approval\_ai/
│── app/
│   └── main.py          # FastAPI web app
│── artifacts/
│   ├── loan\_model.pkl   # Trained ML model
│   └── scaler.pkl       # Standard scaler for preprocessing
│── data/
│   └── loan.csv         # Dataset
│── train\_model.py       # Script to train the ML model
│── requirements.txt     # Project dependencies
│── README.md            # Project documentation

````

## ⚙️ Features
✨ Predicts loan approval with AI model  
✨ Simple and intuitive **web form interface**  
✨ Built using **FastAPI** for backend  
✨ Machine learning with **Scikit-Learn**  
✨ Easy to deploy locally or on cloud  

## 🚀 Getting Started
### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/loan_approval_ai.git
cd loan_approval_ai
````

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Train the model

```bash
python train_model.py
```

This will generate `loan_model.pkl` and `scaler.pkl` in the `artifacts/` folder.

### 4️⃣ Run the web app

```bash
uvicorn app.main:app --reload
```

Visit 👉 [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

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

## 🛠️ Tech Stack

* **Python 3.10+** 🐍
* **FastAPI** ⚡ (Backend Framework)
* **Scikit-Learn** 📊 (Machine Learning)
* **Pandas & NumPy** 🔢 (Data Handling)
* **Uvicorn** 🚀 (ASGI Server)

## 📊 Machine Learning Model

We use a **Logistic Regression** model for binary classification.
📌 Steps involved:

1. Data Preprocessing 🔧
2. Feature Scaling 📏
3. Model Training 🏋️
4. Evaluation & Prediction 🎯

## 📌 Future Improvements

* ✅ Better UI with Tailwind / Bootstrap
* ✅ Deploy on **Heroku / Render**
* ✅ Use advanced ML models (Random Forest, XGBoost)
* ✅ Add database for loan applications

## 👨‍💻 Author

Developed with ❤️ by **Ananya Chakraborty**

## ⭐ Show your support

If you like this project, please **star ⭐ the repo** and share it with others!

