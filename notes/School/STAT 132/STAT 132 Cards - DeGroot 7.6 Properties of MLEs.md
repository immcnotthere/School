---
type: reference
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "DeGroot 7.6 Properties of MLEs"
tags:
  - decks
---
# STAT 132 Cards - DeGroot 7.6 Properties of MLEs

## Invariance Property of MLEs
| Front | Back | Notes |
| --- | --- | --- |
| If $\hat\theta$ is the MLE of $\theta$ and $g$ is a one-to-one function, what is the MLE of $\psi=g(\theta)$? | $g(\hat\theta)$ | p.426; theorem |
| For a general (not necessarily one-to-one) function $g(\theta)$, how is the MLE of $g(\theta)$ defined via Definition 7.6.1? | The value $\hat t$ maximizing $L^*(t)=\max_{\theta\in G_t}\log f_n(x\mid\theta)$ over $t\in G$, where $G_t=\{\theta: g(\theta)=t\}$ | p.427; definition |
| Theorem 7.6.2: if $\hat\theta$ is an MLE of $\theta$, what is an MLE of any function $g(\theta)$ (not necessarily one-to-one)? | $g(\hat\theta)$ | p.427; theorem |
| Electronic components: the MLE of the failure rate is $\hat\theta=0.455$. By invariance, what is the MLE of the mean lifetime $\psi=1/\theta$? | $\hat\psi=1/0.455\approx 2.2$ | p.427; procedure |

## Consistency of the MLE
| Front | Back | Notes |
| --- | --- | --- |
| What does it mean for a sequence of MLEs $\hat\theta_n$ to be consistent? | It converges in probability to the true value of $\theta$ as $n\to\infty$ | p.428; definition |
| For i.i.d. Bernoulli($\theta$) data with a beta prior, why do the Bayes estimator and the MLE both converge to $\theta$ as $n\to\infty$? | The MLE is $\bar X_n$; the law of large numbers gives $\bar X_n\to\theta$ in probability, and the Bayes estimator converges to $\bar X_n$, so both converge to $\theta$ | p.428; procedure |

## Newton's Method
| Front | Back | Notes |
| --- | --- | --- |
| Newton's method: given an initial guess $\theta_0$ for solving $f(\theta)=0$, what is the updated guess $\theta_1$? | $\theta_1=\theta_0-\dfrac{f(\theta_0)}{f'(\theta_0)}$ | p.429; formula |
| Geometrically, what does the Newton's-method guess $\theta_1$ represent? | Where the line tangent to $f$ at $(\theta_0,f(\theta_0))$ crosses the horizontal axis | p.429; definition |
| For a Gamma($\alpha$,1) sample, the MLE of $\alpha$ solves $\psi(\alpha)=\frac1n\sum\log x_i$, where $\psi=\Gamma'/\Gamma$ is the digamma function. What plays the role of $f'(\theta_0)$ in a Newton step here? | The trigamma function $\psi'(\alpha_0)$ | p.430; procedure |
| When can Newton's method fail badly? | When $f'(\theta)/f(\theta)$ gets close to 0 somewhere between $\theta_0$ and the true solution | p.430; discrimination |

## Method of Moments
| Front | Back | Notes |
| --- | --- | --- |
| Method of moments: define the $j$th sample moment $m_j$. | $m_j=\dfrac1n\sum_{i=1}^n X_i^j$ | p.430; definition |
| How is the method of moments estimator of a $k$-dimensional $\theta$ obtained? | Solve the $k$ equations $m_j=\mu_j(\theta)$ for $\theta$ (equivalently $\hat\theta=M(m_1,\dots,m_k)$, the inverse of $\mu$) | p.430; procedure |
| For a Gamma($\alpha,\beta$) sample with $\mu_1=\alpha/\beta$ and $\mu_2=\alpha(\alpha+1)/\beta^2$, what are the method of moments estimators of $\alpha$ and $\beta$? | $\hat\alpha=\dfrac{m_1^2}{m_2-m_1^2}$, $\quad\hat\beta=\dfrac{m_1}{m_2-m_1^2}$ | p.431; formula |
| Yes or no, and why: is the method of moments estimator guaranteed to be consistent, and is it guaranteed to lie in the set of values consistent with the data? | Under mild conditions it is consistent (Theorem 7.6.3), but it need not fall inside the set of parameter values the data actually allow, e.g. the Uniform($\theta$,$\theta$+1) case can give an impossible estimate | p.431; discrimination |

