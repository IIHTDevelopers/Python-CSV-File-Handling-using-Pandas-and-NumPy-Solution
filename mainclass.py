import pandas as pd
import numpy as np

class SalesDataProcessor:
    def __init__(self, file_path):
        """Initialize with the file path to the CSV."""
        self.file_path = file_path
        self.df = None

    def read_csv(self):
        """Read the CSV file into a pandas DataFrame."""
        try:
            self.df = pd.read_csv(self.file_path)
        except FileNotFoundError:
            raise FileNotFoundError(f"The file at {self.file_path} could not be found.")
        except pd.errors.EmptyDataError:
            raise ValueError("The CSV file is empty.")
        except Exception as e:
            raise Exception(f"An error occurred while reading the CSV: {e}")

    def convert_sales_column(self):
        """Convert the total_sales column to a NumPy array."""
        if self.df is not None:
            if 'total_sales' in self.df.columns:
                return np.array(self.df['total_sales'])
            else:
                raise ValueError("'total_sales' column not found in the CSV file.")
        else:
            raise ValueError("CSV data has not been loaded. Please call read_csv() first.")
