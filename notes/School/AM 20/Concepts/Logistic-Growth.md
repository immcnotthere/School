---
type: concept
title: "Logistic Growth"
course: "AM 20"
tags:
  - logistic
  - population
  - carrying-capacity
parent: "[[Math]]"
domain: math
status: draft
prereqs:
  - "[[Equilibrium Solution]]"
  - "[[Separable Equation]]"
retention_band: cold
---

# Logistic Growth

The ODE $y' = r\,y(K - y)$ models **logistic (bounded) population growth**:
- $r > 0$: intrinsic growth rate  
- $K > 0$: carrying capacity

## Equilibria
$y = 0$ (unstable) and $y = K$ (asymptotically stable).

## Behaviour
- $0 < y < K$: population grows toward $K$
- $y > K$: population declines toward $K$

In Example 1 of this lecture: $r = 0.05$, $K = 10$.

## Lecture slides
- Direction field: [[../slides/06-Example1-LogisticField]]
- Equilibria: [[../slides/14-Example1-Equilibria]]
