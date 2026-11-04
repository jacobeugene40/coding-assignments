# M19 Lesson 1 - Activity 1: Identify the dataset for classification
# (the lesson's external matplotlib style file was removed - it needs internet)
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer

dataset = load_breast_cancer()

sns.set_style('dark')
plt.rcParams.update({"figure.figsize": (8, 6), "axes.titlepad": 22.0})

print('Target variables  : ', dataset['target_names'])

(unique, counts) = np.unique(dataset['target'], return_counts=True)

print('Unique values of the target variable', unique)
print('Counts of the target variable :', counts)
print('Two classes -> binary classification' if len(unique) == 2 else 'More than two classes -> multi-class classification')

sns.barplot(x=dataset['target_names'], y=counts)
plt.title('Target variable counts in dataset')
plt.show()
