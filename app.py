import streamlit as st
import numpy as np
import joblib

# Load the model
model = joblib.load("anemia_risk_classifier.pkl")

# --- MAIN UI AREA ---
st.set_page_config(page_title="Anemia Risk Classifier", page_icon="🩺")

st.title("🩺 Anemia Risk Classifier")
st.markdown("### Predict anemia risk based on routine blood test values.")
st.markdown("Enter the values in the sidebar 👉 to get your result.")

# --- SIDEBAR ---
st.sidebar.header("📋 Input Patient Test Values")

age = st.sidebar.number_input("Age (years)", min_value=1, max_value=120, value=25)
sex = st.sidebar.radio("Sex", ["Male", "Female"])
rbc = st.sidebar.number_input("RBC (million cells/µL)", min_value=0.0, value=4.5)
pcv = st.sidebar.number_input("PCV (%)", min_value=0.0, value=36.0)
mcv = st.sidebar.number_input("MCV (fL)", min_value=0.0, value=80.0)
mch = st.sidebar.number_input("MCH (pg)", min_value=0.0, value=28.0)
mchc = st.sidebar.number_input("MCHC (g/dL)", min_value=0.0, value=32.0)
rdw = st.sidebar.number_input("RDW (%)", min_value=0.0, value=14.0)
tlc = st.sidebar.number_input("WBC Count (thousand/µL)", min_value=0.0, value=6.0)
plt = st.sidebar.number_input("Platelet Count (thousand/µL)", min_value=0.0, value=250.0)

# --- PREPROCESSING ---
sex_val = 0.0 if sex == "Male" else 1.0
input_data = np.array([[age, sex_val, rbc, pcv, mcv, mch, mchc, rdw, tlc, plt]])

# --- PREDICTION ---
if st.sidebar.button("🔍 Predict Anemia Risk"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][prediction] * 100

    st.markdown("### 🔎 Prediction Result:")

    if prediction == 1:
        st.error(f"⚠️ **High Risk of Anemia Detected**")
        st.markdown(f"Model confidence: **{probability:.2f}%**")
    else:
        st.success("✅ **No Anemia Detected**")
        st.markdown(f"Model confidence: **{probability:.2f}%**")


# --- FOOTER ---
st.markdown("---")
st.markdown("👩‍💻 Built by **Greeshma** — ML Health Project 2025")
st.markdown("[View source code on GitHub](https://github.com/yourusername/anemia-classifier)")

