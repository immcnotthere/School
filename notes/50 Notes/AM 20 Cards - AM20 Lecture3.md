---
type: reference
parent: "[[AM20]]"
domain: math
course: "AM 20"
status: draft
source: "AM20 Lecture3"
tags:
  - decks
---
# AM 20 Cards - AM20 Lecture3 Integrating Factors

## Canonical Form of a First-Order Linear ODE
| Front | Back | Notes |
| --- | --- | --- |
| What is the canonical form of a first-order linear ODE? | $y' + p(t)y = g(t)$, where $p(t)$ and $g(t)$ are given functions of $t$ | p.1; definition |
| Why is $y' + p(t)y = g(t)$ called linear? | $y$ and $y'$ each appear to the first power, and neither appears inside another function | p.1; concept |
| If the $y'$ term in a first-order ODE has a nonconstant coefficient, what must you do before applying the integrating-factor method? | Divide the whole equation through by that coefficient to put it in canonical form $y' + p(t)y = g(t)$ | p.1, 5; procedure |

## Integrating-Factor
| Front | Back | Notes |
| --- | --- | --- |
| What is the formula for the integrating factor $\mu(t)$ of $y' + p(t)y = g(t)$? | $\mu(t) = e^{\int p(t)\,dt}$ | p.2; formula |
| Once $\mu(t) = e^{\int p(t)dt}$ is known, what is the general solution formula for $y' + p(t)y = g(t)$? | $y(t) = \dfrac{1}{\mu(t)}\left(\int g(t)\mu(t)\,dt + c\right)$ | p.3; formula |
| After multiplying $y' + p(t)y = g(t)$ by $\mu(t) = e^{\int p(t)dt}$, what does the left side become? | $\dfrac{d}{dt}\big(\mu(t)y\big) = g(t)\mu(t)$, the derivative of a single product | p.3; procedure |
| Once the equation is written as $\frac{d}{dt}(\mu(t)y) = g(t)\mu(t)$, what operation makes progress: integrating or differentiating both sides? | Integrating; differentiating would undo the work and return the equation to its previous form | p.3; concept |

## Constant-Coefficient Linear ODE General Solution
| Front | Back | Notes |
| --- | --- | --- |
| What is the general solution of $y' + ay = b$ for constants $a \neq 0$ and $b$? | $y(t) = \dfrac{b}{a} + ce^{-at}$ | p.2; formula |
| For $y' + ay = b$ with $a$ constant, what is the integrating factor $\mu(t)$? | $\mu(t) = e^{at}$ | p.2; formula |

## Interval of Validity (First-Order Linear ODE)
| Front | Back | Notes |
| --- | --- | --- |
| How do you find the interval of validity for the solution of a first-order linear IVP? | Take the largest interval that contains the initial point on which $p(t)$ and $g(t)$ are defined, avoiding any points excluded by a division used to reach canonical form | p.5, 6; procedure |
| In $y(x) = x^2 + \frac{1}{x^2}$, solving $xy' + 2y = 4x^2,\ y(1) = 2$, why is $x = 0$ excluded even though nothing in the answer looks undefined there at first glance? | Reaching canonical form required dividing by $x$, which is invalid at $x = 0$, and the solution itself is also undefined there | p.5; discrimination |

## IVP with Constant Coefficient and Exponential Forcing
| Front | Back | Notes |
| --- | --- | --- |
| Example 1: solve $y' + \frac12 y = \frac12 e^{t/3}$ with $y(0) = 1$. What is the key move after multiplying by $\mu(t) = e^{t/2}$? | Add the exponents, $\frac13 + \frac12 = \frac56$, giving $\frac{d}{dt}(e^{t/2}y) = \frac12 e^{5t/6}$; integrating and dividing by $\mu$ gives $y(t) = \frac35 e^{t/3} + ce^{-t/2}$, and $y(0)=1$ gives $c = \frac25$ | p.3; problem |

## IVP with Constant Coefficient and Polynomial Forcing
| Front | Back | Notes |
| --- | --- | --- |
| Example 2: solve $y' - 2y = 4 - x$, $y(0) = -\frac74$, then describe the general solution as $x \to \infty$. What is the key move for integrating the right side $(4-x)e^{-2x}$? | Split it into $\int 4e^{-2x}dx = -2e^{-2x}$ and integrate $(-x)e^{-2x}$ by parts, giving $y(x) = -\frac74 + \frac{x}{2} + ce^{2x}$ with $c=0$ for the IVP; in the general solution the term $ce^{2x}$ eventually dominates the linear term, so $y \to \infty$ if $c>0$ and $y \to -\infty$ if $c<0$ | p.4; problem |

