---
title: "Continuity"
aliases:
  - continuous
  - continuous case
  - Continuous Function
  - continuous function
  - continuous random variables
  - continuous-time Markov chain
topic: "Analysis / Differential Equations"
course: "AM 20"
tags:
  - am20
  - analysis
  - continuity
  - differential-equations
type: concept
related:
  - "[[Existence_and_Uniqueness_Theorem|Existence and Uniqueness Theorem]]"
  - "[[Linear ODE]]"
  - "[[Homogeneous Linear ODE]]"
  - "[[Abels Formula|Abel's Formula]]"
  - "[[Initial Value Problem]]"
status: draft
parent: "[[Math]]"
domain: math
---

# Continuity

---

## Definition

> A function $f : (a,b) \to \mathbb{R}$ is **continuous** at a point $t_0 \in (a,b)$ if:
> $$\lim_{t \to t_0} f(t) = f(t_0)$$
> It is **continuous on $(a,b)$** if it is continuous at every point of the interval.

Intuitively: no jumps, holes, or blowups — the graph can be drawn without lifting the pen.

---

## Equivalent Formulations

| Formulation | Statement |
|-------------|-----------|
| $\varepsilon$-$\delta$ | $\forall \varepsilon > 0,\ \exists \delta > 0$ such that $|t - t_0| < \delta \implies |f(t) - f(t_0)| < \varepsilon$ |
| Sequential | $t_n \to t_0 \implies f(t_n) \to f(t_0)$ |
| Limit form | $\lim_{t \to t_0} f(t)$ exists and equals $f(t_0)$ |

---

## Why Continuity Matters in ODEs

Continuity of the coefficient functions $p(t)$, $q(t)$, $h(t)$ is the key hypothesis of the [[Existence_and_Uniqueness_Theorem|Existence and Uniqueness Theorem]] for linear ODEs:

> If $p(t)$, $q(t)$, $h(t)$ are **continuous** on $(a,b)$, then the IVP $y'' + py' + qy = h$, $y(t_0) = y_0$, $y'(t_0) = y_1$ has a unique solution on **all of $(a,b)$**.

Without continuity, the solution might only exist locally or fail to exist at all.

Continuity also appears in:
- [[Abels Formula|Abel's Formula]] — $p(t)$ continuous ensures $\int p\,dt$ is well-defined
- The [[Wronskian]] ODE $W' + p(t)W = 0$ — solvable because $p$ is continuous
- [[Fundamental Solutions]] — existence guaranteed on any interval of continuity of $p, q$

---

## Continuity vs. Differentiability

$$\text{Differentiable} \implies \text{Continuous} \implies \text{Integrable (Riemann)}$$

The converse implications fail in general (e.g. $|t|$ is continuous but not differentiable at $t=0$).

---

## Continuous Function

A **continuous function** on an interval $(a,b)$ is one with no discontinuities — the function $f(t)$ is defined and matches its limit at every interior point.

Common continuous functions: polynomials, $e^t$, $\sin t$, $\cos t$, $\ln t$ (on $t > 0$), and sums/products/compositions of these.

---

## Continuous Case (ODEs)

In the context of the [[Existence_and_Uniqueness_Theorem|Existence and Uniqueness Theorem]], the **continuous case** refers to the [[Linear ODE]] setting where $p(t)$, $q(t)$, $h(t) \in C(a,b)$ — this upgrades local existence (the general nonlinear case) to **global** existence on all of $(a,b)$.

---

## Continuous Random Variables

A **continuous random variable** $X$ takes values in an uncountable set (typically an interval $[a,b]$ or $\mathbb{R}$) and is described by a **probability density function** (PDF) $f_X(x) \geq 0$ with:

$$P(a \leq X \leq b) = \int_a^b f_X(x)\,dx, \qquad \int_{-\infty}^{\infty} f_X(x)\,dx = 1$$

Key properties:
- $P(X = x) = 0$ for any single value (unlike discrete RVs)
- CDF: $F_X(x) = P(X \leq x) = \int_{-\infty}^x f_X(t)\,dt$
- $F_X$ is **continuous** (hence the name)

Common continuous distributions: Uniform, Normal/Gaussian, Exponential, Gamma, Beta.

---

## Continuous-Time Markov Chain (CTMC)

A **continuous-time Markov chain** is a stochastic process $\{X(t)\}_{t \geq 0}$ with:
- A **countable** state space $S$
- The **Markov property**: $P(X(t+s) = j \mid X(u),\, u \leq s) = P(X(t+s) = j \mid X(s))$
- **Continuous time** parameter $t \in [0, \infty)$

The process is characterized by its **generator matrix** (or **$Q$-matrix**) $Q = (q_{ij})$:
- $q_{ij} \geq 0$ for $i \neq j$ (transition rates)
- $q_{ii} = -\sum_{j \neq i} q_{ij}$

The time spent in state $i$ before jumping is exponentially distributed with rate $|q_{ii}|$.

Contrast with a **discrete-time** Markov chain, which transitions only at integer steps $n = 0, 1, 2, \ldots$

---

## Key Equations

$$\lim_{t \to t_0} f(t) = f(t_0) \quad \text{(continuity at } t_0\text{)}$$

$$p, q, h \in C(a,b) \implies \text{IVP has unique solution on } (a,b) \quad \text{(E\&U theorem)}$$

$$P(a \leq X \leq b) = \int_a^b f_X(x)\,dx \quad \text{(continuous RV)}$$

$$W(t) = C\,e^{-\int_{t_0}^t p(s)\,ds} \quad \text{(requires } p \text{ continuous; [[Abels Formula|Abel's Formula]])}$$

---

## 📝 Notes
>

---

## Linked Concepts

- [[Existence_and_Uniqueness_Theorem|Existence and Uniqueness Theorem]]
- [[Linear ODE]]
- [[Homogeneous Linear ODE]]
- [[Initial Value Problem]]
- [[Abels Formula|Abel's Formula]]
- [[Wronskian]]
- [[Fundamental Solutions]]
- [[Second Order ODE]]

## See Also

- [[AM 20 – Lecture 10: 2nd Order Linear ODEs I]]