## Asymptotic Normality of the MLE
| Front | Back | Notes |
| --- | --- | --- |
| As $n$ grows, the likelihood function (as a function of $\theta$) comes to resemble what shape, centered where? | A normal-shaped curve $\exp\!\left[-\dfrac{1}{2V_n(\theta)/n}(\theta-\hat\theta)^2\right]$ centered at the MLE $\hat\theta$ | p.432; formula |
| When the prior p.d.f. of $\theta$ is relatively flat compared to a sharply peaked likelihood, what do the posterior mean and variance approach? | Posterior mean $\approx\hat\theta$; posterior variance $\approx V_n(\hat\theta)/n$ | p.432; procedure |
| For i.i.d. Exponential($\theta$) data with $\hat\theta_n=n/T_n$, what is $V_n(\theta)$ in the asymptotic normal approximation of $\hat\theta$? | $V_n(\theta)=\theta^2$ | p.432; formula |

## EM Algorithm
| Front | Back | Notes |
| --- | --- | --- |
| What kind of problem is the EM algorithm designed to solve? | Approximating the MLE when missing data make the likelihood hard to maximize in closed form | p.434; definition |
| In the E step at stage $j$, what is computed? | The conditional distribution of the missing data given the observed data at $\theta=\theta^{(j)}$, then the conditional mean of the full-data log-likelihood, treating $\theta$ as constant and the missing data as random | p.434-435; procedure |
| In the M step at stage $j$, what is computed? | $\theta^{(j+1)}$, the value that maximizes the expected full-data log-likelihood found in the E step | p.435; procedure |
| What is guaranteed about the log-likelihood across EM iterations, and what is not guaranteed? | The log-likelihood increases with every iteration; convergence is only to a local, not necessarily global, maximum | p.439; discrimination |

## MLE Independence from Sampling Plan
| Front | Back | Notes |
| --- | --- | --- |
| If the decision to stop sampling after $n$ observations depends only on the observations seen so far, how does the resulting likelihood function compare to the likelihood from a fixed sample size $n$? | It is proportional (as a function of $\theta$) to $f(x_1\mid\theta)\cdots f(x_n\mid\theta)$, the same form as for a fixed $n$ | p.439-440; formula |
| Because of this proportionality, what can be said about the MLE under two different such stopping rules that happen to produce the same observed values? | The MLE is the same value; it depends only on the data observed, not on which valid sampling plan produced it | p.440; definition |
| An experimenter has 20 Exponential($\theta$) interarrival observations averaging 6, then waits 15 more minutes with no arrival and stops. How must this extra waiting time enter the likelihood? | Multiply the likelihood from the 20 observations by $\exp(-15\theta)$, the probability that the 21st interval exceeds 15, then maximize the product | p.440; procedure |

## Newton's Method for Gamma Shape MLE
| Front | Back | Notes |
| --- | --- | --- |
| A Gamma($\alpha$,1) sample has $n=20$ with $\frac1{20}\sum\log x_i=1.220$ and $\bar x=3.679$. Starting from $\alpha_0=3.679$ with $\psi(\alpha_0)=1.1607$ and $\psi'(\alpha_0)=0.3120$, find the Newton update $\alpha_1$. | $\alpha_1=3.679-\dfrac{1.1607-1.220}{0.3120}\approx 3.871$ | p.430; procedure |

## EM Algorithm for Heights and Weights (Missing Data)
| Front | Back | Notes |
| --- | --- | --- |
| Bivariate normal heights/weights, $\theta^{(0)}=(69.60,194.75,2.87,14.82,0.1764)$; row 4 has height 68 and missing weight $X_{4,2}$. What are the E-step conditional mean and variance used to replace $X_{4,2}$? | Mean $=194.75+0.1764(14.82)^{1/2}\dfrac{68-69.60}{2.87^{1/2}}=193.3$; variance $=(1-0.1764^2)(14.82)^2=212.8$ | p.435-436; procedure |

## EM Algorithm for a Mixture of Two Normals
| Front | Back | Notes |
| --- | --- | --- |
| In the normal-mixture EM algorithm, with $q_i^{(j)}$ the conditional probability that $X_i$ came from the $\mu_1$ component, what are the M-step updates for $p^{(j+1)}$, $\mu_1^{(j+1)}$, and $\mu_2^{(j+1)}$? | $p^{(j+1)}$ is the average of the $q_i^{(j)}$'s; $\mu_1^{(j+1)}$ is the weighted average of the $X_i$'s with weights $q_i^{(j)}$; $\mu_2^{(j+1)}$ is the weighted average with weights $1-q_i^{(j)}$ | p.438; formula |

