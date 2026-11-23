---
type: reference
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "Lecture_03"
tags:
  - decks
---
# STAT 132 Cards - Lecture_03 Posterior Distribution & Conjugate Priors

## Posterior Distribution
| Front | Back | Notes |
| --- | --- | --- |
| What is the posterior distribution of a parameter $\theta$? | The conditional distribution of $\theta$ given the observed data $X_1,\dots,X_n$; denoted $\pi(\theta \mid x_1,\dots,x_n)$. | p.2; definition |
| What do high posterior variance and low posterior variance each indicate about $\theta$? | High posterior variance means we are still uncertain what a likely value of $\theta$ is; low posterior variance means we have little uncertainty about the likely values of $\theta$. | p.2; discrimination |

## Bayesian Approach
| Front | Back | Notes |
| --- | --- | --- |
| What is the main goal of Bayesian inference? | To find or calculate the posterior distribution of the parameter. | p.2; definition |
| Since the posterior is itself a probability distribution, what can be computed from it once it is known? | Summaries such as its mean and variance, which describe our updated beliefs about the parameter. | p.2; procedure |

## Conjugate Prior
| Front | Back | Notes |
| --- | --- | --- |
| What is a conjugate prior for a given likelihood? | A prior distribution such that the resulting posterior distribution belongs to the same family as the prior. | p.4; definition |
| Why are conjugate priors useful for Bayesian updating? | Posterior updating reduces to updating the parameters of the family, rather than recomputing the full posterior integral. | p.4; procedure |

## Beta-Bernoulli Update
| Front | Back | Notes |
| --- | --- | --- |
| Bernoulli sampling $x_1,\dots,x_n$ with a Beta$(\alpha,\beta)$ prior on $p$: what is the posterior distribution of $p$? | Beta$\left(\alpha+\sum_{i=1}^n x_i,\ \ \beta+n-\sum_{i=1}^n x_i\right)$ | p.4; formula |
| In the Beta-Bernoulli update, what do the increases to $\alpha$ and $\beta$ represent? | $\alpha$ increases by the number of observed successes, $\sum x_i$; $\beta$ increases by the number of observed failures, $n-\sum x_i$. | p.4; discrimination |

## Gamma-Poisson Update
| Front | Back | Notes |
| --- | --- | --- |
| Poisson sampling $x_1,\dots,x_n$ with a Gamma$(\alpha,\beta)$ prior on $\lambda$: what is the posterior distribution of $\lambda$? | Gamma$\left(\alpha+\sum_{i=1}^n x_i,\ \ \beta+n\right)$ | p.5; formula |
| In the Gamma-Poisson update, what do the increases to $\alpha$ and $\beta$ represent? | $\alpha$ increases by the total observed count, $\sum x_i$; $\beta$ increases by the number of observations, $n$. | p.5; discrimination |

## Normal-Normal Update
| Front | Back | Notes |
| --- | --- | --- |
| Normal sampling with known variance $\sigma^2$ and a Normal$(\mu_0,\sigma_0^2)$ prior on $\mu$: what is the posterior mean $\mu_1$? | $\mu_1 = \dfrac{\sigma^2\mu_0 + n\sigma_0^2\bar{x}_n}{\sigma^2+n\sigma_0^2}$ | p.5-6; formula |
| In the same Normal-Normal setup, what is the posterior variance $\sigma_1^2$? | $\sigma_1^2 = \dfrac{\sigma^2\sigma_0^2}{\sigma^2+n\sigma_0^2}$ | p.6; formula |
| In Theorem 1.4's Normal-Normal update, which quantity must be known rather than unknown? | The sampling variance $\sigma^2$ must be known; only the mean $\mu$ is unknown. | p.5; discrimination |

## Prior Influence and Sample Size
| Front | Back | Notes |
| --- | --- | --- |
| How does a small vs. large sample size $n$ affect whether the posterior mean is closer to the prior mean or the sample mean? | Small $n$: posterior mean closer to the prior mean. Large $n$: posterior mean pulled closer to the sample mean, giving more weight to the data. | p.7; discrimination |
| How does a small prior variance $\sigma_0^2$ affect the posterior mean? | A small prior variance means a confident prior, which has more influence and pulls the posterior mean closer to the prior mean. | p.7; discrimination |
| As the sample size increases, what happens to the posterior variance? | It decreases. | p.7; definition |

