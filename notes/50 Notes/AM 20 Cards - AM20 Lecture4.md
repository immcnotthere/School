---
type: reference
parent: "[[AM20]]"
domain: math
course: "AM 20"
status: draft
source: "AM20 Lecture4"
tags:
  - decks
---
# AM 20 Cards - AM20 Lecture4 Separable Equations

## Separable Equation
| Front | Back | Notes |
| --- | --- | --- |
| What does it mean for a first-order ODE to be separable? | It can be written as $M(x)\,dx + N(y)\,dy = 0$, where $M$ depends on $x$ alone and $N$ depends on $y$ alone | p.1; definition |
| Once a separable equation is written as $M(x)dx + N(y)dy = 0$, what gives its general implicit solution? | $\int M(x)\,dx + \int N(y)\,dy = c$, integrating each term in its own variable | p.1, 2; formula |
| How does the method of separable equations differ from the method of integrating factors in what equations it can solve? | Integrating factors only solve linear equations; separable equations work for linear or nonlinear equations, as long as the two variables can be pulled apart | p.1; discrimination |
| What is the first algebraic step to put $\frac{dy}{dx} = \frac{x^2}{1-y^2}$ into the separated form $Mdx+Ndy=0$? | Multiply by $(1-y^2)dx$ to get $(1-y^2)dy = x^2dx$, then move everything to one side: $x^2dx - (1-y^2)dy = 0$ | p.2; procedure |

## Implicit Solutions
| Front | Back | Notes |
| --- | --- | --- |
| What is an implicit solution of an ODE? | A relation $G(x,y)=c$ that the solution satisfies but that has not been solved for $y$ | p.2; definition |
| What distinguishes an explicit solution from an implicit solution, and what is an integral curve? | An explicit solution is a formula $y=\phi(x)$ giving $y$ directly; an integral curve is the graph of an explicit solution | p.2; discrimination |
| How do you pick out one member of the family of implicit solutions $\int M dx + \int N dy = c$? | Require the curve to pass through a prescribed point $(x_0,y_0)$, which determines the constant $c$ | p.2; procedure |
| How do you check that an implicit solution $G(x,y)=c$ really solves the original ODE? | Differentiate $G(x,y)=c$ with respect to $x$, treating $y$ as a function of $x$ and applying the chain rule to terms in $y$, then solve for $dy/dx$ and compare to the original equation | p.2; procedure |

## Interval of Validity (Separable Equation)
| Front | Back | Notes |
| --- | --- | --- |
| What two conditions determine the interval of validity for an explicit solution $y=\phi(x)$ from a separable IVP? | (1) Any radicand or other domain restriction in $\phi(x)$ must hold, and (2) any value excluded by the original equation, such as a zero denominator, must be avoided; take the largest interval around the initial point satisfying both | p.4, 5; procedure |
| In Example 2, why is $x=-2$ excluded from the interval of validity even though the radicand $x^3+2x^2+2x+4$ is zero, not negative, there? | At $x=-2$ the solution gives $y=1$, but the original equation has $y-1$ in a denominator, so $y=1$ is not allowed | p.4; discrimination |

## Separable Equation with Cubic Implicit Solution
| Front | Back | Notes |
| --- | --- | --- |
| Example 1: show $\frac{dy}{dx}=\frac{x^2}{1-y^2}$ is separable and find its integral curve through $(0,0)$. What is the key result? | Separating and integrating gives $x^3+y^3-3y=c'$; through $(0,0)$, $c'=0$, so $x^3+y^3-3y=0$ is the implicit solution, left implicit since solving for $y$ would need the cubic formula | p.2; problem |

## IVP with Quadratic-in-y Implicit Solution and Interval of Validity
| Front | Back | Notes |
| --- | --- | --- |
| Example 2: solve $y'=\frac{3x^2+4x+2}{2(y-1)}$, $y(0)=-1$, for the explicit solution and interval of validity. What is the key move? | The implicit solution $(x^3+2x^2+2x)-(y^2-2y)=-3$ rearranges to a quadratic in $y$; the quadratic formula and $y(0)=-1$ select $y=1-\sqrt{x^3+2x^2+2x+4}$, valid on $x>-2$ (excluding where the radicand is $0$, since that gives the forbidden $y=1$) | p.3, 4; problem |

