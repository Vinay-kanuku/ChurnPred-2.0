from abc import ABC, abstractmethod
import logging
import pandas as pd
import numpy as np
from typing import Tuple
from typing_extensions import Annotated

class BaseOutlierHandler(ABC):
    """This is an abstract class to detect and handle outliers."""
    
    @abstractmethod
    def detect(self, data: pd.Series) -> pd.Series:
        """
        Detects outliers in the given data.
        Args:
            data (pd.Series): The data to detect outliers in.
        Returns:
            pd.Series: A boolean series indicating the presence of outliers.
        """
        pass

    @abstractmethod
    def handle(self, data: pd.Series) -> pd.Series:
        """
        Handles outliers in the given data.
        Args:
            data (pd.Series): The data to handle outliers in.
        Returns:
            pd.Series: The data with outliers handled.
        """
        pass

