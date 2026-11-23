---
title: "Homogeneous Linear ODE"
aliases:
  - homogeneous ODE
  - homogeneous linear equation
topic: "Differential Equations"
course: "AM 20"
tags:
  - am20
  - odes
  - differential-equations
  - homogeneous
type: concept
related:
  - "[[Linear ODE]]"
  - "[[Second Order ODE]]"
  - "[[Superposition Principle]]"
  - "[[Fundamental Solutions]]"
  - "[[Wronskian]]"
status: draft
parent: "[[Math]]"
domain: math
---

# Homogeneous Linear ODE

---

## Definition

> A [[Linear ODE]] is **homogeneous** when the right-hand side (the forcing term) is zero:

$$y'' + p(t)\,y' + q(t)\,y = 0 \tag{$\star$}$$

Equivalently, $a(t)y'' + b(t)y' + c(t)y = 0$.

---

## Why "Homogeneous"?

The term means there is **no external forcing** — the system evolves freely from its initial conditions with no input driving it.

Physically:
- [[Spring-Mass-Dashpot]] with $f(t) = 0$: free oscillation with no applied force
- Pendulum released from rest: no driving torque

---

## Structure of the Solution Space

By the [[Superposition Principle]], the set of all solutions of $(\star)$ on $(a,b)$ is a **[[Vector space]]**:

1. $y = 0$ is always a solution (not empty)
2. If $y_1, y_2$ solve $(\star)$, so does $c_1 y_1 + c_2 y_2$ for any $c_1, c_2 \in \mathbb{R}$

This vector space has **dimension 2** — it has a basis of exactly two linearly independent solutions, called a [[Fundamental Set of Solutions]].

$$\text{Solution space} = \text{Span}\{y_1, y_2\}$$

---

## General Solution

$$\boxed{y_h = c_1 y_1 + c_2 y_2}$$

where $\{y_1, y_2\}$ is any [[Fundamental Set of Solutions]] — i.e. two linearly independent solutions of $(\star)$.

The constants $c_1, c_2$ are determined by [[Initial Value Problem|initial conditions]].

---

## Existence of Fundamental Solutions

If $p(t)$ and $q(t)$ are continuous on $(a,b)$, choose any $t_0 \in (a,b)$. The two solutions defined by:

$$y_1(t_0) = 1,\ y_1'(t_0) = 0 \qquad y_2(t_0) = 0,\ y_2'(t_0) = 1$$

always exist (by the [[Existence_and_Uniqueness_Theorem|Existence and Uniqueness Theorem]]) and always form a fundamental pair.

---

## Checking Independence: The [[Wronskian]]

$\{y_1, y_2\}$ is a fundamental pair $\iff$

$$W(y_1, y_2)(t_0) = \begin{vmatrix} y_1(t_0) & y_2(t_0) \\ y_1'(t_0) & y_2'(t_0) \end{vmatrix} \neq 0$$

for some $t_0 \in (a,b)$. By [[Abels Formula|Abel's Formula]], this is equivalent to $W \neq 0$ *everywhere* on $(a,b)$.

---

## Homogeneous vs. Nonhomogeneous

$$y'' + py' + qy = h(t)$$

| $h(t)$ | Name | General solution |
|--------|------|-----------------|
| $= 0$ | Homogeneous | $y_h = c_1 y_1 + c_2 y_2$ |
| $\neq 0$ | Nonhomogeneous | $y = y_h + y_p$ (homogeneous + particular) |

Solving the homogeneous equation is always the **first step** in solving the nonhomogeneous one.

---

## Example

$y'' + 4y' + 4y = 0$ has solutions $y_1 = e^{-2t}$ and $y_2 = te^{-2t}$.

General solution: $y_h = c_1 e^{-2t} + c_2 t e^{-2t}$

Check independence: $W(y_1, y_2)(0) = \begin{vmatrix} 1 & 0 \\ -2 & 1 \end{vmatrix} = 1 \neq 0$ ✓

---

## Key Equations

$$y'' + p(t)y' + q(t)y = 0 \tag{homogeneous $\star$}$$

$$y_h = c_1 y_1 + c_2 y_2 \quad \text{(general solution)}$$

$$W(y_1,y_2)(t) \neq 0 \iff \{y_1, y_2\}\ \text{is a fundamental pair}$$

---

## 📝 Notes
>

---

## Linked Concepts

- [[Linear ODE]]
- [[Second Order ODE]]
- [[Constant Coefficient ODE]]
- [[Superposition Principle]]
- [[Fundamental Solutions]]
- [[Fundamental Set of Solutions]]
- [[Wronskian]]
- [[Abels Formula|Abel's Formula]]
- [[Vector space]]
- [[Linear Independence]]
- [[Initial Value Problem]]
- [[Existence_and_Uniqueness_Theorem|Existence and Uniqueness Theorem]]

## See Also

- [[AM 20 – Lecture 10: 2nd Order Linear ODEs I]]
