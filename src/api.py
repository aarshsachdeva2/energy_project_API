from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
import time
from fastapi.middleware.cors import CORSMiddleware
a=time.time()

b=time.time()
from db import engine

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("model.pkl",'rb') as f:
    model=pickle.load(f)
    
class PredictionRequest(BaseModel):
    date: str
    
@app.post("/predict")
def predict(request: PredictionRequest):
    query="""
        select month,day,"t-7","t-1"
        from feature_tbl
        where date=%(date)s
    """
    
    data_i=pd.read_sql(
        query,
        engine,
        params={"date":request.date}
    )
    c=time.time()
    print('trans load start')
    with open("transformer.pkl","rb") as f:
        transformer=pickle.load(f)
    print('db load end')
    d=time.time()    
    data=transformer.transform(data_i)
    

    
    prediction = model.predict(data)

    return {
        "date": request.date,
        "prediction": prediction[0]
    }
    

