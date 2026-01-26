import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("step3_transformed.csv")

print("Statistical summary:")
print(df.describe())

plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

df["performance"].hist(bins=6)
plt.title("Performance Distribution")
plt.show()