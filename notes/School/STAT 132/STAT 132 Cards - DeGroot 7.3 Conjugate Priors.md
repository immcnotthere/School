---
type: reference
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "DeGroot 7.3 Conjugate Priors"
tags:
  - decks
---
# STAT 132 Cards - DeGroot 7.3 Conjugate Priors

## Conjugate Prior
| Front | Back | Notes |
| --- | --- | --- |
| What does it mean for a family of prior distributions $\Xi$ to be conjugate for samples from $f(x\mid\theta)$? | No matter which prior in $\Xi$ is chosen, how many observations are taken, or what values they take, the resulting posterior $\xi(\theta\mid x)$ is again a member of $\Xi$; $\Xi$ is closed under sampling. | p.395; definition |
| In a conjugate family, what are the prior hyperparameters and posterior hyperparameters? | The prior hyperparameters index the chosen prior distribution in $\Xi$; the posterior hyperparameters index the resulting posterior, which is also a member of $\Xi$. | p.395; definition |
| Which family is conjugate for sampling from a Bernoulli distribution? | The family of beta distributions. | p.394-395; example |

## Beta-Bernoulli Update
| Front | Back | Notes |
| --- | --- | --- |
| $X_1,\dots,X_n$ are Bernoulli($\theta$) with a beta($\alpha,\beta$) prior. What is the posterior distribution of $\theta$ given $\sum x_i = y$? | Beta with parameters $\alpha + y$ and $\beta + n - y$. | p.394-395; formula, Theorem 7.3.1 |
| Inspecting items one at a time starting from a beta($\alpha,\beta$) prior, how does each inspected item change the posterior's parameters? | A defective item increases $\alpha$ by 1; a nondefective item increases $\beta$ by 1. | p.395; procedure |
| In the glove-use study, a beta(1,1) prior meets 56 procedures with 50 gloved. What is the resulting posterior mean of $\theta$? | Posterior is beta($1+50$, $1+6$) = beta(51,7); mean $= 51/58 \approx 0.88$. | p.396; example |

## Gamma-Poisson Update
| Front | Back | Notes |
| --- | --- | --- |
| $X_1,\dots,X_n$ are Poisson($\theta$) with a gamma($\alpha,\beta$) prior. What is the posterior distribution given $\sum x_i = y$? | Gamma with parameters $\alpha + y$ and $\beta + n$. | p.397; formula, Theorem 7.3.2 |
| In the proof of the gamma-Poisson update, what does the Poisson likelihood reduce to after dropping the factor not involving $\theta$? | $f_n(x\mid\theta) \propto e^{-n\theta}\theta^{y}$. | p.397; formula |

## Normal-Normal Update
| Front | Back | Notes |
| --- | --- | --- |
| $X_1,\dots,X_n$ are normal($\theta,\sigma^2$) with $\sigma^2$ known and a normal($\mu_0, v_0^2$) prior on $\theta$. What is the posterior mean $\mu_1$? | $\mu_1 = \dfrac{\sigma^2\mu_0 + n v_0^2 \bar{x}_n}{\sigma^2 + n v_0^2}$. | p.398-399; formula, Theorem 7.3.3 |
| What is the posterior variance $v_1^2$ in the normal-normal update? | $v_1^2 = \dfrac{\sigma^2 v_0^2}{\sigma^2 + n v_0^2}$. | p.398-399; formula |
| $\mu_1$ is a weighted average of $\mu_0$ and $\bar{x}_n$. How does the relative weight on $\bar{x}_n$ change as $n$ grows, and as $\sigma^2$ grows? | The weight on $\bar{x}_n$ increases as $n$ increases, and decreases as $\sigma^2$ increases, for fixed $v_0^2$. | p.400; theorem |
| Yes or no, and why: does the posterior variance $v_1^2$ in the normal-normal update depend on the observed data values? | No: with $\sigma^2$ known, $v_1^2$ depends only on $n$ (and the fixed $\sigma^2, v_0^2$), not on the magnitudes of $x_1,\dots,x_n$. | p.400; theorem |

