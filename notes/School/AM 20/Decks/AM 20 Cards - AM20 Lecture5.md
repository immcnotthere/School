---
type: reference
parent: "[[AM20]]"
domain: math
course: "AM 20"
status: draft
source: "AM20 Lecture5"
tags:
  - decks
---
# AM 20 Cards - AM20 Lecture5 Modeling and Autonomous Equations

## Rate Balance (Inflow Minus Outflow)
| Front | Back | Notes |
| --- | --- | --- |
| What is the general rate-balance equation for a changing quantity $Q$ with an inflow and an outflow? | $\dfrac{dQ}{dt} = \dfrac{dQ}{dt}\bigg\vert_{in} - \dfrac{dQ}{dt}\bigg\vert_{out}$ | p.1; formula |
| What are the four steps for turning a word problem into a differential equation? | Identify what is given and sought; identify the changing quantities and express each change as a rate; write the governing equation with initial conditions and constraints; solve subject to those conditions | p.1; procedure |
| What is the quickest way to catch a modeling mistake when writing a rate-balance equation $dQ/dt = \text{in} - \text{out}$? | Check that the inflow term and the outflow term carry the same units | p.1; concept |
| In a well-stirred tank mixing problem, how do you compute the outflow rate of a dissolved substance? | Multiply the outflow rate of liquid (e.g. gal per min) by the concentration in the tank, which equals the amount of substance divided by the constant volume | p.1, 2; procedure |

## Newton's Law of Cooling
| Front | Back | Notes |
| --- | --- | --- |
| What is Newton's law of cooling as a differential equation? | $\dfrac{dT}{dt} = -k(T-T_a)$, with $k>0$ and room temperature $T_a$ | p.3; formula |
| What is the general solution of Newton's law of cooling, $dT/dt = -k(T-T_a)$? | $T(t) = T_a + Ce^{-kt}$ | p.3; formula |
| Given an object's initial temperature and one later temperature reading, how do you find $C$ and $k$ in $T(t)=T_a+Ce^{-kt}$? | Use $t=0$ and the initial temperature to solve for $C$, then substitute the later time and temperature reading and take a logarithm to solve for $k$ | p.3, 4; procedure |

## Autonomous vs Non-Autonomous ODE
| Front | Back | Notes |
| --- | --- | --- |
| What does it mean for an ODE to be autonomous? | The independent variable does not appear explicitly, so it has the form $dy/dt = f(y)$ | p.4; definition |
| What does it mean for an ODE to be non-autonomous? | The independent variable appears explicitly, so it has the form $dy/dt = f(t,y)$ | p.4; definition |
| Why is $m\,dv/dt = mg-\gamma v$ autonomous, while $dy/dx - 2y = 4-x$ is non-autonomous? | The falling-object equation's right side contains only $v$, not $t$; the second equation's right side contains $x$ explicitly | p.4, 5; discrimination |
| How do you convert a non-autonomous scalar equation $dy/dt = f(t,y)$ into an autonomous system? | Set $y_1=y$, $y_2=t$; then $y_2'=1$, and $y_1'=f(y_2,y_1),\ y_2'=1$ is an autonomous system (one equation becomes two) | p.5; procedure |

## Equilibrium Solution
| Front | Back | Notes |
| --- | --- | --- |
| How can you find the limiting (equilibrium) value of an autonomous ODE $dy/dt=f(y)$ without solving the equation? | Set $f(y)=0$ and solve for $y$; this constant value is where the competing rates (inflow/outflow, growth/decay) balance | p.2; procedure |

## Recognizing Which Solution Method Applies
| Front | Back | Notes |
| --- | --- | --- |
| How can you tell that $y'-2y=4-x$ is not separable? | Its right side $2y+4-x$ is a sum of a term in $y$ and a term in $x$ that cannot be factored into (a function of $x$) times (a function of $y$) | p.6; discrimination |
| For $m\,dv/dt=mg-\gamma v$, what is the linear canonical form, and what does writing it in separable form require? | Dividing by $m$ gives $v'+\frac{\gamma}{m}v=g$ (linear canonical form); the separable form $\frac{m}{mg-\gamma v}dv - dt = 0$ requires dividing by $mg-\gamma v$, valid only where $mg-\gamma v\neq 0$ | p.5, 6; procedure |

