# M20 Lesson 6 - Activity 1: Churn Modelling using ANN - Part 2 (build and evaluate the model)
# Adapted to run in VS Code: Colab upload removed; reads Churn_Modelling.csv from this folder.
# NOTE: the bundled Churn_Modelling.csv is a SAMPLE stand-in - replace with the lesson's file (same name).
# Needs: pip install tensorflow pandas scikit-learn --break-system-packages
# Training (100 epochs) can take a few minutes.
import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from keras.models import Sequential
from keras.layers import Dense, Input

# 2. Import dataset
here = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(here, 'Churn_Modelling.csv'))
print(df.head())
df.info()
print(df.describe())
print("Shape:", df.shape, "| Null values:", df.isnull().sum().sum())

# 3.1 Label encoding
lb = LabelEncoder()
df['Geography'] = lb.fit_transform(df['Geography'])
df['Gender'] = lb.fit_transform(df['Gender'])

# 3.2 Feature selection
df = df.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1)
print(df.shape)

# 3.3 Train/test split
y = df.pop('Exited')
X = df
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# 3.4 Feature scaling (fit on training data only, reuse it for the test data)
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# 4. Model building
classifier = Sequential()

# Input layer + first hidden layer (Input() replaces the old input_dim argument)
classifier.add(Input(shape=(10,)))
classifier.add(Dense(units=6, kernel_initializer='he_uniform', activation='relu'))

# Second hidden layer
classifier.add(Dense(units=6, kernel_initializer='he_uniform', activation='relu'))

# Output layer
classifier.add(Dense(units=1, kernel_initializer='glorot_uniform', activation='sigmoid'))

classifier.compile(optimizer='Adamax', loss='binary_crossentropy', metrics=['accuracy'])

model_history = classifier.fit(X_train, y_train, batch_size=10, epochs=100)

# total params = number of weights and biases
classifier.summary()

# 5. Model evaluation
Y_pred = classifier.predict(X_test)
print(Y_pred)

Y_pred = (Y_pred > 0.5)
print(Y_pred)

cm = confusion_matrix(y_test, Y_pred)
print(cm)

score = accuracy_score(Y_pred, y_test)
print(score)
