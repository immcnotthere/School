---
type: reference
parent: "[[STATS 131]]"
domain: stats
course: "STATS 131"
status: draft
source: "Notes_07"
tags:
  - decks
---
# STATS 131 Cards - Notes_07 Expectation

## Expectation of a Discrete Random Variable
| Front | Back | Notes |
| --- | --- | --- |
| What is the formula for $\mathbb{E}[X]$ for a discrete random variable $X$? | $\mathbb{E}[X] = \sum_x x \cdot P(X=x) = \sum_x x f(x)$ | p.1; formula |
| What condition must hold for $\mathbb{E}[X]$ to exist for a discrete random variable? | The sum $\sum_x x f(x)$ must be finite (converge) | p.1; definition |
| What is another name for $\mathbb{E}[X]$? | The mean of the distribution | p.1; definition |

## Expectation of a Continuous Random Variable
| Front | Back | Notes |
| --- | --- | --- |
| What is the formula for $\mathbb{E}[X]$ for a continuous random variable $X$ with pdf $f(x)$? | $\mathbb{E}[X] = \displaystyle\int_{-\infty}^{\infty} x f(x)\,dx$ | p.2; formula |
| What condition must hold for $\mathbb{E}[X]$ to exist for a continuous random variable? | The integral $\int x f(x)\,dx$ must be finite | p.2; definition |
| How does computing $\mathbb{E}[X]$ differ for a discrete vs a continuous random variable? | Discrete: sum $\sum_x xf(x)$ over the pmf; continuous: integral $\int xf(x)\,dx$ over the pdf | p.1 to p.2; discrimination |

## Law of the unconscious statistician
| Front | Back | Notes |
| --- | --- | --- |
| What does LOTUS let you compute without first finding the distribution of $h(X)$? | $\mathbb{E}[h(X)]$, directly from the distribution of $X$ | p.3; definition |
| LOTUS formula for discrete $X$ and function $h(\cdot)$? | $\mathbb{E}[h(X)] = \sum_x h(x)f(x)$, if the sum is finite | p.3; formula |
| LOTUS formula for continuous $X$ and function $h(\cdot)$? | $\mathbb{E}[h(X)] = \displaystyle\int_{-\infty}^{\infty} h(x)f(x)\,dx$, if the integral is finite | p.3; formula |

## Bivariate LOTUS
| Front | Back | Notes |
| --- | --- | --- |
| Bivariate LOTUS formula for discrete $X, Y$ and function $h(\cdot)$? | $\mathbb{E}[h(X,Y)] = \sum_x\sum_y h(x,y)f(x,y)$, if the sum is finite | p.5; formula |
| Bivariate LOTUS formula for continuous $X, Y$ and function $h(\cdot)$? | $\mathbb{E}[h(X,Y)] = \displaystyle\int_{-\infty}^{\infty}\int_{-\infty}^{\infty} h(x,y)f(x,y)\,dx\,dy$, if the integral is finite | p.5; formula |
| What extra information do you need to use bivariate LOTUS that univariate LOTUS doesn't require? | The joint pmf or pdf $f(x,y)$ of both variables together, not just their marginals | p.5; discrimination |

## Linearity of Expectation
| Front | Back | Notes |
| --- | --- | --- |
| $\mathbb{E}[aX+b] = ?$ | $a\,\mathbb{E}[X] + b$ | p.6; formula |
| $\mathbb{E}\left[\sum_{i=1}^n a_iX_i + b_i\right] = ?$ | $\sum_{i=1}^n \left(a_i\,\mathbb{E}[X_i] + b_i\right)$ | p.6; formula |
| Yes or no, and why: does linearity of expectation require $X_1,\dots,X_n$ to be independent? | No, linearity holds for any random variables, independent or not | p.6; discrimination |

## Expectation of Independent Random Variables
| Front | Back | Notes |
| --- | --- | --- |
| For independent $X_1,\dots,X_n$, $\mathbb{E}\left[\prod_{i=1}^n X_i\right] = ?$ | $\prod_{i=1}^n \mathbb{E}[X_i]$ | p.6; formula |
| For independent $X$ and $Y$, $\mathbb{E}[XY] = ?$ | $\mathbb{E}[X]\cdot \mathbb{E}[Y]$ | p.7; formula |
| Yes or no, and why: if $\mathbb{E}[XY]=\mathbb{E}[X]\mathbb{E}[Y]$, does that mean $X$ and $Y$ are independent? | No, the product rule can hold even when $X$ and $Y$ are dependent | p.7; discrimination |

