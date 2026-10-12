---
type: reference
parent: "[[AM20]]"
domain: math
course: "AM 20"
status: draft
source: "AM20 Review6 Derivative Formulas"
tags:
  - decks
---
# AM 20 Cards - AM20 Review6 Derivative Formulas Derivatives

## Basic Derivative Formulas
| Front | Back | Notes |
| --- | --- | --- |
| $\dfrac{d}{dt}(t^n)$ | $nt^{n-1}$ | p.1; formula |
| $\dfrac{d}{dt}(e^{at})$ | $ae^{at}$ | p.1; formula |
| $\dfrac{d}{dt}(\ln t)$ | $\dfrac{1}{t}$ | p.1; formula |
| $\dfrac{d}{dt}(\sqrt{t})$ | $\dfrac{1}{2\sqrt{t}}$ | p.1; formula |
| $\dfrac{d}{dt}(\sinh at)$ | $a\cosh at$ | p.1; formula |
| $\dfrac{d}{dt}(\sin at)$ | $a\cos at$ | p.1; formula |
| $\dfrac{d}{dt}(\cos at)$ | $-a\sin at$ | p.1; formula |
| $\dfrac{d}{dt}(\tan at)$ | $a\sec^2 at$ | p.1; formula |
| $\dfrac{d}{dt}(\arctan t)$ | $\dfrac{1}{1+t^2}$ | p.1; formula |
| $\dfrac{d}{dt}(\cosh at)$ | $a\sinh at$ | p.1; formula |

## Product Rule (Calculus)
| Front | Back | Notes |
| --- | --- | --- |
| Product rule for $(fg)'$ | $f'g+fg'$ | p.1; formula |

## Quotient Rule
| Front | Back | Notes |
| --- | --- | --- |
| Quotient rule for $(f/g)'$ | $\dfrac{f'g-fg'}{g^2}$ | p.1; formula |

## Chain Rule
| Front | Back | Notes |
| --- | --- | --- |
| Chain rule for $(f(g))'$ | $f'(g)\,g'$ | p.1; formula |
| Why is the chain rule the rule used most often in this course | Because almost every function in this course has something other than $t$ inside it | p.1; definition |

## Recurring Derivative Products
| Front | Back | Notes |
| --- | --- | --- |
| $(te^{at})'$ | $e^{at}+ate^{at}=(1+at)e^{at}$ | p.1; formula |
| $(e^{\alpha t}\cos\beta t)'$ | $e^{\alpha t}(\alpha\cos\beta t-\beta\sin\beta t)$ | p.1; formula |
| $(e^{\alpha t}\sin\beta t)'$ | $e^{\alpha t}(\alpha\sin\beta t+\beta\cos\beta t)$ | p.1; formula |

## Implicit differentiation
| Front | Back | Notes |
| --- | --- | --- |
| When differentiating an expression containing $y$ as an unknown function of $x$, what extra factor appears | A factor $y'$, by the chain rule | p.1; definition |
| $\dfrac{d}{dx}(y^3)$ | $3y^2y'$ | p.1; formula |
| $\dfrac{d}{dx}(xy)$ | $y+xy'$ | p.1; formula |
| $\dfrac{d}{dx}(e^y)$ | $e^yy'$ | p.1; formula |

## Partial Derivatives
| Front | Back | Notes |
| --- | --- | --- |
| For a function of two variables, what does $\partial/\partial x$ do | Differentiates with respect to $x$ while treating $y$ as a constant | p.1; definition |
| For a function of two variables, what does $\partial/\partial y$ do | Differentiates with respect to $y$ while treating $x$ as a constant | p.1; definition |
| Why does no factor $y'$ appear when taking a partial derivative, unlike in implicit differentiation | Because $y$ is treated as an independent variable rather than as a function of $x$ | p.1; discrimination |

## Basic Derivative Practice
| Front | Back | Notes |
| --- | --- | --- |
| Differentiate: (a) $3t^5-2/t$ (b) $e^{-4t}$ (c) $\ln(3t)$ (d) $\sin5t$ (e) $\sqrt t$: key move | Rewrite $2/t=2t^{-1}$ and $\sqrt t=t^{1/2}$, then apply the power, chain, and basic formulas: (a) $15t^4+2/t^2$ (b) $-4e^{-4t}$ (c) $1/t$ (d) $5\cos5t$ (e) $\dfrac{1}{2\sqrt t}$ | p.1-2; problem |

