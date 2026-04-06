import numpy as np
from Particle_Swarm_Optimization import pso
from Differential_Evolution import de
from monte_carlo import monte_carlo_pso, monte_carlo_de

def main():
    n_runs = 30

    print("Running Monte Carlo for DE...")
    resultats_de, historiques_de = monte_carlo_de(n_runs)

    print("\nRunning Monte Carlo for PSO...")
    resultats_pso, historiques_pso = monte_carlo_pso(n_runs)


if __name__ == "__main__":
    main()

