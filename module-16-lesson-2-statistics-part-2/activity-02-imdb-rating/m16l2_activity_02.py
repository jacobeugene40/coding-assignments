# M16 Lesson 2 - Statistics Part 2 - Activity 2: IMDB Rating
# Adapted to run in VS Code: the Colab upload is removed, the CSV is read from
# this folder, and plt.show() is added so each histogram opens in a window.

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Import dataset ("IMDB Dataset.csv" must be in this folder)
data = pd.read_csv('IMDB Dataset.csv')

print(data.head(5))

# Check Null Values
print(data.isnull().sum())

# Plot Histogram for feature Runtime
plt.hist(data['Runtime'])
plt.ylabel("Count of movies")
plt.xlabel("Runtime")
plt.show()

# Plot Histogram for feature IMDB_Rating
plt.hist(data['IMDB_Rating'])
plt.ylabel("Count of movies")
plt.xlabel("IMDB Rating")
plt.show()

# Define parameter bins_time for feature Runtime and plot histogram for it
print(data['Runtime'].unique())

bins_time = np.arange(80, 230, 10)
plt.hist(data['Runtime'], edgecolor="black", bins=bins_time, color='g')
plt.ylabel("Count of movies")
plt.xlabel("Runtime")
plt.show()

# Define parameter bins_rating for feature IMDB_Rating and plot histogram for it
print(data['IMDB_Rating'].unique())

bins_rating = np.arange(8, 10, 0.20)
plt.hist(data['IMDB_Rating'], edgecolor="black", bins=bins_rating, color='g')
plt.ylabel("Count of movies")
plt.xlabel("IMDB Rating")
plt.xticks(bins_rating)
plt.show()