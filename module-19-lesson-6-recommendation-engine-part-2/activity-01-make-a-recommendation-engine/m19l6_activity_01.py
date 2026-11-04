# M19 Lesson 6 - Activity 1: Make a recommendation engine model (content-based)
# Adapted to run in VS Code: reads ratings.csv and movies.csv from this folder, and repeats the
# Part 1 preparation steps (the lesson relied on variables left over from the Part 1 notebook).
# NOTE: the bundled CSVs are SAMPLE stand-ins - replace with the lesson's real files (same names).
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

here = os.path.dirname(os.path.abspath(__file__))
movies_df = pd.read_csv(os.path.join(here, 'movies.csv'))

# --- Part 1 preparation: clean titles, one-hot encode genres ---
movies_df['year'] = movies_df.title.str.extract(r'(\(\d\d\d\d\))', expand=True)
movies_df['year'] = movies_df.year.str.extract(r'(\d\d\d\d)', expand=True)
movies_df['title'] = movies_df.title.str.replace(r'(\(\d\d\d\d\))', '', regex=True)
movies_df['title'] = movies_df['title'].apply(lambda x: x.strip())
movies_df['genres'] = movies_df.genres.str.split('|')

movies_copy = movies_df.copy()
for index, row in movies_df.iterrows():
    for genre in row['genres']:
        movies_copy.at[index, genre] = 1
movies_copy = movies_copy.fillna(0)

# Step 1 - enter your ratings
user_input = [
    {'title': 'Grand Slam', 'rating': 5.6},
    {'title': 'Zero', 'rating': 7},
    {'title': 'Jumanji', 'rating': 8.5},
    {'title': 'Toy Story', 'rating': 4.5},
]
movies_input = pd.DataFrame(user_input)
print(movies_input)

# Step 2 - merge with movie IDs
input_id = movies_df[movies_df['title'].isin(movies_input['title'].tolist())]
movies_input = pd.merge(input_id, movies_input)
movies_input = movies_input.drop(['genres', 'year'], axis=1)
print(movies_input)

# Step 3 - build taste profile
movies_user = movies_copy[movies_copy['movieId'].isin(movies_input['movieId'].tolist())]
movies_user = movies_user.reset_index(drop=True)
UserGenreTable = movies_user.drop(['movieId', 'title', 'genres', 'year'], axis=1)
UserProfile = UserGenreTable.transpose().dot(movies_input['rating'])
print(UserProfile)

# Step 4 - plot taste profile
plt.figure(figsize=(10, 5))
plt.bar(UserProfile.index, UserProfile.values, color='#FF6B6B')
plt.title('Your Taste Profile')
plt.xlabel('Genre')
plt.ylabel('Weight')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# Step 5 - score all movies
GenreTable = movies_copy.set_index(movies_copy['movieId'])
GenreTable = GenreTable.drop(['movieId', 'title', 'genres', 'year'], axis=1)
Recommendation_df = ((GenreTable * UserProfile).sum(axis=1)) / UserProfile.sum()
Recommendation_df = Recommendation_df.sort_values(ascending=False)
print(Recommendation_df.head())

# Step 6 - top recommendations
RecommendationTable = movies_df.loc[movies_df['movieId'].isin(Recommendation_df.head(20).keys())]
print(RecommendationTable)

# Step 7 - plot top picks
top10_scores = Recommendation_df.head(10)
top10_titles = movies_df.set_index('movieId').loc[top10_scores.index]['title']

plt.figure(figsize=(8, 6))
plt.barh(top10_titles[::-1], top10_scores.values[::-1], color='#51CF66')
plt.title('Top 10 Picks')
plt.xlabel('Match Score')
plt.tight_layout()
plt.show()
