import numpy as np

class Client:
    def __init__(self, n_client, category_dict):
        self.category_dict = category_dict
        self.n_client = n_client
        self.n_category = len(category_dict.keys())
        self.n_commodity = count(category_dict)
        self.preference_matrix = np.zeros((n_client, self.n_commodity))
        
    def generate_client_distribution():
        return np.random.uniform(0, 0.8, (n_client, self.n_category))