---
type: reference
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "DeGroot 8.6 Bayesian Normal Samples"
tags:
  - decks
---
# STAT 132 Cards - DeGroot 8.6 Bayesian Normal Samples

## Precision of a Normal Distribution
| Front | Back | Notes |
| --- | --- | --- |
| Definition of the precision $\tau$ of a normal distribution? | $\tau = 1/\sigma^2$, the reciprocal of the variance. | p.510; definition |
| Normal p.d.f. parameterized by mean $\mu$ and precision $\tau$? | $f(x\mid \mu,\tau) = \left(\dfrac{\tau}{2\pi}\right)^{1/2}\exp\left(-\dfrac{\tau(x-\mu)^2}{2}\right)$ | p.510; formula |
| As precision $\tau$ increases, what happens to the spread of the normal distribution? | It becomes narrower/more concentrated, since $\tau=1/\sigma^2$ and a higher $\tau$ means a smaller variance. | p.510; discrimination |

## Normal-Gamma Family of Distributions
| Front | Back | Notes |
| --- | --- | --- |
| Normal-gamma distribution: conditional distribution of $\mu$ given $\tau$, and marginal distribution of $\tau$? | $\mu\mid\tau \sim N(\mu_0, \text{precision }\lambda_0\tau)$; $\tau \sim \text{Gamma}(\alpha_0,\beta_0)$. | p.512; definition |
| What are the four hyperparameters of a normal-gamma distribution? | $\mu_0,\lambda_0,\alpha_0,\beta_0$. | p.512; definition |
| Yes or no, and why: are $\mu$ and $\tau$ independent under a normal-gamma joint distribution? | No; the conditional precision of $\mu$ given $\tau$ is $\lambda_0\tau$, which depends on $\tau$, so they are dependent. | p.512; discrimination |

## Normal-Gamma Posterior Update
| Front | Back | Notes |
| --- | --- | --- |
| Normal-gamma conjugate update: formula for posterior $\mu_1,\lambda_1$ given prior $\mu_0,\lambda_0$ and data $(n,\bar x_n)$? | $\mu_1=\dfrac{\lambda_0\mu_0+n\bar x_n}{\lambda_0+n}$, $\lambda_1=\lambda_0+n$ | p.511; formula |
| Normal-gamma conjugate update: formula for posterior $\alpha_1,\beta_1$ (with $s_n^2=\sum(x_i-\bar x_n)^2$)? | $\alpha_1=\alpha_0+n/2$, $\beta_1=\beta_0+\dfrac{s_n^2}{2}+\dfrac{n\lambda_0(\bar x_n-\mu_0)^2}{2(\lambda_0+n)}$ | p.511; formula |
| In the normal-gamma update, $\mu_1$ is what kind of combination of $\mu_0$ and $\bar x_n$? | A weighted average, weighted by $\lambda_0$ and $n$ respectively. | p.511; concept |
| Why is the normal-gamma family called "conjugate" for normal data with unknown mean and precision? | Because the posterior distribution of $(\mu,\tau)$ given the data is again in the normal-gamma family. | p.511; definition |

## Marginal Distribution of the Mean (Normal-Gamma)
| Front | Back | Notes |
| --- | --- | --- |
| Normal-gamma prior: what distribution does $\left(\dfrac{\lambda_0\alpha_0}{\beta_0}\right)^{1/2}(\mu-\mu_0)$ have? | The $t$ distribution with $2\alpha_0$ degrees of freedom. | p.513; formula |
| How do you get the posterior version of the marginal-mean $t$ statistic? | Replace $\mu_0,\lambda_0,\alpha_0,\beta_0$ with the posterior hyperparameters $\mu_1,\lambda_1,\alpha_1,\beta_1$. | p.514; procedure |
| What two independent building blocks are used to derive that the normal-gamma marginal of $\mu$ is a $t$ distribution? | $Z=(\lambda_0\tau)^{1/2}(\mu-\mu_0)$, standard normal; and $Y=2\beta_0\tau$, $\chi^2_{2\alpha_0}$; their scaled ratio gives the $t$ distribution. | p.513-514; concept |

## Mean and Variance of the Normal-Gamma Marginal Mean
| Front | Back | Notes |
| --- | --- | --- |
| Condition for $E(\mu)$ to exist under a normal-gamma prior, and its value? | Exists if $\alpha_0>1/2$; then $E(\mu)=\mu_0$. | p.514; formula |
| Condition for $Var(\mu)$ to exist under a normal-gamma prior, and its formula? | Exists if $\alpha_0>1$; then $Var(\mu)=\dfrac{\beta_0}{\lambda_0(\alpha_0-1)}$. | p.514; formula |

