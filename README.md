# Proofs of Graffiti conjectures 198, 219, 252, 254 and 712

[日本語](README.ja.md)

Shin Kimura (木村心), 2026-10-07

The proofs were written with the help of AI (Claude by Anthropic).

The conjectures are from S. Fajtlowicz, *Written on the Wall* (July 2004 version) [WOW].
Terms are as defined in the glossary of T. L. Brewster, M. J. Dinneen, V. Faber,
*A computational attack on the conjectures of Graffiti: New counterexamples and proofs*,
Discrete Math. 147 (1995) 35–55 [BDF].

## Notation and definitions

$G$ is a simple graph with $n$ vertices and $m$ edges; $d(v)$ is the degree of $v$, $\delta$ the minimum degree,
and $d(u,v)$ the distance. $A$ is the adjacency matrix and $L = \mathrm{Deg} - A$ the Laplacian, with eigenvalues
$0 = \mu_1 \le \mu_2 \le \dots \le \mu_n$. "Eigenvalues" without qualification are those of $A$.

- **Derivative** of a vector $V$ [BDF p. 52]: sort $V$ increasingly and put $V'(i) = V(i+1) - V(i)$.
  For a vector with $n \ge 2$ components, its minimum is the smallest gap between consecutive sorted components.
- **Even** and **Odd** vectors [BDF pp. 52, 54]: $\mathrm{Even}(v)$ is the number of vertices at even distance from $v$,
  including $v$ itself; $\mathrm{Odd}(v)$ is the number of vertices at odd distance from $v$.
- **Dual degree** [WOW p. 76]: $d^*(v)$ is the mean of the degrees of the neighbours of $v$.
- **Temperature** [BDF p. 54]: $t(v) = d(v)/(n - d(v))$.
- **Gravity matrix** [BDF p. 53]: $\mathrm{Gr}_{uv} = \dfrac{d(u)d(v)}{(n-1) d(u,v)}$ if $u \ne v$ lie in the same component,
  and $0$ otherwise. The **mean gravity** $\overline{\mathrm{Gr}}$ is the average of the entries above the diagonal [BDF p. 52].
- **Nonedge** [BDF p. 53]: a pair of non-adjacent vertices. There are $\binom{n}{2} - m$ of them.

## Two lemmas

**Lemma 1.** Let $x_1 \le \dots \le x_n$ with $n \ge 2$, let $g = \min_i (x_{i+1} - x_i)$ and let $\bar{x}$ be the mean. Then

(a) $g \le \dfrac{x_n - x_1}{n-1}$,

(b) $\displaystyle\sum_i (x_i - \bar{x})^2 \ge \frac{g^2 n (n^2 - 1)}{12}$.

*Proof.* (a) The $n-1$ gaps add up to $x_n - x_1$.
(b) We have $\sum_{i \lt j} (x_j - x_i)^2 = n \sum_i (x_i - \bar{x})^2$, and $x_j - x_i \ge (j-i) g \ge 0$. Hence

$$
n \sum_i (x_i - \bar{x})^2 \ge g^2 \sum_{i \lt j} (j-i)^2 = g^2 \cdot n \sum_{i=1}^{n} \left(i - \frac{n+1}{2}\right)^2 = g^2 \cdot \frac{n^2 (n^2-1)}{12}.
$$

**Lemma 2.** $\mu_n \le n$.

*Proof.* $L(G) + L(\overline{G}) = nI - J$. The all-ones vector is an eigenvector of $L(G)$, so the other eigenvectors
can be taken orthogonal to it. For such an $x$ with $L(G)x = \mu x$ we get $L(\overline{G})x = (n - \mu)x$, and
$L(\overline{G})$ is positive semidefinite, so $\mu \le n$.

## Conjecture 252

> **252.** The minimum of derivative of eigenvalues of Laplacian ≤ the sum of reciprocals of the dual degree.
> (WOW p. 76, "Conjectures for arbitrary graphs (246 : 274)")

