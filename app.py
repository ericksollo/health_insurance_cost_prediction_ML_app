# import libraries
import streamlit as st
import pandas as pd
import numpy as np
import joblib

#load scaler
scaler = joblib.load('models/scaler.pkl')

# load models for categorical features encoding
le_gender = joblib.load('models/LabelEncoder_gender.pkl')
le_diabetic = joblib.load('models/LabelEncoder_diabetic.pkl')
le_smoker= joblib.load('models/LabelEncoder_smoker.pkl')
le_region= joblib.load('models/LabelEncoder_region.pkl')

#load best model
model = joblib.load('models/best_model.pkl')

# STREAMLIT APP

#page config
st.set_page_config(page_title= "Health Insurance Claim Predictor", layout="centered")
st.markdown("<h1 style='text-align: center;'>Health Insurance Payment Prediction App</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter the details below to estimate your Health Insurance payment amount</p>", unsafe_allow_html=True)
# user input form

with st.form("input_form"):
    col1, col2 = st.columns(2)
    with col1:
        age = st.number_input("Age", min_value=0, max_value=100, value=30)
        bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=20.0)
        children =st.number_input("Number of Children",min_value=0, max_value=10, value=1 )
        bloodpressure= st.number_input("Blood Pressure", min_value=60, max_value=200, value=120)


    with col2:
        gender= st.selectbox("Gender", options= le_gender.classes_)
        diabetic = st.selectbox("Diabetic", options= le_diabetic.classes_)
        smoker = st.selectbox("Smoker", options= le_smoker.classes_)
        region = st.selectbox("Region", options= le_region.classes_)

    submitted = st.form_submit_button("Predict Payment")


# user input to DataFrame

if submitted:

    input_data = pd.DataFrame({
        "age": [age],
        "gender": [gender],
        "bmi": [bmi],
        "bloodpressure": [bloodpressure],
        "diabetic": [diabetic],
        "children": [children],
        "smoker": [smoker],
        "region": [region]
    })

    # encoding categorical features
    input_data["gender"] = le_gender.transform(input_data["gender"])
    input_data['diabetic'] = le_diabetic.transform(input_data["diabetic"])
    input_data["smoker"] = le_smoker.transform(input_data["smoker"])
    input_data["region"] = le_region.transform(input_data["region"])

    # scaling numerical features
    numerical_features = ["age", "bmi", "bloodpressure", "children"]
    input_data[numerical_features] = scaler.transform(input_data[numerical_features])

    # prediction of payment amount
    prediction = model.predict(input_data)[0]

    st.success(f"***Estimated Insurance Payment Ammount:*** ${prediction:,.2f}")
