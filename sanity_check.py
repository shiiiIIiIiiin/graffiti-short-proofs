"""Numerical sanity check of the five inequalities on many graphs (not part of the proofs).

Graphs: all graphs on 2..7 vertices (networkx graph atlas) and random graphs G(n, p)
with 8 <= n <= 40. Reports the smallest slack (right side minus left side) per conjecture.

Requires numpy and networkx.
"""
import random

import networkx as nx
import numpy as np


def derivative_min(values):
    v = np.sort(values)
    return float(np.min(np.diff(v)))


def distances(G):
    n = G.number_of_nodes()
    D = np.full((n, n), -1)
    for u, row in nx.all_pairs_shortest_path_length(G):
        for v, d in row.items():
            D[u, v] = d
    return D


def gravity(G, D):
    n = G.number_of_nodes()
    deg = np.array([d for _, d in sorted(G.degree)], dtype=float)
    Gr = np.zeros((n, n))
    mask = D > 0
    Gr[mask] = (np.outer(deg, deg) / (n - 1))[mask] / D[mask]
    return Gr


def slacks(G):
    G = nx.convert_node_labels_to_integers(G)
    n = G.number_of_nodes()
    A = nx.to_numpy_array(G)
    L = np.diag(A.sum(1)) - A
    D = distances(G)
    connected = (D >= 0).all()
    deg = A.sum(1)
    out = {}
    lap = np.linalg.eigvalsh(L)
    adj = np.linalg.eigvalsh(A)
    if (deg > 0).all():
        dual = (A @ deg) / deg
        out[252] = (1 / dual).sum() - derivative_min(lap)
    if connected:
        odd = ((D % 2) == 1).sum(1)
        out[254] = (1 / odd).sum() - derivative_min(lap)
        even = ((D % 2) == 0).sum(1)  # includes distance 0
        if odd.sum() <= even.sum():
            Gr = gravity(G, D)
            mean_gr = Gr[np.triu_indices(n, 1)].mean()
            out[198] = n / mean_gr - derivative_min(adj)
    delta = deg.min()
    out[712] = (adj <= 1e-9).sum() - delta / (n - delta)
    if sum(nx.triangles(G).values()) == 0:
        Gr = gravity(G, D)
        theta = np.sort(np.linalg.eigvalsh(Gr))[::-1]
        out[219] = (n * (n - 1) / 2 - G.number_of_edges()) - theta[1]
    return out


def main():
    random.seed(0)
    graphs = [G for G in nx.graph_atlas_g() if G.number_of_nodes() >= 2]
    for _ in range(4000):
        n = random.randint(8, 40)
        graphs.append(nx.gnp_random_graph(n, random.choice([0.05, 0.1, 0.2, 0.4, 0.6, 0.8, 0.95]),
                                          seed=random.randrange(10 ** 9)))
    worst = {}
    for G in graphs:
        for c, s in slacks(G).items():
            if c not in worst or s < worst[c][0]:
                worst[c] = (s, G.number_of_nodes(), G.number_of_edges())
    for c in sorted(worst):
        s, n, m = worst[c]
        print(f"conjecture {c}: smallest slack {s:+.6f} (n = {n}, m = {m})")
        assert s >= -1e-9, f"violation of {c}"
    print(f"checked {len(graphs)} graphs: no violations")


if __name__ == "__main__":
    main()