## Expected Values of Common Distributions
| Front | Back | Notes |
| --- | --- | --- |
| $X \sim \text{Bernoulli}(p)$: $\mathbb{E}[X] = ?$ | $p$ | p.1; formula |
| $X \sim \text{Poisson}(\lambda)$: $\mathbb{E}[X] = ?$ | $\lambda$ | p.2; formula |
| $X \sim \text{Uniform}(a,b)$: $\mathbb{E}[X] = ?$ | $\dfrac{a+b}{2}$ | p.3; formula |
| $X \sim \text{Exponential}(\lambda)$: $\mathbb{E}[X] = ?$ | $\dfrac{1}{\lambda}$ | p.3; formula |
| $X \sim \text{Binomial}(n,p)$: $\mathbb{E}[X] = ?$ | $np$ | p.6; formula |

## Bernoulli Expectation Derivation
| Front | Back | Notes |
| --- | --- | --- |
| Derive $\mathbb{E}[X]$ for $X\sim\text{Bernoulli}(p)$ from the definition. | $\mathbb{E}[X]=\sum_x xP(X=x) = 0(1-p) + 1(p) = p$ | p.1; procedure |

## Startup Investment Decision
| Front | Back | Notes |
| --- | --- | --- |
| Startup A: 10% chance of +\$10,000,000, 90% chance of -\$1,000,000. Startup B: 50% chance of +\$1,000,000, 50% chance of -\$500,000. Which has the higher expected value? | Startup B: $E[B]=1{,}000{,}000(0.5)+(-500{,}000)(0.5)=\$250{,}000$ beats $E[A]=10{,}000{,}000(0.1)+(-1{,}000{,}000)(0.9)=\$100{,}000$ | p.1; procedure |

## Disk Failure Time
| Front | Back | Notes |
| --- | --- | --- |
| Disk fails w.p. $1/3$ each year; $X$ = years until failure, $f(x)=\frac13\left(1-\frac13\right)^{x-1}$. Key move to evaluate $\mathbb{E}[X]=\frac13\sum_{x\ge1} x(2/3)^{x-1}$? | Recognize the power-series identity $\sum_{x\ge1} xr^{x-1}=1/(1-r)^2$ with $r=2/3$, giving $\mathbb{E}[X]=\frac13\cdot\frac{1}{(1/3)^2}=3$ | p.2; procedure |

## Poisson Expectation Derivation
| Front | Back | Notes |
| --- | --- | --- |
| Key algebra trick to derive $\mathbb{E}[X]=\lambda$ for $X\sim\text{Poisson}(\lambda)$ from $\sum_{x=0}^\infty x\frac{e^{-\lambda}\lambda^x}{x!}$? | Drop the $x=0$ term, cancel one $x$ into $x!=x(x-1)!$, factor out $\lambda e^{-\lambda}$, then re-index $k=x-1$ so the sum becomes $\sum_k \lambda^k/k!=e^\lambda$, leaving $\mathbb{E}[X]=\lambda$ | p.2; procedure |

## Divergent Expectation Example
| Front | Back | Notes |
| --- | --- | --- |
| $X$ has pmf $f(x)=\frac{6}{\pi^2x^2}$ for $x=1,2,3,\dots$. Why does $\mathbb{E}[X]$ not exist? | $\mathbb{E}[X]=\frac{6}{\pi^2}\sum_{x=1}^\infty \frac1x$, the harmonic series, which diverges to infinity | p.2; definition |

## Uniform Expectation Derivation
| Front | Back | Notes |
| --- | --- | --- |
| Key move to get $\mathbb{E}[X]=\frac{a+b}{2}$ for $X\sim\text{Uniform}(a,b)$? | Integrate $\int_a^b x\cdot\frac{1}{b-a}\,dx=\frac{x^2}{2(b-a)}\Big\vert_a^b=\frac{(b-a)(b+a)}{2(b-a)}=\frac{a+b}{2}$ | p.3; procedure |

