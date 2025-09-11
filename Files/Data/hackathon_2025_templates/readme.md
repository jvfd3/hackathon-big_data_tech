# Descrição dos Dados

## Índice das lojas

- file_name: tid-2779033056155408584-f6316110-4c9a-4061-ae48-69b77c7c8c36-4
- Size: 14,419 rows, 5 columns
- Weight: 394.4+ KB

| Column Name   | Type          | Description                 | Range/Values                             | Observations    |
| ------------- | ------------- | --------------------------- | ---------------------------------------- | --------------- |
| #             | int           | Index                       | 0 - 14418                                |                 |
| PDV           | int           | Ponto De Venda              | 1000237487041964405 - 997907800111849739 | 100% distintos  |
| Premise       | string/Object | ?                           | On Premise, Off Premise                  | 57% on, 43% off |
| categoria_pdv | string/Object | Categoria do Ponto De Venda | [Lista de Valores]                       | 54 distintos    |
| zipcode       | int           | CEP? Falta Número?          | 8107 - 90920                             | 788 distintos   |

- [Lista de Valores]
  1. Adult Entertainment
  2. Airline/Airport
  3. All Other N/A Off Premise
  4. All Other N/A On Premise
  5. Asian
  6. Banquet/Caterer
  7. Bar
  8. Barbeque
  9. Billiard/Bowling
  10. Bodega
  11. Casino
  12. Church
  13. Club Store
  14. Coffee House
  15. Convenience
  16. Country/Western
  17. Drug
  18. French
  19. Gay Bar
  20. German
  21. Golf - Private
  22. Golf - Public
  23. Grocery
  24. Gym/Fitness
  25. Health Club
  26. Hotel/Motel
  27. Irish
  28. Italian
  29. Korean
  30. Marina / Lake
  31. Mass Merch
  32. Mexican Rest
  33. Military
  34. Music Venue
  35. Neighborhood Store
  36. Night Club
  37. Non-Traditional
  38. Other Off Premise
  39. Other On Premise
  40. Package/Liquor
  41. Pizza
  42. Race Track
  43. Restaurant
  44. Salon/Spa/Tann
  45. Sample Room
  46. Service Org
  47. Special Event
  48. Sports/Rec Club
  49. Stadium/Concession
  50. Sub Distributor
  51. Super Center
  52. Theatre
  53. Theme Park
  54. Winery

## Transações

file_name: tid-5196563791502273604-c90d3a24-52f2-4955-b4ec-fb143aae74d8-4
Size: 6,560,698 rows, 11 columns
Weight: 550.6+ MB

| Column Name         | Type          | Description                   | Range/Values                             | Observations                           |
| ------------------- | ------------- | ----------------------------- | ---------------------------------------- | -------------------------------------- |
| #                   | int           | Index                         | 0 - 6560697                              |                                        |
| internal_store_id   | int           | Identificador da loja         | 1000237487041964405 - 997907800111849739 | 15086 distintos (<1%)                  |
| internal_product_id | int           | Identificador do produto      | 1000423277513436210 - 999285078291803499 | 7092 distintos (<1%)                   |
| distributor_id      | int           | Identificador do distribuidor | 4 - 11                                   | 8 distintos; (4, 5, 6) = (43, 21, 12)% |
| transaction_date    | string/object | Data da transação             | 2022-01-01 - 2022-12-31                  | 365 distintos                          |
| reference_date      | string/object | Data de referência            | 2022-01-01 - 2022-12-01                  | 12 distintos (9, 8, 6) = (13, 9, 9)%   |
| quantity            | float64       | Quantidade                    | -1530.0 - 94230.0                        | 16449 distintos                        |
| gross_value         | float64       | Valor Bruto (?)               | -42672.8984375 - 604173.9177856445       | 173883 distintos                       |
| net_value           | float64       | Valor Líquido                 | -39848.00004577637 - 604173.9177856445   | 216337 distintos                       |
| gross_profit        | float64       | Lucro Bruto                   | -274396.0 - 274416.0                     | 363451 distintos                       |
| discount            | float64       | Desconto                      | -13096.7998046875 - 240082.96562814713   | 121528 distintos                       |
| taxes               | float64       | Taxas                         | -4099.40869140625 - 2073.237548828125    | 12531 distintos                        |