**Theorem.** This holds for every graph with $n \ge 2$ vertices and no isolated vertex.

*Proof.* If $G$ is disconnected, $0$ is a Laplacian eigenvalue of multiplicity at least $2$, so the left side is $0$,
while the right side is positive. If $G$ is connected, Lemma 1(a) and Lemma 2 give

$$
\min_i (\mu_{i+1} - \mu_i) \le \frac{\mu_n - \mu_1}{n-1} \le \frac{n}{n-1}.
$$

Each $d^*(v)$ is an average of degrees, so $0 < d^*(v) \le n - 1$ and $\sum_v 1/d^*(v) \ge n/(n-1)$. $\square$

## Conjecture 254

> **254.** The minimum of derivative of eigenvalues of Laplacian ≤ the sum of reciprocals of Odd.
> (WOW p. 77, same section)

**Theorem.** This holds for every connected graph with $n \ge 2$ vertices
(and for every disconnected graph for which the right side is defined, since then the left side is $0$).

*Proof.* In a connected graph every vertex has a neighbour (at odd distance $1$) and is itself at even distance $0$,
so $1 \le \mathrm{Odd}(v) \le n - 1$ and $\sum_v 1/\mathrm{Odd}(v) \ge n/(n-1)$.
The left side is at most $n/(n-1)$ as in the proof of 252. $\square$

## Conjecture 712

> **712.** The minimum temperature ≤ number of nonpositive eigenvalues.
> (WOW p. 105)

**Theorem.** This holds for every graph.

*Proof.* The temperature is increasing in the degree, so the minimum temperature is $\delta/(n - \delta)$.
The complement $\overline{G}$ has maximum degree $n - 1 - \delta$, so it has an independent set of size at least
$n/(n - \delta)$ (repeatedly choose a vertex and delete it together with its at most $n - 1 - \delta$ neighbours).
This set is a clique of $G$, so the clique number satisfies $\omega \ge n/(n - \delta)$.
The principal submatrix of $A$ on a maximum clique is $J - I$, with eigenvalues $\omega - 1$ and $-1$
(multiplicity $\omega - 1$). By Cauchy interlacing, $A$ has at least $\omega - 1$ eigenvalues $\le -1$.
Writing $N_{\le 0}$ for the number of nonpositive eigenvalues, we get

$$
N_{\le 0} \ge \omega - 1 \ge \frac{n}{n-\delta} - 1 = \frac{\delta}{n-\delta}. \qquad \square
$$

Equality holds for complete graphs.

## Conjecture 198

> **198.** minimum of derivative of eigenvalues ≤ n / mean gravity.
> (WOW p. 71, in "Conjectures for connected graphs in which the sum of components of D is ≤ the sum of components of E (181:204)",
> where E and D are the Even and Odd vectors of conjecture 96)

**Theorem.** For every connected graph with $n \ge 2$ vertices and $\sum_v \mathrm{Odd}(v) \le \sum_v \mathrm{Even}(v)$,

$$
\min_i (\lambda_{i+1} - \lambda_i) \le \sqrt{\frac{6n}{n^2-1}} \le \frac{4(n-1)}{n} \le \frac{n}{\overline{\mathrm{Gr}}}.
$$

*Proof.* Let $g$ be the left side.

1. Every ordered pair $(v, u)$ is counted once in $\mathrm{Odd}(v)$ or $\mathrm{Even}(v)$, so
   $\sum_v (\mathrm{Odd}(v) + \mathrm{Even}(v)) = n^2$ and the hypothesis gives $\sum_v \mathrm{Odd}(v) \le n^2/2$.
   The neighbours of $v$ are at distance $1$, so $\mathrm{Odd}(v) \ge d(v)$ and $2m \le n^2/2$.
2. The eigenvalues of $A$ have mean $0$ and $\sum_i \lambda_i^2 = 2m$. By Lemma 1(b),
   $g^2 n(n^2-1)/12 \le 2m \le n^2/2$, so $g \le \sqrt{6n/(n^2-1)}$.
