---
parent: "[[AM20]]"
title: "Change"
tags: [concept/foundational, math/calculus, AM20]
related: ["[[Theory]]", "[[Behavior]]", "[[Differentials]]", "[[Limits]]", "[[First Order ODE]]"]
type: concept
status: draft
---

# Change

**Change** is the central object of calculus and differential equations. A theory that says how a variable *changes* is more powerful than one that says what it *is* — because change compresses the entire future of a system into a single rule.

## Change as a Rate

The most precise way to measure change is the **derivative** — the instantaneous rate of change:

$$\frac{dy}{dt} = \lim_{\Delta t \to 0} \frac{y(t + \Delta t) - y(t)}{\Delta t}$$

This asks: how fast is $y$ moving right now?

## Discrete vs. Continuous Change

| Type | Description | Tool |
|---|---|---|
| **Discrete** | Change happens in steps | Difference equations, sequences |
| **Continuous** | Change happens at every instant | Differential equations |

Most natural phenomena change continuously. This is why ODEs appear everywhere in physics, biology, and economics.

## Change in One Variable vs. Many

| | Variable | Equation type |
|---|---|---|
| One independent variable | $y(t)$ | ODE |
| Multiple independent variables | $y(x,t)$ | PDE (partial differential equation) |

AM20 focuses on ODEs — one independent variable, usually time $t$.

## Why "Behave = Change = Derivatives"

The chain:

$$\text{theory describes behavior} \implies \text{behavior means change} \implies \text{change means derivatives} \implies \text{differential equation}$$

Every ODE in the course is just a precise statement about how something changes. Newton's second law says force equals mass times acceleration — acceleration is the second derivative of position. The law of cooling says temperature changes proportionally to the temperature difference. Exponential growth says population changes proportionally to population size.

> [!note]
> The moment you write down *how* something changes, you have written a differential equation. Solving it tells you *what* the thing actually is at every future time.