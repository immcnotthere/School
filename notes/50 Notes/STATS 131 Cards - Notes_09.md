---
type: reference
parent: "[[STATS 131]]"
domain: stats
course: "STATS 131"
status: draft
source: "Notes_09"
tags:
  - decks
---
# STATS 131 Cards - Notes_09 Normal Distribution & Sample Mean

## Normal Distribution
| Front | Back | Notes |
| --- | --- | --- |
| What is the pdf of $X\sim Normal(\mu,\sigma^2)$ for $-\infty<x<\infty$? | $f(x)=\dfrac{1}{\sigma\sqrt{2\pi}}e^{-\frac12\left(\frac{x-\mu}{\sigma}\right)^2}$, with $\sigma>0$ | p.1; definition |
| In $X\sim Normal(\mu,\sigma^2)$, what do $\mu$ and $\sigma$ represent? | $\mu$ is the mean; $\sigma$ is the standard deviation ($\sigma^2$ is the variance) | p.1; definition |
| What shape does the Normal pdf have, and around what value is it symmetric? | Bell-shaped, symmetric around $\mu$ | p.1; discrimination |

## Standard Normal Distribution
| Front | Back | Notes |
| --- | --- | --- |
| What is a standard Normal distribution? | $X\sim Normal(0,1)$, i.e. Normal with mean 0 and variance 1 | p.1; definition |
| What is the pdf of the standard Normal distribution? | $f(x)=\dfrac{1}{\sqrt{2\pi}}e^{-\frac12 x^2}$, for $-\infty<x<\infty$ | p.1; definition |

## Moment Generating Function of the Normal Distribution
| Front | Back | Notes |
| --- | --- | --- |
| What is the moment generating function $\psi_X(t)$ of $X\sim Normal(\mu,\sigma^2)$? | $\psi_X(t)=e^{\mu t+\sigma^2t^2/2}$ | p.1; formula |
| How do you get $E[X]$ and $V(X)$ from the Normal MGF? | Differentiate $\psi_X(t)$ once and evaluate at $t=0$ for $E[X]$; differentiate twice and evaluate at $t=0$ for $E[X^2]$; then $V(X)=E[X^2]-(E[X])^2$ | p.2; procedure |

## Standard Normal CDF (Φ)
| Front | Back | Notes |
| --- | --- | --- |
| How is $\Phi(x)$, the cdf of the standard Normal, defined? | $\Phi(x)=F(x)=P(X\le x)=\dfrac{1}{\sqrt{2\pi}}\displaystyle\int_{-\infty}^x e^{-t^2/2}\,dt$ | p.2; definition |
| Why must $\Phi(x)$ be evaluated numerically or via a table? | The Normal cdf has no closed-form antiderivative | p.2; definition |
| What is the symmetry identity relating $\Phi(-x)$ to $\Phi(x)$? | $\Phi(-x)=1-\Phi(x)$ | p.2; formula |
| For $k>0$, what is $P(-k\le Z\le k)$ in terms of $\Phi(k)$? | $P(-k\le Z\le k)=2\Phi(k)-1$ | p.3; formula |

## Empirical Rule (68-95-99.7)
| Front | Back | Notes |
| --- | --- | --- |
| Per the Empirical Rule, what fraction of a Normal distribution lies within 1 standard deviation of the mean? | $\approx 0.68$ | p.3; definition |
| Per the Empirical Rule, what fraction of a Normal distribution lies within 2 standard deviations of the mean? | $\approx 0.95$ | p.3; definition |
| Per the Empirical Rule, what fraction of a Normal distribution lies within 3 standard deviations of the mean? | $\approx 0.997$ | p.3; definition |

## Chebyshev's Inequality
| Front | Back | Notes |
| --- | --- | --- |
| State Chebyshev's Inequality for $X$ with $E[X]=\mu$, $V(X)=\sigma^2$, and $\varepsilon>0$. | $P(\mid X-\mu\mid\ge \varepsilon)\le \dfrac{\sigma^2}{\varepsilon^2}$ | p.3; formula |
| Unlike the Empirical Rule, what distributions does Chebyshev's Inequality apply to? | Any distribution with finite mean and variance, not just the Normal | p.3; discrimination |
| What bound does Chebyshev's Inequality give for $P(\mid X-\mu\mid\ge k\sigma)$? | $\le 1/k^2$ | p.3; formula |

