import requests

class ArticleFetcher:
    def __init__(self, api_key, source='cryptocurrency'):
        self.api_key = api_key
        self.base_url = "https://newsapi.org/v2/everything"
        self.source = source

    def fetch_articles(self, query="crypto"):
        """Fetch the latest articles related to crypto."""
        params = {
            'q': query,
            'apiKey': self.api_key,
            'language': 'en',
            'sortBy': 'publishedAt',
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()['articles']
        else:
            return []

    def fetch_article_by_url(self, url):
        """Fetch a specific article by URL (for analysis)."""
        response = requests.get(url)
        return response.text if response.status_code == 200 else None
