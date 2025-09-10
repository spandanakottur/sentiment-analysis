import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
# Download VADER lexicon
nltk.download('vader_lexicon')
# Initialize VADER sentiment analyzer
sid = SentimentIntensityAnalyzer()
# Sample text for sentiment analysis
inp_1 = "I had a weird day, I got my amazon Delivery today. I had a late lunch"
inp_2 = "I had a weird day! I got my amazon Delivery today! I had a late lunch"
# Perform sentiment analysis
sentiment_score_1 = sid.polarity_scores(inp_1)
sentiment_score_2 = sid.polarity_scores(inp_2)
# Print sentiment score
print(sentiment_score_1)
print(sentiment_score_2)