---
type: reference
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "DeGroot 7.5 Maximum Likelihood"
tags:
  - decks
---
# STAT 132 Cards - DeGroot 7.5 Maximum Likelihood

## Maximum Likelihood Estimation (MLE)
| Front | Back | Notes |
| --- | --- | --- |
| What value does a maximum likelihood estimate choose for $\theta$? | The value $\theta \in \Omega$ that maximizes the likelihood function $f_n(x\mid\theta)$ for the given observed data $x$. | p.418; definition |
| Instead of maximizing $f_n(x\mid\theta)$ directly, what is the standard shortcut, and why is it valid? | Maximize $\log f_n(x\mid\theta)$ instead; since $\log$ is a strictly increasing function, it has the same maximizing value of $\theta$. | p.419; procedure |
| Unlike a general estimator, what constraint is built into the definition of the M.L.E.? | The M.L.E. $\delta(x)$ is required to be an element of the parameter space $\Omega$. | p.418; definition |

## Log-Likelihood
| Front | Back | Notes |
| --- | --- | --- |
| Define the log-likelihood $L(\theta)$ for observed data $x$. | $L(\theta) = \log f_n(x\mid\theta)$. | p.419; definition |
| What is the standard calculus procedure for finding an M.L.E. using the log-likelihood? | Differentiate $L(\theta)$ with respect to $\theta$, set the derivative to 0 and solve, then confirm a maximum, for example via a negative second derivative. | p.419,421; procedure |

## MLE for Bernoulli Sample
| Front | Back | Notes |
| --- | --- | --- |
| For $X_1,\dots,X_n$ i.i.d. Bernoulli($\theta$), what is the M.L.E. of $\theta$? | $\hat\theta = \bar{X}_n$, the sample proportion of successes. | p.420; formula, Example 7.5.4 |
| How does the Bernoulli M.L.E. $\bar{X}_n$ compare to the Bayes estimator $(\alpha+y)/(\alpha+\beta+n)$ as $n\to\infty$, or as $\alpha,\beta\to0$? | Both converge to the same value: as $n\to\infty$ the Bayes estimator's dependence on the prior vanishes, and as $\alpha,\beta\to0$ the Bayes estimator reduces exactly to $\bar{X}_n$. | p.420; discrimination |

## MLE for Normal Distribution
| Front | Back | Notes |
| --- | --- | --- |
| For a random sample from a normal distribution with known variance $\sigma^2$ and unknown mean $\mu$, what is the M.L.E. of $\mu$? | $\hat\mu = \bar{X}_n$, unaffected by the value of $\sigma^2$. | p.420-421; formula, Example 7.5.5 |
| When both the mean $\mu$ and variance $\sigma^2$ are unknown, what is the joint M.L.E. $(\hat\mu,\widehat{\sigma^2})$? | $\left(\bar{X}_n,\ \dfrac{1}{n}\sum_{i=1}^n (X_i-\bar{X}_n)^2\right)$; note the divisor is $n$, not $n-1$. | p.421-422; formula, Example 7.5.6 |

## MLE for Uniform Distribution
| Front | Back | Notes |
| --- | --- | --- |
| For $X_1,\dots,X_n$ i.i.d. uniform on $[0,\theta]$, what is the M.L.E. of $\theta$? | $\hat\theta = \max\{X_1,\dots,X_n\}$. | p.422; formula, Example 7.5.7 |
| Why is $\hat\theta=\max\{X_1,\dots,X_n\}$ considered a poor estimator despite being the M.L.E.? | $\max\{X_1,\dots,X_n\} < \theta$ with probability 1, so this M.L.E. always underestimates $\theta$; any Bayes estimator would be strictly larger. | p.422; theorem |

## Existence and Uniqueness of the MLE
| Front | Back | Notes |
| --- | --- | --- |
| For the uniform p.d.f. written as $f(x\mid\theta)=1/\theta$ on the open interval $0<x<\theta$, why does the M.L.E. of $\theta$ fail to exist? | $\theta$ must be strictly greater than every $x_i$, so $1/\theta^n$ can be made arbitrarily close to its supremum by taking $\theta$ near $\max\{x_i\}$, but no $\theta \in \Omega$ actually attains that supremum. | p.422-423; example, Example 7.5.8 |
| For $X_1,\dots,X_n$ uniform on $[\theta,\theta+1]$, why is the M.L.E. of $\theta$ not unique? | The likelihood equals 1 for every $\theta$ in $[\max\{x_i\}-1,\ \min\{x_i\}]$ and 0 outside it, so any $\theta$ in that whole interval is a maximizer. | p.423; example, Example 7.5.9 |

