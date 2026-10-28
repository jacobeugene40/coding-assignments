# M15 Lesson 6 - Capstone Project (Iris Data Set Analysis - actually the Heart dataset)
# Adapted to run in VS Code: the Colab upload is removed, the CSV is read from
# this folder, and print()/plt.show() are added so results appear.

# Load Basic Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

warnings.filterwarnings('ignore')

# Reading the csv file (heart.csv must be in this folder)
df = pd.read_csv("heart.csv")

# Display first few rows
print(df.head())

# Display dataset shape
print(df.shape)

# Display column names
print(df.columns)

# Display descriptive statistics
print(df.describe())

# Check for null values
print(df.isnull().sum())

# Display dataset information
print(df.info())

# Create histograms
df.hist(figsize=(12,12), layout=(5,3))
plt.show()

# Create box and whiskers plots
df.plot(kind='box', subplots=True, layout=(5,3), figsize=(12,12))
plt.show()

# Create barplot
sns.barplot(data=df, x='sex', y='chol', hue='target', palette='spring')
plt.show()

# Display value counts for sex column
print(df['sex'].value_counts())

# Display value counts for target column
print(df['target'].value_counts())

# Display value counts for thal column
print(df['thal'].value_counts())

# Create correlation heatmap
plt.figure(figsize=(20,10))
sns.heatmap(df.corr(), annot=True, cmap='terrain')
plt.show()

# Create countplot for sex vs target
sns.countplot(x='sex', data=df, palette='husl', hue='target')
plt.show()

# Create countplot for target
sns.countplot(x="target", palette="BuGn", data=df)
plt.show()

# Create countplot for ca vs target
sns.countplot(x="ca", hue="target", data=df)
plt.show()