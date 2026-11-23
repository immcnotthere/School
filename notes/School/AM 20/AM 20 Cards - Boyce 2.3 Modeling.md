---
type: reference
parent: "[[AM20]]"
domain: math
course: "AM 20"
status: draft
source: "Boyce 2.3 Modeling"
tags:
  - decks
---
# AM 20 Cards - Boyce 2.3 Modeling First-Order Equations

## Rate Balance (Inflow Minus Outflow)
| Front | Back | Notes |
| --- | --- | --- |
| Tank mixing: salt enters at concentration $c_{in}$ lb/gal and flow rate $r$ gal/min. What is the rate salt enters? | $c_{in}\cdot r$ lb/min | p.74; formula |
| Yes or no, and why: if the tank volume stays constant at $V$, is well-stirred, holds $Q(t)$ lb of salt, and drains at $r$ gal/min, what is rate out? | $\dfrac{rQ(t)}{V}$ lb/min | p.74; formula |
| Why does rate out use $Q(t)/V$ instead of the initial concentration $Q_0/V$? | Because the tank is well-stirred, the concentration is uniform but changes over time; the current concentration is $Q(t)/V$ | p.74; discrimination |

## Compound Interest
| Front | Back | Notes |
| --- | --- | --- |
| ODE for value $S(t)$ of an investment with continuously compounded rate of return $r$, no deposits? | $dS/dt = rS$ | p.77; formula |
| Solution of $dS/dt=rS$, $S(0)=S_0$? | $S(t)=S_0e^{rt}$ | p.77; formula |
| ODE for $S(t)$ with continuous rate of return $r$ and continuous deposit or withdrawal rate $k$? | $dS/dt = rS+k$ | p.78; formula |
| In $dS/dt=rS+k$, what does a negative $k$ represent? | A continuous withdrawal instead of a deposit | p.78; discrimination |

## Escape Velocity
| Front | Back | Notes |
| --- | --- | --- |
| Formula for escape velocity $v_e$ from Earth's surface, in terms of $g$ and radius $R$? | $v_e=\sqrt{2gR}$ | p.82; formula |
| Gravitational force (weight) on a body at height $x$ above Earth's surface, mass $m$, surface gravity $g$, radius $R$? | $w(x)=-\dfrac{mgR^2}{(R+x)^2}$ | p.81; formula |
| How is escape velocity derived from the maximum-altitude formula $\xi=\dfrac{v_0^2R}{2gR-v_0^2}$? | Let $\xi\to\infty$: the denominator $2gR-v_0^2\to0$, so $v_0\to\sqrt{2gR}=v_e$ | p.82; procedure |
| Numerically, about how fast is Earth's escape velocity? | About 6.9 mi/s (11.1 km/s) | p.82; definition |

## Velocity Chain Rule Substitution
| Front | Back | Notes |
| --- | --- | --- |
| Chain-rule identity rewriting $dv/dt$ in terms of $x$ instead of $t$ (using $dx/dt=v$)? | $\dfrac{dv}{dt}=v\dfrac{dv}{dx}$ | p.80; formula |
| When should you use $v\,dv/dx$ instead of $dv/dt$ for an equation of motion? | When the force or acceleration is given as a function of position $x$ rather than time $t$, so eliminating $t$ makes the equation separable in $v,x$ | p.80; discrimination |

## Torricelli's Law
| Front | Back | Notes |
| --- | --- | --- |
| Torricelli's principle: outflow velocity $v$ from a hole at depth $h$ below the liquid surface? | $v=\sqrt{2gh}$ | p.83; formula |
| ODE for the height $h(t)$ of liquid draining from a tank with cross-section area $A(h)$, hole area $a$, contraction coefficient $\alpha$? | $A(h)\dfrac{dh}{dt}=-\alpha a\sqrt{2gh}$ | p.83; formula |

## IRA Continuous Investment Problem
| Front | Back | Notes |
| --- | --- | --- |
| IRA starting at \$0, continuous deposits $k=\$2000$/yr, rate of return $r=8\%$. Find the balance $S(40)$. | $S(t)=S_0e^{rt}+\dfrac{k}{r}(e^{rt}-1)$; with $S_0=0$: $S(40)=\dfrac{2000}{0.08}(e^{3.2}-1)\approx\$588{,}313$ | p.78; procedure |

## Chemicals in a Pond
| Front | Back | Notes |
| --- | --- | --- |
| Pond of $10^7$ gal, inflow/outflow both $5\times10^6$ gal/yr, incoming concentration $2+\sin2t$ g/gal, $Q(0)=0$. Set up the ODE for $q(t)=Q(t)/10^6$ and give its solution form. | $dq/dt+q/2=10+5\sin2t$; solution $q(t)=20-\dfrac{40}{17}\cos2t+\dfrac{10}{17}\sin2t+Ce^{-t/2}$, with $C=-300/17$ from $q(0)=0$ | p.79-80; procedure |