## Defective Items Posterior
| Front | Back | Notes |
| --- | --- | --- |
| Proportion defective $\theta$ has a Uniform(0,1) prior; Bernoulli data $x_1,\dots,x_n$ (1 = defective). What is the posterior distribution of $\theta$? | Beta$\left(1+\sum x_i,\ \ 1+n-\sum x_i\right)$, since $\pi(\theta\mid x)\propto \theta^{\sum x_i}(1-\theta)^{n-\sum x_i}\cdot 1$ is the kernel of a Beta density and Uniform(0,1) $=$ Beta(1,1). | p.3; procedure |

## Coin Flip Posterior
| Front | Back | Notes |
| --- | --- | --- |
| 10 coin flips give 8 heads; prior for $p$ is Beta(1,1). Find the posterior distribution, posterior mean, and posterior variance of $p$. | Posterior Beta$(1+8,\ 1+10-8)=$ Beta$(9,3)$; mean $=9/12=0.75$; variance $=\dfrac{9\cdot3}{12^2\cdot13}=\dfrac{27}{1872}\approx0.0144$. | p.4; procedure |

## Store Arrivals Posterior
| Front | Back | Notes |
| --- | --- | --- |
| Poisson arrivals with a Gamma$(\alpha=3,\beta=2)$ prior on $\lambda$; one hour observed, $X=3$. Find the posterior distribution of $\lambda$, the prior variance, and the posterior variance. | Posterior Gamma$(3+3,\ 2+1)=$ Gamma$(6,3)$; prior variance $=3/2^2=0.75$; posterior variance $=6/3^2\approx0.667$. | p.5; procedure |

## Calorie Difference Posterior
| Front | Back | Notes |
| --- | --- | --- |
| Normal data with known $\sigma^2=100$, prior Normal$(\mu_0=0,\sigma_0^2=60)$, $n=20$, $\bar{x}_n=0.125$. Find the posterior distribution of $\mu$. | $\mu_1=\dfrac{100(0)+20(60)(0.125)}{100+20(60)}=\dfrac{150}{1300}\approx0.115$; $\sigma_1^2=\dfrac{100(60)}{1300}=\dfrac{6000}{1300}\approx4.615$; posterior is Normal$(0.115,\,4.615)$. | p.6; procedure |

## Bayes' Theorem for Distributions
| Front | Back | Notes |
| --- | --- | --- |
| State Bayes' Theorem for the posterior pdf/pmf of $\theta$ given a random sample $x_1,\dots,x_n$ with likelihood $f(x\mid\theta)$ and prior $\pi(\theta)$. | $\pi(\theta\mid x_1,\dots,x_n) = \dfrac{f(x_1\mid\theta)\cdots f(x_n\mid\theta)\,\pi(\theta)}{m_n(x_1,\dots,x_n)}$ | p.2; formula |
| In Bayes' Theorem, what is $m_n(x_1,\dots,x_n)$ and how is it computed? | The joint marginal distribution of the data; $m_n(\boldsymbol{x}) = \int_\Theta f(\boldsymbol{x}\mid\theta)\,\pi(\theta)\,d\theta$. | p.3; formula |
| Why can $m_n(x)$ be dropped from the posterior as just a constant? | After integrating out $\theta$, $m_n(x)$ no longer depends on $\theta$, so with respect to $\theta$ it is just a normalizing constant. | p.3; discrimination |

## Beta Distribution
| Front | Back | Notes |
| --- | --- | --- |
| What are the mean and variance of a Beta$(\alpha,\beta)$ distribution? | $E[p]=\dfrac{\alpha}{\alpha+\beta}$, $\mathrm{Var}(p)=\dfrac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}$ | p.4; formula |

