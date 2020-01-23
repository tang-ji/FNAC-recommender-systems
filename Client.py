import numpy as np

def count(y):
    return sum([len(y.get(x, 0)) for x in y])

class Clients:
    def __init__(self, n_client, category_dict):
        self.category_dict = category_dict
        self.n_client = n_client
        self.n_category = len(category_dict.keys())
        self.category_list = list(category_dict.keys())
        self.n_commodity = count(category_dict)
        self.preference_matrix = np.zeros((n_client, self.n_commodity))
        self.proba_commodity = None

        #print(self.category_list)

        self.generate_client_distribution()

        
    def generate_client_distribution(self):
		
        proba_category = np.random.uniform(0, 0.9, (self.n_client, self.n_category))
        proba_commodity_list = []
        for j in range(proba_category.shape[1]):
            #print('---aaa---', np.expand_dims(proba_category[:,j],1).shape)
            proba_commodity_list.append(np.repeat(np.expand_dims(proba_category[:,j],1), len(self.category_dict[self.category_list[j]]), axis=1))
        self.proba_commodity = np.hstack(proba_commodity_list)
        #print(proba_commodity_list[0].shape)
        #print(proba_commodity_list[1].shape)
        #print(self.proba_commodity.shape)
        self.proba_commodity += np.random.uniform(0, 0.1, (self.n_client, self.n_commodity))
		
