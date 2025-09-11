""" Importing libraries """

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Our modules

from Modules.read_parquet import read_parquet_file
""" Setting up the constants """

DATA_PATH = "B:/GitHub/Random/hackaton-big_data_tech/Files/Data/hackathon_2025_templates/"

FILE_NAMES = [
    "part-00000-tid-2779033056155408584-f6316110-4c9a-4061-ae48-69b77c7c8c36-4-1-c000.snappy.parquet",
    "part-00000-tid-5196563791502273604-c90d3a24-52f2-4955-b4ec-fb143aae74d8-4-1-c000.snappy.parquet",
    "part-00000-tid-6364321654468257203-dc13a5d6-36ae-48c6-a018-37d8cfe34cf6-263-1-c000.snappy.parquet",
]
""" Loading the data """

# for file in FILE_NAMES:

file_path = DATA_PATH + FILE_NAMES[2]
print(file_path)
print("\nreading\n")
first_data = pd.read_parquet(file_path)
print("\nread\n")
# df = read_parquet_file(file_path)
# print(f"Data from {file}:")
# display(df.head())
# print("\n\n")

print(first_data.shape)
first_data.info()

# Showing all the categoria_pdv distinct values

# List all columns
cols = first_data.columns.tolist()

for col in cols:
    print(col)
    uniques = first_data[col].nunique()
    col_type = first_data[col].dtype
    min = first_data[col].min()
    max = first_data[col].max()
    print(f"|{col}|{col_type}||{min} - {max}| {uniques} distintos|")