## Gamma-Exponential Update
| Front | Back | Notes |
| --- | --- | --- |
| $X_1,\dots,X_n$ are exponential($\theta$) with a gamma($\alpha,\beta$) prior. What is the posterior distribution given $\sum x_i = y$? | Gamma with parameters $\alpha + n$ and $\beta + y$. | p.401-402; formula, Theorem 7.3.4 |
| Contrast how sample size $n$ and the data sum $y$ enter the posterior parameters for the Gamma-Poisson Update versus the Gamma-Exponential Update. | Gamma-Poisson: the data sum $y$ increases $\alpha$, sample size $n$ increases $\beta$. Gamma-Exponential: sample size $n$ increases $\alpha$, data sum $y$ increases $\beta$; the roles of $n$ and $y$ swap between the two updates. | p.397,401-402; discrimination |

## Improper Prior
| Front | Back | Notes |
| --- | --- | --- |
| What is the general recipe for building an improper prior from a conjugate family that has a convenient hyperparameterization? | Set each prior hyperparameter to 0 in the family's p.d.f. formula; since posterior hyperparameters usually equal a prior hyperparameter plus a statistic, this makes the posterior hyperparameters equal exactly that statistic. | p.403-404; procedure |
| Using the improper "gamma" prior $\xi(\theta) = \theta^{-1}$ for a Poisson rate, what posterior results from 280 counts summing to 196? | Gamma(196, 280), matching the Gamma-Poisson Update with prior hyperparameters $\alpha=0,\beta=0$. | p.404; example |

## Automobile Emissions Posterior
| Front | Back | Notes |
| --- | --- | --- |
| With $n=46$, $\sigma^2=0.25$, prior mean $\mu_0=2$, prior variance $v_0^2=1$, and $\bar{x}_n = 1.329$, what is the key step to get the posterior mean $\mu_1$? | Plug directly into $\mu_1 = (\sigma^2\mu_0 + nv_0^2\bar{x}_n)/(\sigma^2+nv_0^2) = (0.25\times2 + 46\times1.329)/(0.25+46) = 1.333$. | p.399-400; problem |

# Node map
```json
[
 {
  "name": "Conjugate Prior",
  "type": "concept",
  "existing": true,
  "parent": "Bayesian Inference",
  "prereqs": [
   "Prior Distribution",
   "Posterior Distribution"
  ],
  "uses": [],
  "page": 395,
  "summary": "A family of priors $\\Xi$ is conjugate for $f(x\\mid\\theta)$ if the posterior always stays in $\\Xi$, no matter the chosen prior or observed data."
 },
 {
  "name": "Beta-Bernoulli Update",
  "type": "concept",
  "existing": true,
  "parent": "Bayesian Inference",
  "prereqs": [
   "Beta Distribution",
   "Bernoulli Distribution",
   "Conjugate Prior"
  ],
  "uses": [],
  "page": 395,
  "summary": "A beta($\\alpha,\\beta$) prior on a Bernoulli parameter updates, after $y$ successes in $n$ trials, to a beta($\\alpha+y,\\beta+n-y$) posterior."
 },
 {
  "name": "Gamma-Poisson Update",
  "type": "concept",
  "existing": true,
  "parent": "Bayesian Inference",
  "prereqs": [
   "Gamma Distribution",
   "Poisson Distribution",
   "Conjugate Prior"
  ],
  "uses": [],
  "page": 397,
  "summary": "A gamma($\\alpha,\\beta$) prior on a Poisson mean updates, after $n$ observations summing to $y$, to a gamma($\\alpha+y,\\beta+n$) posterior."
 },
 {
  "name": "Normal-Normal Update",
  "type": "concept",
  "existing": true,
  "parent": "Bayesian Inference",
  "prereqs": [
   "Conjugate Prior"
  ],
  "uses": [],
  "page": 398,
  "summary": "A normal($\\mu_0,v_0^2$) prior on a normal mean (known variance $\\sigma^2$) updates to a normal posterior with mean $\\mu_1$ and variance $v_1^2$ as in Theorem 7.3.3."
 },
 {
  "name": "Gamma-Exponential Update",
  "type": "concept",
  "existing": false,
  "parent": "Bayesian Inference",
  "prereqs": [
   "Gamma Distribution",
   "Conjugate Prior"
  ],
  "uses": [],
  "page": 401,
  "summary": "A gamma($\\alpha,\\beta$) prior on an exponential rate updates, after $n$ observations summing to $y$, to a gamma($\\alpha+n,\\beta+y$) posterior."
 },
 {
  "name": "Improper Prior",
  "type": "concept",
  "existing": true,
  "parent": "Bayesian Inference",
  "prereqs": [
   "Conjugate Prior"
  ],
  "uses": [],
  "page": 403,
  "summary": "Setting a conjugate family's prior hyperparameters to 0 gives an improper prior whose posterior hyperparameters equal the corresponding data statistics exactly."
 },
 {
  "name": "Automobile Emissions Posterior",
  "type": "problem",
  "existing": false,
  "parent": "Bayesian Inference",
  "prereqs": [],
  "uses": [
   "Normal-Normal Update",
   "Posterior Distribution"
  ],
  "page": 400,
  "summary": "Plugging n=46, known variance 0.25, and a normal(2,1) prior into the normal-normal formulas gives posterior mean 1.333."
 },
 {
  "name": "Prussian Army Horsekick Deaths",
  "type": "problem",
  "existing": false,
  "parent": "Bayesian Inference",
  "prereqs": [],
  "uses": [
   "Gamma-Poisson Update",
   "Improper Prior"
  ],
  "page": 404,
  "summary": "280 Poisson counts summing to 196, with the improper prior theta^-1, give a gamma(196,280) posterior."
 }
]
```

