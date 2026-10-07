"""Exhaustive check of Graffiti conjecture 198 on all graphs with 2..8 vertices.

198 (connected graphs with sum of Odd <= sum of Even):
    minimum of derivative of eigenvalues <= n / mean gravity.

The proof in README.md covers every n; this is an independent check. It also reports
whether the inequality holds for the connected graphs outside the class.

Graphs are generated up to isomorphism by adding a vertex with every possible
neighbourhood; the counts are checked against OEIS A000088. Requires networkx and numpy.
"""
from itertools import combinations

import networkx as nx
import numpy as np

A000088 = {1: 1, 2: 2, 3: 4, 4: 11, 5: 34, 6: 156, 7: 1044, 8: 12346}


def all_graphs(nmax):
    level = [nx.empty_graph(1)]
    yield 1, level
    for n in range(2, nmax + 1):
        buckets = {}
        for G in level:
            for r in range(n):
                for S in combinations(range(n - 1), r):
                    H = G.copy()
                    H.add_node(n - 1)
                    H.add_edges_from((n - 1, s) for s in S)
                    key = (tuple(sorted(d for _, d in H.degree)),
                           nx.weisfeiler_lehman_graph_hash(H, iterations=3))
                    bucket = buckets.setdefault(key, [])
                    if not any(nx.is_isomorphic(H, K) for K in bucket):
                        bucket.append(H)
        level = [H for b in buckets.values() for H in b]
        yield n, level


def evaluate(G):
    n = G.number_of_nodes()
    D = np.zeros((n, n), dtype=int)
    for u, row in nx.all_pairs_shortest_path_length(G):
        for v, d in row.items():
            D[u, v] = d
    odd = (D % 2 == 1).sum()
    even = (D % 2 == 0).sum()  # includes distance 0
    in_class = odd <= even
    ev = np.sort(np.linalg.eigvalsh(nx.to_numpy_array(G, nodelist=range(n))))
    gap = float(np.min(np.diff(ev)))
    deg = np.array([G.degree(v) for v in range(n)], dtype=float)
    iu = np.triu_indices(n, 1)
    mean_gravity = float((np.outer(deg, deg)[iu] / ((n - 1) * D[iu])).mean())
    return in_class, gap, n / mean_gravity


def main():
    stats = {True: [0, None], False: [0, None]}
    bad = {True: 0, False: 0}
    for n, graphs in all_graphs(8):
        assert len(graphs) == A000088[n], (n, len(graphs))
        if n < 2:
            continue
        for G in graphs:
            if not nx.is_connected(G):
                continue
            in_class, lhs, rhs = evaluate(G)
            stats[in_class][0] += 1
            margin = rhs - lhs
            if stats[in_class][1] is None or margin < stats[in_class][1][0]:
                stats[in_class][1] = (margin, n, sorted(G.edges))
            if margin < -1e-9:
                bad[in_class] += 1
        print(f"n = {n}: {len(graphs)} graphs (A000088 ok)")
    for in_class, label in ((True, "in the class of 198"), (False, "connected, outside the class")):
        count, worst = stats[in_class]
        print(f"{label}: {count} graphs, violations {bad[in_class]}, "
              f"smallest margin {worst[0]:+.6f} at n = {worst[1]}, edges {worst[2]}")
    assert bad[True] == 0
    print("Graffiti 198 holds for every graph in its class on 2..8 vertices.")


if __name__ == "__main__":
    main()
