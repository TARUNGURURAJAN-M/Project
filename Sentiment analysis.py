import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("cleaned_data.csv")

# Ensure 'overview' or a similar text column exists
if 'overview' not in df.columns:
    raise ValueError("Your cleaned_data.csv does not contain an 'overview' column for sentiment analysis.")

# Drop rows with missing overviews
df = df.dropna(subset=['overview'])

# Function to calculate sentiment polarity
def get_sentiment(text):
    try:
        return TextBlob(text).sentiment.polarity
    except:
        return 0

# Apply sentiment analysis
df['sentiment_score'] = df['overview'].astype(str).apply(get_sentiment)

# Classify sentiment
def classify(score):
    if score > 0.1:
        return "Positive"
    elif score < -0.1:
        return "Negative"
    else:
        return "Neutral"

df['sentiment_label'] = df['sentiment_score'].apply(classify)

# Save results
df.to_csv("cleaned_data_with_sentiment.csv", index=False)
print("✅ Sentiment analysis complete. File saved as 'cleaned_data_with_sentiment.csv'.")

# Optional: visualize sentiment distribution
df['sentiment_label'].value_counts().plot(kind='bar', color=['green', 'red', 'gray'])
plt.title("Sentiment Distribution from Overviews")
plt.xlabel("Sentiment")
plt.ylabel("Number of Movies")
plt.tight_layout()
plt.savefig("sentiment_distribution_from_cleaned_data.png")
plt.show()
