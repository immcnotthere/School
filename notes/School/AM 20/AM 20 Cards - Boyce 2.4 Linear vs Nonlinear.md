---
type: reference
parent: "[[AM20]]"
domain: math
course: "AM 20"
status: draft
source: "Boyce 2.4 Linear vs Nonlinear"
tags:
  - decks
---
# AM 20 Cards - Boyce 2.4 Linear vs Nonlinear Equations

## Existence and Uniqueness
| Front | Back | Notes |
| --- | --- | --- |
| Existence-uniqueness theorem for linear IVP $y'+p(t)y=g(t)$, $y(t_0)=y_0$: hypothesis and conclusion? | If $p,g$ continuous on open interval $I\ni t_0$, there is a unique solution $y=\phi(t)$ on all of $I$ | p.91; definition |
| Existence-uniqueness theorem for nonlinear IVP $y'=f(t,y)$, $y(t_0)=y_0$: hypothesis and conclusion? | If $f$ and $\partial f/\partial y$ are continuous in a rectangle around $(t_0,y_0)$, there is a unique solution on some interval $t_0-h<t<t_0+h$ (only guaranteed locally) | p.92; definition |
| Key difference between the linear and nonlinear existence-uniqueness theorems regarding where the solution is guaranteed to exist? | Linear: the solution exists on the whole interval where $p,g$ are continuous. Nonlinear: only guaranteed on some (possibly smaller) interval around $t_0$ | p.92-93; discrimination |
| Geometric consequence of the uniqueness part of these theorems for solution graphs? | Two distinct solution curves of the same equation can never intersect | p.93; concept |
| For the linear equation $y'+p(t)y=g(t)$, at what points can the solution be discontinuous or fail to exist? | Only at points where $p$ or $g$ is discontinuous | p.91; concept |
| Why is the existence-uniqueness proof for linear equations comparatively simple? | It's based on the explicit integrating-factor formula $y=\frac{1}{\mu(t)}\left[\int\mu(s)g(s)\,ds+y_0\right]$, which already shows a solution exists and is unique | p.92; concept |
| For $y'=f(t,y)$, what does continuity of $f$ alone (without $\partial f/\partial y$) guarantee? | Existence of a solution, but not uniqueness | p.93; discrimination |
| For $y'=f(t,y)$ with $f(t,y)=-p(t)y+g(t)$, how do the hypotheses of the nonlinear theorem reduce to the linear one? | $\partial f/\partial y=-p(t)$, so continuity of $f$ and $\partial f/\partial y$ becomes exactly continuity of $p$ and $g$ | p.92; concept |

## Interval of Existence (Nonlinear ODE)
| Front | Back | Notes |
| --- | --- | --- |
| For $y'=y^2$, $y(0)=y_0>0$, the solution $y=y_0/(1-y_0t)$ blows up at $t=1/y_0$. What does this show about nonlinear IVPs? | The interval of existence can depend on the initial condition itself, and generally can't be predicted without solving the equation | p.96; discrimination |

## Implicit Solutions
| Front | Back | Notes |
| --- | --- | --- |
| What is a first integral of a differential equation? | An implicit relation $F(t,y)=0$ satisfied by the solution; its graph is called an integral curve | p.96-97; definition |
| For which type of first-order equations can you usually get an explicit formula $y=\phi(t)$: linear or nonlinear? | Linear; nonlinear equations usually yield only an implicit relation, which may need numerical solving for $y$ | p.97; discrimination |

## Discontinuous Coefficients
| Front | Back | Notes |
| --- | --- | --- |
| How do you solve $y'+p(t)y=g(t)$ when $g$ (or $p$) has a jump discontinuity at $t_0$? | Solve separately on each side of $t_0$, then choose the constant on the later piece so $y$ is continuous at $t_0$ | p.98; procedure |
| Yes or no, and why: at a jump discontinuity matched for continuity, is the solution also differentiable there in general? | No; it's impossible in general to also make $y$ differentiable at $t_0$ when a coefficient jumps there | p.98; concept |

## Bernoulli Equation
| Front | Back | Notes |
| --- | --- | --- |
| General form of a Bernoulli equation? | $y'+p(t)y=q(t)y^n$ | p.99; definition |
| Substitution that linearizes a Bernoulli equation for $n\neq0,1$? | $v=y^{1-n}$ | p.99; procedure |
| What happens to the Bernoulli equation when $n=0$ or $n=1$? | It's already linear, so no substitution is needed | p.99; discrimination |

## Nonuniqueness Example
| Front | Back | Notes |
| --- | --- | --- |
| $y'=y^{1/3}$, $y(0)=0$. Why does the theorem not guarantee uniqueness, and what solutions exist? | $f=y^{1/3}$ is continuous everywhere but $\partial f/\partial y=\tfrac13y^{-2/3}$ is discontinuous at $y=0$; solutions include $y=0$, $y=\pm(2t/3)^{3/2}$, and infinitely many spliced versions | p.95-96; procedure |

