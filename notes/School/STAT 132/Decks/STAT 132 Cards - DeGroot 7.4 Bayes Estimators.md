---
type: reference
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "DeGroot 7.4 Bayes Estimators"
tags:
  - decks
---
# STAT 132 Cards - DeGroot 7.4 Bayes Estimators

## Estimator vs Estimate
| Front | Back | Notes |
| --- | --- | --- |
| What is the difference between an estimator and an estimate of $\theta$? | An estimator $\delta(X_1,\dots,X_n)$ is a function of the random data, hence itself a random variable; an estimate $\delta(x_1,\dots,x_n)$ is the specific numeric value it takes once the data are observed. | p.408; discrimination |
| Must every possible value of an estimator $\delta(X)$ lie inside the parameter space $\Omega$? | No; an estimator may take values outside $\Omega$, and whether that is acceptable depends on the specific problem. | p.408; definition |

## Loss Function
| Front | Back | Notes |
| --- | --- | --- |
| What does a loss function $L(\theta,a)$ measure? | The loss or cost incurred when the true parameter value is $\theta$ and the statistician's estimate is $a$. | p.409; definition |
| If $\xi(\theta\mid x)$ is the posterior p.d.f., how is the posterior expected loss of an estimate $a$ written? | $E[L(\theta,a)\mid x] = \int_\Omega L(\theta,a)\,\xi(\theta\mid x)\, d\theta$. | p.409; formula |

## Squared Error Loss
| Front | Back | Notes |
| --- | --- | --- |
| Write the squared error loss function. | $L(\theta,a) = (\theta-a)^2$. | p.410; formula |
| Under squared error loss, which value of $a$ minimizes the posterior expected loss $E[(\theta-a)^2\mid x]$? | The posterior mean $E(\theta\mid x)$, provided it is finite. | p.410; theorem |

## Absolute Error Loss
| Front | Back | Notes |
| --- | --- | --- |
| Write the absolute error loss function. | $L(\theta,a) = \lvert\theta-a\rvert$. | p.411; formula |
| Under absolute error loss, which value of $a$ minimizes the posterior expected loss $E(\lvert\theta-a\rvert\mid x)$? | A median of the posterior distribution of $\theta$. | p.411; theorem |

## Bayes Estimator
| Front | Back | Notes |
| --- | --- | --- |
| What is the defining property of a Bayes estimate $\delta^*(x)$? | For the observed $x$, $\delta^*(x)$ is a value of $a$ that minimizes the posterior expected loss $E[L(\theta,a)\mid x]$ over all $a$. | p.409-410; definition |
| A Bayes estimator's form depends on two choices the statistician makes. What are they? | The loss function $L(\theta,a)$ used, and the prior distribution $\xi(\theta)$ assigned to the parameter. | p.410; definition |
| For a beta($\alpha,\beta$) prior on a Bernoulli parameter with squared error loss and data sum $y$ out of $n$, what is the Bayes estimator? | $\delta^*(X) = \dfrac{\alpha + \sum_{i=1}^n X_i}{\alpha+\beta+n}$, the posterior mean of the beta($\alpha+y,\beta+n-y$) posterior. | p.410; formula |

## Consistent Estimator
| Front | Back | Notes |
| --- | --- | --- |
| What does it mean for a sequence of estimators to be consistent? | The sequence converges in probability to the true unknown value of the parameter as $n \to \infty$. | p.413; definition |
| Why is the Bayes estimator sequence for a Bernoulli parameter with a conjugate prior consistent? | $\bar{X}_n \to \theta$ in probability by the law of large numbers, and the difference between the Bayes estimator and $\bar{X}_n$ converges to 0, so the Bayes estimator also converges in probability to $\theta$. | p.413; theorem |

