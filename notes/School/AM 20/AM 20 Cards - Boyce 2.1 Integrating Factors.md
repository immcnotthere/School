---
type: reference
parent: "[[AM20]]"
domain: math
course: "AM 20"
status: draft
source: "Boyce 2.1 Integrating Factors"
tags:
  - decks
---
# AM 20 Cards - Boyce 2.1 Integrating Factors: Linear Equations, Method of Integrating Factors

## Integrating-Factor
| Front | Back | Notes |
| --- | --- | --- |
| What is an integrating factor $\mu(t)$ for a linear ODE? | A function that, when both sides of the ODE are multiplied by it, makes the left side the exact derivative of a product $\mu(t)y$, so the equation becomes directly integrable. | p.54-55; definition |
| What are the steps to solve $dy/dt + p(t)y = g(t)$ by the integrating factor method? | (1) Put the equation in standard form. (2) Compute $\mu(t) = \exp\int p(t)\,dt$. (3) Multiply the equation by $\mu(t)$. (4) Recognize the left side as $\dfrac{d}{dt}[\mu(t)y]$ and integrate both sides. (5) Solve for $y$. | p.58-59; procedure |
| Why must $\mu(t)$ in $\mu(t) = \exp\int p(t)\,dt$ be positive for all $t$? | Because $k=0$ is chosen for the simplest integrating factor, and $\exp(\cdot)$ of any real quantity is always positive; this makes $\mu(t)$ never zero, so dividing by it later is always valid. | p.58; definition |

## Variation Of Parameters
| Front | Back | Notes |
| --- | --- | --- |
| In the variation of parameters method for $y' + p(t)y = g(t)$, what form is assumed for the solution? | $y = A(t)\exp\left(-\displaystyle\int p(t)\,dt\right)$, replacing the constant $A$ in the homogeneous solution with an unknown function $A(t)$. | p.63-64; procedure |
| What differential equation must $A(t)$ satisfy in variation of parameters? | $A'(t) = g(t)\exp\left(\displaystyle\int p(t)\,dt\right)$ | p.64; formula |

## Unevaluable-Integral Linear IVP
| Front | Back | Notes |
| --- | --- | --- |
| Solve $2y' + ty = 2$, $y(0) = 1$. What is $\mu(t)$, and why must the answer be left as an integral? | Standard form $y' + (t/2)y = 1$, so $\mu(t) = e^{t^2/4}$. The resulting integral $\int e^{s^2/4}\,ds$ has no elementary antiderivative, so the solution is left as $y = e^{-t^2/4}\left(\displaystyle\int_0^t e^{s^2/4}\,ds + c\right)$ with $c=1$. | p.60-61; key move |

## Direct Product Rule and IVP for a Simple Linear ODE
| Front | Back | Notes |
| --- | --- | --- |
| In $(4+t^2)y' + 2ty = 4t$, why is no separate integrating-factor step needed? | The left side is already the exact derivative of a product: $(4+t^2)y' + 2ty = \dfrac{d}{dt}[(4+t^2)y]$, so the equation can be integrated directly. | p.54; discrimination |

## Canonical Form of a First-Order Linear ODE
| Front | Back | Notes |
| --- | --- | --- |
| What is the standard form of a first order linear ODE, and what condition lets you convert $P(t)y' + Q(t)y = G(t)$ into it? | Standard form: $dy/dt + p(t)y = g(t)$. Divide by $P(t)$, valid as long as $P(t) \neq 0$. | p.54; formula |

## Interval of Validity (First-Order Linear ODE)
| Front | Back | Notes |
| --- | --- | --- |
| In $y' + (2/t)y = 4t$ with $y(1)=2$, why is the solution $y = t^2 + 1/t^2$ only valid for $t>0$? | The coefficient $p(t)=2/t$ has an infinite discontinuity at $t=0$; the solution is restricted to the interval containing $t_0=1$ on which $p(t)$ stays continuous. | p.59-60; discrimination |

