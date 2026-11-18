---
title: "Characteristic Equation"
aliases:
  - characteristic polynomial
  - auxiliary equation
topic: "Differential Equations"
course: "AM 20"
tags:
  - am20
  - odes
  - differential-equations
  - characteristic-equation
  - constant-coefficients
type: concept
related:
  - "[[Constant Coefficient ODE]]"
  - "[[Homogeneous Linear ODE]]"
  - "[[Fundamental Solutions]]"
  - "[[Spring-Mass-Dashpot]]"
status: draft
parent: "[[Math]]"
domain: math
prereqs:
  - "[[Determinant]]"
  - "[[Eigenvalue and Eigenvector Definition]]"
retention_band: cold
---

# Characteristic Equation

---

## Motivation

For the [[Constant Coefficient ODE]] $y'' + py' + qy = 0$, what should we try as a solution?

**Analogy:** For the first-order equation $y' + cy = 0$, the solution is $y = e^{-ct}$ — an exponential. The same intuition applies: **guess $y = e^{\lambda t}$**.

---

## Derivation

Substitute $y = e^{\lambda t}$ into $y'' + py' + qy = 0$:

$$\lambda^2 e^{\lambda t} + p\lambda e^{\lambda t} + q e^{\lambda t} = 0$$

$$e^{\lambda t}\underbrace{(\lambda^2 + p\lambda + q)}_{\text{characteristic polynomial}} = 0$$

Since $e^{\lambda t} \neq 0$, we need:

$$\boxed{\lambda^2 + p\lambda + q = 0}$$

This is the **characteristic equation** (also called the **auxiliary equation** or **characteristic polynomial**).

---

## The Three Cases

The roots $\lambda_1, \lambda_2$ are found from the quadratic formula:

$$\lambda = \frac{-p \pm \sqrt{p^2 - 4q}}{2}$$

Let $\Delta = p^2 - 4q$.

---

### Case 1: Two Distinct Real Roots ($\Delta > 0$)

$$\lambda_1 \neq \lambda_2 \in \mathbb{R}$$

Fundamental solutions:

$$y_1 = e^{\lambda_1 t}, \qquad y_2 = e^{\lambda_2 t}$$

$$y_h = c_1 e^{\lambda_1 t} + c_2 e^{\lambda_2 t}$$

Check independence: $W(y_1,y_2) = (\lambda_2 - \lambda_1)e^{(\lambda_1+\lambda_2)t} \neq 0$ since $\lambda_1 \neq \lambda_2$. ✓

---

### Case 2: Repeated Root ($\Delta = 0$)

$$\lambda_1 = \lambda_2 = \lambda = -\frac{p}{2}$$

One exponential $e^{\lambda t}$ is a solution, but we need a second independent one. The second solution is:

$$y_2 = t\,e^{\lambda t}$$

$$y_h = (c_1 + c_2 t)\,e^{\lambda t}$$

> **Example from lecture:** $y'' + 4y' + 4y = 0$ has $\lambda = -2$ (repeated). Solutions: $e^{-2t}$ and $te^{-2t}$.

---

### Case 3: Complex Conjugate Roots ($\Delta < 0$)

$$\lambda = \alpha \pm i\beta, \qquad \alpha = -\frac{p}{2},\quad \beta = \frac{\sqrt{4q-p^2}}{2}$$

Using Euler's formula $e^{i\beta t} = \cos(\beta t) + i\sin(\beta t)$, the real-valued fundamental solutions are:

$$y_1 = e^{\alpha t}\cos(\beta t), \qquad y_2 = e^{\alpha t}\sin(\beta t)$$

$$y_h = e^{\alpha t}(c_1\cos\beta t + c_2\sin\beta t)$$

---

## Physical Meaning ([[Spring-Mass-Dashpot]])

For $my'' + cy' + ky = 0$, the characteristic equation is $m\lambda^2 + c\lambda + k = 0$:

| $\Delta = c^2 - 4mk$ | Roots | Behavior |
|---------------------|-------|----------|
| $> 0$ | Two negative reals | **Overdamped** — exponential decay, no oscillation |
| $= 0$ | Repeated negative real | **Critically damped** — fastest decay without oscillation |
| $< 0$ | Complex $\alpha \pm i\beta$, $\alpha < 0$ | **Underdamped** — decaying oscillation |
| $c = 0$ | Pure imaginary $\pm i\beta$ | **Undamped** — pure oscillation |

---

## Key Equations

$$y'' + py' + qy = 0 \xrightarrow{y = e^{\lambda t}} \lambda^2 + p\lambda + q = 0$$

$$\lambda = \frac{-p \pm \sqrt{p^2-4q}}{2}$$

$$y_h = \begin{cases} c_1 e^{\lambda_1 t} + c_2 e^{\lambda_2 t} & \Delta > 0 \\ (c_1+c_2 t)e^{\lambda t} & \Delta = 0 \\ e^{\alpha t}(c_1\cos\beta t + c_2\sin\beta t) & \Delta < 0\end{cases}$$

---

## 📝 Notes
>

---

## Linked Concepts

- [[Constant Coefficient ODE]]
- [[Homogeneous Linear ODE]]
- [[Second Order ODE]]
- [[Fundamental Solutions]]
- [[Fundamental Set of Solutions]]
- [[Linear Independence]]
- [[Wronskian]]
- [[Spring-Mass-Dashpot]]

## See Also

- [[AM 20 – Lecture 10: 2nd Order Linear ODEs I]]
