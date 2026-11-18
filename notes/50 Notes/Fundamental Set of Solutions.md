---
title: Fundamental Set of Solutions
aliases:
  - fundamental set
  - basis of solutions
  - solution basis
topic: Differential Equations
course: AM 20
tags:
  - am20
  - odes
  - differential-equations
  - fundamental-solutions
type: concept
related:
  - "[[Fundamental Solutions]]"
  - "[[Homogeneous Linear ODE]]"
  - "[[Linear Independence]]"
  - "[[Wronskian]]"
  - "[[Vector space]]"
status: draft
parent: "[[Math]]"
domain: math
---

# Fundamental Set of Solutions

---

## Definition

> A **fundamental set of solutions** of $y'' + p(t)y' + q(t)y = 0$ on $(a,b)$ is a set $\{y_1, y_2\}$ of solutions that forms a **basis** for the solution space — i.e. they are linearly independent and every solution is a unique linear combination of them.

This is equivalent to saying $\{y_1, y_2\}$ is a [[Fundamental Solutions|fundamental pair]].

---

## The Solution Space as a [[Vector space]]

By the [[Superposition Principle]], the set of all solutions of the [[Homogeneous Linear ODE]] is a vector space. For a 2nd order equation this space has **dimension 2**.

A fundamental set of solutions is precisely a **basis** of this 2-dimensional vector space:

| Linear algebra concept | ODE analog |
|----------------------|------------|
| Vector space | Solution space of $y''+py'+qy=0$ |
| Basis | Fundamental set $\{y_1, y_2\}$ |
| Dimension | 2 (for 2nd order) |
| Coordinates | Constants $c_1, c_2$ |
| Linear combination | General solution $c_1y_1 + c_2y_2$ |

---

## General Solution

$$\boxed{y_h = c_1 y_1 + c_2 y_2}$$

The fundamental set is **not unique** (many bases exist), but the **span** — i.e. the general solution — is always the same.

---

## Testing with the [[Wronskian]]

$\{y_1, y_2\}$ is a fundamental set $\iff$

$$W(y_1,y_2)(t) \neq 0 \quad \text{for some (hence all) } t \in (a,b)$$

This follows from [[Linear Independence]] + [[Abels Formula|Abel's Formula]].

---

## Canonical Construction

For the [[Homogeneous Linear ODE]] with $p, q$ continuous on $(a,b)$, the canonical fundamental set at $t_0 \in (a,b)$ is:

$$y_1:\ y_1(t_0) = 1,\quad y_1'(t_0) = 0$$
$$y_2:\ y_2(t_0) = 0,\quad y_2'(t_0) = 1$$

This gives $W(y_1,y_2)(t_0) = \det\begin{pmatrix}1&0\\0&1\end{pmatrix} = 1 \neq 0$, confirming it is indeed a fundamental set.

---

## 📝 Notes
>

---

## Linked Concepts

- [[Fundamental Solutions]]
- [[Homogeneous Linear ODE]]
- [[Wronskian]]
- [[Abels Formula|Abel's Formula]]
- [[Linear Independence]]
- [[Superposition Principle]]
- [[Vector space]]
- [[Existence_and_Uniqueness_Theorem|Existence and Uniqueness Theorem]]

## See Also

- [[AM 20 – Lecture 10: 2nd Order Linear ODEs I]]
