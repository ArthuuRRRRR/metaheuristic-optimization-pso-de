import numpy as np
from Particle_Swarm_Optimization import pso
from Differential_Evolution import de
from monte_carlo import monte_carlo_pso, monte_carlo_de
from display_result import historiques_vers_dataframe, tracer_graphe_convergence, tracer_violin, tableau_comparatif

import pandas as pd

import csv

def sauvegarder_csv(nom_fichier, resultats):
    with open(nom_fichier, mode='w', newline='') as fichier:
        writer = csv.writer(fichier)

        writer.writerow(["run", "x1", "x2", "x3", "score"])

        for run, solution, score in resultats:
            x1, x2, x3 = solution
            writer.writerow([run, x1, x2, x3, score])
        


def main():
    n_runs = 30
    seed = 42

    resultats_de, historiques_de, compteur_de = monte_carlo_de(n_runs, seed_base = seed)

    resultats_pso, historiques_pso, compteur_pso = monte_carlo_pso(n_runs, seed_base = seed)
    """

    print("\nDE Results:")
    for run, solution, score in resultats_de:
        print(f"Run {run}: Best Solution = {solution}, Best Score = {score}, Compteur = {compteur_de[run][1]}")   

    print("\nPSO Results:")
    for run, solution, score in resultats_pso:
        print(f"Run {run}: Best Solution = {solution}, Best Score = {score}, Compteur = {compteur_pso[run][1]}") """

    #sauvegarder_csv("historique_de.csv", historiques_de)
    #sauvegarder_csv("historique_pso.csv", historiques_pso)  
    df_de = historiques_vers_dataframe(historiques_de, "DE")
    df_pso = historiques_vers_dataframe(historiques_pso, "PSO")

    df_convergence = pd.concat([df_de, df_pso], ignore_index=True)

    tracer_graphe_convergence(df_convergence)
    """
    compteurs_de = [c for _, c in compteur_de]
    compteurs_pso = [c for _, c in compteur_pso]
    
    print("\n=== Budget (nombre d'appels à f) ===")

    print("\nDE :")
    print(f"Moyenne = {np.mean(compteurs_de):.2f}")
    print(f"Médiane = {np.median(compteurs_de):.2f}")
    print(f"Min = {np.min(compteurs_de)}")
    print(f"Max = {np.max(compteurs_de)}")

    print("\nPSO :")
    print(f"Moyenne = {np.mean(compteurs_pso):.2f}")
    print(f"Médiane = {np.median(compteurs_pso):.2f}")
    print(f"Min = {np.min(compteurs_pso)}")
    print(f"Max = {np.max(compteurs_pso)}") """
    

    tracer_violin(resultats_de, "DE test", resultats_pso, "PSO test")

    df_comparatif = tableau_comparatif(resultats_de, "DE test", resultats_pso, "PSO test")
    print("\n=== Tableau Comparatif ===")
    print(df_comparatif)

if __name__ == "__main__":
    main()

