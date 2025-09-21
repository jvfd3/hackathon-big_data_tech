# Como Executar o Código de Submissão

Este notebook gera o arquivo de submissão agregando as vendas por semana, PDV e produto.

## Pré-requisitos

- Python 3.8 ou superior
- Pacotes: pandas, pyarrow
- Arquivo Parquet de transações disponível em `../Data/hackathon_2025_templates/`

## Passos para Execução

1. **Instale os pacotes necessários**

   Execute no terminal:

   ```powershell
   pip install pandas pyarrow
   ```

2. **Abra o notebook**

   Abra o arquivo `mvp.ipynb` na pasta `Submissions/Submission1` usando o Jupyter Notebook ou VS Code.

3. **Execute a célula de código**

   Basta executar a célula única do notebook. Ela irá:

   - Carregar o arquivo Parquet de transações
   - Filtrar e agregar os dados por semana, PDV e produto
   - Salvar o resultado em `submission1.csv` no mesmo diretório
   - Exibir as primeiras linhas do resultado

## Saída

- O arquivo gerado será `submission1.csv` com o formato:

  ```cs
  semana;pdv;produto;quantidade
  1;123;456;789
  ...
  ```

## Observações

- Certifique-se de que o caminho para o arquivo Parquet está correto.
- O notebook pode ser executado em qualquer ambiente Python compatível.
