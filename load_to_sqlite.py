import pandas as pd
import sqlite3

# Load cleaned CSV
df = pd.read_csv("cleaned_data.csv")

# Connect to SQLite database (will create if not exists)
conn = sqlite3.connect("movies.db")
cursor = conn.cursor()

# Optional: Drop table if it exists
cursor.execute("DROP TABLE IF EXISTS movies")

# Load data into SQLite
df.to_sql("movies", conn, index=False)

# Verify
print("✅ Data loaded successfully into 'movies' table in movies.db")
print(f"Rows inserted: {len(df)}")

# Close connection
conn.close()
