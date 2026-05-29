from fastapi import FastAPI
from schema.user_input import Customer
import pandas as pd
import joblib
from fastapi.responses import JSONResponse
from src.customer_churn_prediction.utils import avg_charges

app=FastAPI()

model=joblib.load('models/model.pkl')

@app.get('/')
def home():
    return {'message':'Customer Churn Prediction API'}

@app.post('/predict')
def churn_predict(data:Customer):
    try:
        input_data= data.model_dump()
        df= pd.DataFrame([input_data])

        prediction =int( model.predict(df)[0])
        probability= float(model.predict_proba(df)[0][1])
        
        return JSONResponse(status_code=200,
                            content={
                                'Result':prediction,
                                'Churn_Probabilty':probability
                                })
    except Exception as e:
        return JSONResponse(status_code=500,
                            content={"error":str(e)})
    