## Standardization (math)
| Front | Back | Notes |
| --- | --- | --- |
| If $X\sim Normal(\mu,\sigma^2)$, what transformation of $X$ gives a standard Normal variable $Z$? | $Z=\dfrac{X-\mu}{\sigma}$ | p.4; formula |
| What are $E[Z]$ and $V(Z)$ after standardizing a Normal random variable $X$? | $E[Z]=0$, $V(Z)=1$ | p.4; definition |

## Linear Transformation Property of the Normal Distribution
| Front | Back | Notes |
| --- | --- | --- |
| If $X\sim Normal(\mu,\sigma^2)$ and $Y=aX+b$ with $a>0$, what is the distribution of $Y$? | $Y\sim Normal(a\mu+b,\ a^2\sigma^2)$ | p.4; formula |
| What does the linear transformation property say the Normal distribution has, that most other distributions (e.g. Exponential) lack? | A linear transform of a Normal random variable is still Normal | p.4; discrimination |

## Sum of Independent Normal Random Variables
| Front | Back | Notes |
| --- | --- | --- |
| If $X\sim Normal(\mu_x,\sigma_x^2)$ and $Y\sim Normal(\mu_y,\sigma_y^2)$ are independent and $W=X+Y$, what is the distribution of $W$? | $W\sim Normal(\mu_x+\mu_y,\ \sigma_x^2+\sigma_y^2)$ | p.5; formula |
| When summing two independent Normal random variables, do their standard deviations or their variances add? | Their variances add (not the standard deviations) | p.5; discrimination |

## Sample Mean
| Front | Back | Notes |
| --- | --- | --- |
| What is the formula for the sample mean $\bar X_n$ of $n$ random variables $X_1,\dots,X_n$? | $\bar X_n=\dfrac1n(X_1+X_2+\cdots+X_n)$ | p.6; definition |
| For a random sample from a distribution with mean $\mu$ and variance $\sigma^2$, what is $E[\bar X_n]$? | $\mu$ | p.6; formula |

## Convergence in Probability
| Front | Back | Notes |
| --- | --- | --- |
| What does it mean for a sequence $X_1,X_2,\dots$ to converge to $b$ in probability? | For every $\varepsilon>0$, $\lim_{n\to\infty}P(\mid X_n-b\mid<\varepsilon)=1$ | p.7; definition |
| What notation expresses "$X_n$ converges to $b$ in probability"? | $X_n\xrightarrow{p}b$ | p.7; definition |

## Law of Large Numbers
| Front | Back | Notes |
| --- | --- | --- |
| What does the Law of Large Numbers say about the sample mean $\bar X_n$ as $n\to\infty$? | $\bar X_n\xrightarrow{p}\mu$: the sample mean converges in probability to the true distribution mean | p.7; theorem |
| Which inequality is used to prove the Law of Large Numbers here? | Chebyshev's Inequality | p.7; procedure |

## Central Limit Theorem
| Front | Back | Notes |
| --- | --- | --- |
| What does the CLT say happens to $P\left(\dfrac{\bar X_n-\mu}{\sigma/\sqrt n}\le x\right)$ as $n\to\infty$? | It converges to $\Phi(x)$, the standard Normal cdf | p.8; theorem |
| Per the CLT, for large $n$, $\bar X_n$ is approximately Normal with what mean and variance? | Mean $\mu$, variance $\sigma^2/n$ | p.8; theorem |
| Per the CLT, for large $n$, the sum $\sum_{i=1}^n X_i$ is approximately Normal with what mean and variance? | Mean $n\mu$, variance $n\sigma^2$ | p.8; theorem |
| Does the CLT require the original population to be Normal or continuous? | No; it holds for any distribution (discrete or continuous) with finite mean and variance, as $n$ grows large | p.8; discrimination |

## Probability Within 1 SD Using the Φ Table
| Front | Back | Notes |
| --- | --- | --- |
| Using $\Phi(1.0)=0.8413$, find $P(-1\le X\le1)$ for standard Normal $X$ | $P(-1\le X\le1)=\Phi(1)-\Phi(-1)=\Phi(1)-(1-\Phi(1))=2\Phi(1)-1=2(0.8413)-1=0.6826$ | p.2; procedure |

