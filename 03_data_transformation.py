import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("step2_clean.csv")

numeric_cols = ["age", "salary", "experience"]

scaler = StandardScaler()
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

print("Data scaled")

df.to_csv("step3_transformed.csv", index=False)