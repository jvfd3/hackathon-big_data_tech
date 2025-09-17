#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

def one_hot_encode_parquet(df: pd.DataFrame, columns: list) -> pd.DataFrame:
    """
    Executa one-hot encoding nas colunas especificadas e retorna o dataframe transformado.

    Parâmetros:
    -----------
    df : pd.DataFrame
        DataFrame carregado a partir de arquivo Parquet.
    columns : list
        Lista de nomes de colunas a serem codificadas.

    Retorno:
    --------
    df_encoded : pd.DataFrame
        DataFrame com as colunas originais removidas e substituídas pelas dummies.
    """
    df_encoded = df.copy()
    for col in columns:
        if col in df_encoded.columns:
            # Criar colunas dummies
            dummies = pd.get_dummies(df_encoded[col], prefix=col)
            # Remover coluna original
            df_encoded = df_encoded.drop(columns=[col])
            # Concatenar as novas colunas
            df_encoded = pd.concat([df_encoded, dummies], axis=1)
    return df_encoded

