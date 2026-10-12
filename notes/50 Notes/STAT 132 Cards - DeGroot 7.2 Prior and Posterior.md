---
type: reference
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "DeGroot 7.2 Prior and Posterior"
tags:
  - decks
---
# STAT 132 Cards - DeGroot 7.2 Prior and Posterior Bayesian Updating

## Prior Distribution
| Front | Back | Notes |
| --- | --- | --- |
| Before any data are observed, what is the distribution assigned to a parameter $\theta$ called? | Its prior distribution: the distribution representing belief about $\theta$ before observing the other random variables of interest. | p.386; definition |
| What symbol denotes the prior p.f. or p.d.f. of $\theta$, and how does the choice between them depend on the parameter space? | $\xi(\theta)$; if the parameter space is at most countable it is a prior p.f., if $\theta$ has a continuous distribution it is a prior p.d.f. | p.386; definition |
| If you treat a parameter $\theta$ as random, what other familiar name is "prior distribution" just another name for? | The marginal distribution of the parameter. | p.386; definition |

## Posterior Distribution
| Front | Back | Notes |
| --- | --- | --- |
| How is the posterior p.d.f. or p.f. of $\theta$ given $X_1=x_1,\dots,X_n=x_n$ denoted? | $\xi(\theta \mid x_1,\dots,x_n)$. | p.387; definition |
| In the posterior formula $\xi(\theta\mid \boldsymbol{x}) = f(x_1\mid\theta)\cdots f(x_n\mid\theta)\xi(\theta)/g_n(\boldsymbol{x})$, what does $g_n(\boldsymbol{x})$ represent? | The marginal joint p.d.f. or p.f. of $X_1,\dots,X_n$, obtained by integrating (or summing) the numerator over all $\theta \in \Omega$. | p.387-388; formula |

## Likelihood Function
| Front | Back | Notes |
| --- | --- | --- |
| What is the likelihood function? | The joint p.d.f. or p.f. $f_n(x\mid\theta)$ of the observations in a random sample, regarded as a function of $\theta$ for the given observed values. | p.390; definition |
| For a random sample $X_1,\dots,X_n$ with common p.d.f. $f(x\mid\theta)$, how does the joint likelihood $f_n(x\mid\theta)$ factor? | $f_n(x\mid\theta) = f(x_1\mid\theta)\cdots f(x_n\mid\theta)$, since the observations are conditionally i.i.d. given $\theta$. | p.388; formula |

## Bayes' Theorem for Distributions
| Front | Back | Notes |
| --- | --- | --- |
| Write Bayes' theorem restated for a parameter $\theta$ and a random sample $x$. | $\xi(\theta\mid x) = \dfrac{f(x_1\mid\theta)\cdots f(x_n\mid\theta)\xi(\theta)}{g_n(x)}$ for $\theta \in \Omega$. | p.387; formula, Theorem 7.2.1 |
| How is $g_n(x)$ computed from the conditional joint p.d.f. and the prior? | $g_n(x) = \int_\Omega f_n(x\mid\theta)\xi(\theta)\, d\theta$, an application of the law of total probability for random vectors. | p.388; formula |

## Posterior Proportionality
| Front | Back | Notes |
| --- | --- | --- |
| Why can $\xi(\theta\mid x) = f_n(x\mid\theta)\xi(\theta)/g_n(x)$ be rewritten as $\xi(\theta\mid x) \propto f_n(x\mid\theta)\xi(\theta)$? | $g_n(x)$ does not depend on $\theta$, only on the observed data, so it can be treated as a constant when $\xi(\theta\mid x)$ is viewed as a function of $\theta$. | p.390; formula |
| Once $\xi(\theta\mid x)$ is known only up to a constant, how do you pin down the exact constant? | Use the fact that a p.d.f. must integrate to 1: choose the constant so that $\int_\Omega \xi(\theta\mid x)\, d\theta = 1$. | p.390; procedure |

## Improper Prior
| Front | Back | Notes |
| --- | --- | --- |
| What makes a "prior" improper? | It is a nonnegative function $\xi(\theta)$ used as if it were a prior p.d.f., but $\int_\Omega \xi(\theta)\, d\theta = \infty$, so it is not actually a probability distribution. | p.387; definition |
| Why might a statistician deliberately use an improper prior? | As an expedient when the data contain far more information than any proper prior specification would, so the exact choice of prior matters little to the posterior. | p.387; example |