## Same Equation with a Different Initial Condition
| Front | Back | Notes |
| --- | --- | --- |
| Example 3: repeat Example 2's equation with $y(0)=0$ instead of $y(0)=-1$. What changes, and what is the new interval of validity? | The new constant is $c=0$, giving $y=1-\sqrt{x^3+2x^2+2x+1}$; factoring $x^3+2x^2+2x+1=(x+1)(x^2+x+1)$ with the quadratic factor always positive, the interval of validity is $x>-1$ | p.4; problem |

## Circle Integral Curves from a Separable Equation
| Front | Back | Notes |
| --- | --- | --- |
| Example 4: solve $\frac{dy}{dx}=-\frac{x}{y}$, $y(0)=3$, and describe the integral curves. What is the key result? | Separating gives $x^2+y^2=9$; solving for $y$ through $(0,3)$ gives $y=\sqrt{9-x^2}$, valid on $-3<x<3$, and each solution is the upper half of a circle centered at the origin | p.5; problem |

## IVP Requiring a Square-Root Domain Restriction Away from the Origin
| Front | Back | Notes |
| --- | --- | --- |
| Example 5: solve $\frac{dy}{dx}=\frac{2x}{1+2y}$, $y(2)=0$. What is the key move and the resulting interval of validity? | Separating and integrating gives $x^2-y-y^2=4$; the quadratic formula and $y(2)=0$ select $y=\frac{-1+\sqrt{4x^2-15}}{2}$, valid for $x>\sqrt{15}/2$ (excluding where $1+2y=0$) | p.5; problem |
# Node map
```json
[
 {
  "name": "Separable Equation",
  "type": "concept",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [],
  "uses": [],
  "page": 1,
  "summary": "A first-order ODE that can be written $M(x)dx+N(y)dy=0$, so each term can be integrated in its own variable to give $\\int M\\,dx+\\int N\\,dy=c$."
 },
 {
  "name": "Implicit Solutions",
  "type": "concept",
  "existing": true,
  "parent": "1st Order ODE",
  "prereqs": [
   "Chain Rule"
  ],
  "uses": [],
  "page": 2,
  "summary": "A relation $G(x,y)=c$ satisfied by the solution but not solved for $y$; contrasted with an explicit solution $y=\\phi(x)$, whose graph is an integral curve."
 },
 {
  "name": "Interval of Validity (Separable Equation)",
  "type": "concept",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [
   "Separable Equation",
   "Quadratic Equation"
  ],
  "uses": [],
  "page": "3-5",
  "summary": "The largest interval around the initial point on which both the domain restrictions of the explicit solution (e.g. a radicand) and the restrictions of the original equation (e.g. an excluded denominator value) hold."
 },
 {
  "name": "Separable Equation with Cubic Implicit Solution",
  "type": "problem",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [],
  "uses": [
   "Separable Equation",
   "Implicit Solutions"
  ],
  "page": 2,
  "summary": "Example 1: showing $dy/dx=x^2/(1-y^2)$ is separable and finding the implicit integral curve $x^3+y^3-3y=0$ through the origin."
 },
 {
  "name": "IVP with Quadratic-in-y Implicit Solution and Interval of Validity",
  "type": "problem",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [],
  "uses": [
   "Separable Equation",
   "Implicit Solutions",
   "Interval of Validity (Separable Equation)",
   "Quadratic Equation"
  ],
  "page": "3-4",
  "summary": "Example 2: solving $y'=(3x^2+4x+2)/(2(y-1))$, $y(0)=-1$, for the explicit solution and interval $x>-2$."
 },
 {
  "name": "Same Equation with a Different Initial Condition",
  "type": "problem",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [],
  "uses": [
   "Separable Equation",
   "Implicit Solutions",
   "Interval of Validity (Separable Equation)",
   "Quadratic Equation"
  ],
  "page": 4,
  "summary": "Example 3: repeating Example 2 with $y(0)=0$, giving interval of validity $x>-1$."
 },
 {
  "name": "Circle Integral Curves from a Separable Equation",
  "type": "problem",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [],
  "uses": [
   "Separable Equation",
   "Implicit Solutions",
   "Interval of Validity (Separable Equation)"
  ],
  "page": 5,
  "summary": "Example 4: solving $dy/dx=-x/y$, $y(0)=3$, giving circles $x^2+y^2=9$ and interval $-3<x<3$."
 },
 {
  "name": "IVP Requiring a Square-Root Domain Restriction Away from the Origin",
  "type": "problem",
  "existing": false,
  "parent": "1st Order ODE",
  "prereqs": [],
  "uses": [
   "Separable Equation",
   "Implicit Solutions",
   "Interval of Validity (Separable Equation)",
   "Quadratic Equation"
  ],
  "page": 5,
  "summary": "Example 5: solving $dy/dx=2x/(1+2y)$, $y(2)=0$, giving interval of validity $x>\\sqrt{15}/2$."
 }
]
```

