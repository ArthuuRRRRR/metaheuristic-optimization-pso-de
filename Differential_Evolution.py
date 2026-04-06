import numpy as np
from fitness_function import penaliser_algo

class de:
    def __init__(self, taille_population, nbr_dim, max_iter, min_iter, bornes):
        self.taille_population = taille_population
        self.nbr_dim = nbr_dim
        self.max_iter = max_iter
        self.min_iter = min_iter
        self.bornes = bornes

        self.population = np.array([[np.random.uniform(low, high) for (low, high) in bornes]for _ in range(taille_population)])

    def gerer_bornes(self, valeurs_in):
        for dim in range(self.nbr_dim):
            min, max = self.bornes[dim]
            if valeurs_in[dim] < min:
                valeurs_in[dim] = min
            elif valeurs_in[dim] > max:
                valeurs_in[dim] = max
        return valeurs_in
    
    def mutation(self, idx):
        indices = list(range(self.taille_population))
        #indices.remove(idx)
        
        pass

    def selection():
        pass

    def update_best():
        pass

    def run(self) :
        pass