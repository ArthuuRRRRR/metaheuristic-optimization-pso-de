import numpy as np
from fitness_function import penaliser_algo
class pso:
    def __init__(self, nbr_particules, nbr_dim, max_iter, min_iter, bornes):
        self.nbr_particules = nbr_particules
        self.nbr_dim = nbr_dim
        self.max_iter = max_iter
        self.min_iter = min_iter
        self.bornes = bornes

        self.positions = np.array([[np.random.uniform(low, high) for (low, high) in bornes]for _ in range(nbr_particules)])

        self.vitesses = np.zeros((nbr_particules, nbr_dim))

        self.pbest_positions = self.positions.copy()
        self.pbest_scores = np.full(nbr_particules, np.inf)

        self.gbest_position = np.zeros(nbr_dim)
        self.gbest_score = np.inf

        self.w= 0.5
        self.c1 = 1.5
        self.c2 = 1.5

        self.compteur_cout_fonction_objective = 0
    
        
    def update_vitesse(self) :
        for i in range(self.nbr_particules):
            r1 = np.random.rand(self.nbr_dim)
            r2 = np.random.rand(self.nbr_dim)

            for dim in range(self.nbr_dim):
                inertie = self.w * self.vitesses[i][dim]
                cognitive = self.c1 * r1[dim] * (self.pbest_positions[i][dim] - self.positions[i][dim])
                social = self.c2 * r2[dim] * (self.gbest_position[dim] - self.positions[i][dim])
                self.vitesses[i][dim] = inertie + cognitive + social
            


    def update_position(self) :
        for i in range(self.nbr_particules):
            for dim in range(self.nbr_dim):
                self.positions[i][dim] += self.vitesses[i][dim]

                min, max = self.bornes[dim]

                if self.positions[i][dim] < min:
                    self.positions[i][dim] = min
                elif self.positions[i][dim] > max:
                    self.positions[i][dim] = max
       

    def update_pbest(self) :

        
        for i in range(self.nbr_particules):
            score = penaliser_algo(self.positions[i])
            self.compteur_cout_fonction_objective += 1

            if score < self.pbest_scores[i]:
                self.pbest_scores[i] = score
                self.pbest_positions[i] = self.positions[i].copy()

    def update_gbest(self) :
        for i in range(self.nbr_particules):
            if self.pbest_scores[i] < self.gbest_score:
                self.gbest_score = self.pbest_scores[i]
                self.gbest_position = self.pbest_positions[i].copy()


    def run(self) :
        self.update_pbest()
        self.update_gbest()
        

        ancienne_gbest_score = self.gbest_score
        compteur = 0
        historique = []
        for iter in range(self.max_iter):
            self.update_vitesse()
            self.update_position()
            self.update_pbest()
            self.update_gbest()
            historique.append((iter, self.gbest_score))

            if abs(self.gbest_score - ancienne_gbest_score) < 1e-6:
                compteur += 1
            else: 
                compteur = 0
                ancienne_gbest_score = self.gbest_score
            if compteur >= self.min_iter and compteur >= 10:
                break
        return self.gbest_position, self.gbest_score, historique , self.compteur_cout_fonction_objective
