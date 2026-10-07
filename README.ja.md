# Graffiti 予想 198, 219, 252, 254, 712 の証明

[English](README.md)

木村心（Shin Kimura）、2026-10-07

予想は S. Fajtlowicz『Written on the Wall』（2004 年 7 月版）[WOW] のもの。
用語は T. L. Brewster, M. J. Dinneen, V. Faber,
"A computational attack on the conjectures of Graffiti: New counterexamples and proofs",
Discrete Math. 147 (1995) 35–55 [BDF] の用語集の定義に従う。

## 記号と定義

$G$ は頂点数 $n$、辺数 $m$ の単純グラフ。$d(v)$ は頂点 $v$ の次数、$\delta$ は最小次数、$d(u,v)$ は距離。
$A$ は隣接行列、$L = \mathrm{Deg} - A$ はラプラシアンで、その固有値を $0 = \mu_1 \le \mu_2 \le \dots \le \mu_n$ とする。
断りのない「固有値」は $A$ の固有値を指す。

- ベクトル $V$ の **derivative** [BDF p. 52]：$V$ を小さい順に並べ、$V'(i) = V(i+1) - V(i)$ とおいたもの。
  成分が $n \ge 2$ 個のとき、その最小値は「並べたときの隣どうしの差」の最小値である。
- **Even** と **Odd** [BDF pp. 52, 54]：$\mathrm{Even}(v)$ は $v$ から偶数の距離にある頂点の数（$v$ 自身を含む）、
  $\mathrm{Odd}(v)$ は奇数の距離にある頂点の数。
- **双対次数（dual degree）** [WOW p. 76]：$d^*(v)$ は $v$ の隣接頂点の次数の平均。
- **temperature** [BDF p. 54]：$t(v) = d(v)/(n - d(v))$。
- **重力行列（gravity matrix）** [BDF p. 53]：$u \ne v$ が同じ連結成分にあれば $\mathrm{Gr}_{uv} = \dfrac{d(u)d(v)}{(n-1) d(u,v)}$、
  それ以外は $0$。**mean gravity** $\overline{\mathrm{Gr}}$ は、対角より上の成分の平均 [BDF p. 52]。
- **非辺（nonedge）** [BDF p. 53]：隣接していない 2 頂点の組。全部で $\binom{n}{2} - m$ 個ある。

## 2 つの補題

**補題 1.** $n \ge 2$ として $x_1 \le \dots \le x_n$ とし、$g = \min_i (x_{i+1} - x_i)$、平均を $\bar{x}$ とする。このとき

(a) $g \le \dfrac{x_n - x_1}{n-1}$,

(b) $\displaystyle\sum_i (x_i - \bar{x})^2 \ge \frac{g^2 n (n^2 - 1)}{12}$.

*証明.* (a) $n-1$ 個の差を足すと $x_n - x_1$ になる。
(b) $\sum_{i \lt j} (x_j - x_i)^2 = n \sum_i (x_i - \bar{x})^2$ であり、$x_j - x_i \ge (j-i) g \ge 0$ である。よって

$$
n \sum_i (x_i - \bar{x})^2 \ge g^2 \sum_{i \lt j} (j-i)^2 = g^2 \cdot n \sum_{i=1}^{n} \left(i - \frac{n+1}{2}\right)^2 = g^2 \cdot \frac{n^2 (n^2-1)}{12}.
$$

**補題 2.** $\mu_n \le n$.

*証明.* $L(G) + L(\overline{G}) = nI - J$ が成り立つ。全成分 1 のベクトルは $L(G)$ の固有ベクトルなので、
ほかの固有ベクトルはこれと直交するようにとれる。そのような $x$ で $L(G)x = \mu x$ とすると $L(\overline{G})x = (n - \mu)x$ となり、
$L(\overline{G})$ は半正定値なので $\mu \le n$.

## 予想 252

> **252.** ラプラシアンの固有値の derivative の最小値 ≤ 双対次数の逆数の和。
> （WOW p. 76、「任意のグラフについての予想（246 : 274）」）

**定理.** 頂点数 $n \ge 2$ で孤立点のないすべてのグラフで成り立つ。

