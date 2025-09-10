import pandas as pd

def read_parquet_file(file_path):
  """
  Reads a Parquet file from the given file path and returns the data as a pandas DataFrame.

  Args:
    file_path (str): Path to the Parquet file.

  Returns:
    pd.DataFrame: Data read from the Parquet file.
  """
  return pd.read_parquet(file_path)