## Coffee Cooling Problem
| Front | Back | Notes |
| --- | --- | --- |
| Coffee at 200F cools to 190F in 1 min in a 70F room. Find $k$, then when it reaches 150F. | $u=70+130e^{-kt}$; $u(1)=190\Rightarrow k=\ln(130/120)\approx0.080$; solving $70+130e^{-kt}=150$ gives $t=\ln(130/80)/k\approx6.07$ min | p.85 (Problem 16); procedure |

## Brachistochrone Problem
| Front | Back | Notes |
| --- | --- | --- |
| Brachistochrone: $(1+y'^2)y=k^2$. What substitution and result give the parametric cycloid solution? | Let $y=k^2\sin^2t$; separating variables gives $2k^2\sin^2t\,dt=dx$. With $\theta=2t$, integrating gives $x=k^2(\theta-\sin\theta)/2$, $y=k^2(1-\cos\theta)/2$: a cycloid | p.89-90; procedure |

## Steady State Solution
| Front | Back | Notes |
| --- | --- | --- |
| If surroundings temperature varies, e.g. $T(t)=T_0+T_1\cos\omega t$, what are the transient and steady-state parts of the solution? | The transient part decays to zero as $t\to\infty$; the remaining oscillatory part is the steady state $S(t)$ | p.85; discrimination |

# Node map
```json
[
 {
  "name": "Rate Balance (Inflow Minus Outflow)",
  "type": "concept",
  "existing": true,
  "parent": "Modeling with First-Order Equations",
  "prereqs": [],
  "uses": [],
  "page": 74,
  "summary": "For a quantity Q(t) accumulating with flow in and flow out, dQ/dt = (rate in) - (rate out); each rate is typically a concentration or per-unit rate times a flow rate."
 },
 {
  "name": "Compound Interest",
  "type": "concept",
  "existing": true,
  "parent": "Growth and Decay Models",
  "prereqs": [
   "Separable Equation",
   "Integrating-Factor"
  ],
  "uses": [],
  "page": 77,
  "summary": "Continuously compounded investment value S(t) satisfies dS/dt = rS (S = S_0 e^{rt}); with continuous deposits or withdrawals at rate k, dS/dt = rS + k."
 },
 {
  "name": "Escape Velocity",
  "type": "concept",
  "existing": false,
  "parent": "Modeling with First-Order Equations",
  "prereqs": [
   "Velocity Chain Rule Substitution",
   "Separable Equation"
  ],
  "uses": [],
  "page": 82,
  "summary": "The minimum initial velocity for a body launched from Earth's surface to never fall back is v_e = sqrt(2gR)."
 },
 {
  "name": "Velocity Chain Rule Substitution",
  "type": "concept",
  "existing": false,
  "parent": "Modeling with First-Order Equations",
  "prereqs": [
   "Chain Rule"
  ],
  "uses": [],
  "page": 80,
  "summary": "When force depends on position x rather than time t, eliminate t using dv/dt = v dv/dx, giving a separable ODE in v and x."
 },
 {
  "name": "Torricelli's Law",
  "type": "concept",
  "existing": false,
  "parent": "Modeling with First-Order Equations",
  "prereqs": [],
  "uses": [],
  "page": 83,
  "summary": "Outflow velocity from a draining tank's hole at depth h below the surface is v = sqrt(2gh)."
 },
 {
  "name": "Newton's Law of Cooling",
  "type": "concept",
  "existing": true,
  "parent": "Growth and Decay Models",
  "prereqs": [
   "Separable Equation"
  ],
  "uses": [],
  "page": 85,
  "summary": "Temperature changes at a rate proportional to the difference from ambient temperature: du/dt = -k(u-T)."
 },
 {
  "name": "Salt Tank Mixing Problem",
  "type": "problem",
  "existing": false,
  "parent": "Modeling with First-Order Equations",
  "prereqs": [
   "Rate Balance (Inflow Minus Outflow)",
   "Integrating-Factor"
  ],
  "uses": [
   "Rate Balance (Inflow Minus Outflow)",
   "Integrating-Factor",
   "Separable Equation"
  ],
  "page": 75,
  "summary": "Classic tank-mixing IVP solved by writing the balance law as a linear ODE and applying an integrating factor."
 },
 {
  "name": "IRA Continuous Investment Problem",
  "type": "problem",
  "existing": false,
  "parent": "Growth and Decay Models",
  "prereqs": [
   "Compound Interest"
  ],
  "uses": [
   "Compound Interest",
   "Integrating-Factor"
  ],
  "page": 78,
  "summary": "Applies the continuous-deposit compound interest formula to compute a 40-year IRA balance."
 },
 {
  "name": "Chemicals in a Pond",
  "type": "problem",
  "existing": false,
  "parent": "Modeling with First-Order Equations",
  "prereqs": [
   "Rate Balance (Inflow Minus Outflow)",
   "Integrating-Factor"
  ],
  "uses": [
   "Rate Balance (Inflow Minus Outflow)",
   "Integrating-Factor"
  ],
  "page": 79,
  "summary": "Rate-balance model with a periodically varying inflow concentration, solved with an integrating factor."
 },
 {
  "name": "Coffee Cooling Problem",
  "type": "problem",
  "existing": false,
  "parent": "Growth and Decay Models",
  "prereqs": [
   "Newton's Law of Cooling"
  ],
  "uses": [
   "Newton's Law of Cooling"
  ],
  "page": 85,
  "summary": "Uses Newton's Law of Cooling to find the cooling constant and the time to reach a target temperature."
 },
 {
  "name": "Brachistochrone Problem",
  "type": "problem",
  "existing": false,
  "parent": "Modeling with First-Order Equations",
  "prereqs": [
   "Separable Equation",
   "U Substitution"
  ],
  "uses": [
   "Separable Equation",
   "U Substitution"
  ],
  "page": 89,
  "summary": "The classic minimum-time-descent problem; solved by substitution to yield a cycloid in parametric form."
 },
 {
  "name": "Steady State Solution",
  "type": "concept",
  "existing": true,
  "parent": "",
  "prereqs": [],
  "summary": ""
 }
]
```

# Frankenstein problems

**FP1.** A 200-gal tank initially contains 300 lb of salt. Brine containing 2 lb/gal enters at 3 gal/min and the well-stirred mixture drains at the same rate. Simultaneously the tank's surrounding air temperature obeys Newton's Law of Cooling, $du/dt=-0.1(u-60)$, $u(0)=90$. Find $Q(t)$ and $u(t)$, and determine which quantity reaches 90% of its way to its limiting value first.

*Concepts tested:* Rate Balance (Inflow Minus Outflow), Integrating-Factor, Newton's Law of Cooling.

*Solution.* Salt balance: $dQ/dt = 2(3) - \dfrac{3Q}{200} = 6-\dfrac{3Q}{200}$, i.e. $dQ/dt+\dfrac{3}{200}Q=6$. Integrating factor $\mu=e^{3t/200}$ gives $Q(t)=400+(300-400)e^{-3t/200}=400-100e^{-3t/200}$, with limiting value $Q_L=400$. Reaching 90% of the way there means $Q=360$: $400-100e^{-3t/200}=360\Rightarrow e^{-3t/200}=0.4\Rightarrow t=-\dfrac{200}{3}\ln(0.4)\approx61.1$ min.

Temperature: $u(t)=60+30e^{-0.1t}$, limiting value 60. Reaching 90% of the way there means $u-60=0.1(90-60)=3$: $30e^{-0.1t}=3\Rightarrow e^{-0.1t}=0.1\Rightarrow t=10\ln10\approx23.0$ min.

The temperature reaches 90% of its approach to equilibrium first ($t\approx23.0$ min $<61.1$ min).

**FP2.** A body of mass $m$ is projected straight up from Earth's surface with initial velocity $v_0=0.9v_e$ (90% of escape velocity), no air resistance. (a) Using $dv/dt=v\,dv/dx$, find $v^2$ as a function of altitude $x$. (b) Find the maximum altitude $\xi$ reached, in terms of $R$. (c) Suppose a cylindrical tank of cross-section $A=1\,\mathrm{m}^2$ and hole area $a=0.01\,\mathrm{m}^2$ ($\alpha=1$) starts full of water at height $\xi$ (from part b, treated as a length in meters). How long does it take to drain to $h=\xi/4$?

*Concepts tested:* Escape Velocity, Velocity Chain Rule Substitution, Torricelli's Law.

*Solution.* (a) $v\,dv/dx=-gR^2/(R+x)^2$. Integrating: $v^2/2=gR^2/(R+x)+c$; at $x=0$, $v=v_0$ gives $c=v_0^2/2-gR$, so $v^2=v_0^2-2gR+\dfrac{2gR^2}{R+x}$.

(b) At maximum altitude $v=0$, $x=\xi$: $0=v_0^2-2gR+\dfrac{2gR^2}{R+\xi}\Rightarrow \xi=\dfrac{Rv_0^2}{2gR-v_0^2}$. Since $v_0=0.9v_e$ and $v_e^2=2gR$, $v_0^2=1.62gR$, so $2gR-v_0^2=0.38gR$ and $\xi=R\cdot\dfrac{1.62gR}{0.38gR}=\dfrac{1.62}{0.38}R\approx4.26R$.

(c) Torricelli: $A\,dh/dt=-\alpha a\sqrt{2gh}$, i.e. $dh/dt=-0.01\sqrt{2gh}$. Separating: $h^{-1/2}dh=-0.01\sqrt{2g}\,dt$, so $2\sqrt{h}=-0.01\sqrt{2g}\,t+2\sqrt{\xi}$. At $h=\xi/4$, $2\sqrt{h}=\sqrt{\xi}$, giving $\sqrt{\xi}-2\sqrt{\xi}=-0.01\sqrt{2g}\,t\Rightarrow t=\dfrac{\sqrt{\xi}}{0.01\sqrt{2g}}=100\sqrt{\dfrac{\xi}{2g}}\approx100\sqrt{\dfrac{2.13R}{g}}$.
