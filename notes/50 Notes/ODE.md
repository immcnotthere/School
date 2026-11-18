---
title: "Ordinary Differential Equation"
aliases:
  - ODE
  - ordinary differential equation
  - differential equation
topic: "Differential Equations"
course: "AM 20"
tags:
  - am20
  - odes
  - differential-equations
  - calculus
  - mathematics
type: concept
related:
  - "[[Second Order ODE]]"
  - "[[Linear ODE]]"
  - "[[Homogeneous Linear ODE]]"
  - "[[Constant Coefficient ODE]]"
  - "[[Initial Value Problem]]"
  - "[[Existence_and_Uniqueness_Theorem|Existence and Uniqueness Theorem]]"
  - "[[Rate]]"
  - "[[Linear Operator Theory]]"
status: draft
parent: "[[Math]]"
domain: math
retention_band: cold
prereqs:
  - "[[Differential Equation]]"
---

# Ordinary Differential Equation (ODE)

---

## Definition

> An **ordinary differential equation** is an equation involving an unknown function $y(t)$ and one or more of its derivatives with respect to a single independent variable $t$:
>
> $$F\!\left(t,\, y,\, y',\, y'',\, \ldots,\, y^{(n)}\right) = 0$$

The word *ordinary* distinguishes it from a **partial differential equation** (PDE), where the unknown depends on multiple independent variables and partial derivatives appear.

---

## Order

The **order** of an ODE is the order of the highest derivative appearing:

| ODE | Order |
|-----|-------|
| $y' = ky$ | 1st |
| $y'' + py' + qy = 0$ | 2nd |
| $y''' + y = \sin t$ | 3rd |
| $y^{(n)} + \cdots = f(t)$ | $n$th |

Most physical systems produce 1st or 2nd order ODEs. Higher orders arise in beam bending, control theory, and higher-order circuits.

---

## Normal Form

> The **normal form** of an $n$th order ODE expresses the highest derivative explicitly in terms of all lower-order quantities:
>
> $$y^{(n)} = f\!\left(t,\, y,\, y',\, \ldots,\, y^{(n-1)}\right)$$

This is the standard form required by the [[Existence_and_Uniqueness_Theorem|Existence and Uniqueness Theorem]]. Any ODE that can be solved for its highest derivative can be written in normal form.

### Why normal form matters

- The [[Existence_and_Uniqueness_Theorem|Existence and Uniqueness Theorem]] is stated for ODEs in normal form — the hypothesis is that $f$ is well-behaved as a function of all its arguments
- Numerical solvers (Euler, Runge-Kutta) require normal form — they step forward by evaluating $f$ at each point
- The reduction to a first-order system (see below) requires normal form as a starting point
- An ODE not solvable for $y^{(n)}$ — called an **implicit ODE** — requires separate theory (differential-algebraic equations)

### Normal form for linear ODEs

Starting from $a(t)y'' + b(t)y' + c(t)y = f(t)$, dividing by $a(t)$ wherever $a(t) \neq 0$ gives:

$$y'' = -p(t)\,y' - q(t)\,y + h(t), \qquad p = \frac{b}{a},\quad q = \frac{c}{a},\quad h = \frac{f}{a}$$

This is the normal form for a 2nd order [[Linear ODE]]. The equation is well-defined as an ODE on any interval where $a(t) \neq 0$.

### Normal form and the first-order system

Any $n$th order ODE in normal form can be rewritten as a **first-order system** by introducing new variables for each derivative. For a 2nd order ODE $y'' = f(t, y, y')$:

Let $u_1 = y$, $u_2 = y'$. Then:

$$\begin{cases} u_1' = u_2 \\ u_2' = f(t,\, u_1,\, u_2) \end{cases} \qquad \text{i.e.} \quad \mathbf{u}' = \mathbf{F}(t, \mathbf{u})$$

This reduction is fundamental — it means all ODE theory can in principle be developed for first-order systems, and results lifted back to higher orders.

---

## Classification

### By linearity

| Type | Form | Key property |
|------|------|-------------|
| [[Linear ODE\|Linear]] | $a_n(t)y^{(n)} + \cdots + a_0(t)y = f(t)$ | [[Superposition Principle]] holds |
| Nonlinear | $F(t,y,y',\ldots) = 0$, not linear in $y$ and derivatives | Superposition fails; richer behavior |

### By homogeneity (linear ODEs only)

| Type | Condition | Solution space |
|------|-----------|---------------|
| [[Homogeneous Linear ODE\|Homogeneous]] | $f(t) = 0$ | [[Vector space]] of dimension $n$ |
| Nonhomogeneous | $f(t) \neq 0$ | Affine: $y_h + y_p$ |

### By coefficient type

| Type | Coefficients | Solution method |
|------|-------------|----------------|
| [[Constant Coefficient ODE\|Constant coefficient]] | $a_i \in \mathbb{R}$ | [[Characteristic Equation]] |
| Variable coefficient | $a_i = a_i(t)$ | Power series, special functions |

### By order

| Order | Typical source | General solution has |
|-------|---------------|---------------------|
| 1st | [[Rate]] laws, RC circuits | 1 free constant |
| 2nd | [[Spring-Mass-Dashpot]], pendulum, beam | 2 free constants |
| $n$th | Higher-order systems | $n$ free constants |

---

## Solution Types

### General solution

Contains all free constants — for a linear $n$th order ODE this means $n$ constants $c_1, \ldots, c_n$:

$$y_{\text{general}} = c_1 y_1 + \cdots + c_n y_n + y_p$$

### Particular solution

A single specific solution — either a member of the general solution with constants fixed, or $y_p$ satisfying the nonhomogeneous equation.

### Singular solution

A solution not obtainable from the general solution for any choice of constants. Arises only in nonlinear ODEs.

---

## The [[Initial Value Problem]]

An ODE of order $n$ requires $n$ initial conditions to pick out a unique solution:

$$y^{(n)} = f(t, y, \ldots, y^{(n-1)}), \qquad y(t_0) = y_0,\quad y'(t_0) = y_1,\quad \ldots,\quad y^{(n-1)}(t_0) = y_{n-1}$$

The [[Existence_and_Uniqueness_Theorem|Existence and Uniqueness Theorem]] guarantees a unique solution under appropriate hypotheses on $f$.

---

## Existence and Uniqueness

### General case

If $f$ is continuous and Lipschitz in $y, y', \ldots, y^{(n-1)}$ near the initial point, the IVP has a unique solution **locally** (in a bubble around $t_0$).

### Linear case

If $p(t), q(t), h(t)$ are continuous on $(a,b)$, the IVP has a unique solution on **all of $(a,b)$** — a global guarantee. See [[Existence_and_Uniqueness_Theorem|Existence and Uniqueness Theorem]].

---

## ODEs as Dynamical Systems

Every ODE in normal form defines a **vector field** on a state space. For the first-order system $\mathbf{u}' = \mathbf{F}(t, \mathbf{u})$:

- The state $\mathbf{u}(t) \in \mathbb{R}^n$ is a point in state space
- $\mathbf{F}$ assigns a velocity vector to each point
- A solution is a **flow line** — a curve in state space tangent to the vector field at every point
- The [[Initial Value Problem]] picks a starting point; the flow carries it forward in time

This geometric picture underlies phase plane analysis, stability theory, and chaos.

---

## Examples Across Science

| Field | ODE | Models |
|-------|-----|--------|
| Mechanics | $m\ddot{x} + c\dot{x} + kx = f(t)$ | [[Spring-Mass-Dashpot]], pendulum |
| Circuits | $L\ddot{q} + R\dot{q} + q/C = \mathcal{E}(t)$ | RLC circuit |
| Biology | $\dot{N} = rN(1-N/K)$ | Logistic population growth |
| Chemistry | $\dot{N} = -\lambda N$ | Radioactive decay |
| Thermodynamics | $\dot{T} = -k(T-T_\infty)$ | Newton's cooling |
| Epidemiology | $\dot{S} = -\beta SI$, $\dot{I} = \beta SI - \gamma I$ | SIR model |
| Economics | $\dot{K} = sY - \delta K$ | Solow growth model |

---

## Key Equations

$$F(t,y,y',\ldots,y^{(n)}) = 0 \quad \text{(implicit form)}$$

$$y^{(n)} = f(t, y, y', \ldots, y^{(n-1)}) \quad \text{(normal form)}$$

$$a(t)y'' + b(t)y' + c(t)y = f(t) \quad \text{(2nd order linear)}$$

$$y'' = -p(t)y' - q(t)y + h(t) \quad \text{(normal form, 2nd order linear)}$$

$$\mathbf{u}' = \mathbf{F}(t,\mathbf{u}), \quad u_1 = y,\ u_2 = y' \quad \text{(reduction to system)}$$

$$y_{\text{general}} = c_1y_1 + \cdots + c_ny_n + y_p \quad \text{(general solution)}$$

---

## 📝 Notes
>

---

## Linked Concepts

- [[Second Order ODE]]
- [[Linear ODE]]
- [[Homogeneous Linear ODE]]
- [[Constant Coefficient ODE]]
- [[Initial Value Problem]]
- [[Existence_and_Uniqueness_Theorem|Existence and Uniqueness Theorem]]
- [[Superposition Principle]]
- [[Linear Operator Theory]]
- [[Fundamental Solutions]]
- [[Fundamental Set of Solutions]]
- [[Wronskian]]
- [[Abels Formula|Abel's Formula]]
- [[Characteristic Equation]]
- [[Spring-Mass-Dashpot]]
- [[Forcing Function]]
- [[Rate]]
- [[Vector space]]
- [[Continuity]]