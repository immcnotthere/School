---
type: reference
parent: "[[AM20]]"
domain: math
course: "AM 20"
status: draft
source: "Boyce 2.2 Separable Equations"
tags:
  - decks
---
# AM 20 Cards - Boyce 2.2 Separable Equations

## Separable Equation
| Front | Back | Notes |
| --- | --- | --- |
| Why does integrating $M(x)\,dx$ and $N(y)\,dy$ separately give a valid solution? | By the chain rule, $H_2'(y)\,dy/dx = \dfrac{d}{dx}H_2(y)$, so the original equation becomes $\dfrac{d}{dx}[H_1(x)+H_2(y)]=0$; integrating both sides gives $H_1(x)+H_2(y)=c$. | p.66; definition |
| For a separable IVP $M(x)\,dx+N(y)\,dy=0$, $y(x_0)=y_0$, how do you find $c$? | Substitute $x_0$ and $y_0$ into $H_1(x)+H_2(y)=c$ and solve: $c = H_1(x_0)+H_2(y_0)$. | p.67; procedure |

## Interval of Validity (Separable Equation)
| Front | Back | Notes |
| --- | --- | --- |
| For an implicitly-defined solution of a separable equation, where does the interval of validity typically end? | At a point where the integral curve has a vertical tangent, i.e. where $dy/dx$ is undefined because its denominator (the "$y$-side" expression) is zero. | p.67-69; definition |
| In $y' = (4x-x^3)/(4+y^3)$ with solution through $(0,1)$ implicit as $y^4+16y+x^4-8x^2=17$, how is the interval of validity found? | Find where $4+y^3=0$ (vertical tangent), giving $y=(-4)^{1/3}\approx -1.5874$; substitute back into the implicit equation to get the corresponding $x \approx \pm 3.3488$, which bound the interval. | p.68-69; procedure |

## Implicit Solutions
| Front | Back | Notes |
| --- | --- | --- |
| When must a separable equation's solution be left implicit rather than solved explicitly? | When the resulting equation cannot be algebraically solved for $y$ in terms of $x$ (e.g. a quartic in $y$, as in $y^4+16y+x^4-8x^2=c$). | p.68-69; discrimination |

## explicit solution
| Front | Back | Notes |
| --- | --- | --- |
| What is an explicit solution of a differential equation? | A solution written directly as $y=\varphi(x)$, with $y$ isolated as a function of $x$. | p.67; definition |
| In $y^2-2y=x^3+2x^2+2x+3$ with $y(0)=-1$, how is the explicit solution obtained and which branch is correct? | Solve the quadratic in $y$: $y=1\pm\sqrt{x^3+2x^2+2x+4}$; since $y(0)=-1$, the minus branch is correct: $y=1-\sqrt{x^3+2x^2+2x+4}$. | p.67; procedure |