## Sensitivity Analysis
| Front | Back | Notes |
| --- | --- | --- |
| What is a sensitivity analysis in Bayesian inference? | Comparing the posterior distributions that result from several different prior distributions, to see how much the choice of prior affects the conclusions. | p.386; definition |
| For a small data set, how does the choice of prior typically affect the posterior compared to a large data set? | With a small data set the posterior can still differ a lot across priors; with a lot of data, different priors tend to produce nearly the same posterior. | p.386,389-390; example |

## Sequential Bayesian Updating
| Front | Back | Notes |
| --- | --- | --- |
| After observing $x_1,\dots,x_{n-1}$ sequentially, what role does the current posterior $\xi(\theta\mid x_1,\dots,x_{n-1})$ play when the next value $x_n$ is observed? | It serves as the prior for $\theta$ going into the update on $x_n$: $\xi(\theta\mid x_1,\dots,x_n) \propto f(x_n\mid\theta)\xi(\theta\mid x_1,\dots,x_{n-1})$. | p.391; formula |
| Yes or no, and why: does updating on observations one at a time ever give a different final posterior than updating on the whole sample at once? | No: given conditionally i.i.d. observations, the posterior $\xi(\theta\mid x)$ is the same whether computed sequentially or directly from Bayes' theorem on the full sample. | p.391-392; theorem |

## Posterior Predictive Distribution
| Front | Back | Notes |
| --- | --- | --- |
| How do you find the conditional p.d.f. of a future observation $X_n$ given the previously observed $x_1,\dots,x_{n-1}$? | Average the conditional p.d.f. $f(x_n\mid\theta)$ over the current posterior: $f(x_n\mid x_1,\dots,x_{n-1}) = \int_\Omega f(x_n\mid\theta)\,\xi(\theta\mid x_1,\dots,x_{n-1})\, d\theta$. | p.392; formula |
| In the sequential relation $\xi(\theta\mid x) \propto f(x_n\mid\theta)\xi(\theta\mid x_1,\dots,x_{n-1})$, what is the missing proportionality constant equal to? | 1 over the posterior predictive p.d.f. $f(x_n\mid x_1,\dots,x_{n-1})$. | p.392; formula |

## Fluorescent Lamp Posterior
| Front | Back | Notes |
| --- | --- | --- |
| Five lamp lifetimes ($n=5$, sum $y=16{,}178$) are exponential($\theta$) given $\theta$, with a gamma(4, 20000) prior. What is the key step that identifies the posterior without doing the integral? | Drop constants to get $f_n(x\mid\theta)\xi(\theta) \propto \theta^{n+3}e^{-(y+20{,}000)\theta} = \theta^{8}e^{-36{,}178\theta}$, recognize this as a gamma kernel, giving posterior gamma$(n+4,\, y+20{,}000)$ = gamma(9, 36178). | p.388-389; problem |

## Defective Items Beta Posterior
| Front | Back | Notes |
| --- | --- | --- |
| In Example 7.2.7, the product $f_n(x\mid\theta)\xi(\theta) = \theta^y(1-\theta)^{n-y}$ for $0 < \theta < 1$ is recognized as proportional to which named p.d.f., and with what parameters? | The beta p.d.f. with parameters $\alpha = y+1$ and $\beta = n-y+1$. | p.390-391; example |

## Next Lamp Lifetime Prediction
| Front | Back | Notes |
| --- | --- | --- |
| Given the gamma(9, 36178) posterior for $\theta$ from five lamp lifetimes, what is the key step to get the predictive p.d.f. of the sixth lifetime $X_6$? | Integrate the exponential likelihood against the posterior: $f(x_6\mid x) = \int_0^\infty \theta e^{-\theta x_6}\,\xi(\theta\mid x)\, d\theta$, which reduces via the gamma integral formula to $9.555\times10^{41}/(x_6+36{,}178)^{10}$. | p.392; problem |

## Kernel of a Distribution
| Front | Back | Notes |
| --- | --- | --- |
| Describe the shortcut for finding a posterior p.d.f. without doing the integral in $g_n(x)$ directly. | Drop any factor from the prior and likelihood that does not involve $\theta$, multiply what remains, then recognize the resulting kernel $g(\theta)$ as (part of) a named p.d.f.; that named distribution is the posterior. | p.391; procedure |

