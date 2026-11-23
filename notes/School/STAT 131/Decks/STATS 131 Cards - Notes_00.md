---
type: reference
parent: "[[STATS 131]]"
domain: stats
course: "STATS 131"
status: draft
source: "Notes_00"
tags:
  - decks
---
# STATS 131 Cards - Notes_00 Calculus Review

## Geometric Series
| Front | Back | Notes |
| --- | --- | --- |
| Finite geometric series $S = 1+x+x^2+\cdots+x^n$ (for $x\neq1$): formula for $S$? | $S = \dfrac{1-x^{n+1}}{1-x}$ | p.1; formula |
| Infinite geometric series $S=1+x+x^2+\cdots$ for $\lvert x\rvert<1$: formula for $S$? | $S=\dfrac{1}{1-x}$ | p.1; formula |
| Key algebra trick to derive the finite geometric series formula? | Multiply $S$ by $(1-x)$: $(1-x)S = S - xS$ telescopes to $1-x^{n+1}$, then divide by $(1-x)$ | p.1; procedure |

## Term-by-Term Differentiation of Series
| Front | Back | Notes |
| --- | --- | --- |
| General technique: given a power series that equals a closed form $f(x)$, how do you find $\sum n a_n x^{n-1}$? | Differentiate both sides with respect to $x$; the derivative of the series is $\sum n a_n x^{n-1}$ and the derivative of $f(x)$ gives the closed form | p.1-2; procedure |
| Why must you check $\lvert x\rvert<1$ before differentiating the infinite geometric series term by term? | The series only converges (equals $1/(1-x)$) for $\lvert x\rvert<1$, so term-by-term differentiation is only valid inside that radius | p.2; discrimination |

## Integration By Parts
| Front | Back | Notes |
| --- | --- | --- |
| Integration by parts formula? | $\displaystyle\int_a^b u\,dv = \big[uv\big]_a^b - \int_a^b v\,du$ | p.2; formula |
| When is integration by parts most useful? | When integrating a product of two functions | p.2; definition |
| For $\int y e^{-y}\,dy$, what choice of $u$ and $dv$ makes integration by parts work? | $u=y$, $dv=e^{-y}dy$, so $du=dy$, $v=-e^{-y}$ | p.2; procedure |

## Double Integrals
| Front | Back | Notes |
| --- | --- | --- |
| How do you evaluate a double integral $\iint f\,dx\,dy$ over fixed bounds? | View it as two single integrations in sequence: integrate with respect to one variable first (holding the other fixed), then integrate that result with respect to the second variable | p.2-3; procedure |
| In $\int_0^\infty\!\int_0^y e^{-y}\,dx\,dy$, which variable do you integrate first? | $x$ first, treating $y$ as a constant, since $dx$ is the inner differential | p.3; procedure |

## Order of Integration
| Front | Back | Notes |
| --- | --- | --- |
| What must you do before swapping the order of integration in a double integral? | Sketch and understand the region of integration in the $xy$-plane, so you can rewrite the bounds for the new order | p.3; procedure |
| Region $0\le x\le y$, $0\le y<\infty$: what are the swapped bounds to integrate $y$ first? | $x$ ranges from $0$ to $\infty$; for fixed $x$, $y$ ranges from $x$ to $\infty$ | p.3; procedure |

## Fundamental Theorem of Calculus
| Front | Back | Notes |
| --- | --- | --- |
| FTC: $\dfrac{d}{dx}\displaystyle\int_a^x f(t)\,dt = ?$ | $f(x)$ | p.4; formula |
| What does $\int_a^x f(t)\,dt$ represent geometrically? | The area under the curve of $f$ from $t=a$ to $t=x$ | p.4; definition |
| Key limit step in the intuition for $\frac{d}{dx}\int_a^x f(t)dt=f(x)$? | $\displaystyle\lim_{\Delta\to0}\frac{\int_x^{x+\Delta}f(t)\,dt}{\Delta} \approx \lim_{\Delta\to0}\frac{f(x)\Delta}{\Delta}=f(x)$ | p.5; procedure |

