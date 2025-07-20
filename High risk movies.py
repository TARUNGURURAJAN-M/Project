import pandas as pd

# Load the cleaned data
df = pd.read_csv("cleaned_data.csv")

# Filter for unsuccessful movies
unsuccessful = df[df['success'] == 0]

# Calculate 75th percentile of budget
high_budget_threshold = unsuccessful['budget'].quantile(0.75)

# Filter high-budget unsuccessful movies
high_risk = unsuccessful[unsuccessful['budget'] >= high_budget_threshold]

# Calculate financial loss
high_risk['loss'] = high_risk['budget'] - high_risk['revenue']

# Sort by most loss
high_risk_sorted = high_risk.sort_values(by='loss', ascending=False)

# Select top columns
output = high_risk_sorted[['title', 'release_year', 'budget', 'revenue', 'loss', 'genres']]

# Save to CSV
output.to_csv("high_risk_movies.csv", index=False)

print("✅ high_risk_movies.csv created:", output.shape[0], "movies")
