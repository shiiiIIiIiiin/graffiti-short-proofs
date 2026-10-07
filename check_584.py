"""Numerical check of Graffiti conjecture 584 and its girth >= 5 extension (not part of the proof).

584: for every tree T, lambda_max(L(T)) <= alpha(T) + 2.
Checks all trees with 2..18 vertices (alpha = n - matching number, by Konig's theorem) and
random graphs of girth at least five (alpha by brute force on the complement's cliques).
Requires networkx and numpy.
"""
import random

import networkx as nx
import numpy as np


def lap_max(G):
    A = nx.to_numpy_array(G)
    return float(np.linalg.eigvalsh(np.diag(A.sum(1)) - A)[-1])


def main():
    worst = None
    count = 0
    for n in range(2, 19):
        for T in nx.nonisomorphic_trees(n):
            count += 1
            alpha = n - len(nx.max_weight_matching(T, maxcardinality=True))
            slack = alpha + 2 - lap_max(T)
            assert slack > -1e-9
            if worst is None or slack < worst[0]:
                worst = (slack, n, sorted(d for _, d in T.degree))
    print(f"{count} trees with 2..18 vertices: no violation; "
          f"smallest alpha + 2 - lambda_max = {worst[0]:.6f} (n = {worst[1]}, degrees {worst[2]})")

    rng = random.Random(4)
    checked = 0
    for _ in range(3000):
        n = rng.randint(6, 26)
        G = nx.gnp_random_graph(n, rng.uniform(0.05, 0.3), seed=rng.randrange(10 ** 9))
        if G.number_of_edges() == 0 or nx.girth(G) < 5:
            continue
        alpha = max(len(c) for c in nx.find_cliques(nx.complement(G)))
        assert lap_max(G) <= alpha + 2 + 1e-9
        checked += 1
    print(f"{checked} random graphs of girth at least five: no violation")


if __name__ == "__main__":
    main()