## Exponential Expectation Derivation
| Front | Back | Notes |
| --- | --- | --- |
| Key technique to find $\mathbb{E}[X]=\int_0^\infty x\lambda e^{-\lambda x}\,dx$ for $X\sim\text{Exponential}(\lambda)$? | Integration by parts with $u=\lambda x$, $dv=e^{-\lambda x}dx$, which gives $\mathbb{E}[X]=1/\lambda$ | p.3; procedure |

## Expected Volume of a Sphere
| Front | Back | Notes |
| --- | --- | --- |
| $R$ takes values $1,2,3$ each w.p. $1/3$. Key move to find $\mathbb{E}[\text{Volume}]=\mathbb{E}\left[\frac43\pi R^3\right]$? | Apply LOTUS with $h(r)=\frac43\pi r^3$: $\mathbb{E}[\text{Volume}]=\frac13\left(\frac43\pi(1^3+2^3+3^3)\right)=16\pi$ | p.4; procedure |

## Direct Computation of E(X) and E(2X to the 2+3)
| Front | Back | Notes |
| --- | --- | --- |
| $P(X=0)=0.2$, $P(X=1)=0.5$, $P(X=2)=0.3$. Find $\mathbb{E}[X]$ and $\mathbb{E}[2X^2+3]$. | $\mathbb{E}[X]=0(0.2)+1(0.5)+2(0.3)=1.1$; by LOTUS $\mathbb{E}[2X^2+3]=3(0.2)+5(0.5)+11(0.3)=6.4$ | p.4; procedure |

## Uniform Second Moment via LOTUS
| Front | Back | Notes |
| --- | --- | --- |
| Key move to find $\mathbb{E}[X^2]$ for $X\sim\text{Uniform}(a,b)$ by LOTUS? | $\mathbb{E}[X^2]=\int_a^b x^2\cdot\frac{1}{b-a}\,dx=\frac{b^3-a^3}{3(b-a)}=\frac{a^2+ab+b^2}{3}$ | p.4; procedure |

## Expected Time to Failure via Transformation
| Front | Back | Notes |
| --- | --- | --- |
| $X$ has pdf $f(x)=3x^2$ on $(0,1)$; find $\mathbb{E}[Y]$ for $Y=1/X$, two ways. | LOTUS directly: $\mathbb{E}[1/X]=\int_0^1 3x\,dx=3/2$. Or find $F_Y(y)=1-(1/y)^3$ for $y>1$, differentiate to $f_Y(y)=3y^{-4}$, then $\int_1^\infty y\cdot3y^{-4}\,dy=3/2$ | p.5; procedure |

## Expected Area of a Random Rectangle
| Front | Back | Notes |
| --- | --- | --- |
| $(X,Y)$ uniform on $[0,1]^2$; find $\mathbb{E}[XY]$ using bivariate LOTUS. | $\mathbb{E}[XY]=\int_0^1\int_0^1 xy\cdot1\,dx\,dy=\int_0^1 \frac{y}{2}\,dy=\frac14$ | p.5; procedure |

## Binomial Expectation via Linearity
| Front | Back | Notes |
| --- | --- | --- |
| Key move to find $\mathbb{E}[X]=np$ for $X\sim\text{Binomial}(n,p)$ using linearity? | Write $X=X_1+\cdots+X_n$ with $X_i\sim\text{Bernoulli}(p)$, then $\mathbb{E}[X]=\sum \mathbb{E}[X_i]=np$ by linearity, with no independence needed | p.6; procedure |

## Cup Matching Problem
| Front | Back | Notes |
| --- | --- | --- |
| $n$ people grab a random cup; $X$ = number who get their own cup. Key move to find $\mathbb{E}[X]$, and does it depend on $n$? | Let $Z_i=1$ if person $i$ gets their own cup ($P=1/n$), else 0; by linearity $\mathbb{E}[X]=\sum \mathbb{E}[Z_i]=n\cdot\frac1n=1$, independent of $n$ | p.6; procedure |

