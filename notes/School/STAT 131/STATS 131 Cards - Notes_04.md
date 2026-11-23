---
type: reference
parent: "[[STATS 131]]"
domain: stats
course: "STATS 131"
status: draft
source: "Notes_04"
tags:
  - decks
---
# STATS 131 Cards - Notes_04 Continuous Random Variables and CDFs

## Probability density function
| Front | Back | Notes |
| --- | --- | --- |
| What is the probability density function (pdf) of a continuous random variable X? | A non-negative function $f(x)$ such that $P(a \le X \le b) = \int_a^b f(x)\,dx$, with $\int_{-\infty}^{\infty} f(x)\,dx = 1$ (the unity property). | p.1; definition |
| For a continuous random variable X, what is $P(X=a)$, even if $f(a)>0$? | $P(X=a)=0$; probability density is not the same thing as probability. | p.1; discrimination |
| For a continuous random variable X, how do you find $P(E)$ for an event E in terms of the pdf? | $P(E) = \int_{x \in E} f(x)\,dx$ | p.1; formula |

## Support (Probability)
| Front | Back | Notes |
| --- | --- | --- |
| What is the support of a continuous random variable X? | The set $\{x : f(x) > 0\}$, i.e., all values where the pdf is strictly positive. | p.2; definition |
| What is the difference between the support of X and the value $P(X=a)$ for a single point a? | The support describes the range of possible values (where $f(x)>0$); $P(X=a)=0$ for any single point since X is continuous. | p.2; discrimination |

## Normalizing Constant
| Front | Back | Notes |
| --- | --- | --- |
| In $f(x) = c \cdot g(x)$, what is c called? | The normalizing constant. | p.2; definition |
| How do you solve for the normalizing constant c of a pdf $f(x)=c\cdot g(x)$? | Set $\int_{-\infty}^{\infty} c\cdot g(x)\,dx = 1$ (the unity property) and solve for c. | p.3; procedure |
| What does the notation $f(x) \propto g(x)$ mean? | f(x) is proportional to g(x); that is, $f(x) = c \cdot g(x)$ for some unknown constant c. | p.2; definition |

## Uniform Distribution (Continuous)
| Front | Back | Notes |
| --- | --- | --- |
| What is the pdf of a continuous random variable X that is uniform on $[a,b]$? | $f(x) = \dfrac{1}{b-a}$ for $a \le x \le b$, and 0 otherwise. | p.4; definition |
| How do you verify $\int_{-\infty}^{\infty} f(x)\,dx = 1$ for a uniform distribution on $[a,b]$? | $\int_a^b \frac{1}{b-a}\,dx = \frac{x}{b-a}\Big\vert _a^b = \frac{b-a}{b-a} = 1$. | p.4; procedure |
| What is $F(x)$ for a uniform distribution on $[a,b]$, for $a \le x \le b$? | $F(x) = \dfrac{x-a}{b-a}$. | p.4; formula |

## Exponential Distribution
| Front | Back | Notes |
| --- | --- | --- |
| What is the pdf of an exponential distribution with rate $\lambda$? | $f(x) = \lambda e^{-\lambda x}$ for $x \ge 0$, and 0 otherwise. | p.4; definition |
| How do you verify $\int_0^{\infty} \lambda e^{-\lambda x}\,dx = 1$? | $\lambda \int_0^{\infty} e^{-\lambda x}\,dx = \lambda\left[-\frac{1}{\lambda}e^{-\lambda x}\right]_0^{\infty} = \lambda\left(0-\left(-\frac1\lambda\right)\right)=1$. | p.4; procedure |
| What is the CDF of an exponential distribution with rate $\lambda$? | $F(x) = 1 - e^{-\lambda x}$ for $x \ge 0$. | p.4; formula |
| What is the median of an exponential distribution with rate $\lambda$? | $\text{median} = \dfrac{\ln 2}{\lambda}$. | p.4; formula |

