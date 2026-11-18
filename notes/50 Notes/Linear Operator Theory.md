---
title: Linear Operator Theory
aliases:
  - linear operator
  - differential operator
  - linear map
  - operator theory
  - L[y]
topic: Linear Algebra / Differential Equations
course: AM 20
tags:
  - am20
  - linear-algebra
  - odes
  - operator-theory
  - differential-equations
type: concept
related:
  - "[[Linear ODE]]"
  - "[[Homogeneous Linear ODE]]"
  - "[[Superposition Principle]]"
  - "[[Vector space]]"
  - "[[Linear Transformation]]"
  - "[[Fundamental Solutions]]"
  - "[[Forcing Function]]"
status: draft
parent: "[[Math]]"
domain: math
---

# Linear Operator Theory

---

## Definition

> A **linear operator** is a map $L : V \to W$ between [[Vector space|vector spaces]] $V$ and $W$ satisfying:
>
> - **Additivity:** $L[u + v] = L[u] + L[v]$
> - **Homogeneity:** $L[cu] = c\,L[u]$ for all scalars $c$
>
> Equivalently: $L[c_1 u + c_2 v] = c_1 L[u] + c_2 L[v]$ for all $u, v \in V$ and $c_1, c_2 \in \mathbb{R}$.

---

## The Differential Operator $L$

In the context of [[Linear ODE|linear ODEs]], the key linear operator is:

$$L[y] = y'' + p(t)\,y' + q(t)\,y$$

This maps a twice-differentiable function $y$ to a new function $L[y]$.

- The [[Homogeneous Linear ODE]] is: $L[y] = 0$
- The nonhomogeneous [[Linear ODE]] is: $L[y] = h(t)$

### Verifying Linearity

$$L[c_1 y_1 + c_2 y_2]$$
$$= (c_1 y_1 + c_2 y_2)'' + p(c_1 y_1 + c_2 y_2)' + q(c_1 y_1 + c_2 y_2)$$
$$= c_1(y_1'' + py_1' + qy_1) + c_2(y_2'' + py_2' + qy_2)$$
$$= c_1 L[y_1] + c_2 L[y_2] \checkmark$$

This is precisely the [[Superposition Principle]].

---

## Kernel and Image

For a linear operator $L : V \to W$:

| Concept | Definition | ODE meaning |
|---------|-----------|-------------|
| **Kernel** $\ker(L)$ | $\{v \in V : L[v] = 0\}$ | All solutions of the homogeneous equation $L[y] = 0$ |
| **Image** $\text{im}(L)$ | $\{L[v] : v \in V\}$ | All functions $h(t)$ for which $L[y] = h$ has a solution |

### Key Facts

- $\ker(L)$ is always a [[Vector space|subspace]] of $V$ (the [[Homogeneous Linear ODE]] solution space)
- For a 2nd order operator, $\dim(\ker L) = 2$ — it has a 2-dimensional basis ([[Fundamental Solutions]])
- The nonhomogeneous equation $L[y] = h$ is solvable iff $h \in \text{im}(L)$

---

## The Rank-Nullity Theorem (Analogy)

From linear algebra: for a linear map $A : \mathbb{R}^n \to \mathbb{R}^m$:

$$\dim(\ker A) + \dim(\text{im}\, A) = n$$

For the differential operator $L$ on a suitable function space, an analogous structure holds — the dimension of the kernel (= 2 for a 2nd order ODE) constrains the solution space.

---

## General Solution via Operator Language

The general solution of $L[y] = h$ decomposes as:

$$y = \underbrace{y_h}_{\ker(L)} + \underbrace{y_p}_{\text{particular}}$$

- $y_h \in \ker(L)$: solves $L[y] = 0$, contains all free constants
- $y_p$: any single function with $L[y_p] = h$

**Why this works:** If $y$ and $y_p$ both solve $L[y] = h$, then:

$$L[y - y_p] = L[y] - L[y_p] = h - h = 0$$

So $y - y_p \in \ker(L)$, meaning $y - y_p = c_1 y_1 + c_2 y_2$, hence $y = y_h + y_p$.

---

## Superposition of Inputs

Because $L$ is linear, if:

$$L[y_1] = h_1 \quad \text{and} \quad L[y_2] = h_2$$

then:

$$L[\alpha y_1 + \beta y_2] = \alpha h_1 + \beta h_2$$

This means if a [[Forcing Function]] can be decomposed as $h = \alpha h_1 + \beta h_2$, we can solve for each piece separately and add the results. This is the foundation of **Fourier methods** and **Laplace transforms**.

---

## Common Linear Operators

