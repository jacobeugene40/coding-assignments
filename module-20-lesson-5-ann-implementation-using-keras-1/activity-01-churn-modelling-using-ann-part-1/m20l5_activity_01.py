# M20 Lesson 5 - Activity 1: Churn Modelling using ANN - Part 1 (data preprocessing)
# Adapted to run in VS Code: Colab upload removed; reads Churn_Modelling.csv from this folder.
# NOTE: the bundled Churn_Modelling.csv is a SAMPLE stand-in - replace with the lesson's file (same name).
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split

# 2. Import dataset
here = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(here, 'Churn_Modelling.csv'))
print(df.head())

df.info()
print(df.describe())
# Conclusion: shape (10000, 14), 11 numerical features, 3 categorical, 0 null values
print("Shape:", df.shape)
print("Null values:", df.isnull().sum().sum())

# 3.1 Label encoding
lb = LabelEncoder()
df['Geography'] = lb.fit_transform(df['Geography'])
df['Gender'] = lb.fit_transform(df['Gender'])
print(df)
df.info()

# 3.2 Feature selection - drop columns that don't help prediction
df = df.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1)
print(df.shape)

# 3.3 Train/test split
y = df.pop('Exited')
X = df
print(X.shape)
print(y.shape)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# 3.4 Feature scaling
# Fit the scaler on the training data only, then apply the SAME scaling to the test data
# (the lesson called fit_transform on the test set too, which leaks/changes the scaling).
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

print(X_train)
