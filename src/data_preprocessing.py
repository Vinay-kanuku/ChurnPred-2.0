import  pandas as pd 
import numpy as np 
from abc import ABC, abstractmethod
import logging 
from typing import Tuple
from typing_extensions import Annotated

class DataPreprocessing(ABC):
    """ This class is an abstract class for data preprocessing"""
    @abstractmethod
    def preprocess(self, df:pd.DataFrame) -> pd.DataFrame:
        pass 
    




