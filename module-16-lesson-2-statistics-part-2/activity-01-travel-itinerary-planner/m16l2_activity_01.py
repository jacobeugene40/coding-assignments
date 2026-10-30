# M16 Lesson 2 - Statistics Part 2 - Activity 1: Travel Itinerary Planner
# Adapted to run in VS Code: the Colab upload is removed and the CSV is read
# from this folder; print() is added so results appear.

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import dataset ("Weather Dataset.csv" must be in this folder)
data = pd.read_csv('Weather Dataset.csv')

print(data.head(5))

data.info()

# Check Null Values
print(data.isnull().sum())

# Mean, Variance and Standard Deviation of Temperature (C)

mean_temp = np.mean(data['Temperature (C)'])
print("Mean Temperature is :", mean_temp)

var_temp = np.var(data['Temperature (C)'])
print("Variation of Temperature is :", var_temp)

standard_deviation_temp = np.std(data['Temperature (C)'])
print("Standard Deviation of Temperature is :", standard_deviation_temp)

# Mean and Standard Deviation of Temperature (C) for every month

for i in range(1, 13):
  month = data.loc[data["month"] == i]["Temperature (C)"]
  print("For month "+str(i))
  print("Mean temperature is "+ str(np.mean(month)))
  print("Standard deviation is "+ str(np.std(month))+"\n")