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
        self.best_score = float("inf")
        self.best_solution = None

        self.population = np.array([[np.random.uniform(low, high) for (low, high) in bornes]for _ in range(taille_population)])

        self.compteur_cout_fonction_objective = 0

    def gerer_bornes(self, valeurs_in): # Check des bornes
        for dim in range(self.nbr_dim):
            min, max = self.bornes[dim]
            if valeurs_in[dim] < min:
                valeurs_in[dim] = min
            elif valeurs_in[dim] > max:
                valeurs_in[dim] = max
        return valeurs_in
    
    def mutation(self, idx): # Mutation genere 3 vecteurs randoms et calcule nouv vecteur mutant 
        indices = list(range(self.taille_population))
        indices.remove(idx)

        a, b, c = np.random.choice(indices, 3, replace=False)

        x_a = self.population[a]
        x_b = self.population[b]
        x_c = self.population[c]

        vect_mutant = x_a + self.facteur_diff * (x_b - x_c)
        vect_mutant_borne = self.gerer_bornes(vect_mutant)

        return vect_mutant_borne

    def selection(self, i, candidat): # Compare candidat et vecteur cible et garde best
        result_cible = penaliser_algo(self.population[i])
        self.compteur_cout_fonction_objective += 1
        result_candidat = penaliser_algo(candidat)
        self.compteur_cout_fonction_objective += 1
        if result_candidat <= result_cible:
            self.population[i] = candidat
            return result_candidat
        else:
            return result_cible

    def update_best(self): # MAJ de la meilleure solution et score de la population
        for i in range(self.taille_population):
            score = penaliser_algo(self.population[i])
            self.compteur_cout_fonction_objective += 1
            if score < self.best_score:
                self.best_score = score
                self.best_solution = self.population[i].copy()

    def croisement(self, cible, mutant): # Croisement de vecteur cible et mutant pour generer un candidat
        candidat = np.copy(cible)
        j_random = np.random.randint(self.nbr_dim)
        for j in range(self.nbr_dim):
            if np.random.rand() < self.taux_croisement or j == j_random:
                candidat[j] = mutant[j]
        candidat= self.gerer_bornes(candidat)
        return candidat
        

    def run(self) : # Boucle principale de DE
        compteur_sans_amelioration = 0
        historique = []
        for iteration in range(self.max_iter):
            ancien_best_score = self.best_score
            for i in range(self.taille_population):
                cible = self.population[i].copy()
                mutant = self.mutation(i)
                candidat = self.croisement(cible, mutant)

                self.selection(i, candidat)
            self.update_best()
            historique.append((iteration, self.compteur_cout_fonction_objective, self.best_score))

            if abs(self.best_score - ancien_best_score) < 1e-6:
                compteur_sans_amelioration += 1
            else:
                compteur_sans_amelioration = 0
            if compteur_sans_amelioration >= self.min_iter:
                break
        return self.best_solution, self.best_score, historique, self.compteur_cout_fonction_objective