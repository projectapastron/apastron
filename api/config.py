import os

class Config:
    """Configuration class for the application."""
    API_HOST = '0.0.0.0'
    API_PORT = 5000
    ARTICLE_API_URL = os.getenv('ARTICLE_API_URL', 'https://api.example.com/get_article')
