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
from datetime import datetime

def format_output(data):
  """ Formats the output data into CSV format.

  Args:
    data (parquet data): Headers: ['semana', 'pdv', 'produto', 'quantidade']

  Returns:
    str: The formatted CSV string.
  """
  if not data:
    return ""
  
  # converting the parquet data to CSV format
  df = pd.DataFrame(data, columns=['semana', 'pdv', 'produto', 'quantidade'])
  csv_data = df.to_csv(index=False, sep=';', encoding='utf-8')
  return csv_data
  
def save_to_csv(data, file_path='Files/Output/results'):
  """ Saves the formatted data to a CSV file.

  Args:
    data (str): The formatted CSV string.
    file_path (str): The path where the CSV file will be saved.
  """
  # Get timestamp for unique file naming
  timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
  file_path = f"{file_path}_{timestamp}.csv"
  
  with open(file_path, 'w') as file:
    file.write(data)