## Cumulative Distribution Function (CDF)
| Front | Back | Notes |
| --- | --- | --- |
| What is the CDF $F(x)$ of a random variable X, for any $x \in \mathbb{R}$? | $F(x) = P(X \le x)$. | p.6; definition |
| How is the CDF computed from a discrete pmf versus a continuous pdf? | Discrete: $F(x) = \sum_{x_i \le a} f(x_i)$, a sum over the pmf. Continuous: $F(x) = \int_{-\infty}^{a} f(x)\,dx$, an integral over the pdf. | p.6; discrimination |
| For a continuous random variable X, how do you recover the pdf $f(x)$ from the CDF $F(x)$? | $f(x) = \dfrac{d}{dx}F(x)$, by the Fundamental Theorem of Calculus. | p.7; formula |
| If you know the CDF $F(x)$, how do you find $P(X>a)$? | $P(X>a) = 1 - F(a)$. | p.6; formula |

## Properties of CDFs
| Front | Back | Notes |
| --- | --- | --- |
| What happens to $F(x)$ as $x \to -\infty$ and as $x \to \infty$? | $\lim_{x\to-\infty}F(x)=0$ and $\lim_{x\to\infty}F(x)=1$. | p.8; concept |
| How does $F(x)$ behave as x increases (monotonicity)? | $F(x)$ is non-decreasing: $F(x_1)\le F(x_2)$ whenever $x_1<x_2$. | p.8; concept |
| For $x_1 < x_2$, how do you express $P(x_1 < X \le x_2)$ using the CDF? | $P(x_1 < X \le x_2) = F(x_2) - F(x_1)$. | p.8; formula |

## Quantile Function
| Front | Back | Notes |
| --- | --- | --- |
| What is the p-quantile (the $100p$th percentile) of a random variable X with CDF $F(x)$? | $F^{-1}(p)$, the smallest value x such that $F(x) \ge p$, defined for $0<p<1$. | p.8; definition |
| What are the median, lower quartile, and upper quartile in terms of quantiles? | Median = 1/2 quantile (50th percentile); lower quartile = 1/4 quantile (25th percentile); upper quartile = 3/4 quantile (75th percentile). | p.8; discrimination |
| When X is continuous, what is the relationship between $F^{-1}$ and F? | $F^{-1}$ is the inverse function of F. | p.8; concept |
| How do you find the quantile function $F^{-1}(p)$ given $F(x)$? | Set $p = F(x)$ and solve for x in terms of p. | p.9; procedure |

## Two-Year-Old Weights (Support and Probability)
| Front | Back | Notes |
| --- | --- | --- |
| For the two-year-old weight pdf $f(x)=\frac{3}{40}-\frac{3}{4000}(x-25)^2$ on $[15,35]$, what is the key move to find $P(X>30)$? | Integrate the pdf from 30 to 35: $P(X>30)=\int_{30}^{35}\left(\frac{3}{40}-\frac{3}{4000}(x-25)^2\right)dx \approx 0.156$. | p.2; procedure |

## Normalizing Constant for f(x) proportional to e to the (-2x)
| Front | Back | Notes |
| --- | --- | --- |
| For $f(x)\propto e^{-2x}$ on $x>0$, what are the normalizing constant and $P(1<X<2)$? | $c=2$, since $\int_0^{\infty} c\,e^{-2x}dx = c/2=1$, so $f(x)=2e^{-2x}$; then $P(1<X<2)=\int_1^2 2e^{-2x}dx = e^{-2}-e^{-4}\approx 0.117$. | p.3; procedure |

## CDF of a Bernoulli Distribution
| Front | Back | Notes |
| --- | --- | --- |
| What is the CDF of a Bernoulli(p) random variable? | $F(x)=0$ for $x<0$; $F(x)=1-p$ for $0\le x<1$; $F(x)=1$ for $x\ge1$. | p.6; procedure |

## CDF of a Uniform(0,1) Distribution
| Front | Back | Notes |
| --- | --- | --- |
| What is the CDF of a Uniform[0,1] random variable, for $0\le x \le 1$? | $F(x)=x$ (with $F(x)=0$ for $x<0$ and $F(x)=1$ for $x>1$). | p.7; procedure |

## Identify Distribution from CDF (lambda=5)
| Front | Back | Notes |
| --- | --- | --- |
| If a random variable has CDF $F(x)=1-e^{-5x}$, what is its pdf and what distribution is this? | $f(x)=F'(x)=5e^{-5x}$; this is the exponential distribution with $\lambda=5$. | p.8; procedure |

