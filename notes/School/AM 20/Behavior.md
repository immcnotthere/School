---
parent: "[[AM20]]"
title: "Behavior"
tags: [concept/foundational, math/ODE, AM20]
related: ["[[Theory]]", "[[Change]]", "[[Limits]]", "[[Steady State Solution]]", "[[Homogenous (Transient) Solution|Homogeneous (Transient) Solution]]"]
type: concept
status: draft
---

# Behavior

In mathematics and differential equations, **behavior** describes the qualitative character of a solution — not just what value it takes, but what it *does* over time. Does it grow? Decay? Oscillate? Blow up? Settle?

## Why Behavior Matters

Knowing the exact formula for $y(t)$ is one thing. Understanding its behavior is another — and often more useful. An engineer needs to know whether a bridge oscillates and decays or oscillates and grows. The exact numbers come second.

## Types of Behavior in ODEs

| Behavior | Description | Caused by |
|---|---|---|
| **Exponential growth** | $y \to \infty$ as $t \to \infty$ | Positive real characteristic root |
| **Exponential decay** | $y \to 0$ as $t \to \infty$ | Negative real characteristic root |
| **Pure oscillation** | Bounded, periodic, no decay | Pure imaginary roots $\pm i\omega$ |
| **Damped oscillation** | Oscillates toward zero | Complex roots $\lambda \pm i\omega$, $\lambda < 0$ |
| **Growing oscillation** | Oscillates with increasing amplitude | Complex roots with $\lambda > 0$ |
| **Constant** | $y$ does not change | Root $r = 0$ |

## Reading Behavior from the Characteristic Roots

For $ay'' + by' + cy = 0$ with roots $r_1, r_2$:

$$\text{sign of real part} \implies \text{growth or decay}$$
$$\text{imaginary part} \implies \text{oscillation}$$

The behavior as $t \to \infty$ is determined entirely by whichever root has the **largest real part**.

## Long-Run Behavior

The key question is always: what does $y(t)$ do as $t \to \infty$?

For the nonhomogeneous equation $ay'' + by' + cy = f(t)$:

- The **homogeneous solution** $y_h$ governs the transient behavior — it dies out when roots have negative real parts
- The **particular solution** $y_p$ governs the long-run or steady-state behavior

> [!tip]
> Behavior is the bridge between the algebra of solving and the physics of interpreting. Once you know the roots, you know the story of the solution without needing to plot it.