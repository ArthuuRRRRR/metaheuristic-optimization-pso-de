import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from fitness_function import verification_contraintes


def historiques_vers_dataframe(historiques, nom_algo): #Convertion historique en dataframe pour les analyses
    lignes = []

    for run, historique in historiques:
        for item in historique:
            if len(item) == 3:
                iteration, budget, cout = item
            else:
                iteration, cout = item
                budget = iteration

            lignes.append({
                "run": run,
                "algo": nom_algo,
                "iteration": iteration,
                "budget": budget,
                "cout": cout
            })

    return pd.DataFrame(lignes)


def tracer_graphe_convergence(df): # en fonction de l iteration
    plt.figure(figsize=(10, 6))

    for algo in df["algo"].unique():
        df_algo = df[df["algo"] == algo]

        stats = df_algo.groupby("iteration")["cout"].agg(median="median",q1=lambda x: x.quantile(0.25),q3=lambda x: x.quantile(0.75)).reset_index()

        plt.plot(stats["iteration"], stats["median"], label=f"{algo} médiane")
        plt.fill_between(stats["iteration"], stats["q1"], stats["q3"], alpha=0.2)

    plt.xlabel("Itération")
    plt.ylabel("Coût pénalisé")
    plt.yscale("log")
    plt.title("Profil de convergence statistique")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def tracer_violin(resultats_de,nom_algo_1,resultats_pso, nom_algo_2): # Tracer d'un graphique violin pour comparer les distributions des résultats
    data = []

    for _, _, score in resultats_de:
        data.append({"algo": nom_algo_1, "score": score})

    for _, _, score in resultats_pso:
        data.append({"algo": nom_algo_2, "score": score})

    df = pd.DataFrame(data)

    plt.figure(figsize=(8, 6))

    parts = plt.violinplot([df[df["algo"] == nom_algo_1]["score"], df[df["algo"] == nom_algo_2]["score"]], showmeans=True, showmedians=True)

    plt.xticks([1, 2], [nom_algo_1, nom_algo_2])
    plt.ylabel("Coût pénalisé")
    plt.title("Distribution des performances finales")

    plt.grid(True)
    plt.tight_layout()
    plt.show()


def tableau_comparatif(resultats_de, nom_algo_1, resultats_pso, nom_algo_2): # Apperçu statistique des résultats 
    lignes = []

    algorithmes = {
        nom_algo_1: resultats_de,
        nom_algo_2: resultats_pso
    }

    for nom_algo, resultats in algorithmes.items():
        scores = [score for _, _, score in resultats]

        nb_runs = len(resultats)
        meilleur = np.min(scores)
        pire = np.max(scores)
        mediane = np.median(scores)
        moyenne = np.mean(scores)
        ecart_type = np.std(scores, ddof=1) if nb_runs > 1 else 0.0
        q1 = np.quantile(scores, 0.25)
        q3 = np.quantile(scores, 0.75)
        iqr = q3 - q1


        nb_faisables = 0
        for _, solution, _ in resultats:
            if verification_contraintes(solution):
                nb_faisables += 1

        proportion_faisable = nb_faisables / nb_runs if nb_runs > 0 else 0.0

        lignes.append({
            "Algorithme": nom_algo,
            "Nb runs": nb_runs,
            "Meilleur score": meilleur,
            "Pire score": pire,
            "Médiane": mediane,
            "Moyenne": moyenne,
            "Écart-type": ecart_type,
            "Q1": q1,
            "Q3": q3,
            "IQR": iqr,
            "Proportion faisable": proportion_faisable
        })

    df = pd.DataFrame(lignes)

    return df


def tracer_graphe_convergence_budget(df): # en fonction du budget (nombre d'appels à la fonction objectif)
    plt.figure(figsize=(10, 6))

    for algo in df["algo"].unique():
        df_algo = df[df["algo"] == algo]

        stats = df_algo.groupby("budget")["cout"].agg(
            median="median",
            q1=lambda x: x.quantile(0.25),
            q3=lambda x: x.quantile(0.75)
        ).reset_index()

        plt.plot(stats["budget"], stats["median"], label=f"{algo} médiane")
        plt.fill_between(stats["budget"], stats["q1"], stats["q3"], alpha=0.2)

    plt.xlabel("Budget : nombre d'appels à la fonction objectif")
    plt.ylabel("Coût pénalisé")
    plt.yscale("log")
    plt.title("Profil de convergence en fonction du budget")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()