## ?

file_name: tid-6364321654468257203-dc13a5d6-36ae-48c6-a018-37d8cfe34cf6-263
Size: 7092 rows, 8 columns
Weight: 443.4+ KB

| Column Name  | Type          | Description   | Range/Values                                                                              | Observations                                                    |
| ------------ | ------------- | ------------- | ----------------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| #            | int           | Index         | 0 - 7091                                                                                  |                                                                 |
| produto      | int           | Id do Produto | 1000423277513436210 - 999285078291803499                                                  | 7092 distintos                                                  |
| categoria    | string/object |               | ABA Spirits - Wine                                                                        | 7 distintos (Distilled Spirits, Wine, Package) = (31, 26, 20)%  |
| descricao    | string/object |               | 10 BARREL ACTION VARIETY PACK 2/12/12 CN - ZENTOPIA-CBD WATERMELON SELTZER WATER 12/16 CN | 7092 distintos                                                  |
| tipos        | string/object |               | Allocated Spirits - Wine RTD                                                              | 22 distintos (Distilled Spirits, Package, Wine) = (26, 20, 19)% |
| label        | string/object |               | Allocated - Winter Seasonal                                                               | 14 distintos; 1473 faltantes                                    |
| subcategoria | string/object |               | Ale - White Wine                                                                          | 42 distintos; 32 faltantes                                      |
| marca        | string/object |               | 10 Barrel Action Variety Pack - Zentopia-CBD Watermelon Seltzer Water                     | 4221 distintos; 0 faltantes                                     |
| fabricante   | string/object |               | 10th Mountain Whiskey & Spirit Co - Zyms Beverage Group                                   | 343 distintos; 0 faltantes                                      |

- categoria - Unique values (7):

  1. ABA Spirits
  2. Distilled Spirits
  3. Draft
  4. Non-Alcohol
  5. Package
  6. Tobacco
  7. Wine

- tipos - Unique values (22):

  1. Allocated Spirits
  2. Cider Dft
  3. Cider Pkg
  4. Dairy
  5. Dist Spirits-RTD Domestic
  6. Distilled Spirits
  7. Distilled Spirits-Domest
  8. Distilled Spirits-RTD
  9. Draft
  10. Hispanic
  11. MB Wine < 14 %
  12. N/A Beer
  13. Non Alcohol
  14. Non Alcohol W&S
  15. Package
  16. Pkg 3.2
  17. Talking Rain
  18. Tobacco
  19. Wine < 14 %
  20. Wine < 14 % - Domestic
  21. Wine > 14 %
  22. Wine RTD

- label - Unique values (15):

  1. Allocated
  2. Clearing
  3. Close Out
  4. Core
  5. Discontinued
  6. Fall Seasonal
  7. In&Out
  8. Other
  9. Private Label
  10. Speciality
  11. Specialty
  12. Spring Seasonal
  13. Summer Seasonal
  14. Winter Seasonal

- subcategoria - Unique values (43):
  1. Ale
  2. Bourbon Whiskey
  3. Brandy / Cognac
  4. Canadian Whisky
  5. Dairy beverage
  6. Dessert Wine
  7. Energy
  8. Gin
  9. Gose
  10. Hard Cider
  11. IPA
  12. Irish Whiskey
  13. Juice & Tea
  14. Lager
  15. Lager / Pilsner
  16. Liqueurs & Cordials
  17. Mixers
  18. Non-Alcoholic
  19. Other ABA Spirits
  20. Other Draft
  21. Other Non-Alcoholic
  22. Other Package
  23. Other Spirits
  24. Other Wine
  25. Pale Ale
  26. Ready-to-Drink
  27. Red Wine
  28. Rosé Wine
  29. Rum
  30. Scotch Whisky
  31. Soda
  32. Sour
  33. Sour / Wild Ale
  34. Sparkling Wine
  35. Specialty
  36. Specialty Beer
  37. Stout & Porter
  38. Tequila / Mezcal
  39. Vodka
  40. Water
  41. Wheat Beer
  42. White Wine
