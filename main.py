import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("="*50)
print("         LIFE EXPECTANCY ANALYZER")
print("="*50)

df=pd.read_csv("life.csv")
df.columns=df.columns.str.strip()
print("first 5 rows", df.head())
print("Missing Values", df.isnull().sum())
print("Statistical Summary", df.describe())
print("Average life expectancy", df["life_exp"].mean())
print("Highest", df.loc[df["life_exp"].idxmax(),["country", "life_exp"]])
print("Lowest", df.loc[df["life_exp"].idxmin(),["country", "life_exp"]])

print("Correlation", df.corr(numeric_only=True))
sns.relplot(data=df, x="gdp_cap", y="life_exp", hue="continent")
plt.title("GDP vs Life Expectancy Distribution")
plt.show()

sns.scatterplot(data=df, x="gdp_cap", y="life_exp", size="population", hue="continent", sizes=(20,500))
plt.title("GDP vs Life Expectancy Distribution")
plt.show()