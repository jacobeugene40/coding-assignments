# M16 Lesson 4 - Activity 2: Countplots (Titanic)
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

# Set Plot Style
sns.set_style('whitegrid')

# Countplot for feature 'Survived'
sns.countplot(x='Survived', data=data)
plt.show()

# Barchart for passengers of different gender who survived or not
sns.countplot(x='Gender', hue='Survived', data=data)
plt.show()

# Customize Plots
sns.countplot(x='Survived', data=data, palette='winter')
plt.show()

sns.countplot(x='Gender', hue='Survived', data=data, palette='winter')
plt.show()

# Countplot for Embarked
sns.countplot(x='Embarked', data=data)
plt.show()

# Rotate the value labels and modify their font size
sns.countplot(x='Embarked', data=data)
plt.xticks(rotation=30, fontsize=20)
plt.show()