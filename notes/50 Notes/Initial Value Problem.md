---
title: "Initial Value Problem"
aliases:
  - IVP
  - initial conditions
topic: "Differential Equations"
course: "AM 20"
tags:
  - am20
  - odes
  - differential-equations
  - initial-value-problem
type: concept
related:
  - "[[Second Order ODE]]"
  - "[[Existence_and_Uniqueness_Theorem|Existence and Uniqueness Theorem]]"
  - "[[Fundamental Solutions]]"
status: draft
parent: "[[Math]]"
domain: math
prereqs:
  - "[[Differential Equation]]"
  - "[[Independent vs Dependent Variable]]"
retention_band: cold
---
# Initial Value Problem (IVP)

---

## Definition

> An **initial value problem** (IVP) is an ODE together with **initial conditions** that specify the value of the solution (and enough of its derivatives) at a single point $t_0$.

For a [[Second Order ODE]]:

$$y'' + p(t)\,y' + q(t)\,y = h(t), \qquad y(t_0) = y_0,\quad y'(t_0) = y_1$$

Two initial conditions are required because the solution space is 2-dimensional.

---

## Why Two Conditions for 2nd Order?

The general solution of a 2nd order [[Homogeneous Linear ODE]] has **two free constants**:

$$y_h = c_1 y_1 + c_2 y_2$$

Specifying $y(t_0) = y_0$ and $y'(t_0) = y_1$ gives a $2 \times 2$ linear system for $c_1, c_2$:

$$\begin{bmatrix} y_1(t_0) & y_2(t_0) \\ y_1'(t_0) & y_2'(t_0) \end{bmatrix} \begin{bmatrix} c_1 \\ c_2 \end{bmatrix} = \begin{bmatrix} y_0 \\ y_1 \end{bmatrix}$$

This system has a unique solution whenever $\det = W(y_1,y_2)(t_0) \neq 0$, i.e. when $\{y_1,y_2\}$ is a [[Fundamental Set of Solutions]].

---

## Existence and Uniqueness

By the [[Existence_and_Uniqueness_Theorem|Existence and Uniqueness Theorem]] for linear ODEs:

> If $p(t)$, $q(t)$, and $h(t)$ are **continuous** on $(a,b)$ and $t_0 \in (a,b)$, then for **any** $y_0, y_1 \in \mathbb{R}$, the IVP has a **unique solution on all of $(a,b)$**.

This is a much stronger guarantee than for nonlinear ODEs (where existence may only be local).

---

## Worked Example

Solve $y'' + 4y' + 4y = 0$, $y(0) = a$, $y'(0) = b$.

Fundamental solutions: $y_1 = e^{-2t}$, $y_2 = te^{-2t}$.

Apply initial conditions:

$$c_1 \cdot 1 + c_2 \cdot 0 = a \implies c_1 = a$$
$$-2c_1 + c_2 = b \implies c_2 = 2a + b$$

Unique solution:

$$y = a\,e^{-2t} + (2a+b)\,t\,e^{-2t}$$

---

## Physical Meaning

For the [[Spring-Mass-Dashpot]] system $my'' + cy' + ky = f(t)$:

- $y(t_0) = y_0$: **initial position** (displacement from equilibrium)
- $y'(t_0) = v_0$: **initial velocity**

These two numbers completely determine all future (and past) motion — determinism in classical mechanics.

---

## Key Equations

$$y'' + p(t)y' + q(t)y = h(t), \quad y(t_0)=y_0,\quad y'(t_0)=y_1 \quad \text{(IVP)}$$

$$\begin{bmatrix} y_1(t_0) & y_2(t_0) \\ y_1'(t_0) & y_2'(t_0) \end{bmatrix}\begin{bmatrix}c_1\\c_2\end{bmatrix} = \begin{bmatrix}y_0\\y_1\end{bmatrix} \quad \text{(system for constants)}$$

---
## Solution

To solve an $n$-th order IVP, your function must meet exactly three requirements:

- **Be smooth enough:** It must be differentiable $n$ times in a continuous stretch (an interval) around your starting point ($x_0$).
    
- **Obey the governing rule:** When you plug the function and its derivatives back into the differential equation, the equation must hold true for every point $x$ within that interval.
    
- **Hit the starting target:** At the exact starting coordinate ($x_0$), the function and its derivatives must perfectly match the specific initial conditions you were given.
    

**The TL;DR:**

A valid IVP solution is a sufficiently smooth curve that satisfies the general differential equation _and_ anchors perfectly to your specific starting conditions.
## 📝 Notes
>

---

## Linked Concepts

- [[Second Order ODE]]
- [[Linear ODE]]
- [[Homogeneous Linear ODE]]
- [[Existence_and_Uniqueness_Theorem|Existence and Uniqueness Theorem]]
- [[Fundamental Solutions]]
- [[Fundamental Set of Solutions]]
- [[Wronskian]]
- [[Spring-Mass-Dashpot]]

## See Also

- [[AM 20 – Lecture 10: 2nd Order Linear ODEs I]]
