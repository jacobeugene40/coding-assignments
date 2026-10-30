# M16 Lesson 6 - Activity 1: Exploratory Data Analysis (Titanic)
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

# Passengers belonging to which gender survived the most
sns.countplot(data=data, x='Gender', hue='Survived')
plt.title("Survival by Gender")
plt.show()

# Passengers belonging to which PClass survived the most and the least
sns.countplot(data=data, x='Pclass', hue='Survived')
plt.title("Survival by Passenger Class")
plt.show()

# Highest number of passengers belong to which Age
sns.histplot(data['Age'], bins=40, kde=False)
plt.title("Distribution of Passenger Age")
plt.xlabel("Age")
plt.ylabel("Number of Passengers")
plt.show()

# Highest number of passengers belong to which Gender
sns.countplot(data=data, x='Gender')
plt.title("Passengers by Gender")
plt.show()

# Is SibSp correlated/associated with Survived feature?
sns.countplot(data=data, x='Survived', hue='SibSp', palette="mako")
plt.title("Survival by Number of Siblings/Spouses")
plt.show()

# Is Parch correlated/associated with Survived feature?
sns.countplot(data=data, x='Survived', hue='Parch', palette="mako")
plt.title("Survival by Number of Parents/Children")
plt.show()

# Is the Fare having normal distribution/spread of data?
sns.histplot(data['Fare'], kde=True)
plt.title("Distribution of Fare")
plt.xlabel("Fare")
plt.ylabel("Frequency")
plt.show()

# Check the age group of majority of people belonging to PClass = 1
sns.boxplot(data=data, x='Pclass', y='Age', hue='Pclass', palette='winter', legend=False)
plt.title("Age Distribution by Passenger Class")
plt.show()

# Check the correlation of numerical features with the target variable 'Survived'
numeric_data = data.select_dtypes(include=['number'])

plt.figure(figsize=(10, 7))
sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()