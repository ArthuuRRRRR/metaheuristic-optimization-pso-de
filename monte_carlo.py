import numpy as np
from Particle_Swarm_Optimization import pso
from Differential_Evolution import de


def monte_carlo_de(n_runs,taille_population,nbr_dim,max_iter,min_iter, seed_base=None):
    resultats = []
    historiques = []
    compteur =[]

    for run in range(n_runs ):
        if seed_base is not None:
            np.random.seed(seed_base + run)

        de_algo = de(taille_population=taille_population,nbr_dim=nbr_dim,max_iter=max_iter,min_iter=min_iter,bornes=[(0.05, 2.00), (0.25, 1.30), (2.00, 15.0)],facteur_diff=0.8,taux_croisement=0.9)

        best_solution, best_score, historique, compteur_cout_fonction_objective = de_algo.run()

        resultats.append((run, best_solution, best_score))
        historiques.append((run, historique))
        compteur.append((run, compteur_cout_fonction_objective))

    return resultats, historiques, compteur

def monte_carlo_pso(n_runs,nbr_particules,nbr_dim,max_iter,min_iter, seed_base=None):
    resultats = []
    historiques = []
    compteur =[]
    for run in range(n_runs):
        if seed_base is not None:
            np.random.seed(seed_base + run)

        pso_algo = pso(nbr_particules=nbr_particules, nbr_dim=nbr_dim, max_iter=max_iter, min_iter=min_iter, bornes=[(0.05, 2.00), (0.25, 1.30), (2.00, 15.0)])

        gbest_position, gbest_score, historique, compteur_cout_fonction_objective = pso_algo.run()

        resultats.append((run, gbest_position, gbest_score))
        historiques.append((run, historique))
        compteur.append((run, compteur_cout_fonction_objective))

    return resultats, historiques, compteur