import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("step3_transformed.csv")

df.groupby("department")["salary"].mean().plot(kind="bar")
plt.title("Average Salary by Department")
plt.ylabel("Salary")
plt.show()

df.describe().to_csv("summary_report.csv")
print("Report saved as summary_report.csv")