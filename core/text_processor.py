import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

class TextProcessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))

    def clean_text(self, text):
        """Cleans input text by removing unwanted characters."""
        text = re.sub(r'\s+', ' ', text)  # Remove excessive spaces
        text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Remove non-alphanumeric characters
        return text.lower()

    def tokenize_text(self, text):
        """Tokenizes the text and removes stop words."""
        words = word_tokenize(text)
        return [word for word in words if word not in self.stop_words]

    def process(self, text):
        """Process text by cleaning and tokenizing."""
        cleaned_text = self.clean_text(text)
        tokens = self.tokenize_text(cleaned_text)
        return tokens
