---
type: reference
parent: "[[AM20]]"
domain: math
course: "AM 20"
status: draft
source: "AM20 Lecture2 Notation"
tags:
  - decks
---
# AM 20 Cards - AM20 Lecture2 Notation Derivative notation and choosing the unknown

> [!important] Why this deck exists (2026-09-30, from lecture)
> The falling ball was rewritten from $m\frac{dv}{dt} = mg - \gamma v$ to $m\frac{d^2x}{dt^2} = mg - \gamma\frac{dx}{dt}$. Two things to own: what the notation means, and why swapping the unknown changes the order. Do these cards first today.

## Leibniz Notation for Higher Derivatives
| Front | Back | Notes |
| --- | --- | --- |
| In $\frac{dx}{dt}$, which variable is independent? | **$t$, on the bottom:** the one you differentiate with respect to. | lecture 9/30; notation |
| In $\frac{dx}{dt}$, which variable is dependent? | **$x$, on top:** the unknown function. | lecture 9/30; notation |
| In $\frac{d^2x}{dt^2}$, what does the 2 mean? | **Differentiate twice.** It is the derivative of $\frac{dx}{dt}$; nothing is squared. | lecture; definition |
| Write $\frac{d}{dt}\left(\frac{dx}{dt}\right)$ two shorter ways. | $\frac{d^2x}{dt^2}$ and $x''$. | lecture; notation |
| In $\frac{d^2x}{dt^2}$, why is the 2 on $d$ at the top but on $dt$ at the bottom? | **Top: the operation $d$ is applied twice to x. Bottom: you divide by $dt$ once per derivative.** It is bookkeeping, not algebra. | lecture; notation |
| $\frac{d^2x}{dt^2}$ vs $\left(\frac{dx}{dt}\right)^2$: which is the second derivative, and which is velocity squared? | $\frac{d^2x}{dt^2}$ is the second derivative. $\left(\frac{dx}{dt}\right)^2$ is velocity squared, and it would make an ODE nonlinear. | lecture; discrimination |
| In $\frac{d^3y}{dx^3}$, what is the unknown function? | $y$ | general; procedure |
| In $\frac{d^3y}{dx^3}$, what is the independent variable? | $x$ | general; procedure |
| In $\frac{d^3y}{dx^3}$, how many derivatives are taken? | Three: it's $y'''$. | general; procedure |
| In physics, what do $\dot x$ and $\ddot x$ mean? | $\dot x = \frac{dx}{dt}$ and $\ddot x = \frac{d^2x}{dt^2}$: each dot is one time derivative. | general; notation |

## Position, Velocity and Acceleration
| Front | Back | Notes |
| --- | --- | --- |
| If $x(t)$ is position, what are $\frac{dx}{dt}$ and $\frac{d^2x}{dt^2}$? | Velocity $v$, and acceleration $a$. | lecture; definition |
| Given $v = \frac{dx}{dt}$, write $\frac{dv}{dt}$ in terms of $x$. | $\frac{dv}{dt} = \frac{d^2x}{dt^2}$. | lecture; formula |

