# 📌 TP3 – Métaheuristiques (PSO & DE)

Ce projet a été réalisé dans le cadre du cours **8INF852 – Métaheuristiques en optimisation**.
L’objectif est de comparer deux algorithmes d’optimisation :

* Particle Swarm Optimization (PSO)
* Differential Evolution (DE)

Le problème traité est un problème contraint de conception de ressort mécanique.

---

## ⚙️ Installation

### 1. Cloner le projet

```bash
git clone <url_du_repo>
cd nom_du_projet
```

### 2. Installer les dépendances

```bash
pip install numpy matplotlib pandas
```

---

## ▶️ Lancer le programme

### 🔹 Lancer avec les paramètres par défaut

```bash
python main.py
```

### 🔹 Choisir un algorithme

```bash
python main.py --algo pso
python main.py --algo de
python main.py --algo both
```

### 🔹 Modifier les paramètres

Exemple :

```bash
python main.py --algo both --runs 30 --population 30 --max_iter 100
python main.py --algo both --save
```

Paramètres disponibles :

* `--algo` : pso, de ou both
* `--runs` : nombre de simulations Monte Carlo
* `--seed` : graine aléatoire
* `--population` : taille de la population / essaim
* `--max_iter` : nombre max d’itérations
* `--min_iter` : critère d’arrêt (stagnation)
* `--facteur_diff` : paramètre F pour DE
* `--taux_croisement` : paramètre CR pour DE
* `--save ` : sauvegarde pour commande both

---

### 🔹 Mode menu interactif (je recommende)

```bash
python main.py --menu
```

Permet de :

* analyser PSO
* analyser DE
* comparer PSO vs DE

---

## 📊 Résultats

Le programme génère :

* Graphiques de convergence
* Graphiques de distribution (violin plot)
* Tableau comparatif des performances

Les résultats des runs sont aussi sauvegardés en fichiers CSV :

* `resultats_de.csv`
* `resultats_pso.csv`

---

## 🔁 Reproduire les résultats

Pour reproduire les résultats du rapport :

```bash
python main.py --algo both --runs 30 --population 30 --max_iter 100 --seed 42
```

---

## 🧠 Remarques

* Les deux algorithmes utilisent une fonction de pénalisation pour gérer les contraintes.
* La comparaison est faite sur un budget basé sur le nombre d’appels à la fonction objectif.
* Les résultats peuvent varier légèrement à cause du caractère aléatoire.

---

## 👤 Auteur

Arthur Delhaye
