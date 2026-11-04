# M19 Lesson 2 - Activity 2: Logistic Regression analysis (create a model and predict)
from sklearn.datasets import make_classification
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Random data each run (as in the lesson); add random_state=... to make it repeatable
x, y = make_classification(
    n_samples=100, n_features=1, n_classes=2, n_clusters_per_class=1,
    flip_y=0.03, n_informative=1, n_redundant=0, n_repeated=0,
)

plt.scatter(x, y, c=y, cmap='rainbow')
plt.title('Scatter Plot of Logistic Regression')
plt.show()

x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1)

log_reg = LogisticRegression()
log_reg.fit(x_train, y_train)

print(log_reg.coef_)
print(log_reg.intercept_)

y_pred = log_reg.predict(x_test)
print(y_pred)