## Mixing Tank IVP, Solution, and Long-Run Level
| Front | Back | Notes |
| --- | --- | --- |
| Example 1(a-c): set up and solve the salt-tank IVP $Q'+\frac{r}{100}Q=\frac{r}{4}$, $Q(0)=Q_0$, and find $Q_L=\lim_{t\to\infty}Q(t)$. What is the key result? | Using $\mu(t)=e^{rt/100}$, $Q(t)=25+(Q_0-25)e^{-rt/100}$; since $r>0$, $e^{-rt/100}\to0$, so $Q_L=25$ lb, which also follows directly from setting $Q'=0$ | p.1, 2; problem |
| In the mixing-tank problem, why does the equilibrium salt level $Q_L=25$ lb not depend on the flow rate $r$? | $Q_L$ solves $\frac{r}{100}Q=\frac{r}{4}$, and $r$ cancels from both sides, leaving $Q=25$ regardless of $r$ | p.2; discrimination |

## Mixing Tank Time to Reach Within 2% of Equilibrium
| Front | Back | Notes |
| --- | --- | --- |
| Example 1(d): with $r=3$ and $Q_0=2Q_L=50$, find the time $T$ after which $\lvert Q(t)-Q_L\rvert \le 0.02\,Q_L$ for all $t\ge T$. What is the key move and answer? | $Q(t)-Q_L=25e^{-3t/100}$ is positive, so solve $25e^{-3t/100}\le 0.5$, i.e. $e^{-3t/100}\le 0.02$; taking logs (and flipping the inequality) gives $t \ge \frac{-100\ln(0.02)}{3}\approx 130.4$ minutes | p.2, 3; problem |

## Flow Rate Needed to Reach Equilibrium by a Deadline
| Front | Back | Notes |
| --- | --- | --- |
| Example 2: using the setup of part (d), find $r$ so that the settling time $T\le 45$ minutes. What is the key move and answer? | The same inequality gives $T=\frac{-100\ln(0.02)}{r}$; requiring $T\le 45$ gives $r \ge \frac{-100\ln(0.02)}{45}\approx 8.693$ gal/min, so a higher flow rate shortens the settling time | p.3; problem |

## Two-Point Fit for Newton's Law of Cooling and Time to Target Temperature
| Front | Back | Notes |
| --- | --- | --- |
| Example 3: an object cools from $100^\circ$ to $60^\circ$C in 10 minutes in a $T_a=20^\circ$ room; find $T(t)$ and the time to reach $30^\circ$. What is the key result? | $T(t)=20+80e^{-kt}$ with $60=20+80e^{-10k}$ giving $k=\frac{\ln 2}{10}$, so $T(t)=20+80(1/2)^{t/10}$; setting $T=30$ gives $(1/2)^{t/10}=1/8=(1/2)^3$, so $t=30$ minutes | p.3, 4; problem |

## Converting a Non-Autonomous Equation to an Autonomous System
| Front | Back | Notes |
| --- | --- | --- |
| Example 7: convert $y'-2y=4-x$ into an autonomous system. What is the key move and result? | Solve for the derivative, $y'=2y+4-x$; set $y_1=y,\ y_2=x$, giving the autonomous system $y_1'=2y_1+4-y_2,\ y_2'=1$ | p.5; problem |

## Classifying and Writing Canonical Forms for Three Equations
| Front | Back | Notes |
| --- | --- | --- |
| Example 8: for the falling-object, population, and $y'-2y=4-x$ equations, which solution methods apply and what are their canonical forms? | Falling object $mv'=mg-\gamma v$: both methods apply, linear form $v'+\frac{\gamma}{m}v=g$; population $p'=\frac12p-a$: both apply, linear form $p'-\frac12p=-a$; $y'-2y=4-x$: not separable, so only integrating factors applies, already canonical as $y'-2y=4-x$ | p.5, 6; problem |