## Estimating a Function of the Parameter
| Front | Back | Notes |
| --- | --- | --- |
| If $\psi = h(\theta)$ and squared error loss $L(\psi,a)=(\psi-a)^2$ is used, what is the Bayes estimate of $\psi$? | The posterior mean $E(\psi\mid x) = E(h(\theta)\mid x)$. | p.414; theorem |
| Yes or no, and why: is $E(h(\theta)\mid x)$ generally equal to $h(E(\theta\mid x))$? | No; for example with $\psi=1/\theta$ under a gamma(4,8.6) posterior, $E(1/\theta\mid x)=2.867$, while $1/E(\theta\mid x) = 8.6/4 = 2.15$. | p.414-415; example |

## Bernoulli Bayes Estimate
| Front | Back | Notes |
| --- | --- | --- |
| With an improper beta(0,0) prior and $n=40$ Bernoulli trials giving 22 successes, what is the key step to the squared-error Bayes estimate? | Posterior is beta(22,18); its mean is $22/40 = 0.55$, the squared-error Bayes estimate. The absolute-error estimate is the posterior median, $0.5508$. | p.410-411; problem |

## Mean Time to Failure Estimate
| Front | Back | Notes |
| --- | --- | --- |
| The posterior of a failure rate $\theta$ is gamma(4, 8.6). What is the key step to the squared-error Bayes estimate of $\psi = 1/\theta$? | Compute $E(1/\theta\mid x) = \int_0^\infty \theta^{-1}\xi(\theta\mid x)\,d\theta = \dfrac{\beta}{\alpha-1} = \dfrac{8.6}{3} \approx 2.867$ using the gamma integral. | p.414-415; problem |
# Node map
```json
[
 {
  "name": "Estimator vs Estimate",
  "type": "concept",
  "existing": false,
  "parent": "Bayesian Inference",
  "prereqs": [
   "Statistic (inference)"
  ],
  "uses": [],
  "page": 408,
  "summary": "An estimator is a function of the random data (a random variable); an estimate is its observed numeric value."
 },
 {
  "name": "Loss Function",
  "type": "concept",
  "existing": false,
  "parent": "Bayesian Inference",
  "prereqs": [
   "Estimator vs Estimate"
  ],
  "uses": [],
  "page": 409,
  "summary": "$L(\\theta,a)$ measures the cost of estimating true value theta with a; the statistician wants to minimize its posterior expectation."
 },
 {
  "name": "Squared Error Loss",
  "type": "concept",
  "existing": false,
  "parent": "Bayesian Inference",
  "prereqs": [
   "Loss Function"
  ],
  "uses": [],
  "page": 410,
  "summary": "$L(\\theta,a)=(\\theta-a)^2$; minimized in posterior expectation by the posterior mean."
 },
 {
  "name": "Absolute Error Loss",
  "type": "concept",
  "existing": false,
  "parent": "Bayesian Inference",
  "prereqs": [
   "Loss Function"
  ],
  "uses": [],
  "page": 411,
  "summary": "$L(\\theta,a)=|\\theta-a|$; minimized in posterior expectation by a posterior median."
 },
 {
  "name": "Bayes Estimator",
  "type": "concept",
  "existing": false,
  "parent": "Bayesian Inference",
  "prereqs": [
   "Loss Function",
   "Posterior Distribution"
  ],
  "uses": [],
  "page": 409,
  "summary": "The estimator delta*(x) that minimizes the posterior expected loss E[L(theta,a)|x] over all choices of a."
 },
 {
  "name": "Consistent Estimator",
  "type": "concept",
  "existing": false,
  "parent": "Bayesian Inference",
  "prereqs": [
   "Bayes Estimator",
   "Law of Large Numbers"
  ],
  "uses": [],
  "page": 413,
  "summary": "A sequence of estimators that converges in probability to the true parameter value as the sample size grows."
 },
 {
  "name": "Estimating a Function of the Parameter",
  "type": "concept",
  "existing": false,
  "parent": "Bayesian Inference",
  "prereqs": [
   "Bayes Estimator"
  ],
  "uses": [],
  "page": 414,
  "summary": "To estimate psi=h(theta) under squared error loss, use the posterior mean of psi, which generally differs from h applied to the posterior mean of theta."
 },
 {
  "name": "Bernoulli Bayes Estimate",
  "type": "problem",
  "existing": false,
  "parent": "Bayesian Inference",
  "prereqs": [],
  "uses": [
   "Beta-Bernoulli Update",
   "Squared Error Loss",
   "Bayes Estimator"
  ],
  "page": 410,
  "summary": "With an improper beta(0,0) prior and 22 successes in 40 trials, the squared-error Bayes estimate is 0.55."
 },
 {
  "name": "Mean Time to Failure Estimate",
  "type": "problem",
  "existing": false,
  "parent": "Bayesian Inference",
  "prereqs": [],
  "uses": [
   "Estimating a Function of the Parameter",
   "Gamma-Exponential Update",
   "Bayes Estimator"
  ],
  "page": 414,
  "summary": "Given a gamma(4,8.6) posterior on a failure rate, the Bayes estimate of the mean time to failure 1/theta is 2.867."
 }
]
```

