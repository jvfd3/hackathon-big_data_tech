""" Aims to format the output data into a structured format (CSV) for required submission

1. **Arquivo de previsão** no formato **CSV ou Parquet**, com as seguintes colunas:

   | **semana** | **pdv** | **produto** | **quantidade** |
   | ---------- | ------- | ----------- | -------------- |
   | 1          | 1023    | 123         | 120            |
   | 2          | 1045    | 234         | 85             |
   | 3          | 1023    | 456         | 110            |

   No caso do csv, utilize ";" como caractere separador (exemplo: 1;1023;123;120) e encoding UTF-8.

   1. semana (número inteiro): número da semana (1 a 4 de janeiro/2023)
   2. pdv (número inteiro): código do ponto de venda
   3. produto (número inteiro): código do SKU
   4. quantidade (número inteiro): previsão de vendas
"""

import pandas as pd

def forecast_to_output(predictions) -> pd.DataFrame:
    """
    Converte a previsão do modelo em um DataFrame formatado para submissão.
    
    Args:
        prediction (torch.Tensor): Tensor de previsão com shape (num_predictions, output_size).
        col_id (str): Identificador da coluna no formato 'produto_loja'.
        
    Returns:
        pd.DataFrame: DataFrame formatado com colunas ['semana', 'pdv', 'produto', 'quantidade'].
    """
    import math

    df_final = pd.DataFrame(columns=['semana', 'pdv', 'produto', 'quantidade'])
    df_final = df_final.astype({
        'semana': 'int32',
        'pdv': 'int32',
        'produto': 'int32',
        'quantidade': 'int32'
    })
    
    for key, value in predictions.items():
        product_id, store_id = key
        values = value.detach().cpu().numpy().flatten()

        weeks = []
        for i in range(0, len(values), 7):
            week_sum = values[i:i+7].sum()
            weeks.append(math.ceil(week_sum))

        # Crie o DataFrame final
        df_temp = pd.DataFrame({
            'semana': list(range(1, len(weeks) + 1)),
            'pdv': store_id,
            'produto': product_id,
            'quantidade': weeks
        })
        # Append to df_final
        df_final = pd.concat([df_final, df_temp], ignore_index=True)

    df_final.to_csv('submission.csv', index=False, sep=';', encoding='utf-8')
    return df_final