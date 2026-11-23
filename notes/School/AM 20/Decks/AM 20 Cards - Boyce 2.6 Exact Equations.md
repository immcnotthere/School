---
type: reference
parent: "[[AM20]]"
domain: math
course: "AM 20"
status: draft
source: "Boyce 2.6 Exact Equations"
tags:
  - decks
---
# AM 20 Cards - Boyce 2.6 Exact Equations and Integrating Factors

## Exact Equation
| Front | Back | Notes |
| --- | --- | --- |
| Test for exactness of $M(x,y)+N(x,y)y'=0$? | Exact iff $M_y=N_x$ on a simply connected region | p.118; definition |
| If $M+Ny'=0$ is exact, what two conditions define $\psi(x,y)$, and how are solutions expressed? | $\psi_x=M$, $\psi_y=N$; solutions are given implicitly by $\psi(x,y)=c$ | p.117-118; definition |
| Procedure to find $\psi(x,y)$ for an exact equation $M+Ny'=0$? | Integrate $\psi_x=M$ with respect to $x$ (adding an unknown function $h(y)$ instead of a constant); differentiate with respect to $y$, set equal to $N$, and solve for $h(y)$ | p.120; procedure |
| Why must the exactness test's region be simply connected? | Theorem 2.6.1 (that $M_y=N_x$ guarantees an exact $\psi$ exists) only holds on regions with no holes, such as rectangles or disks, not an annulus | p.118 (footnote); concept |
| If $M+Ny'=0$ is not exact, what PDE must a general integrating factor $\mu(x,y)$ satisfy? | $M\mu_y-N\mu_x+(M_y-N_x)\mu=0$ | p.121; formula |
| Condition for $M+Ny'=0$ to have an integrating factor $\mu$ depending on $x$ only, and the ODE it satisfies? | If $(M_y-N_x)/N$ is a function of $x$ alone, then $\mu(x)$ satisfies the linear separable ODE $d\mu/dx=\dfrac{M_y-N_x}{N}\mu$ | p.121-122; procedure |
| Why can a non-exact equation have more than one valid integrating factor? | The PDE for $\mu$ can have multiple solutions; any one of them makes the equation exact and yields a (possibly differently expressed) implicit solution | p.122; concept |

## Exactness Check and Solve
| Front | Back | Notes |
| --- | --- | --- |
| Solve $2x+y^2+2xyy'=0$ by recognizing exactness. | $M=2x+y^2,N=2xy$; $M_y=2y=N_x$, exact. $\psi=x^2+xy^2+h(y)$; matching $\psi_y=N$ gives $h'(y)=0$. Solution: $x^2+xy^2=c$ | p.117; procedure |

## Non-exact to Integrating Factor Example
| Front | Back | Notes |
| --- | --- | --- |
| $(3xy+y^2)+(x^2+xy)y'=0$ is not exact. Find an integrating factor $\mu(x)$ and solve. | $(M_y-N_x)/N=(3x+2y-2x-y)/(x^2+xy)=1/x$, so $\mu=x$. The exact equation $(3x^2y+xy^2)+(x^3+x^2y)y'=0$ has solution $x^3y+\tfrac12x^2y^2=c$ | p.120-122; procedure |

# Node map
```json
[
 {
  "name": "Exact Equation",
  "type": "concept",
  "existing": false,
  "parent": "Exact Equations and Integrating Factors",
  "prereqs": [
   "Separable Equation"
  ],
  "uses": [],
  "page": 117,
  "summary": "M(x,y) + N(x,y)y' = 0 is exact when M_y = N_x; then a function psi with psi_x = M, psi_y = N gives solutions implicitly as psi(x,y) = c."
 },
 {
  "name": "Integrating-Factor",
  "type": "concept",
  "existing": true,
  "parent": "Exact Equations and Integrating Factors",
  "prereqs": [
   "Exact Equation",
   "Separable Equation"
  ],
  "uses": [],
  "page": 121,
  "summary": "A function mu(x,y) that, when multiplied through a non-exact equation, makes it exact; mu(x) alone works when (M_y - N_x)/N depends only on x."
 },
 {
  "name": "Exactness Check and Solve",
  "type": "problem",
  "existing": false,
  "parent": "Exact Equations and Integrating Factors",
  "prereqs": [
   "Exact Equation"
  ],
  "uses": [
   "Exact Equation"
  ],
  "page": 117,
  "summary": "Worked example verifying exactness and solving by integrating M then matching N."
 },
 {
  "name": "Non-exact to Integrating Factor Example",
  "type": "problem",
  "existing": false,
  "parent": "Exact Equations and Integrating Factors",
  "prereqs": [
   "Exact Equation",
   "Integrating-Factor"
  ],
  "uses": [
   "Exact Equation",
   "Integrating-Factor"
  ],
  "page": 120,
  "summary": "An equation that fails the exactness test is fixed with an x-only integrating factor and then solved."
 }
]
```

