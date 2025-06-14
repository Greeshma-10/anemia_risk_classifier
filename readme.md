# 🩺 Anemia Risk Classifier (ML + Streamlit)

A machine learning-based web app that predicts anemia risk using routine blood test parameters. Built using Python, scikit-learn, and Streamlit — no HTML/CSS/JS required!


## 🔬 Problem Statement

Early detection of anemia is critical, especially among women and children. This app uses standard blood test features like RBC, PCV, MCH, etc., to predict anemia risk using a trained classification model.


## 🧠 Features

- Clean UI built using Streamlit  
- Live prediction with probability score  
- Random Forest Classifier trained on real patient data  
- Feature importance visualized  
- Interactive sidebar input


## 🚀 Demo

> 🔗 Live App: *(add your Streamlit Cloud URL here)*  
> 📹 Video Demo: *(optional)*


## 📊 Model Details

- **Algorithm:** RandomForestClassifier  
- **Accuracy:** ~89% (without using hemoglobin directly)  
- **Features used:** Age, Sex, RBC, PCV, MCH, MCHC, RDW, TLC, Platelet  
- **EDA:** Performed using pandas, seaborn  
- **Target:** Anemia (1 = Yes, 0 = No) derived from HGB thresholds (WHO)

---

## 📁 Project Structure

anemia-risk-classifier/
├── anemia_classifier.ipynb # Full notebook (EDA + model training)
├── anemia_risk_classifier.pkl # Trained model
├── app.py # Streamlit web app
└── README.md # This file



## 🛠️ How to Run Locally

1. Clone the repo  
2. Install requirements:
```bash
pip install streamlit scikit-learn pandas numpy joblib
Run the app:
streamlit run app.py

🌟 Credits
Streamlit for rapid UI

Scikit-learn for model building

Real patient dataset (anonymized for educational use)- kaggle 

