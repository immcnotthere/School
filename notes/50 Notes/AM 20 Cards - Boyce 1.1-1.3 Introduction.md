---
type: reference
parent: "[[AM20]]"
domain: math
course: "AM 20"
status: draft
source: "Boyce 1.1-1.3 Introduction"
tags:
  - decks
---
# AM 20 Cards - Boyce 1.1-1.3 Introduction: Models, Direction Fields, Classification

## Mathematical Model
| Front | Back | Notes |
| --- | --- | --- |
| What is a mathematical model of a physical process? | A differential equation (or system) that describes the process, derived from physical laws or hypotheses (e.g. Newton's second law, proportional growth). | p.24; definition |
| Why must a mathematical model always be tested against reality? | Its predictions must be compared with observations; if they disagree badly, the model must be refined even though it may still be useful qualitatively. | p.37; definition |

## Direction Field
| Front | Back | Notes |
| --- | --- | --- |
| How do you construct a direction field without solving the ODE? | Evaluate $f(t,y)$ at each point of a rectangular grid and draw a short segment of that slope at each point; no integration is needed. | p.27; procedure |
| What can a direction field reveal about solutions that you cannot get without solving the equation? | The qualitative long-term behavior (increasing, decreasing, converging, diverging) of every solution, without finding an explicit formula. | p.25; definition |

## General Solution
| Front | Back | Notes |
| --- | --- | --- |
| What is the general solution of $dy/dt = ay - b$ for $a \neq 0$? | $y = \dfrac{b}{a} + ce^{at}$, where $c$ is an arbitrary constant. | p.35; formula |
| What role does the arbitrary constant $c$ play in a general solution? | Each value of $c$ selects one member of the infinite family of solutions; $c=0$ gives the equilibrium solution. | p.35; definition |

## Integral Curve
| Front | Back | Notes |
| --- | --- | --- |
| What is an integral curve of a differential equation? | The graph of one particular solution (one value of the arbitrary constant) in the $ty$-plane. | p.35; definition |
| How do you find the integral curve through a given initial point from the general solution? | Substitute the initial point into the general solution and solve for $c$; that value of $c$ picks out the curve through the point. | p.35; procedure |

## Initial Value Problem
| Front | Back | Notes |
| --- | --- | --- |
| What is an initial value problem (IVP)? | A differential equation paired with an initial condition $y(t_0) = y_0$ that singles out one particular solution. | p.34; definition |
| For $dy/dt = ay - b$ with $y(0) = y_0$, what is $c$ in the general solution $y = b/a + ce^{at}$? | $c = y_0 - b/a$ | p.35; formula |

## Order of a Differential Equation
| Front | Back | Notes |
| --- | --- | --- |
| What is the order of a differential equation? | The order of the highest derivative that appears in the equation. | p.42; definition |
| What order is $y''' + 2e^{t}y'' + yy' = t^4$? | Third order, since $y'''$ is the highest derivative present. | p.42; formula |

## System of Differential Equations
| Front | Back | Notes |
| --- | --- | --- |
| When is a system of differential equations needed instead of one equation? | When two or more unknown functions must be determined simultaneously. | p.41-42; definition |
| Write the Lotka-Volterra (predator-prey) system and identify $x$ and $y$. | $dx/dt = ax - \alpha xy$, $dy/dt = -cy + \gamma xy$, where $x(t)$ is the prey population and $y(t)$ is the predator population. | p.42; formula |

## Linear ODE
| Front | Back | Notes |
| --- | --- | --- |
| What is the general form of a linear ODE of order $n$? | $a_0(t)y^{(n)} + a_1(t)y^{(n-1)} + \cdots + a_n(t)y = g(t)$ | p.42-43; formula |
| How do you test whether $F(t,y,y',\ldots,y^{(n)})=0$ is linear? | $F$ must be a linear function of $y, y', \ldots, y^{(n)}$: no products, powers, or nonlinear functions of $y$ or its derivatives. | p.42-43; procedure |

## Existence and Uniqueness
| Front | Back | Notes |
| --- | --- | --- |
| What does the existence question ask about a differential equation? | Whether a function $y=\varphi(t)$ that actually satisfies the equation exists at all; writing down an equation does not guarantee a solution does. | p.44; definition |
| What does the uniqueness question ask, once a solution is known to exist? | Whether that solution is the only one satisfying the given initial condition, or whether other solutions also pass through the same point. | p.45; definition |

## Falling Object Model
| Front | Back | Notes |
| --- | --- | --- |
| A falling object of mass $m$ has drag proportional to velocity with coefficient $\gamma$. What is the equation of motion and its equilibrium (terminal) velocity? | $m\,dv/dt = mg - \gamma v$; equilibrium (terminal) velocity is $v = mg/\gamma$. | p.24-25; key move |

## Field Mice and Owls
| Front | Back | Notes |
| --- | --- | --- |
| A mouse population grows at rate $r$ and is preyed on at constant rate $k$: $dp/dt = rp - k$. What is the general solution? | $p(t) = \dfrac{k}{r} + \left(p_0 - \dfrac{k}{r}\right)e^{rt}$ | p.32-33; key move |

## Asymptotic Stability
| Front | Back | Notes |
| --- | --- | --- |
| What distinguishes an attracting equilibrium solution from a repelling one? | Attracting: nearby solutions converge to it as $t$ increases (e.g. the falling object's $v=49$). Repelling: nearby solutions diverge from it (e.g. the mouse population's $p=900$). | p.28-29; discrimination |

## Partial Differential Equation (PDE)
| Front | Back | Notes |
| --- | --- | --- |
| Give one PDE example from Boyce 1.3 and name it. | Heat conduction equation $\alpha^2 u_{xx} = u_t$; also the wave equation $a^2 u_{xx} = u_{tt}$. | p.41; definition |

# Node map
```json
[
 {
  "name": "Mathematical Model",
  "type": "concept",
  "existing": true,
  "parent": "Differential Equation",
  "prereqs": [],
  "uses": [],
  "page": 24,
  "summary": "A differential equation that describes a physical process; must be validated against observation."
 },
 {
  "name": "Direction Field",
  "type": "concept",
  "existing": true,
  "parent": "Differential Equation",
  "prereqs": [],
  "uses": [],
  "page": 25,
  "summary": "A grid of tangent-slope segments for $dy/dt=f(t,y)$ that reveals qualitative solution behavior without solving."
 },
 {
  "name": "Equilibrium Solution",
  "type": "concept",
  "existing": true,
  "parent": "Differential Equation",
  "prereqs": [
   "Direction Field"
  ],
  "uses": [],
  "page": 25,
  "summary": "A constant solution $y_e$ where $f(t,y_e)=0$; can be attracting or repelling."
 },
 {
  "name": "General Solution",
  "type": "concept",
  "existing": true,
  "parent": "Differential Equation",
  "prereqs": [],
  "uses": [],
  "page": 35,
  "summary": "The full family of solutions of a differential equation, parameterized by an arbitrary constant $c$."
 },
 {
  "name": "Integral Curve",
  "type": "concept",
  "existing": true,
  "parent": "Differential Equation",
  "prereqs": [
   "General Solution"
  ],
  "uses": [],
  "page": 35,
  "summary": "The graph of one particular solution corresponding to one value of $c$."
 },
 {
  "name": "Initial Value Problem",
  "type": "concept",
  "existing": true,
  "parent": "Differential Equation",
  "prereqs": [
   "General Solution"
  ],
  "uses": [],
  "page": 34,
  "summary": "A differential equation plus an initial condition $y(t_0)=y_0$ that fixes one solution."
 },
 {
  "name": "Order of a Differential Equation",
  "type": "concept",
  "existing": true,
  "parent": "Differential Equation",
  "prereqs": [],
  "uses": [],
  "page": 42,
  "summary": "The order of the highest derivative appearing in the equation."
 },
 {
  "name": "Ordinary (Math)",
  "type": "concept",
  "existing": true,
  "parent": "Differential Equation",
  "prereqs": [],
  "uses": [],
  "page": 41,
  "summary": "Distinguishes ODEs (single independent variable) from PDEs (several independent variables)."
 },
 {
  "name": "System of Differential Equations",
  "type": "concept",
  "existing": false,
  "parent": "Differential Equation",
  "prereqs": [],
  "uses": [],
  "page": 41,
  "summary": "Two or more coupled differential equations for two or more unknown functions, e.g. the Lotka-Volterra predator-prey system."
 },
 {
  "name": "Linear ODE",
  "type": "concept",
  "existing": true,
  "parent": "Differential Equation",
  "prereqs": [
   "Order of a Differential Equation"
  ],
  "uses": [],
  "page": 42,
  "summary": "An ODE $a_0(t)y^{(n)}+\\cdots+a_n(t)y=g(t)$ where $F$ is linear in $y$ and its derivatives."
 },
 {
  "name": "Linearization",
  "type": "concept",
  "existing": true,
  "parent": "Differential Equation",
  "prereqs": [
   "Linear ODE"
  ],
  "uses": [],
  "page": 43,
  "summary": "Approximating a nonlinear equation by a linear one over a restricted range, e.g. $\\sin\\theta \\approx \\theta$."
 },
 {
  "name": "Existence and Uniqueness",
  "type": "concept",
  "existing": true,
  "parent": "Differential Equation",
  "prereqs": [
   "Initial Value Problem"
  ],
  "uses": [],
  "page": 44,
  "summary": "Whether a solution to a given equation/IVP exists, and if so whether it is the only one."
 },
 {
  "name": "Falling Object Model",
  "type": "problem",
  "existing": false,
  "parent": "Differential Equation",
  "prereqs": [
   "Mathematical Model"
  ],
  "uses": [
   "Mathematical Model",
   "Direction Field",
   "Equilibrium Solution"
  ],
  "page": 24,
  "summary": "Newton's second law with linear drag gives $m\\,dv/dt=mg-\\gamma v$, equilibrium $v=mg/\\gamma$."
 },
 {
  "name": "Field Mice and Owls",
  "type": "problem",
  "existing": false,
  "parent": "Differential Equation",
  "prereqs": [
   "Mathematical Model"
  ],
  "uses": [
   "Mathematical Model",
   "Equilibrium Solution",
   "General Solution",
   "Initial Value Problem"
  ],
  "page": 32,
  "summary": "Population growth minus constant predation, $dp/dt=rp-k$, solved by direct integration."
 },
 {
  "name": "Asymptotic Stability",
  "type": "concept",
  "existing": true,
  "parent": "",
  "prereqs": [],
  "summary": ""
 },
 {
  "name": "Partial Differential Equation (PDE)",
  "type": "concept",
  "existing": true,
  "parent": "",
  "prereqs": [],
  "summary": ""
 }
]
```

# Frankenstein problems

**FP1: Repelling population with a linear IVP**
A population satisfies $dp/dt = 0.2p - 40$.
(a) Find the equilibrium solution and classify it as attracting or repelling.
(b) Find the general solution.
(c) Solve the initial value problem $p(0) = 150$.
(d) State the order of the equation and whether it is linear.

**Solution.** (a) Set $0.2p - 40 = 0 \Rightarrow p = 200$. Since the coefficient of $p$ is $+0.2 > 0$ (same sign pattern as the field-mice equation $dp/dt = rp-k$), nearby solutions diverge from $p=200$: it is repelling.
(b) This has the form $dy/dt = ay - b$ with $a=0.2$, $b=40$, so $p(t) = \dfrac{40}{0.2} + ce^{0.2t} = 200 + ce^{0.2t}$.
(c) $p(0)=150 \Rightarrow 150 = 200 + c \Rightarrow c = -50$. So $p(t) = 200 - 50e^{0.2t}$.
(d) First order; linear (it has the form $dp/dt - 0.2p = -40$, linear in $p$).
Concepts tested: Equilibrium Solution, General Solution, Initial Value Problem, Order of a Differential Equation, Linear ODE.

**FP2: Pendulum classification and linearization**
A pendulum of length $L = 2$ m satisfies $\theta'' + (g/L)\sin\theta = 0$ with $g = 9.8\text{ m/s}^2$.
(a) State the order of this equation and whether it is linear or nonlinear; justify using the definition of a linear ODE.
(b) Write the linearized version valid for small $\theta$ and compute its coefficient.
(c) For the linearized equation with $\theta(0)=\theta_0$ and $\theta'(0)=0$ specified, what two questions about the resulting solution would a mathematician ask before trying to solve it?

**Solution.** (a) Second order (highest derivative is $\theta''$). Nonlinear, because $\sin\theta$ is a nonlinear function of $\theta$, so $F$ is not linear in $\theta$.
(b) Using $\sin\theta \approx \theta$: $\theta'' + (g/L)\theta = 0$. Coefficient: $g/L = 9.8/2 = 4.9$, so $\theta'' + 4.9\theta = 0$.
(c) Existence: does a solution $\theta(t)$ satisfying both the equation and both initial conditions actually exist? Uniqueness: if one exists, is it the only solution satisfying those same initial conditions?
Concepts tested: Order of a Differential Equation, Linear ODE, Linearization, Existence and Uniqueness.