## Posterior Interval for the Mean (Normal-Gamma)
| Front | Back | Notes |
| --- | --- | --- |
| Formula for a $1-\alpha$ posterior probability interval for $\mu$ under a normal-gamma posterior (hyperparams $\mu_1,\lambda_1,\alpha_1,\beta_1$)? | $\mu_1 \pm T_{2\alpha_1}^{-1}(1-\alpha/2)\sqrt{\dfrac{\beta_1}{\alpha_1\lambda_1}}$ | p.519; formula |
| How many degrees of freedom does the $t$ quantile use in this posterior interval for $\mu$? | $2\alpha_1$. | p.519; formula |

## Improper Prior for a Normal Mean and Precision
| Front | Back | Notes |
| --- | --- | --- |
| Usual improper joint prior "p.d.f." for $(\mu,\tau)$ of a normal distribution? | $\xi(\mu,\tau) \propto 1/\tau$, for $-\infty<\mu<\infty$, $\tau>0$. | p.517-518; formula |
| What "pretend" hyperparameters $(\mu_0,\lambda_0,\alpha_0,\beta_0)$ reproduce this improper prior inside the normal-gamma formulas? | $\mu_0=\lambda_0=\beta_0=0$, $\alpha_0=-1/2$ (not a real normal-gamma distribution). | p.518; formula |
| Under the usual improper prior, what are the resulting posterior hyperparameters $\mu_1,\lambda_1,\alpha_1,\beta_1$? | $\mu_1=\bar x_n$, $\lambda_1=n$, $\alpha_1=(n-1)/2$, $\beta_1=s_n^2/2$. | p.518; formula |

## Improper Priors Yield Confidence Intervals
| Front | Back | Notes |
| --- | --- | --- |
| Under the usual improper prior, how does a Bayesian posterior interval for $\mu$ compare numerically to the classical confidence interval for $\mu$? | They are identical: the posterior probability that $\mu$ lies in the interval equals the confidence coefficient. | p.518-519; concept |
| Why do the posterior and sampling distributions of $U=\sqrt{n}(X_n-\mu)/\hat\sigma$ coincide under the improper prior? | Both are the $t_{n-1}$ distribution: one as the sampling distribution given $\mu,\sigma$, the other as the posterior distribution given the data; they turn out to be the same distribution. | p.519; concept |
| This posterior-equals-sampling-distribution equivalence under an improper prior also holds for which quantity used to estimate $\sigma^2$? | $V=(n-1)\hat\sigma^2/\sigma^2$, which is $\chi^2_{n-1}$ both as sampling distribution and as improper-prior posterior distribution. | p.519; concept |

## Acid Concentration in Cheese Posterior
| Front | Back | Notes |
| --- | --- | --- |
| Cheese acid, Bayesian: prior normal-gamma($\mu_0=1,\lambda_0=1,\alpha_0=0.5,\beta_0=0.5$); data $n=10$, $\bar x_n=1.379$, $s_n^2=0.9663$. Key move to get the posterior, then $Pr(\sigma>0.3\mid x)$? | $\mu_1=(1+13.79)/11=1.345$, $\lambda_1=11$, $\alpha_1=5.5$, $\beta_1=0.5+0.9663/2+\frac{10(0.379)^2}{22}=1.0484$; use $2\beta_1\tau\sim\chi^2_{11}$ to get $Pr(\tau<11.11\mid x)=Pr(\chi^2_{11}\le23.30)\approx0.984$. | p.512-513; problem |

## Nursing Homes in New Mexico Posterior Interval
| Front | Back | Notes |
| --- | --- | --- |
| Nursing homes: prior beliefs give $\mu_0=200,\lambda_0=2,\alpha_0=2,\beta_0=6300$ (normal-gamma). Data: $n=18$, $\bar x_n=182.17$, $s_n^2=88678.5$. Key move to get the 95% posterior interval for $\mu$? | Update to $\mu_1=183.95$, $\lambda_1=20$, $\alpha_1=11$, $\beta_1=50925.37$; $U=(\lambda_1\alpha_1/\beta_1)^{1/2}(\mu-\mu_1)=0.0657(\mu-183.95)\sim t_{22}$; with $T_{22}^{-1}(0.975)=2.074$, interval $=(152.38,215.52)$. | p.515-517; problem |