## Extension of the FTC
| Front | Back | Notes |
| --- | --- | --- |
| Extension of the FTC: $\dfrac{d}{dx}\displaystyle\int_a^{g(x)} f(t)\,dt = ?$ | $f(g(x))\cdot g'(x)$ | p.5; formula |
| What extra rule does the extended FTC combine with the basic FTC? | The chain rule, since the upper bound is itself a function $g(x)$ | p.5; discrimination |

## Euler's Number
| Front | Back | Notes |
| --- | --- | --- |
| Euler's number $e$ defined as a limit? | $e=\displaystyle\lim_{n\to\infty}\left(1+\frac{1}{n}\right)^n$ | p.5; definition |
| General limit form: $\displaystyle\lim_{n\to\infty}\left(1+\frac{x}{n}\right)^n = ?$ (constant $x$) | $e^x$ | p.6; formula |

## Taylor Series
| Front | Back | Notes |
| --- | --- | --- |
| Taylor series of $f(x)$ expanded around $0$? | $p(x)=f(0)+\dfrac{f'(0)}{1!}x+\dfrac{f''(0)}{2!}x^2+\dfrac{f'''(0)}{3!}x^3+\cdots$ | p.6; formula |
| What must be true of $f$ for a Taylor series expansion around $0$ to exist? | $f$ must be infinitely differentiable at $0$ | p.6; definition |
| As you include more terms of a Taylor series, what happens to $p(x)$? | $p(x)$ approaches $f(x)$; with infinitely many terms, $p(x)=f(x)$ | p.6; definition |

## Weighted Geometric Series (n x to the (n-1))
| Front | Back | Notes |
| --- | --- | --- |
| Key move to evaluate $S=1+2x+3x^2+\cdots+nx^{n-1}$ (finite) or its infinite version? | Recognize $S = \frac{d}{dx}(1+x+x^2+\cdots+x^n)$; differentiate the closed-form geometric series formula, giving $S=\dfrac{1-(n+1)x^n+nx^{n+1}}{(1-x)^2}$ (finite) or $S=\dfrac{1}{(1-x)^2}$ (infinite, $\lvert x\rvert<1$) | p.1-2; procedure |

## Integration by Parts, y e to the (-y)
| Front | Back | Notes |
| --- | --- | --- |
| Key move and result for $\int_0^\infty y e^{-y}\,dy$? | By parts with $u=y$, $dv=e^{-y}dy$: $=\big[-ye^{-y}\big]_0^\infty - \int_0^\infty(-e^{-y})dy = 0 + \big[-e^{-y}\big]_0^\infty = 1$ | p.2; procedure |

## Double Integral, e to the (-y) over a Triangle
| Front | Back | Notes |
| --- | --- | --- |
| Key move for $\int_0^\infty\!\int_0^y e^{-y}\,dx\,dy$? | Integrate over $x$ first (treating $y$ as constant): the inner integral gives $ye^{-y}$, leaving $\int_0^\infty y e^{-y}\,dy=1$ | p.3; procedure |

## Changing Order of Integration, e to the (-y) over a Triangle
| Front | Back | Notes |
| --- | --- | --- |
| Key move to evaluate $\int_0^\infty\!\int_0^y e^{-y}\,dx\,dy$ by swapping the order? | Swap to $\int_0^\infty\!\int_x^\infty e^{-y}\,dy\,dx = \int_0^\infty e^{-x}\,dx=1$ | p.3; procedure |

## Double Integral with ln Bounds
| Front | Back | Notes |
| --- | --- | --- |
| Key move for $\int_1^e\int_0^{\ln x} 1\,dy\,dx$? | Inner integral over $y$ gives $\ln x$; then integrate $\int_1^e \ln x\,dx$ by parts ($u=\ln x$, $dv=dx$) to get $\big[x\ln x - x\big]_1^e = 1$ | p.4; procedure |