# Frankenstein problems

**FP1.** Consider $y+(2xy-e^{-2y})y'=0$, i.e. $M=y$, $N=2xy-e^{-2y}$. (a) Show the equation is not exact. (b) Show that $\mu(y)=e^{2y}/y$ is an integrating factor. (c) Solve the resulting exact equation.

*Concepts tested:* Exact Equation, Integrating-Factor, Separable Equation.

*Solution.* (a) $M_y=1$, $N_x=2y$; since $M_y\neq N_x$ in general, the equation is not exact.

(b) For an integrating factor depending on $y$ only, setting $\mu_x=0$ in $M\mu_y-N\mu_x+(M_y-N_x)\mu=0$ gives $M\mu_y=(N_x-M_y)\mu$, i.e. $\dfrac{d\mu}{\mu}=\dfrac{N_x-M_y}{M}\,dy=\dfrac{2y-1}{y}\,dy=\left(2-\dfrac1y\right)dy$. This is separable and integrates to $\ln\mu=2y-\ln y$, so $\mu(y)=e^{2y}/y$.

Multiplying: $M^{*}=y\cdot\dfrac{e^{2y}}{y}=e^{2y}$, and $N^{*}=(2xy-e^{-2y})\cdot\dfrac{e^{2y}}{y}=2xe^{2y}-\dfrac1y$. Check: $M^{*}_y=2e^{2y}=N^{*}_x$. Exact confirmed.

(c) $\psi_x=M^{*}=e^{2y}\Rightarrow\psi=xe^{2y}+h(y)$. Then $\psi_y=2xe^{2y}+h'(y)=N^{*}=2xe^{2y}-1/y\Rightarrow h'(y)=-1/y\Rightarrow h(y)=-\ln y$. Solution: $xe^{2y}-\ln y=c$.

**FP2.** Consider $(3x^2y+2xy+y^3)+(x^2+y^2)y'=0$. (a) Check exactness. (b) If not exact, find an integrating factor. (c) Solve the equation.

*Concepts tested:* Exact Equation, Integrating-Factor, General Solution.

*Solution.* (a) $M_y=3x^2+2x+3y^2$, $N_x=2x$; $M_y\neq N_x$, not exact.

(b) $(M_y-N_x)/N=(3x^2+2x+3y^2-2x)/(x^2+y^2)=3(x^2+y^2)/(x^2+y^2)=3$, a constant (so trivially a function of $x$ alone). Then $d\mu/dx=3\mu\Rightarrow\mu=e^{3x}$.

(c) Multiplying: $M^{*}=e^{3x}(3x^2y+2xy+y^3)$, $N^{*}=e^{3x}(x^2+y^2)$. It's simpler to integrate the smaller expression $\psi_y=N^{*}$ first: $\psi=e^{3x}\left(x^2y+\dfrac{y^3}{3}\right)+g(x)$. Then $\psi_x=3e^{3x}\left(x^2y+\dfrac{y^3}{3}\right)+e^{3x}(2xy)+g'(x)=e^{3x}(3x^2y+y^3+2xy)+g'(x)$, which matches $M^{*}=e^{3x}(3x^2y+2xy+y^3)$ when $g'(x)=0$. General solution: $e^{3x}\left(x^2y+\dfrac{y^3}{3}\right)=c$, equivalently $e^{3x}(3x^2y+y^3)=C$.
