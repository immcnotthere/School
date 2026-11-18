---
title: "Spring-Mass-Dashpot"
aliases:
  - spring mass dashpot
  - mass-spring-damper
  - damped harmonic oscillator
  - spring-dashpot system
topic: "Differential Equations / Mechanics"
course: "AM 20"
tags:
  - am20
  - odes
  - differential-equations
  - mechanics
  - oscillator
  - spring-mass-dashpot
type: concept
related:
  - "[[Second Order ODE]]"
  - "[[Linear ODE]]"
  - "[[Constant Coefficient ODE]]"
  - "[[Characteristic Equation]]"
  - "[[Homogeneous Linear ODE]]"
status: draft
parent: "[[Math]]"
domain: math
---

# Spring-Mass-Dashpot

---

## The Physical System

A mass $m$ is attached to:
- A **spring** with spring constant $k$ (restoring force)
- A **dashpot** (damper) with damping coefficient $c$ (resistive force)
- An **external forcing** $f(t)$

Let $y(t)$ = displacement from equilibrium (positive = stretched).

---

## Forces

| Component | Force | Direction |
|-----------|-------|-----------|
| Spring | $F_{\text{spring}} = -ky$ | Restores toward equilibrium |
| Dashpot | $F_{\text{dash}} = -cy'$ | Opposes velocity |
| External | $f(t)$ | Applied forcing |

---

## Equation of Motion

By Newton's second law ($F = ma = my''$):

$$\boxed{m\,y'' + c\,y' + k\,y = f(t)}$$

This is a [[Constant Coefficient ODE|constant-coefficient]] [[Linear ODE]]. It is:
- **[[Homogeneous Linear ODE|Homogeneous]]** when $f(t) = 0$ (free vibration)
- **Nonhomogeneous** when $f(t) \neq 0$ (forced vibration)

---

## [[Characteristic Equation]]

For the free ($f=0$) case, substitute $y = e^{\lambda t}$:

$$m\lambda^2 + c\lambda + k = 0$$

$$\lambda = \frac{-c \pm \sqrt{c^2 - 4mk}}{2m}$$

---

## The Four Regimes

Let $\Delta = c^2 - 4mk$.

### Undamped ($c = 0$)

$$m\lambda^2 + k = 0 \implies \lambda = \pm i\omega_0, \qquad \omega_0 = \sqrt{k/m}$$

$$y = c_1\cos(\omega_0 t) + c_2\sin(\omega_0 t)$$

Pure oscillation at **natural frequency** $\omega_0$. No energy loss.

### Underdamped ($\Delta < 0$, $c > 0$ small)

$$\lambda = -\frac{c}{2m} \pm i\beta, \qquad \beta = \frac{\sqrt{4mk-c^2}}{2m}$$

$$y = e^{-ct/2m}(c_1\cos\beta t + c_2\sin\beta t)$$

Oscillates with **exponentially decaying amplitude**. System "rings down."

### Critically Damped ($\Delta = 0$, $c = 2\sqrt{mk}$)

$$\lambda = -\frac{c}{2m} \quad \text{(repeated)}$$

$$y = (c_1 + c_2 t)\,e^{-ct/2m}$$

Fastest return to equilibrium **without** oscillating. Used in precision instruments.

### Overdamped ($\Delta > 0$, $c$ large)

$$\lambda_1, \lambda_2 < 0 \quad \text{(distinct negative reals)}$$

$$y = c_1 e^{\lambda_1 t} + c_2 e^{\lambda_2 t}$$

Returns to equilibrium **slowly** without oscillating. "Sluggish."

---

## Summary Table

| Regime | Condition | Behavior | General Solution |
|--------|-----------|----------|-----------------|
| Undamped | $c = 0$ | Pure oscillation | $c_1\cos\omega_0t + c_2\sin\omega_0t$ |
| Underdamped | $c^2 < 4mk$ | Decaying oscillation | $e^{-ct/2m}(c_1\cos\beta t+c_2\sin\beta t)$ |
| Critically damped | $c^2 = 4mk$ | Fastest non-oscillatory decay | $(c_1+c_2t)e^{-ct/2m}$ |
| Overdamped | $c^2 > 4mk$ | Slow exponential decay | $c_1e^{\lambda_1 t}+c_2e^{\lambda_2 t}$ |

---

## Initial Conditions

The [[Initial Value Problem]] requires:

- $y(0) = y_0$ — initial **displacement**
- $y'(0) = v_0$ — initial **velocity**

These two conditions uniquely determine $c_1, c_2$ in the general solution.

---

## Key Equations

$$my'' + cy' + ky = f(t) \quad \text{(equation of motion)}$$

$$m\lambda^2 + c\lambda + k = 0 \quad \text{([[Characteristic Equation]])}$$

$$\omega_0 = \sqrt{k/m} \quad \text{(natural frequency, undamped)}$$

$$\Delta = c^2 - 4mk \quad \text{(discriminant)}$$

---

## 📝 Notes
>

---

## Linked Concepts

- [[Second Order ODE]]
- [[Linear ODE]]
- [[Constant Coefficient ODE]]
- [[Homogeneous Linear ODE]]
- [[Characteristic Equation]]
- [[Fundamental Solutions]]
- [[Initial Value Problem]]
- [[Existence_and_Uniqueness_Theorem|Existence and Uniqueness Theorem]]

## See Also

- [[AM 20 – Lecture 10: 2nd Order Linear ODEs I]]