## Chebyshev Bounds for k=1,2,3 SDs
| Front | Back | Notes |
| --- | --- | --- |
| Using Chebyshev's Inequality, find the lower bound on $P(\vert X-\mu\vert <2\sigma)$ | $P(\vert X-\mu\vert \ge2\sigma)\le\dfrac{\sigma^2}{(2\sigma)^2}=\dfrac14$, so $P(\vert X-\mu\vert <2\sigma)\ge1-\dfrac14=\dfrac34$ | p.3; procedure |

## P(1≤X≤8) for a Normal(5,4) Variable
| Front | Back | Notes |
| --- | --- | --- |
| For $X\sim Normal(5,4)$, find $P(1\le X\le8)$ by standardizing | $P\left(\dfrac{1-5}{2}\le Z\le\dfrac{8-5}{2}\right)=P(-2\le Z\le1.5)=\Phi(1.5)-\Phi(-2)=0.9332-(1-0.9772)=0.9104$ | p.4; procedure |

## Long Jumper, Feet to Inches (Linear Transform)
| Front | Back | Notes |
| --- | --- | --- |
| $X\sim Normal(16,2)$ is a jump distance in feet. For $Y=12X$ in inches, find the distribution of $Y$ | $Y=12X\sim Normal(12\cdot16,\ 12^2\cdot2)=Normal(192,\ 288)$ | p.5; procedure |

## Total Weight of Three Carrot Bags
| Front | Back | Notes |
| --- | --- | --- |
| Three iid bags $X_i\sim Normal(1.18,0.07^2)$. Find the distribution of the total weight $T=X_1+X_2+X_3$ | $T\sim Normal(3(1.18),\ 3(0.07)^2)=Normal(3.54,\ 0.0147)$ | p.6; procedure |

## Coin Toss, More Than 495 Heads in 900 Tosses
| Front | Back | Notes |
| --- | --- | --- |
| A fair coin is tossed 900 times, $S=$ number of heads. Use the CLT to approximate $P(S>495)$ | $E[S]=450$, $V(S)=900(\tfrac14)=225$, $\sigma_S=15$. $P(S>495)=P\left(Z>\dfrac{495-450}{15}\right)=P(Z>3)=1-\Phi(3)=1-0.9987=0.0013$ | p.8; procedure |

## Sample Mean of a Uniform(0,1) Sample, n=12
| Front | Back | Notes |
| --- | --- | --- |
| $n=12$ iid samples from Uniform(0,1). Use the CLT to approximate $P(\vert \bar X_{12}-\tfrac12\vert \le0.1)$ | $E[X_i]=\tfrac12$, $V(X_i)=\tfrac1{12}$, so $V(\bar X_{12})=\tfrac{1/12}{12}=\tfrac1{144}$, $\sigma_{\bar X}=\tfrac1{12}$. $P(-0.1\le \bar X_{12}-\tfrac12\le0.1)=P(-1.2\le Z\le1.2)=2\Phi(1.2)-1\approx0.7698$ | p.8; procedure |

## Signal and Noise, Sum of 100 Uniform Noise Sources
| Front | Back | Notes |
| --- | --- | --- |
| 100 iid noise sources $X_i\sim Uniform(-1,1)$, $S=\sum X_i$. Use the CLT to approximate $P(-10\le S\le10)$ | $E[X_i]=0$, $V(X_i)=\tfrac13$, so $E[S]=0$, $V(S)=100/3$, $\sigma_S=\sqrt{100/3}$. $P(-10\le S\le10)=P(-\sqrt3\le Z\le\sqrt3)=2\Phi(\sqrt3)-1\approx0.91$ | p.9; procedure |

