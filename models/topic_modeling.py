from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer

class TopicModeling:
    def __init__(self, n_topics=5):
        self.n_topics = n_topics
        self.vectorizer = CountVectorizer(stop_words='english')
        self.lda = LatentDirichletAllocation(n_components=n_topics)

    def fit(self, documents):
        """Fit the LDA model on the given documents."""
        X = self.vectorizer.fit_transform(documents)
        self.lda.fit(X)

    def transform(self, document):
        """Get the topics of a given document."""
        X = self.vectorizer.transform([document])
        return self.lda.transform(X)