## Sampling Distribution of the Uniform Upper-Bound MLE
| Front | Back | Notes |
| --- | --- | --- |
| For $\hat\theta=\max\{X_1,\dots,X_n\}$ from the Uniform(0,$\theta$) distribution, what are $E(\hat\theta)$ and $Var(\hat\theta)$? | $E(\hat\theta)=\dfrac{n}{n+1}\theta$, $\quad Var(\hat\theta)=\dfrac{n}{(n+1)^2(n+2)}\theta^2$ | p.434; formula |
# Node map
```json
[
 {
  "name": "Invariance Property of MLEs",
  "type": "concept",
  "existing": false,
  "parent": "Properties of Maximum Likelihood Estimators",
  "prereqs": [
   "Maximum Likelihood Estimation (MLE)"
  ],
  "uses": [],
  "page": 426,
  "summary": "If $\\hat\\theta$ is the MLE of $\\theta$, then for any function $g$ (one-to-one or, via Definition 7.6.1, general), $g(\\hat\\theta)$ is the MLE of $g(\\theta)$."
 },
 {
  "name": "Consistency of the MLE",
  "type": "concept",
  "existing": false,
  "parent": "Properties of Maximum Likelihood Estimators",
  "prereqs": [
   "Maximum Likelihood Estimation (MLE)",
   "Consistent Estimator",
   "Law of Large Numbers"
  ],
  "uses": [],
  "page": 428,
  "summary": "Under typical conditions the sequence of MLEs of a parameter converges in probability to the true parameter value as sample size increases."
 },
 {
  "name": "Newton's Method",
  "type": "concept",
  "existing": false,
  "parent": "Properties of Maximum Likelihood Estimators",
  "prereqs": [],
  "uses": [],
  "page": 429,
  "summary": "An iterative root-finding method that updates a guess $\\theta_0$ to $\\theta_1=\\theta_0-f(\\theta_0)/f'(\\theta_0)$, used to solve MLE equations with no closed form."
 },
 {
  "name": "Method of Moments",
  "type": "concept",
  "existing": false,
  "parent": "Properties of Maximum Likelihood Estimators",
  "prereqs": [
   "Law of Large Numbers",
   "Consistent Estimator"
  ],
  "uses": [],
  "page": 430,
  "summary": "Estimates parameters by equating sample moments $m_j$ to theoretical moments $\\mu_j(\\theta)$ and solving for $\\theta$; simpler than MLE but occasionally inconsistent with the data range."
 },
 {
  "name": "Asymptotic Normality of the MLE",
  "type": "concept",
  "existing": false,
  "parent": "Properties of Maximum Likelihood Estimators",
  "prereqs": [
   "Central Limit Theorem",
   "Maximum Likelihood Estimation (MLE)",
   "Posterior Distribution"
  ],
  "uses": [],
  "page": 432,
  "summary": "For large $n$, the likelihood function looks approximately normal in $\\theta$ around the MLE, so both the posterior distribution and the sampling distribution of the MLE are approximately normal."
 },
 {
  "name": "EM Algorithm",
  "type": "concept",
  "existing": false,
  "parent": "Properties of Maximum Likelihood Estimators",
  "prereqs": [
   "Maximum Likelihood Estimation (MLE)"
  ],
  "uses": [],
  "page": 434,
  "summary": "An iterative E-step/M-step procedure for approximating the MLE when missing data make direct maximization of the likelihood difficult; the log-likelihood increases every iteration but only a local maximum is guaranteed."
 },
 {
  "name": "MLE Independence from Sampling Plan",
  "type": "concept",
  "existing": false,
  "parent": "Properties of Maximum Likelihood Estimators",
  "prereqs": [
   "Likelihood Function",
   "Maximum Likelihood Estimation (MLE)"
  ],
  "uses": [],
  "page": 439,
  "summary": "If the decision to stop sampling depends only on data seen so far, the likelihood is proportional to the fixed-sample-size likelihood, so the MLE does not depend on which such sampling plan was used."
 },
 {
  "name": "Newton's Method for Gamma Shape MLE",
  "type": "problem",
  "existing": false,
  "parent": "Properties of Maximum Likelihood Estimators",
  "prereqs": [],
  "uses": [
   "Newton's Method"
  ],
  "page": 430,
  "summary": "Applies one Newton iteration, using digamma and trigamma values, to approximate the MLE of a gamma shape parameter."
 },
 {
  "name": "EM Algorithm for Heights and Weights (Missing Data)",
  "type": "problem",
  "existing": false,
  "parent": "Properties of Maximum Likelihood Estimators",
  "prereqs": [],
  "uses": [
   "EM Algorithm"
  ],
  "page": 435,
  "summary": "Computes the E-step conditional mean and variance for a missing bivariate-normal coordinate given partially observed height/weight data."
 },
 {
  "name": "EM Algorithm for a Mixture of Two Normals",
  "type": "problem",
  "existing": false,
  "parent": "Properties of Maximum Likelihood Estimators",
  "prereqs": [],
  "uses": [
   "EM Algorithm"
  ],
  "page": 437,
  "summary": "Derives the M-step weighted-average updates for a two-component normal mixture fit by EM."
 },
 {
  "name": "Sampling Distribution of the Uniform Upper-Bound MLE",
  "type": "problem",
  "existing": false,
  "parent": "Properties of Maximum Likelihood Estimators",
  "prereqs": [],
  "uses": [
   "MLE for Uniform Distribution"
  ],
  "page": 434,
  "summary": "Gives the mean and variance of $\\hat\\theta=\\max\\{X_1,\\dots,X_n\\}$, the MLE of the upper bound of a Uniform(0,$\\theta$) distribution."
 }
]
```