## MLE vs Most Likely Parameter Value
| Front | Back | Notes |
| --- | --- | --- |
| Yes or no, and why: is the M.L.E. the value of $\theta$ that is "most likely" given the observed data? | No: the M.L.E. maximizes $P(\text{data}\mid\theta)$ over $\theta$, not $P(\theta\mid\text{data})$; identifying the most likely $\theta$ requires a posterior distribution, which needs a prior. | p.424; discrimination |
| In the disease-test example, if the test is positive the M.L.E. is $\hat\theta=0.9$ (has the disease). Why can the posterior probability of disease still be small? | If the prior probability of the disease is small, one imperfect positive test may not contain enough information to overcome the prior; the M.L.E. ignores the prior entirely, while the posterior does not. | p.424-425; example |

## MLE for Exponential Lifetimes
| Front | Back | Notes |
| --- | --- | --- |
| Three lifetimes $x=(3, 1.5, 2.1)$ are modeled as exponential($\theta$). What is the key step to the M.L.E. of $\theta$? | Maximize $L(\theta)=3\log\theta - 6.6\theta$: set $dL/d\theta = 3/\theta - 6.6=0$, giving $\hat\theta = 3/6.6 \approx 0.455$, a maximum since $d^2L/d\theta^2<0$. | p.419; problem |

## Disease Test MLE
| Front | Back | Notes |
| --- | --- | --- |
| The parameter space is $\Omega=\{0.1,0.9\}$ with $f(x\mid\theta)=\theta^x(1-\theta)^{1-x}$. What is the M.L.E. as a function of the test result $X$? | $\hat\theta = 0.1$ if $X=0$, since $f(0\mid0.1)=0.9 > f(0\mid0.9)=0.1$; $\hat\theta=0.9$ if $X=1$, since $f(1\mid0.9)=0.9 > f(1\mid0.1)=0.1$. | p.419-420; problem |
# Node map
```json
[
 {
  "name": "Maximum Likelihood Estimation (MLE)",
  "type": "concept",
  "existing": true,
  "parent": "Frequentist Approach",
  "prereqs": [
   "Likelihood Function"
  ],
  "uses": [],
  "page": 418,
  "summary": "The M.L.E. is the value of theta in the parameter space that maximizes the likelihood function for the observed data."
 },
 {
  "name": "Log-Likelihood",
  "type": "concept",
  "existing": true,
  "parent": "Frequentist Approach",
  "prereqs": [
   "Likelihood Function",
   "Maximum Likelihood Estimation (MLE)"
  ],
  "uses": [],
  "page": 419,
  "summary": "log f_n(x|theta), maximized in place of the likelihood itself since log is increasing; found by calculus."
 },
 {
  "name": "MLE for Bernoulli Sample",
  "type": "concept",
  "existing": false,
  "parent": "Frequentist Approach",
  "prereqs": [
   "Maximum Likelihood Estimation (MLE)",
   "Bernoulli Distribution"
  ],
  "uses": [],
  "page": 420,
  "summary": "The M.L.E. of a Bernoulli parameter is the sample proportion of successes, X-bar-n."
 },
 {
  "name": "MLE for Normal Distribution",
  "type": "concept",
  "existing": false,
  "parent": "Frequentist Approach",
  "prereqs": [
   "Maximum Likelihood Estimation (MLE)"
  ],
  "uses": [],
  "page": 420,
  "summary": "With known variance the M.L.E. of the mean is X-bar-n; with both parameters unknown the M.L.E. of the variance divides by n, not n-1."
 },
 {
  "name": "MLE for Uniform Distribution",
  "type": "concept",
  "existing": false,
  "parent": "Frequentist Approach",
  "prereqs": [
   "Maximum Likelihood Estimation (MLE)"
  ],
  "uses": [],
  "page": 422,
  "summary": "For uniform(0,theta) data, the M.L.E. is the sample maximum, which always underestimates theta."
 },
 {
  "name": "Existence and Uniqueness of the MLE",
  "type": "concept",
  "existing": false,
  "parent": "Frequentist Approach",
  "prereqs": [
   "Maximum Likelihood Estimation (MLE)"
  ],
  "uses": [],
  "page": 422,
  "summary": "An M.L.E. can fail to exist (open-interval uniform support) or fail to be unique (uniform on [theta,theta+1])."
 },
 {
  "name": "MLE vs Most Likely Parameter Value",
  "type": "concept",
  "existing": false,
  "parent": "Frequentist Approach",
  "prereqs": [
   "Maximum Likelihood Estimation (MLE)",
   "Posterior Distribution"
  ],
  "uses": [],
  "page": 424,
  "summary": "The M.L.E. maximizes P(data|theta), not P(theta|data); it is not the same as the most probable parameter value unless the prior is flat or the data are very informative."
 },
 {
  "name": "MLE for Exponential Lifetimes",
  "type": "problem",
  "existing": false,
  "parent": "Frequentist Approach",
  "prereqs": [],
  "uses": [
   "Maximum Likelihood Estimation (MLE)",
   "Log-Likelihood"
  ],
  "page": 419,
  "summary": "Three exponential lifetimes summing to 6.6 give M.L.E. theta-hat = 3/6.6 = 0.455."
 },
 {
  "name": "Disease Test MLE",
  "type": "problem",
  "existing": false,
  "parent": "Frequentist Approach",
  "prereqs": [],
  "uses": [
   "Maximum Likelihood Estimation (MLE)",
   "MLE vs Most Likely Parameter Value"
  ],
  "page": 419,
  "summary": "With parameter space {0.1,0.9}, the M.L.E. of the disease-test parameter jumps to whichever value best explains the observed test result."
 }
]
```

