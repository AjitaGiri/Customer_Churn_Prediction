import streamlit as st
import requests

API_URL = "https://customer-churn-prediction-1sxg.onrender.com/predict"
st.title("Customer Churn Prediction")

st.subheader("Customer Details")
gender=st.selectbox("gender",['Male','Female'])
SeniorCitizen=st.selectbox("SeniorCitizen",[0,1])
Partner=st.selectbox("Partner",['Yes','No'])
Dependents=st.selectbox("Dependents",['Yes','No'])
tenure=st.number_input('tenure',min_value=1,max_value=72)
PhoneService=st.selectbox('PhoneService',['Yes','No'])
MultipleLines=st.selectbox('MultipleLines',['No phone service','No','Yes'])
InternetService=st.selectbox('InternetService', ['DSL','Fiber optic','No'])
OnlineSecurity=st.selectbox('OnlineSecurity',['No','Yes','No internet service'])
OnlineBackup=st.selectbox('OnlineBackup', ['Yes','No','No internet service'])
DeviceProtection=st.selectbox('DeviceProtection', ['No','Yes','No internet service'])
TechSupport=st.selectbox('TechSupport', ['No','Yes','No internet service'])
StreamingTV=st.selectbox('StreamingTV',['No','Yes','No internet service'])
StreamingMovies=st.selectbox('StreamingMovies',['No','Yes','No internet service'])
Contract=st.selectbox('Contract',['Month-to-month','One year','Two year']) 
PaperlessBilling=st.selectbox('PaperlessBilling',['Yes','No'])
PaymentMethod=st.selectbox('PaymentMethod', ['Bank transfer (automatic)','Credit card (automatic)','Electronic check','Mailed check'])
MonthlyCharges=st.number_input('MonthlyCharges',min_value=0.0) 
TotalCharges=st.number_input('TotalCharges',min_value=0.0)

if st.button('Predict Churn'):

    input_data = {
    'gender': gender,
    'SeniorCitizen': SeniorCitizen,
    'Partner': Partner,
    'Dependents': Dependents,
    'tenure': tenure,
    'PhoneService': PhoneService,
    'MultipleLines': MultipleLines,
    'InternetService': InternetService,
    'OnlineSecurity': OnlineSecurity,
    'OnlineBackup': OnlineBackup,
    'DeviceProtection': DeviceProtection,
    'TechSupport': TechSupport,
    'StreamingTV': StreamingTV,
    'StreamingMovies': StreamingMovies,
    'Contract': Contract,
    'PaperlessBilling': PaperlessBilling,
    'PaymentMethod': PaymentMethod,
    'MonthlyCharges': MonthlyCharges,
    'TotalCharges': TotalCharges
 }
    
    response=requests.post(API_URL,json=input_data)
    result=response.json()
    
    prob= result['Churn_Probabilty']
    if result['Result']==1:
      st.error('Customer likely to churn')
      st.write(f"Churn Probability: {prob:.2f}")
    else:
     st.success('Customer is not likely to churn')
     st.write(f"Churn Probability: {prob:.2f}")


