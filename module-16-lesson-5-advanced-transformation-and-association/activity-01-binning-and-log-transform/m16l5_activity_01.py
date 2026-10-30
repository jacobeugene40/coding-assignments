# M16 Lesson 5 - Activity 1: Binning and Log Transform (Titanic)
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

# Minimum and Maximum Values of Age
minimum_age = data['Age'].min()
print('Minimum Age :', minimum_age)

maximum_age = data['Age'].max()
print('Maximum Age :', maximum_age)

# Creating binned age and giving it a label
bins = [0, 15, 30, 45, 60, 75]

data['binned_age'] = pd.cut(data['Age'], bins)

print(data[['binned_age', 'Age']].head())

age_labels = ['Young', 'Young - Adult', 'Middle Aged', 'Middle-Older Age', 'Senior']

# Bin the values of the 'Age' column and specify the labels
data['binned_age'] = pd.cut(data['Age'], bins, labels = age_labels)

# Barplot for binned age
data['binned_age'].value_counts().plot(kind='bar')

# Label the bar graph
plt.title('Dance Class Age Distribution')
plt.xlabel('Ages')
plt.ylabel('Count')
plt.show()

# Conclusion
# - Features Gender and Embarked have only 2 and 3 categories respectively
# - Other categorical features have too many categories to even collapse

# Check distribution and skewness of all the features
# (histplot with kde=True replaces the old, removed sns.distplot)
labels = ['PassengerId','Survived','Pclass','Age','SibSp','Parch','Fare']
for label in labels:
  print('Distribution of', label)
  sns.histplot(data[label], kde=True)
  plt.show()
  print('Skewness -', data[label].skew())

# Conclusion
# - Features - SibSp, Parch and Fare are skewed

# Log Transform Skewed Features
# (log of 0 gives -inf with a warning - that is expected for SibSp/Parch/Fare zeros)
data['log_SibSp'] = np.log(data['SibSp'])
data['log_Parch'] = np.log(data['Parch'])
data['log_Fare'] = np.log(data['Fare'])
print(data[['log_SibSp', 'log_Parch', 'log_Fare']].head())