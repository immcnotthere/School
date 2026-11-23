---
title: "Vector Space"
aliases:
  - vector space
  - linear space
topic: "Linear Algebra / Differential Equations"
course: "AM 20"
tags:
  - am20
  - linear-algebra
  - odes
  - vector-space
type: concept
related:
  - "[[Superposition Principle]]"
  - "[[Linear Independence]]"
  - "[[Fundamental Solutions]]"
  - "[[Homogeneous Linear ODE]]"
status: draft
---

# Vector Space

---

## Definition

> A **vector space** (over $\mathbb{R}$) is a set $V$ with operations of addition and scalar multiplication satisfying:
> 1. **Closure under addition:** $u, v \in V \implies u + v \in V$
> 2. **Closure under scalar multiplication:** $v \in V,\ c \in \mathbb{R} \implies cv \in V$
> 3. **Zero element:** $\exists\, \mathbf{0} \in V$ such that $v + \mathbf{0} = v$
> 4. (Plus standard associativity, commutativity, distributivity axioms)

---

## The Solution Space of a Homogeneous ODE

The set of all solutions of the [[Homogeneous Linear ODE]]:

$$y'' + p(t)y' + q(t)y = 0$$

on $(a,b)$ is a **vector space** because:

| Axiom | Verification |
|-------|-------------|
| Zero element | $y = 0$ is always a solution |
| Closed under addition | If $y_1, y_2$ solve $(\star)$, so does $y_1 + y_2$ ([[Superposition Principle]]) |
| Closed under scalar mult. | If $y$ solves $(\star)$, so does $cy$ |

---

## Dimension

For a **2nd order** [[Homogeneous Linear ODE]], this solution space has **dimension 2**:

- A **basis** consists of exactly 2 linearly independent solutions: the [[Fundamental Set of Solutions]] $\{y_1, y_2\}$
- Every solution is uniquely expressible as $y = c_1 y_1 + c_2 y_2$

For an $n$th order equation, the solution space has dimension $n$.

---

## Analogy: $\mathbb{R}^n$ vs. Solution Space

| $\mathbb{R}^n$ | Solution space of $n$th order ODE |
|---------------|----------------------------------|
| Vectors $\mathbf{v}$ | Functions $y(t)$ |
| Basis $\{e_1,\ldots,e_n\}$ | [[Fundamental Set of Solutions]] $\{y_1,\ldots,y_n\}$ |
| Coordinates $(c_1,\ldots,c_n)$ | Constants in $c_1y_1+\cdots+c_ny_n$ |
| $\mathbf{0}$ vector | Zero function $y=0$ |
| Linear independence | [[Linear Independence]] of functions |

---

## Why This Matters

Recognizing the solution space as a vector space justifies:
1. Looking for a **basis** (fundamental solutions)
2. Using the **[[Wronskian]]** as an analog of the determinant
3. Knowing the solution space is exactly 2-dimensional — no more, no less

---

## 📝 Notes
>

---

## Linked Concepts

- [[Superposition Principle]]
- [[Linear Independence]]
- [[Fundamental Solutions]]
- [[Fundamental Set of Solutions]]
- [[Homogeneous Linear ODE]]
- [[Wronskian]]

## See Also

- [[AM 20 – Lecture 10: 2nd Order Linear ODEs I]]
