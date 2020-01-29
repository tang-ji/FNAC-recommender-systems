import numpy as np

def count(y):
    return sum([len(y.get(x, 0)) for x in y])

class Clients:
    def __init__(self, n_client, category_dict, desire_threshold=5):
        self.category_dict = category_dict
        self.category_list = list(category_dict.keys())
        self.n_client = n_client
        self.n_category = len(category_dict.keys())
        self.n_commodity = count(category_dict)
        self.desire_threshold_list = [desire_threshold] * n_client
        self.preference_matrix = np.zeros((n_client, self.n_commodity))
        self.desire_matrix = np.zeros((n_client, self.n_commodity))
        
        self.generate_client_distribution()
        
    def generate_client_distribution(self):
        proba_category = np.random.uniform(0, 0.9, (self.n_client, self.n_category))
        proba_commodity_list = []
        for j in range(proba_category.shape[1]):
            #print('---aaa---', np.expand_dims(proba_category[:,j],1).shape)
            proba_commodity_list.append(np.repeat(np.expand_dims(proba_category[:,j],1), len(self.category_dict[self.category_list[j]]), axis=1))
        self.preference_matrix = np.hstack(proba_commodity_list)
        #print(proba_commodity_list[0].shape)
        #print(proba_commodity_list[1].shape)
        #print(self.proba_commodity.shape)
        self.preference_matrix += np.random.uniform(0, 0.1, (self.n_client, self.n_commodity))
        return
    
    def get_clients(self, n):
        return np.random.choice(list(range(self.n_client)), n, replace=False)
    
    def update_desire(self, clients_list, rate_rise=None, rate_decay=0.01):
        if rate_decay is not None:
            self.desire_matrix *= 1 - rate_decay
        
        if rate_rise is None:
            rate_rise = np.random.normal()
        if rate_rise < 0:
            rate_rise = 0
        self.desire_matrix[clients_list] += rate_rise * self.preference_matrix[clients_list]
    
    def get_waiting_list(self, client):
        client_desire = self.desire_matrix[client]
        return client_desire[client_desire>self.desire_threshold_list[client]]
    
    def return_command(self, client, recommandation):
        pass