# Node map
```json
[
 {
  "name": "Rate Balance (Inflow Minus Outflow)",
  "type": "concept",
  "existing": false,
  "parent": "Modeling with ODEs",
  "prereqs": [],
  "uses": [],
  "page": 1,
  "summary": "The modeling equation $dQ/dt = (dQ/dt)_{in} - (dQ/dt)_{out}$ used to turn a description of a changing quantity into a first-order ODE."
 },
 {
  "name": "Newton's Law of Cooling",
  "type": "concept",
  "existing": true,
  "parent": "Modeling with ODEs",
  "prereqs": [
   "Integrating-Factor"
  ],
  "uses": [],
  "page": 3,
  "summary": "The model $dT/dt=-k(T-T_a)$, with general solution $T(t)=T_a+Ce^{-kt}$, fit using an initial temperature and one later reading."
 },
 {
  "name": "Autonomous vs Non-Autonomous ODE",
  "type": "concept",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [],
  "uses": [],
  "page": "4-5",
  "summary": "An ODE $dy/dt=f(y)$ is autonomous (no explicit $t$); $dy/dt=f(t,y)$ is non-autonomous; any non-autonomous scalar equation can be made autonomous by promoting $t$ to a second unknown function."
 },
 {
  "name": "Equilibrium Solution",
  "type": "concept",
  "existing": true,
  "parent": "1st Order ODE",
  "prereqs": [
   "Autonomous vs Non-Autonomous ODE"
  ],
  "uses": [],
  "page": 2,
  "summary": "For an autonomous equation $dy/dt=f(y)$, the constant (limiting) solutions solve $f(y)=0$, found without solving the full ODE."
 },
 {
  "name": "Recognizing Which Solution Method Applies",
  "type": "concept",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [
   "Integrating-Factor"
  ],
  "uses": [],
  "page": "5-6",
  "summary": "An equation is separable only if its right side factors into a function of the independent variable times a function of the dependent variable; otherwise, if linear, use integrating factors instead."
 },
 {
  "name": "Mixing Tank IVP, Solution, and Long-Run Level",
  "type": "problem",
  "existing": false,
  "parent": "Modeling with ODEs",
  "prereqs": [],
  "uses": [
   "Rate Balance (Inflow Minus Outflow)",
   "Integrating-Factor",
   "Equilibrium Solution"
  ],
  "page": "1-2",
  "summary": "Example 1(a-c): setting up and solving the salt-tank IVP and finding the long-run salt level $Q_L=25$ lb."
 },
 {
  "name": "Mixing Tank Time to Reach Within 2% of Equilibrium",
  "type": "problem",
  "existing": false,
  "parent": "Modeling with ODEs",
  "prereqs": [],
  "uses": [
   "Rate Balance (Inflow Minus Outflow)",
   "Equilibrium Solution"
  ],
  "page": "2-3",
  "summary": "Example 1(d): solving an exponential inequality to find the time after which the salt level stays within 2% of equilibrium."
 },
 {
  "name": "Flow Rate Needed to Reach Equilibrium by a Deadline",
  "type": "problem",
  "existing": false,
  "parent": "Modeling with ODEs",
  "prereqs": [],
  "uses": [
   "Rate Balance (Inflow Minus Outflow)",
   "Equilibrium Solution"
  ],
  "page": 3,
  "summary": "Example 2: finding the minimum flow rate $r$ so the tank settles to within 2% of equilibrium within 45 minutes."
 },
 {
  "name": "Two-Point Fit for Newton's Law of Cooling and Time to Target Temperature",
  "type": "problem",
  "existing": false,
  "parent": "Modeling with ODEs",
  "prereqs": [],
  "uses": [
   "Newton's Law of Cooling"
  ],
  "page": "3-4",
  "summary": "Example 3: fitting $T(t)=20+80e^{-kt}$ from two temperature readings and finding when the object reaches 30 degrees."
 },
 {
  "name": "Converting a Non-Autonomous Equation to an Autonomous System",
  "type": "problem",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [],
  "uses": [
   "Autonomous vs Non-Autonomous ODE"
  ],
  "page": 5,
  "summary": "Example 7: converting $y'-2y=4-x$ into the autonomous system $y_1'=2y_1+4-y_2,\\ y_2'=1$."
 },
 {
  "name": "Classifying and Writing Canonical Forms for Three Equations",
  "type": "problem",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [],
  "uses": [
   "Recognizing Which Solution Method Applies",
   "Autonomous vs Non-Autonomous ODE"
  ],
  "page": "5-6",
  "summary": "Example 8: classifying the falling-object, population, and $y'-2y=4-x$ equations by which solution methods apply."
 }
]
```

