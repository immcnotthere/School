---
title: "Abel's Formula"
aliases:
  - Abel's theorem
  - Wronskian formula
  - Abel-Liouville formula
topic: "Differential Equations"
course: "AM 20"
tags:
  - am20
  - odes
  - differential-equations
  - wronskian
  - abels-formula
type: theorem
related:
  - "[[Wronskian]]"
  - "[[Homogeneous Linear ODE]]"
  - "[[Fundamental Solutions]]"
  - "[[Linear Independence]]"
status: draft
parent: "[[Math]]"
domain: math
---

# Abel's Formula

---

## Statement ⭐

> If $y_1$ and $y_2$ are solutions of $y'' + p(t)y' + q(t)y = 0$ on $(a,b)$, then the [[Wronskian]] $W(y_1,y_2)$ satisfies:

$$\boxed{W(y_1,y_2)(t) = C\,\exp\!\left(-\int_{t_0}^{t} p(s)\,ds\right)}$$

for some constant $C \in \mathbb{R}$ and any $t_0 \in (a,b)$.

---

## Derivation

**Step 1:** Compute $W'$.

$$W = y_1 y_2' - y_1' y_2$$
$$W' = y_1 y_2'' + \cancel{y_1'y_2'} - y_1''y_2 - \cancel{y_1'y_2'} = y_1 y_2'' - y_1'' y_2$$

**Step 2:** Substitute the ODE. Since $y_i'' = -py_i' - qy_i$:

$$W' = y_1(-py_2'-qy_2) - (-py_1'-qy_1)y_2$$
$$= -py_1y_2' + \cancel{-qy_1y_2} + py_1'y_2 + \cancel{qy_1y_2}$$
$$= -p(y_1y_2' - y_1'y_2) = -pW$$

**Step 3:** Solve $W' + p(t)W = 0$ (first-order linear, separable):

$$\frac{dW}{W} = -p(t)\,dt \implies \ln|W| = -\int p\,dt + \text{const}$$

$$W(t) = C\,e^{-\int_{t_0}^t p(s)\,ds}$$

---

## Key Consequence: Wronskian is All-or-Nothing

Since $e^{-\int p\,ds} \neq 0$ always:

$$C = 0 \iff W(t) = 0 \text{ for all } t \in (a,b)$$
$$C \neq 0 \iff W(t) \neq 0 \text{ for all } t \in (a,b)$$

Therefore:

> **$W$ is either identically zero or never zero on $(a,b)$.**

This is why the [[Wronskian]] criterion only needs to be checked at one point.

---

## Computing $C$

Simply evaluate $W$ at $t_0$:

$$W(t_0) = C \cdot e^0 = C$$

So $C = W(y_1,y_2)(t_0)$ — the Wronskian at the initial point.

---

## Example

For $y_1 = e^{-2t}$, $y_2 = te^{-2t}$ solving $y'' + 4y' + 4y = 0$ (so $p = 4$):

$$W(t) = C\,e^{-\int_0^t 4\,ds} = C\,e^{-4t}$$

At $t=0$: $W(0) = e^{-2\cdot0}(1 - 0) - (-2e^0)(0) = 1$, so $C = 1$.

$$W(t) = e^{-4t} \neq 0 \checkmark$$

---

## Why "Abel"?

Named after **Niels Henrik Abel** (1802–1829), the Norwegian mathematician who first noted this identity. It is sometimes called the **Abel–Liouville formula** (Liouville generalized it to systems).

---

## Key Equations

$$W' + p(t)W = 0 \quad \text{(Wronskian satisfies this 1st order ODE)}$$

$$W(t) = W(t_0)\,e^{-\int_{t_0}^t p(s)\,ds} \quad \text{(Abel's formula)}$$

$$W \equiv 0 \text{ or } W \neq 0 \text{ everywhere on } (a,b)$$

---

## 📝 Notes
>

---

## Linked Concepts

- [[Wronskian]]
- [[Homogeneous Linear ODE]]
- [[Fundamental Solutions]]
- [[Fundamental Set of Solutions]]
- [[Linear Independence]]
- [[Existence_and_Uniqueness_Theorem|Existence and Uniqueness Theorem]]

## See Also

- [[AM 20 – Lecture 10: 2nd Order Linear ODEs I]]
