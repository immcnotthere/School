---
type: reference
parent: "[[AM20]]"
domain: math
course: "AM 20"
status: draft
source: "AM20 Lecture2"
tags:
  - decks
---
# AM 20 Cards - AM20 Lecture2 Classifying ODEs

## ODE
| Front | Back | Notes |
| --- | --- | --- |
| What is an ordinary differential equation (ODE)? | A differential equation in which the unknown function depends on a single independent variable. | p.1; definition |
| In an ODE, how are derivatives written? | As ordinary derivatives, using $d/dt$ notation or a prime, e.g. $y'$. | p.1; definition |
| In $F=ma=m\frac{dv}{dt}$, why is this an ODE? | Because only one independent variable, $t$, appears. | p.1; discrimination |

## Partial Differential Equation (PDE)
| Front | Back | Notes |
| --- | --- | --- |
| What is a partial differential equation (PDE)? | A differential equation in which the unknown function depends on two or more independent variables. | p.2; definition |
| In a PDE, how are derivatives written? | As partial derivatives, using $\partial/\partial t$ notation. | p.2; definition |
| ODE vs PDE: what single feature distinguishes them? | The number of independent variables the unknown function depends on: one for an ODE, two or more for a PDE. | p.1-2; discrimination |
| In $\frac{\partial T}{\partial t}=\kappa\frac{\partial^2 T}{\partial x^2}$, why is this a PDE? | Because $T$ depends on two independent variables, $x$ and $t$. | p.2; discrimination |

## Order of a Differential Equation
| Front | Back | Notes |
| --- | --- | --- |
| In $(y'')^3 + y' - y = 0$, why is the order 2 and not 3? | The order is set by the highest derivative present, $y''$, not by the power it is raised to. | p.3; discrimination |
| What is the order of $y'''' + 2e^t y'' + yy' = t$? | Fourth order, since the highest derivative is $y''''$. | p.3; procedure |

## Time-Invariant vs Time-Varying
| Front | Back | Notes |
| --- | --- | --- |
| When is a differential equation called time-invariant? | When the independent variable $t$ does not appear explicitly in the equation. | p.3; definition |
| When is a differential equation called time-varying? | When the independent variable $t$ appears explicitly in the equation. | p.3; definition |
| Is $y''' + yy' + 4y = 0$ time-invariant or time-varying? | Time-invariant, since $t$ does not appear explicitly. | p.3; discrimination |

## Linear ODE
| Front | Back | Notes |
| --- | --- | --- |
| What makes an ODE linear? | Each of $y, y', y'', \dots, y^{(n)}$ appears to the first power, multiplied only by functions of $t$, with no products or compositions among them. | p.4; definition |
| Which is disallowed in a linear ODE: a coefficient like $\sin t$, or a coefficient like $\cos y$? | A coefficient like $\cos y$ is disallowed since it involves the dependent variable; $\sin t$ is fine since it involves only the independent variable. | p.4; discrimination |
| Why is $y''' + \sin(t)y'' + y = t$ linear even though it contains $\sin(t)$? | Because $\sin t$ is a coefficient involving only the independent variable $t$, not the dependent variable $y$. | p.4; discrimination |

