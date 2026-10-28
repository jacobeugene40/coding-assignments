# M16 Lesson 1 - Statistics Part 1 - Activity 1: Titanic Survival Prediction
# Adapted to run in VS Code: the Colab upload is removed and the CSV is read
# from this folder; print() is added so results appear.

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import dataset ("Titanic Dataset.csv" must be in this folder)
data = pd.read_csv('Titanic Dataset.csv')
print(data.head(5))

# Check the datatype
print(data.dtypes)

# Check Null Values
print(data.isnull().sum())