# Node map
```json
[
 {
  "name": "Posterior Distribution",
  "type": "concept",
  "existing": true,
  "parent": "Bayesian Approach",
  "prereqs": [
   "Conditional Probability",
   "Prior Distribution",
   "Probability distribution"
  ],
  "uses": [],
  "page": 2,
  "summary": "The posterior distribution $\\pi(\\theta\\mid x_1,\\dots,x_n)$ is the conditional distribution of a parameter $\\theta$ given the observed data; it represents updated knowledge about $\\theta$ after seeing the data."
 },
 {
  "name": "Bayesian Approach",
  "type": "concept",
  "existing": true,
  "parent": "Posterior Distribution",
  "prereqs": [
   "Posterior Distribution"
  ],
  "uses": [],
  "page": 2,
  "summary": "Bayesian inference is centered on the posterior distribution; its main goal is to find or calculate this distribution and summarize it."
 },
 {
  "name": "Bayes' Rule",
  "type": "concept",
  "existing": true,
  "parent": "Posterior Distribution",
  "prereqs": [
   "Posterior Distribution",
   "Prior Distribution",
   "Conditional Probability"
  ],
  "uses": [],
  "page": 2,
  "summary": "For an i.i.d. sample with likelihood $f(x\\mid\\theta)$ and prior $\\pi(\\theta)$, the posterior is $\\pi(\\theta\\mid x)=\\dfrac{f(x_1\\mid\\theta)\\cdots f(x_n\\mid\\theta)\\pi(\\theta)}{m_n(x)}$, i.e. proportional to the likelihood times the prior."
 },
 {
  "name": "Conjugate Prior",
  "type": "concept",
  "existing": true,
  "parent": "Posterior Distribution",
  "prereqs": [
   "Bayes' Rule",
   "Prior Distribution",
   "Posterior Distribution"
  ],
  "uses": [],
  "page": 4,
  "summary": "A prior is conjugate for a given likelihood if the resulting posterior belongs to the same distributional family as the prior, so updating reduces to updating parameters."
 },
 {
  "name": "Beta-Bernoulli Update",
  "type": "concept",
  "existing": true,
  "parent": "Posterior Distribution",
  "prereqs": [
   "Conjugate Prior",
   "Bayes' Rule"
  ],
  "uses": [],
  "page": 4,
  "summary": "Bernoulli data with a Beta$(\\alpha,\\beta)$ prior on $p$ gives a Beta$(\\alpha+\\sum x_i,\\ \\beta+n-\\sum x_i)$ posterior."
 },
 {
  "name": "Gamma-Poisson Update",
  "type": "concept",
  "existing": true,
  "parent": "Posterior Distribution",
  "prereqs": [
   "Conjugate Prior",
   "Bayes' Rule"
  ],
  "uses": [],
  "page": 5,
  "summary": "Poisson data with a Gamma$(\\alpha,\\beta)$ prior on $\\lambda$ gives a Gamma$(\\alpha+\\sum x_i,\\ \\beta+n)$ posterior."
 },
 {
  "name": "Normal-Normal Update",
  "type": "concept",
  "existing": true,
  "parent": "Posterior Distribution",
  "prereqs": [
   "Conjugate Prior",
   "Bayes' Rule"
  ],
  "uses": [],
  "page": 5,
  "summary": "Normal data with known variance $\\sigma^2$ and a Normal$(\\mu_0,\\sigma_0^2)$ prior on $\\mu$ gives a Normal$(\\mu_1,\\sigma_1^2)$ posterior with $\\mu_1=\\dfrac{\\sigma^2\\mu_0+n\\sigma_0^2\\bar{x}_n}{\\sigma^2+n\\sigma_0^2}$ and $\\sigma_1^2=\\dfrac{\\sigma^2\\sigma_0^2}{\\sigma^2+n\\sigma_0^2}$."
 },
 {
  "name": "Prior Influence and Sample Size",
  "type": "concept",
  "existing": true,
  "parent": "Normal-Normal Update",
  "prereqs": [
   "Normal-Normal Update"
  ],
  "uses": [],
  "page": 7,
  "summary": "Small sample size or small prior variance pulls the posterior mean toward the prior mean; large sample size pulls it toward the sample mean and shrinks the posterior variance."
 },
 {
  "name": "Defective Items Posterior",
  "type": "problem",
  "existing": false,
  "parent": "Posterior Distribution",
  "prereqs": [],
  "uses": [
   "Bayes' Rule",
   "Beta-Bernoulli Update"
  ],
  "page": 3,
  "summary": "A Uniform(0,1) prior on a defect proportion $\\theta$ combined with Bernoulli data yields, via $\\pi(\\theta\\mid x)\\propto f(x\\mid\\theta)\\pi(\\theta)$, a Beta$(1+\\sum x_i,\\,1+n-\\sum x_i)$ posterior."
 },
 {
  "name": "Coin Flip Posterior",
  "type": "problem",
  "existing": false,
  "parent": "Beta-Bernoulli Update",
  "prereqs": [],
  "uses": [
   "Beta-Bernoulli Update"
  ],
  "page": 4,
  "summary": "10 flips, 8 heads, Beta(1,1) prior gives posterior Beta(9,3) with mean 0.75 and variance about 0.0144."
 },
 {
  "name": "Store Arrivals Posterior",
  "type": "problem",
  "existing": false,
  "parent": "Gamma-Poisson Update",
  "prereqs": [],
  "uses": [
   "Gamma-Poisson Update"
  ],
  "page": 5,
  "summary": "Gamma(3,2) prior, Poisson data $X=3$ in one hour gives posterior Gamma(6,3); prior variance 0.75, posterior variance about 0.667."
 },
 {
  "name": "Calorie Difference Posterior",
  "type": "problem",
  "existing": false,
  "parent": "Normal-Normal Update",
  "prereqs": [],
  "uses": [
   "Normal-Normal Update"
  ],
  "page": 6,
  "summary": "Known variance 100, prior Normal(0,60), n=20, sample mean 0.125 gives posterior Normal(0.115, 4.615) for the mean difference."
 },
 {
  "name": "Bayes' Theorem for Distributions",
  "type": "concept",
  "existing": true,
  "parent": "",
  "prereqs": [],
  "summary": ""
 },
 {
  "name": "Beta Distribution",
  "type": "concept",
  "existing": true,
  "parent": "",
  "prereqs": [],
  "summary": ""
 }
]
```

