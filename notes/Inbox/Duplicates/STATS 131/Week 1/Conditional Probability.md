---
title: Conditional Probability
aliases:
  - Definition of Conditional Probability
  - P(A | B)
tags:
  - probability
  - conditional
node_id: prob.rules.conditional.definition
mastery: 0
reps: 0
last_reviewed:
next_reviewed:
prereqs: []
related:
  - "[[Multiplication Rule (General)]]"
  - "[[Addition Rule (General)]]"
---

## Summary
$P(A\mid B)$ is the probability that $A$ occurs given that $B$ has occurred.

## Definition
For $P(B)>0$:
$$
P(A\mid B)=\frac{P(A\cap B)}{P(B)}
$$

## Rearrangements (useful identities)
From the definition:
$$
P(A\cap B)=P(A\mid B)\,P(B)
$$
Also:
$$
P(B\mid A)=\frac{P(A\cap B)}{P(A)} \quad \text{for } P(A)>0
$$

## Interpretation
Conditioning on $B$ restricts the sample space to outcomes in $B$.

## Example
If $P(A\cap B)=0.10$ and $P(B)=0.25$:
$$
P(A\mid B)=\frac{0.10}{0.25}=0.40
$$

## Common mistakes
- Dividing by $P(A)$ when you mean $P(A\mid B)$.
- Forgetting the condition $P(B)>0$.