*証明.* $G$ が非連結なら、$0$ がラプラシアンの重複度 $2$ 以上の固有値なので、左辺は $0$、右辺は正である。
$G$ が連結なら、補題 1(a) と補題 2 より

$$
\min_i (\mu_{i+1} - \mu_i) \le \frac{\mu_n - \mu_1}{n-1} \le \frac{n}{n-1}.
$$

各 $d^*(v)$ は次数の平均なので $0 < d^*(v) \le n - 1$ であり、$\sum_v 1/d^*(v) \ge n/(n-1)$. $\square$

## 予想 254

> **254.** ラプラシアンの固有値の derivative の最小値 ≤ Odd の逆数の和。
> （WOW p. 77、同じ節）

**定理.** 頂点数 $n \ge 2$ のすべての連結グラフで成り立つ
（右辺が定義される非連結グラフでも成り立つ。そのとき左辺は $0$ だから）。

*証明.* 連結グラフでは、どの頂点にも隣接頂点があり（奇数の距離 $1$）、頂点自身は偶数の距離 $0$ にある。
よって $1 \le \mathrm{Odd}(v) \le n - 1$ であり、$\sum_v 1/\mathrm{Odd}(v) \ge n/(n-1)$。
左辺が $n/(n-1)$ 以下であることは 252 の証明と同じ。$\square$

## 予想 712

> **712.** temperature の最小値 ≤ 0 以下の固有値の個数。
> （WOW p. 105）

**定理.** すべてのグラフで成り立つ。

*証明.* temperature は次数について増加なので、その最小値は $\delta/(n - \delta)$ である。
補グラフ $\overline{G}$ の最大次数は $n - 1 - \delta$ なので、$\overline{G}$ には大きさ $n/(n - \delta)$ 以上の独立集合がある
（頂点を 1 つ選び、その頂点と高々 $n - 1 - \delta$ 個の隣接頂点を消す操作を繰り返す）。
これは $G$ のクリークなので、クリーク数は $\omega \ge n/(n - \delta)$ を満たす。
最大クリーク上の $A$ の主小行列は $J - I$ で、固有値は $\omega - 1$ と $-1$（重複度 $\omega - 1$）。
コーシーのインターレース定理より、$A$ には $-1$ 以下の固有値が $\omega - 1$ 個以上ある。
0 以下の固有値の個数を $N_{\le 0}$ と書くと

$$
N_{\le 0} \ge \omega - 1 \ge \frac{n}{n-\delta} - 1 = \frac{\delta}{n-\delta}. \qquad \square
$$

完全グラフで等号が成り立つ。

## 予想 198

> **198.** 固有値の derivative の最小値 ≤ n / mean gravity。
> （WOW p. 71、「D の成分の和が E の成分の和以下である連結グラフについての予想（181:204）」。
> E と D は予想 96 の Even と Odd）

**定理.** 頂点数 $n \ge 2$ で $\sum_v \mathrm{Odd}(v) \le \sum_v \mathrm{Even}(v)$ を満たすすべての連結グラフについて

$$
\min_i (\lambda_{i+1} - \lambda_i) \le \sqrt{\frac{6n}{n^2-1}} \le \frac{4(n-1)}{n} \le \frac{n}{\overline{\mathrm{Gr}}}.
$$

*証明.* 左辺を $g$ とおく。

1. 順序つきの組 $(v, u)$ は、それぞれ $\mathrm{Odd}(v)$ か $\mathrm{Even}(v)$ のどちらか一方でちょうど 1 回数えられるので、
   $\sum_v (\mathrm{Odd}(v) + \mathrm{Even}(v)) = n^2$。仮定より $\sum_v \mathrm{Odd}(v) \le n^2/2$。
   $v$ の隣接頂点は距離 $1$ にあるので $\mathrm{Odd}(v) \ge d(v)$ であり、$2m \le n^2/2$。
2. $A$ の固有値の平均は $0$ で、$\sum_i \lambda_i^2 = 2m$。補題 1(b) より
   $g^2 n(n^2-1)/12 \le 2m \le n^2/2$ なので、$g \le \sqrt{6n/(n^2-1)}$。
