---
type: reference
parent: "[[AM20]]"
domain: math
course: "AM 20"
status: draft
source: "AM20 Review7 Integration Formulas"
tags:
  - decks
---
# AM 20 Cards - AM20 Review7 Integration Formulas Integration

## Basic Antiderivatives
| Front | Back | Notes |
| --- | --- | --- |
| $\int t^n\,dt$ ($n\neq -1$) | $\dfrac{t^{n+1}}{n+1}$ | p.1; formula |
| $\int \dfrac{1}{t}\,dt$ | $\ln\lvert t\rvert$ | p.1; formula |
| $\int e^{at}\,dt$ | $\dfrac{e^{at}}{a}$ | p.1; formula |
| $\int \dfrac{1}{1+t^2}\,dt$ | $\arctan t$ | p.1; formula |
| $\int \tan t\,dt$ | $-\ln\lvert \cos t\rvert$ | p.1; formula |
| $\int \sin at\,dt$ | $-\dfrac{\cos at}{a}$ | p.1; formula |
| $\int \cos at\,dt$ | $\dfrac{\sin at}{a}$ | p.1; formula |
| $\int \sec^2 at\,dt$ | $\dfrac{\tan at}{a}$ | p.1; formula |
| $\int \dfrac{1}{a^2+t^2}\,dt$ | $\dfrac{1}{a}\arctan\dfrac{t}{a}$ | p.1; formula |
| $\int \sec t\,dt$ | $\ln\lvert \sec t+\tan t\rvert$ | p.1; formula |

