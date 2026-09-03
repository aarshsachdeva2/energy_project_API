import pandas as pd


class data_load():
    def __init__(self):
        pass
        
    def data_loading(self,path):
        df=pd.read_csv(path)
        return df
    
    