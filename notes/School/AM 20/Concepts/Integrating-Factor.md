---
type: concept
title: "Integrating Factor"
course: "AM 20"
tags:
  - integrating factor
  - linear ODE
  - mu
  - product rule
parent: "[[Math]]"
domain: math
status: draft
prereqs:
  - "[[Canonical Form of a First-Order Linear ODE]]"
  - "[[Natural logarithm]]"
retention_band: cold
---

# Integrating Factor

The **integrating factor** for $y' - a(t)y = 0$ is
$$\mu(t) = e^{-A(t)}, \quad A'(t) = a(t)$$

Multiplying the ODE by $\mu(t)$ yields:
$$\bigl[\mu(t)\cdot y\bigr]' = 0 \implies \mu(t)\cdot y = C \implies y = Ce^{A(t)}$$

## Why it works
The product rule: $(\mu y)' = \mu y' + \mu' y$.  
We need $\mu' = -a(t)\mu$, which gives $\mu = e^{-A(t)}$.

## Generalisation (Friday)
For $y' + p(t)y = g(t)$, the integrating factor is $\mu = e^{\int p(t)\,dt}$, giving:
$$(\mu y)' = \mu g(t) \implies y = \frac{1}{\mu}\int \mu g(t)\,dt + C$$

## Lecture slides
- Derivation: [[../slides/27-IntegratingFactorMethod]]
- Terminology: [[../slides/28-Terminology-IntegratingFactor]]
- Example: [[../slides/29-Example-IVP]]
