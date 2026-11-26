
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("-"*30)
print("      Flights over the years")
print("-"*30)

print("Available dataset")
print(sns.get_dataset_names())

df = sns.load_dataset('flights')

print("First 5 rows:\n", df.head())
print("Missing Values:\n", df.isnull().sum())
print("Statistical Summary:\n", df.describe())

print("Average passengers:", df["passengers"].mean())
print("Highest:\n", df.loc[df["passengers"].idxmax(),["year", "month", "passengers"]])
print("Lowest:\n", df.loc[df["passengers"].idxmin(), ["year", "month", "passengers"]])
print("Correlation:\n", df.corr(numeric_only=True))

sns.relplot(data=df, x="year", y="passengers", hue="month", kind="scatter")
plt.title("Passengers Over the Years")
plt.show()

sns.scatterplot(data=df,x="year", y="passengers", hue="month", size="passengers", sizes=(20, 200))
plt.title("Passenger Distribution Over the Years")
plt.show()
