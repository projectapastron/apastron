import pandas as pd

class DataLoader:
    def __init__(self, data_path):
        self.data_path = data_path

    def load_data(self):
        """Load data from the specified CSV file."""
        return pd.read_csv(self.data_path)

    def get_features_labels(self):
        """Split data into features and labels."""
        data = self.load_data()
        X = data['text']
        y = data['label']
        return X, y
