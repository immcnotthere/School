---
parent: "[[AM20]]"
title: "Week 1 Reading"
tags: [MATH, AM20, differential-equations]
type: lecture
status: draft
---

# Chapter 1: Introduction

## 1.1 Applications Leading to Differential Equations

Mathematical models often involve equations relating an unknown function and its derivatives. All examples here deal with functions of time $t$, with $y' = dy/dt$.

### Population Growth and Decay

$$P' = a(P)\cdot P \tag{1.1.1}$$

**Malthusian model** — $a$ constant:

$$P' = aP \tag{1.1.2}$$

Solutions $P = ce^{at}$, so $P(t) = P_0 e^{at}$. **Equilibrium** at $P = 0$: unstable if $a > 0$, stable if $a < 0$.

**Verhulst (logistic) model:**

$$P' = aP(1 - \alpha P) \tag{1.1.4}$$

$$P = \frac{P_0}{\alpha P_0 + (1 - \alpha P_0)e^{-at}}$$

**Equilibria:** $P = 0$ (unstable) and $P = 1/\alpha$ (asymptotically stable). All solutions with $P_0 > 0$ satisfy $\lim_{t\to\infty} P(t) = 1/\alpha$.

### Newton's Law of Cooling

$$T' = -k(T - T_m) \tag{1.1.5}$$

$k > 0$, so $T_m$ is an **asymptotically stable equilibrium**. Solution: $T = T_m + (T_0 - T_m)e^{-kt}$.

When the medium temperature also changes, energy conservation $a(T - T_0) + a_m(T_m - T_{m0}) = 0$ yields a modified ODE whose solution is:

$$T = \frac{aT_0 + a_m T_{m0}}{a + a_m} + \frac{a_m(T_0 - T_{m0})}{a + a_m}e^{-k(1 + a/a_m)t}$$

### Glucose Absorption

$$G' = -\lambda G \tag{1.1.7}$$

With intravenous injection at rate $r$:

$$G' = -\lambda G + r \tag{1.1.9}$$

Equilibrium at $G = r/\lambda$ (asymptotically stable). Solution: $G = \dfrac{r}{\lambda} + \!\left(G_0 - \dfrac{r}{\lambda}\right)e^{-\lambda t}$.

### Spread of Epidemics

$$I' = rI(S - I)$$

Solution: $I = \dfrac{SI_0}{I_0 + (S - I_0)e^{-rSt}}$. Equilibria at $I = 0$ (unstable) and $I = S$ (stable), so all susceptible people eventually become infected.

### Newton's Second Law of Motion

