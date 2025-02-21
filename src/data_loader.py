import pandas as pd
import logging
from pathlib import Path

class DataLoader:
    """A utility class to load datasets."""
    def load_data(self, path:str) -> pd.DataFrame:
        """
        Loads the data from the specified path.
        Returns:
            pd.DataFrame: The loaded dataset.
        Raises:
            FileNotFoundError: If the file does not exist.
            ValueError: If the file cannot be loaded into a DataFrame.
        """
        try:
            path: Path = Path(path)
            if not path.exists():
                raise FileNotFoundError(f"File not found: {path}")
            
            # Attempt to load the CSV file
            df = pd.read_csv(path)
            logging.info(f"Data loaded successfully from {path}")
            return df
        except FileNotFoundError as e:
            logging.error(f"FileNotFoundError: {e}")
            raise
        except pd.errors.ParserError as e:
            logging.error(f"ParserError while loading the file: {e}")
            raise ValueError(f"Failed to parse the file at {path}") from e
        except Exception as e:
            logging.error(f"Unexpected error while loading the data: {e}")
            raise
