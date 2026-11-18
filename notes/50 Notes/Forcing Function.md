---
title: "Forcing Function"
aliases:
  - forcing term
  - external force
  - driving function
  - input function
  - nonhomogeneous term
  - f(t)
  - h(t)
topic: "Differential Equations"
course: "AM 20"
tags:
  - am20
  - odes
  - differential-equations
  - forcing
  - nonhomogeneous
type: concept
related:
  - "[[Linear ODE]]"
  - "[[Homogeneous Linear ODE]]"
  - "[[Second Order ODE]]"
  - "[[Spring-Mass-Dashpot]]"
  - "[[Initial Value Problem]]"
  - "[[Existence_and_Uniqueness_Theorem|Existence and Uniqueness Theorem]]"
  - "[[Superposition Principle]]"
status: draft
parent: "[[Math]]"
domain: math
---

# Forcing Function

---

## Definition

> The **forcing function** (also called the **forcing term**, **driving function**, or **[[Forcing Function|nonhomogeneous term]] term**) is the right-hand side $f(t)$ of a [[Linear ODE]]:

$$a(t)\,y'' + b(t)\,y' + c(t)\,y = \underbrace{f(t)}_{\text{forcing function}}$$

or in standard form:

$$y'' + p(t)\,y' + q(t)\,y = \underbrace{h(t)}_{\text{forcing function}}$$

It represents an **external input** driving the system — something imposed from outside rather than arising from the system's own dynamics.

---

## Homogeneous vs. Nonhomogeneous

| $f(t)$        | Equation type                           | Physical meaning                                                                             |
| ------------- | --------------------------------------- | -------------------------------------------------------------------------------------------- |
| $f(t) = 0$    | [[Homogeneous Linear ODE\|Homogeneous]] | System evolves freely from [[Initial Value Problem\|initial conditions]] — no external input |
| $f(t) \neq 0$ | Nonhomogeneous                          | System is driven by an external force (See [[Affinity\|affine]])                             |

The presence or absence of a forcing function **fundamentally changes** the solution structure.

---

## Physical Interpretation

### [[Spring-Mass-Dashpot]]

$$m\,y'' + c\,y' + k\,y = \underbrace{f(t)}_{\text{applied force}}$$

$f(t)$ is the **external force** applied to the mass. Common examples:

| Forcing function | Physical scenario |
|-----------------|-------------------|
| $f(t) = 0$ | Free vibration — released from rest or given a push, no ongoing force |
| $f(t) = F_0$ (constant) | Constant applied load |
| $f(t) = F_0\cos(\omega t)$ | Periodic driving force (e.g. motor, shaker) |
| $f(t) = F_0 e^{-\alpha t}$ | Decaying force (e.g. impact) |
| $f(t) = \delta(t - t_0)$ | Impulsive force (sharp blow at time $t_0$) |

---

## Effect on Solution Structure

### Homogeneous ($f = 0$)

Solution space is a **[[Vector space]]** — general solution is:

$$y_h = c_1 y_1 + c_2 y_2$$

where $\{y_1, y_2\}$ is a [[Fundamental Set of Solutions]].

### Nonhomogeneous ($f \neq 0$)

The solution space is **not** a vector space (sum of two solutions is not a solution). General solution is:

$$\boxed{y = \underbrace{c_1 y_1 + c_2 y_2}_{y_h,\ \text{homogeneous (transient)}} + \underbrace{y_p}_{\text{particular (steady-state)}}}$$

where $y_p$ is **any single solution** of the full nonhomogeneous equation.

> The forcing function shapes $y_p$ — different $f(t)$ require different methods to find $y_p$ (undetermined coefficients, variation of parameters, Laplace transforms).

---

## Why $y_h + y_p$ Gives All Solutions

If $y_p$ is a particular solution and $y$ is any solution of $y'' + py' + qy = h$, then:

$$y'' + py' + qy = h \quad \text{and} \quad y_p'' + py_p' + qy_p = h$$

Subtracting: $(y - y_p)'' + p(y-y_p)' + q(y-y_p) = 0$

So $y - y_p$ solves the **homogeneous** equation → $y - y_p = c_1 y_1 + c_2 y_2$ → $y = y_h + y_p$. ✓

---

## Role in the [[Existence_and_Uniqueness_Theorem|Existence and Uniqueness Theorem]]

For the [[Existence_and_Uniqueness_Theorem|Existence and Uniqueness Theorem]] to guarantee a global solution on $(a,b)$, the forcing function $h(t)$ must be **[[Continuity|continuous]]** on $(a,b)$, alongside $p(t)$ and $q(t)$.

If $h(t)$ has a discontinuity (e.g. a jump) at some $t^* \in (a,b)$, then the interval must be split at $t^*$ and solutions matched at the boundary.

---

## The [[Superposition Principle]] for Forcing

If $y_1$ is a particular solution when $f(t) = f_1(t)$, and $y_2$ is a particular solution when $f(t) = f_2(t)$, then $\alpha y_1 + \beta y_2$ is a particular solution when $f(t) = \alpha f_1(t) + \beta f_2(t)$.

This is the **superposition of inputs** — extremely useful when $f(t)$ can be decomposed into simpler components (e.g. Fourier series).

$$L[y_1] = f_1,\ L[y_2] = f_2 \implies L[\alpha y_1 + \beta y_2] = \alpha f_1 + \beta f_2$$

---

## Resonance

When the forcing function has the **same frequency** as the system's natural frequency $\omega_0 = \sqrt{k/m}$:

$$f(t) = F_0\cos(\omega_0 t) \quad \text{(undamped system)}$$

the particular solution grows **without bound**:

$$y_p = \frac{F_0}{2m\omega_0}\,t\sin(\omega_0 t) \quad \longrightarrow \infty \text{ as } t \to \infty$$

This is **resonance** — the forcing function drives the system at exactly the frequency it "wants" to oscillate at. Physically catastrophic (bridges, buildings, machine parts).

---

## Finding Particular Solutions

| Forcing function form | Method |
|----------------------|--------|
| Polynomial $p(t)$ | Undetermined coefficients |
| $e^{\alpha t}$, $\cos(\omega t)$, $\sin(\omega t)$ | Undetermined coefficients |
| General $h(t)$ | Variation of parameters |
| Piecewise / discontinuous | Laplace transforms |
| Impulsive $\delta(t)$ | Laplace transforms / Green's functions |

---

## Key Equations

$$y'' + p(t)y' + q(t)y = h(t) \quad \text{(nonhomogeneous)}$$

$$y_{\text{general}} = c_1 y_1 + c_2 y_2 + y_p$$

$$y - y_p \in \ker(L) = \text{Span}\{y_1, y_2\} \quad \text{(homogeneous solution space)}$$

$$L[\alpha y_1 + \beta y_2] = \alpha f_1 + \beta f_2 \quad \text{(superposition of inputs)}$$

---

## 📝 Notes
>

---

## Linked Concepts

- [[Linear ODE]]
- [[Homogeneous Linear ODE]]
- [[Second Order ODE]]
- [[Constant Coefficient ODE]]
- [[Spring-Mass-Dashpot]]
- [[Superposition Principle]]
- [[Fundamental Solutions]]
- [[Fundamental Set of Solutions]]
- [[Initial Value Problem]]
- [[Existence_and_Uniqueness_Theorem|Existence and Uniqueness Theorem]]
- [[Continuity]]
- [[Vector space]]
- [[Characteristic Equation]]

## See Also

- [[AM 20 – Lecture 10: 2nd Order Linear ODEs I]]
