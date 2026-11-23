---
type: reference
parent: "[[AM20]]"
domain: math
course: "AM 20"
status: draft
source: "AM20 Lecture1"
tags:
  - decks
---
# AM 20 Cards - AM20 Lecture1 First-Order ODEs

## Differential Equation
| Front | Back | Notes |
| --- | --- | --- |
| What is a differential equation? | An equation containing one or more derivatives of an unknown function. | p.1; definition |

## Independent vs Dependent Variable
| Front | Back | Notes |
| --- | --- | --- |
| What is the independent variable in a differential equation? | The variable whose values are chosen freely and do not depend on anything else, often $t$ or $x$. | p.2; definition |
| What is the dependent variable in a differential equation? | The variable whose value is determined by the independent variable, e.g. through $v = v(t)$. | p.2; definition |
| In $\frac{dv}{dt} = -\frac{1}{5}(v-49)$, which variable is independent and which is dependent? | $t$ is independent; $v$ is dependent. | p.2; discrimination |

## Direction Field
| Front | Back | Notes |
| --- | --- | --- |
| What can a direction field never give you directly? | A formula for the solution; it only shows the shape or behavior of solutions. | p.2; discrimination |
| Why is the slope in the falling-object direction field the same at every time $t$ for a fixed $v$? | Because the right-hand side $-\frac{1}{5}(v-49)$ depends only on $v$, not on $t$. | p.2-3; concept |
| How do you find where a direction field's slope is zero? | Set the right-hand side of the differential equation equal to 0 and solve for the dependent variable. | p.3; procedure |

## Equilibrium Solution
| Front | Back | Notes |
| --- | --- | --- |
| How do you find the equilibrium solution(s) of $\frac{dv}{dt} = -\frac{1}{5}(v-49)$? | Set the right-hand side to 0 and solve: $-\frac{1}{5}(v-49)=0 \Rightarrow v=49$. | p.3; procedure |

## Separation of Variables
| Front | Back | Notes |
| --- | --- | --- |
| What is the first step of separation of variables on $\frac{dv}{dt} = -\frac{1}{5}(v-49)$? | Divide both sides by $(v-49)$ to put all $v$ terms on one side and all $t$ terms on the other: $\frac{dv/dt}{v-49} = -\frac{1}{5}$. | p.4; procedure |
| After separating variables, what is the next step? | Integrate both sides with respect to $t$ (substitute $u=v-49$ on the left) to get $\ln\lvert v-49 \rvert = -\frac{t}{5} + c$. | p.4; procedure |
| How do you undo the logarithm after integrating a separated equation? | Exponentiate both sides: $\lvert v-49 \rvert = e^{-t/5+c} = e^c e^{-t/5}$. | p.4; procedure |
| Why can $\lvert v-49 \rvert = e^c e^{-t/5}$ be rewritten as $v-49 = Ce^{-t/5}$ for an arbitrary nonzero constant $C$? | Removing the absolute value introduces a $\pm$ sign, and $e^c$ is an arbitrary positive number, so together they form one arbitrary nonzero constant $C = \pm e^c$. | p.4; concept |

## Initial Value Problem
| Front | Back | Notes |
| --- | --- | --- |
| What is an initial condition? | A condition that fixes the value of the unknown function at one value of the independent variable, e.g. $v(0)=0$. | p.4; definition |
| What is an initial value problem (IVP)? | A differential equation together with an initial condition. | p.4; definition |
| How do you find the constant $C$ in a solution family using an initial condition? | Substitute the given point (e.g. $t=0$) and the known value into the general solution, then solve for $C$. | p.4; procedure |

## General Solution
| Front | Back | Notes |
| --- | --- | --- |
| What is a general solution of a differential equation? | A family of solutions containing an arbitrary constant $C$ that covers every solution of the equation, e.g. $v(t) = 49 + Ce^{-t/5}$. | p.4; definition |
| How do you turn a general solution into a particular solution? | Apply the initial condition and solve for the constant $C$. | p.4; procedure |

## Verifying a Solution by Substitution
| Front | Back | Notes |
| --- | --- | --- |
| Key move to verify that $y(t)=3e^{2t}$ solves $y' = 2y$? | Differentiate to get $y' = 6e^{2t}$, compute $2y = 6e^{2t}$, and confirm the two expressions agree for every $t$. | p.1; procedure |