## Nonlinear ODE
| Front | Back | Notes |
| --- | --- | --- |
| In a system with unknowns $x(t)$ and $y(t)$, what counts as a y-thing in the y-count test? | **Every unknown and its derivatives:** $x$, $x'$, $y$, $y'$. | lecture 9/30; procedure |
| Why is the term $xy$ nonlinear? | It multiplies two unknowns: 2 y-things in one term. | lecture 9/30; procedure |
| Doubling test: replace $y$ with $2y$. What happens to a linear term like $2e^t y''$? | It exactly doubles. | lecture 9/30; procedure |
| Doubling test: replace $y$ with $2y$. What happens to $yy'$? | It quadruples: $(2y)(2y') = 4yy'$, so it's nonlinear. | lecture 9/30; procedure |
| $2e^t y''$ vs $y\,y'$: both scale a derivative. Why is one linear and the other not? | **$2e^t$ depends only on $t$: a known dial that changes over time.** In $y\,y'$ the dial is $y$ itself, the unknown, so the unknown multiplies the unknown. | lecture 9/30; discrimination |
| What are the only two things a linear ODE may do to $y$, $y'$, $y''$, ...? | **Multiply each by a coefficient (a number or a function of $t$), then add them up.** Any other operation on a y-thing (a power, a product, $\sin$, $e$) makes it nonlinear. | lecture 9/30; definition |
| Why does a power like $(y'')^3$ make an ODE nonlinear? | **A power is repeated multiplication: $y'' \cdot y'' \cdot y''$ has 3 y-things in one term.** Cubing is also a function applied to $y''$, like $\sin$. | lecture 9/30; key move |
| $(y'')^3 + y' - y = 0$: what order is it? | **2**: the highest derivative is $y''$; the cube doesn't change the order. | lecture 9/30; discrimination |
| $(y'')^3 + y' - y = 0$: which term makes it nonlinear? | $(y'')^3$: 3 y-things multiplied in one term. | lecture 9/30; discrimination |
| y-count test: what do you count in each term? | **The y-things:** $y$, $y'$, $y''$, ... | lecture 9/30; procedure |
| y-count test: what count per term means linear? | **Exactly 1** (or 0 for pure-$t$ terms). A 2 or more, or a $y$ inside a function, means nonlinear. | lecture 9/30; procedure |
| Why is $y''' + yy' + 4y = 0$ nonlinear? | **The term $yy'$ has two y-factors, $y$ times $y'$.** $y'''$ and $4y$ have one each; that single product breaks linearity. | lecture 9/30; key move |
| Linear vs nonlinear: which variable decides it, the dependent ($y$) or the independent ($t$)? | **Only the dependent one: $y$ and its derivatives.** $t$ can appear any way it likes ($t^2$, $\sin t$, $e^t$) and the equation stays linear, which keeps it solvable by standard methods. | lecture 9/30; Jacob's rule |
| $y' + t^2 y = e^t$ vs $y' + y^2 = t$: which term makes one of them nonlinear? | $y^2$, in the second one. $t^2$ and $e^t$ only involve $t$. | lecture 9/30; discrimination |
| What makes an ODE nonlinear? | It is any ODE that is not linear: the dependent variable or its derivatives appear as powers, products with each other, or inside another function. | p.4; definition |
| Why is $y''' + \cos(y)y'' + y = t$ nonlinear? | The coefficient $\cos(y)$ involves the dependent variable $y$, so the term $\cos(y)y''$ is not linear in $y$. | p.4; discrimination |
| Why is $y''' + e^y y'' + \sin(y') = t$ nonlinear? | Both $e^y y''$ and $\sin(y')$ place the dependent variable or its derivative inside another function. | p.4; discrimination |
| Lotka-Volterra: which terms are the linear part? | $ax$ and $-cy$: one unknown each. | lecture 9/30; procedure |
| Lotka-Volterra: which terms are the nonlinear part? | $-bxy$ and $dxy$: two unknowns multiplied (the predator-prey interaction). | lecture 9/30; procedure |

## Scalar vs System of Differential Equations
| Front | Back | Notes |
| --- | --- | --- |
| What is a scalar differential equation? | A differential equation with a single unknown function. | p.2; definition |
| What is a system of differential equations? | Two or more equations that together determine two or more unknown functions. | p.2-3; definition |
| In the Lotka-Volterra predator-prey equations, why is the system nonlinear? | Each equation contains a product of the two unknown functions, $xy$, and a linear equation only allows an unknown multiplied by a function of the independent variable alone. | p.3,6; discrimination |

## Linearization
| Front | Back | Notes |
| --- | --- | --- |
| What is linearization of a nonlinear ODE? | Replacing the nonlinear equation with a linear one that agrees with it over a restricted range. | p.4; definition |
| What small-angle approximation linearizes the pendulum equation $\frac{d^2\theta}{dt^2} + \frac{g}{L}\sin\theta = 0$? | $\sin\theta \approx \theta$ for $\vert \theta\vert  \ll 1$, giving $\frac{d^2\theta}{dt^2} + \frac{g}{L}\theta = 0$. | p.4-5; procedure |
| At $\theta = 0.5$ radians, how large is the error in the small-angle approximation $\sin\theta \approx \theta$? | About 0.0206, roughly 4.1 percent of 0.5, since $\sin(0.5) = 0.4794$. | p.5; concept |