## Product Rule Without Independence
| Front | Back | Notes |
| --- | --- | --- |
| Give a counterexample showing $\mathbb{E}[XY]=\mathbb{E}[X]\mathbb{E}[Y]$ does not imply $X,Y$ independent. | $X\in\{-1,0,1\}$ each w.p. $1/3$, $Y=X^2$: $P(X=1,Y=1)=1/3\ne P(X=1)P(Y=1)$, so dependent, yet $\mathbb{E}[XY]=\mathbb{E}[X^3]=0=\mathbb{E}[X]\mathbb{E}[Y]$ | p.7; procedure |
# Node map
```json
[
 {
  "name": "Expectation of a Discrete Random Variable",
  "type": "concept",
  "existing": false,
  "parent": "Expectation and Variance",
  "prereqs": [
   "Probability distribution"
  ],
  "uses": [],
  "page": 1,
  "summary": "For a discrete random variable $X$, the expectation (mean) is $\\mathbb{E}[X]=\\sum_x xP(X=x)$, provided the sum converges."
 },
 {
  "name": "Expectation of a Continuous Random Variable",
  "type": "concept",
  "existing": false,
  "parent": "Expectation and Variance",
  "prereqs": [
   "Expectation of a Discrete Random Variable",
   "Probability density function"
  ],
  "uses": [],
  "page": 2,
  "summary": "For a continuous random variable $X$ with pdf $f(x)$, $\\mathbb{E}[X]=\\int_{-\\infty}^{\\infty} xf(x)\\,dx$, provided the integral converges."
 },
 {
  "name": "Law of the unconscious statistician",
  "type": "concept",
  "existing": true,
  "parent": "Expectation and Variance",
  "prereqs": [
   "Expectation of a Discrete Random Variable",
   "Expectation of a Continuous Random Variable"
  ],
  "uses": [],
  "page": 3,
  "summary": "LOTUS lets you compute $\\mathbb{E}[h(X)]$ directly from the distribution of $X$, without first finding the distribution of $h(X)$."
 },
 {
  "name": "Bivariate LOTUS",
  "type": "concept",
  "existing": false,
  "parent": "Expectation and Variance",
  "prereqs": [
   "Law of the unconscious statistician",
   "Joint probability distribution"
  ],
  "uses": [],
  "page": 5,
  "summary": "Extends LOTUS to two random variables: $\\mathbb{E}[h(X,Y)]$ computed as a sum or double integral against the joint pmf/pdf $f(x,y)$."
 },
 {
  "name": "Linearity of Expectation",
  "type": "concept",
  "existing": false,
  "parent": "Expectation and Variance",
  "prereqs": [
   "Expectation of a Discrete Random Variable"
  ],
  "uses": [],
  "page": 6,
  "summary": "Expectation is linear: $\\mathbb{E}[aX+b]=a\\mathbb{E}[X]+b$, and this extends to sums of many random variables, with no independence required."
 },
 {
  "name": "Expectation of Independent Random Variables",
  "type": "concept",
  "existing": false,
  "parent": "Expectation and Variance",
  "prereqs": [
   "Linearity of Expectation"
  ],
  "uses": [],
  "page": 6,
  "summary": "If $X_1,\\dots,X_n$ are independent, $\\mathbb{E}[\\prod X_i]=\\prod \\mathbb{E}[X_i]$; the converse does not hold in general."
 },
 {
  "name": "Expected Values of Common Distributions",
  "type": "concept",
  "existing": false,
  "parent": "Expectation and Variance",
  "prereqs": [
   "Expectation of a Discrete Random Variable",
   "Expectation of a Continuous Random Variable",
   "Common Distributions"
  ],
  "uses": [],
  "page": 1,
  "summary": "Standard results: $\\mathbb{E}[X]=p$ for Bernoulli(p), $\\lambda$ for Poisson($\\lambda$), $(a+b)/2$ for Uniform(a,b), $1/\\lambda$ for Exponential($\\lambda$), and $np$ for Binomial(n,p)."
 },
 {
  "name": "Bernoulli Expectation Derivation",
  "type": "problem",
  "existing": false,
  "parent": "Expectation and Variance",
  "prereqs": [],
  "uses": [
   "Expectation of a Discrete Random Variable",
   "Expected Values of Common Distributions"
  ],
  "page": 1,
  "summary": "Derives $E[X]=p$ for $X\\sim\\text{Bernoulli}(p)$ directly from the discrete expectation definition."
 },
 {
  "name": "Startup Investment Decision",
  "type": "problem",
  "existing": false,
  "parent": "Expectation and Variance",
  "prereqs": [],
  "uses": [
   "Expectation of a Discrete Random Variable"
  ],
  "page": 1,
  "summary": "Compares two risky startup investments by computing and comparing their expected dollar payoffs."
 },
 {
  "name": "Disk Failure Time",
  "type": "problem",
  "existing": false,
  "parent": "Expectation and Variance",
  "prereqs": [],
  "uses": [
   "Expectation of a Discrete Random Variable",
   "Expected Values of Common Distributions"
  ],
  "page": 2,
  "summary": "Finds the expected number of years until a disk fails by summing a geometric-type power series."
 },
 {
  "name": "Poisson Expectation Derivation",
  "type": "problem",
  "existing": false,
  "parent": "Expectation and Variance",
  "prereqs": [],
  "uses": [
   "Expectation of a Discrete Random Variable",
   "Expected Values of Common Distributions"
  ],
  "page": 2,
  "summary": "Derives $E[X]=\\lambda$ for a Poisson($\\lambda$) random variable via series manipulation and re-indexing."
 },
 {
  "name": "Divergent Expectation Example",
  "type": "problem",
  "existing": false,
  "parent": "Expectation and Variance",
  "prereqs": [],
  "uses": [
   "Expectation of a Discrete Random Variable"
  ],
  "page": 2,
  "summary": "Shows a pmf $f(x)=6/(\\pi^2x^2)$ for which $E[X]$ does not exist because the resulting sum is the divergent harmonic series."
 },
 {
  "name": "Uniform Expectation Derivation",
  "type": "problem",
  "existing": false,
  "parent": "Expectation and Variance",
  "prereqs": [],
  "uses": [
   "Expectation of a Continuous Random Variable",
   "Expected Values of Common Distributions"
  ],
  "page": 3,
  "summary": "Derives $E[X]=(a+b)/2$ for $X\\sim\\text{Uniform}(a,b)$ by direct integration."
 },
 {
  "name": "Exponential Expectation Derivation",
  "type": "problem",
  "existing": false,
  "parent": "Expectation and Variance",
  "prereqs": [],
  "uses": [
   "Expectation of a Continuous Random Variable",
   "Expected Values of Common Distributions"
  ],
  "page": 3,
  "summary": "Derives $E[X]=1/\\lambda$ for $X\\sim\\text{Exponential}(\\lambda)$ using integration by parts."
 },
 {
  "name": "Expected Volume of a Sphere",
  "type": "problem",
  "existing": false,
  "parent": "Expectation and Variance",
  "prereqs": [],
  "uses": [
   "Law of the unconscious statistician"
  ],
  "page": 4,
  "summary": "Applies LOTUS with $h(r)=\\frac43\\pi r^3$ to find the expected volume of a sphere with random integer radius."
 },
 {
  "name": "Direct Computation of E(X) and E(2X to the 2+3)",
  "type": "problem",
  "existing": false,
  "parent": "Expectation and Variance",
  "prereqs": [],
  "uses": [
   "Expectation of a Discrete Random Variable",
   "Law of the unconscious statistician"
  ],
  "page": 4,
  "summary": "Computes $E[X]$ and $E[2X^2+3]$ for a simple three-point discrete distribution."
 },
 {
  "name": "Uniform Second Moment via LOTUS",
  "type": "problem",
  "existing": false,
  "parent": "Expectation and Variance",
  "prereqs": [],
  "uses": [
   "Law of the unconscious statistician",
   "Expected Values of Common Distributions"
  ],
  "page": 4,
  "summary": "Uses LOTUS to find $E[X^2]=(a^2+ab+b^2)/3$ for $X\\sim\\text{Uniform}(a,b)$."
 },
 {
  "name": "Expected Time to Failure via Transformation",
  "type": "problem",
  "existing": false,
  "parent": "Expectation and Variance",
  "prereqs": [],
  "uses": [
   "Law of the unconscious statistician"
  ],
  "page": 5,
  "summary": "Finds $E[1/X]$ for $X$ with pdf $3x^2$ on $(0,1)$ both directly via LOTUS and via the CDF of the transformed variable."
 },
 {
  "name": "Expected Area of a Random Rectangle",
  "type": "problem",
  "existing": false,
  "parent": "Expectation and Variance",
  "prereqs": [],
  "uses": [
   "Bivariate LOTUS"
  ],
  "page": 5,
  "summary": "Uses bivariate LOTUS to find $E[XY]=1/4$ for $(X,Y)$ uniform on the unit square."
 },
 {
  "name": "Binomial Expectation via Linearity",
  "type": "problem",
  "existing": false,
  "parent": "Expectation and Variance",
  "prereqs": [],
  "uses": [
   "Linearity of Expectation",
   "Expected Values of Common Distributions"
  ],
  "page": 6,
  "summary": "Writes a Binomial(n,p) variable as a sum of n iid Bernoulli(p) variables to get $E[X]=np$ by linearity."
 },
 {
  "name": "Cup Matching Problem",
  "type": "problem",
  "existing": false,
  "parent": "Expectation and Variance",
  "prereqs": [],
  "uses": [
   "Linearity of Expectation"
  ],
  "page": 6,
  "summary": "Uses indicator variables and linearity to show the expected number of people who pick their own cup at random is 1, regardless of n."
 },
 {
  "name": "Product Rule Without Independence",
  "type": "problem",
  "existing": false,
  "parent": "Expectation and Variance",
  "prereqs": [],
  "uses": [
   "Expectation of Independent Random Variables"
  ],
  "page": 7,
  "summary": "Constructs a dependent pair X, Y=X^2 that still satisfies E[XY]=E[X]E[Y], showing the product rule doesn't imply independence."
 }
]
```