## Deriving the Falling Object Equation
| Front | Back | Notes |
| --- | --- | --- |
| Key move in deriving $m\frac{dv}{dt} = mg - \gamma v$ for a falling object with drag? | Set Newton's second law $F = ma = m\frac{dv}{dt}$ equal to the total force $F = mg - \gamma v$ (gravity minus a drag force proportional to velocity). | p.1-2; procedure |

## Direction Field and Terminal Velocity for the Falling Object
| Front | Back | Notes |
| --- | --- | --- |
| Key move to read the terminal velocity off $\frac{dv}{dt} = -\frac{1}{5}(v-49)$ without solving it? | Set the right side to 0 to get $v=49$; direction field segments above and below this line both point toward it as $t$ grows. | p.2-3; procedure |

## Solving the Falling Object Initial Value Problem
| Front | Back | Notes |
| --- | --- | --- |
| Key move to solve $\frac{dv}{dt} = -\frac{1}{5}(v-49)$ with $v(0)=0$? | Separate variables to get the general solution $v(t) = 49 + Ce^{-t/5}$, then use $v(0)=0$ to find $C=-49$, giving $v(t) = 49(1-e^{-t/5})$. | p.3-4; procedure |

## Distance Fallen and Time of Impact
| Front | Back | Notes |
| --- | --- | --- |
| Key move to find the time when $x(t) = 49t - 245(1-e^{-t/5})$ reaches 300? | Integrate $v(t)$ to get $x(t)$, then solve the transcendental equation $49t_g + 245e^{-t_g/5} - 545 = 0$ numerically by checking where $h(t)$ changes sign and narrowing the interval. | p.5; procedure |

## Direction Field Depending on Both Variables
| Front | Back | Notes |
| --- | --- | --- |
| Key move to sketch the direction field of $y' = \frac{x-y}{1+x^2}$? | Compute $y'$ at a grid of $(x,y)$ pairs; since $1+x^2>0$ always, the sign of $y'$ matches the sign of $x-y$, so slopes are zero on $y=x$, positive below it, negative above it. | p.6; procedure |

## Falling Object with Different Initial Velocities
| Front | Back | Notes |
| --- | --- | --- |
| Key move to solve $v(0)=50$ and $v(0)=100$ using $v(t)=49+Ce^{-t/5}$? | Plug in $t=0$ and the given initial velocity to solve for $C$ each time: $C=1$ gives $v(t)=49+e^{-t/5}$; $C=51$ gives $v(t)=49+51e^{-t/5}$. | p.6-7; procedure |

## Class Attendance Model
| Front | Back | Notes |
| --- | --- | --- |
| Key move to solve $\frac{dp}{dt} = \frac{1}{2}p - 100$, $p(0)=170$, for when attendance hits 0? | Rewrite as $\frac{dp}{dt} = \frac{1}{2}(p-200)$, separate and solve to get $p(t)=200-30e^{t/2}$, then set $p(t)=0$ and solve $e^{t/2}=\frac{20}{3}$ for $t \approx 3.794$ months. | p.7-8; procedure |

## Verifying a Solution to an ODE
| Front | Back | Notes |
| --- | --- | --- |
| What must you do to verify a proposed solution to a differential equation? | Differentiate the proposed function, then substitute it (and its derivative) back into the equation and check both sides agree. | p.1; procedure |

## Terminal Velocity
| Front | Back | Notes |
| --- | --- | --- |
| In the falling-object example, what physical name is given to the equilibrium value $v=49$? | The terminal velocity. | p.3; definition |