## IVP with Variable Coefficient after Dividing by x
| Front | Back | Notes |
| --- | --- | --- |
| Example 3: solve $xy' + 2y = 4x^2$, $y(1)=2$, and find the interval of validity. What is the key move to get $\mu(x)$ after dividing by $x$ to get $p(x) = 2/x$? | $\mu(x) = e^{\int (2/x)dx} = e^{2\ln\vert x\vert } = x^2$; then $x^2y = x^4+c$ gives $y(x) = x^2 + c/x^2$, and $y(1)=2$ gives $c=1$; the interval of validity is $(0,\infty)$ | p.5; problem |

## Direct Product Rule and IVP for a Simple Linear ODE
| Front | Back | Notes |
| --- | --- | --- |
| Examples 4-5: find the general solution of $ty' + y = 0$, then solve it with $y(1)=3$. What is the key shortcut? | The left side is already $\frac{d}{dt}(ty) = ty'+y$, so the equation is $\frac{d}{dt}(ty)=0$ directly, giving $y = c/t$; with $y(1)=3$, $c=3$, so $y(t) = 3/t$ on $(0,\infty)$ | p.5, 6; problem |

## IVP with Trigonometric Coefficient and Interval of Validity
| Front | Back | Notes |
| --- | --- | --- |
| Example 6: solve $y' + (\cot x)y = x\csc x$ with $y(\pi/2)=1$. What is the key move to find $\mu(x)$, and what interval of validity results? | Substitute $u = \sin x$ so $\int \cot x\,dx = \ln\vert \sin x\vert $, giving $\mu(x) = \sin x$; then $y\sin x = \frac{x^2}{2}+c$, so $y(x) = \frac{x^2}{2\sin x} + \frac{c}{\sin x}$; with $y(\pi/2)=1$, $c = 1-\pi^2/8$, and the interval of validity is $(0,\pi)$ | p.6, 7; problem |
# Node map
```json
[
 {
  "name": "Canonical Form of a First-Order Linear ODE",
  "type": "concept",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [],
  "uses": [],
  "page": 1,
  "summary": "The standard form $y'+p(t)y=g(t)$ for a first-order linear ODE, required before applying the integrating-factor method."
 },
 {
  "name": "Integrating-Factor",
  "type": "concept",
  "existing": true,
  "parent": "1st Order ODE",
  "prereqs": [
   "Canonical Form of a First-Order Linear ODE",
   "Natural logarithm"
  ],
  "uses": [],
  "page": "2-3",
  "summary": "A function $\\mu(t)=e^{\\int p(t)dt}$ that turns $y'+p(t)y=g(t)$ into the derivative of a single product $\\mu(t)y$, so the equation can be solved by integrating once."
 },
 {
  "name": "Constant-Coefficient Linear ODE General Solution",
  "type": "concept",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [
   "Integrating-Factor"
  ],
  "uses": [],
  "page": 2,
  "summary": "For $y'+ay=b$ with constants $a\\neq0, b$, the general solution is $y(t)=b/a+ce^{-at}$, obtained using the integrating factor $\\mu(t)=e^{at}$."
 },
 {
  "name": "Interval of Validity (First-Order Linear ODE)",
  "type": "concept",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [
   "Canonical Form of a First-Order Linear ODE"
  ],
  "uses": [],
  "page": "5-6",
  "summary": "The largest interval containing the initial point on which $p(t)$, $g(t)$, and any coefficients divided out along the way are defined; an IVP solution is valid only there."
 },
 {
  "name": "IVP with Constant Coefficient and Exponential Forcing",
  "type": "problem",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [],
  "uses": [
   "Canonical Form of a First-Order Linear ODE",
   "Integrating-Factor"
  ],
  "page": 3,
  "summary": "Example 1: solving $y'+\\frac12y=\\frac12e^{t/3}$, $y(0)=1$, by the integrating-factor method."
 },
 {
  "name": "IVP with Constant Coefficient and Polynomial Forcing",
  "type": "problem",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [
   "Integration By Parts"
  ],
  "uses": [
   "Integrating-Factor"
  ],
  "page": 4,
  "summary": "Example 2: solving $y'-2y=4-x$, $y(0)=-7/4$, and describing the long-run behavior of the general solution as $x\\to\\infty$."
 },
 {
  "name": "IVP with Variable Coefficient after Dividing by x",
  "type": "problem",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [],
  "uses": [
   "Canonical Form of a First-Order Linear ODE",
   "Integrating-Factor",
   "Interval of Validity (First-Order Linear ODE)"
  ],
  "page": 5,
  "summary": "Example 3: solving $xy'+2y=4x^2$, $y(1)=2$, and finding the interval of validity $(0,\\infty)$."
 },
 {
  "name": "Direct Product Rule and IVP for a Simple Linear ODE",
  "type": "problem",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [],
  "uses": [
   "Integrating-Factor"
  ],
  "page": "5-6",
  "summary": "Examples 4-5: recognizing $ty'+y=0$ as already $\\frac{d}{dt}(ty)=0$, giving $y=c/t$, then solving with $y(1)=3$."
 },
 {
  "name": "IVP with Trigonometric Coefficient and Interval of Validity",
  "type": "problem",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [],
  "uses": [
   "Integrating-Factor",
   "Interval of Validity (First-Order Linear ODE)"
  ],
  "page": "6-7",
  "summary": "Example 6: solving $y'+(\\cot x)y=x\\csc x$, $y(\\pi/2)=1$, and finding the interval of validity $(0,\\pi)$."
 }
]
```

