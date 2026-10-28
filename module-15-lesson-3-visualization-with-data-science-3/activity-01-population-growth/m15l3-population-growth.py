# M15 Lesson 3 - Population Growth (top 10 countries, 1952 to 2007)
# Adapted to run in VS Code: the Colab upload is replaced by reading
# population.csv from the same folder, and the country names for the bar
# labels are taken from the data itself.

import pandas as pd
import matplotlib.pyplot as plt

# Read the file (population.csv must be in this folder)
countries_df = pd.read_csv("population.csv")

countries = countries_df

print(countries.head(3))

# Extract the rows where the year is 1952
c_52 = countries.loc[countries['year'] == 1952]
print(c_52.head())

# Extract the rows where the year is 2007
c_07 = countries.loc[countries['year'] == 2007]
print(c_07.head())

# Merge the 1952 and 2007 dataframes together
c_merge = c_52.merge(c_07, left_on='country', right_on='country')
print(c_merge.head())

# Drop both year columns
c_merge = c_merge.drop(['year_x', 'year_y'], axis=1)
print(c_merge.head())

# Create a new column for population growth
c_merge['population_growth'] = (
    c_merge['population_y'] - c_merge['population_x']
)
print(c_merge.head())

# Sort values and get the 10 countries with the biggest population growth
c_merge = c_merge.sort_values(
    'population_growth',
    ascending=False
).head(10)

# Reset the index
c_merge = c_merge.reset_index()

# Drop the index column
c_merge = c_merge.drop(['index'], axis=1)

# Top 10 countries with the highest population growth
print(c_merge)

# Plot the data
names = list(c_merge['country'])

pop_grow = c_merge['population_growth'] / 10**6

plt.figure(figsize=(15, 9))

plt.bar(names, pop_grow, width=0.6)

plt.xlabel('Country')
plt.ylabel('Population Growth (Millions)')
plt.title(
    'Top 10 Countries w/the Biggest Population Growth from 1952 to 2007'
)

plt.xticks(rotation=45)

# Add values above each bar
for x, y in zip(names, pop_grow):
    label = "{:.2f}".format(y)

    plt.annotate(
        label,
        (x, y),
        textcoords="offset points",
        xytext=(0, 10),
        ha='center'
    )

plt.show()