## Improper Prior for Seeded Cloud Rainfall
| Front | Back | Notes |
| --- | --- | --- |
| Seeded cloud rainfall, usual improper prior; $n=26$, $\bar x_n=5.134$, $s_n^2=63.96$. Key move to get the 95% posterior interval for $\mu$ and $Pr(\mu>4\mid x)$? | Posterior $\mu_1=5.134,\lambda_1=26,\alpha_1=12.5,\beta_1=31.98$; $U=3.188(\mu-5.134)\sim t_{25}$; 95% interval $=(4.488,5.780)$, identical to the frequentist CI; $Pr(\mu>4\mid x)=1-T_{25}(-3.615)=0.9993$. | p.518-519; problem |
# Node map
```json
[
 {
  "name": "Precision of a Normal Distribution",
  "type": "concept",
  "existing": false,
  "parent": "Bayesian Inference",
  "prereqs": [
   "Normal distribution",
   "Variance of the Sample Mean"
  ],
  "uses": [],
  "page": 510,
  "summary": "The precision $\\tau$ of a normal distribution is $1/\\sigma^2$; it reparameterizes the normal pdf as $f(x\\mid\\mu,\\tau)=(\\tau/2\\pi)^{1/2}\\exp(-\\tau(x-\\mu)^2/2)$."
 },
 {
  "name": "Normal-Gamma Family of Distributions",
  "type": "concept",
  "existing": false,
  "parent": "Bayesian Inference",
  "prereqs": [
   "Precision of a Normal Distribution",
   "Gamma Distribution",
   "Conjugate Prior"
  ],
  "uses": [],
  "page": 512,
  "summary": "A joint distribution for $(\\mu,\\tau)$ where $\\mu\\mid\\tau\\sim N(\\mu_0,\\lambda_0\\tau)$ and $\\tau\\sim\\text{Gamma}(\\alpha_0,\\beta_0)$; the conjugate family for normal data with unknown mean and precision."
 },
 {
  "name": "Normal-Gamma Posterior Update",
  "type": "concept",
  "existing": false,
  "parent": "Bayesian Inference",
  "prereqs": [
   "Normal-Gamma Family of Distributions",
   "Sample Mean and Sample Variance"
  ],
  "uses": [],
  "page": 511,
  "summary": "Given a normal-gamma prior and a normal sample of size $n$, the posterior is normal-gamma with $\\mu_1,\\lambda_1,\\alpha_1,\\beta_1$ computed from the prior hyperparameters and the data."
 },
 {
  "name": "Marginal Distribution of the Mean (Normal-Gamma)",
  "type": "concept",
  "existing": false,
  "parent": "Bayesian Inference",
  "prereqs": [
   "Normal-Gamma Family of Distributions",
   "t Distribution"
  ],
  "uses": [],
  "page": 513,
  "summary": "Under a normal-gamma distribution, $(\\lambda_0\\alpha_0/\\beta_0)^{1/2}(\\mu-\\mu_0)$ has the t distribution with $2\\alpha_0$ degrees of freedom."
 },
 {
  "name": "Mean and Variance of the Normal-Gamma Marginal Mean",
  "type": "concept",
  "existing": false,
  "parent": "Bayesian Inference",
  "prereqs": [
   "Marginal Distribution of the Mean (Normal-Gamma)",
   "Moments of the t Distribution"
  ],
  "uses": [],
  "page": 514,
  "summary": "If $\\alpha_0>1/2$, $E(\\mu)=\\mu_0$; if $\\alpha_0>1$, $Var(\\mu)=\\beta_0/[\\lambda_0(\\alpha_0-1)]$."
 },
 {
  "name": "Posterior Interval for the Mean (Normal-Gamma)",
  "type": "concept",
  "existing": false,
  "parent": "Bayesian Inference",
  "prereqs": [
   "Marginal Distribution of the Mean (Normal-Gamma)",
   "Normal-Gamma Posterior Update"
  ],
  "uses": [],
  "page": 519,
  "summary": "A $1-\\alpha$ posterior interval for $\\mu$ is $\\mu_1\\pm T_{2\\alpha_1}^{-1}(1-\\alpha/2)\\sqrt{\\beta_1/(\\alpha_1\\lambda_1)}$."
 },
 {
  "name": "Improper Prior for a Normal Mean and Precision",
  "type": "concept",
  "existing": false,
  "parent": "Bayesian Inference",
  "prereqs": [
   "Improper Prior",
   "Normal-Gamma Posterior Update"
  ],
  "uses": [],
  "page": 517,
  "summary": "The usual improper prior for $(\\mu,\\tau)$ is $\\xi(\\mu,\\tau)\\propto 1/\\tau$; plugging pretend hyperparameters $\\mu_0=\\lambda_0=\\beta_0=0,\\alpha_0=-1/2$ into the normal-gamma update gives posterior $\\mu_1=\\bar x_n,\\lambda_1=n,\\alpha_1=(n-1)/2,\\beta_1=s_n^2/2$."
 },
 {
  "name": "Improper Priors Yield Confidence Intervals",
  "type": "concept",
  "existing": false,
  "parent": "Bayesian Inference",
  "prereqs": [
   "Improper Prior for a Normal Mean and Precision",
   "Confidence Interval"
  ],
  "uses": [],
  "page": 518,
  "summary": "Under the usual improper prior, a Bayesian posterior interval for $\\mu$ (or $\\sigma^2$) is numerically identical to the corresponding classical confidence interval, because the pivotal's sampling and posterior distributions coincide."
 },
 {
  "name": "Acid Concentration in Cheese Posterior",
  "type": "problem",
  "existing": false,
  "parent": "Bayesian Inference",
  "prereqs": [],
  "uses": [
   "Normal-Gamma Posterior Update",
   "Gamma Distribution"
  ],
  "page": 512,
  "summary": "Updates a normal-gamma prior on cheese lactic-acid concentration with $n=10$ data and computes the posterior probability that $\\sigma>0.3$ via the gamma/chi-square link."
 },
 {
  "name": "Nursing Homes in New Mexico Posterior Interval",
  "type": "problem",
  "existing": false,
  "parent": "Bayesian Inference",
  "prereqs": [],
  "uses": [
   "Normal-Gamma Posterior Update",
   "Posterior Interval for the Mean (Normal-Gamma)",
   "Mean and Variance of the Normal-Gamma Marginal Mean"
  ],
  "page": 515,
  "summary": "Elicits normal-gamma prior hyperparameters from prior beliefs about nursing-home bed occupancy, updates with $n=18$ data, and finds a 95% posterior interval for mean in-patient days."
 },
 {
  "name": "Improper Prior for Seeded Cloud Rainfall",
  "type": "problem",
  "existing": false,
  "parent": "Bayesian Inference",
  "prereqs": [],
  "uses": [
   "Improper Prior for a Normal Mean and Precision",
   "Improper Priors Yield Confidence Intervals",
   "t Distribution"
  ],
  "page": 518,
  "summary": "Uses the usual improper prior on seeded-cloud rainfall data to get a posterior interval for $\\mu$ identical to the Sec. 8.5 confidence interval, and computes $Pr(\\mu>4\\mid x)$."
 }
]
```