# Node map
```json
[
 {
  "name": "Differential Equation",
  "type": "concept",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [],
  "uses": [],
  "page": 1,
  "summary": "A differential equation is an equation containing one or more derivatives of an unknown function."
 },
 {
  "name": "Independent vs Dependent Variable",
  "type": "concept",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [
   "Differential Equation"
  ],
  "uses": [],
  "page": 2,
  "summary": "The independent variable is chosen freely (e.g. $t$); the dependent variable's value is determined by it (e.g. $v=v(t)$)."
 },
 {
  "name": "Direction Field",
  "type": "concept",
  "existing": true,
  "parent": "1st Order ODE",
  "prereqs": [
   "Differential Equation",
   "Independent vs Dependent Variable"
  ],
  "uses": [],
  "page": 2,
  "summary": "A picture of a first-order ODE made by drawing a short segment of the assigned slope at each point of the plane; shows solution shape, not a formula."
 },
 {
  "name": "Equilibrium Solution",
  "type": "concept",
  "existing": true,
  "parent": "Separable Differential Equations",
  "prereqs": [
   "Differential Equation"
  ],
  "uses": [],
  "page": 3,
  "summary": "A constant solution where the derivative is zero everywhere, found by setting the right-hand side of the ODE to zero and solving."
 },
 {
  "name": "Separation of Variables",
  "type": "concept",
  "existing": false,
  "parent": "Separable Differential Equations",
  "prereqs": [
   "Differential Equation"
  ],
  "uses": [],
  "page": 4,
  "summary": "A method for solving separable ODEs: isolate all terms of the dependent variable on one side and the independent variable on the other, then integrate both sides."
 },
 {
  "name": "Initial Value Problem",
  "type": "concept",
  "existing": true,
  "parent": "Separable Differential Equations",
  "prereqs": [
   "Differential Equation",
   "Independent vs Dependent Variable"
  ],
  "uses": [],
  "page": 4,
  "summary": "A differential equation paired with an initial condition that fixes the unknown function's value at one point, used to pin down the constant in a general solution."
 },
 {
  "name": "General Solution",
  "type": "concept",
  "existing": false,
  "parent": "Separable Differential Equations",
  "prereqs": [
   "Separation of Variables"
  ],
  "uses": [],
  "page": 4,
  "summary": "The family of all solutions of an ODE, written with an arbitrary constant $C$; an initial condition selects one particular solution from the family."
 },
 {
  "name": "Verifying a Solution by Substitution",
  "type": "problem",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [],
  "uses": [
   "Differential Equation"
  ],
  "page": 1,
  "summary": "Check that $y(t)=3e^{2t}$ satisfies $y'=2y$ by differentiating and comparing to $2y$."
 },
 {
  "name": "Deriving the Falling Object Equation",
  "type": "problem",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [],
  "uses": [
   "Differential Equation"
  ],
  "page": 1,
  "summary": "Combine gravity $mg$ and drag $-\\gamma v$ with Newton's second law to derive $m\\frac{dv}{dt}=mg-\\gamma v$, then reduce to $\\frac{dv}{dt}=-\\frac{1}{5}(v-49)$ for $m=10$, $\\gamma=2$."
 },
 {
  "name": "Direction Field and Terminal Velocity for the Falling Object",
  "type": "problem",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [],
  "uses": [
   "Direction Field",
   "Equilibrium Solution"
  ],
  "page": 3,
  "summary": "Compute slopes of $\\frac{dv}{dt}=-\\frac{1}{5}(v-49)$ at several $v$ values and identify $v=49$ as the terminal velocity toward which all solutions move."
 },
 {
  "name": "Solving the Falling Object Initial Value Problem",
  "type": "problem",
  "existing": false,
  "parent": "Separable Differential Equations",
  "prereqs": [],
  "uses": [
   "Separation of Variables",
   "Initial Value Problem",
   "General Solution",
   "Equilibrium Solution"
  ],
  "page": 4,
  "summary": "Solve $\\frac{dv}{dt}=-\\frac{1}{5}(v-49)$ with $v(0)=0$ to get $v(t)=49(1-e^{-t/5})$."
 },
 {
  "name": "Distance Fallen and Time of Impact",
  "type": "problem",
  "existing": false,
  "parent": "Separable Differential Equations",
  "prereqs": [],
  "uses": [
   "Solving the Falling Object Initial Value Problem"
  ],
  "page": 5,
  "summary": "Integrate $v(t)$ to get position $x(t)=49t-245(1-e^{-t/5})$, then solve $x(t_g)=300$ numerically for the impact time $t_g\\approx10.51$ s and impact speed $\\approx43.01$ m/sec."
 },
 {
  "name": "Direction Field Depending on Both Variables",
  "type": "problem",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [],
  "uses": [
   "Direction Field",
   "Independent vs Dependent Variable"
  ],
  "page": 6,
  "summary": "Sketch the direction field of $y'=\\frac{x-y}{1+x^2}$ by evaluating slopes at sample $(x,y)$ pairs; slope sign matches the sign of $x-y$."
 },
 {
  "name": "Falling Object with Different Initial Velocities",
  "type": "problem",
  "existing": false,
  "parent": "Separable Differential Equations",
  "prereqs": [],
  "uses": [
   "General Solution",
   "Initial Value Problem"
  ],
  "page": 6,
  "summary": "Apply $v(0)=50$ and $v(0)=100$ to $v(t)=49+Ce^{-t/5}$ to get $v(t)=49+e^{-t/5}$ and $v(t)=49+51e^{-t/5}$ respectively."
 },
 {
  "name": "Class Attendance Model",
  "type": "problem",
  "existing": false,
  "parent": "Separable Differential Equations",
  "prereqs": [],
  "uses": [
   "Separation of Variables",
   "Equilibrium Solution",
   "Initial Value Problem",
   "General Solution"
  ],
  "page": 7,
  "summary": "Solve $\\frac{dp}{dt}=\\frac{1}{2}p-100$ with $p(0)=170$ to get $p(t)=200-30e^{t/2}$; find $p(3)\\approx65.55$ students and the time attendance hits 0, $t\\approx3.794$ months."
 },
 {
  "name": "Verifying a Solution to an ODE",
  "type": "concept",
  "existing": true,
  "parent": "",
  "prereqs": [],
  "summary": ""
 },
 {
  "name": "Terminal Velocity",
  "type": "concept",
  "existing": true,
  "parent": "",
  "prereqs": [],
  "summary": ""
 }
]
```

