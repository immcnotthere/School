---
title: Inclusion-Exclusion (3 Events)
aliases:
  - Addition Rule (3 Events)
  - Inclusion-Exclusion Principle (3 events)
tags:
  - probability
  - sets
  - union
  - inclusion-exclusion
node_id: prob.rules.inclusion_exclusion.3
mastery: 0
reps: 0
last_reviewed:
next_reviewed:
prereqs:
  - "[[Addition Rule (General)]]"
related:
  - "[[Complement Rule and De Morgan]]"
---

## Summary
Probability of "at least one of $A,B,C$" while correcting for overlaps.

## Formula
$$
\begin{aligned}
P(A\cup B\cup C) =\ &P(A)+P(B)+P(C) \\
&-P(A\cap B)-P(A\cap C)-P(B\cap C) \\
&+P(A\cap B\cap C)
\end{aligned}
$$

## When to use
- You need $P(A\cup B\cup C)$.
- You have single probabilities and intersections.

## Intuition
Singles add, pair overlaps subtract, triple overlap add back.

## Common mistakes
- Forgetting $+P(A\cap B\cap C)$.
- Subtracting the triple intersection instead of adding it.
