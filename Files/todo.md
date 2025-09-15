# To Do

- [ ] Create the project structure
  - Loading
    - [ ] Load Data
  - Transforming
    - normalization
      - [ ] Removing outliers
      - [ ] Analysing the distribution of the Ids
        - [ ] Renaming the IDs if needed
    - [ ] Feature Selection (?)
    - [ ] Handling missing values
  - enrichment
    - [ ] Encoding Strategies
      - [ ] 1️⃣♨️ encoding
      - [ ] Label encoding (?)
      - [ ] Target encoding (?)
    - [ ] Add location related features
      - [ ] find data from zipcode
        - [ ] Latitude
        - [ ] Longitude
        - [ ] Temperature
        - [ ] Rain
        - [ ] Country
    - [ ] Add time related features
      - [ ] Date to: YEAR|MONTH|DAY|WEEKDAY|WEEKEND|YEARSDAY|DAYSTOWEEKEND
    - [ ] Add Money related features
      - [ ] Sum of last 7 days sales
      - [ ] Moving average of last 30 days sales
  - training
    - [ ] Model selection
      - Baselines:
        - [ ] Moving Average
        - [ ] Naive Forecast
      - Classical ML:
        - [ ] LightGBM
        - [ ] XGBoost
        - [ ] CatBoost
      - DL models
        - [ ] RNN
        - [ ] LSTM
        - [ ] TemporalFusionTransformer
    - [ ] Change parameters
      - [ ] Window size
      - [ ] Learning rate
      - [ ] Batch size
      - [ ] Number of epochs
      - [ ] Layers
      - [ ] Dropout
      - [ ] Activation functions
  - evaluation
    - [ ] Entender como aplicar o WMAPE

## Previsão de Demanda com WMAPE

Eles estão usando o WMAPE (Weighted Mean Absolute Percentage Error) como métrica para avaliar a precisão das previsões de demanda.

WMAPE (Weighted Mean Absolute Percentage Error) é uma métrica que mede a precisão das previsões de demanda, ponderando os erros com base na importância de cada item, como o volume de vendas ou o faturamento. Ao contrário do MAPE, o WMAPE evita distorções causadas por produtos de baixo giro e permite comparar produtos com volumes de venda diferentes, focando nos itens mais representativos para o negócio. É um indicador estratégico usado no planejamento de demanda para garantir que os erros de previsão tenham um impacto alinhado com os objetivos da empresa.
