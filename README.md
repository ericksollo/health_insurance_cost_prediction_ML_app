# 🏥 Health Insurance Cost Prediction

A machine learning web application that predicts health insurance payment amounts based on patient details. Built with **Scikit-learn**, **XGBoost**, and deployed with **Streamlit**.

🔗 **Live App:** [health-insurance-cost-prediction-ml-app.streamlit.app](https://health-insurance-cost-prediction-ml-app.streamlit.app)

---

## 📌 Overview

This project trains and compares multiple regression models to predict health insurance claim amounts. The best-performing model is then served through an interactive Streamlit web app where users can enter their personal details and instantly get an estimated insurance payment amount.

---

## 🚀 Features

- 🔍 Predict insurance payment amount based on patient profile
- 📊 Full EDA with visualizations in Jupyter Notebook
- 🤖 5 ML models trained and compared — best one auto-selected
- ⚙️ Preprocessing pipeline with Label Encoding and Standard Scaling
- 🌐 Fully deployed and accessible online via Streamlit Cloud

---

## 🛠️ Tech Stack

| Tool                 | Purpose                              |
| -------------------- | ------------------------------------ |
| Python 3.11          | Core programming language            |
| Scikit-learn         | ML models, preprocessing, evaluation |
| XGBoost              | Gradient boosting regression         |
| Pandas & NumPy       | Data processing                      |
| Matplotlib & Seaborn | Data visualization                   |
| Streamlit            | Web app framework & deployment       |
| Joblib               | Model serialization                  |
| Jupyter Notebook     | EDA & model training                 |

---

## 📁 Project Structure

```
health_insurance_cost_prediction_ML_app/
├── data/
│   └── raw/
│       └── insurance.csv         # Raw dataset
├── models/
│   ├── best_model.pkl            # Best trained ML model
│   ├── scaler.pkl                # StandardScaler for numerical features
│   ├── LabelEncoder_gender.pkl   # Encoder for gender
│   ├── LabelEncoder_diabetic.pkl # Encoder for diabetic status
│   ├── LabelEncoder_smoker.pkl   # Encoder for smoker status
│   └── LabelEncoder_region.pkl   # Encoder for region
├── app.py                        # Streamlit web application
├── notebook.ipynb                # EDA, preprocessing & model training
├── requirements.txt              # Project dependencies
├── runtime.txt                   # Python version reference (3.11)
└── .gitignore
```

---

## 📦 Dataset

- **Source:** [Insurance Data — GitHub](https://github.com/Onurbltc/InsuranceData) by Onurbltc
- **Features:** `age`, `gender`, `bmi`, `bloodpressure`, `diabetic`, `children`, `smoker`, `region`
- **Target:** `claim` — insurance payment amount in USD

> ✅ The dataset is already included in `data/raw/insurance.csv`. No separate download needed.

---

## 🤖 Models Trained & Compared

Five regression models were trained and evaluated using **R², MAE, and RMSE**:

| Model                           | Notes                                 |
| ------------------------------- | ------------------------------------- |
| Linear Regression               | Baseline model                        |
| Polynomial Regression           | Degrees 2 and 3 tested, best selected |
| Random Forest                   | Tuned with GridSearchCV               |
| Support Vector Regression (SVR) | Tuned with GridSearchCV               |
| **XGBoost** ⭐                  | Best performing model                 |

The model with the highest **R² score** was automatically selected and saved as `best_model.pkl`.

---

## 📊 ML Workflow

```
Raw Data → EDA → Data Cleaning → Feature Encoding →
Feature Scaling → Model Training → Model Comparison →
Best Model Selection → Deployment
```

1. **EDA** — distributions, correlations, claim analysis by region, gender, and smoker status
2. **Data Cleaning** — dropped missing values and duplicates
3. **Feature Encoding** — LabelEncoder for gender, diabetic, smoker, region
4. **Feature Scaling** — StandardScaler for age, bmi, bloodpressure, children
5. **Model Training** — 5 models trained with GridSearchCV hyperparameter tuning
6. **Deployment** — best model exported as `.pkl` and served via Streamlit

---

## ⚙️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/ericksollo/health_insurance_cost_prediction_ML_app.git
cd health_insurance_cost_prediction_ML_app
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

---

## ☁️ Deploy on Streamlit Cloud

1. Fork this repository
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub
3. Click **"New app"** and select your forked repo
4. Set **main file path** to `app.py`
5. ⚠️ **IMPORTANT:** Go to **Advanced settings → Python version** and set it to **Python 3.11**
6. Click **Deploy**

> **Why Python 3.11?** Streamlit Cloud defaults to Python 3.13 which has compatibility issues with some ML packages used in this project. Python 3.11 is fully tested and stable with all dependencies here.

---

## 🐛 Troubleshooting

| Error                         | Cause                                     | Fix                                                      |
| ----------------------------- | ----------------------------------------- | -------------------------------------------------------- |
| `ModuleNotFoundError: joblib` | Wrong Python version on Streamlit Cloud   | Set Python version to **3.11** in Streamlit App Settings |
| `pandas` version conflict     | pandas 3.x is incompatible with streamlit | Use `pandas==2.2.2` as already set in `requirements.txt` |
| Model file not found          | Wrong file path                           | Ensure the `models/` folder exists in the repo root      |
| App crashes on load           | Missing `.pkl` files on GitHub            | Make sure all 6 model files are committed and pushed     |

---

## 👤 Author

**Ericksollo**

- GitHub: [@ericksollo](https://github.com/ericksollo)
- Linkedin: [@ericksollo](https://www.linkedin.com/in/ericksollo/)
- Live App: [health-insurance-cost-prediction-ml-app.streamlit.app](https://health-insurance-cost-prediction-ml-app.streamlit.app)

---
