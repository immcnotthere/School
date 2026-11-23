---
title: Multiplication Rule (General)
aliases:
  - General Product Rule
  - AND Rule (General)
tags:
  - probability
  - conditional
  - intersection
node_id: prob.rules.multiplication.general
mastery: 0
reps: 0
last_reviewed:
next_reviewed:
prereqs:
  - "[[STATS 131/Week 1/Conditional Probability]]"
related:
  - "[[Multiplication Rule (Independent)]]"
  - "[[Addition Rule (General)]]"
---

## Summary
Use this for probabilities of **$A$ and $B$**.

## Formula
$$
P(A\cap B)=P(A)\,P(B\mid A)
$$
Equivalently:
$$
P(A\cap B)=P(B)\,P(A\mid B)
$$

## When to use
- You see "and", "both", "together".
- You can compute a conditional probability like $P(B\mid A)$.

## Example
If $P(A)=0.30$ and $P(B\mid A)=0.40$:
$$
P(A\cap B)=0.30\cdot 0.40=0.12
$$

## Common mistakes
- Replacing $P(B\mid A)$ with $P(B)$ without independence.
- Conditioning on the wrong event.
