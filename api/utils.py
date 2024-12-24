import requests

def fetch_article(url):
    """Fetch an article from a URL."""
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None