# Frankenstein problems

**Problem 1: Chip defect rate.**
A quality-control engineer's prior belief about the defect proportion $\theta$ of a batch of chips is Beta(2,3). She tests 15 chips and finds 4 defective.

(a) Explain why Beta(2,3) is a conjugate prior for this sampling model.
(b) Find the posterior distribution of $\theta$.
(c) Compute the prior variance and posterior variance of $\theta$, and state whether the posterior reflects more or less certainty about $\theta$.

Concepts tested: Conjugate Prior, Bayes' Rule, Beta-Bernoulli Update, Posterior Distribution.

Worked solution:
(a) With Bernoulli sampling, Bayes' Rule gives $\pi(\theta\mid x)\propto \theta^{\sum x_i}(1-\theta)^{n-\sum x_i}\cdot\theta^{\alpha-1}(1-\theta)^{\beta-1}$, which is again a Beta kernel, so the posterior stays in the Beta family: Beta(2,3) is conjugate.
(b) By the Beta-Bernoulli update with $\alpha=2,\ \beta=3,\ n=15,\ \sum x_i=4$: posterior is Beta$(2+4,\ 3+15-4)=$ Beta$(6,14)$.
(c) Prior variance: $\dfrac{2\cdot3}{5^2\cdot6}=\dfrac{6}{150}=0.04$. Posterior variance: $\dfrac{6\cdot14}{20^2\cdot21}=\dfrac{84}{8400}=0.01$. Since $0.01<0.04$, the posterior reflects less uncertainty (more certainty) about $\theta$ than the prior, consistent with lower posterior variance meaning more confidence in the likely value of $\theta$.

**Problem 2: Reaction-time difference and sample size.**
A researcher models a reaction-time difference $\mu$ as Normal with known variance $\sigma^2=16$, using a Normal$(\mu_0=0,\sigma_0^2=4)$ prior.

(a) With $n=5$ observations and sample mean $\bar{x}=3$, find the posterior distribution of $\mu$.
(b) With $n=50$ observations and the same sample mean $\bar{x}=3$, find the posterior distribution of $\mu$.
(c) Using the prior-influence-and-sample-size principle, explain why the posterior mean in (b) is closer to the sample mean than in (a).

Concepts tested: Prior Distribution, Posterior Distribution, Normal-Normal Update, Prior Influence and Sample Size.

Worked solution:
(a) $\mu_1=\dfrac{16(0)+5(4)(3)}{16+5(4)}=\dfrac{60}{36}=\dfrac{5}{3}\approx1.667$; $\sigma_1^2=\dfrac{16(4)}{36}=\dfrac{64}{36}=\dfrac{16}{9}\approx1.778$. Posterior: Normal$(1.667,\ 1.778)$.
(b) $\mu_1=\dfrac{16(0)+50(4)(3)}{16+50(4)}=\dfrac{600}{216}=\dfrac{25}{9}\approx2.778$; $\sigma_1^2=\dfrac{16(4)}{216}=\dfrac{64}{216}=\dfrac{8}{27}\approx0.296$. Posterior: Normal$(2.778,\ 0.296)$.
(c) With $n=50$ instead of $n=5$, the data term $n\sigma_0^2\bar{x}_n$ dominates the fixed prior term $\sigma^2\mu_0$ far more strongly, so the posterior mean shifts much closer to the sample mean (2.778 vs. 1.667, both toward $\bar{x}=3$) and the posterior variance shrinks (0.296 vs. 1.778), matching the rule that a larger sample size pulls the posterior toward the data and decreases posterior variance.