## Limit Definition of e to the x
| Front | Back | Notes |
| --- | --- | --- |
| Key move to show $\lim_{n\to\infty}(1+x/n)^n=e^x$? | Substitute $a=n/x$ so $n\to\infty \Rightarrow a\to\infty$; rewrite as $\left[\left(1+\frac{1}{a}\right)^a\right]^x \to e^x$ | p.6; procedure |

## Taylor Expansion of e to the x
| Front | Back | Notes |
| --- | --- | --- |
| Key move for the Taylor expansion of $f(x)=e^x$? | All derivatives of $e^x$ equal $e^x$, so $f^{(n)}(0)=1$ for every $n$, giving $e^x=1+x+\dfrac{x^2}{2!}+\dfrac{x^3}{3!}+\cdots$ | p.7; procedure |

## Taylor Expansion of e to the (-x)
| Front | Back | Notes |
| --- | --- | --- |
| Key move for the Taylor expansion of $f(x)=e^{-x}$? | Derivatives alternate sign ($f^{(n)}(0)=(-1)^n$), giving $e^{-x}=1-x+\dfrac{x^2}{2!}-\dfrac{x^3}{3!}+\cdots$ | p.7; procedure |

# Node map
```json
[
 {
  "name": "Geometric Series",
  "type": "concept",
  "existing": true,
  "parent": "Geometric Series",
  "prereqs": [
   "Limits"
  ],
  "uses": [],
  "page": 1,
  "summary": "The finite sum $1+x+\\cdots+x^n$ equals $(1-x^{n+1})/(1-x)$ for $x\\neq1$, and the infinite sum equals $1/(1-x)$ for $|x|<1$."
 },
 {
  "name": "Term-by-Term Differentiation of Series",
  "type": "concept",
  "existing": false,
  "parent": "Geometric Series",
  "prereqs": [
   "Geometric Series",
   "Derivatives"
  ],
  "uses": [],
  "page": 2,
  "summary": "Differentiating both sides of a convergent power series with respect to $x$ produces the series for $\\sum n a_n x^{n-1}$ and its closed form."
 },
 {
  "name": "Integration By Parts",
  "type": "concept",
  "existing": true,
  "parent": "Integration",
  "prereqs": [
   "Integrals"
  ],
  "uses": [],
  "page": 2,
  "summary": "For products of two functions, $\\int_a^b u\\,dv = [uv]_a^b - \\int_a^b v\\,du$."
 },
 {
  "name": "Double Integrals",
  "type": "concept",
  "existing": false,
  "parent": "Integration",
  "prereqs": [
   "Integrals"
  ],
  "uses": [],
  "page": 2,
  "summary": "A double integral is evaluated as two nested single integrations, integrating one variable at a time while holding the other fixed."
 },
 {
  "name": "Order of Integration",
  "type": "concept",
  "existing": false,
  "parent": "Integration",
  "prereqs": [
   "Double Integrals"
  ],
  "uses": [],
  "page": 3,
  "summary": "The order of integration in a double integral can be swapped by sketching the region and rewriting the bounds accordingly."
 },
 {
  "name": "Fundamental Theorem of Calculus",
  "type": "concept",
  "existing": true,
  "parent": "Integration",
  "prereqs": [
   "Integrals",
   "Limits"
  ],
  "uses": [],
  "page": 4,
  "summary": "The derivative of the accumulated area function $\\int_a^x f(t)dt$ with respect to $x$ is $f(x)$."
 },
 {
  "name": "Extension of the FTC",
  "type": "concept",
  "existing": false,
  "parent": "Integration",
  "prereqs": [
   "Fundamental Theorem of Calculus",
   "Chain Rule"
  ],
  "uses": [],
  "page": 5,
  "summary": "When the upper bound of the integral is a function $g(x)$, $\\frac{d}{dx}\\int_a^{g(x)}f(t)dt = f(g(x))\\cdot g'(x)$, combining the FTC with the chain rule."
 },
 {
  "name": "Euler's Number",
  "type": "concept",
  "existing": true,
  "parent": "Limits",
  "prereqs": [
   "Limits"
  ],
  "uses": [],
  "page": 5,
  "summary": "Euler's number $e$ is defined by the limit $\\lim_{n\\to\\infty}(1+1/n)^n$, and more generally $\\lim_{n\\to\\infty}(1+x/n)^n = e^x$."
 },
 {
  "name": "Taylor Series",
  "type": "concept",
  "existing": true,
  "parent": "Taylor Series",
  "prereqs": [
   "Derivatives"
  ],
  "uses": [],
  "page": 6,
  "summary": "For a function infinitely differentiable at $0$, its Taylor series around $0$ is $p(x)=\\sum f^{(n)}(0)x^n/n!$, which approaches $f(x)$ as more terms are added."
 },
 {
  "name": "Weighted Geometric Series (n x to the (n-1))",
  "type": "problem",
  "existing": false,
  "parent": "Geometric Series",
  "prereqs": [],
  "uses": [
   "Geometric Series",
   "Term-by-Term Differentiation of Series"
  ],
  "page": 1,
  "summary": "Evaluating $S=1+2x+3x^2+\\cdots$ by differentiating the geometric series formula term by term."
 },
 {
  "name": "Integration by Parts, y e to the (-y)",
  "type": "problem",
  "existing": false,
  "parent": "Integration",
  "prereqs": [],
  "uses": [
   "Integration By Parts"
  ],
  "page": 2,
  "summary": "Evaluating $\\int_0^\\infty ye^{-y}dy=1$ using integration by parts."
 },
 {
  "name": "Double Integral, e to the (-y) over a Triangle",
  "type": "problem",
  "existing": false,
  "parent": "Integration",
  "prereqs": [],
  "uses": [
   "Double Integrals"
  ],
  "page": 3,
  "summary": "Evaluating $\\int_0^\\infty\\int_0^y e^{-y}dx\\,dy=1$ by integrating over $x$ first."
 },
 {
  "name": "Changing Order of Integration, e to the (-y) over a Triangle",
  "type": "problem",
  "existing": false,
  "parent": "Integration",
  "prereqs": [],
  "uses": [
   "Order of Integration",
   "Double Integrals"
  ],
  "page": 3,
  "summary": "Re-evaluating the same double integral by swapping the order of integration and sketching the region."
 },
 {
  "name": "Double Integral with ln Bounds",
  "type": "problem",
  "existing": false,
  "parent": "Integration",
  "prereqs": [],
  "uses": [
   "Double Integrals",
   "Order of Integration",
   "Integration By Parts"
  ],
  "page": 4,
  "summary": "Evaluating $\\int_1^e\\int_0^{\\ln x}1\\,dy\\,dx=1$ both directly and by swapping the order of integration."
 },
 {
  "name": "Limit Definition of e to the x",
  "type": "problem",
  "existing": false,
  "parent": "Limits",
  "prereqs": [],
  "uses": [
   "Euler's Number"
  ],
  "page": 6,
  "summary": "Showing $\\lim_{n\\to\\infty}(1+x/n)^n=e^x$ via substitution into the definition of $e$."
 },
 {
  "name": "Taylor Expansion of e to the x",
  "type": "problem",
  "existing": false,
  "parent": "Taylor Series",
  "prereqs": [],
  "uses": [
   "Taylor Series"
  ],
  "page": 7,
  "summary": "Deriving $e^x=1+x+x^2/2!+x^3/3!+\\cdots$ since every derivative of $e^x$ at $0$ is $1$."
 },
 {
  "name": "Taylor Expansion of e to the (-x)",
  "type": "problem",
  "existing": false,
  "parent": "Taylor Series",
  "prereqs": [],
  "uses": [
   "Taylor Series"
  ],
  "page": 7,
  "summary": "Deriving $e^{-x}=1-x+x^2/2!-x^3/3!+\\cdots$ using alternating-sign derivatives at $0$."
 }
]
```

