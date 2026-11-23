---
title: Permutation count notation
aliases:
  - Permutations (counting)
  - nPr notation
  - nP r notation
  - Falling factorial (as a count)
tags:
  - math
  - counting
  - permutations
  - combinatorics
  - probability
---

# Permutation count notation

## Core definition

### [[Permutation count]] (ordered selection without replacement)
The permutation count is the number of ways to choose and arrange $r$ distinct items from $n$ distinct items (order matters, no repeats).

Common notations (all mean the same thing):
- $P(n,r)$
- $nP_r$
- ${}_nP_r$
- $nPr$

Value:
$$P(n,r)=nP_r={}_nP_r=\frac{n!}{(n-r)!}.$$

Equivalent product (the “decreasing choices” form):
$$P(n,r)=n(n-1)(n-2)\cdots(n-r+1).$$

---

## How to read it

- $P(n,r)$: “permutations of size $r$ from $n$”
- $\frac{n!}{(n-r)!}$: “all orderings of $n$, but ignore the tail after choosing $r$ items”
- $n(n-1)\cdots(n-r+1)$: “$n$ choices for the first slot, $n-1$ for the second, …”

---

## When to use it

Use a permutation count when:
- you are building an **ordered list** of length $r$ from $n$ options, and
- repeats are **not allowed** (“without replacement,” “distinct,” “at most one per box”).

Typical stories:
- Assign $r$ labeled balls to $r$ distinct boxes chosen from $n$ boxes.
- Arrange $r$ students in $r$ distinct seats chosen from $n$ seats.
- Choose a president/VP/secretary from a group (roles make order matter).

---

## Connection to probability

Many probability problems are:
$$\Pr(A)=\frac{\#\text{ favorable outcomes}}{\#\text{ total outcomes}}.$$

If “favorable outcomes” require all choices to be distinct and ordered, the numerator is often a permutation count.

Example (12 labeled balls into 20 labeled boxes, no box gets more than one ball):
- Favorable outcomes: $P(20,12)=\frac{20!}{8!}$
- Total outcomes: $20^{12}$
- Probability:
$$\Pr(A)=\frac{P(20,12)}{20^{12}}.$$

---

## Product notation form (big Pi)

Permutation counts can be written with $\prod$:

$$P(n,r)=\prod_{j=0}^{r-1}(n-j).$$

Read: “multiply $(n-j)$ as $j$ goes from $0$ to $r-1$.”

Example:
$$P(20,12)=\prod_{j=0}^{11}(20-j).$$

---

## Neighboring terms

### [[Combination]] vs [[Permutation count]]
- Combination (order does not matter):
$$\binom{n}{r}=\frac{n!}{r!(n-r)!}.$$
- Permutation count (order matters):
$$P(n,r)=\frac{n!}{(n-r)!}.$$

Relationship:
$$P(n,r)=\binom{n}{r}\,r!.$$
(Choose the $r$ items, then arrange them.)

### [[Factorial cancellation identity]]
The factorial ratio form uses cancellation:
$$\frac{n!}{(n-r)!}=n(n-1)\cdots(n-r+1).$$

---

## Quick checklist

1. Are you selecting $r$ items from $n$?
2. Does **order matter** (roles, positions, labeled balls)?
3. Are repeats forbidden (“distinct,” “without replacement”)?

If yes to all 3, use:
$$P(n,r)=\frac{n!}{(n-r)!}.$$

---

## Related links
- [[Factorial]]
- [[Factorial cancellation identity]]
- [[Falling factorial]]
- [[Combination]]
- [[Binomial coefficient]]
- [[Counting]]
- [[Sample space]]

