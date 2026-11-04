# M19 Lesson 5 - Activity 1: Recommendation Engine, Part 1 (prepare the movie data)
# Adapted to run in VS Code: Colab uploads removed; reads ratings.csv and movies.csv from this folder.
# NOTE: the bundled CSVs are SAMPLE stand-ins - replace with the lesson's real files (same names).
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

here = os.path.dirname(os.path.abspath(__file__))

# Step 2 - ratings
ratings_df = pd.read_csv(os.path.join(here, 'ratings.csv'))
print(ratings_df.head())

# Step 3 - movies
movies_df = pd.read_csv(os.path.join(here, 'movies.csv'))
print(movies_df.head())

# Step 4 - clean titles: pull the year out of "Title (1995)"
movies_df['year'] = movies_df.title.str.extract(r'(\(\d\d\d\d\))', expand=True)
movies_df['year'] = movies_df.year.str.extract(r'(\d\d\d\d)', expand=True)
movies_df['title'] = movies_df.title.str.replace(r'(\(\d\d\d\d\))', '', regex=True)
movies_df['title'] = movies_df['title'].apply(lambda x: x.strip())
print(movies_df.head())

# Step 5 - one-hot encode genres
movies_df['genres'] = movies_df.genres.str.split('|')

movies_copy = movies_df.copy()
for index, row in movies_df.iterrows():
    for genre in row['genres']:
        movies_copy.at[index, genre] = 1
movies_copy = movies_copy.fillna(0)
print(movies_copy.head())

# Step 6 - drop the timestamp column
ratings_df = ratings_df.drop('timestamp', axis=1)
print(ratings_df.head())

# Step 7 - genre-count chart
genre_counts = movies_copy.drop(['movieId', 'title', 'genres', 'year'], axis=1).sum().sort_values(ascending=False)
print(genre_counts)

plt.figure(figsize=(10, 5))
plt.bar(genre_counts.index, genre_counts.values, color='#4DABF7')
plt.title('Number of Movies per Genre')
plt.xlabel('Genre')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