# Node map
```json
[
 {
  "name": "Normal Distribution",
  "type": "concept",
  "existing": false,
  "parent": "The Normal Distribution",
  "prereqs": [],
  "uses": [],
  "page": 1,
  "summary": "A continuous random variable $X$ follows a Normal$(\\mu,\\sigma^2)$ distribution if $f(x)=\\frac{1}{\\sigma\\sqrt{2\\pi}}e^{-\\frac12(\\frac{x-\\mu}{\\sigma})^2}$; $\\mu$ is the mean and $\\sigma$ the standard deviation."
 },
 {
  "name": "Standard Normal Distribution",
  "type": "concept",
  "existing": false,
  "parent": "The Normal Distribution",
  "prereqs": [
   "Normal Distribution"
  ],
  "uses": [],
  "page": 1,
  "summary": "The special case $X\\sim Normal(0,1)$, with pdf $f(x)=\\frac{1}{\\sqrt{2\\pi}}e^{-x^2/2}$."
 },
 {
  "name": "Moment Generating Function of the Normal Distribution",
  "type": "concept",
  "existing": false,
  "parent": "The Normal Distribution",
  "prereqs": [
   "Normal Distribution"
  ],
  "uses": [],
  "page": 1,
  "summary": "For $X\\sim Normal(\\mu,\\sigma^2)$, the MGF is $\\psi_X(t)=e^{\\mu t+\\sigma^2t^2/2}$; differentiating it recovers the mean and variance."
 },
 {
  "name": "Standard Normal CDF (Φ)",
  "type": "concept",
  "existing": false,
  "parent": "The Normal Distribution",
  "prereqs": [
   "Standard Normal Distribution"
  ],
  "uses": [],
  "page": 2,
  "summary": "$\\Phi(x)=P(Z\\le x)$ for standard Normal $Z$, evaluated numerically; it satisfies $\\Phi(-x)=1-\\Phi(x)$, so $P(-k\\le Z\\le k)=2\\Phi(k)-1$."
 },
 {
  "name": "Empirical Rule (68-95-99.7)",
  "type": "concept",
  "existing": false,
  "parent": "The Normal Distribution",
  "prereqs": [
   "Standard Normal CDF (Φ)"
  ],
  "uses": [],
  "page": 3,
  "summary": "For a Normal distribution, about 68%, 95%, and 99.7% of probability lies within 1, 2, and 3 standard deviations of the mean."
 },
 {
  "name": "Chebyshev's Inequality",
  "type": "concept",
  "existing": false,
  "parent": "The Normal Distribution",
  "prereqs": [
   "Expectation and Variance"
  ],
  "uses": [],
  "page": 3,
  "summary": "For any $X$ with finite mean $\\mu$ and variance $\\sigma^2$, $P(|X-\\mu|\\ge\\varepsilon)\\le\\sigma^2/\\varepsilon^2$ for any $\\varepsilon>0$, regardless of the distribution's shape."
 },
 {
  "name": "Standardization (math)",
  "type": "concept",
  "existing": true,
  "parent": "The Normal Distribution",
  "prereqs": [
   "Normal Distribution",
   "Standard Normal Distribution"
  ],
  "uses": [],
  "page": 4,
  "summary": "For $X\\sim Normal(\\mu,\\sigma^2)$, $Z=(X-\\mu)/\\sigma$ is standard Normal, allowing any Normal probability to be read off the $\\Phi$ table."
 },
 {
  "name": "Linear Transformation Property of the Normal Distribution",
  "type": "concept",
  "existing": false,
  "parent": "The Normal Distribution",
  "prereqs": [
   "Normal Distribution"
  ],
  "uses": [],
  "page": 4,
  "summary": "If $X\\sim Normal(\\mu,\\sigma^2)$ and $Y=aX+b$ with $a>0$, then $Y\\sim Normal(a\\mu+b,a^2\\sigma^2)$: a linear transform of a Normal stays Normal."
 },
 {
  "name": "Sum of Independent Normal Random Variables",
  "type": "concept",
  "existing": false,
  "parent": "The Normal Distribution",
  "prereqs": [
   "Normal Distribution"
  ],
  "uses": [],
  "page": 5,
  "summary": "If $X\\sim Normal(\\mu_x,\\sigma_x^2)$ and $Y\\sim Normal(\\mu_y,\\sigma_y^2)$ are independent, $W=X+Y\\sim Normal(\\mu_x+\\mu_y,\\sigma_x^2+\\sigma_y^2)$: means and variances add."
 },
 {
  "name": "Sample Mean",
  "type": "concept",
  "existing": false,
  "parent": "Properties of the Sample Mean",
  "prereqs": [
   "Expectation and Variance"
  ],
  "uses": [],
  "page": 6,
  "summary": "The sample mean $\\bar X_n=\\frac1n\\sum X_i$ of an iid sample with mean $\\mu$, variance $\\sigma^2$ has $E[\\bar X_n]=\\mu$ and $V(\\bar X_n)=\\sigma^2/n$."
 },
 {
  "name": "Convergence in Probability",
  "type": "concept",
  "existing": false,
  "parent": "Properties of the Sample Mean",
  "prereqs": [],
  "uses": [],
  "page": 7,
  "summary": "$X_n\\xrightarrow{p}b$ means for every $\\varepsilon>0$, $\\lim_{n\\to\\infty}P(|X_n-b|<\\varepsilon)=1$."
 },
 {
  "name": "Law of Large Numbers",
  "type": "concept",
  "existing": true,
  "parent": "Properties of the Sample Mean",
  "prereqs": [
   "Sample Mean",
   "Convergence in Probability",
   "Chebyshev's Inequality"
  ],
  "uses": [],
  "page": 7,
  "summary": "For an iid sample with finite mean $\\mu$ and variance, the sample mean converges in probability to $\\mu$: $\\bar X_n\\xrightarrow{p}\\mu$."
 },
 {
  "name": "Central Limit Theorem",
  "type": "concept",
  "existing": true,
  "parent": "Properties of the Sample Mean",
  "prereqs": [
   "Sample Mean",
   "Standard Normal Distribution"
  ],
  "uses": [],
  "page": 8,
  "summary": "For an iid sample with mean $\\mu$ and variance $\\sigma^2$, $\\frac{\\bar X_n-\\mu}{\\sigma/\\sqrt n}$ converges in distribution to standard Normal as $n\\to\\infty$, regardless of the original distribution."
 },
 {
  "name": "Deriving Mean and Variance of the Normal via MGF",
  "type": "problem",
  "existing": false,
  "parent": "The Normal Distribution",
  "prereqs": [],
  "uses": [
   "Moment Generating Function of the Normal Distribution"
  ],
  "page": 2,
  "summary": "Differentiate the Normal MGF to show $E[X]=\\mu$ and $V(X)=\\sigma^2$."
 },
 {
  "name": "Probability Within 1 SD Using the Φ Table",
  "type": "problem",
  "existing": false,
  "parent": "The Normal Distribution",
  "prereqs": [],
  "uses": [
   "Standard Normal CDF (Φ)"
  ],
  "page": 2,
  "summary": "Uses the Φ table and symmetry to compute $P(-1\\le X\\le1)=0.6826$."
 },
 {
  "name": "General Formula for P(X Within k SDs)",
  "type": "problem",
  "existing": false,
  "parent": "The Normal Distribution",
  "prereqs": [],
  "uses": [
   "Standard Normal CDF (Φ)",
   "Probability Within 1 SD Using the Φ Table"
  ],
  "page": 3,
  "summary": "Generalizes the 1-SD case to derive $P(-k\\le Z\\le k)=2\\Phi(k)-1$."
 },
 {
  "name": "Chebyshev Bounds for k=1,2,3 SDs",
  "type": "problem",
  "existing": false,
  "parent": "The Normal Distribution",
  "prereqs": [],
  "uses": [
   "Chebyshev's Inequality"
  ],
  "page": 3,
  "summary": "Applies Chebyshev's Inequality to bound $P(|X-\\mu|<k\\sigma)$ for $k=1,2,3$."
 },
 {
  "name": "P(1≤X≤8) for a Normal(5,4) Variable",
  "type": "problem",
  "existing": false,
  "parent": "The Normal Distribution",
  "prereqs": [],
  "uses": [
   "Standardization (math)",
   "Standard Normal CDF (Φ)"
  ],
  "page": 4,
  "summary": "Standardizes $X\\sim Normal(5,4)$ to compute $P(1\\le X\\le8)=0.9104$."
 },
 {
  "name": "Long Jumper, Feet to Inches (Linear Transform)",
  "type": "problem",
  "existing": false,
  "parent": "The Normal Distribution",
  "prereqs": [],
  "uses": [
   "Linear Transformation Property of the Normal Distribution"
  ],
  "page": 5,
  "summary": "Converts $X\\sim Normal(16,2)$ feet to $Y=12X$ inches, giving $Y\\sim Normal(192,288)$."
 },
 {
  "name": "Total Weight of Three Carrot Bags",
  "type": "problem",
  "existing": false,
  "parent": "The Normal Distribution",
  "prereqs": [],
  "uses": [
   "Sum of Independent Normal Random Variables"
  ],
  "page": 6,
  "summary": "Sums three iid $Normal(1.18,0.07^2)$ bag weights to get $T\\sim Normal(3.54,0.0147)$."
 },
 {
  "name": "Coin Toss, More Than 495 Heads in 900 Tosses",
  "type": "problem",
  "existing": false,
  "parent": "Properties of the Sample Mean",
  "prereqs": [],
  "uses": [
   "Central Limit Theorem",
   "Sample Mean",
   "Standard Normal CDF (Φ)"
  ],
  "page": 8,
  "summary": "Uses the CLT on a Binomial(900,1/2) count to approximate $P(S>495)\\approx0.0013$."
 },
 {
  "name": "Sample Mean of a Uniform(0,1) Sample, n=12",
  "type": "problem",
  "existing": false,
  "parent": "Properties of the Sample Mean",
  "prereqs": [],
  "uses": [
   "Central Limit Theorem",
   "Sample Mean",
   "Standardization (math)"
  ],
  "page": 8,
  "summary": "Uses the CLT to approximate $P(|\\bar X_{12}-\\tfrac12|\\le0.1)\\approx0.7698$."
 },
 {
  "name": "Signal and Noise, Sum of 100 Uniform Noise Sources",
  "type": "problem",
  "existing": false,
  "parent": "Properties of the Sample Mean",
  "prereqs": [],
  "uses": [
   "Central Limit Theorem",
   "Sample Mean"
  ],
  "page": 9,
  "summary": "Uses the CLT on a sum of 100 iid Uniform(-1,1) noise terms to approximate $P(-10\\le S\\le10)\\approx0.91$."
 }
]
```