# Frankenstein problems

**Problem 1.** A calibration experiment records $n=10$ i.i.d. Normal($\mu,\sigma^2$) measurements (both parameters unknown), with sample mean $\bar{x}=50.2$ and $\sum_{i=1}^{10}(x_i-\bar{x})^2 = 18$. (a) Write the log-likelihood $L(\mu,\sigma^2)$. (b) Find the M.L.E. of $(\mu,\sigma^2)$. (c) Explain why this M.L.E. is guaranteed to exist and be unique here, unlike the uniform-distribution M.L.E.

*Solution.* (a) The Log-Likelihood is
$$L(\mu,\sigma^2) = -\frac{n}{2}\log(2\pi) - \frac{n}{2}\log\sigma^2 - \frac{1}{2\sigma^2}\sum_{i=1}^n (x_i-\mu)^2.$$

(b) By the MLE for Normal Distribution two-stage argument, the maximizing $\mu$ for any fixed $\sigma^2$ is $\hat\mu = \bar{x}_n = 50.2$; substituting back and maximizing over $\sigma^2$ gives
$$\widehat{\sigma^2} = \frac{1}{n}\sum_{i=1}^n (x_i-\bar{x}_n)^2 = \frac{18}{10} = 1.8.$$
So the M.L.E. is $(\hat\mu,\widehat{\sigma^2}) = (50.2,\ 1.8)$.

(c) By Maximum Likelihood Estimation (MLE) theory, $L(\mu,\sigma^2)$ is a smooth, strictly concave function of $\mu$ for fixed $\sigma^2$ (a downward parabola in $\mu$) and has a single interior critical point in $\sigma^2>0$ with a negative second derivative there, so the maximizer is attained at one finite interior point of the parameter space $\Omega = \mathbb{R}\times(0,\infty)$. This is Existence and Uniqueness of the MLE working in our favor: unlike the uniform($0,\theta$) problem, there is no boundary of $\Omega$ that the optimal value is pushed against or excluded from, so the M.L.E. exists and is unique.

Concepts tested: Log-Likelihood, MLE for Normal Distribution, Maximum Likelihood Estimation (MLE), Existence and Uniqueness of the MLE.

**Problem 2.** A random sample of 6 arrival gaps (in minutes) is modeled as uniform($0,\theta$): 2.1, 4.8, 3.3, 1.9, 4.2, 3.9. (a) Find the M.L.E. of $\theta$. (b) Explain why this M.L.E. should not be read as "the most likely value of $\theta$," and in which direction a Bayes estimator would differ. (c) State the version of the uniform p.d.f. under which no M.L.E. would exist for this same data.

*Solution.* (a) By the MLE for Uniform Distribution, $\hat\theta = \max\{2.1,4.8,3.3,1.9,4.2,3.9\} = 4.8$.

(b) By MLE vs Most Likely Parameter Value, the M.L.E. only asks which $\theta$ makes the observed data most probable, and $1/\theta^n$ is maximized by taking $\theta$ as small as the data allow; it does not weigh how plausible different $\theta$ values were beforehand. Since every value in the sample satisfies $x_i \le \theta$ with probability 1, the true $\theta$ is necessarily at least 4.8, and typically larger; a Bayes estimator (combining a prior with the data) would therefore be strictly larger than 4.8, consistent with Maximum Likelihood Estimation (MLE) always underestimating $\theta$ here.

(c) By Existence and Uniqueness of the MLE, if the p.d.f. is instead written $f(x\mid\theta)=1/\theta$ for the open interval $0<x<\theta$, then $\theta$ must be strictly greater than every $x_i$, and no smallest such $\theta$ exists; the M.L.E. would not exist for this data set.

Concepts tested: MLE for Uniform Distribution, MLE vs Most Likely Parameter Value, Maximum Likelihood Estimation (MLE), Existence and Uniqueness of the MLE.
