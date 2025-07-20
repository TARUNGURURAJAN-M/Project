import pandas as pd
import numpy as np
import ast

def parse_genres(genre_str):
    """Convert JSON-style genres column into comma-separated strings."""
    try:
        genres = ast.literal_eval(genre_str)
        return ", ".join([g["name"] for g in genres])
    except:
        return np.nan

def preprocess_movie_data(input_file="movies_metadata.csv", output_file="cleaned_data.csv"):
    print("🔄 Loading raw movie data...")
    df = pd.read_csv(input_file, low_memory=False)

    # Keep only numeric and meaningful budget and revenue values
    df = df[pd.to_numeric(df['budget'], errors='coerce').notnull()]
    df = df[pd.to_numeric(df['revenue'], errors='coerce').notnull()]
    df['budget'] = df['budget'].astype(float)
    df['revenue'] = df['revenue'].astype(float)
    df = df[(df['budget'] > 0) & (df['revenue'] > 0)]

    # Convert and extract year from release_date
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce')
    df = df.dropna(subset=['release_date'])
    df['release_year'] = df['release_date'].dt.year

    # Parse genres
    df['genres'] = df['genres'].apply(parse_genres)

    # Label success if revenue > budget
    df['success'] = np.where(df['revenue'] > df['budget'], 1, 0)

    # Select required columns
    selected_columns = ['title', 'release_year', 'budget', 'revenue', 'runtime',
                        'vote_average', 'vote_count', 'popularity', 'genres', 'overview', 'success']
    df_cleaned = df[selected_columns].dropna()

    # Save the cleaned data
    df_cleaned.to_csv(output_file, index=False)
    print(f"✅ Cleaned data saved to '{output_file}' with {df_cleaned.shape[0]} rows.")

if __name__ == "__main__":
    preprocess_movie_data()