3. $d(u,v) \ge 1$ と $\sum_v d(v)^2 \ge (2m)^2/n$ より

$$
\overline{\mathrm{Gr}} \le \frac{1}{\binom{n}{2}(n-1)} \sum_{u \lt v} d(u)d(v)
= \frac{(2m)^2 - \sum_v d(v)^2}{n(n-1)^2}
\le \frac{(2m)^2}{n^2(n-1)} \le \frac{n^2}{4(n-1)},
$$

   よって $n/\overline{\mathrm{Gr}} \ge 4(n-1)/n$。
4. $\dfrac{6n}{n^2-1} \le \left(\dfrac{4(n-1)}{n}\right)^2$ は $6n^3 \le 16(n-1)^3(n+1)$ と同値である。
   $n = 2$ で等号が成り立ち、$n \ge 3$ では $n - 1 \ge 2n/3$ かつ $n + 1 \ge 4$ なので
   $16(n-1)^3(n+1) \ge 16 \cdot \frac{8}{27} n^3 \cdot 4 > 6n^3$。$\square$

*注.* mean gravity を $n^2$ 個すべての成分の平均とすると、値は $(n-1)/n$ 倍に小さくなるので、この評価はそのまま成り立つ。

## 予想 219

> **219.** 重力行列の 2 番目に大きい固有値 ≤ 非辺の数。
> （WOW p. 73、「三角形を含まないグラフについての予想（212:220）」）

**定理.** 頂点数 $n \ge 2$ の三角形を含まないすべてのグラフで成り立つ。

*$n \ge 9$ の証明.* $\mathrm{Gr}$ の固有値を $\theta_1 \ge \theta_2 \ge \dots$ とする。$\theta_2 \le 0$ なら示すことはない。
そうでなければ

$$
2\theta_2^2 \le \theta_1^2 + \theta_2^2 \le \sum_i \theta_i^2 = \sum_{u \ne v} \mathrm{Gr}_{uv}^2
\le \frac{1}{(n-1)^2} \sum_{u \ne v} d(u)^2 d(v)^2 \le \frac{1}{(n-1)^2} \left( \sum_v d(v)^2 \right)^2 .
$$

三角形を含まないグラフでは、隣接する 2 頂点の近傍は交わらないので、すべての辺 $uv$ で $d(u) + d(v) \le n$ となり、
$\sum_v d(v)^2 = \sum_{uv \in E} (d(u) + d(v)) \le mn$。よって $\theta_2 \le \dfrac{mn}{\sqrt{2}(n-1)}$ であり、次を示せば十分：

$$
m \left(1 + \frac{n}{\sqrt{2}(n-1)}\right) \le \binom{n}{2}.
$$

Mantel の定理より $m \le \lfloor n^2/4 \rfloor$。
$n = 9$ のとき、左辺は $20(1 + 9/(8\sqrt{2})) < 35.91 < 36$ で抑えられる。
$n \ge 10$ のときは $m \le n^2/4$ を使うと、$n^2 \le \sqrt{2}(n-1)(n-2)$ を示せば十分である。
これは $n = 10$ で成り立ち（$100 \le 101.8$）、$\sqrt{2}(n-1)(n-2) - n^2$ は $n \ge 10$ で増加する。

*$2 \le n \le 8$ の証明.* 計算機による：`check_219_small.py` は 2〜8 頂点の三角形を含まないグラフ 581 個
（同型を除く。個数は OEIS A006785 と一致）をすべて生成し、非辺の数を $k$ として、
$\mathrm{Gr} - kI$ の正の固有値が高々 1 個であることを厳密な有理数演算で確かめる
（実根のみをもつ特性多項式にデカルトの符号法則を使う）。$\square$

## スクリプト

| スクリプト | 目的 | 必要なもの |
|---|---|---|
| `check_219_small.py` | 219 の証明の計算機部分（厳密計算） | Python 3、networkx、numpy、sympy |
| `sanity_check.py` | 7 頂点以下のすべてのグラフとランダムグラフ 4000 個で 5 つの不等式を数値的に確かめる（証明の一部ではない） | Python 3、networkx、numpy |

## ライセンス

コード：MIT（`LICENSE` を参照）。文章：CC BY 4.0。