# Frankenstein problems

**Problem A.** Solve $xy' - y = x^3$, $y(1) = 2$, and give the interval of validity.

*Concepts tested:* Canonical Form of a First-Order Linear ODE, Integrating-Factor, Interval of Validity (First-Order Linear ODE).

*Solution.* Divide by $x$ (requires $x \neq 0$) to reach canonical form: $y' - \frac{1}{x}y = x^2$, so $p(x) = -1/x$ and $g(x) = x^2$.

Integrating factor: $\mu(x) = e^{\int -\frac{1}{x}dx} = e^{-\ln|x|} = \frac{1}{x}$ (taking $x>0$).

Then $\dfrac{d}{dx}\left(\dfrac{y}{x}\right) = g(x)\mu(x) = x^2 \cdot \dfrac{1}{x} = x$.

Integrate: $\dfrac{y}{x} = \dfrac{x^2}{2} + c$, so $y(x) = \dfrac{x^3}{2} + cx$.

Apply $y(1) = 2$: $2 = \frac12 + c \implies c = \frac32$.

So $y(x) = \dfrac{x^3}{2} + \dfrac{3x}{2} = \dfrac{x^3+3x}{2}$.

Check: $y' = \frac{3x^2+3}{2}$, so $xy' - y = \frac{3x^3+3x}{2} - \frac{x^3+3x}{2} = \frac{2x^3}{2} = x^3$. Correct.

Interval of validity: the initial point $x=1$ is positive and dividing by $x$ excluded $x=0$, so the interval is $(0,\infty)$.

**Problem B.** Solve $y' + y\tan t = t\sec t$, $y(0) = 0$, and give the interval of validity.

*Concepts tested:* Canonical Form of a First-Order Linear ODE, Integrating-Factor, Interval of Validity (First-Order Linear ODE); uses Integration By Parts (prereq).

*Solution.* The equation is already in canonical form with $p(t) = \tan t$, $g(t) = t\sec t$.

Integrating factor: $\int \tan t\,dt = -\ln|\cos t|$, so $\mu(t) = e^{-\ln|\cos t|} = \dfrac{1}{|\cos t|}$; near $t=0$, $\cos t > 0$, so $\mu(t) = \sec t$.

Then $\dfrac{d}{dt}(y\sec t) = g(t)\mu(t) = (t\sec t)(\sec t) = t\sec^2 t$.

Integrate by parts with $u=t$, $dv=\sec^2t\,dt$, so $du=dt$, $v=\tan t$:
$$\int t\sec^2 t\,dt = t\tan t - \int \tan t\,dt = t\tan t + \ln|\cos t| + c.$$

So $y\sec t = t\tan t + \ln|\cos t| + c$.

Apply $y(0)=0$: left side is $0 \cdot \sec 0 = 0$; right side is $0\cdot\tan 0 + \ln|\cos 0| + c = 0 + 0 + c = c$. So $c = 0$.

Thus $y\sec t = t\tan t + \ln|\cos t|$, so $y(t) = \cos t\,(t\tan t + \ln|\cos t|) = t\sin t + \cos t\ln|\cos t|$.

Check at $t=0$: $y(0) = 0 + 1\cdot\ln 1 = 0$. Correct. A full derivative check confirms $y' + y\tan t = t\sec t$.

Interval of validity: $\sec t$ and $\tan t$ require $\cos t \neq 0$; the largest such interval containing $t=0$ is $\left(-\dfrac{\pi}{2}, \dfrac{\pi}{2}\right)$.