# Frankenstein problems

**Problem 1.** Two analysts assign different priors to a website's conversion rate $\theta$: analyst A uses beta(2,2), analyst B uses beta(20,20) (a much stronger belief that $\theta$ is near 0.5). A trial of $n=200$ visitors yields $y=40$ conversions. Find both posteriors, their means, and comment on what a sensitivity analysis reveals here.

*Solution.* By the Beta-Bernoulli Update (Conjugate Prior family), each posterior is beta($\alpha+y,\beta+n-y$).

Analyst A: beta($2+40$, $2+160$) = beta(42,162); posterior mean $= 42/204 \approx 0.2059$.

Analyst B: beta($20+40$, $20+160$) = beta(60,180); posterior mean $= 60/240 = 0.25$.

Even though the two priors disagreed sharply (mean 0.5 vs mean 0.5, but very different spreads, with B far more concentrated), the posterior means differ by only about $0.25-0.2059 = 0.044$ after 200 observations (Posterior Distribution). This is exactly the pattern behind Sensitivity Analysis: with a reasonably large sample, moderately different conjugate priors converge toward similar conclusions.

Concepts tested: Beta-Bernoulli Update, Conjugate Prior, Posterior Distribution, Sensitivity Analysis.

**Problem 2.** A cable inspector models flaws in cable as a Poisson process with rate $\theta$ flaws per meter, and, equivalently, the length until the first flaw as exponential($\theta$). Using the improper prior $\xi(\theta)=\theta^{-1}$ in both cases: (a) Five one-meter segments are inspected and a total of $y=12$ flaws are counted; find the posterior. (b) Instead, five independent segments are measured until their first flaw, with lengths summing to $y=8$; find the posterior. (c) Contrast the two posteriors.

*Solution.* The improper prior $\theta^{-1}$ is the gamma(0,0) limit (Improper Prior).

(a) Treating the counts as Poisson data with $n=5$, $y=12$, the Gamma-Poisson Update gives posterior gamma($0+12$, $0+5$) = gamma(12,5).

(b) Treating the lengths as exponential data with $n=5$, $y=8$, the Gamma-Exponential Update gives posterior gamma($0+5$, $0+8$) = gamma(5,8).

(c) Both start from the same improper prior, but the sampling scheme decides which of $n$ and $y$ becomes the shape parameter and which becomes the rate parameter: for Poisson counting data, the total count $y=12$ becomes the shape ($\alpha=12$) and the number of segments $n=5$ becomes the rate ($\beta=5$); for exponential waiting-time data, the number of segments $n=5$ becomes the shape ($\alpha=5$) and the total length $y=8$ becomes the rate ($\beta=8$). Same process, same improper prior, genuinely different posteriors.

Concepts tested: Gamma-Poisson Update, Gamma-Exponential Update, Improper Prior, Conjugate Prior.
