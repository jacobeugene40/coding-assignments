# M19 Lesson 3 - Activity 1: Apply the binary class algorithm to the dataset
# Adapted to run in VS Code: Colab upload removed; reads insurance_data.csv from this folder.
# NOTE: the bundled insurance_data.csv is a SAMPLE - replace with the lesson's file (same name) if you have it.
import os
import math
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

here = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(here, "insurance_data.csv"))
print(df.head())

plt.scatter(df.age, df.bought_insurance, marker='+', color='red')
plt.xlabel('age')
plt.ylabel('bought_insurance')
plt.show()

X_train, X_test, y_train, y_test = train_test_split(df[['age']], df.bought_insurance, train_size=0.8)
print("X_test:\n", X_test)

model = LogisticRegression()
model.fit(X_train, y_train)

y_predicted = model.predict(X_test)
print("Probabilities:\n", model.predict_proba(X_test))
print("Accuracy:", model.score(X_test, y_test))
print("Predicted:", y_predicted)
print("coef:", model.coef_)
print("intercept:", model.intercept_)

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

# Uses the coefficients learned above (the lesson hard-coded 0.042 and -1.53,
# which only match its own data/split)
def prediction_function(age):
    z = model.coef_[0][0] * age + model.intercept_[0]
    return sigmoid(z)

for age in (35, 43):
    p = prediction_function(age)
    print(f"Age {age}: probability of buying insurance = {p:.3f} ->",
          "will buy" if p > 0.5 else "will not buy")
