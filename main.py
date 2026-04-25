import argparse

import numpy as np
from Particle_Swarm_Optimization import pso
from Differential_Evolution import de
from monte_carlo import monte_carlo_pso, monte_carlo_de
from display_result import historiques_vers_dataframe, tracer_graphe_convergence, tracer_violin, tableau_comparatif, tracer_graphe_convergence_budget

import pandas as pd

import csv

def sauvegarder_csv(nom_fichier, resultats): #fonction sauvegarde
    with open(nom_fichier, mode='w', newline='') as fichier:
        writer = csv.writer(fichier)

        writer.writerow(["run", "x1", "x2", "x3", "score"])

        for run, solution, score in resultats:
            x1, x2, x3 = solution
            writer.writerow([run, x1, x2, x3, score])
    print(f"Résultats sauvegardés")
        


def construire_parser(): # Pour avoir les commandes d execution
    parser = argparse.ArgumentParser(description="TP3 - Exécution des expériences PSO / DE")

    parser.add_argument("--algo",type=str,choices=["pso", "de", "both"],default="both",help="Algorithme à exécuter")

    parser.add_argument("--runs",type=int,default=30,help="Nombre de runs Monte-Carlo")

    parser.add_argument("--seed",type=int,default=42,help="Seed de base")

    parser.add_argument("--population",type=int,default=30,help="Taille de la population pour DE et nombre de particules pour PSO")

    parser.add_argument("--max_iter",type=int,default=100,help="Nombre maximum d'itérations pour DE et PSO")

    parser.add_argument("--min_iter",type=int,default=10,help="Nombre minimum d'itérations pour DE et PSO")

    parser.add_argument("--facteur_diff",type=float,default=0.8,help="Facteur de différenciation pour DE")

    parser.add_argument("--taux_croisement",type=float,default=0.9,help="Taux de croisement pour DE")

    parser.add_argument("--menu",action="store_true",help="Afficher le menu interactif")

    parser.add_argument("--save", action="store_true", help="Sauvegarder les résultats en CSV")

    return parser


def afficher_budget(compteurs_de, compteurs_pso): # budget
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
    print(f"Max = {np.max(compteurs_pso)}")


