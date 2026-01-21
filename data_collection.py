import pandas as pd

df = pd.read_csv("data.csv")

print("Data collected successfully")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\nSample data:")
print(df.head())

df.to_csv("step1_raw.csv", index=False)