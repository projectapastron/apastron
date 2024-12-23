from text_processor import TextProcessor
from sentiment_analyzer import SentimentAnalyzer

class ArticleProcessor:
    def __init__(self):
        self.text_processor = TextProcessor()
        self.sentiment_analyzer = SentimentAnalyzer()

    def analyze_article(self, article):
        """Analyze the article by processing its text and determining sentiment."""
        tokens = self.text_processor.process(article)
        sentiment = self.sentiment_analyzer.analyze(article)
        return {
            'tokens': tokens,
            'sentiment': sentiment
        }
