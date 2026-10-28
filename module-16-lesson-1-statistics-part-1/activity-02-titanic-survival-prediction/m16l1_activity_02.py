# M16 Lesson 1 - Statistics Part 1 - Activity 2: Mean of Age and Fare
# Adapted to run in VS Code: the Colab upload is removed and the CSV is read
# from this folder; print() is added so results appear.

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import Dataset ("Titanic Dataset.csv" must be in this folder)
data = pd.read_csv('Titanic Dataset.csv')

print(data.head())

# Mean Value of Age and Fare

# Mean Value of age
mean_age = np.mean(data['Age'])
print("Mean Age of Passengers is - ",mean_age)

# Mean Value of Fare
mean_fare = np.mean(data['Fare'])
print("Mean Fare is - ",mean_fare)