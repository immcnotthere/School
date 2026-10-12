---
type: reference
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "DeGroot 8.1 Sampling Distributions"
tags:
  - decks
---
# STAT 132 Cards - DeGroot 8.1 Sampling Distributions

## Sampling Distribution
| Front | Back | Notes |
| --- | --- | --- |
| What is the sampling distribution of a statistic $T$? | The distribution of $T=r(X_1,\dots,X_n,\theta)$ itself, viewed as a random variable for a given value of $\theta$, prior to observing the data | p.464; definition |
| Why is $T$'s distribution called a "sampling" distribution? | Because $T$ is computed from a random sample, so its distribution is derived from the sample's distribution | p.465; definition |
| How does the sampling distribution of $\hat\theta$ differ from its posterior distribution? | The sampling distribution is the conditional distribution of $\hat\theta$ given $\theta$ (before data are observed); the posterior distribution is the conditional distribution of $\theta$ given the observed data (after) | p.465-466; discrimination |
| How can $\Pr(\lvert\hat\theta-\theta\rvert<0.1)$ be computed from the sampling distribution of $\hat\theta$ and a prior on $\theta$? | By the law of total probability: $\Pr(\lvert\hat\theta-\theta\rvert<0.1)=E\!\left[\Pr(\lvert\hat\theta-\theta\rvert<0.1\mid\theta)\right]$, averaging the sampling-distribution probability over the prior | p.466; formula |

## Pivotal Quantity (Preview)
| Front | Back | Notes |
| --- | --- | --- |
| What property makes $\hat\theta/\theta$ a pivotal quantity in the electronic-components MLE example? | Its distribution does not depend on the unknown $\theta$: here $\hat\theta/\theta=3/(\theta T)$ and $\theta T\sim$ Gamma(3,1) regardless of $\theta$ | p.467; definition |
| Why is a pivotal quantity useful to a statistician who will not assign a prior to $\theta$? | Probability statements built from it (e.g. $\Pr(\lvert\hat\theta/\theta-1\rvert<0.1)$) hold for every value of $\theta$, giving a guarantee without needing a prior or posterior | p.467; procedure |

## Sampling Distribution of Relapse Proportion (Clinical Trial)
| Front | Back | Notes |
| --- | --- | --- |
| 40 imipramine patients are conditionally i.i.d. Bernoulli($\theta$); $T$ is the observed proportion without relapse. What is the p.f. of $T$ given $\theta$? | $f(t\mid\theta)=\binom{40}{40t}\theta^{40t}(1-\theta)^{40(1-t)}$ for $t=0,\frac1{40},\dots,1$ | p.464; formula |

## Sampling Distribution of the Posterior Mean vs the MLE (Electronic Components)
| Front | Back | Notes |
| --- | --- | --- |
| With $n=3$ Exponential($\theta$) lifetimes, prior Gamma(1,2), posterior mean $\hat\theta=4/(2+T)$ where $T\sim$ Gamma(3,$\theta$), express $\Pr(\hat\theta\le t\mid\theta)$ using the Gamma(3,$\theta$) c.d.f. $G(\cdot\mid\theta)$. | $F(t\mid\theta)=1-G\!\left(\dfrac4t-2\,\middle\vert\,\theta\right)$ for $t>0$ | p.466; procedure |

## Pivotal Quantity for the Exponential MLE
| Front | Back | Notes |
| --- | --- | --- |
| With $\hat\theta=3/T$, $T\sim$ Gamma(3,$\theta$) so $\theta T\sim$ Gamma(3,1), compute $\Pr(\lvert\hat\theta/\theta-1\rvert<0.1)$. | $=\Pr(2.73<\theta T<3.33)=G(3.33\mid1)-G(2.73\mid1)=0.134$ | p.467; procedure |
# Node map
```json
[
 {
  "name": "Sampling Distribution",
  "type": "concept",
  "existing": false,
  "parent": "Sampling Distribution of a Statistic",
  "prereqs": [
   "Statistic (inference)"
  ],
  "uses": [],
  "page": 464,
  "summary": "The sampling distribution of a statistic $T$ is the distribution of $T$ (given $\\theta$) prior to observing the data; it lets us assess how close an estimator is likely to be to the parameter."
 },
 {
  "name": "Pivotal Quantity (Preview)",
  "type": "concept",
  "existing": false,
  "parent": "Sampling Distribution of a Statistic",
  "prereqs": [
   "Sampling Distribution"
  ],
  "uses": [],
  "page": 467,
  "summary": "A pivotal quantity built from an estimator and the parameter (e.g. $\\hat\\theta/\\theta$) has a distribution free of $\\theta$, so probability statements about it hold for every $\\theta$."
 },
 {
  "name": "Sampling Distribution of Relapse Proportion (Clinical Trial)",
  "type": "problem",
  "existing": false,
  "parent": "Sampling Distribution of a Statistic",
  "prereqs": [],
  "uses": [
   "Sampling Distribution",
   "Binomial Distribution"
  ],
  "page": 464,
  "summary": "Derives the p.f. of the sample proportion without relapse as a rescaled binomial distribution."
 },
 {
  "name": "Sampling Distribution of the Posterior Mean vs the MLE (Electronic Components)",
  "type": "problem",
  "existing": false,
  "parent": "Sampling Distribution of a Statistic",
  "prereqs": [],
  "uses": [
   "Sampling Distribution",
   "Gamma Distribution",
   "Posterior Distribution"
  ],
  "page": 466,
  "summary": "Expresses the c.d.f. of the posterior-mean estimator of an exponential rate in terms of a gamma c.d.f."
 },
 {
  "name": "Pivotal Quantity for the Exponential MLE",
  "type": "problem",
  "existing": false,
  "parent": "Sampling Distribution of a Statistic",
  "prereqs": [],
  "uses": [
   "Sampling Distribution",
   "Pivotal Quantity (Preview)",
   "Gamma Distribution"
  ],
  "page": 467,
  "summary": "Shows the MLE-to-parameter ratio is pivotal and computes the probability it falls within 10% of 1."
 }
]
```

