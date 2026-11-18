---
title: "Fundamental Solutions"
aliases:
  - fundamental pair
  - fundamental pair of solutions
topic: "Differential Equations"
course: "AM 20"
tags:
  - am20
  - odes
  - differential-equations
  - fundamental-solutions
type: concept
related:
  - "[[Fundamental Set of Solutions]]"
  - "[[Homogeneous Linear ODE]]"
  - "[[Wronskian]]"
  - "[[Linear Independence]]"
  - "[[Superposition Principle]]"
status: draft
parent: "[[Math]]"
domain: math
---

# Fundamental Solutions

---

## Definition

> A **fundamental pair of solutions** of the [[Homogeneous Linear ODE]]:
> $$y'' + p(t)\,y' + q(t)\,y = 0 \tag{$\star$}$$
> is a pair $\{y_1, y_2\}$ of solutions that are **linearly independent** on $(a,b)$.

The general solution is then:

$$\boxed{y_h = c_1 y_1 + c_2 y_2}$$

and every solution of $(\star)$ has a **unique** representation in this form.

---

## Existence Theorem ⭐

If $p(t)$ and $q(t)$ are continuous on $(a,b)$, then a fundamental pair always exists.

**Construction:** Choose any $t_0 \in (a,b)$ and define:

$$y_1:\ y_1(t_0)=1,\quad y_1'(t_0)=0$$
$$y_2:\ y_2(t_0)=0,\quad y_2'(t_0)=1$$

By the [[Existence_and_Uniqueness_Theorem|Existence and Uniqueness Theorem]], both $y_1$ and $y_2$ exist on all of $(a,b)$.

**Why every solution is a combination:** If $y$ is any solution with $y(t_0) = u_0$, $y'(t_0) = v_0$, then:

$$\tilde{y} = u_0 y_1 + v_0 y_2$$

satisfies the same initial conditions as $y$ → by uniqueness, $y = \tilde{y}$.

---

## Checking: The [[Wronskian]] Criterion

$\{y_1, y_2\}$ is a fundamental pair $\iff$

$$W(y_1,y_2)(t_0) \neq 0 \quad \text{at some (equivalently, any) } t_0 \in (a,b)$$

By [[Abels Formula|Abel's Formula]], $W$ is either always zero or never zero on $(a,b)$, so one check suffices.

---

## Example

For $y'' + 4y' + 4y = 0$:

$$y_1 = e^{-2t}, \qquad y_2 = te^{-2t}$$

$$W(y_1,y_2)(0) = \begin{vmatrix} 1 & 0 \\ -2 & 1\end{vmatrix} = 1 \neq 0 \implies \text{fundamental pair} \checkmark$$

General solution: $y_h = c_1 e^{-2t} + c_2 t e^{-2t}$

---

## Non-uniqueness of Fundamental Pairs

Fundamental pairs are **not unique** — any two linearly independent solutions form one. For example, $\{e^{-2t},\, (e^{-2t} + te^{-2t})\}$ is also a valid fundamental pair for the above equation. What is unique is the **general solution** (the span), not the specific basis.

---

## Key Equations

$$y_h = c_1 y_1 + c_2 y_2 \quad \text{(general solution)}$$

$$W(y_1,y_2)(t_0) \neq 0 \iff \{y_1,y_2\}\ \text{fundamental pair}$$

---

## 📝 Notes
>

---

## Linked Concepts

- [[Fundamental Set of Solutions]]
- [[Homogeneous Linear ODE]]
- [[Wronskian]]
- [[Abels Formula|Abel's Formula]]
- [[Linear Independence]]
- [[Superposition Principle]]
- [[Existence_and_Uniqueness_Theorem|Existence and Uniqueness Theorem]]
- [[Vector space]]

## See Also

- [[AM 20 – Lecture 10: 2nd Order Linear ODEs I]]
