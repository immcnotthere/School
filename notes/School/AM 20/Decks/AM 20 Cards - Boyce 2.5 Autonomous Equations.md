---
type: reference
parent: "[[AM20]]"
domain: math
course: "AM 20"
status: draft
source: "Boyce 2.5 Autonomous Equations"
tags:
  - decks
---
# AM 20 Cards - Boyce 2.5 Autonomous Equations and Population Dynamics

## Equilibrium Solution
| Front | Back | Notes |
| --- | --- | --- |
| What is the phase line for an autonomous equation? | The y-axis marked with dots at the equilibrium points and arrows showing whether $y$ increases or decreases between them, based on the sign of $f(y)$ | p.102-103; definition |

## Asymptotic Stability
| Front | Back | Notes |
| --- | --- | --- |
| Derivative test for stability of a critical point $y_1$ where $f(y_1)=0$? | Asymptotically stable if $f'(y_1)<0$; unstable if $f'(y_1)>0$ | p.111; procedure |

## Semistable Equilibrium
| Front | Back | Notes |
| --- | --- | --- |
| Definition: semistable equilibrium solution? | An equilibrium that solutions approach from one side but move away from on the other side | p.111; definition |
| For $dy/dt=k(1-y)^2$ ($k>0$), classify the equilibrium $y=1$. | Semistable: $(1-y)^2\ge0$ always, so $y$ increases on both sides of 1; solutions below approach it, solutions above move away | p.111; discrimination |

## Logistic-Growth
| Front | Back | Notes |
| --- | --- | --- |
| Logistic (Verhulst) equation in standard form, intrinsic growth rate $r$, carrying capacity $K$? | $dy/dt=r\left(1-\dfrac{y}{K}\right)y$ | p.102; formula |
| Explicit solution of the logistic equation with $y(0)=y_0$? | $y(t)=\dfrac{y_0K}{y_0+(K-y_0)e^{-rt}}$ | p.105; formula |
| What is the meaning of the constant $K$ in the logistic model? | The carrying capacity or saturation level: the population approaches $K$ as $t\to\infty$ for any positive initial population | p.104-105; definition |
| At what population value does the logistic growth curve have its inflection point? | $y=K/2$ (concave up for $0<y<K/2$, concave down for $K/2<y<K$) | p.104; formula |
| In the logistic equation $dy/dt=r(1-y/K)y$, which equilibrium is asymptotically stable and which is unstable? | $y=K$ is asymptotically stable; $y=0$ is unstable | p.105-106; discrimination |

## Critical Threshold Model
| Front | Back | Notes |
| --- | --- | --- |
| Threshold equation and the stability of its two equilibria? | $dy/dt=-r(1-y/T)y$; $y=0$ is asymptotically stable, $y=T$ is unstable | p.107-108; formula |
| In the threshold model, what happens if $y_0<T$ vs $y_0>T$? | If $y_0<T$: $y\to0$ (extinction). If $y_0>T$: $y$ grows without bound, reaching a vertical asymptote at a finite time $t^{*}$ | p.108-109; discrimination |
| How does the threshold model relate algebraically to the logistic equation? | It is the logistic equation with $K$ replaced by $T$ and $r$ replaced by $-r$ | p.107; concept |

## Logistic Growth with a Threshold
| Front | Back | Notes |
| --- | --- | --- |
| Equation and equilibria (with stability) of the logistic-with-threshold model, $0<T<K$? | $dy/dt=-r(1-y/T)(1-y/K)y$; equilibria $y=0$ (stable), $y=T$ (unstable), $y=K$ (stable) | p.109-110; formula |
| What determines whether a population goes extinct or approaches the carrying capacity in this model? | Whether the initial population $y_0$ is below the threshold $T$ (extinction) or above it (approaches $K$) | p.110; discrimination |

## Bifurcation
| Front | Back | Notes |
| --- | --- | --- |
| Definition: bifurcation point of a parametrized family $dy/dt=f(a,y)$? | A parameter value $a$ at which critical points come together, separate, appear, or disappear as $a$ varies | p.115; definition |
| $dy/dt=a-y^2$: how many equilibria for $a<0$, $a=0$, $a>0$, and what is this bifurcation called? | 0 for $a<0$; 1 for $a=0$; 2 for $a>0$; a saddle-node bifurcation | p.115; formula |
| $dy/dt=ay-y^3$ has what type of bifurcation at $a=0$? | A pitchfork bifurcation (one equilibrium splits into three as $a$ crosses 0) | p.116; discrimination |
| $dy/dt=ay-y^2$ has a transcritical bifurcation at $a=0$. What changes there? | The number of equilibria stays the same ($y=0$ and $y=a$), but their stability swaps as $a$ passes through 0 | p.116; discrimination |