## Finite-Time Blowup
| Front | Back | Notes |
| --- | --- | --- |
| Solve $y'=y^2$, $y(0)=y_0>0$, and state the interval of existence. | Separable: $-1/y=t+c$, $c=-1/y_0$, so $y=\dfrac{y_0}{1-y_0t}$, valid on $-\infty<t<1/y_0$ | p.96; procedure |

## Discontinuous Forcing IVP
| Front | Back | Notes |
| --- | --- | --- |
| Solve $y'+2y=g(t)$, $y(0)=0$, where $g(t)=1$ for $0\le t\le1$ and $g(t)=0$ for $t>1$. | For $0\le t\le1$: $y=\tfrac12(1-e^{-2t})$. Matching at $t=1$ gives, for $t>1$: $y=\tfrac12(e^2-1)e^{-2t}$ | p.98; procedure |

## Bernoulli Substitution Example
| Front | Back | Notes |
| --- | --- | --- |
| Solve $t^2y'+2ty-y^3=0$ ($t>0$) as a Bernoulli equation. | Rewrite $y'+(2/t)y=t^{-2}y^3$ ($n=3$); let $v=y^{-2}$ to get the linear equation $v'-(4/t)v=-2t^{-2}$, solved with integrating factor $\mu=t^{-4}$ | p.100; procedure |

# Node map
```json
[
 {
  "name": "Existence and Uniqueness",
  "type": "concept",
  "existing": true,
  "parent": "Differences Between Linear and Nonlinear Equations",
  "prereqs": [],
  "uses": [],
  "page": 91,
  "summary": "Linear IVPs with continuous p,g have a unique solution on the whole interval of continuity; nonlinear IVPs with continuous f and partial f/partial y have a unique solution only locally."
 },
 {
  "name": "Linear ODE",
  "type": "concept",
  "existing": true,
  "parent": "Differences Between Linear and Nonlinear Equations",
  "prereqs": [
   "Integrating-Factor"
  ],
  "uses": [],
  "page": 91,
  "summary": "First order linear equations y' + p(t)y = g(t) have solutions guaranteed to exist and be unique wherever p and g are continuous."
 },
 {
  "name": "Nonlinear ODE",
  "type": "concept",
  "existing": true,
  "parent": "Differences Between Linear and Nonlinear Equations",
  "prereqs": [
   "Existence and Uniqueness"
  ],
  "uses": [],
  "page": 92,
  "summary": "Equations y' = f(t,y) that are not linear; existence and uniqueness require continuity of both f and partial f/partial y, and only hold locally."
 },
 {
  "name": "Interval of Existence (Nonlinear ODE)",
  "type": "concept",
  "existing": false,
  "parent": "Differences Between Linear and Nonlinear Equations",
  "prereqs": [
   "Nonlinear ODE",
   "Existence and Uniqueness"
  ],
  "uses": [],
  "page": 94,
  "summary": "For nonlinear IVPs the interval on which a solution exists often depends on the initial condition and can only be found by solving the equation."
 },
 {
  "name": "Implicit Solutions",
  "type": "concept",
  "existing": true,
  "parent": "Differences Between Linear and Nonlinear Equations",
  "prereqs": [
   "Separable Equation"
  ],
  "uses": [],
  "page": 96,
  "summary": "A first integral F(t,y)=0 defines the solution implicitly when an explicit formula cannot be found, common for nonlinear equations."
 },
 {
  "name": "Discontinuous Coefficients",
  "type": "concept",
  "existing": false,
  "parent": "Differences Between Linear and Nonlinear Equations",
  "prereqs": [
   "Integrating-Factor",
   "Linear ODE"
  ],
  "uses": [],
  "page": 98,
  "summary": "When a linear equation's coefficients have a jump discontinuity, solve piecewise and match constants for continuity at the break point."
 },
 {
  "name": "Bernoulli Equation",
  "type": "concept",
  "existing": false,
  "parent": "Differences Between Linear and Nonlinear Equations",
  "prereqs": [
   "Linear ODE",
   "Integrating-Factor"
  ],
  "uses": [],
  "page": 99,
  "summary": "y' + p(t)y = q(t)y^n is linearized by the substitution v = y^(1-n) for n not equal to 0 or 1."
 },
 {
  "name": "Nonuniqueness Example",
  "type": "problem",
  "existing": false,
  "parent": "Differences Between Linear and Nonlinear Equations",
  "prereqs": [
   "Existence and Uniqueness",
   "Nonlinear ODE"
  ],
  "uses": [
   "Existence and Uniqueness",
   "Nonlinear ODE"
  ],
  "page": 95,
  "summary": "y' = y^(1/3), y(0)=0 has infinitely many solutions because partial f/partial y fails to be continuous at y=0."
 },
 {
  "name": "Finite-Time Blowup",
  "type": "problem",
  "existing": false,
  "parent": "Differences Between Linear and Nonlinear Equations",
  "prereqs": [
   "Nonlinear ODE",
   "Interval of Existence (Nonlinear ODE)"
  ],
  "uses": [
   "Existence and Uniqueness",
   "Interval of Existence (Nonlinear ODE)",
   "Nonlinear ODE"
  ],
  "page": 96,
  "summary": "y' = y^2 has a solution that blows up in finite time depending on the initial condition."
 },
 {
  "name": "Discontinuous Forcing IVP",
  "type": "problem",
  "existing": false,
  "parent": "Differences Between Linear and Nonlinear Equations",
  "prereqs": [
   "Discontinuous Coefficients"
  ],
  "uses": [
   "Discontinuous Coefficients",
   "Integrating-Factor"
  ],
  "page": 98,
  "summary": "Piecewise-defined forcing term solved on each interval and matched for continuity."
 },
 {
  "name": "Bernoulli Substitution Example",
  "type": "problem",
  "existing": false,
  "parent": "Differences Between Linear and Nonlinear Equations",
  "prereqs": [
   "Bernoulli Equation"
  ],
  "uses": [
   "Bernoulli Equation",
   "Integrating-Factor"
  ],
  "page": 100,
  "summary": "Worked Bernoulli equation reduced to a linear ODE and solved by integrating factor."
 }
]
```