# Frankenstein problems

**Problem 1.** A bottling machine fills bottles with volume normally distributed with unknown mean $\mu$ and unknown precision $\tau$. Prior belief is expressed as a normal-gamma distribution with hyperparameters $\mu_0=500$, $\lambda_0=4$, $\alpha_0=3$, $\beta_0=12$ (mL). A sample of $n=6$ bottles gives $\bar x_n = 498$ and $s_n^2=\sum(x_i-\bar x_n)^2=50$. Find the posterior hyperparameters and a 90% posterior probability interval for $\mu$ (use $T_{12}^{-1}(0.95)=1.782$).

*Concepts tested:* Precision of a Normal Distribution, Normal-Gamma Family of Distributions, Normal-Gamma Posterior Update, Posterior Interval for the Mean (Normal-Gamma).

*Solution.*
$\mu_1 = \dfrac{4(500)+6(498)}{4+6} = \dfrac{2000+2988}{10} = 498.8$
$\lambda_1 = 4+6 = 10$
$\alpha_1 = 3 + 6/2 = 6$
$\beta_1 = 12 + \dfrac{50}{2} + \dfrac{6(4)(498-500)^2}{2(4+6)} = 12+25+4.8 = 41.8$

90% interval ($\alpha=0.10$, df $=2\alpha_1=12$): $\sqrt{\beta_1/(\alpha_1\lambda_1)} = \sqrt{41.8/60} = 0.8347$. Margin $=1.782(0.8347)=1.487$.
Interval $= 498.8 \pm 1.487 = (497.31, 500.29)$.

**Problem 2.** A sample of $n=9$ measurements from a normal population with unknown $\mu,\sigma$ gives $\bar x_n=20.5$ and $s_n^2=\sum(x_i-\bar x_n)^2=28.8$. Using the usual improper prior, find the 95% posterior probability interval for $\mu$, and show it equals the classical 95% confidence interval for $\mu$ (use $T_8^{-1}(0.975)=2.306$).

*Concepts tested:* Improper Prior for a Normal Mean and Precision, Improper Priors Yield Confidence Intervals, t Distribution, Confidence Interval for the Mean of a Normal Distribution.

*Solution.* Improper-prior posterior: $\mu_1=\bar x_n=20.5$, $\lambda_1=n=9$, $\alpha_1=(n-1)/2=4$, $\beta_1=s_n^2/2=14.4$.
$U=(\lambda_1\alpha_1/\beta_1)^{1/2}(\mu-\mu_1) = \sqrt{36/14.4}(\mu-20.5)=1.5811(\mu-20.5)\sim t_8$.
Margin $=2.306/1.5811=1.458$. Posterior interval $=(19.04, 21.96)$.

Classical check: $\hat\sigma^2=s_n^2/(n-1)=28.8/8=3.6$, $\hat\sigma=1.897$. Margin $=2.306(1.897)/\sqrt 9 = 1.458$. Same interval $(19.04,21.96)$: confirms the improper-prior posterior interval equals the confidence interval.
