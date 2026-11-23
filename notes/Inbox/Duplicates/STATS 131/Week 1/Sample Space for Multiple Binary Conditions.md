---
title: Sample Space for Multiple Binary Conditions
aliases:
  - Product Sample Space (Binary)
  - Joint Outcomes for Multiple Events
tags:
  - probability
  - sample-space
  - sets
  - modeling
node_id: prob.modeling.sample_space.binary_product
mastery: 0
reps: 0
last_reviewed:
next_reviewed:
prereqs:
  - "[[Formal Set Notation for Probability]]"
related:
  - "[[STATS 131/Week 1/Conditional Probability]]"
  - "[[Addition Rule (General)]]"
  - "[[Multiplication Rule (General)]]"
---

Summary
When a situation is described by several yes/no attributes (conditions, features, test results), model each attribute as a binary variable and define the sample space as all combinations. This creates a complete, mutually exclusive list of outcomes.

Core idea
Suppose there are $n$ binary attributes. For each attribute $i$, define an indicator variable:
$$
X_i\in\{0,1\}
$$
where $X_i=1$ means "attribute $i$ is present" and $X_i=0$ means "attribute $i$ is absent".

Sample space (binary product space)
The sample space is the Cartesian product:
$$
\Omega=\{0,1\}^n=\{(x_1,\dots,x_n): x_i\in\{0,1\}\ \text{for all }i\}
$$
Number of outcomes:
$$
|\Omega|=2^n
$$

Outcome meaning
Each outcome $\omega=(x_1,\dots,x_n)$ is one complete scenario specifying presence/absence for every attribute.

Event sets from indicators
For attribute $i$, the event that attribute $i$ is present is:
$$
A_i=\{\omega\in\Omega:\ x_i=1\}
$$
The event that attribute $i$ is absent is:
$$
A_i^c=\{\omega\in\Omega:\ x_i=0\}
$$

Joint events
For a subset $S\subseteq\{1,\dots,n\}$, the event that all attributes in $S$ are present is:
$$
\bigcap_{i\in S} A_i=\{\omega\in\Omega:\ x_i=1\ \text{for all } i\in S\}
$$
If you also want all attributes in $T$ absent (where $S\cap T=\varnothing$):
$$
\left(\bigcap_{i\in S} A_i\right)\cap\left(\bigcap_{j\in T} A_j^c\right)
=\{\omega\in\Omega:\ x_i=1\ \forall i\in S,\ x_j=0\ \forall j\in T\}
$$

Exactly one, at least one, none (general forms)
At least one of the $n$ attributes occurs:
$$
\bigcup_{i=1}^n A_i
$$
None occur:
$$
\left(\bigcup_{i=1}^n A_i\right)^c=\bigcap_{i=1}^n A_i^c
$$
Exactly one occurs:
$$
\bigcup_{k=1}^n \left(A_k \cap \bigcap_{i\ne k} A_i^c\right)
$$

Partition property
The outcomes in $\Omega$ are mutually exclusive and collectively exhaustive:
- Mutually exclusive: distinct $\omega,\omega'\in\Omega$ cannot both occur
- Exhaustive: exactly one $\omega\in\Omega$ occurs each trial

This implies any event $E\subseteq\Omega$ can be expressed as a union of disjoint singleton outcomes:
$$
E=\bigcup_{\omega\in E}\{\omega\}
$$

Where probabilities enter (without assuming a specific model)
A probability model assigns a probability measure $P$ on subsets of $\Omega$:
$$
P:\mathcal{F}\to[0,1],\quad \mathcal{F}\subseteq 2^\Omega
$$
Typically for finite $\Omega$, you can take $\mathcal{F}=2^\Omega$ and require:
- $P(\Omega)=1$
- If $E_1,E_2$ are disjoint, then $P(E_1\cup E_2)=P(E_1)+P(E_2)$

Notes and common pitfalls
- Do not assume independence unless stated; the sample space construction does not imply independence.
- Keep outcomes exclusive: each $\omega$ is one complete configuration.
- Use indicator definitions consistently: decide what $1$ and $0$ mean and do not flip them across notes.