## Quantile Function of Exponential (lambda=2)
| Front | Back | Notes |
| --- | --- | --- |
| For an exponential distribution with $\lambda=2$, what is the quantile function $F^{-1}(p)$ and the median? | $F^{-1}(p) = -\dfrac{\ln(1-p)}{2}$; median $=F^{-1}(0.5)=\dfrac{\ln 2}{2}\approx0.347$. | p.9; procedure |

# Node map
```json
[
 {
  "name": "Probability density function",
  "type": "concept",
  "existing": true,
  "parent": "Continuous Random Variables",
  "prereqs": [
   "Probability distribution"
  ],
  "uses": [],
  "page": 1,
  "summary": "A non-negative function $f(x)$ describing a continuous random variable, where $P(a\\le X\\le b)=\\int_a^b f(x)\\,dx$ and $\\int_{-\\infty}^{\\infty}f(x)\\,dx=1$."
 },
 {
  "name": "Support (Probability)",
  "type": "concept",
  "existing": false,
  "parent": "Continuous Random Variables",
  "prereqs": [
   "Probability density function"
  ],
  "uses": [],
  "page": 2,
  "summary": "The set of x values where a continuous random variable's pdf is strictly positive, $\\{x: f(x)>0\\}$."
 },
 {
  "name": "Normalizing Constant",
  "type": "concept",
  "existing": false,
  "parent": "Continuous Random Variables",
  "prereqs": [
   "Probability density function"
  ],
  "uses": [],
  "page": 2,
  "summary": "The constant c in $f(x)=c\\cdot g(x)$ that makes a pdf known only up to proportionality integrate to 1."
 },
 {
  "name": "Uniform Distribution (Continuous)",
  "type": "concept",
  "existing": false,
  "parent": "Continuous Random Variables",
  "prereqs": [
   "Probability density function"
  ],
  "uses": [],
  "page": 4,
  "summary": "A continuous random variable X is uniform on $[a,b]$ if $f(x)=\\frac{1}{b-a}$ for $a\\le x\\le b$ and 0 otherwise."
 },
 {
  "name": "Exponential Distribution",
  "type": "concept",
  "existing": false,
  "parent": "Continuous Random Variables",
  "prereqs": [
   "Probability density function"
  ],
  "uses": [],
  "page": 4,
  "summary": "A continuous random variable X follows an exponential distribution with rate $\\lambda$ if $f(x)=\\lambda e^{-\\lambda x}$ for $x\\ge0$."
 },
 {
  "name": "Cumulative Distribution Function (CDF)",
  "type": "concept",
  "existing": false,
  "parent": "Cumulative Distribution Functions",
  "prereqs": [
   "Probability density function",
   "Probability distribution"
  ],
  "uses": [],
  "page": 6,
  "summary": "$F(x)=P(X\\le x)$, defined for both discrete and continuous random variables as a sum or integral of the pmf/pdf respectively."
 },
 {
  "name": "Properties of CDFs",
  "type": "concept",
  "existing": false,
  "parent": "Cumulative Distribution Functions",
  "prereqs": [
   "Cumulative Distribution Function (CDF)"
  ],
  "uses": [],
  "page": 8,
  "summary": "The CDF is non-decreasing, approaches 0 at $-\\infty$ and 1 at $\\infty$, and satisfies $P(x_1<X\\le x_2)=F(x_2)-F(x_1)$."
 },
 {
  "name": "Quantile Function",
  "type": "concept",
  "existing": false,
  "parent": "Cumulative Distribution Functions",
  "prereqs": [
   "Cumulative Distribution Function (CDF)"
  ],
  "uses": [],
  "page": 8,
  "summary": "$F^{-1}(p)$ is the smallest x such that $F(x)\\ge p$; for continuous X it is the true inverse of F, and includes the median and quartiles as special cases."
 },
 {
  "name": "Two-Year-Old Weights (Support and Probability)",
  "type": "problem",
  "existing": false,
  "parent": "Continuous Random Variables",
  "prereqs": [],
  "uses": [
   "Probability density function",
   "Support (Probability)"
  ],
  "page": 2,
  "summary": "Finds the support and $P(X>30)$ for the pdf of two-year-old weights, $f(x)=\\frac{3}{40}-\\frac{3}{4000}(x-25)^2$ on $[15,35]$."
 },
 {
  "name": "Normalizing Constant for f(x) proportional to e to the (-2x)",
  "type": "problem",
  "existing": false,
  "parent": "Continuous Random Variables",
  "prereqs": [],
  "uses": [
   "Normalizing Constant",
   "Probability density function"
  ],
  "page": 3,
  "summary": "Finds the normalizing constant $c=2$ for $f(x)\\propto e^{-2x}$, $x>0$, then computes $P(1<X<2)=e^{-2}-e^{-4}$."
 },
 {
  "name": "CDF of a Bernoulli Distribution",
  "type": "problem",
  "existing": false,
  "parent": "Cumulative Distribution Functions",
  "prereqs": [],
  "uses": [
   "Cumulative Distribution Function (CDF)"
  ],
  "page": 6,
  "summary": "Derives the step-function CDF of a Bernoulli(p) random variable."
 },
 {
  "name": "CDF of a Uniform(0,1) Distribution",
  "type": "problem",
  "existing": false,
  "parent": "Cumulative Distribution Functions",
  "prereqs": [],
  "uses": [
   "Cumulative Distribution Function (CDF)",
   "Uniform Distribution (Continuous)"
  ],
  "page": 7,
  "summary": "Derives $F(x)=x$ on $[0,1]$ by integrating the uniform pdf."
 },
 {
  "name": "Identify Distribution from CDF (lambda=5)",
  "type": "problem",
  "existing": false,
  "parent": "Cumulative Distribution Functions",
  "prereqs": [],
  "uses": [
   "Cumulative Distribution Function (CDF)",
   "Exponential Distribution"
  ],
  "page": 8,
  "summary": "Differentiates $F(x)=1-e^{-5x}$ to recover $f(x)=5e^{-5x}$ and identifies it as exponential with $\\lambda=5$."
 },
 {
  "name": "Quantile Function of Exponential (lambda=2)",
  "type": "problem",
  "existing": false,
  "parent": "Cumulative Distribution Functions",
  "prereqs": [],
  "uses": [
   "Quantile Function",
   "Exponential Distribution"
  ],
  "page": 9,
  "summary": "Solves $p=1-e^{-2x}$ for x to find the quantile function and median of an exponential($\\lambda=2$) distribution."
 }
]
```

