---
title: "Constant Coefficient ODE"
aliases:
  - constant coefficient differential equation
  - ODE with constant coefficients
topic: "Differential Equations"
course: "AM 20"
tags:
  - am20
  - odes
  - differential-equations
  - constant-coefficients
  - characteristic-equation
type: concept
related:
  - "[[Linear ODE]]"
  - "[[Homogeneous Linear ODE]]"
  - "[[Characteristic Equation]]"
  - "[[Fundamental Solutions]]"
status: draft
parent: "[[Math]]"
domain: math
---

# Constant Coefficient ODE

---

## Definition

> A [[Linear ODE]] has **constant coefficients** if $p(t)$ and $q(t)$ are constants (not functions of $t$):

$$ay'' + by' + cy = f(t), \qquad a, b, c \in \mathbb{R},\ a \neq 0$$

Or in standard form:

$$y'' + py' + qy = f(t), \qquad p, q \in \mathbb{R}$$

---

## Why Constant Coefficients Are Special

For variable-coefficient equations, finding closed-form solutions is often impossible. With constant coefficients, we can always solve by guessing $y = e^{\lambda t}$, which leads to the [[Characteristic Equation]].

---

## Homogeneous Case: The Guess $y = e^{\lambda t}$

For $y'' + py' + qy = 0$, try $y = e^{\lambda t}$:

$$\lambda^2 e^{\lambda t} + p\lambda e^{\lambda t} + q e^{\lambda t} = 0$$
$$e^{\lambda t}(\lambda^2 + p\lambda + q) = 0$$

Since $e^{\lambda t} \neq 0$, we need:

$$\lambda^2 + p\lambda + q = 0 \tag{Characteristic Equation}$$

See [[Characteristic Equation]] for the three cases (distinct real, repeated, complex roots).

---

## The Three Cases

Let $\Delta = p^2 - 4q$ be the discriminant of the [[Characteristic Equation]].

### Case 1: Two Distinct Real Roots ($\Delta > 0$)

Roots $\lambda_1 \neq \lambda_2 \in \mathbb{R}$:

$$y_1 = e^{\lambda_1 t}, \qquad y_2 = e^{\lambda_2 t}$$
$$y_h = c_1 e^{\lambda_1 t} + c_2 e^{\lambda_2 t}$$

### Case 2: Repeated Root ($\Delta = 0$)

One root $\lambda = -p/2$ with multiplicity 2:

$$y_1 = e^{\lambda t}, \qquad y_2 = t\,e^{\lambda t}$$
$$y_h = (c_1 + c_2 t)\,e^{\lambda t}$$

> Example from lecture: $y'' + 4y' + 4y = 0$ has $\lambda = -2$ (repeated). General solution: $y_h = (c_1 + c_2 t)e^{-2t}$.

### Case 3: Complex Conjugate Roots ($\Delta < 0$)

Roots $\lambda = \alpha \pm i\beta$ where $\alpha = -p/2$, $\beta = \sqrt{4q-p^2}/2$:

$$y_1 = e^{\alpha t}\cos(\beta t), \qquad y_2 = e^{\alpha t}\sin(\beta t)$$
$$y_h = e^{\alpha t}(c_1 \cos\beta t + c_2 \sin\beta t)$$

---

## Physical Interpretation ([[Spring-Mass-Dashpot]])

For $my'' + cy' + ky = 0$, the characteristic equation is $m\lambda^2 + c\lambda + k = 0$:

| Discriminant | Physical behavior | Name |
|-------------|-------------------|------|
| $\Delta > 0$ | Exponential decay, no oscillation | Overdamped |
| $\Delta = 0$ | Critical boundary case | Critically damped |
| $\Delta < 0$ | Oscillates with decaying amplitude | Underdamped |
| $c = 0$ | Pure oscillation (no decay) | Undamped |

---

## Key Equations

$$ay'' + by' + cy = 0 \quad \text{(homogeneous constant coefficient)}$$

$$\lambda^2 + p\lambda + q = 0 \quad \text{([[Characteristic Equation]])}$$

$$\Delta = p^2 - 4q \quad \text{(discriminant)}$$

$$y_h = \begin{cases} c_1 e^{\lambda_1 t} + c_2 e^{\lambda_2 t} & \Delta > 0 \\ (c_1 + c_2 t)e^{\lambda t} & \Delta = 0 \\ e^{\alpha t}(c_1\cos\beta t + c_2\sin\beta t) & \Delta < 0 \end{cases}$$

---

## 📝 Notes
>

---

## Linked Concepts

- [[Linear ODE]]
- [[Homogeneous Linear ODE]]
- [[Second Order ODE]]
- [[Characteristic Equation]]
- [[Fundamental Solutions]]
- [[Fundamental Set of Solutions]]
- [[Wronskian]]
- [[Spring-Mass-Dashpot]]
- [[Linear Independence]]

## See Also

- [[AM 20 – Lecture 10: 2nd Order Linear ODEs I]]