## Halibut Population (Logistic Growth Example)
| Front | Back | Notes |
| --- | --- | --- |
| Halibut: $r=0.71$/yr, $K=80.5\times10^6$ kg, $y_0=0.25K$. Find $y(2)/K$ and the time $\tau$ for $y=0.75K$. | $y(2)/K=\dfrac{0.25}{0.25+0.75e^{-1.42}}\approx0.580$, so $y(2)\approx46.7\times10^6$ kg; $\tau=\dfrac{\ln9}{0.71}\approx3.095$ years | p.106; procedure |

## Epidemic Spread Model
| Front | Back | Notes |
| --- | --- | --- |
| Fraction infectious $y$ satisfies $dy/dt=\alpha y(1-y)$, $y(0)=y_0\in(0,1)$. Find the equilibria, classify stability, and state $\lim_{t\to\infty}y(t)$. | Same form as logistic with $r=\alpha$, $K=1$: $y=0$ unstable, $y=1$ asymptotically stable; since $0<y_0<1$, $y(t)\to1$ | p.114; procedure |

## Schaefer Fishing Model
| Front | Back | Notes |
| --- | --- | --- |
| Schaefer model with constant effort $E<r$: $dy/dt=r(1-y/K)y-Ey$. Find the equilibria and the sustainable yield $Y(E)$ at the stable one. | Equilibria $y_1=0$ (unstable), $y_2=K(1-E/r)$ (stable); $Y=Ey_2=EK(1-E/r)$, maximized at $E=r/2$ giving $Y_m=rK/4$ | p.113; procedure |

# Node map
```json
[
 {
  "name": "Equilibrium Solution",
  "type": "concept",
  "existing": true,
  "parent": "Autonomous Equations and Population Dynamics",
  "prereqs": [],
  "uses": [],
  "page": 101,
  "summary": "A constant solution y = y1 of dy/dt = f(y) with f(y1) = 0; also called a critical point."
 },
 {
  "name": "Asymptotic Stability",
  "type": "concept",
  "existing": true,
  "parent": "Autonomous Equations and Population Dynamics",
  "prereqs": [
   "Equilibrium Solution"
  ],
  "uses": [],
  "page": 105,
  "summary": "An equilibrium that nearby solutions converge to as t goes to infinity; tested by f'(y1) < 0."
 },
 {
  "name": "Semistable Equilibrium",
  "type": "concept",
  "existing": false,
  "parent": "Autonomous Equations and Population Dynamics",
  "prereqs": [
   "Equilibrium Solution",
   "Asymptotic Stability"
  ],
  "uses": [],
  "page": 111,
  "summary": "An equilibrium approached from one side and departed from on the other."
 },
 {
  "name": "Logistic-Growth",
  "type": "concept",
  "existing": true,
  "parent": "Autonomous Equations and Population Dynamics",
  "prereqs": [
   "Equilibrium Solution",
   "Separable Equation"
  ],
  "uses": [],
  "page": 102,
  "summary": "dy/dt = r(1-y/K)y models growth limited by carrying capacity K; solutions approach K."
 },
 {
  "name": "Critical Threshold Model",
  "type": "concept",
  "existing": false,
  "parent": "Autonomous Equations and Population Dynamics",
  "prereqs": [
   "Logistic-Growth",
   "Asymptotic Stability"
  ],
  "uses": [],
  "page": 107,
  "summary": "dy/dt = -r(1-y/T)y: populations below threshold T die out, above it grow without bound in finite time."
 },
 {
  "name": "Logistic Growth with a Threshold",
  "type": "concept",
  "existing": false,
  "parent": "Autonomous Equations and Population Dynamics",
  "prereqs": [
   "Critical Threshold Model",
   "Logistic-Growth"
  ],
  "uses": [],
  "page": 109,
  "summary": "dy/dt = -r(1-y/T)(1-y/K)y with 0<T<K has three equilibria: 0 and K stable, T unstable."
 },
 {
  "name": "Bifurcation",
  "type": "concept",
  "existing": false,
  "parent": "Autonomous Equations and Population Dynamics",
  "prereqs": [
   "Equilibrium Solution",
   "Asymptotic Stability"
  ],
  "uses": [],
  "page": 115,
  "summary": "A parameter value where equilibria of dy/dt = f(a,y) appear, disappear, or change stability; saddle-node, pitchfork, and transcritical types."
 },
 {
  "name": "Halibut Population (Logistic Growth Example)",
  "type": "problem",
  "existing": false,
  "parent": "Autonomous Equations and Population Dynamics",
  "prereqs": [
   "Logistic-Growth"
  ],
  "uses": [
   "Logistic-Growth"
  ],
  "page": 106,
  "summary": "Numeric application of the logistic solution formula to a fish population."
 },
 {
  "name": "Epidemic Spread Model",
  "type": "problem",
  "existing": false,
  "parent": "Autonomous Equations and Population Dynamics",
  "prereqs": [
   "Logistic-Growth"
  ],
  "uses": [
   "Logistic-Growth",
   "Equilibrium Solution",
   "Asymptotic Stability"
  ],
  "page": 114,
  "summary": "Proportion infectious follows a logistic-shaped equation; disease eventually spreads through the whole population."
 },
 {
  "name": "Schaefer Fishing Model",
  "type": "problem",
  "existing": false,
  "parent": "Autonomous Equations and Population Dynamics",
  "prereqs": [
   "Logistic-Growth"
  ],
  "uses": [
   "Logistic-Growth",
   "Equilibrium Solution",
   "Asymptotic Stability"
  ],
  "page": 113,
  "summary": "Constant-effort harvesting added to the logistic equation; finds the maximum sustainable yield."
 }
]
```

