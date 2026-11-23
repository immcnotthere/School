---
title: Linear Independence
aliases:
  - linearly independent
  - linearly dependent
topic: Linear Algebra / Differential Equations
course: AM 20
tags:
  - am20
  - linear-algebra
  - odes
  - linear-independence
type: concept
related:
  - "[[Wronskian]]"
  - "[[Fundamental Solutions]]"
  - "[[Vector space]]"
  - "[[Superposition Principle]]"
status: draft
parent: "[[Math]]"
domain: math
---

# Linear Independence

---

## Definition (Functions)

> Two functions $y_1(t)$ and $y_2(t)$ on $(a,b)$ are **linearly independent** if:
> $$c_1 y_1(t) + c_2 y_2(t) = 0 \text{ for all } t \in (a,b) \implies c_1 = c_2 = 0$$
> If non-trivial $c_1, c_2$ exist making this hold, they are **linearly dependent**.

Linearly dependent means one is a scalar multiple of the other: $y_2 = ky_1$ for some constant $k$.

---

## Testing Independence: Direct Method

Show that $c_1 y_1 + c_2 y_2 = 0$ (as the zero function) forces $c_1 = c_2 = 0$.

**Example:** $y_1 = e^{-2t}$, $y_2 = te^{-2t}$.

Suppose $c_1 e^{-2t} + c_2 te^{-2t} = 0$ for all $t$.

- At $t = 0$: $c_1 = 0$
- At $t = 1$: $c_2 e^{-2} = 0 \implies c_2 = 0$ ✓

---

## Testing Independence: The [[Wronskian]]

For solutions of a [[Homogeneous Linear ODE]], the [[Wronskian]] provides a cleaner test:

$$W(y_1,y_2)(t_0) \neq 0 \implies y_1,y_2\ \text{linearly independent}$$

Combined with [[Abels Formula|Abel's Formula]]: if $W \neq 0$ at one point, it's nonzero everywhere.

> ⚠️ For **general** functions (not solutions of an ODE), $W \equiv 0$ does not guarantee dependence. But for ODE solutions it does.

---

## Why It Matters for ODEs

A fundamental pair of solutions must be linearly independent. If $y_1$ and $y_2$ are dependent (say $y_2 = ky_1$), then:

$$c_1 y_1 + c_2 y_2 = (c_1 + kc_2)y_1$$

only one free parameter — **not enough** to satisfy arbitrary initial conditions $y(t_0) = y_0$, $y'(t_0) = v_0$.

Linear independence guarantees the solution space is genuinely 2-dimensional and every IVP has a unique solution.

---

## Generalization: $n$ Functions

$\{f_1, \ldots, f_n\}$ are linearly independent on $(a,b)$ if:

$$c_1 f_1 + c_2 f_2 + \cdots + c_n f_n = 0 \implies c_1 = c_2 = \cdots = c_n = 0$$

For an $n$th order linear ODE, we need $n$ linearly independent solutions to form a fundamental set.

---

## Key Equations

$$c_1 y_1 + c_2 y_2 = 0 \text{ for all } t \implies c_1=c_2=0 \quad \text{(linear independence)}$$

$$W(y_1,y_2)(t_0) \neq 0 \implies \text{linearly independent (for ODE solutions)}$$

---

## 📝 Notes
>

---

## Linked Concepts

- [[Wronskian]]
- [[Abels Formula|Abel's Formula]]
- [[Fundamental Solutions]]
- [[Fundamental Set of Solutions]]
- [[Vector space]]
- [[Homogeneous Linear ODE]]
- [[Superposition Principle]]

## See Also

- [[AM 20 – Lecture 10: 2nd Order Linear ODEs I]]