# Frankenstein problems

**Problem A.** A 200-gallon tank starts with 10 lb of dissolved salt. Brine containing 0.5 lb of salt per gallon enters at 5 gal/min, and the well-stirred solution drains at the same rate. Find $Q(t)$, the equilibrium level $Q_L$, and the time $T$ after which $Q(t)$ stays within 5% of $Q_L$.

*Concepts tested:* Rate Balance (Inflow Minus Outflow), Integrating-Factor, Equilibrium Solution.

*Solution.* Inflow rate of salt: $(0.5)(5) = 2.5$ lb/min. Outflow rate: $\frac{Q}{200}\cdot 5 = \frac{Q}{40}$ lb/min. By the rate balance,
$$\frac{dQ}{dt} = 2.5 - \frac{Q}{40} \implies Q' + \frac{1}{40}Q = 2.5,\qquad Q(0)=10.$$

Integrating factor: $\mu(t) = e^{t/40}$. Then $\dfrac{d}{dt}(e^{t/40}Q) = 2.5e^{t/40}$, so
$$e^{t/40}Q = 2.5\cdot 40\, e^{t/40} + c = 100e^{t/40} + c \implies Q(t) = 100 + ce^{-t/40}.$$

Apply $Q(0)=10$: $10 = 100+c \implies c=-90$. So
$$Q(t) = 100 - 90e^{-t/40}.$$

Equilibrium: setting $Q'=0$ in $Q'+\frac1{40}Q=2.5$ gives $\frac{Q}{40}=2.5 \implies Q_L = 100$ lb, matching $\lim_{t\to\infty}Q(t)$.

Time within 5%: $\lvert Q(t)-Q_L\rvert = 90e^{-t/40} \le 0.05(100) = 5$, so $e^{-t/40}\le \frac{5}{90}=\frac1{18}$, giving $t \ge 40\ln 18 \approx 40(2.890) \approx 115.6$ minutes.

**Problem B.** A cup of coffee at $95^\circ$C sits in a room at $T_a=25^\circ$C and obeys Newton's law of cooling, cooling to $80^\circ$C after 5 minutes. (a) Explain why the equation is autonomous and give its equilibrium temperature without solving it. (b) Find $T(t)$ and $k$. (c) Find the time at which the coffee is within 1 degree of room temperature.

*Concepts tested:* Newton's Law of Cooling, Autonomous vs Non-Autonomous ODE, Equilibrium Solution.

*Solution.* (a) $dT/dt = -k(T-T_a)$ has $t$ nowhere on the right side, so it is autonomous. Setting $dT/dt=0$ gives $T=T_a=25^\circ$C as the equilibrium temperature, with no need to solve the equation.

(b) The general solution is $T(t) = 25 + Ce^{-kt}$. Using $T(0)=95$: $C=70$. Using $T(5)=80$:
$$80 = 25+70e^{-5k} \implies e^{-5k} = \frac{55}{70} = \frac{11}{14} \implies k = \frac{1}{5}\ln\frac{14}{11} \approx 0.04823\ \text{min}^{-1}.$$
So $T(t) = 25 + 70e^{-kt} = 25+70\left(\frac{11}{14}\right)^{t/5}$.

(c) Require $T(t)-25 = 70e^{-kt} \le 1$, so $e^{-kt}\le \frac1{70}$, giving $t \ge \dfrac{\ln 70}{k} \approx \dfrac{4.2485}{0.04823} \approx 88.1$ minutes.
