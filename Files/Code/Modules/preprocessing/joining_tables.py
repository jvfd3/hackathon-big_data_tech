import pandas as pd

def join_tables(parquet_files): # Not working yet
  # parquet_files: [lojas_path, transacoes_path, produtos_path]
  lojas = pd.read_parquet(parquet_files[0])
  transacoes = pd.read_parquet(parquet_files[1])
  produtos = pd.read_parquet(parquet_files[2])

  # Join LOJAS with TRANSAÇÕES on PDV <-> internal_store_id
  lojas_transacoes = transacoes.merge(
    lojas,
    left_on='internal_store_id',
    right_on='PDV',
    how='left'
  )

  # Join with PRODUTOS on produto <-> internal_product_id
  full_joined = lojas_transacoes.merge(
    produtos,
    left_on='internal_product_id',
    right_on='produto',
    how='left'
  )

  return full_joined

# Example usage:
# parquet_files = [
#     'path/to/lojas.parquet',
#     'path/to/transacoes.parquet',
#     'path/to/produtos.parquet'
# ]
# df = join_tables(parquet_files)