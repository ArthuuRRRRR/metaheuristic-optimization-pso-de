import numpy as np
from fitness_function import penaliser_algo

class de:
    def __init__(self, taille_population, nbr_dim, max_iter, min_iter, bornes, facteur_diff, taux_croisement):
        self.taille_population = taille_population
        self.nbr_dim = nbr_dim
        self.max_iter = max_iter
        self.min_iter = min_iter
        self.bornes = bornes
        self.facteur_diff = facteur_diff
        self.taux_croisement = taux_croisement

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
        indices.remove(idx)

        a, b, c = np.random.choice(indices, 3, replace=False)

        x_a = self.population[a]
        x_b = self.population[b]
        x_c = self.population[c]

        vect_mutant = x_a + self.facteur_diff * (x_b - x_c)
        vect_mutant_borne = self.gerer_bornes(vect_mutant)

        return vect_mutant_borne

    def selection(self, i):
        result = penaliser_algo(self.population[i])

    def update_best():
        pass

    def croisement():
        pass

    def run(self) :
        compteur_sans_amelioration = 0
        historique = []
        for iteration in range(self.max_iter):
            pass