# Frankenstein problems

**Frankenstein Problem 1.** Two independent production lines fill bottles with volumes $X_1\sim Normal(70,9)$ mL and $X_2\sim Normal(75,16)$ mL. Let $T=X_1+X_2$ be the combined volume from one bottle off each line, and let $Y=0.5T$ be the average volume per bottle. Find $P(70\le Y\le75)$.

*Solution.*
1. **Sum of Independent Normal Random Variables:** $T=X_1+X_2\sim Normal(70+75,\ 9+16)=Normal(145,25)$.
2. **Linear Transformation Property:** $Y=0.5T\sim Normal(0.5\cdot145,\ 0.5^2\cdot25)=Normal(72.5,\ 6.25)$, so $\sigma_Y=2.5$.
3. **Standardization:** $Z_1=\dfrac{70-72.5}{2.5}=-1$, $Z_2=\dfrac{75-72.5}{2.5}=1$.
4. **Standard Normal CDF (Φ):** $P(-1\le Z\le1)=2\Phi(1)-1=2(0.8413)-1=0.6826$.

Answer: $P(70\le Y\le75)\approx0.6826$. (Checked: $9+16=25$; $0.25\times25=6.25$; $2.5/2.5=1$ exactly on both sides; $2(0.8413)-1=0.6826$.)

