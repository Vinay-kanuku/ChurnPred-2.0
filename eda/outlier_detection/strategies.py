from .base_outlier_handler import BaseOutlierHandler
from abc import ABC, abstractmethod
import pandas as pd 
import numpy as np 
from src.data_loader import DataLoader

class IQRHandler(BaseOutlierHandler):
    def detect(self, data:pd.Series) -> pd.Series:
        """
        This methos detect the outliers by IQR method
        args: pd.Series
        retuns: pd.Series
        """
        q1 = data.quantile(0.25)
        q3 = data.quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        outliers = (data < lower_bound) | (data > upper_bound)
        print(f"couutn{outliers.sum()}")
        return  outliers
    def handle(self, data:pd.Series) -> pd.Series:
        is_outlier = self.detect(data=data)
        return data[~is_outlier]
    

class Outliers:
    def __init__(self, data: pd.Series):
        self._data = data

    def perform(self) -> pd.Series:
        """
        This method handles the outliers in the data using IQRHandler
        args: None
        returns: pd.Series
        """
        return IQRHandler().handle(self._data)

if __name__ ==  "__main__":
    path = r"D:\Machine Learning\Projects\customer_churn_prediction\data\Telco-Customer-Churn.csv"
    
    df = DataLoader().load_data(path=path)
    new_df = Outliers(pd.to_numeric(df["TotalCharges"], errors="coerce")).perform()
    print(new_df)
    