def menu(): # Menu interactif pour choisir les analyses à faire
    print("=== TP3 - Expériences PSO / DE ===")
    print("1. Analyse PSO")
    print("2. Analyse DE")
    print("3. Exécuter les deux et comparer")
    print("4. Quitter")

    choix = input("Entrez votre choix (1-4) : ")

    if choix == "1":
        print("Analyse taille de l'essaim PSO")
        resultats_pso_nbr_particule_1, historiques_pso_nbr_particule_1, compteur_pso_1 = monte_carlo_pso(n_runs=30, seed_base=42,nbr_particules=30,nbr_dim=3,max_iter=100,min_iter=10)
        resultats_pso_nbr_particules_2, historiques_pso_nbr_particules_2, compteur_pso_2 = monte_carlo_pso(n_runs=30, seed_base=42,nbr_particules=60,nbr_dim=3,max_iter=100,min_iter=10)
        df_pso_nbr_particule_1 = historiques_vers_dataframe(historiques_pso_nbr_particule_1, "PSO - 30 particules")
        df_pso_nbr_particule_2 = historiques_vers_dataframe(historiques_pso_nbr_particules_2, "PSO - 60 particules")
        df_convergence_pso = pd.concat([df_pso_nbr_particule_1, df_pso_nbr_particule_2], ignore_index=True)
        tracer_graphe_convergence(df_convergence_pso)
        tracer_violin(resultats_pso_nbr_particule_1, "PSO - 30 particules", resultats_pso_nbr_particules_2, "PSO - 60 particules")

    if choix == "2":
        print("Analyse taille de la population DE")
        resultats_de_taille_population_1, historiques_de_taille_population_1, compteur_de_1 = monte_carlo_de(n_runs=30,taille_population=30,nbr_dim=3,max_iter=100,min_iter=10,facteur_diff=0.8,taux_croisement=0.9,seed_base=42)
        resultats_de_taille_population_2, historiques_de_taille_population_2, compteur_de_2 = monte_carlo_de(n_runs=30,taille_population=60,nbr_dim=3,max_iter=100,min_iter=10,facteur_diff=0.8,taux_croisement=0.9,seed_base=42)
        df_de_taille_population_1 = historiques_vers_dataframe(historiques_de_taille_population_1, "DE - 30 individus")
        df_de_taille_population_2 = historiques_vers_dataframe(historiques_de_taille_population_2, "DE - 60 individus")
        df_convergence_de = pd.concat([df_de_taille_population_1, df_de_taille_population_2], ignore_index=True)
        tracer_graphe_convergence(df_convergence_de)
        tracer_violin(resultats_de_taille_population_1, "DE - 30 individus", resultats_de_taille_population_2, "DE - 60 individus")
    
    if choix == "3":
        print("Comparaison PSO vs DE avec budget et sauvegarde resultats")
        resultats_de, historiques_de, compteur_de = monte_carlo_de(n_runs=30,taille_population=30,nbr_dim=3,max_iter=100,min_iter=10,facteur_diff=0.8,taux_croisement=0.9,seed_base=42)
        resultats_pso, historiques_pso, compteur_pso = monte_carlo_pso(n_runs=30, seed_base=42,nbr_particules=30,nbr_dim=3,max_iter=100,min_iter=10)
        df_de = historiques_vers_dataframe(historiques_de, "DE")
        df_pso = historiques_vers_dataframe(historiques_pso, "PSO")
        df_convergence = pd.concat([df_de, df_pso], ignore_index=True)
        tracer_graphe_convergence(df_convergence)
        tracer_violin(resultats_de, "DE", resultats_pso, "PSO")
        df_comparatif = tableau_comparatif(resultats_de, "DE", resultats_pso, "PSO")
        print("\n=== Tableau Comparatif ===")
        print(df_comparatif)

        compteurs_de = [c for _, c in compteur_de]
        compteurs_pso = [c for _, c in compteur_pso]
        
        afficher_budget(compteurs_de, compteurs_pso)

        tracer_graphe_convergence_budget(df_convergence)

        sauvegarder_csv("resultats_de.csv", resultats_de)
        sauvegarder_csv("resultats_pso.csv", resultats_pso)
    
    if choix == "4":
        print("Au revoir!")
        exit()
    


def main():
    parser = construire_parser()

    args = parser.parse_args()

    if args.menu:
        menu()
        return 
    elif args.algo in ["de", "both"]:
        resultats_de, historiques_de, compteur_de = monte_carlo_de(n_runs=args.runs,taille_population=args.population,nbr_dim=3,max_iter=args.max_iter,min_iter=args.min_iter, facteur_diff=args.facteur_diff,taux_croisement=args.taux_croisement,seed_base=args.seed)
        df_de = historiques_vers_dataframe(historiques_de, "DE")
        tracer_graphe_convergence(df_de)
        tracer_graphe_convergence_budget(df_de)
    if args.algo in ["pso", "both"]:
        resultats_pso, historiques_pso, compteur_pso = monte_carlo_pso(n_runs=args.runs,seed_base=args.seed,nbr_particules=args.population,nbr_dim=3,max_iter=args.max_iter,min_iter=args.min_iter)
        df_pso = historiques_vers_dataframe(historiques_pso, "PSO")
        tracer_graphe_convergence(df_pso)
        tracer_graphe_convergence_budget(df_pso)

    if args.algo == "both":
        df = tableau_comparatif(resultats_de, "DE", resultats_pso, "PSO")
        print("\n=== Tableau Comparatif ===")
        print(df)
        tracer_violin(resultats_de, "DE", resultats_pso, "PSO")
        if args.save:
            sauvegarder_csv("resultats_de.csv", resultats_de)
            sauvegarder_csv("resultats_pso.csv", resultats_pso)


if __name__ == "__main__":
    main()