Concepts tested: Normal Distribution, Sum of Independent Normal Random Variables, Linear Transformation Property of the Normal Distribution, Standardization (math), Standard Normal CDF (Φ).

**Frankenstein Problem 2.** A random sample of $n=64$ iid measurements is drawn from a (non-Normal) population with mean $\mu=50$ and variance $\sigma^2=64$. Let $\bar X_{64}$ be the sample mean. Use the CLT to approximate $P(48\le\bar X_{64}\le52)$.

*Solution.*
1. **Sample Mean:** $E[\bar X_{64}]=\mu=50$, $V(\bar X_{64})=\sigma^2/n=64/64=1$, so $\sigma_{\bar X}=1$.
2. **Central Limit Theorem:** for large $n$, $\bar X_{64}$ is approximately $Normal(50,1)$.
3. **Standardization:** $Z_1=\dfrac{48-50}{1}=-2$, $Z_2=\dfrac{52-50}{1}=2$.
4. **Standard Normal CDF (Φ):** $P(-2\le Z\le2)=2\Phi(2)-1=2(0.9772)-1=0.9544$.

Answer: $P(48\le\bar X_{64}\le52)\approx0.9544$. (Checked: $64/64=1$ exactly; matches the Empirical Rule's "~95% within 2 SDs" as a sanity check.)

Concepts tested: Sample Mean, Central Limit Theorem, Standardization (math), Standard Normal CDF (Φ).
