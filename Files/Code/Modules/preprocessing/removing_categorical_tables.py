import pandas as pd

def get_numerical_table(tables) -> pd.DataFrame:
    """ Returns only the numerical columns of a DataFrame """
    transactions = tables["transacoes"]
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
    # print(transactions.dtypes) # List columns and types
    transactions = transactions.drop(columns=cols_to_drop)
    # print(transactions.dtypes) # List columns and types

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
    transactions[cols_to_convert] = transactions[cols_to_convert].astype(int)

    return transactions
