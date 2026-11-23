---
title: "Permutations, Falling Factorials, and No-Repeat Probabilities"
aliases:
  - "N P n"
  - "nPr"
  - "Falling factorial"
  - "No-collision probability"
  - "Birthday-style probability"
tags:
  - stat131
  - probability
  - counting
  - permutations
  - factorials
  - products
---

# Setup

You perform $n$ draws from $N$ equally likely labels.

- With replacement: each draw has $N$ choices, so total outcomes $N^n$.
- Event $A$: no repeats (all $n$ draws are distinct).

# Equivalent forms for the count of no-repeat sequences

Let the number of length-$n$ sequences with no repeats from $N$ labels be:

## Permutation notation

All of these mean the same count:
- $P(N,n)$
- ${}_NP_n$
- $N P n$ (plain-text style)
- “$N$ permute $n$”

## Factorial form

$$
P(N,n)=\frac{N!}{(N-n)!}.
$$

## Falling factorial form

Define the [[falling factorial]]:

$$
(N)_n := N(N-1)(N-2)\cdots(N-n+1).
$$

Then:

$$
P(N,n)=(N)_n.
$$

## Big-Pi product form

$$
P(N,n)=\prod_{k=0}^{n-1}(N-k).
$$

# Equivalent forms for the probability of no repeats (with replacement)

Total outcomes: $N^n$.

$$
\Pr(A)=\frac{P(N,n)}{N^n}.
$$

Substitute any equivalent form for $P(N,n)$:

## Factorial probability form

$$
\Pr(A)=\frac{N!}{(N-n)!\,N^n}.
$$

## Big-Pi probability form

$$
\Pr(A)=\frac{\prod_{k=0}^{n-1}(N-k)}{N^n}.
$$

## Product of fractions (most “probability-looking”)

$$
\Pr(A)=\prod_{k=0}^{n-1}\frac{N-k}{N}.
$$

Expanded:

$$
\Pr(A)=\frac{N}{N}\cdot\frac{N-1}{N}\cdot\frac{N-2}{N}\cdots\frac{N-n+1}{N}.
$$

# How to move between forms (mechanical rules)

## 1) Permutation ↔ factorial

$$
P(N,n)=\frac{N!}{(N-n)!}.
$$

## 2) Permutation ↔ falling factorial

$$
P(N,n)=(N)_n.
$$

## 3) Falling factorial ↔ big-Pi

$$
(N)_n=\prod_{k=0}^{n-1}(N-k).
$$

## 4) Count ↔ probability (with replacement)

$$
\Pr(A)=\frac{\#\text{favorable}}{\#\text{total}}=\frac{P(N,n)}{N^n}.
$$

## 5) Turning “count over $N^n$” into “product of fractions”

Start with:

$$
\Pr(A)=\frac{\prod_{k=0}^{n-1}(N-k)}{N^n}
$$

Then push the denominator inside the product:

$$
\Pr(A)=\prod_{k=0}^{n-1}\frac{N-k}{N}.
$$

# Specialization: your numbers

For $N=20$ and $n=12$:

$$
P(20,12)={}_{20}P_{12}=\frac{20!}{8!}=\prod_{k=0}^{11}(20-k).
$$

$$
\Pr(A)=\frac{{}_{20}P_{12}}{20^{12}}=\prod_{k=0}^{11}\frac{20-k}{20}.
$$

# Note on “$\Pr_{(N,n)}$” style notation

Some instructors write $\Pr_{(N,n)}$ to mean “the no-repeat probability for parameters $(N,n)$”.

A clean definition is:

$$
\Pr_{(N,n)} := \prod_{k=0}^{n-1}\frac{N-k}{N}=\frac{P(N,n)}{N^n}.
$$

# Related links

- [[Permutations nPr]]
- [[Combinations nCr]]
- [[Sampling with replacement]]
- [[Sampling without replacement]]
- [[Birthday problem]]
- [[Falling factorial]]
