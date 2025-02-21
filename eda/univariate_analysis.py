import pandas as pd 
import numpy as np
from typing import Tuple
import logging 
from typing_extensions import Annotated
from .base_eda import BaseEDA
import matplotlib.pyplot as plt 
import seaborn as sns
from src.data_loader import DataLoader

class NumericalUnivariateAnalyser(BaseEDA):
    """This class is used to perform univariate analysis on numerical data"""
 
    def analyse(self, df) -> None:
        """This method is used to analyse the data
        args: df: pd.DataFrame
        returns: None
        """
        try:
            df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
            numerical_data = df.select_dtypes(include=[np.number])
            print(numerical_data.columns)
            summary = numerical_data.describe()
            logging.info("Data analysis completed")
            return summary
        except Exception as e:
            logging.error("Error while analysing the data")
            raise e 

    def visualize(self, df:pd.DataFrame) -> None:
        """This method is used to visualize the data
        args: df: pd.DataFrame
        returns: None
    
        """
        col = df.columns
        for i in col:
            df[i].plot(kind="hist")
            plt.title(i)
            plt.show()

class CategoricalUnivariateAnalyser(BaseEDA):

    def analyse(self, df):
        pass 

    def visualize(self, df):
        pass

class UnivariateAnalyserFactory:
    def __init__(self, path:str, strategy:BaseEDA) -> None:
        self._path = path
        self._strategy = strategy

    def set_strategy(self, strategy:BaseEDA) -> None:
        self._strategy = strategy

    def perform_univariate_analysis(self) -> None:
        df = DataLoader().load_data(self._path)
        summary = self._strategy.analyse(df)
        print(summary)
        self._strategy.visualize(summary)


if __name__ == "__main__":
    path =  r"D:\Machine Learning\Projects\customer_churn_prediction\data\Telco-Customer-Churn.csv"
    num_strategy = NumericalUnivariateAnalyser()
    per = UnivariateAnalyserFactory(path, num_strategy)
    per.perform_univariate_analysis()

    
 