# M16 Lesson 3 - Activity 2: Boxplots (Titanic)
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

# Check Null Values
print(data.isnull().sum())

# Boxplot of Feature Age and Pclass
plt.boxplot(data['Age'])
plt.title('Age distribution')
plt.show()

plt.boxplot(data['Pclass'])
plt.title('Passenger Class distribution')
plt.show()