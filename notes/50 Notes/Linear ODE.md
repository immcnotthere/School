---
title: "Linear ODE"
aliases:
  - linear differential equation
  - linear ordinary differential equation
topic: "Differential Equations"
course: "AM 20"
tags:
  - am20
  - odes
  - differential-equations
  - linearity
type: concept
related:
  - "[[Second Order ODE]]"
  - "[[Homogeneous Linear ODE]]"
  - "[[Constant Coefficient ODE]]"
  - "[[Superposition Principle]]"
status: draft
parent: "[[Math]]"
domain: math
prereqs:
  - "[[ODE]]"
retention_band: cold
---

# Linear ODE

---

## Definition

> A [[Second Order ODE]] $y'' = f(t, y, y')$ is **linear** if it can be written in the form:

$$a(t)\,y'' + b(t)\,y' + c(t)\,y = f(t)$$

where $a(t), b(t), c(t), f(t)$ are functions of $t$ only — **not** of $y$ or its derivatives.

The equation is linear **in** $y$, $y'$, and $y''$.

---

## What Makes an ODE Linear?

Linearity means the dependent variable $y$ and all its derivatives appear only:
- To the **first power**
- Without being **multiplied together**
- Without appearing inside **nonlinear functions** (like $\sin y$, $e^y$, $y^2$)

| ODE | Linear? | Reason |
|-----|---------|--------|
| $y'' + 3y' - 2y = \cos t$ | ✅ Yes | $y, y', y''$ each appear linearly |
| $y'' + \sin(y) = 0$ | ❌ No | $\sin(y)$ is nonlinear in $y$ |
| $y'' + y\,y' = 0$ | ❌ No | $y \cdot y'$ is a product of $y$ and $y'$ |
| $m\ell\,\theta'' + mg\sin\theta = 0$ | ❌ No | $\sin\theta$ nonlinear |
| $my'' + cy' + ky = f(t)$ | ✅ Yes | [[Spring-Mass-Dashpot]] |

---

## Standard Form

After dividing by $a(t)$ (where $a(t) \neq 0$):

$$y'' + p(t)\,y' + q(t)\,y = h(t)$$

where $p = b/a$, $q = c/a$, $h = f/a$. This is the form most theorems are stated in.

---

## Why Linearity Matters

Linearity unlocks powerful structural results unavailable for nonlinear ODEs:

1. **[[Existence_and_Uniqueness_Theorem]]** — for linear ODEs, the solution exists on the *entire* interval where $p, q, h$ are continuous (not just locally)
2. **[[Superposition Principle]]** — linear combinations of solutions are solutions
3. **[[Fundamental Set of Solutions]]** — solution space has a nice basis structure (dimension 2 for 2nd order)
4. **[[Wronskian]]** test for linear independence of solutions
5. **[[Abels Formula|Abel's Formula]]** — the Wronskian satisfies its own simple ODE

None of these hold in general for nonlinear ODEs.

---

## Homogeneous vs. Nonhomogeneous

$$y'' + p(t)y' + q(t)y = \underbrace{h(t)}_{\text{forcing}}$$

| $h(t)$ | Type | Solutions |
|--------|------|-----------|
| $h(t) = 0$ | [[Homogeneous Linear ODE\|Homogeneous]] | Solution space is a vector space |
| $h(t) \neq 0$ | Nonhomogeneous | General solution = homogeneous solution + particular solution |

$$y_{\text{general}} = \underbrace{c_1 y_1 + c_2 y_2}_{y_h,\ \text{homogeneous}} + \underbrace{y_p}_{\text{particular}}$$

---

## Key Equations

$$a(t)y'' + b(t)y' + c(t)y = f(t) \quad \text{(general linear form)}$$

$$y'' + p(t)y' + q(t)y = h(t) \quad \text{(standard form)}$$

$$y_{\text{general}} = c_1 y_1 + c_2 y_2 + y_p \quad \text{(full general solution)}$$

---

## 📝 Notes
>

---

## Linked Concepts

- [[Second Order ODE]]
- [[Homogeneous Linear ODE]]
- [[Constant Coefficient ODE]]
- [[Initial Value Problem]]
- [[Existence_and_Uniqueness_Theorem|Existence and Uniqueness Theorem]]
- [[Superposition Principle]]
- [[Fundamental Solutions]]
- [[Fundamental Set of Solutions]]
- [[Wronskian]]
- [[Abels Formula|Abel's Formula]]
- [[Spring-Mass-Dashpot]]

## See Also

- [[AM 20 – Lecture 10: 2nd Order Linear ODEs I]]
