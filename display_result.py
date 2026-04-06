import matplotlib.pyplot as plt
import pandas as pd


def historiques_vers_dataframe(historiques, nom_algo):
    lignes = []

    for run, historique in historiques:
        for item in historique:
            if isinstance(item, tuple) and len(item) == 2:
                iteration, cout = item
            else:
                iteration = len([x for x in lignes if x["run"] == run and x["algo"] == nom_algo])
                cout = item

            lignes.append({"run": run,"algo": nom_algo,"iteration": iteration,"cout": cout})

    return pd.DataFrame(lignes)


def tracer_graphe_convergence(df):
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