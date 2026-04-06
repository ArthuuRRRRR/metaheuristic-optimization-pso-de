import numpy as np
from Particle_Swarm_Optimization import pso
from Differential_Evolution import de

def main():
    pso_algo = pso(nbr_particules=30, nbr_dim=3, max_iter=100, min_iter=10, bornes=[(0.05, 2.00), (0.25, 1.30), (2.00, 15.0)])
    gbest_position, gbest_score, historique = pso_algo.run()
    print("Meilleure position trouvée :", gbest_position)
    print("Meilleur score trouvé :", gbest_score)
    print("Historique des scores :", historique)

    de_algo = de(taille_population=30, nbr_dim=3, max_iter=100, min_iter=10, bornes=[(0.05, 2.00), (0.25, 1.30), (2.00, 15.0)], facteur_diff=0.8, taux_croisement=0.9)
    best_solution, best_score, historique_de = de_algo.run()
    print("Meilleure solution trouvée :", best_solution)
    print("Meilleur score trouvé :", best_score)
    print("Historique des scores :", historique_de)



if __name__ == "__main__":
    main()