# Frankenstein problems

**Problem 1.** Suppose a continuous random variable X has pdf $f(x) = c\,x$ for $0 \le x \le 4$, and $f(x)=0$ otherwise.

(a) Find the normalizing constant c and state the support of X.
(b) Find the CDF $F(x)$.
(c) Use the CDF to find $P(X>3)$.

*Concepts tested: Probability density function, Normalizing Constant, Support (Probability), Cumulative Distribution Function (CDF), Properties of CDFs.*

Solution:
(a) Unity property: $\int_0^4 c\,x\,dx = c\left[\frac{x^2}{2}\right]_0^4 = c\cdot 8 = 1$, so $c = \frac{1}{8}$. Thus $f(x)=\frac{x}{8}$ on $[0,4]$, and the support is $[0,4]$.
(b) For $0\le x\le 4$: $F(x) = \int_0^x \frac{t}{8}\,dt = \frac{x^2}{16}$. So $F(x)=0$ for $x<0$, $F(x)=\frac{x^2}{16}$ for $0\le x\le4$, and $F(x)=1$ for $x>4$.
(c) $P(X>3) = 1-F(3) = 1-\frac{9}{16} = \frac{7}{16} = 0.4375$.

**Problem 2.** A random variable X follows an exponential distribution with rate $\lambda=3$.

(a) Write its pdf and CDF.
(b) Use the CDF and the complement property to find $P(X>1)$.
(c) Find the median of X using the quantile function.

*Concepts tested: Exponential Distribution, Cumulative Distribution Function (CDF), Properties of CDFs, Quantile Function.*

Solution:
(a) $f(x) = 3e^{-3x}$ for $x\ge0$; $F(x) = 1-e^{-3x}$.
(b) $P(X>1) = 1-F(1) = 1-(1-e^{-3}) = e^{-3} \approx 0.0498$.
(c) Set $p = 1-e^{-3x}$, solve for x: $x = -\frac{\ln(1-p)}{3}$, so $F^{-1}(p) = -\frac{\ln(1-p)}{3}$. Median $= F^{-1}(0.5) = \frac{\ln 2}{3} \approx 0.2310$.
