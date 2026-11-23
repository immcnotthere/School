---
title: Addition Rule (Disjoint)
aliases:
  - Disjoint Addition Rule
  - Mutually Exclusive Addition Rule
tags:
  - probability
  - sets
  - union
  - disjoint
node_id: prob.rules.addition.disjoint
mastery: 0
reps: 0
last_reviewed:
next_reviewed:
prereqs:
  - "[[Addition Rule (General)]]"
related:
  - "[[Exactly One of A, B]]"
---

## Summary
Use this when $A$ and $B$ cannot happen together.

## Condition
$$
A\cap B=\varnothing \quad \text{(mutually exclusive)}
$$

## Formula
$$
P(A\cup B)=P(A)+P(B)
$$

## Example
If $P(A)=0.40$, $P(B)=0.20$, and $A\cap B=\varnothing$:
$$
P(A\cup B)=0.60
$$

## Common mistakes
- Assuming disjoint without being told.
- Confusing disjoint with independent.

## Notes
If $A$ and $B$ are disjoint and both have positive probability, then they are not independent because $P(A\cap B)=0$ but $P(A)P(B)>0$.