# Frankenstein problems

**Problem 1.** Find the Taylor series of $f(x) = \dfrac{1}{(1-x)^2}$ around $0$ two ways: (a) by differentiating the geometric series term by term, and (b) by directly computing derivatives and applying the Taylor series formula. Confirm the two answers agree.

*Concepts tested:* Geometric Series, Term-by-Term Differentiation of Series, Taylor Series.

*Solution.*

(a) Start from $\dfrac{1}{1-x} = 1+x+x^2+x^3+\cdots$ for $\lvert x\rvert<1$. Differentiate both sides with respect to $x$:
$$\frac{1}{(1-x)^2} = 1+2x+3x^2+4x^3+\cdots = \sum_{n=0}^{\infty}(n+1)x^n.$$

(b) Let $f(x)=(1-x)^{-2}$. Compute derivatives using the chain rule:
$f(x)=(1-x)^{-2}$, so $f(0)=1$.
$f'(x)=2(1-x)^{-3}$, so $f'(0)=2$.
$f''(x)=6(1-x)^{-4}$, so $f''(0)=6$.
$f'''(x)=24(1-x)^{-5}$, so $f'''(0)=24$.
The pattern is $f^{(n)}(0)=(n+1)!$ (check: $1=1!$, $2=2!$, $6=3!$, $24=4!$). The Taylor coefficient of $x^n$ is
$$\frac{f^{(n)}(0)}{n!} = \frac{(n+1)!}{n!} = n+1.$$
So $p(x) = \sum_{n=0}^{\infty}(n+1)x^n = 1+2x+3x^2+4x^3+\cdots$.

