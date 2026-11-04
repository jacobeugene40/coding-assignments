# M18 Lesson 2 - Activity 1: Data preprocessing (Titanic)
# Adapted to run in VS Code: Colab upload removed; reads the tab-separated file from this folder.
# NOTE: titanic_tab_separated.csv is a SAMPLE stand-in - replace with the lesson's file and
# change FILENAME below to its name.
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

FILENAME = 'titanic_tab_separated.csv'
here = os.path.dirname(os.path.abspath(__file__))

# The Titanic file is tab-separated, so sep="\t"
Titanic = pd.read_csv(os.path.join(here, FILENAME), sep="\t")

print(Titanic.head())
print(Titanic.columns)
print(Titanic.shape)
print(Titanic.isnull().sum())

plt.figure(figsize=(10, 6))
sns.heatmap(Titanic.isnull(), cmap="spring")
plt.show()

# Cabin has too many missing values
Titanic.drop("Cabin", axis=1, inplace=True)
print(Titanic.head())

# Remove remaining rows with missing values
Titanic.dropna(inplace=True)
print(Titanic.isnull().sum())

plt.figure(figsize=(10, 6))
sns.heatmap(Titanic.isnull(), cbar=False)
plt.show()

# Dummy variables
print(pd.get_dummies(Titanic["Sex"]).head())
sex = pd.get_dummies(Titanic["Sex"], drop_first=True)
print(sex.head(4))

print(pd.get_dummies(Titanic["Embarked"]).head(4))
embarked = pd.get_dummies(Titanic["Embarked"], drop_first=True)
print(embarked.head(4))

pclass = pd.get_dummies(Titanic["Pclass"], drop_first=True)
print(pclass.head(4))

Titanic = pd.concat([Titanic, sex, embarked, pclass], axis=1)
print(Titanic.head())
