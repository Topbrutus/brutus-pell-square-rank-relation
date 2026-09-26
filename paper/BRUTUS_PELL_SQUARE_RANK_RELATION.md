# Brutus-Pell Square-Rank Relation

**Gabriel St-Pierre**

Date: 2026-09-25

## Abstract

We record an explicit Pell rank-of-apparition family obtained from standard prime-power lifting and the least-common-multiple rule for coprime moduli.
Let `P_0=0`, `P_1=1`, and `P_{n+1}=2P_n+P_{n-1}`.
For `m>=1`, write `z_P(m)=min{n>=1 : m divides P_n}`.
Using `z_P(3)=4`, `z_P(7)=6`, and the ordinary Lucas prime-power lifting law at 3 and 7, one obtains

`z_P(21^k)=4*21^(k-1)` for every `k>=2`.

For odd `k=2r+1>=3`, this becomes the square-rank subfamily

`z_P(21^(2r+1))=(2*21^r)^2`.

The result is presented as a specialized explicit corollary of classical Lucas-sequence theory.

## 1. Definitions

The Pell sequence is the Lucas sequence `U_n(2,-1)`:

`P_0=0, P_1=1, P_{n+1}=2P_n+P_{n-1}`.

The rank of apparition of `m` is

`z_P(m)=min{n>=1 : m | P_n}`.

## 2. Two local ranks

Directly from the Pell sequence:

`P_4=12`, hence `z_P(3)=4` and `v_3(P_4)=1`.

`P_6=70`, hence `z_P(7)=6` and `v_7(P_6)=1`.

For a nondegenerate Lucas sequence, the standard prime-power rank-lifting theorem gives, when the first occurrence has p-adic valuation one,

`z_P(p^k)=p^(k-1) z_P(p)`.

Therefore

`z_P(3^k)=4*3^(k-1)`

and

`z_P(7^k)=6*7^(k-1)`

for every `k>=1`.

## 3. Coprime composition

For coprime positive integers `a,b`, the strong divisibility/rank property for Lucas sequences gives

`z_P(ab)=lcm(z_P(a),z_P(b))`.

Since `gcd(3^k,7^k)=1`,

`z_P(21^k)=lcm(4*3^(k-1), 6*7^(k-1))`.

For `k>=2`, the exponent of 3 in the first argument is at least one, so the least common multiple is

`4*3^(k-1)*7^(k-1)=4*21^(k-1)`.

Hence

**Theorem.** For every integer `k>=2`,

`z_P(21^k)=4*21^(k-1)`.

## 4. Square-rank subfamily

Let `k=2r+1` with `r>=1`. Then

`z_P(21^(2r+1)) = 4*21^(2r)`

`= (2*21^r)^2`.

Thus every odd exponent at least three gives an exact square rank.

Examples:

- `z_P(21^3)=1764=42^2`.
- `z_P(21^5)=777924=882^2`.

The boundary case `k=1` is different:

`z_P(21)=lcm(4,6)=12`,

so the formula `4*21^(k-1)` intentionally begins at `k=2`.

## 5. Relation to 1,203,930

`1,203,930 = 130*21^3`.

The previously observed square rank `1764=42^2` for that composite is compatible with the `21^3` component, but extending a rank unchanged after multiplication by another factor requires the corresponding least-common-multiple conditions.
That extension must therefore be checked separately rather than inferred from the square-rank family alone.

## 6. Prior-art position

The general machinery used here is classical: ranks of apparition, strong divisibility, and prime-power lifting for Lucas sequences.
Ray, Irmak and Patel (2018) treat ranks of apparition of powers in nondegenerate Lucas sequences and explicitly build on p-adic valuation formulas.
Lehmer (1930) is a foundational source for Lucas-function divisibility theory.

This note does **not** claim novelty for the general lifting theorem.
Its purpose is to isolate and document the explicit Pell specialization at `21^k`, especially the square-rank odd-exponent subfamily.

## 7. Reproducibility

The companion script `scripts/verify_family.py` verifies the local ranks, computes the predicted formula, and checks modular divisibility for a configurable finite range.

## References

1. D. H. Lehmer, *An Extended Theory of Lucas' Functions*, Annals of Mathematics 31(3), 419-448 (1930). DOI: 10.2307/1968235.
2. P. K. Ray, N. Irmak, B. K. Patel, *The rank of apparition of powers of Lucas sequence*, Turkish Journal of Mathematics 42(4), 1566-1570 (2018). DOI: 10.3906/mat-1705-116.

## Citation status

Author: Gabriel St-Pierre.
Suggested title: **Brutus-Pell Square-Rank Relation**.
Keywords: Pell sequence; rank of apparition; Lucas sequence; modular arithmetic; divisibility; prime-power lifting; Brutus-Pell.
