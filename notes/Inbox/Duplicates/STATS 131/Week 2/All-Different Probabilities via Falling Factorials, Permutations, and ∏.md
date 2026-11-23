---
title: "All-Different Probabilities via Falling Factorials, Permutations, and ∏"
aliases:
  - "birthday problem method"
  - "all distinct probability"
  - "falling factorial probability"
  - "P(n,k) over n^k"
tags:
  - stat131
  - probability
  - counting
  - permutations
  - birthday-problem
---

:contentReference[oaicite:0]{index=0}

# Core idea

When you sample **k times** from **n equally likely labels** (birthdays, die faces, people, etc.), the probability that **all k outcomes are different** is

$$
\Pr(\text{all distinct})=\frac{n(n-1)(n-2)\cdots(n-k+1)}{n^k}
=\frac{P(n,k)}{n^k}
=\prod_{i=0}^{k-1}\frac{n-i}{n}.
$$

Where the **permutation count** (ordered, no repeats) is

$$
P(n,k)=n\cdot(n-1)\cdots(n-k+1)=\frac{n!}{(n-k)!}.
$$

---

# Why the denominator is usually $n^k$

## Case A: Ordered draws, with replacement (repeats allowed)
- Example: roll a die k times, or pick a random birthday k times.
- Each draw has n options, independent.
- Total outcomes:  
$$
n^k.
$$

---

# Why the numerator becomes a “falling product”

## Case B: Ordered draws, without replacement (no repeats)
To have all distinct:
- 1st draw: n choices
- 2nd draw: n−1 choices
- …
- kth draw: n−(k−1) choices

So favorable outcomes:
$$
n(n-1)\cdots(n-k+1)=P(n,k)=\frac{n!}{(n-k)!}.
$$

---

# Product (big-∏) form

You can write the probability directly as a chain of conditional probabilities:

$$
\Pr(\text{all distinct})
=\Pr(X_2\neq X_1)\Pr(X_3\neq X_1,X_2)\cdots\Pr(X_k\neq X_1,\dots,X_{k-1})
$$

For uniform draws from n labels (with replacement), each factor is:
$$
\Pr(X_j\notin\{X_1,\dots,X_{j-1}\})=\frac{n-(j-1)}{n}.
$$

So:
$$
\Pr(\text{all distinct})=\prod_{j=1}^{k}\frac{n-(j-1)}{n}
=\prod_{i=0}^{k-1}\frac{n-i}{n}.
$$

---

# “Pr(20,12)” notation you were told

Often people write:
- $P(20,12)$ or $\Pr(20,12)$ meaning “20 permute 12”:

$$
P(20,12)=\frac{20!}{(20-12)!}=\frac{20!}{8!}.
$$

Then:
$$
\Pr(\text{all distinct in 12 draws from 20})=\frac{P(20,12)}{20^{12}}
=\frac{20!}{8!\,20^{12}}
=\prod_{i=0}^{11}\frac{20-i}{20}.
$$

---

# Worked example: 3 dice (all different)

Here n=6 faces, k=3 rolls.

- Total outcomes: $6^3$.
- Favorable: $6\cdot5\cdot4=P(6,3)=\frac{6!}{3!}$.

So:
$$
\Pr(\text{all different})=\frac{6\cdot5\cdot4}{6^3}=\frac{120}{216}=\frac{5}{9}\approx0.5556.
$$

Product form:
$$
\frac{6}{6}\cdot\frac{5}{6}\cdot\frac{4}{6}.
$$

---

# Birthday problem (standard form)

With n=365 days, k people:

$$
\Pr(\text{no shared birthdays})
=\frac{P(365,k)}{365^k}
=\prod_{i=0}^{k-1}\frac{365-i}{365}.
$$

The “at least one match” version is the complement:

$$
\Pr(\text{at least one shared birthday})
=1-\Pr(\text{no shared birthdays}).
$$

---

# Quick “which counting object?” checklist

## 1) Order matters?
- Yes → permutations / $P(n,k)$ or powers $n^k$.
- No → combinations / $\binom{n}{k}$.

## 2) Replacement allowed?
- Yes → repeats allowed → often $n^k$ (if ordered).
- No → no repeats → falling product $n(n-1)\cdots$.

## 3) Probability of “all distinct” in repeated uniform draws
Almost always:
$$
\frac{P(n,k)}{n^k}=\prod_{i=0}^{k-1}\frac{n-i}{n}.
$$

---

# Mini examples to recognize patterns

## Example 1: “Pick 5 cards from 52, what is probability all 5 are different ranks?”
This is NOT the plain birthday setup because the sample space is not “52 equally likely ranks”; the labels (ranks) have multiplicities. Use combinations with counting by rank patterns.

## Example 2: “Random 12-digit code where each digit is 0–9, probability all digits distinct”
Here n=10, k=12, but k>n so probability = 0.

---

# Notation recap

- **Power**: $n^k$ (ordered, with replacement)
- **Permutation**: $P(n,k)=\dfrac{n!}{(n-k)!}$ (ordered, without replacement)
- **Combination**: $\binom{n}{k}=\dfrac{n!}{k!(n-k)!}$ (unordered, without replacement)
- **All-distinct probability** (birthday-style):
$$
\frac{P(n,k)}{n^k}=\prod_{i=0}^{k-1}\frac{n-i}{n}.
$$
