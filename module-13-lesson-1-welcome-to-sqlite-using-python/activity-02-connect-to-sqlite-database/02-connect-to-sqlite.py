# Connect to a SQLite database and print all the tables inside it.
# (Adapted to run in VS Code: the Colab file-upload step is not needed,
#  because database.sqlite just sits in the same folder as this script.)

# 1. Connect with SQLite Database
import sqlite3

database = 'database.sqlite'

conn = sqlite3.connect(database)
print('Opened data successfully')

# Read SQL query for getting all the tables of the database into a dataframe
# Here SELECT * means select all
import pandas as pd
tables = pd.read_sql("""SELECT *
                    FROM sqlite_master
                    WHERE type='table';""", conn)
print(tables)