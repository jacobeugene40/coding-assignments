# M16 Lesson 4 - Activity 1: Categorical Variables (Titanic)
# Adapted to run in VS Code: the Colab upload is removed, the CSV is read from
# this folder, and print()/plt.show() are added so results appear.

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import dataset ("Titanic Dataset.csv" must be in this folder)
data = pd.read_csv('Titanic Dataset.csv')
print(data.head(5))

# Check datatypes
print(data.dtypes)

# Nominal and Ordinal Categorical Features -

# Nominal Categorical Variables
nominal_cat = ['Name','Ticket','Cabin']

# Ordinal Categorical Variables
ordinal_cat = ['Embarked','Gender']

# Median value of feature Gender and Embarked
print(data['Gender'].value_counts())

gender_categories = ['Female','Male']

data['Gender'] = pd.Categorical(data['Gender'], gender_categories, ordered=True)

median_index = np.median(data['Gender'].cat.codes)
median_gender = gender_categories[int(median_index)]
print(median_gender)

print(data['Embarked'].value_counts())

embarked_categories = ['S','C','Q']

data['Embarked'] = pd.Categorical(data['Embarked'], embarked_categories, ordered=True)

median_index = np.median(data['Embarked'].cat.codes)
median_embarked = embarked_categories[int(median_index)]
print(median_embarked)