3. Since $d(u,v) \ge 1$ and $\sum_v d(v)^2 \ge (2m)^2/n$,

$$
\overline{\mathrm{Gr}} \le \frac{1}{\binom{n}{2}(n-1)} \sum_{u \lt v} d(u)d(v)
= \frac{(2m)^2 - \sum_v d(v)^2}{n(n-1)^2}
\le \frac{(2m)^2}{n^2(n-1)} \le \frac{n^2}{4(n-1)},
$$

   so $n/\overline{\mathrm{Gr}} \ge 4(n-1)/n$.
4. $\dfrac{6n}{n^2-1} \le \left(\dfrac{4(n-1)}{n}\right)^2$ is equivalent to $6n^3 \le 16(n-1)^3(n+1)$.
   Equality holds for $n = 2$, and for $n \ge 3$ we have $n - 1 \ge 2n/3$ and $n + 1 \ge 4$,
   so $16(n-1)^3(n+1) \ge 16 \cdot \frac{8}{27} n^3 \cdot 4 > 6n^3$. $\square$

*Remark.* If the mean gravity is taken over all $n^2$ entries, it is smaller by the factor $(n-1)/n$, so the bound still holds.

## Conjecture 219

> **219.** 2-nd largest eigenvalue of Gravity ≤ number of nonedges.
> (WOW p. 73, "Conjectures for triangle-free graphs (212:220)")

**Theorem.** This holds for every triangle-free graph with $n \ge 2$ vertices.

*Proof for $n \ge 9$.* Let $\theta_1 \ge \theta_2 \ge \dots$ be the eigenvalues of $\mathrm{Gr}$. If $\theta_2 \le 0$ there is nothing to prove.
Otherwise

$$
2\theta_2^2 \le \theta_1^2 + \theta_2^2 \le \sum_i \theta_i^2 = \sum_{u \ne v} \mathrm{Gr}_{uv}^2
\le \frac{1}{(n-1)^2} \sum_{u \ne v} d(u)^2 d(v)^2 \le \frac{1}{(n-1)^2} \left( \sum_v d(v)^2 \right)^2 .
$$

In a triangle-free graph adjacent vertices have disjoint neighbourhoods, so $d(u) + d(v) \le n$ for every edge $uv$, and
$\sum_v d(v)^2 = \sum_{uv \in E} (d(u) + d(v)) \le mn$. Hence $\theta_2 \le \dfrac{mn}{\sqrt{2}(n-1)}$, and it suffices to show

$$
m \left(1 + \frac{n}{\sqrt{2}(n-1)}\right) \le \binom{n}{2}.
$$

By Mantel's theorem $m \le \lfloor n^2/4 \rfloor$.
For $n = 9$ the left side is at most $20(1 + 9/(8\sqrt{2})) < 35.91 < 36$.
For $n \ge 10$, using $m \le n^2/4$, it suffices that $n^2 \le \sqrt{2}(n-1)(n-2)$;
this holds at $n = 10$ ($100 \le 101.8$), and $\sqrt{2}(n-1)(n-2) - n^2$ is increasing for $n \ge 10$.

*Proof for $2 \le n \le 8$.* By computer: `check_219_small.py` generates all 581 triangle-free graphs on 2 to 8 vertices
(up to isomorphism; the counts agree with OEIS A006785) and checks with exact rational arithmetic that
$\mathrm{Gr} - kI$, where $k$ is the number of nonedges, has at most one positive eigenvalue
(Descartes' rule of signs applied to its real-rooted characteristic polynomial). $\square$

## Scripts

| script | purpose | requires |
|---|---|---|
| `check_219_small.py` | the computer part of the proof of 219 (exact) | Python 3, networkx, numpy, sympy |
| `sanity_check.py` | numerical check of all five inequalities on all graphs with up to 7 vertices and 4000 random graphs (not part of the proofs) | Python 3, networkx, numpy |

## License

Code: MIT (see `LICENSE`). Text: CC BY 4.0.
