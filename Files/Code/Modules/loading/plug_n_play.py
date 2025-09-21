""" Importing libraries """

import pandas as pd
import time

""" Importing our modules """

""" USE THIS FOR LOCAL FUNCTION TESTING """
# from Files.Code.Modules.loading.read_parquet import get_file_paths, load_dataframes
# # from Files.Code.Modules.preprocessing.onehot import one_hot_encode_parquet
# from Files.Code.Modules.preprocessing.removing_categorical_tables import get_numerical_table
# from Files.Code.Modules.preprocessing.removing_outliers import remove_outliers
# from Files.Code.Modules.preprocessing.pivoting import pivoting_df
# from Files.Code.Modules.preprocessing.rescaling import rescale_zero_to_one

""" USE THIS FOR MODULE USAGE """
from Modules.loading.read_parquet import get_file_paths, load_dataframes
# from Modules.preprocessing.onehot import one_hot_encode_parquet
from Modules.preprocessing.removing_categorical_tables import get_numerical_table
from Modules.preprocessing.removing_outliers import remove_outliers
from Modules.preprocessing.pivoting import pivoting_df
# from Modules.preprocessing.rescaling import rescale_zero_to_one

last_run = time.time()

def debug_time(label: str, debug: dict):
    global last_run
    if not debug['time']:
        return
    current_time = time.time()
    elapsed = current_time - last_run
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)
    miliseconds = int((elapsed - minutes * 60 - seconds) * 1000)
    print(f"{minutes:02d}:{seconds:02d}:{miliseconds:03d}", label)
    last_run = current_time

def get_clean_data(debug) -> pd.DataFrame:
    debug = hyperparams['debug']
    outliers = hyperparams['loading']['ourliers']
    FILE_PATHS = get_file_paths() # Setting up the constants
    debug_time('loaded_data', debug)
    loaded_data = load_dataframes(FILE_PATHS) # Loading the data
    debug_time('numerical_table', debug)
    numerical_table = get_numerical_table(loaded_data) # getting only the needed numerical data
    outlierless = remove_outliers(numerical_table.copy(), 'quantity', 0.1, 0.9) # Removing outliers from 'quantity' column
    debug_time('outlierless', debug)
    debug_time('pivoted_df', debug)
    pivoted_df = pivoting_df(outlierless.copy()) # Pivoting the DataFrame
    
    # debug_time('rescaled_df', debug)
    # rescaled_df = rescale_zero_to_one(pivoted_df.copy()) # Re-scaling
    # debug_time('copying', debug)
    # clean_data = rescaled_df.copy() # Final clean data
    
    debug_time('returning', debug)
    return pivoted_df
