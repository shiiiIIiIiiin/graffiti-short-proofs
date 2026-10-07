"""Exact check of Graffiti conjecture 219 for all triangle-free graphs on 2..8 vertices.

219: if G is triangle-free then the 2nd largest eigenvalue of the gravity matrix <= number of nonedges.

This covers the cases n <= 8 that the analytic argument in README.md leaves open.

- The triangle-free graphs are generated up to isomorphism by adding a vertex whose
  neighbourhood is an independent set (every triangle-free graph on k+1 vertices arises
  from one on k vertices this way). The counts are checked against OEIS A006785.
- For each graph, with k = number of nonedges, "2nd largest eigenvalue of Gr <= k" means
  that Gr - kI has at most one positive eigenvalue. Gr has rational entries, so the
  characteristic polynomial of Gr - kI is computed exactly; it is real-rooted (Gr is
  symmetric), so by Descartes' rule of signs its number of positive roots equals the
  number of sign changes of its coefficients.

Requires sympy, networkx and numpy.
"""
from itertools import combinations

import networkx as nx
import numpy as np
import sympy as sp

A006785 = {1: 1, 2: 2, 3: 3, 4: 7, 5: 14, 6: 38, 7: 107, 8: 410}


def independent_sets(G):
    nodes = list(G.nodes)
    for r in range(len(nodes) + 1):
        for S in combinations(nodes, r):
            if not any(G.has_edge(u, v) for u, v in combinations(S, 2)):
                yield S


def triangle_free_graphs(nmax):
    level = [nx.empty_graph(1)]
    yield 1, level
    for n in range(2, nmax + 1):
        buckets = {}
        for G in level:
            for S in independent_sets(G):
                H = G.copy()
                H.add_node(n - 1)
                H.add_edges_from((n - 1, s) for s in S)
                key = nx.weisfeiler_lehman_graph_hash(H, iterations=3)
                bucket = buckets.setdefault(key, [])
                if not any(nx.is_isomorphic(H, K) for K in bucket):
                    bucket.append(H)
        level = [H for b in buckets.values() for H in b]
        yield n, level


def gravity(G):
    n = G.number_of_nodes()
    dist = dict(nx.all_pairs_shortest_path_length(G))
    deg = dict(G.degree)
    Gr = sp.zeros(n, n)
    for u in range(n):
        for v in range(n):
            if u != v and v in dist[u]:
                Gr[u, v] = sp.Rational(deg[u] * deg[v], (n - 1) * dist[u][v])
    return Gr


def sign_changes(coeffs):
    signs = [c > 0 for c in coeffs if c != 0]
    return sum(1 for a, b in zip(signs, signs[1:]) if a != b)


def main():
    worst = None
    for n, graphs in triangle_free_graphs(8):
        assert len(graphs) == A006785[n], (n, len(graphs))
        if n < 2:
            continue
        for G in graphs:
            k = n * (n - 1) // 2 - G.number_of_edges()
            Gr = gravity(G)
            positive = sign_changes((Gr - k * sp.eye(n)).charpoly().all_coeffs())
            assert positive <= 1, f"219 fails: {sorted(G.edges)}"
            # numerical margin, for information only
            ev = np.sort(np.linalg.eigvalsh(np.array(Gr.tolist(), dtype=float)))[::-1]
            margin = k - ev[1]
            if worst is None or margin < worst[0]:
                worst = (margin, n, sorted(G.edges))
        print(f"n = {n}: {len(graphs)} triangle-free graphs, all satisfy 219")
    print(f"smallest margin (nonedges - 2nd eigenvalue): {worst[0]:.6f} at n = {worst[1]}, edges {worst[2]}")
    print("Graffiti 219 holds for every triangle-free graph on 2..8 vertices.")


if __name__ == "__main__":
    main()
