---
title: Formal Set Notation for Probability
aliases:
  - Set Notation (Events)
  - Event Algebra Basics
tags:
  - probability
  - sets
  - notation
node_id: prob.sets.notation.formal
mastery: 0
reps: 0
last_reviewed:
next_reviewed:
prereqs: []
related:
  - "[[Complement Rule and De Morgan]]"
  - "[[Addition Rule (General)]]"
  - "[[Multiplication Rule (General)]]"
---

Summary
Events are sets. Use a universe (sample space) $\Omega$. Events $A,B$ satisfy $A,B\subseteq \Omega$.

Universe and membership
- Universe (sample space): $\Omega$
- Element: $x\in\Omega$
- Membership: $x\in A$ (in $A$), $x\notin A$ (not in $A$)

Union
Meaning: $A$ or $B$
$$
A\cup B=\{x\in\Omega:\; x\in A\ \lor\ x\in B\}
$$

Intersection
Meaning: $A$ and $B$
$$
A\cap B=\{x\in\Omega:\; x\in A\ \land\ x\in B\}
$$

Complement
Meaning: not $A$
$$
A^c=\Omega\setminus A=\{x\in\Omega:\; x\notin A\}
$$

Set difference
Meaning: in $A$ but not in $B$
$$
A\setminus B=\{x\in\Omega:\; x\in A\ \land\ x\notin B\}=A\cap B^c
$$

Empty set
Meaning: impossible event
$$
\varnothing=\{x\in\Omega:\; \text{false}\}
$$

Disjoint (mutually exclusive)
Meaning: cannot both occur
$$
A\cap B=\varnothing
$$

Key decomposition (partition of $A$ by $B$)
This is used to derive identities like $P(A\cap B^c)=P(A)-P(A\cap B)$.
$$
A=(A\cap B)\ \cup\ (A\cap B^c)
$$
and it is a disjoint union:
$$
(A\cap B)\cap(A\cap B^c)=\varnothing
$$

De Morgan's laws
$$
(A\cup B)^c=A^c\cap B^c
$$
$$
(A\cap B)^c=A^c\cup B^c
$$

Quick translations (English to sets)
- "A or B": $A\cup B$
- "A and B": $A\cap B$
- "not A": $A^c$
- "A but not B": $A\cap B^c$
- "neither A nor B": $A^c\cap B^c$
- "at least one of A,B": $A\cup B$
- "exactly one of A,B": $(A\cap B^c)\cup(A^c\cap B)$

Common mistakes
- Treating "neither A nor B" as $A^c\cup B^c$ (incorrect)
- Forgetting complements switch union and intersection under $^c$ (De Morgan)