## Choosing the Unknown Changes the Order
| Front | Back | Notes |
| --- | --- | --- |
| Falling ball with drag: write Newton's law with position $x$ as the unknown. | $m\frac{d^2x}{dt^2} = mg - \gamma\frac{dx}{dt}$ | lecture; formula |
| Falling ball: the $v$ form $m\frac{dv}{dt} = mg - \gamma v$ is first order. What order is the $x$ form? | **Second order.** | lecture; key move |
| Falling ball: why does rewriting it in $x$ raise the order by one? | **The unknown moved one derivative down ($v = x'$), so every derivative gains one order.** | lecture; key move |
| Why rewrite the falling ball in terms of $x$ at all? | **To answer "where is it?"** (e.g. when it hits the ground), not just "how fast?". | lecture; key move |
| When can a second-order equation in $x$ be rewritten as a first-order equation in $v = x'$? | **When $x$ itself never appears, only $x'$ and $x''$.** Then substitute $v = x'$ and $v' = x''$. | general; procedure |
| Spring with damping, $mx'' = -kx - \gamma x'$: what blocks rewriting it as a first-order equation in $v = x'$ alone? | **The $-kx$ term:** it needs the position $x$ itself, which $v$ alone can't supply. | general; discrimination |
| Circuit: current is $I = \frac{dQ}{dt}$. What is $\frac{dI}{dt}$ in terms of the charge $Q$? | $\frac{d^2Q}{dt^2}$: the same pattern as $v = x'$ and $a = x''$. | general; transfer |
| General rule: if $u = \frac{dy}{dt}$ and $y$ itself is absent, how does the order of the $u$ form compare to the $y$ form? | **One lower**, because $u' = y''$, $u'' = y'''$, and so on. | general; abstraction |

## Falling Ball in Position Form
| Front | Back | Notes |
| --- | --- | --- |
| Classify $m\frac{d^2x}{dt^2} = mg - \gamma\frac{dx}{dt}$ under all four criteria. | Second order, linear, time-invariant, scalar ODE. | lecture; key move |

## Second Law of Motion
| Front | Back | Notes |
| --- | --- | --- |
| Newton's second law $F = ma$, written with position $x(t)$ as the unknown? | $F = m\frac{d^2x}{dt^2}$. | lecture; formula |

# Node map
```json
[
 {
  "name": "Leibniz Notation for Higher Derivatives",
  "type": "concept",
  "existing": false,
  "parent": "Classifying Differential Equations",
  "prereqs": [
   "Derivative"
  ],
  "uses": [],
  "page": 1,
  "summary": "$\\frac{d^nx}{dt^n}$ means differentiate $x$ with respect to $t$, $n$ times; the exponent-looking $n$ counts derivatives and squares nothing. Same as $x^{(n)}$; in physics $\\dot x$, $\\ddot x$."
 },
 {
  "name": "Position, Velocity and Acceleration",
  "type": "concept",
  "existing": false,
  "parent": "Classifying Differential Equations",
  "prereqs": [
   "Leibniz Notation for Higher Derivatives",
   "Velocity"
  ],
  "uses": [],
  "page": 1,
  "summary": "For position $x(t)$: velocity $v = \\frac{dx}{dt}$ and acceleration $a = \\frac{dv}{dt} = \\frac{d^2x}{dt^2}$, so Newton's law reads $F = m\\frac{d^2x}{dt^2}$."
 },
 {
  "name": "Choosing the Unknown Changes the Order",
  "type": "concept",
  "existing": false,
  "parent": "Classifying Differential Equations",
  "prereqs": [
   "Order of a Differential Equation",
   "Position, Velocity and Acceleration"
  ],
  "uses": [],
  "page": 1,
  "summary": "The same system can be written with different unknowns; writing it for $x$ instead of $v = x'$ raises the order by one. Going back down works only when $x$ itself does not appear."
 },
 {
  "name": "Falling Ball in Position Form",
  "type": "problem",
  "existing": false,
  "parent": "Classifying Differential Equations",
  "prereqs": [],
  "uses": [
   "Choosing the Unknown Changes the Order",
   "Order of a Differential Equation",
   "Linear ODE",
   "Time-Invariant vs Time-Varying",
   "Scalar vs System of Differential Equations"
  ],
  "page": 1,
  "summary": "Rewrites $m\\,v' = mg - \\gamma v$ as $m\\,x'' = mg - \\gamma x'$ and classifies it: second order, linear, time-invariant, scalar."
 },
 {
  "name": "Second Law of Motion",
  "type": "concept",
  "existing": true,
  "parent": "",
  "prereqs": [],
  "summary": ""
 }
]
```

# Frankenstein problems

**Frankenstein Problem 1.** A ball of mass $m = 2$ kg falls with drag $\gamma = 4$ kg/s and $g = 9.8$ m/s². (a) Write the equation with velocity as the unknown, then with position. (b) Classify both. (c) Find the terminal velocity.
Solution: (a) $2\frac{dv}{dt} = 19.6 - 4v$, and $2\frac{d^2x}{dt^2} = 19.6 - 4\frac{dx}{dt}$. (b) The $v$ form is first order; the $x$ form is second order. Both are linear, time-invariant, scalar ODEs. (c) Terminal velocity: set $\frac{dv}{dt} = 0$, so $4v = 19.6$ and $v = 4.9$ m/s.
Concepts: Choosing the Unknown Changes the Order; Order of a Differential Equation; Linear ODE; Position, Velocity and Acceleration.

**Frankenstein Problem 2.** A circuit obeys $L\frac{d^2Q}{dt^2} + R\frac{dQ}{dt} + \frac{Q}{C} = E(t)$. (a) What is the order? (b) Substitute $I = \frac{dQ}{dt}$: why can't you get a first-order equation in $I$ alone? (c) Is it linear? (d) Time-invariant when $E$ is constant; what about $E(t) = \sin t$?
Solution: (a) Second order. (b) The term $\frac{Q}{C}$ needs $Q$ itself, which $I$ alone doesn't give (same as the spring's $-kx$). (c) Linear: $Q$, $Q'$, $Q''$ each appear to the first power with constant coefficients. (d) With $E(t) = \sin t$, $t$ appears explicitly, so it is time-varying (and still linear).
Concepts: Leibniz Notation for Higher Derivatives; Choosing the Unknown Changes the Order; Linear ODE; Time-Invariant vs Time-Varying.
