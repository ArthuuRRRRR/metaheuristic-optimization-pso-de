import numpy as np
from Particle_Swarm_Optimization import pso

def main():
    pso_algo = pso(nbr_particules=30, nbr_dim=3, max_iter=100, min_iter=10, bornes=[(78, 102), (33, 45), (27, 45)])
    gbest_position, gbest_score, historique = pso_algo.run()
    print("Meilleure position trouvée :", gbest_position)
    print("Meilleur score trouvé :", gbest_score)
    print("Historique des scores :", historique)


if __name__ == "__main__":
    main()