# Frankenstein problems

**FP1.** Consider the IVP $y'+\dfrac{1}{t}y=ty^3$, $y(1)=1$, for $t>0$. (a) Is this equation linear or nonlinear? Which theorem applies near $t=1$, and what does it guarantee? (b) Recognize it as a Bernoulli equation and solve for $y(t)$. (c) State the exact interval on which your explicit solution is valid, and explain why this could not have been predicted from the existence-uniqueness theorem alone.

*Concepts tested:* Existence and Uniqueness, Nonlinear ODE, Bernoulli Equation.

*Solution.* (a) Nonlinear (the $y^3$ term). With $f(t,y)=ty^3-y/t$, $\partial f/\partial y=3ty^2-1/t$ is continuous for $t\neq0$, so Theorem 2.4.2 applies near $(1,1)$: it guarantees a unique solution on some interval around $t=1$, without saying how large.

(b) This is Bernoulli with $n=3$. Dividing by $y^3$: $y^{-3}y'+\dfrac1t y^{-2}=t$. Let $v=y^{-2}$, so $v'=-2y^{-3}y'$, giving $-\tfrac12v'+v/t=t$, i.e. $v'-\dfrac2t v=-2t$. Integrating factor $\mu=t^{-2}$: $(vt^{-2})'=-2/t$, so $vt^{-2}=-2\ln t+C$, $v=t^2(C-2\ln t)$. At $t=1$, $y=1\Rightarrow v=1=1\cdot(C-0)\Rightarrow C=1$. So $v=t^2(1-2\ln t)$ and $y=\dfrac{1}{t\sqrt{1-2\ln t}}$ (positive root since $y(1)=1>0$).

(c) The solution requires $1-2\ln t>0$, i.e. $t<\sqrt e\approx1.6487$, together with $t>0$; the interval of existence containing $t=1$ is $0<t<\sqrt e$. This blow-up point could not be predicted from Theorem 2.4.2 alone, since it only guarantees local existence near $t=1$ without specifying how far the solution extends; for nonlinear equations the interval of existence depends on the initial condition and is found only by solving.

**FP2.** Solve the IVP $y'+p(t)y=0$, $y(0)=3$, where $p(t)=1$ for $0\le t\le2$ and $p(t)=3$ for $t>2$. State whether the resulting $y(t)$ is continuous and/or differentiable at $t=2$.

*Concepts tested:* Discontinuous Coefficients, Integrating-Factor, General Solution.

*Solution.* For $0\le t\le2$: $y'+y=0\Rightarrow y=Ce^{-t}$; $y(0)=3\Rightarrow y=3e^{-t}$, so $y(2)=3e^{-2}$. For $t>2$: $y'+3y=0\Rightarrow y=De^{-3t}$; matching at $t=2$: $De^{-6}=3e^{-2}\Rightarrow D=3e^4$, so $y=3e^{4-3t}$ for $t>2$. Checking derivatives: $y'(2^-)=-3e^{-2}$ (from $y=3e^{-t}$), while $y'(2^+)=-9e^{-2}$ (from $y=3e^{4-3t}$, $y'=-9e^{4-3t}$ at $t=2$). Since $y(2^-)=y(2^+)=3e^{-2}$, $y$ is continuous at $t=2$, but since $-3e^{-2}\neq-9e^{-2}$, $y$ is not differentiable there.