| Operator | Notation | Action |
|----------|----------|--------|
| Differentiation | $D[y] = y'$ | Maps $y \mapsto y'$ |
| Second derivative | $D^2[y] = y''$ | Maps $y \mapsto y''$ |
| 2nd order ODE | $L[y] = y'' + py' + qy$ | Maps $y \mapsto y''+py'+qy$ |
| Integration | $I[f] = \int_a^t f(s)\,ds$ | Maps $f \mapsto$ its antiderivative |
| Identity | $I[y] = y$ | Maps $y \mapsto y$ |

All of these are linear. Note: $L[y] = y'' + py' + qy$ can be written using $D$:

$$L = D^2 + p(t)D + q(t) \cdot I$$

---

## Nonlinear Operators — What Breaks

An operator $N$ is **nonlinear** if it fails additivity or homogeneity. Examples:

| Operator | Why nonlinear |
|----------|--------------|
| $N[y] = y^2$ | $N[y_1 + y_2] = (y_1+y_2)^2 \neq y_1^2 + y_2^2$ |
| $N[y] = \sin(y)$ | $N[c\,y] = \sin(cy) \neq c\sin(y)$ |
| $N[y] = y\,y'$ | Product of $y$ and $y'$ — not linear in $y$ |

This is why $y' = y^2$ (the general case example) cannot be handled with the same structural tools as $y' = y$.

---

## Operator Norm and Boundedness

For operators on function spaces, **boundedness** is the infinite-dimensional analog of a matrix having finite entries:

$$\|L[y]\| \leq C\,\|y\| \quad \text{for some constant } C$$

Bounded linear operators are the "well-behaved" ones. The differential operator $D$ is actually **unbounded** on $L^2$ — this is why existence and regularity theorems for ODEs require careful hypotheses (continuity of $p, q, h$ in the [[Existence_and_Uniqueness_Theorem|Existence and Uniqueness Theorem]]).

---

## Eigenvalue Problems

For a linear operator $L$, an **eigenfunction** $\phi$ with **eigenvalue** $\lambda$ satisfies:

$$L[\phi] = \lambda\,\phi$$

For the operator $L = -D^2$ on $[0, \pi]$ with $\phi(0) = \phi(\pi) = 0$:

$$-\phi'' = \lambda\,\phi \implies \phi_n(x) = \sin(nx),\quad \lambda_n = n^2, \quad n = 1,2,3,\ldots$$

These eigenfunctions form a complete orthogonal basis — the foundation of **Fourier series** and **Sturm-Liouville theory**.

---

## Connection to Matrices

Every linear operator on a finite-dimensional space is a matrix. The operator $L$ on the solution space $\text{Span}\{y_1, y_2\}$ can be represented as a $2 \times 2$ matrix once a basis is chosen.

| Linear algebra | Operator theory |
|---------------|----------------|
| Matrix $A$ | Differential operator $L$ |
| $A\mathbf{x} = \mathbf{0}$ | $L[y] = 0$ (homogeneous ODE) |
| $A\mathbf{x} = \mathbf{b}$ | $L[y] = h$ (nonhomogeneous ODE) |
| Null space of $A$ | $\ker(L)$ — homogeneous solutions |
| Column space of $A$ | $\text{im}(L)$ — achievable right-hand sides |
| Eigenvalues of $A$ | Eigenvalues of $L$ |
| Determinant | [[Wronskian]] |

---

## Key Equations

$$L[y] = y'' + p(t)y' + q(t)y \quad \text{(2nd order differential operator)}$$

$$L[c_1 y_1 + c_2 y_2] = c_1 L[y_1] + c_2 L[y_2] \quad \text{(linearity)}$$

$$\ker(L) = \{y : L[y] = 0\} = \text{Span}\{y_1, y_2\} \quad \text{(2-dimensional)}$$

$$y_{\text{general}} = y_h + y_p, \quad y_h \in \ker(L),\quad L[y_p] = h \quad \text{(solution structure)}$$

$$L[\alpha y_1 + \beta y_2] = \alpha h_1 + \beta h_2 \quad \text{(superposition of inputs)}$$

---

## 📝 Notes
>

---

## Linked Concepts

- [[Linear ODE]]
- [[Homogeneous Linear ODE]]
- [[Superposition Principle]]
- [[Vector space]]
- [[Linear Transformation]]
- [[Fundamental Solutions]]
- [[Fundamental Set of Solutions]]
- [[Forcing Function]]
- [[Wronskian]]
- [[Characteristic Equation]]
- [[Eigenvalues]]
- [[Fourier Series]]
- [[Existence_and_Uniqueness_Theorem|Existence and Uniqueness Theorem]]
- [[Kernel]]
- [[Image]]

## See Also

- [[AM 20 – Lecture 10: 2nd Order Linear ODEs I]]
