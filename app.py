import streamlit as st
import pickle

# Load trained model
model = pickle.load(open("diabetes_model.pkl","rb"))

st.title("Diabetes Prediction App")

# User inputs
preg = st.number_input("Pregnancies", 0, 20, 1)
glucose = st.number_input("Glucose", 0, 200, 100)
bp = st.number_input("Blood Pressure", 0, 150, 70)
skin = st.number_input("Skin Thickness", 0, 100, 20)
insulin = st.number_input("Insulin", 0, 900, 80)
bmi = st.number_input("BMI", 0.0, 70.0, 25.0)
dpf = st.number_input("Diabetes Pedigree Function", 0.0, 2.5, 0.5)
age = st.number_input("Age", 0, 100, 30)

# Prediction
features = [[preg, glucose, bp, skin, insulin, bmi, dpf, age]]
prediction = model.predict(features)

st.write("Prediction:", "Diabetic" if prediction[0]==1 else "Non-Diabetic")
