import requests

class DataStrategy:
    def __init__(self, sources=None):
        self.sources = sources if sources else [
            "https://newsapi.org",
            "https://cryptopanic.com",
            "https://cointelegraph.com"
        ]

    def fetch_articles(self, query="crypto", limit=10):
        """Simulate fetching articles from different sources."""
        articles = []
        for source in self.sources:
            articles.append({
                "source": source,
                "query": query,
                "limit": limit,
                "status": "fetched"
            })
        return articles

    def filter_articles(self, articles, min_word_count=300):
        """Filter articles by minimum word count."""
        return [article for article in articles if len(article.get('content', '')) > min_word_count]

    def log_sources(self):
        """Log the sources used for article collection."""
        return f"Data collected from: {', '.join(self.sources)}"
    
if __name__ == "__main__":
    collector = DataStrategy()
    articles = collector.fetch_articles("bitcoin")
    print(collector.log_sources())
    print(f"Fetched {len(articles)} articles.")