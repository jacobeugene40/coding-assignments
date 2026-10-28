# M15 Lesson 5 - House Rent Prediction (USA Housing)
# Adapted to run in VS Code: the Colab upload and %matplotlib inline are removed,
# the CSV is read from this folder, print()/plt.show() are added, and the
# missing numeric_df variable (used by the heatmap) is defined.

# Import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset (USA_Housing.csv must be in this folder)
HouseDF = pd.read_csv("USA_Housing.csv")

# Display first few rows
print(HouseDF.head())

# Dataset information
HouseDF.info()

# Statistical summary
print(HouseDF.describe())

# Column names
print(HouseDF.columns)

# Pairplot for numerical features
sns.pairplot(HouseDF)
plt.show()

# Correlation heatmap (numeric columns only - Address is text)
numeric_df = HouseDF.select_dtypes(include='number')

plt.figure(figsize=(8,6))

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap='coolwarm',
    linewidths=0.5
)

plt.title("Correlation Heatmap")
plt.show()