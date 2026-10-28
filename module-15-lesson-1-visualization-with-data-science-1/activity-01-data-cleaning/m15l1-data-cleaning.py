# M15 Lesson 1 - Data Cleaning (country vaccinations)
# Adapted to run in VS Code: the Colab upload is replaced by reading the CSV
# from the same folder, and print()/plt.show() are added so results appear.

# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read data from CSV file (country_vaccinations.csv must be in this folder)
df = pd.read_csv("country_vaccinations.csv")

# Display first 10 rows
print(df.head(10))

# Check for any null values in each column
print(df.isnull().any())

# Visualize missing values using a heatmap (optimize by using a subset of data)
subset = df.iloc[:5200, :]
plt.figure(figsize=(12, 8))
sns.heatmap(subset.isnull(), cbar=False, cmap="viridis")
plt.show()

# Drop rows where all values are NaN
print(df.dropna(how="all"))

# Fill missing values using backward fill method
print(df.bfill())

# Interpolate missing values (numeric columns only)
print(df.select_dtypes(include='number').interpolate())

# Drop all rows with any NaN values
df_dropped = df.dropna()
print(df_dropped)