# Node map
```json
[
 {
  "name": "Prior Distribution",
  "type": "concept",
  "existing": true,
  "parent": "Bayesian Inference",
  "prereqs": [],
  "uses": [],
  "page": 386,
  "summary": "The distribution assigned to a parameter $\\theta$ before observing data; discrete parameters get a prior p.f., continuous ones a prior p.d.f. $\\xi(\\theta)$."
 },
 {
  "name": "Posterior Distribution",
  "type": "concept",
  "existing": true,
  "parent": "Bayesian Inference",
  "prereqs": [
   "Prior Distribution",
   "Likelihood Function"
  ],
  "uses": [],
  "page": 387,
  "summary": "The conditional distribution of $\\theta$ given the observed data, denoted $\\xi(\\theta \\mid x_1,\\dots,x_n)$."
 },
 {
  "name": "Likelihood Function",
  "type": "concept",
  "existing": true,
  "parent": "Bayesian Inference",
  "prereqs": [],
  "uses": [],
  "page": 390,
  "summary": "The joint p.f./p.d.f. of the sample, $f_n(x\\mid\\theta)$, viewed as a function of $\\theta$ for the fixed observed data."
 },
 {
  "name": "Bayes' Theorem for Distributions",
  "type": "concept",
  "existing": true,
  "parent": "Bayesian Inference",
  "prereqs": [
   "Prior Distribution",
   "Likelihood Function"
  ],
  "uses": [],
  "page": 387,
  "summary": "$\\xi(\\theta\\mid x) = f_n(x\\mid\\theta)\\xi(\\theta)/g_n(x)$, where $g_n(x)$ is the marginal p.d.f./p.f. of the data."
 },
 {
  "name": "Posterior Proportionality",
  "type": "concept",
  "existing": false,
  "parent": "Bayesian Inference",
  "prereqs": [
   "Bayes' Theorem for Distributions"
  ],
  "uses": [],
  "page": 390,
  "summary": "Since $g_n(x)$ does not depend on $\\theta$, $\\xi(\\theta\\mid x)\\propto f_n(x\\mid\\theta)\\xi(\\theta)$; the missing constant is fixed by requiring the posterior to integrate to 1."
 },
 {
  "name": "Normalizing Constant",
  "type": "concept",
  "existing": true,
  "parent": "Bayesian Inference",
  "prereqs": [
   "Posterior Proportionality"
  ],
  "uses": [],
  "page": 391,
  "summary": "Drop constant factors from the prior and likelihood, multiply, recognize the kernel as a known p.d.f. shape, then attach that distribution's constant."
 },
 {
  "name": "Improper Prior",
  "type": "concept",
  "existing": false,
  "parent": "Bayesian Inference",
  "prereqs": [
   "Prior Distribution"
  ],
  "uses": [],
  "page": 387,
  "summary": "A nonnegative function $\\xi(\\theta)$ with $\\int \\xi(\\theta)\\,d\\theta = \\infty$, used as if it were a prior when the data are far more informative than any proper prior."
 },
 {
  "name": "Sensitivity Analysis",
  "type": "concept",
  "existing": false,
  "parent": "Bayesian Inference",
  "prereqs": [
   "Prior Distribution",
   "Posterior Distribution"
  ],
  "uses": [],
  "page": 386,
  "summary": "Comparing the posteriors produced by several different priors to see how much the choice of prior affects the conclusions."
 },
 {
  "name": "Sequential Bayesian Updating",
  "type": "concept",
  "existing": false,
  "parent": "Bayesian Inference",
  "prereqs": [
   "Bayes' Theorem for Distributions"
  ],
  "uses": [],
  "page": 391,
  "summary": "Today's posterior serves as tomorrow's prior; updating one observation at a time gives the same final posterior as updating on the whole sample at once."
 },
 {
  "name": "Posterior Predictive Distribution",
  "type": "concept",
  "existing": false,
  "parent": "Bayesian Inference",
  "prereqs": [
   "Posterior Distribution",
   "Law of Total Probability (Random Variables)"
  ],
  "uses": [],
  "page": 392,
  "summary": "The conditional distribution of a future observation given the data so far, found by averaging $f(x_{n+1}\\mid\\theta)$ over the posterior of $\\theta$."
 },
 {
  "name": "Fluorescent Lamp Posterior",
  "type": "problem",
  "existing": false,
  "parent": "Bayesian Inference",
  "prereqs": [],
  "uses": [
   "Prior Distribution",
   "Likelihood Function",
   "Posterior Distribution",
   "Normalizing Constant"
  ],
  "page": 389,
  "summary": "An exponential sample of 5 lifetimes with a gamma(4,20000) prior gives a gamma(9,36178) posterior."
 },
 {
  "name": "Defective Items Beta Posterior",
  "type": "problem",
  "existing": false,
  "parent": "Bayesian Inference",
  "prereqs": [],
  "uses": [
   "Prior Distribution",
   "Likelihood Function",
   "Posterior Distribution"
  ],
  "page": 390,
  "summary": "A uniform(0,1) prior on a Bernoulli success probability becomes a beta(y+1, n-y+1) posterior after y successes in n trials."
 },
 {
  "name": "Next Lamp Lifetime Prediction",
  "type": "problem",
  "existing": false,
  "parent": "Bayesian Inference",
  "prereqs": [],
  "uses": [
   "Posterior Predictive Distribution",
   "Posterior Distribution"
  ],
  "page": 392,
  "summary": "Integrating the exponential likelihood against the gamma(9,36178) posterior gives the predictive p.d.f. of the sixth lamp's lifetime."
 },
 {
  "name": "Kernel of a Distribution",
  "type": "concept",
  "existing": true,
  "parent": "",
  "prereqs": [],
  "summary": ""
 }
]
```

