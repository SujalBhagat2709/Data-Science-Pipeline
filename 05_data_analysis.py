import pandas as pd

df = pd.read_csv("step3_transformed.csv")

print("Average performance by department:")
print(df.groupby("department")["performance"].mean())

print("\nCorrelation with performance:")
for col in ["age", "salary", "experience"]:
    print(col, ":", df[col].corr(df["performance"]))