# Frankenstein problems

**Problem 1.** A sensor is calibrated by taking $n=25$ i.i.d. Normal($\theta,\sigma^2=4$) readings ($\sigma^2$ known), with prior $\theta \sim$ Normal($\mu_0=10, v_0^2=9$). The sample mean is $\bar{x}=12.4$. (a) Find the Bayes estimate of $\theta$ under squared error loss. (b) Find it under absolute error loss. (c) Explain why the sequence of such Bayes estimators is consistent as more readings are taken.

*Solution.* (a) By the Normal-Normal Update, the posterior mean is
$$\mu_1 = \frac{\sigma^2\mu_0 + n v_0^2 \bar{x}}{\sigma^2 + n v_0^2} = \frac{4\times10 + 25\times9\times12.4}{4+25\times9} = \frac{40+2790}{229} = \frac{2830}{229} \approx 12.358.$$
Under Squared Error Loss, the Bayes Estimator is this posterior mean, $\delta^*(x)\approx 12.358$.

(b) Since the posterior is normal, its median equals its mean, so under Absolute Error Loss the Bayes estimate is also $\approx 12.358$.

(c) As $n\to\infty$, the weight $nv_0^2/(\sigma^2+nv_0^2)$ on $\bar{x}_n$ tends to 1 while the weight on $\mu_0$ tends to 0, so $\mu_1 \to \theta$ in probability by the law of large numbers applied to $\bar{x}_n$; the Bayes Estimator sequence is a Consistent Estimator.

Concepts tested: Normal-Normal Update, Squared Error Loss, Absolute Error Loss, Bayes Estimator, Consistent Estimator.

**Problem 2.** A call center's call rate $\theta$ (calls per minute) has a gamma(3,2) prior. Over $n=4$ minutes, a total of $y=10$ calls are observed. Estimate $\psi = 1/\theta$, the mean time between calls, under squared error loss.

*Solution.* By the Gamma-Poisson Update, the posterior is gamma($3+10$, $2+4$) = gamma(13,6). To estimate the function $\psi=1/\theta$ (Estimating a Function of the Parameter) under Squared Error Loss, the Bayes Estimator is the posterior mean of $\psi$:
$$E(1/\theta\mid x) = \int_0^\infty \theta^{-1}\,\frac{6^{13}}{\Gamma(13)}\theta^{12}e^{-6\theta}\,d\theta = \frac{6^{13}}{\Gamma(13)}\cdot\frac{\Gamma(12)}{6^{12}} = \frac{6\,\Gamma(12)}{\Gamma(13)} = \frac{6}{12} = 0.5,$$
using $\Gamma(13)=12\,\Gamma(12)$. So the estimated mean time between calls is 0.5 minutes.

Concepts tested: Gamma-Poisson Update, Estimating a Function of the Parameter, Squared Error Loss, Bayes Estimator.
