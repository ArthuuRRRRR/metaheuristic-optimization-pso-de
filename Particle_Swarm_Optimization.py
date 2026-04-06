import numpy as np

class PSO:
    def __init__(self, nbr_particules, nbr_dim, max_iter, min_iter, bornes, fonction_objectives):
        self.nbr_particules = nbr_particules
        self.nbr_dim = nbr_dim
        self.max_iter = max_iter
        self.min_iter = min_iter
        self.bornes = bornes
        self.fonction_objectives = fonction_objectives

        self.positions = np.array([[np.random.uniform(low, high) for (low, high) in bornes]for _ in range(nbr_particules)])

        self.vitesses = np.zeros((nbr_particules, nbr_dim))

        self.pbest_positions = self.positions.copy()
        self.pbest_scores = np.full(nbr_particules, np.inf)

        self.gbest_position = np.zeros(nbr_dim)
        self.gbest_score = np.inf
        
    def update_vitesse() :
        pass
    def update_position() :
        pass

    def update_pbest() :
        pass
    def update_gbest() :
        pass
    def run(self) :
        pass