# Frankenstein problems

**Frankenstein Problem 1.** A quality-control station tests $n=4$ independent components; each is defective independently with probability $p=0.1$. Let $X = X_1+X_2+X_3+X_4$ be the number of defective components, where $X_i\sim\text{Bernoulli}(0.1)$. The inspection cost is $C = 50X + 20$ dollars. Each defective component $i$ independently requires a repair time $Y_i\sim\text{Uniform}(5,15)$ minutes (repair time is 0 if the component is not defective, i.e. define $T_i = X_iY_i$ with $Y_i$ independent of $X_i$), and total repair time is $T = T_1+T_2+T_3+T_4$. Find $\mathbb{E}[C]$ and $\mathbb{E}[T]$.

*Solution.* By linearity, $\mathbb{E}[X]=\sum_{i=1}^4 \mathbb{E}[X_i] = 4(0.1) = 0.4$ (this is the Binomial(4,0.1) mean, $np=0.4$). Then $\mathbb{E}[C]=\mathbb{E}[50X+20]=50(0.4)+20=20+20=40$ dollars.

For $T$: since $X_i$ and $Y_i$ are independent, $\mathbb{E}[T_i]=\mathbb{E}[X_i]\mathbb{E}[Y_i]$. $\mathbb{E}[X_i]=p=0.1$ (Bernoulli mean) and $\mathbb{E}[Y_i]=(5+15)/2=10$ (Uniform mean), so $\mathbb{E}[T_i]=0.1(10)=1$. By linearity, $\mathbb{E}[T]=\sum_{i=1}^4 \mathbb{E}[T_i]=4(1)=4$ minutes.

