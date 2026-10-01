import numpy as np
import pandas as pd

df = pd.read_csv(r"D:\AI\titanic_dataset.csv")
print(df.describe)
print(df.isna().sum())
# print(df.nunique())
# print(df[' '].unique())
df = df['Cabin'].drop()
df.isna().sum()
