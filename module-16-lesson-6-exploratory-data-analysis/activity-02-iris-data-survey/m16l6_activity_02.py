# M16 Lesson 6 - Activity 2: Iris Data Survey
# Adapted to run in VS Code: the Colab upload is removed, the CSV is read from
# this folder, and print()/plt.show() are added so results appear.

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import dataset ("Iris.csv" must be in this folder)
data = pd.read_csv('Iris.csv')
print(data.head(5))

# Check Null Values
print(data.isnull().sum())

# Statistical Information of Features
print(data.describe())

# Create Boxplot of all the numerical features and check if outliers are present
labels = ['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']

for label in labels:
    print('Distribution of', label)
    sns.boxplot(x=data[label])
    plt.show()

# Conclusion: SepalWidthCm has outliers

# Check Correlation Between All Numerical Features
numeric_data = data.select_dtypes(include=['number'])

plt.figure(figsize=(8, 6))
sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# Check if any feature is skewed or not
for label in labels:
    print('Distribution of', label)
    sns.histplot(data[label], kde=True)
    plt.show()

# Check Skewness of Each Feature
for label in labels:
    print('Skewness of', label)
    print(data[label].skew())