import numpy as np
from Particle_Swarm_Optimization import pso
from Differential_Evolution import de
from monte_carlo import monte_carlo_pso, monte_carlo_de
from display_result import historiques_vers_dataframe, tracer_graphe_convergence

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

    print("Running Monte Carlo for DE...")
    resultats_de, historiques_de = monte_carlo_de(n_runs)

    print("\nRunning Monte Carlo for PSO...")
    resultats_pso, historiques_pso = monte_carlo_pso(n_runs)

    print("\nDE Results:")
    for run, solution, score in resultats_de:
        print(f"Run {run}: Best Solution = {solution}, Best Score = {score}")   

    print("\nPSO Results:")
    for run, solution, score in resultats_pso:
        print(f"Run {run}: Best Solution = {solution}, Best Score = {score}") 

    #sauvegarder_csv("historique_de.csv", historiques_de)
    #sauvegarder_csv("historique_pso.csv", historiques_pso)  
    df_de = historiques_vers_dataframe(historiques_de, "DE")
    df_pso = historiques_vers_dataframe(historiques_pso, "PSO")

    df_convergence = pd.concat([df_de, df_pso], ignore_index=True)

    tracer_graphe_convergence(df_convergence)

if __name__ == "__main__":
    main()

