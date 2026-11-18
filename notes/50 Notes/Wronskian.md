---
title: "Wronskian"
aliases:
  - Wronskian determinant
  - W(y1,y2)
topic: "Differential Equations"
course: "AM 20"
tags:
  - am20
  - odes
  - differential-equations
  - wronskian
  - linear-independence
type: concept
related:
  - "[[Fundamental Solutions]]"
  - "[[Fundamental Set of Solutions]]"
  - "[[Linear Independence]]"
  - "[[Abels Formula|Abel's Formula]]"
  - "[[Homogeneous Linear ODE]]"
status: draft
parent: "[[Math]]"
domain: math
---

# Wronskian

---

## Definition

> For two differentiable functions $y_1(t)$ and $y_2(t)$, the **Wronskian** is the determinant:

$$W(y_1, y_2)(t) = \begin{vmatrix} y_1(t) & y_2(t) \\ y_1'(t) & y_2'(t) \end{vmatrix} = y_1(t)\,y_2'(t) - y_1'(t)\,y_2(t)$$

It is a function of $t$.

---

## Purpose

The Wronskian is the main tool for checking whether two solutions of a [[Homogeneous Linear ODE]] are **linearly independent** (and thus form a [[Fundamental Set of Solutions]]).

---

## Wronskian Criterion ⭐

If $y_1, y_2$ are solutions of $y'' + p(t)y' + q(t)y = 0$ on $(a,b)$, then:

$$\{y_1, y_2\}\ \text{is a fundamental pair} \iff W(y_1,y_2)(t_0) \neq 0 \text{ for some } t_0 \in (a,b)$$

By [[Abels Formula|Abel's Formula]], $W$ is either always zero or never zero on $(a,b)$, so checking at **any single point** is sufficient.

---

## Proof of Criterion ($\Rightarrow$)

Suppose $W(y_1,y_2)(t_0) \neq 0$. Let $y_3$ be any solution with $y_3(t_0)=u_0$, $y_3'(t_0)=v_0$. The system:

$$\begin{bmatrix} y_1(t_0) & y_2(t_0) \\ y_1'(t_0) & y_2'(t_0) \end{bmatrix} \begin{bmatrix} c_1 \\ c_2 \end{bmatrix} = \begin{bmatrix} u_0 \\ v_0 \end{bmatrix}$$

has a unique solution $(c_1,c_2)$ since the determinant $= W(y_1,y_2)(t_0) \neq 0$. Then $\tilde{y} = c_1y_1 + c_2y_2$ matches $y_3$ at $t_0$ and its derivative — by uniqueness $y_3 = \tilde{y}$. ✓

---

## Abel's Formula for $W$

By [[Abels Formula|Abel's Formula]], if $y_1, y_2$ solve $y''+py'+qy=0$, then:

$$W(t) = C\,\exp\!\left(-\int_{t_0}^t p(s)\,ds\right)$$

Since the exponential is never zero:

$$W(t_0) = 0 \implies C = 0 \implies W \equiv 0 \text{ on } (a,b)$$
$$W(t_0) \neq 0 \implies C \neq 0 \implies W \neq 0 \text{ everywhere on } (a,b)$$

---

## Derivation of the Wronskian ODE

$$W = y_1 y_2' - y_1' y_2$$
$$W' = y_1 y_2'' + \cancel{y_1'y_2'} - y_1''y_2 - \cancel{y_1'y_2'} = y_1 y_2'' - y_1'' y_2$$

Substituting $y_i'' = -py_i' - qy_i$:

$$W' = y_1(-py_2'-qy_2) - (-py_1'-qy_1)y_2 = -p(y_1y_2'-y_1'y_2) = -pW$$

So $W$ satisfies: $W' + p(t)W = 0$ — a separable first order ODE.

---

## Examples

### $y_1 = e^{-2t}$, $y_2 = te^{-2t}$

$$W = e^{-2t}(e^{-2t} - 2te^{-2t}) - (-2e^{-2t})(te^{-2t})$$
$$= e^{-4t} - 2te^{-4t} + 2te^{-4t} = e^{-4t} \neq 0$$

Fundamental pair ✓. Note: $W(t) = e^{-4t} = W(0)\cdot e^{-\int_0^t 4\,ds}$ — consistent with Abel (here $p=4$).

### Dependent functions: $y_1 = e^t$, $y_2 = 3e^t$

$$W = e^t \cdot 3e^t - e^t \cdot 3e^t = 0$$

$W \equiv 0$ → linearly dependent → **not** a fundamental pair.

---

## Key Equations

$$W(y_1,y_2)(t) = y_1 y_2' - y_1' y_2$$

$$W' + p(t)W = 0 \quad \text{(Wronskian ODE)}$$

$$W(t) = C\,e^{-\int p\,dt} \quad \text{([[Abels Formula|Abel's Formula]])}$$

$$W(t_0)\neq 0 \iff \{y_1,y_2\}\ \text{is a fundamental pair}$$

---

## 📝 Notes
>

---

## Linked Concepts

- [[Fundamental Solutions]]
- [[Fundamental Set of Solutions]]
- [[Linear Independence]]
- [[Abels Formula|Abel's Formula]]
- [[Homogeneous Linear ODE]]
- [[Existence_and_Uniqueness_Theorem|Existence and Uniqueness Theorem]]
- [[Superposition Principle]]

## See Also

- [[AM 20 – Lecture 10: 2nd Order Linear ODEs I]]