## Homogeneous Equation (First Order)
| Front | Back | Notes |
| --- | --- | --- |
| When is a first order equation $dy/dx=f(x,y)$ called homogeneous (in this section's sense)? | When the right side depends only on the ratio $y/x$, i.e. $dy/dx = f(y/x)$. Note: this is a different meaning of "homogeneous" from homogeneous linear systems. | p.71-72; definition |
| What substitution reduces a homogeneous equation to a separable one, and what does it give for $dy/dx$? | Let $v=y/x$ (so $y=xv$); then $dy/dx = v + x\,dv/dx$, and substituting turns the equation into a separable equation in $v$ and $x$. | p.72; procedure |
| After solving the separable equation in $v$, how do you get back the solution in $x$ and $y$? | Replace $v$ by $y/x$ in the solution for $v(x)$. | p.72; procedure |

## Equilibrium Solution
| Front | Back | Notes |
| --- | --- | --- |
| For $dy/dx=f(x,y)$, how do you find a constant solution $y=y_0$ directly, without separating variables? | Find a value $y_0$ such that $f(x,y_0)=0$ for all $x$; then the constant function $y=y_0$ is automatically a solution. | p.69; procedure |

## Homogeneous Equation via Substitution
| Front | Back | Notes |
| --- | --- | --- |
| Solve $dy/dx=(y-4x)/(x-y)$ using $v=y/x$. What separable equation in $v$ results? | Substituting $y=xv$: $x\,dv/dx = (v^2-4)/(1-v)$, which is separable in $v$ and $x$. | p.72; key move |

# Node map
```json
[
 {
  "name": "Separable Equation",
  "type": "concept",
  "existing": true,
  "parent": "Differential Equation",
  "prereqs": [
   "U Substitution"
  ],
  "uses": [],
  "page": 64,
  "summary": "A first order equation $M(x)+N(y)y'=0$, solved by integrating each side separately to get $H_1(x)+H_2(y)=c$."
 },
 {
  "name": "Interval of Validity (Separable Equation)",
  "type": "concept",
  "existing": true,
  "parent": "Separable Equation",
  "prereqs": [
   "Separable Equation"
  ],
  "uses": [],
  "page": 67,
  "summary": "The domain over which an implicit solution stays differentiable, bounded by points of vertical tangent."
 },
 {
  "name": "Implicit Solutions",
  "type": "concept",
  "existing": true,
  "parent": "Separable Equation",
  "prereqs": [
   "Separable Equation"
  ],
  "uses": [],
  "page": 66,
  "summary": "A solution left as $H_1(x)+H_2(y)=c$ because $y$ cannot be isolated algebraically."
 },
 {
  "name": "explicit solution",
  "type": "concept",
  "existing": true,
  "parent": "Separable Equation",
  "prereqs": [
   "Separable Equation"
  ],
  "uses": [],
  "page": 67,
  "summary": "A solution written directly as $y=\\varphi(x)$, chosen from possible branches using the initial condition."
 },
 {
  "name": "Homogeneous Equation (First Order)",
  "type": "concept",
  "existing": false,
  "parent": "Separable Equation",
  "prereqs": [
   "Separable Equation"
  ],
  "uses": [],
  "page": 71,
  "summary": "$dy/dx=f(y/x)$; the substitution $y=xv$ reduces it to a separable equation in $v$ and $x$."
 },
 {
  "name": "Equilibrium Solution",
  "type": "concept",
  "existing": true,
  "parent": "Differential Equation",
  "prereqs": [],
  "uses": [],
  "page": 69,
  "summary": "For $dy/dx=f(x,y)$, a constant solution $y=y_0$ found by solving $f(x,y_0)=0$."
 },
 {
  "name": "Implicit IVP with Quadratic Branch",
  "type": "problem",
  "existing": false,
  "parent": "Separable Equation",
  "prereqs": [
   "Separable Equation"
  ],
  "uses": [
   "Separable Equation",
   "explicit solution",
   "Interval of Validity (Separable Equation)"
  ],
  "page": 67,
  "summary": "$y'=(3x^2+4x+2)/(2(y-1))$, $y(0)=-1$, solved explicitly with correct branch, valid for $x>-2$."
 },
 {
  "name": "Homogeneous Equation via Substitution",
  "type": "problem",
  "existing": false,
  "parent": "Separable Equation",
  "prereqs": [
   "Separable Equation"
  ],
  "uses": [
   "Homogeneous Equation (First Order)",
   "Separable Equation"
  ],
  "page": 72,
  "summary": "$dy/dx=(y-4x)/(x-y)$ reduced via $v=y/x$ to a separable equation in $v$."
 }
]
```

# Frankenstein problems

**FP1: Separable IVP with an all-reals interval of validity**
Solve $dy/dx = x/(y-1)$, $y(0) = 3$. Find the explicit solution, state whether it is explicit or implicit, and find its interval of validity.

**Solution.** Separate: $(y-1)\,dy = x\,dx$. Integrate: $\dfrac{y^2}{2} - y = \dfrac{x^2}{2} + c$. Apply $y(0)=3$: $\dfrac{9}{2}-3=\dfrac{3}{2}=c$.
Multiply by 2: $y^2 - 2y = x^2 + 3 \Rightarrow y^2-2y-(x^2+3)=0$.
Quadratic formula: $y = 1 \pm \sqrt{1+x^2+3} = 1\pm\sqrt{x^2+4}$.
Since $y(0)=3$ requires $1+\sqrt{4}=3$, take the plus branch: $y = 1+\sqrt{x^2+4}$, an explicit solution.
Since $x^2+4>0$ for every real $x$, there is no vertical tangent anywhere, so the interval of validity is all real $x$.
Concepts tested: Separable Equation, explicit solution, Interval of Validity (Separable Equation).

**FP2: Homogeneous equation reduced and solved explicitly**
Solve $dy/dx = (x^2+y^2)/(xy)$, $y(1) = 2$, and give an explicit formula for $y$.

**Solution.** The right side depends only on $y/x$: $(x^2+y^2)/(xy) = x/y + y/x$. Let $v=y/x$, so $y=xv$ and $dy/dx = v+x\,dv/dx$. In terms of $v$: right side is $1/v+v$, so
$v + x\,dv/dx = v + 1/v \Rightarrow x\,dv/dx = 1/v \Rightarrow v\,dv = dx/x$.
Integrate: $v^2/2 = \ln|x| + c \Rightarrow v^2 = 2\ln|x|+2c$.
Replace $v=y/x$: $y^2 = x^2(2\ln|x|+2c)$. Apply $y(1)=2$: $4 = 1\cdot(0+2c) \Rightarrow c=2$.
So $y^2 = x^2(2\ln|x|+4)$, and taking the positive branch (matching $y(1)=2>0$) for $x>0$:
$y = x\sqrt{2\ln x + 4}$. Check: at $x=1$, $y=1\cdot\sqrt{0+4}=2$. Correct.
Concepts tested: Homogeneous Equation (First Order), Separable Equation, explicit solution.