# Frankenstein problems

**Problem A.** Solve $\dfrac{dy}{dx} = \dfrac{3x^2+2x+4}{2y-2}$, $y(0) = 3$. Find the explicit solution and its interval of validity.

*Concepts tested:* Separable Equation, Implicit Solutions, Interval of Validity (Separable Equation); uses Quadratic Equation (prereq).

*Solution.* Separate: $(2y-2)\,dy = (3x^2+2x+4)\,dx$.

Integrate each side: $y^2 - 2y = x^3+x^2+4x + c$.

Apply $y(0)=3$: $9-6 = 3 = c$ (the right side is $0$ at $x=0$). So the implicit solution is
$$y^2 - 2y - (x^3+x^2+4x+3) = 0.$$

Solve for $y$ as a quadratic with $a=1,\ b=-2,\ c_{\text{quad}}=-(x^3+x^2+4x+3)$:
$$y = \frac{2 \pm \sqrt{4+4(x^3+x^2+4x+3)}}{2} = 1 \pm \sqrt{x^3+x^2+4x+4}.$$

Factor the radicand by grouping: $x^3+x^2+4x+4 = x^2(x+1)+4(x+1) = (x^2+4)(x+1)$.

At $x=0$: radicand $=4$, so the branches give $y=1+2=3$ and $y=1-2=-1$. Since $y(0)=3$, take the plus branch:
$$y(x) = 1+\sqrt{(x^2+4)(x+1)}.$$

Interval of validity: $x^2+4>0$ always, so the radicand's sign matches $x+1$, requiring $x\geq -1$. The original equation has $2y-2$ in the denominator, so $y=1$ is excluded; that happens exactly where the radicand is $0$, i.e. $x=-1$. Dropping that point, the interval of validity is $x>-1$.

**Problem B.** Solve $\dfrac{dy}{dx} = \dfrac{2x+3}{3y^2-4}$, $y(0) = 2$, and verify the implicit solution by differentiating.

*Concepts tested:* Separable Equation, Implicit Solutions; uses Chain Rule (prereq).

*Solution.* Separate: $(3y^2-4)\,dy = (2x+3)\,dx$.

Integrate each side: $y^3 - 4y = x^2 + 3x + c$.

Apply $y(0)=2$: $8-8=0$ on the left, and the right side is $0$ at $x=0$, so $c=0$. The implicit solution is
$$y^3 - 4y = x^2 + 3x.$$

This is a cubic in $y$, so (as in Example 1) it is left implicit rather than solved explicitly.

Check by differentiating both sides with respect to $x$, using the chain rule on $y^3$ and $4y$:
$$3y^2\frac{dy}{dx} - 4\frac{dy}{dx} = 2x+3 \implies \frac{dy}{dx}(3y^2-4) = 2x+3 \implies \frac{dy}{dx} = \frac{2x+3}{3y^2-4},$$
which matches the original equation, confirming the implicit solution.