# Node map
```json
[
 {
  "name": "Integrating-Factor",
  "type": "concept",
  "existing": true,
  "parent": "Linear ODE",
  "prereqs": [
   "Linear ODE"
  ],
  "uses": [],
  "page": 54,
  "summary": "A function $\\mu(t)=\\exp\\int p(t)\\,dt$ that makes the left side of a linear ODE an exact derivative of a product, enabling direct integration."
 },
 {
  "name": "Linear ODE",
  "type": "concept",
  "existing": true,
  "parent": "Differential Equation",
  "prereqs": [],
  "uses": [],
  "page": 54,
  "summary": "Standard form $dy/dt+p(t)y=g(t)$ for first order linear equations; obtained by dividing by the leading coefficient."
 },
 {
  "name": "Discontinuity",
  "type": "concept",
  "existing": true,
  "parent": "Linear ODE",
  "prereqs": [
   "Integrating-Factor",
   "Initial Value Problem"
  ],
  "uses": [],
  "page": 59,
  "summary": "Infinite discontinuities in a linear ODE's coefficient functions restrict the interval on which its solution is valid."
 },
 {
  "name": "Variation Of Parameters",
  "type": "concept",
  "existing": true,
  "parent": "Linear ODE",
  "prereqs": [
   "Integrating-Factor"
  ],
  "uses": [],
  "page": 63,
  "summary": "Alternate solution method for linear ODEs: assume $y=A(t)\\exp(-\\int p\\,dt)$ and solve for $A(t)$; equivalent to the integrating factor result."
 },
 {
  "name": "Non-Constant-Coefficient Linear IVP",
  "type": "problem",
  "existing": false,
  "parent": "Linear ODE",
  "prereqs": [
   "Integrating-Factor"
  ],
  "uses": [
   "Integrating-Factor",
   "Linear ODE",
   "Discontinuity",
   "Initial Value Problem"
  ],
  "page": 59,
  "summary": "$ty'+2y=4t^2$, $y(1)=2$ solved via $\\mu(t)=t^2$, giving $y=t^2+1/t^2$ for $t>0$."
 },
 {
  "name": "Unevaluable-Integral Linear IVP",
  "type": "problem",
  "existing": false,
  "parent": "Linear ODE",
  "prereqs": [
   "Integrating-Factor"
  ],
  "uses": [
   "Integrating-Factor",
   "Linear ODE"
  ],
  "page": 60,
  "summary": "$2y'+ty=2$, $y(0)=1$ solved via $\\mu(t)=e^{t^2/4}$; the resulting integral has no elementary closed form."
 },
 {
  "name": "Direct Product Rule and IVP for a Simple Linear ODE",
  "type": "concept",
  "existing": true,
  "parent": "",
  "prereqs": [],
  "summary": ""
 },
 {
  "name": "Canonical Form of a First-Order Linear ODE",
  "type": "concept",
  "existing": true,
  "parent": "",
  "prereqs": [],
  "summary": ""
 },
 {
  "name": "Interval of Validity (First-Order Linear ODE)",
  "type": "concept",
  "existing": true,
  "parent": "",
  "prereqs": [],
  "summary": ""
 }
]
```

# Frankenstein problems

**FP1: Linear IVP with a discontinuity check**
Solve $ty' + 3y = t^2$, $y(1) = 1$, and state the interval of validity, given the discontinuity in the standard-form coefficient at $t=0$.

**Solution.** Standard form: $y' + (3/t)y = t$, so $p(t) = 3/t$.
Integrating factor: $\mu(t) = \exp\int (3/t)\,dt = \exp(3\ln|t|) = t^3$ (for $t>0$).
Multiply: $t^3y' + 3t^2y = t^4 \Rightarrow \dfrac{d}{dt}(t^3y) = t^4$.
Integrate: $t^3y = \dfrac{t^5}{5} + c \Rightarrow y = \dfrac{t^2}{5} + \dfrac{c}{t^3}$.
Apply $y(1) = 1$: $1 = \dfrac{1}{5} + c \Rightarrow c = \dfrac{4}{5}$.
So $y(t) = \dfrac{t^2}{5} + \dfrac{4}{5t^3}$.
Since $p(t)=3/t$ has an infinite discontinuity at $t=0$ and $t_0=1>0$, the solution is valid on $t>0$.
Concepts tested: Integrating-Factor, Linear ODE, Discontinuity, Initial Value Problem.

**FP2: Integrating factor vs. variation of parameters**
For $y' + 2y = e^{-t}$: (a) solve using the integrating factor method. (b) Solve using variation of parameters with $y = A(t)e^{-2t}$, and verify the two methods agree.

**Solution.** (a) Here $p(t)=2$, so $\mu(t) = e^{2t}$. Multiplying: $e^{2t}y' + 2e^{2t}y = e^{2t}e^{-t} = e^{t}$, i.e. $\dfrac{d}{dt}(e^{2t}y) = e^{t}$. Integrating: $e^{2t}y = e^{t} + c$, so $y = e^{-t} + ce^{-2t}$.
(b) The homogeneous solution factor is $\exp(-\int 2\,dt) = e^{-2t}$, so assume $y = A(t)e^{-2t}$. Then $A'(t) = g(t)\exp\int p(t)\,dt = e^{-t}\cdot e^{2t} = e^{t}$, so $A(t) = e^{t} + c$. Then $y = (e^{t}+c)e^{-2t} = e^{-t} + ce^{-2t}$, matching part (a).
Concepts tested: Integrating-Factor, Variation Of Parameters, Linear ODE, General Solution.
