---
parent: "[[AM20]]"
type: concept
title: "Existence and Uniqueness"
course: "AM 20"
tags:
  - existence
  - uniqueness
  - IVP
  - non-intersection
domain: math
status: draft
prereqs:
  - "[[Initial Value Problem]]"
retention_band: cold
---

# Existence and Uniqueness Theorem

Under regularity conditions on $f(t,y)$ (e.g. $f$ and $\partial f/\partial y$ continuous), the IVP
$$y' = f(t,y), \quad y(t_0) = y_0$$
has a **unique solution** on some interval around $t_0$.

## Consequences
1. **Solutions never intersect** — two distinct solution curves cannot meet.
2. **Equilibrium lines trap solutions** — a solution between two equilibria stays there.
3. **Non-tangency** — distinct solutions cannot be tangent to each other either.

## Why it matters for direction fields
Every arrow in the slope field belongs to exactly *one* solution curve.

## Lecture slides
- Preview: [[../slides/15-ExistenceUniqueness-NonIntersection]]
- Trapping argument: [[../slides/17-Example3-Trapping]]