Concepts tested: Linearity of Expectation, Expectation of Independent Random Variables, Expected Values of Common Distributions (Bernoulli and Uniform means), Expectation of a Discrete Random Variable.

**Frankenstein Problem 2.** Let $X\sim\text{Poisson}(2)$ count typos on a page, and let $(U,V)$ be independent of $X$ and uniformly distributed on the square $[0,1]^2$. Define the cost $H = XUV + 3$ dollars. Find $\mathbb{E}[H]$.

*Solution.* First, $\mathbb{E}[UV]$: by bivariate LOTUS with $h(u,v)=uv$ and joint density $f(u,v)=1$ on $[0,1]^2$, $\mathbb{E}[UV]=\int_0^1\int_0^1 uv\,du\,dv = \left(\int_0^1 u\,du\right)\left(\int_0^1 v\,dv\right) = \frac12\cdot\frac12=\frac14$.

Since $X$ is independent of the pair $(U,V)$, $\mathbb{E}[XUV]=\mathbb{E}[X]\cdot\mathbb{E}[UV]$. For $X\sim\text{Poisson}(2)$, $\mathbb{E}[X]=\lambda=2$. So $\mathbb{E}[XUV]=2\cdot\frac14=0.5$.

By linearity, $\mathbb{E}[H]=\mathbb{E}[XUV]+3=0.5+3=3.5$ dollars.

Concepts tested: Bivariate LOTUS, Expectation of Independent Random Variables, Expected Values of Common Distributions (Poisson mean), Linearity of Expectation.
