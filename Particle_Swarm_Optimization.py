import numpy as np

class pso:
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

        self.w= 0.5
        self.c1 = 1.5
        self.c2 = 1.5
    
        
    def update_vitesse(self) :
        for i in range(self.nbr_particules):
            r1 = np.random.rand(self.nbr_dim)
            r2 = np.random.rand(self.nbr_dim)

            for dim in range(self.nbr_dim):
                inertie = self.w * self.vitesses[i][dim]
                cog = 1.5 * r1[dim] * self.pbest_positions[i][dim]
                #cognitive = self.c1 * r1[dim] * (self.pbest_positions[i][dim] - self.positions[i][dim])
                #social = self.c2 * r2[dim] * (self.gbest_position[dim] - self.positions[i][dim])
                #self.vitesses[i][dim] = inertie + cognitive + social
            


    def update_position(self) :
        for i in range(self.nbr_particules):
            for dim in range(self.nbr_dim):
                self.positions[i][dim] += self.vitesses[i][dim]

                min, max = self.bornes[dim]

                if self.positions[i][dim] < min:
                    self.positions[i][dim] = min
                elif self.positions[i][dim] > max:
                    self.positions[i][dim] = max

       

    def update_pbest() :
        pass
    def update_gbest() :
        pass
    def run(self) :
        pass