# Frankenstein problems

**Problem 1.** A cup of coffee cools according to $\frac{dT}{dt} = -\frac{1}{10}(T-20)$, where $T$ is temperature in Celsius and $t$ is time in minutes. The coffee starts at $90^\circ$C.
(a) Find the equilibrium solution and say what it represents physically.
(b) Solve the initial value problem for $T(t)$.
(c) Find the time when the coffee reaches $25^\circ$C.

*Concepts tested: Differential Equation, Equilibrium Solution, Separation of Variables, General Solution, Initial Value Problem.*

Solution.
(a) Set the right side to 0: $-\frac{1}{10}(T-20)=0 \Rightarrow T=20$. This is room temperature, the temperature the coffee approaches as $t\to\infty$.
(b) Separate variables: $\frac{dT/dt}{T-20} = -\frac{1}{10}$. Integrating, $\ln\lvert T-20\rvert = -\frac{t}{10}+c$, so $T-20 = Ce^{-t/10}$, i.e. $T(t) = 20 + Ce^{-t/10}$. Apply $T(0)=90$: $90 = 20 + C \Rightarrow C = 70$. So $T(t) = 20 + 70e^{-t/10}$.
(c) Set $T(t)=25$: $25 = 20 + 70e^{-t/10} \Rightarrow 5 = 70e^{-t/10} \Rightarrow e^{-t/10} = \frac{1}{14}$. Taking logs, $-\frac{t}{10} = -\ln 14 \Rightarrow t = 10\ln 14$. Since $\ln 14 = \ln 2 + \ln 7 \approx 0.6931 + 1.9459 = 2.6390$, $t \approx 26.39$ minutes.

**Problem 2.** Consider $\frac{dy}{dx} = -2(y-5)$.
(a) Identify the independent and dependent variable.
(b) Find the equilibrium solution.
(c) Compute $\frac{dy}{dx}$ at $y=3$ and at $y=8$, and describe how the direction field behaves near the equilibrium.
(d) Solve the initial value problem $y(0)=1$.

*Concepts tested: Independent vs Dependent Variable, Direction Field, Equilibrium Solution, Differential Equation, Separation of Variables, Initial Value Problem, General Solution.*

Solution.
(a) $x$ is the independent variable; $y$ is the dependent variable.
(b) Set the right side to 0: $-2(y-5)=0 \Rightarrow y=5$.
(c) At $y=3$: $\frac{dy}{dx} = -2(3-5) = -2(-2) = 4 > 0$, so $y$ increases toward 5. At $y=8$: $\frac{dy}{dx} = -2(8-5) = -6 < 0$, so $y$ decreases toward 5. In both cases the slope points toward $y=5$, so the direction field shows every solution converging on this equilibrium, just as the falling-object field converged on $v=49$.
(d) Separate variables: $\frac{dy}{y-5} = -2\,dx$. Integrating, $\ln\lvert y-5\rvert = -2x + c$, so $y - 5 = Ce^{-2x}$, i.e. $y(x) = 5 + Ce^{-2x}$. Apply $y(0)=1$: $1 = 5 + C \Rightarrow C = -4$. So $y(x) = 5 - 4e^{-2x}$. Check: $y'(x) = 8e^{-2x}$, and $-2(y-5) = -2(-4e^{-2x}) = 8e^{-2x}$, which matches.