# Frankenstein problems

**Frankenstein 1: Gamma Shape via Method of Moments, Newton's Method, and Invariance**
A sample of $n=20$ i.i.d. Gamma($\alpha$,1) observations has $\bar x=3.679$ and $\frac1{20}\sum\log x_i=1.220$.

(a) Give the method of moments estimate of $\alpha$.
(b) Use it as the initial guess $\alpha_0$ for one step of Newton's method toward the digamma equation $\psi(\alpha)=1.220$, given $\psi(\alpha_0)=1.1607$ and $\psi'(\alpha_0)=0.3120$.
(c) Using the invariance property, give the (updated) MLE of $\psi=1/\alpha$, the reciprocal shape parameter.

**Solution.**
(a) The mean of Gamma($\alpha$,1) is $\mu_1(\alpha)=\alpha$, so the method of moments estimator is $\hat\alpha=m_1=\bar x=3.679$.

(b) $\alpha_1=\alpha_0-\dfrac{\psi(\alpha_0)-1.220}{\psi'(\alpha_0)}=3.679-\dfrac{1.1607-1.220}{0.3120}=3.679-(-0.1901)=3.679+0.1901\approx 3.871$.

(c) By the invariance property, the MLE of $\psi=1/\alpha$ is $1/\hat\alpha$ evaluated at the best available MLE, $\hat\alpha\approx3.871$: $\hat\psi=1/3.871\approx 0.2583$.

Concepts tested: Method of Moments, Newton's Method, Invariance Property of MLEs.

**Frankenstein 2: Stopping Rule, Asymptotic Normality, and Consistency for an Exponential Rate**
An experimenter samples Exponential($\theta$) interarrival times one at a time, stopping according to a rule that depends only on the observations seen so far. She stops after $n=25$ observations with sample mean $\bar x=5$.

(a) State the MLE of $\theta$ and explain why it is legitimate to use it despite the informal stopping rule.
(b) Using the asymptotic normal approximation to the MLE's sampling distribution, approximate $Var(\hat\theta)$ for this $n$.
(c) Argue that the sequence of such MLEs is consistent as $n\to\infty$.

**Solution.**
(a) Because the stopping rule depends only on data already observed, the likelihood is proportional to the fixed-$n$ likelihood $f(x_1\mid\theta)\cdots f(x_n\mid\theta)$, so the ordinary MLE formula applies: $\hat\theta=1/\bar x=1/5=0.2$.

(b) For the exponential MLE, $V_n(\theta)=\theta^2$, so $Var(\hat\theta)\approx V_n(\hat\theta)/n=\hat\theta^2/n=(0.2)^2/25=0.04/25=0.0016$ (SD $\approx0.04$).

(c) $\hat\theta_n=1/\bar X_n$ is a continuous function of $\bar X_n$, and by the law of large numbers $\bar X_n\to1/\theta$ in probability as $n\to\infty$; hence $\hat\theta_n\to\theta$ in probability, so the sequence of MLEs is consistent, matching the general consistency result for MLEs.

Concepts tested: MLE Independence from Sampling Plan, Asymptotic Normality of the MLE, Consistency of the MLE.