# Frankenstein problems

**Frankenstein 1: A New Prior, the Sampling Distribution, and a Pivotal Ratio**
Let $X_1,\dots,X_4$ be i.i.d. Exponential($\theta$) lifetimes with $T=\sum_{i=1}^4 X_i$, and suppose the prior on $\theta$ is Gamma(2,3).

(a) Give the posterior distribution of $\theta$ and the posterior mean estimator $\hat\theta_B$.
(b) Express the sampling distribution (c.d.f.) of $\hat\theta_B$ in terms of the c.d.f. $G(\cdot\mid\theta)$ of the distribution of $T$.
(c) Show that the ratio of the MLE to $\theta$ is a pivotal quantity, and express $\Pr(\lvert\hat\theta_{MLE}/\theta-1\rvert<0.2)$ in terms of $G(\cdot\mid1)$.

**Solution.**
(a) By the gamma-exponential conjugate update, the posterior is Gamma($2+4$, $3+T$) = Gamma(6, $3+T$), so $\hat\theta_B=6/(3+T)$.

(b) For $t>0$: $\hat\theta_B\le t \iff 6/(3+T)\le t \iff T\ge 6/t-3$, so $F(t\mid\theta)=\Pr(\hat\theta_B\le t\mid\theta)=1-G\!\left(\dfrac6t-3\,\middle\vert\,\theta\right)$, where $G(\cdot\mid\theta)$ is the c.d.f. of $T\sim$ Gamma(4,$\theta$).

(c) The MLE is $\hat\theta_{MLE}=4/T$, so $\hat\theta_{MLE}/\theta=4/(\theta T)$. Since $T\sim$ Gamma(4,$\theta$), the scaled variable $\theta T\sim$ Gamma(4,1), whose distribution does not depend on $\theta$; hence $\hat\theta_{MLE}/\theta$ is pivotal. Now $\lvert 4/(\theta T)-1\rvert<0.2 \iff 0.8<4/(\theta T)<1.2 \iff 4/1.2<\theta T<4/0.8 \iff 3.33<\theta T<5$. So $\Pr(\lvert\hat\theta_{MLE}/\theta-1\rvert<0.2)=G(5\mid1)-G(3.33\mid1)$ (evaluated numerically from a Gamma(4,1) c.d.f. table or software, as in Example 8.1.5).

Concepts tested: Sampling Distribution, Pivotal Quantity (Preview), Gamma-Exponential Update.

**Frankenstein 2: Normal Approximation to a Binomial Sampling Distribution**
Suppose 100 patients are conditionally i.i.d. Bernoulli($\theta$), and $T$ is the observed proportion without relapse.

(a) Give the exact sampling distribution (p.f.) of $T$.
(b) Use the central limit theorem to give a normal approximation to the sampling distribution of $T$ for this $n$.
(c) Argue that $T$ is a consistent estimator of $\theta$ as $n\to\infty$.
(d) At $\theta=0.5$, use the normal approximation and the empirical rule to approximate $\Pr(\lvert T-0.5\rvert<0.05)$.

**Solution.**
(a) $100T\sim$ Binomial(100,$\theta$), so $f(t\mid\theta)=\binom{100}{100t}\theta^{100t}(1-\theta)^{100(1-t)}$ for $t=0,\frac1{100},\dots,1$.

(b) By the central limit theorem, $T\approx$ Normal$\!\left(\theta,\dfrac{\theta(1-\theta)}{100}\right)$ for large $n$.

(c) By the law of large numbers, $T=\bar X_n\to\theta$ in probability as $n\to\infty$, so $T$ is a consistent estimator of $\theta$.

(d) At $\theta=0.5$: $SD(T)=\sqrt{0.5\times0.5/100}=\sqrt{0.0025}=0.05$. So $\Pr(\lvert T-0.5\rvert<0.05)\approx\Pr(\lvert Z\rvert<1)$, and by the empirical rule this is about $0.6827$.

Concepts tested: Sampling Distribution, Central Limit Theorem, Law of Large Numbers, Empirical Rule (68-95-99.7).
