---
type: reference
parent: "[[AM20]]"
domain: math
course: "AM 20"
status: draft
source: "AM20 L1 Supplementary Problems"
tags:
  - decks
---
# AM 20 Cards - AM20 L1 Supplementary Problems First Order ODEs

## Verifying a Solution to an ODE
| Front | Back | Notes |
| --- | --- | --- |
| What are the 3 steps to verify that a proposed $y(t)$ solves an ODE? | 1) Differentiate the proposed y to get the left side; 2) substitute y into the right side; 3) compare: if both sides match for all t, and any given initial condition holds, y solves the equation. | p.1; procedure |
| When solving an initial value problem, what is checked in addition to the differential equation itself? | The initial condition: substitute the given starting time into the proposed solution and confirm it equals the given initial value. | p.1; discrimination |
| General template: to check $y=Ce^{kt}+a$ solves $y'=k(y-a)$, what do you compute on each side? | Left side: $y'=Cke^{kt}$. Right side: $k(y-a)=k\cdot Ce^{kt}$. These match for every C, confirming the general solution form. | p.1; procedure |

## Order and Variables of an ODE
| Front | Back | Notes |
| --- | --- | --- |
| In an ODE, how do you identify the independent variable? | It is the variable being differentiated with respect to; it appears in the denominator of the derivative, e.g. in $dQ/dt$, t is independent. | p.1; definition |
| In an ODE, how do you identify the dependent variable? | It is the unknown function whose derivative is being taken, e.g. in $dQ/dt$, Q is dependent. | p.1; definition |
| How is the order of an ODE determined? | By the order of the highest derivative appearing; the power to which a derivative is raised does not affect the order. | p.2; definition |

## Terminal Velocity
| Front | Back | Notes |
| --- | --- | --- |
| What is the terminal velocity of a falling object, in terms of the ODE $dv/dt=f(v)$? | The value of v where $dv/dt=0$; velocity stops changing because drag exactly balances gravity. | p.2; definition |
| For $dv/dt = g - (\gamma/m)v$, what is the terminal velocity? | $v_{term} = mg/\gamma$ | p.2; formula |
| How do you find terminal velocity without solving the ODE for v(t)? | Set the right hand side of the ODE to zero and solve for v algebraically. | p.2; procedure |

## Equilibrium Solution
| Front | Back | Notes |
| --- | --- | --- |
| What is an equilibrium solution of an autonomous ODE $y'=f(y)$? | A constant solution $y(t)\equiv c$ where $f(c)=0$, so $y'=0$ for all t. | p.2; definition |
| How do you find all equilibrium solutions of $y'=y(3-y)$? | Set $y(3-y)=0$, giving $y=0$ and $y=3$. | p.5; procedure |
| Yes or no, and why: is the curve where $y'=0$ always itself a solution of the ODE? | Only for autonomous equations $y'=f(y)$; for equations like $y'=t-y$, the zero slope line $y=t$ is not itself a solution. | p.3; discrimination |

## Asymptotic Stability
| Front | Back | Notes |
| --- | --- | --- |
| When is an equilibrium of an autonomous ODE called stable? | When solutions starting near it move toward it as t increases, on both sides. | p.3; definition |
| When is an equilibrium of an autonomous ODE called unstable? | When solutions starting near it move away from it on both sides. | p.3; definition |
| How do you classify an equilibrium's stability using sign analysis? | Test one point in each interval between equilibria; if $y'$ is negative below and positive above, solutions move away and it is unstable; if signs point toward it, it is stable. | p.5; procedure |

## Direction Field
| Front | Back | Notes |
| --- | --- | --- |
| What does a direction field, or slope field, show at each point (t, y)? | A short line segment with slope equal to $y'=f(t,y)$ evaluated at that point. | p.3; definition |

## Separation of Variables
| Front | Back | Notes |
| --- | --- | --- |
| What are the steps of separation of variables for $dy/dt = k(y-a)$? | 1) Rewrite as $\dfrac{dy/dt}{y-a}=k$; 2) integrate both sides to get $\ln\lvert y-a\rvert = kt+c$; 3) exponentiate and absorb the sign and constant to get $y=a+Ce^{kt}$; 4) apply the initial condition to solve for C. | p.4; procedure |
| General solution of $dy/dt = k(y-a)$? | $y(t) = a + Ce^{kt}$ | p.4; formula |
| What value of C in $y=a+Ce^{kt}$ recovers the equilibrium solution? | $C=0$, giving $y\equiv a$. | p.4; discrimination |
| Why must you assume $y\neq a$ before dividing by $(y-a)$ in separation of variables? | Division by zero is undefined at the equilibrium; the constant solution $y\equiv a$ is checked separately and added back in afterward. | p.4; procedure |

