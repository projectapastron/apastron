from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

class CryptoSentimentModel:
    def __init__(self):
        self.vectorizer = CountVectorizer(stop_words='english')
        self.model = MultinomialNB()

    def train(self, X, y):
        """Train the sentiment model."""
        X_transformed = self.vectorizer.fit_transform(X)
        self.model.fit(X_transformed, y)

    def predict(self, text):
        """Predict sentiment for the given text."""
        X_transformed = self.vectorizer.transform([text])
        prediction = self.model.predict(X_transformed)
        return prediction[0]

    def save(self, model_path, vectorizer_path):
        """Save the trained model and vectorizer."""
        joblib.dump(self.model, model_path)
        joblib.dump(self.vectorizer, vectorizer_path)

    def load(self, model_path, vectorizer_path):
        """Load the trained model and vectorizer."""
        self.model = joblib.load(model_path)
        self.vectorizer = joblib.load(vectorizer_path)