# Frankenstein problems

**FP1.** A population obeys $dy/dt=0.4\left(1-\dfrac{y}{50}\right)\left(\dfrac{y}{10}-1\right)y$. (a) Rewrite this in the standard logistic-with-threshold form $dy/dt=-r(1-y/T)(1-y/K)y$ and identify $r,T,K$. (b) Find and classify all equilibria. (c) If $y_0=5$, what happens as $t\to\infty$? If $y_0=20$?

*Concepts tested:* Logistic Growth with a Threshold, Equilibrium Solution, Asymptotic Stability.

*Solution.* (a) $0.4(1-y/50)(y/10-1)y=-0.4(1-y/50)(1-y/10)y$, matching the standard form with $r=0.4$, $T=10$, $K=50$.

(b) Equilibria at $y=0,10,50$. For $0<y<10$: both factors $(1-y/50),(1-y/10)$ positive, so $f<0$ (since of the leading minus sign), meaning $y$ decreases toward 0: $y=0$ is asymptotically stable. For $10<y<50$: $(1-y/50)>0$, $(1-y/10)<0$, so $f>0$: $y$ increases away from 10 toward 50, making $y=10$ unstable. For $y>50$: both factors negative, product positive, so $f<0$: $y$ decreases back toward 50, so $y=50$ is asymptotically stable.

(c) $y_0=5$ is in $(0,10)$ where $y$ decreases, so $y\to0$ (extinction). $y_0=20$ is in $(10,50)$ where $y$ increases, so $y\to50$.

**FP2.** For the family $dy/dt=ay-y^2$ ($a$ a real parameter): (a) find the equilibria in terms of $a$. (b) Determine their stability for $a<0$ and $a>0$ using the derivative test. (c) Name the bifurcation at $a=0$ and describe what exchanges there. (d) If $a=3$ and $y_0=1$, does $y$ increase or decrease initially, and what does it approach as $t\to\infty$?

*Concepts tested:* Bifurcation, Equilibrium Solution, Asymptotic Stability.

*Solution.* (a) $f(y)=ay-y^2=y(a-y)$, so equilibria are $y=0$ and $y=a$.

(b) $f'(y)=a-2y$. At $y=0$: $f'(0)=a$. At $y=a$: $f'(a)=-a$. For $a<0$: $y=0$ is stable ($f'(0)=a<0$), $y=a$ is unstable ($f'(a)=-a>0$). For $a>0$: $y=0$ is unstable, $y=a$ is stable.

(c) This is a transcritical bifurcation at $a=0$: the number of equilibria (2) doesn't change, but the stability of $y=0$ and $y=a$ swaps as $a$ crosses 0.

(d) At $a=3$: $y=0$ is unstable, $y=3$ is stable. With $y_0=1$: $f(1)=3(1)-1^2=2>0$, so $y$ increases initially. Since $0<y_0<3$, $y$ increases and approaches the stable equilibrium $y=3$ as $t\to\infty$.