Both methods give $\dfrac{1}{(1-x)^2}=1+2x+3x^2+4x^3+\cdots$, confirming agreement.

---

**Problem 2.** Evaluate $I = \displaystyle\int_0^1\int_0^x y e^{-x}\,dy\,dx$ by changing the order of integration, then verify by evaluating the original iterated integral directly.

*Concepts tested:* Double Integrals, Order of Integration, Integration By Parts.

*Solution.*

The region is $0\le y\le x\le 1$, a triangle. Swapping the order (integrate $x$ first, for fixed $y\in[0,1]$, $x$ ranges from $y$ to $1$):
$$I = \int_0^1\int_y^1 y e^{-x}\,dx\,dy = \int_0^1 y\big[-e^{-x}\big]_y^1\,dy = \int_0^1 y\left(e^{-y}-e^{-1}\right)dy = \int_0^1 y e^{-y}\,dy \; - \; e^{-1}\int_0^1 y\,dy.$$

For $\int_0^1 y e^{-y}\,dy$, use integration by parts with $u=y$, $dv=e^{-y}dy$, so $du=dy$, $v=-e^{-y}$:
$$\int_0^1 y e^{-y}\,dy = \big[-ye^{-y}\big]_0^1 - \int_0^1(-e^{-y})\,dy = -e^{-1} + \big[-e^{-y}\big]_0^1 = -e^{-1} + \left(-e^{-1}+1\right) = 1-2e^{-1}.$$

Also $\int_0^1 y\,dy = \tfrac{1}{2}$, so $e^{-1}\int_0^1 y\,dy = \tfrac{1}{2}e^{-1}$.

Therefore
$$I = \left(1-2e^{-1}\right) - \tfrac{1}{2}e^{-1} = 1 - \tfrac{5}{2}e^{-1} = 1-\frac{5}{2e}.$$

*Verification (original order):* Inner integral over $y$ from $0$ to $x$: $\int_0^x y e^{-x}\,dy = e^{-x}\cdot\tfrac{x^2}{2}$. So $I=\tfrac{1}{2}\int_0^1 x^2 e^{-x}\,dx$. Using integration by parts twice, $\int x^2 e^{-x}\,dx = -e^{-x}(x^2+2x+2)+C$. Evaluating from $0$ to $1$: at $x=1$, $-e^{-1}(1+2+2)=-5e^{-1}$; at $x=0$, $-1\cdot(0+0+2)=-2$. Difference: $-5e^{-1}-(-2)=2-5e^{-1}$. So $I=\tfrac12(2-5e^{-1}) = 1-\tfrac{5}{2}e^{-1}$, matching the first method exactly.