$$y'' + q(y,y')y' + p(y) = f(t)$$

**Second order** ODE. Classification note: nonlinear if $q$ or $p$ depend on $y$ or $y'$.

### Interacting Species: Competition

$$P' = aP - \alpha Q, \qquad Q' = -\beta P + bQ \tag{1.1.10}$$

A line $L$ through the origin separates initial conditions leading to extinction of one species or the other.

---

## 1.2 Basic Concepts

### Classification

A **differential equation** contains one or more derivatives of an unknown function. Key classifications:

| Property | Definition |
|----------|-----------|
| **Order** | Highest derivative present |
| **ODE** | Unknown function of one variable only |
| **PDE** | Involves partial derivatives (more than one independent variable) |
| **Linear** | Can be written $y^{(n)} + p_{n-1}(x)y^{(n-1)} + \cdots + p_0(x)y = f(x)$ — coefficients depend only on $x$, not $y$ |
| **Nonlinear** | $y$ appears squared, inside $\sin(y)$, $e^y$, or as $yy'$, etc. |

A **first-order ODE is linear** if and only if it can be written:

$$y' + p(x)y = f(x)$$

This is the form required for the **Integrating Factor method**. If $y$ is squared, inside a trig function, or multiplied by its own derivative, the equation is **nonlinear** and requires a different approach.

**Examples of classification:**

$$\frac{dy}{dx} - x^2 = 0 \quad \text{(1st order, linear)}$$

$$\frac{d^2y}{dx^2} + 2\frac{dy}{dx} + y = 2x \quad \text{(2nd order, linear)}$$

$$xy'' + y^2 = \sin x \quad \text{(2nd order, nonlinear — } y^2 \text{)}$$

General form:

$$y^{(n)} = f(x,\, y,\, y',\, \ldots,\, y^{(n-1)}) \tag{1.2.2}$$

### Solutions, Solution Curves, and Integral Curves

A **solution** of a differential equation is a function satisfying it on some **open interval** $(a, b)$. Its graph is a **solution curve**.

An **integral curve** is a curve where every function-segment is a solution — but the full curve need not be a single function.

> **Critical distinction:** The circle $x^2 + y^2 = a^2$ is an integral curve of $y' = -x/y$ but *not* a solution curve. It fails the vertical line test, so it's actually composed of two separate solutions: $y = \sqrt{a^2 - x^2}$ and $y = -\sqrt{a^2 - x^2}$, each defined on the open interval $(-a, a)$.

This matters for identifying the **interval of validity** — the largest open interval containing $x_0$ on which the solution is defined and satisfies the equation.

**Example 1.2.2.** $y = \dfrac{x^2}{3} + \dfrac{1}{x}$ solves $xy' + y = x^2$ on $(0,\infty)$ and $(-\infty,0)$ — two separate intervals since $y$ is undefined at $x = 0$.

**Example 1.2.3.** $y = (c_1 + c_2 x)e^{-x} + 2x - 4$ solves $y'' + 2y' + y = 2x$ on $(-\infty,\infty)$.

**Example 1.2.4.** All solutions of $y^{(n)} = e^{2x}$:

$$y = \frac{e^{2x}}{2^n} + c_1 + c_2 x + \cdots + c_n x^{n-1}$$

### Initial Value Problems

An **IVP** specifies $y$ and its first $n-1$ derivatives at a point $x_0$:

$$y'' - 2y' + 3y = e^x, \quad y(0) = 1,\quad y'(0) = 2 \tag{1.2.11}$$

**Example 1.2.5.** $y' = x^3$, $y(1) = 2$ $\Rightarrow$ $y = \dfrac{x^4 + 7}{4}$, valid on $(-\infty,\infty)$.

**Example 1.2.8 (Free Fall).**

$$y'' = -g, \quad y(0) = y_0, \quad y'(0) = v_0 \tag{1.2.17}$$

$$y = -\frac{g}{2}t^2 + v_0 t + y_0$$

---

## 1.3 Direction Fields and Qualitative Analysis

### Direction Fields

For $y' = f(x, y)$ when an explicit solution is impossible, draw a **direction field**: a short line segment with slope $f(x_i, y_j)$ at each grid point. Integral curves flow tangent to these segments.

For $y' = A(x,y)/B(x,y)$, software solves $dx/dt = B$, $dy/dt = A$ parametrically. The integral curves of $y' = -x/y$ are circles centered at the origin.

### Equilibrium Solutions and Stability

An **equilibrium solution** is a constant function $y = c$ satisfying $f(x, c) = 0$ for all $x$. These appear as horizontal lines in a direction field.

**Stability classification** for $y' = f(y)$ (autonomous equations):

| Type | Behavior of nearby solutions | Condition |
|------|------------------------------|-----------|
| **Asymptotically stable** | Approach $y = c$ as $t \to \infty$ | $f'(c) < 0$ |
| **Unstable** | Move away from $y = c$ | $f'(c) > 0$ |
| **Semi-stable** | Approach from one side, diverge from the other | $f'(c) = 0$ |

This lets you predict **long-term behavior without solving** the ODE.

**Example — logistic equation** $P' = aP(1 - \alpha P)$: equilibria at $P = 0$ (unstable, $f'(0) = a > 0$) and $P = 1/\alpha$ (stable, $f'(1/\alpha) = -a < 0$).

### Euler's Method (Numerical Approximation)

When no closed-form solution exists, **Euler's method** steps through an approximate solution using:

$$y(x + h) \approx y(x) + f(x, y) \cdot h$$

Starting from $(x_0, y_0)$, iterate to get $y_1, y_2, \ldots$ at $x_1 = x_0 + h$, $x_2 = x_0 + 2h$, etc. Smaller step size $h$ gives better accuracy. This is the foundation for numerical methods in Chapter 3 (Improved Euler, Runge-Kutta) and MATLAB's `ode45`.

---

## Skill Summary

| Skill | Question to ask |
|-------|----------------|
| **Classify** | What order? Linear or nonlinear? ODE or PDE? |
| **Equilibrium** | Where is $f(x,c) = 0$? Stable, unstable, or semi-stable? |
| **Approximate** | Can I apply Euler's method? What step size? |
| **Interval of validity** | Where is the solution defined? Does it hit a singularity? |
