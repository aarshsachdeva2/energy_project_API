import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer 
from dotenv import load_dotenv
from sqlalchemy import inspect
import pickle
from features import create_features,data_processing


with open('db_instance.pkl','rb') as f:
    data=pickle.load(f)

df=create_features(data)
X_train,X_test,y_train,y_test=data_processing(df,"mw")

lr=LinearRegression()
model=lr.fit(X_train,y_train)

with open("model.pkl","wb") as f:
    pickle.dump(model,f)