## Bisection Method
| Front | Back | Notes |
| --- | --- | --- |
| How do you numerically solve an equation $h(t)=0$ that mixes linear and exponential terms? | Evaluate $h(t)$ at trial points until it changes sign, then narrow the interval by testing points inside it until the root is pinned down. | p.6; procedure |
| How do you know a root of $h(t)=0$ lies between two points $t_1<t_2$? | When $h(t_1)$ and $h(t_2)$ have opposite signs, assuming h is continuous. | p.6; discrimination |

## Problem 1 Verify Exponential Solution
| Front | Back | Notes |
| --- | --- | --- |
| Key move: verify $y=4e^{5t}$ solves $y'=5y$? | Differentiate to get $y'=20e^{5t}$; compute $5y=20e^{5t}$; they match, so it is a solution, true for any constant multiple. | p.1; procedure |

## Problem 2 Verify Solution and Initial Condition
| Front | Back | Notes |
| --- | --- | --- |
| Key move: verify $y=3e^{-2t}+1$ solves $y'=-2y+2$, $y(0)=4$? | $y'=-6e^{-2t}$ matches $-2y+2=-6e^{-2t}$, and $y(0)=3+1=4$ matches the initial condition. | p.1 to 2; procedure |

## Problem 3 Identify Order and Variables
| Front | Back | Notes |
| --- | --- | --- |
| Key move: classify $(y')^3+ty=0$ by order and variables? | t is independent, y is dependent; the only derivative present is $y'$, so despite the cube, the equation is first order. | p.2; procedure |

## Problem 4 Falling Object Force Balance
| Front | Back | Notes |
| --- | --- | --- |
| Key move: find terminal velocity for $m\,dv/dt=mg-\gamma v$ without solving the ODE? | Set $dv/dt=0$: $0=mg-\gamma v \Rightarrow v=mg/\gamma$; with $m=4,\gamma=2,g=9.8$, $v=19.6$ m per sec. | p.2; procedure |

## Problem 5 Equilibrium of y prime equals y minus 2
| Front | Back | Notes |
| --- | --- | --- |
| Key move: find and classify the equilibrium of $y'=y-2$? | Equilibrium at $y=2$ where $y'=0$; the slope is negative below and positive above, so solutions move away, unstable. | p.2 to 3; procedure |

## Problem 6 Slope Table for y prime equals t minus y
| Front | Back | Notes |
| --- | --- | --- |
| Key move: find where $y'=t-y$ has zero slope, and is that curve a solution? | Zero slope occurs along $y=t$; substituting shows $y'=1$ but $t-y=0$ there, so $y=t$ is not itself a solution, just a set of horizontal tangent points. | p.3; procedure |

## Problem 7 Solve the Falling Object Equation
| Front | Back | Notes |
| --- | --- | --- |
| Key move: solve $dv/dt=9.8-0.5v$, $v(0)=0$, and find $v(4)$? | Separate variables to get $v(t)=19.6(1-e^{-t/2})$; then $v(4)=19.6(1-e^{-2})\approx 16.95$ m per sec. | p.3 to 4; procedure |

## Problem 8 Population Model Reaching Zero
| Front | Back | Notes |
| --- | --- | --- |
| Key move: solve $dp/dt=0.3p-60$, $p(0)=100$, and find when p reaches zero? | Solving gives $p(t)=200-100e^{0.3t}$; setting p to zero gives $e^{0.3t}=2 \Rightarrow t=\ln 2/0.3\approx 2.31$ years. | p.5; procedure |

## Problem 9 Equilibria of y prime equals y times 3 minus y
| Front | Back | Notes |
| --- | --- | --- |
| Key move: find and classify all equilibria of $y'=y(3-y)$? | Equilibria at $y=0$, unstable, and $y=3$, stable, found by testing the sign of $y'$ on the intervals $y<0$, $0<y<3$, and $y>3$. | p.5 to 6; procedure |

## Problem 10 Impact Time by Bisection
| Front | Back | Notes |
| --- | --- | --- |
| Key move: find the impact time $t_g$ when $x(t)=19.6t-39.2(1-e^{-t/2})=100$? | No closed form exists, so bracket sign changes of $h(t)=x(t)-100$ numerically, giving $t_g\approx 7.04$ sec and impact speed $v(t_g)\approx 19.02$ m per sec. | p.6 to 7; procedure |

## Problem 11 General Falling Object Formula and t90
| Front | Back | Notes |
| --- | --- | --- |
| Key move: find $t_{90}$, the time to reach 90 percent of the terminal velocity $mg/\gamma$? | Set $1-e^{-\gamma t_{90}/m}=0.9$, giving $t_{90}=(m/\gamma)\ln 10$; this does not depend on g. | p.7 to 8; procedure |

## Problem 12 Infer Drag and Gravity from Data
| Front | Back | Notes |
| --- | --- | --- |
| Key move: find gamma and g from a measured $v(t)=30(1-e^{-t/3})$ with $m=6$? | Match the exponent: $\gamma/m=1/3 \Rightarrow \gamma=2$ kg per sec; match the coefficient: $mg/\gamma=30 \Rightarrow g=10$ m per sec squared. | p.8 to 9; procedure |

## Problem 13 Object Thrown Upward
| Front | Back | Notes |
| --- | --- | --- |
| Key move: set up v(t) for the lecture object thrown up with $v(0)=-10$, down positive? | Reuse the general solution $v=49+Ce^{-t/5}$; $v(0)=-10$ gives $C=-59$, so $v(t)=49-59e^{-t/5}$, negative v means moving upward. | p.9 to 10; procedure |

## Problem 14 Attendance Model Thresholds
| Front | Back | Notes |
| --- | --- | --- |
| Key move: find the smallest whole $p_0$ with $p(3)\ge 150$ for $p(t)=200+(p_0-200)e^{t/2}$? | Solve $150=200+(p_0-200)e^{1.5}$ to get $p_0\approx 188.84$, then round up to the nearest whole number that still satisfies the inequality: $p_0=189$. | p.10 to 11; procedure |

## Problem 15 Isocline and Local Minimum
| Front | Back | Notes |
| --- | --- | --- |
| Key move: is the origin a local min or max for the solution of $y'=(x-y)/(1+x^2)$ through (0,0)? | Differentiate implicitly to get $2xy'+(1+x^2)y''=1-y'$; at (0,0), with $y'=0$, this gives $y''(0)=1>0$, so it is a local minimum. | p.11; procedure |

## Problem 16 Bounding Impact Speed
| Front | Back | Notes |
| --- | --- | --- |
| Key move: bound the impact speed for $v(0)=60$ without finding the impact time? | Since $v(t)=49+11e^{-t/5}$ and $0<e^{-t/5}<1$ for $t>0$, the impact speed satisfies $49<v<60$. | p.12; procedure |
| For a linear autonomous ODE $dy/dt=k(y-a)$ with $k<0$, why does $v(t)-a$ never change sign? | Because $v(t)-a=(v_0-a)e^{kt}$ and $e^{kt}>0$ for all t, so $v(t)-a$ always has the same sign as $v_0-a$; solutions never cross the equilibrium. | p.12; formula |

## Falling Object Model
| Front | Back | Notes |
| --- | --- | --- |
| For an object falling with drag coefficient gamma, what is the force balance F in terms of mg and v? | $F = mg - \gamma v$, gravity down, drag opposing the motion and proportional to speed. | p.2; formula |
| Newton's second law applied to a falling object with drag gives what ODE for v(t)? | $m\dfrac{dv}{dt} = mg - \gamma v$ | p.2; formula |
| With $m=4$ kg, $\gamma=2$ kg per sec, $g=9.8$, what does $m\,dv/dt = mg-\gamma v$ simplify to? | $\dfrac{dv}{dt} = 9.8 - 0.5v$, dividing the whole equation by m equals 4. | p.2; procedure |

## Isoclines
| Front | Back | Notes |
| --- | --- | --- |
| How do you find the curve along which every slope in a direction field equals a constant c? | Set $f(t,y)=c$ and solve for y in terms of t; this curve is called an isocline. | p.11; procedure |
| Yes or no, and why: is an isocline, a curve of constant slope, generally a solution curve? | No, it only marks where solutions have that particular slope as they cross it, not a curve that solutions follow. | p.11; discrimination |

# Node map
```json
[
 {
  "name": "Verifying a Solution to an ODE",
  "type": "concept",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [
   "Chain Rule"
  ],
  "uses": [],
  "page": 1,
  "summary": "To verify a proposed y(t) solves an ODE, differentiate it for the left side, substitute it into the right side, and confirm the two match for all t (and any initial condition holds)."
 },
 {
  "name": "Order and Variables of an ODE",
  "type": "concept",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [
   "Derivative"
  ],
  "uses": [],
  "page": 1,
  "summary": "The independent variable is the one differentiated with respect to, the dependent variable is the unknown function, and the order is set by the highest derivative present regardless of any power it is raised to."
 },
 {
  "name": "Second Law of Motion",
  "type": "concept",
  "existing": true,
  "parent": "1st Order ODE",
  "prereqs": [
   "Derivative"
  ],
  "uses": [],
  "page": 2,
  "summary": "For a falling object with linear drag, the force balance $F=mg-\\gamma v$ combined with $F=m\\,dv/dt$ gives the ODE $m\\,dv/dt=mg-\\gamma v$."
 },
 {
  "name": "Terminal Velocity",
  "type": "concept",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [
   "Second Law of Motion"
  ],
  "uses": [],
  "page": 2,
  "summary": "Terminal velocity is the constant speed at which a falling object's acceleration is zero, found by setting the right side of its velocity ODE to zero; for $dv/dt=g-(\\gamma/m)v$ it equals $mg/\\gamma$."
 },
 {
  "name": "Equilibrium Solution",
  "type": "concept",
  "existing": true,
  "parent": "1st Order ODE",
  "prereqs": [],
  "uses": [],
  "page": 2,
  "summary": "An equilibrium solution of an autonomous ODE $y'=f(y)$ is a constant function $y\\equiv c$ with $f(c)=0$; the zero-slope set is only guaranteed to be a solution when the equation is autonomous."
 },
 {
  "name": "Asymptotic Stability",
  "type": "concept",
  "existing": true,
  "parent": "1st Order ODE",
  "prereqs": [
   "Equilibrium Solution"
  ],
  "uses": [],
  "page": 3,
  "summary": "An equilibrium is stable if nearby solutions move toward it and unstable if they move away, classified by testing the sign of y' in the intervals between equilibria; for linear autonomous ODEs solutions never cross the equilibrium."
 },
 {
  "name": "Direction Field",
  "type": "concept",
  "existing": true,
  "parent": "1st Order ODE",
  "prereqs": [],
  "uses": [],
  "page": 3,
  "summary": "A direction field shows the slope $y'=f(t,y)$ as a short segment at each point; an isocline is a curve where that slope is constant, and it is generally not itself a solution curve."
 },
 {
  "name": "Separation of Variables",
  "type": "concept",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [
   "Equilibrium Solution",
   "Natural logarithm"
  ],
  "uses": [],
  "page": 4,
  "summary": "To solve $dy/dt=k(y-a)$, divide by $(y-a)$ assuming $y\\neq a$, integrate both sides to get $\\ln|y-a|=kt+c$, exponentiate, and absorb constants to reach the general solution $y=a+Ce^{kt}$."
 },
 {
  "name": "Bisection Method",
  "type": "concept",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [],
  "uses": [],
  "page": 6,
  "summary": "When an equation mixing linear and exponential terms has no closed-form root, evaluate the function at trial points until the sign changes, then narrow the bracketing interval to approximate the root."
 },
 {
  "name": "Problem 1 Verify Exponential Solution",
  "type": "problem",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [
   "Chain Rule"
  ],
  "uses": [
   "Verifying a Solution to an ODE"
  ],
  "page": 1,
  "summary": "Shows $y=4e^{5t}$ satisfies $y'=5y$ by differentiating and comparing both sides."
 },
 {
  "name": "Problem 2 Verify Solution and Initial Condition",
  "type": "problem",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [],
  "uses": [
   "Verifying a Solution to an ODE",
   "Initial Value Problem"
  ],
  "page": 1,
  "summary": "Shows $y=3e^{-2t}+1$ solves the IVP $y'=-2y+2$, $y(0)=4$ by checking both the equation and the initial condition."
 },
 {
  "name": "Problem 3 Identify Order and Variables",
  "type": "problem",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [],
  "uses": [
   "Order and Variables of an ODE"
  ],
  "page": 2,
  "summary": "Identifies the independent variable, dependent variable, and order for three sample ODEs."
 },
 {
  "name": "Problem 4 Falling Object Force Balance",
  "type": "problem",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [],
  "uses": [
   "Second Law of Motion",
   "Terminal Velocity"
  ],
  "page": 2,
  "summary": "Sets up the falling-object ODE for m=4, gamma=2, g=9.8 and finds the terminal velocity 19.6 m/sec without solving the ODE."
 },
 {
  "name": "Problem 5 Equilibrium of y prime equals y minus 2",
  "type": "problem",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [],
  "uses": [
   "Equilibrium Solution",
   "Asymptotic Stability"
  ],
  "page": 2,
  "summary": "Finds the equilibrium y=2 of $y'=y-2$ and shows it is unstable since nearby solutions move away."
 },
 {
  "name": "Problem 6 Slope Table for y prime equals t minus y",
  "type": "problem",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [],
  "uses": [
   "Direction Field",
   "Equilibrium Solution"
  ],
  "page": 3,
  "summary": "Tabulates slopes of $y'=t-y$ at nine points and shows the zero-slope line y=t is not itself a solution."
 },
 {
  "name": "Problem 7 Solve the Falling Object Equation",
  "type": "problem",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [
   "Second Law of Motion"
  ],
  "uses": [
   "Separation of Variables",
   "Terminal Velocity",
   "Initial Value Problem"
  ],
  "page": 3,
  "summary": "Solves $dv/dt=9.8-0.5v$, $v(0)=0$ by separation of variables to get $v(t)=19.6(1-e^{-t/2})$ and evaluates v(4)."
 },
 {
  "name": "Problem 8 Population Model Reaching Zero",
  "type": "problem",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [],
  "uses": [
   "Separation of Variables",
   "Equilibrium Solution"
  ],
  "page": 5,
  "summary": "Solves $dp/dt=0.3p-60$, $p(0)=100$ and finds the time at which the population reaches zero."
 },
 {
  "name": "Problem 9 Equilibria of y prime equals y times 3 minus y",
  "type": "problem",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [],
  "uses": [
   "Equilibrium Solution",
   "Asymptotic Stability"
  ],
  "page": 5,
  "summary": "Finds equilibria 0 and 3 of $y'=y(3-y)$ and classifies 0 as unstable and 3 as stable using sign analysis."
 },
 {
  "name": "Problem 10 Impact Time by Bisection",
  "type": "problem",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [
   "Terminal Velocity"
  ],
  "uses": [
   "Bisection Method",
   "Separation of Variables"
  ],
  "page": 6,
  "summary": "Finds the distance function x(t) for the falling object and numerically solves for the time it falls 100 meters."
 },
 {
  "name": "Problem 11 General Falling Object Formula and t90",
  "type": "problem",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [],
  "uses": [
   "Terminal Velocity",
   "Separation of Variables",
   "Verifying a Solution to an ODE"
  ],
  "page": 7,
  "summary": "Verifies the general falling-object formula, derives $t_{90}=(m/\\gamma)\\ln 10$, and applies it to the lecture object."
 },
 {
  "name": "Problem 12 Infer Drag and Gravity from Data",
  "type": "problem",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [],
  "uses": [
   "Terminal Velocity",
   "Separation of Variables"
  ],
  "page": 8,
  "summary": "Matches a measured velocity function to the general falling-object formula to back out gamma and g."
 },
 {
  "name": "Problem 13 Object Thrown Upward",
  "type": "problem",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [
   "Second Law of Motion"
  ],
  "uses": [
   "Separation of Variables",
   "Asymptotic Stability"
  ],
  "page": 9,
  "summary": "Applies the same falling-object ODE with a negative initial velocity to model an object thrown upward, finding peak height and return speed."
 },
 {
  "name": "Problem 14 Attendance Model Thresholds",
  "type": "problem",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [],
  "uses": [
   "Separation of Variables",
   "Equilibrium Solution"
  ],
  "page": 10,
  "summary": "Uses the general solution of an attendance model to find initial enrollments meeting given thresholds at t=3."
 },
 {
  "name": "Problem 15 Isocline and Local Minimum",
  "type": "problem",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [
   "Chain Rule"
  ],
  "uses": [
   "Direction Field"
  ],
  "page": 11,
  "summary": "Finds the isocline of slope 1 for $y'=(x-y)/(1+x^2)$, shows no line solves it, and classifies the origin as a local minimum."
 },
 {
  "name": "Problem 16 Bounding Impact Speed",
  "type": "problem",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [],
  "uses": [
   "Asymptotic Stability",
   "Separation of Variables"
  ],
  "page": 11,
  "summary": "Shows the sign of v(t)-49 never changes and uses this to bound the impact speed without computing the impact time."
 },
 {
  "name": "Falling Object Model",
  "type": "concept",
  "existing": true,
  "parent": "",
  "prereqs": [],
  "summary": ""
 },
 {
  "name": "Isoclines",
  "type": "concept",
  "existing": true,
  "parent": "",
  "prereqs": [],
  "summary": ""
 }
]
```

# Frankenstein problems

**Frankenstein Problem 1.** An object of mass $m=5$ kg falls from rest under gravity $g=9.8$ m/sec squared with drag coefficient $\gamma=1$ kg per sec, released from a height of 50 meters. Find the terminal velocity, solve for v(t) and x(t), and estimate the time to hit the ground and the impact speed.

*Concepts tested:* Second Law of Motion, Terminal Velocity, Separation of Variables, Initial Value Problem, Bisection Method.

Solution. Step 1. Force balance and terminal velocity. By Newton's second law, $m\,dv/dt = mg-\gamma v$, so $dv/dt = 9.8 - 0.2v$. Setting the right side to zero, $0=9.8-0.2v \Rightarrow v=49$ m per sec, the terminal velocity.

Step 2. Separate variables. Writing $9.8-0.2v = -0.2(v-49)$, since $-0.2(-49)=9.8$, separating and integrating gives $v(t) = 49 + Ce^{-0.2t}$. With $v(0)=0$, $C=-49$, so
$$v(t) = 49\left(1-e^{-0.2t}\right).$$

Step 3. Integrate for position. With $x(0)=0$,
$$x(t) = \int_0^t 49\left(1-e^{-0.2s}\right)ds = 49t - 49\cdot 5\left(1-e^{-0.2t}\right) = 49t - 245\left(1-e^{-0.2t}\right).$$

Step 4. Set up the impact equation. Setting $x(t_g)=50$,
$$49t_g - 245\left(1-e^{-0.2t_g}\right) = 50 \implies 49t_g + 245e^{-0.2t_g} = 295.$$

Step 5. Solve numerically. Let $h(t)=49t+245e^{-0.2t}-295$.
$h(3) = 147+245(0.5488)-295 = 147+134.46-295 = -13.54$.
$h(4) = 196+245(0.4493)-295 = 196+110.09-295 = 11.09$.
The root lies between 3 and 4. Narrowing, $h(3.57) = 174.93+245(0.4897)-295 = 174.93+119.98-295 = -0.09$, and $h(3.58) = 175.42+245(0.4887)-295 = 175.42+119.73-295 = 0.15$. So $t_g \approx 3.57$ seconds.

Step 6. Impact speed. $v(t_g) = 49\left(1-e^{-0.2(3.57)}\right) = 49(1-0.4897) = 49(0.5103) \approx 25.0$ m per sec.

The object reaches terminal velocity 49 m per sec, falls the 50 meters in about 3.57 seconds, and hits the ground at about 25.0 m per sec, roughly half its terminal speed.

**Frankenstein Problem 2.** Consider the autonomous equation $y' = (y+2)(1-y)$, where the prime denotes $d/dt$.
(a) State the order of this ODE and identify the independent and dependent variables.
(b) Find all equilibrium solutions.
(c) Using sign analysis, classify each equilibrium as stable or unstable.
(d) Verify that the constant function $y\equiv 1$ is a solution of the ODE.

*Concepts tested:* Order and Variables of an ODE, Equilibrium Solution, Asymptotic Stability, Verifying a Solution to an ODE.

Solution. (a) The prime denotes $d/dt$, so t is the independent variable and y is the dependent variable. The only derivative present is $y'$, so the equation is first order.

(b) Setting the right side to zero, $(y+2)(1-y)=0$, so $y=-2$ or $y=1$. Both $y\equiv -2$ and $y\equiv 1$ are equilibrium solutions.

(c) The two equilibria split the line into three intervals: $y<-2$, $-2<y<1$, and $y>1$.
Test $y=-3$: $(-3+2)(1-(-3)) = (-1)(4) = -4$, negative.
Test $y=0$: $(0+2)(1-0) = (2)(1) = 2$, positive.
Test $y=2$: $(2+2)(1-2) = (4)(-1) = -4$, negative.
At $y=-2$: just below, the slope is negative (moving further away), and just above, the slope is positive (also moving away from $-2$, toward 1). Both sides move away, so $y=-2$ is unstable.
At $y=1$: just below, the slope is positive (moving up toward 1), and just above, the slope is negative (moving down toward 1). Both sides approach, so $y=1$ is stable.

(d) For $y\equiv 1$, the left side is $y'=0$. The right side is $(1+2)(1-1) = (3)(0) = 0$. Both sides equal zero, so $y\equiv 1$ solves the ODE.
