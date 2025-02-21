import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np 
from src.data_loader import DataLoader

class DataInspection:
    """This class is """
    def __init__(self, df):
        self.df = df

    def get_data_summary(self):
        shape = self.df.shape
        dtypes = self.df.dtypes
        columns = self.df.columns
        memory_usage = self.df.memory_usage(deep=True)
        
        # Create a DataFrame to summarize all information
        summary_df = pd.DataFrame({
            'Description': ['Number of Rows', 'Number of Columns', 'Column Names', 'Column Data Types', 'Memory Usage'],
            'Details': [
                shape[0], 
                shape[1],  
                list(columns),   
                list(dtypes),   
                memory_usage.sum()   
            ]
        })
        return summary_df 
    
    def missing_data_summary(self):
        missing_count = self.df.isnull().sum()
        missing_percentage = (missing_count / len(self.df)) * 100
        return f"Missing Count: {missing_count}, \n Missing Percentage {missing_percentage}" 
    
    def descriptive_statistics(self):
        print("Descriptive Statistics..")
        return self.df.describe()
     
if __name__  == "__main__":
    path = r"D:\Machine Learning\Projects\customer_churn_prediction\data\Telco-Customer-Churn.csv"
    df = DataLoader().load_data(path)
    inspect = DataInspection(df=df)
    print( inspect.get_data_summary())
    print()
    print(inspect.missing_data_summary())
    print()
    print(inspect.descriptive_statistics())
