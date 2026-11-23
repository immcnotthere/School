---
title: Addition Rule (General)
aliases:
  - General Addition Rule
  - Inclusion-Exclusion (2 events)
tags:
  - probability
  - sets
  - union
  - inclusion-exclusion
node_id: prob.rules.addition.general
mastery: 0
reps: 0
last_reviewed:
next_reviewed:
prereqs:
  - "[[STATS 131/Week 1/Conditional Probability]]"
related:
  - "[[Addition Rule (Disjoint)]]"
  - "[[Complement Rule and De Morgan]]"
  - "[[Inclusion-Exclusion (3 Events)]]"
---

## Summary
Use this for the probability of **$A$ or $B$** when the events may overlap.

## Formula
$$
P(A \cup B)=P(A)+P(B)-P(A\cap B)
$$

## When to use
- Problem says "or", "at least one", "either".
- You are not told $A$ and $B$ are disjoint.
- You have or can find $P(A\cap B)$.

## Intuition
$P(A)+P(B)$ counts outcomes in $A\cap B$ twice, so subtract $P(A\cap B)$ once.

## Example
Given $P(A)=0.60$, $P(B)=0.50$, $P(A\cap B)=0.20$:
$$
P(A\cup B)=0.60+0.50-0.20=0.90
$$

## Common mistakes
- Using $P(A)+P(B)$ without checking disjointness.
- Confusing $A\cap B$ with $A\cup B$.

## Quick checks
- Always true: $P(A\cup B)\le 1$
- Always true: $P(A\cup B)\ge \max(P(A),P(B))$