## Product Rule with Two Functions
| Front | Back | Notes |
| --- | --- | --- |
| Differentiate $t^2e^{3t}$ and $e^{-t}\cos2t$: key move | Product rule with $f=t^2,g=e^{3t}$ gives $(2t+3t^2)e^{3t}$; with $f=e^{-t},g=\cos2t$ gives $e^{-t}(-\cos2t-2\sin2t)$, matching the recurring pattern with $\alpha=-1,\beta=2$ | p.2; problem |

## Quotient Rule for a Logarithm over t
| Front | Back | Notes |
| --- | --- | --- |
| Differentiate $\dfrac{\ln t}{t}$: key move | Quotient rule with $f=\ln t, g=t$ gives $\dfrac{(1/t)t-(\ln t)(1)}{t^2}=\dfrac{1-\ln t}{t^2}$ | p.2; problem |

## Chain Rule with Composed Functions
| Front | Back | Notes |
| --- | --- | --- |
| Differentiate $e^{t^2}$ and $\sqrt{x^3+2x^2+2x+4}$: key move | Outside function times derivative of inside: $(e^{t^2})'=2te^{t^2}$; $\dfrac{d}{dx}\sqrt{x^3+2x^2+2x+4}=\dfrac{3x^2+4x+2}{2\sqrt{x^3+2x^2+2x+4}}$ | p.2-3; problem |

## First and Second Derivative of a Recurring Product
| Front | Back | Notes |
| --- | --- | --- |
| Find $y'$ and $y''$ for $y=te^{-3t}$: key move | $y'=e^{-3t}-3te^{-3t}$; differentiate again with the product rule to get $y''=-6e^{-3t}+9te^{-3t}$; every derivative keeps the form $(A+Bt)e^{-3t}$ | p.3; problem |

## Implicit Derivative from an Equation
| Front | Back | Notes |
| --- | --- | --- |
| Find $dy/dx$ from $x^3+y^3-3y=c$: key move | Differentiate both sides: $3x^2+3y^2y'-3y'=0$; solve to get $y'=\dfrac{x^2}{1-y^2}$ | p.3; problem |

## Partial Derivatives of a Two Variable Function
| Front | Back | Notes |
| --- | --- | --- |
| For $\Psi(x,y)=y\sin x+x^2e^y-y$, find $\Psi_x$ and $\Psi_y$: key move | Treating the other variable as constant: $\Psi_x=y\cos x+2xe^y$ and $\Psi_y=\sin x+x^2e^y-1$; no factor $y'$ appears since $x,y$ are independent | p.3; problem |
# Node map

