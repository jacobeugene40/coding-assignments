# M16 Lesson 1 - Statistics Part 1 - Activity 3: Median and Mode
# Adapted to run in VS Code: the Colab upload is removed and the CSV is read
# from this folder; print() is added so results appear. Missing ages are
# skipped with dropna() so the median and mode are real numbers, not NaN.

# Import Libraries
import pandas as pd
import numpy as np
import statistics as stats
import matplotlib.pyplot as plt
import seaborn as sns

# Import Dataset ("Titanic Dataset.csv" must be in this folder)
data = pd.read_csv('Titanic Dataset.csv')

print(data.head())

# Median Value of Age and Fare

median_age = np.median(data['Age'].dropna())
print("Median value of Age -", median_age)

median_fare = np.median(data['Fare'])
print("Median value of Fare -", median_fare)

# Mode Value of Age and PClass

mode_age = stats.mode(data['Age'].dropna())
print("Mode value of Age -", mode_age)

mode_class = stats.mode(data['Pclass'])
print("Mode value of PClass -", mode_class)

# Mode Value of Categorical Feature - Gender

mode_gender = data['Gender'].value_counts().index[0]
print("Mode of Feature Gender -", mode_gender)