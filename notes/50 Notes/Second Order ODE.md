---
title: "Second Order ODE"
aliases:
  - second order differential equation
  - 2nd order ODE
topic: "Differential Equations"
course: "AM 20"
tags:
  - am20
  - odes
  - differential-equations
type: concept
related:
  - "[[Linear ODE]]"
  - "[[Homogeneous Linear ODE]]"
  - "[[Initial Value Problem]]"
  - "[[Existence_and_Uniqueness_Theorem|Existence and Uniqueness Theorem]]"
status: draft
parent: "[[Math]]"
domain: math
---

# Second Order ODE

---

## Definition

> A **second order ODE** is a differential equation involving a function $y(t)$, its first derivative $y'$, and its second derivative $y''$:

$$y'' = f(t,\, y,\, y')$$

It is "second order" because the highest derivative appearing is $y''$.

---

## General Form vs. Linear Form

| Type | Form |
|------|------|
| General (possibly nonlinear) | $y'' = f(t, y, y')$ |
| [[Linear ODE\|Linear]] | $a(t)y'' + b(t)y' + c(t)y = f(t)$ |
| [[Homogeneous Linear ODE\|Homogeneous linear]] | $a(t)y'' + b(t)y' + c(t)y = 0$ |
| [[Constant Coefficient ODE\|Constant coefficient]] | $ay'' + by' + cy = f(t)$, $a,b,c$ constant |

---

## Examples

### Nonlinear: Undamped Pendulum

$$m\ell\,\theta'' + mg\sin\theta = 0$$

Nonlinear because of the $\sin\theta$ term — cannot be written in linear form.

### Linear: [[Spring-Mass-Dashpot]]

$$m\,y'' + c\,y' + k\,y = f(t)$$

Linear in $y$, $y'$, $y''$. See [[Spring-Mass-Dashpot]] for physical interpretation.

---

## Why Second Order?

Newton's second law $F = ma$ involves acceleration $a = y''$ — so most physical systems (oscillators, circuits, beams) naturally produce second order ODEs. Two initial conditions are needed: position $y(t_0)$ and velocity $y'(t_0)$.

---

## Solution Space

For the [[Homogeneous Linear ODE]] $y'' + p(t)y' + q(t)y = 0$, the set of all solutions forms a **[[Vector space]]** of dimension **2** — spanned by a [[Fundamental Set of Solutions]] $\{y_1, y_2\}$:

$$y_h = c_1 y_1 + c_2 y_2$$

This is why two solutions are needed, and why the [[Wronskian]] is used to check independence.

---

## Reduction to Standard Form

Divide $a(t)y'' + b(t)y' + c(t)y = f(t)$ by $a(t)$ wherever $a(t) \neq 0$:

$$y'' + p(t)y' + q(t)y = h(t), \qquad p = \frac{b}{a},\quad q = \frac{c}{a},\quad h = \frac{f}{a}$$

The equation is well-defined as a 2nd order ODE on any interval where $a(t) \neq 0$.

---

## Key Equations

$$y'' = f(t, y, y') \quad \text{(general form)}$$

$$a(t)y'' + b(t)y' + c(t)y = f(t) \quad \text{(linear form)}$$

$$y'' + p(t)y' + q(t)y = 0 \quad \text{(standard homogeneous)}$$

$$y_h = c_1 y_1 + c_2 y_2 \quad \text{(general solution, homogeneous case)}$$

---

## 📝 Notes
>

---

## Linked Concepts

- [[Linear ODE]]
- [[Homogeneous Linear ODE]]
- [[Constant Coefficient ODE]]
- [[Initial Value Problem]]
- [[Existence_and_Uniqueness_Theorem|Existence and Uniqueness Theorem]]
- [[Superposition Principle]]
- [[Fundamental Solutions]]
- [[Wronskian]]
- [[Spring-Mass-Dashpot]]
- [[Vector space]]

## See Also

- [[AM 20 – Lecture 10: 2nd Order Linear ODEs I]]
