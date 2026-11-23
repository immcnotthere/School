---
title: Superposition Principle
aliases:
  - superposition
  - linearity of solutions
  - superposition of inputs
  - superposition of outputs
  - principle of superposition
topic: Differential Equations / Linear Algebra / Physics
course: AM 20
tags:
  - am20
  - odes
  - differential-equations
  - superposition
  - linearity
  - linear-operator
  - physics
  - signals
type: theorem
related:
  - "[[Homogeneous Linear ODE]]"
  - "[[Linear ODE]]"
  - "[[Linear Operator Theory]]"
  - "[[Vector space]]"
  - "[[Fundamental Solutions]]"
  - "[[Forcing Function]]"
  - "[[Kernel]]"
status: draft
parent: "[[Math]]"
domain: math
---

# Superposition Principle

---

## Core Idea

> **Whenever a system is governed by a linear rule, its responses to multiple inputs can be computed separately and then added.**

This single idea underlies ODEs, linear algebra, quantum mechanics, signal processing, circuit theory, acoustics, and optics. The ODE version is one instance of a universal structural fact about [[Linear Operator Theory|linear operators]]. 

---

## General Statement (Operator Form)

Let $L$ be any [[Linear Operator Theory|linear operator]] on a [[Vector space]] $V$. Then for any $u, v \in V$ and scalars $c_1, c_2 \in \mathbb{R}$:

$$\boxed{L[c_1 u + c_2 v] = c_1\,L[u] + c_2\,L[v]}$$

This single equation encodes both forms of superposition:

| Form | Setting | What it says |
|------|---------|-------------|
| **Superposition of solutions** | $L[u] = 0$, $L[v] = 0$ | $L[c_1u + c_2v] = 0$ — combinations of solutions are solutions |
| **Superposition of inputs** | $L[u] = f$, $L[v] = g$ | $L[c_1u + c_2v] = c_1f + c_2g$ — responses add when inputs add |

---

## Form 1 — Superposition of Solutions

### Statement

If $y_1$ and $y_2$ are both solutions of the [[Homogeneous Linear ODE]]:

$$y'' + p(t)\,y' + q(t)\,y = 0 \tag{$\star$}$$

on $(a,b)$, then for any $c_1, c_2 \in \mathbb{R}$:

$$\tilde{y} = c_1 y_1 + c_2 y_2$$

is also a solution of $(\star)$ on $(a,b)$.

### Proof

$$\tilde{y}'' + p\tilde{y}' + q\tilde{y}$$
$$= (c_1 y_1 + c_2 y_2)'' + p(c_1 y_1 + c_2 y_2)' + q(c_1 y_1 + c_2 y_2)$$
$$= c_1(y_1'' + py_1' + qy_1) + c_2(y_2'' + py_2' + qy_2)$$
$$= c_1 \cdot 0 + c_2 \cdot 0 = 0 \checkmark$$

### Consequence: Solution Space is a [[Vector space]]

The solution set of $(\star)$ is closed under addition and scalar multiplication, and contains $\mathbf{0}$ (since $y = 0$ always solves $(\star)$). Therefore it is a vector space — of **dimension 2** for a 2nd order equation, with basis $\{y_1, y_2\}$ ([[Fundamental Set of Solutions]]).

---

## Form 2 — Superposition of Inputs

### Statement

If $L[y_1] = h_1$ and $L[y_2] = h_2$, then:

$$L[\alpha y_1 + \beta y_2] = \alpha h_1 + \beta h_2$$

### What this buys

If a [[Forcing Function]] can be decomposed as $h = \alpha h_1 + \beta h_2$, the particular solutions for each piece can be found separately and summed. This is the engine behind:

- **Fourier series**: decompose $h(t)$ into sinusoids, solve for each, add responses
- **Laplace transforms**: linearity of $\mathcal{L}$ lets you handle sums of inputs term by term
- **Green's functions**: treat $h(t)$ as a continuous sum of impulses $\delta(t - s)$, superpose the impulse responses

---

## Why Homogeneity Is Required

Superposition of *solutions* fails for nonhomogeneous equations. If $y_1$ and $y_2$ both solve $L[y] = h \neq 0$, then:

$$L[c_1 y_1 + c_2 y_2] = (c_1 + c_2)\,h$$

which equals $h$ only when $c_1 + c_2 = 1$ — not for arbitrary scalars.

The correct structure for the nonhomogeneous case is:

$$y_{\text{general}} = \underbrace{c_1 y_1 + c_2 y_2}_{y_h \,\in\, \ker(L)} + \underbrace{y_p}_{\text{particular solution}}$$

- $y_h$: full freedom from the homogeneous part — superposition applies here
- $y_p$: any single solution of $L[y] = h$ — pins the solution to the right output