```json
[
 {
  "name": "Basic Derivative Formulas",
  "type": "concept",
  "existing": false,
  "parent": "Derivatives",
  "prereqs": [
   "Derivative"
  ],
  "uses": [],
  "page": 1,
  "summary": "Table of standard derivatives for powers, exponentials, logs, roots, and the trig and hyperbolic functions."
 },
 {
  "name": "Product Rule (Calculus)",
  "type": "concept",
  "existing": true,
  "parent": "Derivatives",
  "prereqs": [
   "Derivative"
  ],
  "uses": [],
  "page": 1,
  "summary": "$(fg)'=f'g+fg'$."
 },
 {
  "name": "Quotient Rule",
  "type": "concept",
  "existing": true,
  "parent": "Derivatives",
  "prereqs": [
   "Derivative"
  ],
  "uses": [],
  "page": 1,
  "summary": "$(f/g)'=\\dfrac{f'g-fg'}{g^2}$."
 },
 {
  "name": "Chain Rule",
  "type": "concept",
  "existing": true,
  "parent": "Derivatives",
  "prereqs": [
   "Derivative"
  ],
  "uses": [],
  "page": 1,
  "summary": "$(f(g))'=f'(g)g'$; the most-used rule since most functions in this course have a composed inside function."
 },
 {
  "name": "Recurring Derivative Products",
  "type": "concept",
  "existing": false,
  "parent": "Derivatives",
  "prereqs": [
   "Product Rule (Calculus)",
   "Chain Rule",
   "Basic Derivative Formulas"
  ],
  "uses": [],
  "page": 1,
  "summary": "Three products that appear constantly: $(te^{at})'$, $(e^{\\alpha t}\\cos\\beta t)'$, and $(e^{\\alpha t}\\sin\\beta t)'$."
 },
 {
  "name": "Implicit differentiation",
  "type": "concept",
  "existing": true,
  "parent": "Derivatives",
  "prereqs": [
   "Chain Rule"
  ],
  "uses": [],
  "page": 1,
  "summary": "Differentiating an expression containing $y$ as an unknown function of $x$ brings out a factor $y'$ by the chain rule."
 },
 {
  "name": "Partial Derivatives",
  "type": "concept",
  "existing": false,
  "parent": "Derivatives",
  "prereqs": [
   "Derivative"
  ],
  "uses": [],
  "page": 1,
  "summary": "$\\partial/\\partial x$ differentiates with respect to $x$ holding $y$ constant, and vice versa for $\\partial/\\partial y$; no $y'$ factor appears."
 },
 {
  "name": "Basic Derivative Practice",
  "type": "problem",
  "existing": false,
  "parent": "Derivatives",
  "prereqs": [
   "Basic Derivative Formulas",
   "Chain Rule"
  ],
  "uses": [
   "Basic Derivative Formulas",
   "Chain Rule"
  ],
  "page": 1,
  "summary": "Differentiates five short functions using the power, chain, and basic formulas."
 },
 {
  "name": "Product Rule with Two Functions",
  "type": "problem",
  "existing": false,
  "parent": "Derivatives",
  "prereqs": [
   "Product Rule (Calculus)",
   "Recurring Derivative Products"
  ],
  "uses": [
   "Product Rule (Calculus)",
   "Recurring Derivative Products"
  ],
  "page": 2,
  "summary": "Differentiates $t^2e^{3t}$ and $e^{-t}\\cos2t$ with the product rule."
 },
 {
  "name": "Quotient Rule for a Logarithm over t",
  "type": "problem",
  "existing": false,
  "parent": "Derivatives",
  "prereqs": [
   "Quotient Rule"
  ],
  "uses": [
   "Quotient Rule"
  ],
  "page": 2,
  "summary": "Differentiates $(\\ln t)/t$ with the quotient rule."
 },
 {
  "name": "Chain Rule with Composed Functions",
  "type": "problem",
  "existing": false,
  "parent": "Derivatives",
  "prereqs": [
   "Chain Rule",
   "Basic Derivative Formulas"
  ],
  "uses": [
   "Chain Rule",
   "Basic Derivative Formulas"
  ],
  "page": 2,
  "summary": "Differentiates $e^{t^2}$ and a square root of a cubic using the chain rule."
 },
 {
  "name": "First and Second Derivative of a Recurring Product",
  "type": "problem",
  "existing": false,
  "parent": "Derivatives",
  "prereqs": [
   "Product Rule (Calculus)",
   "Recurring Derivative Products"
  ],
  "uses": [
   "Product Rule (Calculus)",
   "Recurring Derivative Products"
  ],
  "page": 3,
  "summary": "Finds $y'$ and $y''$ for $y=te^{-3t}$, showing the pattern $(A+Bt)e^{-3t}$ persists."
 },
 {
  "name": "Implicit Derivative from an Equation",
  "type": "problem",
  "existing": false,
  "parent": "Derivatives",
  "prereqs": [
   "Implicit differentiation"
  ],
  "uses": [
   "Implicit differentiation"
  ],
  "page": 3,
  "summary": "Finds $dy/dx$ from $x^3+y^3-3y=c$ by implicit differentiation."
 },
 {
  "name": "Partial Derivatives of a Two Variable Function",
  "type": "problem",
  "existing": false,
  "parent": "Derivatives",
  "prereqs": [
   "Partial Derivatives"
  ],
  "uses": [
   "Partial Derivatives"
  ],
  "page": 3,
  "summary": "Finds $\\Psi_x$ and $\\Psi_y$ for $\\Psi(x,y)=y\\sin x+x^2e^y-y$."
 }
]
```

# Frankenstein problems

**Problem 1.** Differentiate $f(t) = t\,e^{-2t}\cos 3t$.

*Concepts tested:* Product Rule (Calculus), Chain Rule, Basic Derivative Formulas, Recurring Derivative Products.

*Solution.*

Group $f(t) = u(t)v(t)$ with $u(t) = te^{-2t}$ and $v(t) = \cos 3t$.

By the recurring product pattern with $a=-2$: $u'(t) = (1+at)e^{at} = (1-2t)e^{-2t}$.

By the chain rule and the basic formula for $\cos at$ with $a=3$: $v'(t) = -3\sin 3t$.

By the product rule, $f'(t) = u'v + uv'$:
$$f'(t) = (1-2t)e^{-2t}\cos 3t + te^{-2t}(-3\sin 3t) = e^{-2t}\big[(1-2t)\cos 3t - 3t\sin 3t\big].$$
