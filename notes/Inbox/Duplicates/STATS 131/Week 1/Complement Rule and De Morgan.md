---
title: Complement Rule and De Morgan
aliases:
  - De Morgan's Laws (Probability)
  - At Least One via Complement
tags:
  - probability
  - sets
  - complement
  - de-morgan
node_id: prob.rules.complement.demorgan
mastery: 0
reps: 0
last_reviewed:
next_reviewed:
prereqs: []
related:
  - "[[Neither A nor B]]"
  - "[[Addition Rule (General)]]"
---

## Summary
Convert "not", "at least one", and "neither" statements into easier probabilities.

## Complement rule
For any event $E$:
$$
P(E^c)=1-P(E)
$$

## De Morgan's laws
$$
(A\cup B)^c = A^c\cap B^c
$$
$$
(A\cap B)^c = A^c\cup B^c
$$

## At least one (two events)
"At least one of $A$ or $B$" is $A\cup B$:
$$
P(A\cup B)=1-P(A^c\cap B^c)
$$

## Example
If $P(A^c\cap B^c)=0.35$, then:
$$
P(A\cup B)=1-0.35=0.65
$$

## Common mistakes
- Swapping $\cap$ and $\cup$ when taking complements.
- Treating $A^c\cap B^c$ as "not A or not B" (it is "not A and not B").