---

## Generalizations

### $n$th Order ODEs

For an $n$th order linear ODE with solutions $y_1, \ldots, y_n$:

$$y = c_1 y_1 + c_2 y_2 + \cdots + c_n y_n$$

is the general solution. The solution space has dimension $n$.

### Systems of ODEs

For a linear system $\mathbf{y}' = A(t)\mathbf{y}$, if $\mathbf{y}_1$ and $\mathbf{y}_2$ are solutions then so is $c_1\mathbf{y}_1 + c_2\mathbf{y}_2$. The solution space has dimension $n$ (the size of the system).

### Partial Differential Equations

The heat equation $u_t = \alpha u_{xx}$, the wave equation $u_{tt} = c^2 u_{xx}$, and Laplace's equation $\nabla^2 u = 0$ are all linear PDEs — superposition applies directly and underlies the entire theory of Fourier series solutions.

### Quantum Mechanics

The Schrödinger equation $i\hbar\,\partial_t\psi = \hat{H}\psi$ is linear in $\psi$. If $\psi_1$ and $\psi_2$ are valid quantum states, so is $c_1\psi_1 + c_2\psi_2$. This is the origin of **quantum superposition** — particles exist in linear combinations of states until measured.

### Circuit Theory

In a linear circuit with multiple sources, the voltage or current at any element equals the sum of the contributions from each source acting alone (all others set to zero). A direct application of operator superposition to Kirchhoff's laws.

### Acoustics and Optics

Sound waves and light waves obey linear wave equations. Two waves passing through the same point superpose — amplitudes add algebraically, producing constructive or destructive interference.

---

## Linear Algebra Analogy

| Linear algebra | Superposition principle |
|---------------|------------------------|
| Null space $\ker(A) = \{\mathbf{x}: A\mathbf{x}=\mathbf{0}\}$ | Solution space of $L[y]=0$ |
| $A\mathbf{x}=\mathbf{0} \Rightarrow A(c_1\mathbf{x}_1+c_2\mathbf{x}_2)=\mathbf{0}$ | $L[y]=0 \Rightarrow L[c_1y_1+c_2y_2]=0$ |
| Column space / image of $A$ | Set of achievable forcing functions $h$ |
| Particular solution $\mathbf{x}_p$ of $A\mathbf{x}=\mathbf{b}$ | Particular solution $y_p$ of $L[y]=h$ |
| General solution $\mathbf{x}_h + \mathbf{x}_p$ | General solution $y_h + y_p$ |
| Basis of null space | [[Fundamental Set of Solutions]] |

---

## What Breaks Superposition

Superposition holds **only for linear systems**. The following all violate it:

| System | Why superposition fails |
|--------|------------------------|
| $y' = y^2$ | $(y_1+y_2)^2 \neq y_1^2 + y_2^2$ |
| $y'' + \sin(y) = 0$ | $\sin(y_1+y_2) \neq \sin y_1 + \sin y_2$ |
| Navier-Stokes | Nonlinear convective term $(\mathbf{u}\cdot\nabla)\mathbf{u}$ |
| General relativity | Einstein field equations are nonlinear in the metric |
| Systems with saturation | Amplifiers, biological systems — output saturates at large inputs |

Nonlinear systems admit behavior with no linear analog: bifurcations, chaos, limit cycles, solitons.

---

## Key Equations

$$L[c_1 u + c_2 v] = c_1 L[u] + c_2 L[v] \quad \text{(general superposition)}$$

$$L[y_1] = L[y_2] = 0 \implies L[c_1y_1+c_2y_2] = 0 \quad \text{(homogeneous form)}$$

$$L[y_i] = h_i \implies L\!\left[\textstyle\sum \alpha_i y_i\right] = \sum \alpha_i h_i \quad \text{(input form)}$$

$$y_{\text{general}} = c_1y_1 + c_2y_2 + y_p \quad \text{(full nonhomogeneous solution)}$$

---

## 📝 Notes
>

---

## Linked Concepts

- [[Linear Operator Theory]]
- [[Homogeneous Linear ODE]]
- [[Linear ODE]]
- [[Vector space]]
- [[Linear Independence]]
- [[Fundamental Solutions]]
- [[Fundamental Set of Solutions]]
- [[Forcing Function]]
- [[Second Order ODE]]
- [[Kernel]]
- [[Fourier Series]]
- [[Laplace Transform]]
- [[Green's Function]]
- [[Wave Equation]]
- [[Heat Equation]]
- [[Quantum Mechanics]]

## See Also

- [[AM 20 – Lecture 10: 2nd Order Linear ODEs I]]
- [[Linear Operator Theory]] — the abstract framework of which this is one instance