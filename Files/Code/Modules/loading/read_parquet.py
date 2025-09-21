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

def get_file_paths():
    """
    Returns a list of file paths to Parquet files.

    Returns:
        list: List of Parquet file paths.
    """

    DATA_PATH = "../Data/hackathon_2025_templates/part-00000-tid-"

    FILE_HASH = [
        "2779033056155408584-f6316110-4c9a-4061-ae48-69b77c7c8c36", # LOJAS
        "5196563791502273604-c90d3a24-52f2-4955-b4ec-fb143aae74d8", # TRANSAÇÕES
        "7173294866425216458-eae53fbf-d19e-4130-ba74-78f96b9675f1", # PRODUTOS
    ]

    SUFIX = "-4-1-c000.snappy.parquet"

    FILE_NAMES = [DATA_PATH + hash + SUFIX for hash in FILE_HASH]
    return FILE_NAMES

def load_dataframes(file_paths):
    """
    Loads multiple Parquet files into a dictionary of pandas DataFrames.

    Args:
        file_paths (list): List of file paths to Parquet files.

    Returns:
        dict: Dictionary where keys are file identifiers and values are corresponding DataFrames.
    """
    dataframes = {}
    identifiers = ["lojas", "transacoes", "produtos"]

    for path, id in zip(file_paths, identifiers):
        dataframes[id] = read_parquet_file(path)

    return dataframes

def lazy_load_clean_data():
    """
    Lazily loads a preprocessed clean data Parquet file.

    Returns:
        pd.DataFrame: Data read from the clean data Parquet file.
    """
    CLEAN_DATA_PATH = "../Data/clean_data.parquet"
    return read_parquet_file(CLEAN_DATA_PATH)

def save_cleaned_data_path(df: pd.DataFrame):
    """
    Saves the given DataFrame to a Parquet file.

    Args:
        df (pd.DataFrame): DataFrame to be saved.
    """
    CLEAN_DATA_PATH = "../Data/clean_data.parquet"
    df.to_parquet(CLEAN_DATA_PATH, index=True)
