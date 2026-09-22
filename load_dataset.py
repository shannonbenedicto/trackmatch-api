import kagglehub
import pandas as pd
import sqlite3

# Manual CSV finding - chose over using the KAGGLEADAPTER wrapper for understanding
# Download file and find local path
path = kagglehub.dataset_download("maharshipandya/-spotify-tracks-dataset")

# Find the CSV inside the folder and load it
df = pd.read_csv(f'{path}/dataset.csv')

# Push to SQLite database
con = sqlite3.connect('trackmatch.db')
df.to_sql('tracks', con, if_exists='replace', index=False)

# Test querying works as expected
cur = con.cursor()
for row in cur.execute('SELECT * FROM tracks LIMIT 3;'):
    print(row)

con.close()