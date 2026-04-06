import numpy as np
from Particle_Swarm_Optimization import pso
from Differential_Evolution import de


def monte_carlo_de(n_runs):
    resultats = []
    historiques = []

    for run in range(n_runs):
        np.random.seed(run)

        de_algo = de(taille_population=30,nbr_dim=3,max_iter=100,min_iter=10,bornes=[(0.05, 2.00), (0.25, 1.30), (2.00, 15.0)],facteur_diff=0.8,taux_croisement=0.9)

        best_solution, best_score, historique = de_algo.run()

        resultats.append((run, best_solution, best_score))
        historiques.append((run, historique))

    return resultats, historiques

def monte_carlo_pso(n_runs):
    resultats = []
    historiques = []

    for run in range(n_runs):
        np.random.seed(run)

        pso_algo = pso(nbr_particules=30, nbr_dim=3, max_iter=100, min_iter=10, bornes=[(0.05, 2.00), (0.25, 1.30), (2.00, 15.0)])

        gbest_position, gbest_score, historique = pso_algo.run()

        resultats.append((run, gbest_position, gbest_score))
        historiques.append((run, historique))


    return resultats, historiques