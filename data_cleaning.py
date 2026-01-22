import pandas as pd
import numpy as np

df = pd.read_csv("step1_raw.csv")

before = df.shape[0]
df = df.drop_duplicates()
print("Duplicates removed:", before - df.shape[0])

for col in df.select_dtypes(include=np.number):
    if df[col].isnull().sum() > 0:
        df[col] = df[col].fillna(df[col].median())

for col in df.select_dtypes(include="object"):
    df[col] = df[col].fillna("unknown")

print("\nMissing values after cleaning:")
print(df.isnull().sum())

df.to_csv("step2_clean.csv", index=False)