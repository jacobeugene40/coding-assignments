# M20 Lesson 4 - Activity 1: House Price Prediction using Keras
# Adapted to run in VS Code: Colab upload removed; reads housing_data.csv from this folder.
# NOTE: the bundled housing_data.csv is a SAMPLE stand-in - replace with the lesson's file (same name).
# Needs: pip install tensorflow pandas scikit-learn --break-system-packages
import os
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Input
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

here = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(here, "housing_data.csv"))
print(df.head())

# split into input (X) and output (Y) variables
y = df.pop('AboveMedianPrice')
x = df

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# create model (Input layer replaces the old input_dim argument)
model = Sequential()
model.add(Input(shape=(10,)))
model.add(Dense(10, kernel_initializer='random_normal', activation='relu'))
model.add(Dense(6, kernel_initializer='random_normal', activation='relu'))
model.add(Dense(1, kernel_initializer='random_normal'))

model.compile(loss='mean_squared_error', optimizer='adam')

# Fit the ANN to the training set
model_history = model.fit(X_train, y_train, batch_size=10, epochs=100)

# total params = number of weights and biases
model.summary()

# Predict the test set results
Y_pred = model.predict(X_test)
print(Y_pred)

# Model performance
mae = mean_absolute_error(y_test, Y_pred)
print("Mean absolute error:", mae)
print("Model Accuracy = 1 -", round(mae, 2), "=", round(1 - mae, 2))
