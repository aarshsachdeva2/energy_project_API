import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.model_selection import train_test_split
import pickle


def create_features(df):

    df.datetime_beginning_ept=pd.to_datetime(df.datetime_beginning_ept).dt.date
    daily_df=df.groupby('datetime_beginning_ept')['mw'].sum()
    daily_df=pd.DataFrame(daily_df).reset_index()
    daily_df['month']=pd.to_datetime(daily_df.datetime_beginning_ept).dt.month
    daily_df['day']=pd.to_datetime(daily_df.datetime_beginning_ept).dt.day
    daily_df['t-7']=daily_df.mw.shift(7)
    daily_df['t-1']=daily_df.mw.shift(1)
    daily_df.dropna(inplace=True)
    daily_df.reset_index(drop=True,inplace=True)
    daily_df=daily_df[['month','day','t-7','t-1','mw']]
    
    return daily_df

def data_processing(df,y):
    
    target=df[y]
    
    X=df.drop(columns=[y])
    
    cat_cols=[
        col for col in X.columns if X[col].nunique()<20
    ]
    
    num_cols=[
        col for col in X.columns if col not in cat_cols
    ]
    trans=ColumnTransformer(
        transformers=[
           ('num_cols',StandardScaler(),num_cols),
           ('cat_cols',OneHotEncoder(sparse_output=False,handle_unknown='ignore'),cat_cols)
        ],

    )
    
    
    X_train,X_test,y_train,y_test=train_test_split(X,target,train_size=0.8,shuffle=False)
    X_train=pd.DataFrame(trans.fit_transform(X_train))
    X_test=pd.DataFrame(trans.transform(X_test))
    
    with open("transformer.pkl","wb") as f:
        pickle.dump(trans,f)
    
    return X_train,X_test,y_train,y_test

    
  