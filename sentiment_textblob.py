from textblob import TextBlob
# Sample text for sentiment analysis
inp_1 = "I had a weird day, I got my amazon Delivery today. I had a late lunch"
inp_2 = "I had a weird day! I got my amazon Delivery today! I had a late lunch"
# Create a TextBlob object
blob_1 = TextBlob(inp_1)
blob_2 = TextBlob(inp_2)
# Perform sentiment analysis
sentiment_1 = blob_1.sentiment
sentiment_2 = blob_2.sentiment
# Print sentiment
print(sentiment_1)
print(sentiment_2)