## Deriving the Circuit Differential Equation
| Front | Back | Notes |
| --- | --- | --- |
| Key move to derive the circuit equation for charge $Q$ from $E(t)=L\frac{dI}{dt}+RI+\frac{Q}{C}$? | Substitute $I=\frac{dQ}{dt}$ (so $\frac{dI}{dt}=\frac{d^2Q}{dt^2}$) to eliminate $I$, giving $E(t) = LQ'' + RQ' + \frac{1}{C}Q$. | p.1-2; procedure |

## Verifying the Wave Equation Solution
| Front | Back | Notes |
| --- | --- | --- |
| Key move to verify $u(x,t)=f(x-at)$ solves $\frac{\partial u}{\partial t}+a\frac{\partial u}{\partial x}=0$? | Apply the chain rule to get $\frac{\partial u}{\partial t}=-af'(x-at)$ and $\frac{\partial u}{\partial x}=f'(x-at)$, then show they combine to $-af'(x-at)+af'(x-at)=0$. | p.2; procedure |

## Determining Order and Time-Variance
| Front | Back | Notes |
| --- | --- | --- |
| Key move to classify $(y')^2 + ty' + 4y = 0$ by order and time-variance? | The highest derivative is $y'$, so it is first order; $t$ appears explicitly, so it is time-varying. | p.3; procedure |

## Classifying Equations as Linear or Nonlinear
| Front | Back | Notes |
| --- | --- | --- |
| Key move to tell $y'''+\sin(t)y''+y=t$ (linear) apart from $y'''+\cos(y)y''+y=t$ (nonlinear)? | Check whether the coefficient of a derivative involves the dependent variable: $\sin t$ depends only on $t$ (linear), but $\cos y$ depends on $y$ itself (nonlinear). | p.4; procedure |

## Classifying Equations 1 Through 5 Under All Four Criteria
| Front | Back | Notes |
| --- | --- | --- |
| Key move to classify Eq. (1), (4), (5), (6), (7) under all four criteria at once? | Check independent variables (ODE or PDE), number of unknowns (scalar or system), highest derivative (order), and whether the dependent variable appears linearly; e.g. Eq. (7) is ODE, system, nonlinear, first order. | p.5-6; procedure |

## Classifying an Equation Under All Four Criteria
| Front | Back | Notes |
| --- | --- | --- |
| Key move to classify $y''+3ty'+(\cos t)y=e^t$ under all four criteria? | One variable $t$ gives ODE, one unknown $y$ gives scalar, highest derivative $y''$ gives second order, and coefficients $\cos t, 3t, 1$ depend only on $t$ so it is linear; since $t$ appears explicitly it is time-varying. | p.6; procedure |

## System of Differential Equations
| Front | Back | Notes |
| --- | --- | --- |
| Lotka-Volterra $x' = ax - bxy$: what does $ax$ mean? | Prey grow on their own. | lecture 9/30; key move |
| Lotka-Volterra $x' = ax - bxy$: what does $-bxy$ mean? | Prey get eaten: more encounters ($xy$), more eaten. | lecture 9/30; key move |
| Lotka-Volterra $y' = -cy + dxy$: what does $-cy$ mean? | Predators die off without food. | lecture 9/30; key move |
| Lotka-Volterra $y' = -cy + dxy$: what does $dxy$ mean? | Predators grow by eating prey. | lecture 9/30; key move |

# Node map
```json
[
 {
  "name": "ODE",
  "type": "concept",
  "existing": true,
  "parent": "Classifying Differential Equations",
  "prereqs": [],
  "uses": [],
  "page": 1,
  "summary": "A differential equation whose unknown function depends on a single independent variable; derivatives are written $d/dt$ or with a prime."
 },
 {
  "name": "Partial Differential Equation (PDE)",
  "type": "concept",
  "existing": false,
  "parent": "Classifying Differential Equations",
  "prereqs": [
   "ODE"
  ],
  "uses": [],
  "page": 2,
  "summary": "A differential equation whose unknown function depends on two or more independent variables; derivatives are written $\\partial/\\partial t$."
 },
 {
  "name": "Order of a Differential Equation",
  "type": "concept",
  "existing": false,
  "parent": "Classifying Differential Equations",
  "prereqs": [
   "ODE"
  ],
  "uses": [],
  "page": 3,
  "summary": "The order of a differential equation is the order of its highest derivative; the power that derivative is raised to does not affect the order."
 },
 {
  "name": "Time-Invariant vs Time-Varying",
  "type": "concept",
  "existing": false,
  "parent": "Classifying Differential Equations",
  "prereqs": [
   "Order of a Differential Equation"
  ],
  "uses": [],
  "page": 3,
  "summary": "An equation is time-invariant if the independent variable $t$ does not appear explicitly, and time-varying if it does."
 },
 {
  "name": "Linear ODE",
  "type": "concept",
  "existing": true,
  "parent": "Classifying Differential Equations",
  "prereqs": [
   "ODE"
  ],
  "uses": [],
  "page": 4,
  "summary": "An ODE is linear if the dependent variable and its derivatives each appear to the first power, multiplied only by functions of the independent variable."
 },
 {
  "name": "Nonlinear ODE",
  "type": "concept",
  "existing": true,
  "parent": "Classifying Differential Equations",
  "prereqs": [
   "Linear ODE"
  ],
  "uses": [],
  "page": 4,
  "summary": "An ODE that is not linear: the dependent variable or its derivatives appear as powers, products, or inside another function."
 },
 {
  "name": "Scalar vs System of Differential Equations",
  "type": "concept",
  "existing": false,
  "parent": "Classifying Differential Equations",
  "prereqs": [
   "ODE"
  ],
  "uses": [],
  "page": 2,
  "summary": "A scalar equation has one unknown function; a system has two or more unknown functions tied together by two or more equations."
 },
 {
  "name": "Linearization",
  "type": "concept",
  "existing": false,
  "parent": "Linearization",
  "prereqs": [
   "Nonlinear ODE"
  ],
  "uses": [],
  "page": 4,
  "summary": "Replacing a nonlinear differential equation with a linear one that agrees with it over a restricted range, e.g. via a Taylor approximation."
 },
 {
  "name": "Deriving the Circuit Differential Equation",
  "type": "problem",
  "existing": false,
  "parent": "Classifying Differential Equations",
  "prereqs": [],
  "uses": [
   "ODE",
   "Linear ODE"
  ],
  "page": 1,
  "summary": "Combine Kirchhoff's voltage law with $I=dQ/dt$ to derive $LQ''+RQ'+\\frac{1}{C}Q=E(t)$, a linear second-order ODE for charge $Q$."
 },
 {
  "name": "Verifying the Wave Equation Solution",
  "type": "problem",
  "existing": false,
  "parent": "Classifying Differential Equations",
  "prereqs": [],
  "uses": [
   "Partial Differential Equation (PDE)"
  ],
  "page": 2,
  "summary": "Show $u(x,t)=f(x-at)$ solves $u_t+au_x=0$ using the chain rule."
 },
 {
  "name": "Determining Order and Time-Variance",
  "type": "problem",
  "existing": false,
  "parent": "Classifying Differential Equations",
  "prereqs": [],
  "uses": [
   "Order of a Differential Equation",
   "Time-Invariant vs Time-Varying"
  ],
  "page": 3,
  "summary": "Classify five sample equations by order and by whether $t$ appears explicitly."
 },
 {
  "name": "Classifying Equations as Linear or Nonlinear",
  "type": "problem",
  "existing": false,
  "parent": "Classifying Differential Equations",
  "prereqs": [],
  "uses": [
   "Linear ODE",
   "Nonlinear ODE"
  ],
  "page": 4,
  "summary": "Classify four equations as linear or nonlinear by checking whether coefficients depend on the dependent variable."
 },
 {
  "name": "Linearizing the Pendulum Equation",
  "type": "problem",
  "existing": false,
  "parent": "Linearization",
  "prereqs": [],
  "uses": [
   "Linearization"
  ],
  "page": 4,
  "summary": "Replace $\\sin\\theta$ with $\\theta$ in the pendulum equation to obtain a linear, constant-coefficient, second-order ODE valid for small oscillations."
 },
 {
  "name": "Classifying Equations 1 Through 5 Under All Four Criteria",
  "type": "problem",
  "existing": false,
  "parent": "Classifying Differential Equations",
  "prereqs": [],
  "uses": [
   "ODE",
   "Partial Differential Equation (PDE)",
   "Scalar vs System of Differential Equations",
   "Linear ODE",
   "Nonlinear ODE",
   "Order of a Differential Equation"
  ],
  "page": 5,
  "summary": "Apply all four classification schemes at once to the five earlier example equations, e.g. the predator-prey system is an ODE, a system, nonlinear, and first order."
 },
 {
  "name": "Showing the Predator-Prey System Is Nonlinear",
  "type": "problem",
  "existing": false,
  "parent": "Classifying Differential Equations",
  "prereqs": [],
  "uses": [
   "Nonlinear ODE",
   "Scalar vs System of Differential Equations"
  ],
  "page": 6,
  "summary": "Point to the product-of-unknowns terms in the Lotka-Volterra system to show it is nonlinear."
 },
 {
  "name": "Classifying an Equation Under All Four Criteria",
  "type": "problem",
  "existing": false,
  "parent": "Classifying Differential Equations",
  "prereqs": [],
  "uses": [
   "ODE",
   "Order of a Differential Equation",
   "Linear ODE",
   "Time-Invariant vs Time-Varying"
  ],
  "page": 6,
  "summary": "Classify $y''+3ty'+(\\cos t)y=e^t$ as ODE, scalar, second order, linear, and time-varying."
 },
 {
  "name": "System of Differential Equations",
  "type": "concept",
  "existing": true,
  "parent": "",
  "prereqs": [],
  "summary": ""
 }
]
```

# Frankenstein problems

**Problem 1.** Consider the coupled system
$$\frac{dx}{dt} = -2x + 3xy, \qquad \frac{dy}{dt} = 4y - xy.$$
(a) Is this a single differential equation or a system? Is it scalar, or does it involve several unknown functions?
(b) What is the order of the system?
(c) Is the system linear or nonlinear? Justify using the definition of a linear ODE.
(d) Is it time-invariant or time-varying?

*Concepts tested: Scalar vs System of Differential Equations, Order of a Differential Equation, Linear ODE, Nonlinear ODE, Time-Invariant vs Time-Varying, ODE.*

Solution.
(a) There are two unknown functions, $x(t)$ and $y(t)$, each satisfying its own differential equation, so together they form a system (not a single scalar equation).
(b) Each equation contains only a first derivative ($dx/dt$, $dy/dt$), so the system is first order.
(c) Nonlinear. The terms $3xy$ and $-xy$ are products of the two unknown functions; a linear equation requires each unknown to appear to the first power multiplied only by a function of the independent variable $t$, and $xy$ is not of that form.
(d) Time-invariant, since the independent variable $t$ does not appear explicitly in either equation (it enters only through $x(t)$ and $y(t)$).

**Problem 2.** A signal $u(x,t)$ satisfies $\frac{\partial u}{\partial t} + u\frac{\partial u}{\partial x} = 0$.
(a) Explain why this is a PDE rather than an ODE.
(b) What is its order?
(c) Explain why the equation is nonlinear.
(d) If $u$ stays close to a constant background value $u_0$, replace the coefficient $u$ multiplying $\partial u/\partial x$ by $u_0$ to linearize the equation. State the order and linearity of the result.

*Concepts tested: Partial Differential Equation (PDE), Order of a Differential Equation, Nonlinear ODE, Linearization.*

Solution.
(a) Two independent variables, $x$ and $t$, appear, so the unknown $u$ depends on more than one independent variable; that makes it a PDE rather than an ODE.
(b) The highest derivative present is a first partial derivative ($\partial u/\partial t$ or $\partial u/\partial x$), so the equation is first order.
(c) The term $u\,\partial u/\partial x$ is the unknown function $u$ multiplied by its own derivative, which is a product of the dependent variable with itself rather than with a function of the independent variable alone, so the equation is nonlinear.
(d) Replacing the coefficient $u$ by the constant $u_0$ gives $\frac{\partial u}{\partial t} + u_0\frac{\partial u}{\partial x} = 0$. This linearized equation is still first order, and it is now linear, since $u_0$ is a fixed constant (not the unknown itself) multiplying $\partial u/\partial x$, and every remaining term is to the first power in $u$ or its derivatives.