## U Substitution
| Front | Back | Notes |
| --- | --- | --- |
| Substitution formula when the integrand contains a function and its derivative | $\int f(g(t))g'(t)\,dt=\int f(u)\,du$, where $u=g(t)$ | p.1; formula |
| Most common substitution case in this course | $\int \dfrac{g'(t)}{g(t)}\,dt=\ln\lvert g(t)\rvert$, which is what turns every separable equation into logarithms | p.1; formula |

## Integration By Parts
| Front | Back | Notes |
| --- | --- | --- |
| Integration by parts formula | $\int u\,dv=uv-\int v\,du$ | p.1; formula |
| How to choose $u$ and $dv$ in integration by parts | $u$ should be the factor that simplifies when differentiated, usually a power of $t$; $dv$ should be the factor that is easy to integrate, usually an exponential or trig function | p.1; procedure |

## Partial Fractions
| Front | Back | Notes |
| --- | --- | --- |
| Partial fraction term contributed by a distinct linear factor $s-a$ | $\dfrac{A}{s-a}$ | p.1; formula |
| Partial fraction terms contributed by a repeated factor $(s-a)^k$ | One term for each power: $\dfrac{A_1}{s-a}+\cdots+\dfrac{A_k}{(s-a)^k}$ | p.1; formula |
| Partial fraction term contributed by an irreducible quadratic $s^2+ps+q$ | $\dfrac{As+B}{s^2+ps+q}$, with a linear numerator | p.1; formula |
| After splitting into partial fractions, how do you find the constants | Clear the denominators, then find the constants either by substituting the roots or by matching coefficients | p.1; procedure |

## Exponential Times Trigonometric Integrals
| Front | Back | Notes |
| --- | --- | --- |
| $\int e^{at}\cos bt\,dt$ | $\dfrac{e^{at}(a\cos bt+b\sin bt)}{a^2+b^2}$ | p.1; formula |
| $\int e^{at}\sin bt\,dt$ | $\dfrac{e^{at}(a\sin bt-b\cos bt)}{a^2+b^2}$ | p.2; formula |

## Completing the Square
| Front | Back | Notes |
| --- | --- | --- |
| Completing the square for $s^2+ps+q$ | $s^2+ps+q=\left(s+\dfrac{p}{2}\right)^2+\left(q-\dfrac{p^2}{4}\right)$ | p.2; formula |
| When is completing the square used for an integral with a quadratic denominator | When the quadratic has no real roots, turning the integral into an arctangent, or a Laplace transform into a shifted sine or cosine | p.2; discrimination |

## Improper Integrals
| Front | Back | Notes |
| --- | --- | --- |
| Definition of an integral to infinity | $\int_0^\infty f(t)\,dt=\lim_{A\to\infty}\int_0^A f(t)\,dt$ | p.2; formula |
| For $s>0$, what two facts make every Laplace transform converge | $e^{-sA}\to 0$ and $A^ne^{-sA}\to 0$ as $A\to\infty$, since an exponential decays faster than any power grows | p.2; definition |

## Basic Antiderivative Practice
| Front | Back | Notes |
| --- | --- | --- |
| Evaluate: (a) $\int t^4\,dt$ (b) $\int e^{-2t}\,dt$ (c) $\int dt/t^2$ (d) $\int \cos3t\,dt$ (e) $\int dt/(4+t^2)$: key move | Apply the basic table directly: (a) $t^5/5$ (b) $-\tfrac12e^{-2t}$ (c) $-1/t$ (d) $\tfrac13\sin3t$ (e) $\tfrac12\arctan(t/2)$ using $a=2$ | p.2; problem |

## Substitution Practice
| Front | Back | Notes |
| --- | --- | --- |
| Evaluate by substitution: (a) $\int te^{-t^2}\,dt$ (b) $\int \dfrac{2t}{1+t^2}\,dt$ (c) $\int \tan t\,dt$: key move | (a) $u=-t^2$ gives $-\tfrac12e^{-t^2}$ (b) the numerator is the derivative of the denominator, giving $\ln(1+t^2)$ (c) write $\tan t=\sin t/\cos t$ with $u=\cos t$, giving $-\ln\lvert\cos t\rvert$ | p.2-3; problem |

## Integration by Parts Practice
| Front | Back | Notes |
| --- | --- | --- |
| Evaluate by parts: (a) $\int te^{-st}\,dt$ (b) $\int t\sin t\,dt$: key move | (a) $u=t, dv=e^{-st}dt$ gives $-\dfrac{te^{-st}}{s}-\dfrac{e^{-st}}{s^2}$ (b) $u=t, dv=\sin t\,dt$ gives $-t\cos t+\sin t$ | p.3; problem |

## Partial Fractions Practice
| Front | Back | Notes |
| --- | --- | --- |
| Evaluate by partial fractions: (a) $\int \dfrac{dt}{(t-1)(t+2)}$ (b) $\int \dfrac{s+3}{s(s+1)}\,ds$: key move | (a) split into $\tfrac{1/3}{t-1}-\tfrac{1/3}{t+2}$, integrate to $\tfrac13\ln\left\lvert\tfrac{t-1}{t+2}\right\rvert$ (b) split into $\tfrac3s-\tfrac2{s+1}$, integrate to $3\ln\lvert s\rvert-2\ln\lvert s+1\rvert$ | p.3-4; problem |

## Exponential Times Cosine Integral with Check
| Front | Back | Notes |
| --- | --- | --- |
| Evaluate $\int e^{2t}\cos3t\,dt$ and check by differentiating: key move | Apply the exponential-times-trig formula with $a=2,b=3$, $a^2+b^2=13$: $\dfrac{e^{2t}(2\cos3t+3\sin3t)}{13}$; differentiating the right side by the product rule recovers $e^{2t}\cos3t$ | p.4; problem |

## Improper Integral Laplace Transforms of 1 and t
| Front | Back | Notes |
| --- | --- | --- |
| Evaluate $\int_0^\infty e^{-st}\,dt$ and $\int_0^\infty te^{-st}\,dt$ for $s>0$: key move | Take the antiderivative, evaluate at $A$, and let $A\to\infty$ using $e^{-sA}\to0$ and $Ae^{-sA}\to0$: results are $\mathcal{L}\{1\}=1/s$ and $\mathcal{L}\{t\}=1/s^2$ | p.4-5; problem |

## Integral via Completing the Square
| Front | Back | Notes |
| --- | --- | --- |
| Evaluate $\int \dfrac{dt}{t^2+4t+8}$: key move | Complete the square: $t^2+4t+8=(t+2)^2+4$; substitute $u=t+2$ and use the arctangent entry with $a=2$: $\tfrac12\arctan\dfrac{t+2}{2}$ | p.5; problem |
# Node map

```json
[
 {
  "name": "Basic Antiderivatives",
  "type": "concept",
  "existing": false,
  "parent": "Integration",
  "prereqs": [
   "Antiderivative"
  ],
  "uses": [],
  "page": 1,
  "summary": "Table of standard antiderivatives for powers, $1/t$, exponentials, arctangent forms, tangent, sine, cosine, and secant squared."
 },
 {
  "name": "U Substitution",
  "type": "concept",
  "existing": true,
  "parent": "Integration",
  "prereqs": [
   "Chain Rule"
  ],
  "uses": [],
  "page": 1,
  "summary": "If the integrand contains a function and its derivative, set $u$ equal to the inside function; the common case $\\int g'(t)/g(t)\\,dt=\\ln|g(t)|$ turns separable equations into logarithms."
 },
 {
  "name": "Integration By Parts",
  "type": "concept",
  "existing": true,
  "parent": "Integration",
  "prereqs": [
   "Product Rule (Calculus)"
  ],
  "uses": [],
  "page": 1,
  "summary": "$\\int u\\,dv=uv-\\int v\\,du$; choose $u$ as the factor that simplifies when differentiated and $dv$ as the easy-to-integrate factor."
 },
 {
  "name": "Partial Fractions",
  "type": "concept",
  "existing": false,
  "parent": "Integration",
  "prereqs": [
   "Integration"
  ],
  "uses": [],
  "page": 1,
  "summary": "To integrate a proper rational function, factor the denominator and split into terms for each distinct linear factor, repeated factor, or irreducible quadratic, then solve for the constants."
 },
 {
  "name": "Exponential Times Trigonometric Integrals",
  "type": "concept",
  "existing": false,
  "parent": "Integration",
  "prereqs": [
   "Integration By Parts"
  ],
  "uses": [],
  "page": 1,
  "summary": "Closed forms for $\\int e^{at}\\cos bt\\,dt$ and $\\int e^{at}\\sin bt\\,dt$, both confirmed by differentiating the right side."
 },
 {
  "name": "Completing the Square",
  "type": "concept",
  "existing": true,
  "parent": "Integration",
  "prereqs": [],
  "uses": [],
  "page": 2,
  "summary": "When a quadratic denominator has no real roots, $s^2+ps+q=(s+p/2)^2+(q-p^2/4)$ turns the integral into an arctangent."
 },
 {
  "name": "Improper Integrals",
  "type": "concept",
  "existing": false,
  "parent": "Integration",
  "prereqs": [
   "Limits"
  ],
  "uses": [],
  "page": 2,
  "summary": "An integral to infinity is a limit of integrals to $A$ as $A\\to\\infty$; for $s>0$, exponential decay beats polynomial growth, making Laplace transforms converge."
 },
 {
  "name": "Basic Antiderivative Practice",
  "type": "problem",
  "existing": false,
  "parent": "Integration",
  "prereqs": [
   "Basic Antiderivatives"
  ],
  "uses": [
   "Basic Antiderivatives"
  ],
  "page": 2,
  "summary": "Evaluates five short antiderivatives directly from the basic table."
 },
 {
  "name": "Substitution Practice",
  "type": "problem",
  "existing": false,
  "parent": "Integration",
  "prereqs": [
   "U Substitution"
  ],
  "uses": [
   "U Substitution"
  ],
  "page": 2,
  "summary": "Evaluates three integrals by substitution, including the common log case."
 },
 {
  "name": "Integration by Parts Practice",
  "type": "problem",
  "existing": false,
  "parent": "Integration",
  "prereqs": [
   "Integration By Parts"
  ],
  "uses": [
   "Integration By Parts"
  ],
  "page": 3,
  "summary": "Evaluates $\\int te^{-st}dt$ and $\\int t\\sin t\\,dt$ by parts."
 },
 {
  "name": "Partial Fractions Practice",
  "type": "problem",
  "existing": false,
  "parent": "Integration",
  "prereqs": [
   "Partial Fractions"
  ],
  "uses": [
   "Partial Fractions"
  ],
  "page": 3,
  "summary": "Evaluates two rational integrals by splitting into partial fractions."
 },
 {
  "name": "Exponential Times Cosine Integral with Check",
  "type": "problem",
  "existing": false,
  "parent": "Integration",
  "prereqs": [
   "Exponential Times Trigonometric Integrals"
  ],
  "uses": [
   "Exponential Times Trigonometric Integrals"
  ],
  "page": 4,
  "summary": "Evaluates $\\int e^{2t}\\cos3t\\,dt$ and verifies the result by differentiating it back."
 },
 {
  "name": "Improper Integral Laplace Transforms of 1 and t",
  "type": "problem",
  "existing": false,
  "parent": "Integration",
  "prereqs": [
   "Improper Integrals",
   "Integration by Parts Practice"
  ],
  "uses": [
   "Improper Integrals",
   "Integration by Parts Practice"
  ],
  "page": 4,
  "summary": "Evaluates $\\int_0^\\infty e^{-st}dt$ and $\\int_0^\\infty te^{-st}dt$, identifying them as the Laplace transforms of $1$ and $t$."
 },
 {
  "name": "Integral via Completing the Square",
  "type": "problem",
  "existing": false,
  "parent": "Integration",
  "prereqs": [
   "Completing the Square",
   "U Substitution"
  ],
  "uses": [
   "Completing the Square",
   "U Substitution"
  ],
  "page": 5,
  "summary": "Evaluates $\\int dt/(t^2+4t+8)$ by completing the square and substituting."
 }
]
```

# Frankenstein problems

**Problem 1.** Evaluate $\displaystyle\int \frac{3t+5}{(t-1)(t^2+4)}\,dt$.

*Concepts tested:* Partial Fractions, U Substitution, Basic Antiderivatives.

*Solution.*

Split into partial fractions: $\dfrac{3t+5}{(t-1)(t^2+4)} = \dfrac{A}{t-1} + \dfrac{Bt+C}{t^2+4}$, so $3t+5 = A(t^2+4) + (Bt+C)(t-1)$.

Setting $t=1$: $8 = 5A$, so $A = 8/5$.

Matching the $t^2$ coefficient: $0 = A+B$, so $B = -8/5$. Matching the constant term: $5 = 4A - C$, so $C = 4A-5 = 32/5-25/5=7/5$. (Check the $t^1$ coefficient: $-B+C = 8/5+7/5=15/5=3$, correct.)

So the integrand is $\dfrac{8/5}{t-1} + \dfrac{-\tfrac85 t+\tfrac75}{t^2+4}$.

Integrate the first term with the basic $1/t$-type formula: $\dfrac85\ln|t-1|$.

Integrate $-\tfrac85\dfrac{t}{t^2+4}$ by substitution $u=t^2+4, du=2t\,dt$: $-\tfrac85\cdot\tfrac12\ln(t^2+4) = -\tfrac45\ln(t^2+4)$.

Integrate $\tfrac75\dfrac{1}{t^2+4}$ with the basic arctangent formula ($a=2$): $\tfrac75\cdot\tfrac12\arctan\dfrac{t}{2} = \tfrac{7}{10}\arctan\dfrac{t}{2}$.

$$\int \frac{3t+5}{(t-1)(t^2+4)}\,dt = \frac{8}{5}\ln|t-1| - \frac{4}{5}\ln(t^2+4) + \frac{7}{10}\arctan\frac{t}{2} + C.$$