# Frankenstein problems

**Problem 1.** A machine's defect rate $\theta$ has prior p.d.f. $\xi(\theta) = 2(1-\theta)$ for $0 < \theta < 1$. A sample of $n=10$ items is inspected and $y=3$ are found defective. Find the posterior distribution of $\theta$, its exact normalizing constant, and the posterior mean.

*Solution.* The likelihood is $f_n(x\mid\theta) = \theta^y(1-\theta)^{n-y} = \theta^3(1-\theta)^7$. Multiplying by the prior and dropping the constant factor 2 (Normalizing Constant technique):
$$f_n(x\mid\theta)\xi(\theta) \propto \theta^3(1-\theta)^8.$$
This is the kernel of a beta$(\alpha,\beta)$ p.d.f. with $\alpha - 1 = 3$ and $\beta - 1 = 8$, so $\alpha=4$, $\beta=9$ (Posterior Proportionality, Bayes' Theorem for Distributions). The exact normalizing constant is
$$C = \frac{\Gamma(13)}{\Gamma(4)\Gamma(9)} = \frac{12!}{3!\,8!} = \frac{479{,}001{,}600}{6\times 40{,}320} = 1980,$$
so $\xi(\theta\mid x) = 1980\,\theta^3(1-\theta)^8$ for $0<\theta<1$ (Posterior Distribution). The posterior mean is $\alpha/(\alpha+\beta) = 4/13 \approx 0.3077$.

Concepts tested: Prior Distribution, Likelihood Function, Posterior Proportionality, Normalizing Constant, Posterior Distribution.

**Problem 2.** The rate $\theta$ of an exponential interarrival process has a gamma(2,1) prior. Two interarrival times are observed sequentially: $x_1=1.5$, then $x_2=0.5$. (a) Find the posterior after $x_1$ alone. (b) Update again after $x_2$, and check it against the batch formula. (c) Find the predictive p.d.f. of the next interarrival time $X_3$, and verify it integrates to 1.

*Solution.* The gamma(2,1) prior kernel is $\xi(\theta)\propto \theta^{1}e^{-\theta}$ (Prior Distribution).

(a) After $x_1=1.5$: $\xi(\theta\mid x_1)\propto \theta e^{-\theta}\cdot \theta e^{-1.5\theta} = \theta^2 e^{-2.5\theta}$, a gamma(3, 2.5) kernel (Sequential Bayesian Updating).

(b) This posterior becomes the prior for $x_2=0.5$: $\xi(\theta\mid x_1,x_2)\propto \theta^2e^{-2.5\theta}\cdot\theta e^{-0.5\theta} = \theta^3 e^{-3\theta}$, a gamma(4,3) kernel. Checking directly against the full sample, the batch gamma-exponential pattern gives gamma$(\alpha_0+n,\ \beta_0+y) =$ gamma$(2+2,\ 1+2) =$ gamma(4,3): the two routes agree (Posterior Distribution).

(c) The predictive p.d.f. is
$$f(x_3\mid x_1,x_2) = \int_0^\infty \theta e^{-\theta x_3}\cdot \frac{3^4}{\Gamma(4)}\theta^3 e^{-3\theta}\, d\theta = \frac{81}{6}\int_0^\infty \theta^4 e^{-(3+x_3)\theta}\, d\theta = \frac{81}{6}\cdot\frac{4!}{(3+x_3)^5} = \frac{324}{(3+x_3)^5}$$
(Posterior Predictive Distribution). Checking: $\int_0^\infty 324(3+x_3)^{-5}\,dx_3 = 324\cdot\dfrac{3^{-4}}{4} = \dfrac{324}{324}=1$, confirming a valid p.d.f.

Concepts tested: Prior Distribution, Sequential Bayesian Updating, Posterior Distribution, Posterior Predictive Distribution.
