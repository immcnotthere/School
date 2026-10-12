---
title: Exactly One of A, B
aliases:
  - XOR Probability (Two Events)
  - Exclusive OR Probability
tags:
  - probability
  - sets
  - xor
node_id: prob.rules.exactly_one.2
mastery: 0
reps: 0
last_reviewed:
next_reviewed:
prereqs:
  - "[[Addition Rule (General)]]"
related:
  - "[[Addition Rule (Disjoint)]]"
---

## Summary
"Exactly one" means one happens and the other does not.

## Event form
$$
(A\cap B^c)\cup(A^c\cap B)
$$

## Formulas
Disjoint sum form:
$$
P(\text{exactly one})=P(A\cap B^c)+P(A^c\cap B)
$$

Overlap form:
$$
P(\text{exactly one})=P(A)+P(B)-2P(A\cap B)
$$

## Example
If $P(A)=0.60$, $P(B)=0.50$, $P(A\cap B)=0.20$:
$$
P(\text{exactly one})=0.60+0.50-2(0.20)=0.70
$$

## Common mistakes
- Confusing "exactly one" with "at least one" ($A\cup B$).
- Forgetting the factor $2$ on $P(A\cap B)$.
