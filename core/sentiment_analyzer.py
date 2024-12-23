from textblob import TextBlob

class SentimentAnalyzer:
    def analyze(self, text):
        """Analyze the sentiment of the input text."""
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        return sentiment
