import pandas as pd
import numpy as np

def get_numerical_table(tables) -> pd.DataFrame:
    """ Returns only the numerical columns of a DataFrame """
    tids = tables["transacoes"]
    # Drop columns
    cols_to_drop = [
      'discount',
      'distributor_id',
      'gross_profit',
      'gross_value',
      # 'internal_product_id', # Mandatory
      # 'internal_store_id', # Mandatory
      'net_value',
      # 'quantity', # Mandatory
      'reference_date',
      'taxes',
      # 'transaction_date' # Mandatory
    ]
    # print(tids.dtypes) # List columns and types
    tids = tids.drop(columns=cols_to_drop)
    # print(tids.dtypes) # List columns and types

    cols_to_convert = [
        # 'discount',
        # 'distributor_id',
        # 'gross_profit',
        # 'gross_value',
        # 'internal_product_id',
        # 'internal_store_id',
        # 'net_value',
        'quantity',
        # 'reference_date',
        # 'taxes',
        # 'transaction_date'
    ]
    # Convert those columns types to int
    # tids[cols_to_convert] = tids[cols_to_convert].astype(int)
    tids[cols_to_convert] = np.ceil(tids[cols_to_convert]).astype(int)
    # tids['reference_date'] = pd.to_datetime(tids["reference_date"])
    tids['transaction_date'] = pd.to_datetime(tids["transaction_date"])

    return tids
