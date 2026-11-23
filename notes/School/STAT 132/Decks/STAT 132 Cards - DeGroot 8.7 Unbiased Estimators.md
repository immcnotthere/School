---
type: reference
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "DeGroot 8.7 Unbiased Estimators"
tags:
  - decks
---
# STAT 132 Cards - DeGroot 8.7 Unbiased Estimators

## Unbiased Estimator
| Front | Back | Notes |
| --- | --- | --- |
| Definition: when is estimator $\delta(X)$ an unbiased estimator of $g(\theta)$? | When $E_\theta[\delta(X)]=g(\theta)$ for every possible value of $\theta$. | p.521; definition |
| Definition of the bias of an estimator $\delta$ of $g(\theta)$? | $E_\theta[\delta(X)]-g(\theta)$. | p.521; definition |
| $\delta$ is unbiased if and only if its bias equals what, for all $\theta$? | 0. | p.521; definition |
| Sample mean $X_n$ as estimator of the population mean $\theta$: unbiased or biased? | Unbiased; $E_\theta(X_n)=\theta$ for all $\theta$. | p.521; discrimination |

## Mean Squared Error (MSE)
| Front | Back | Notes |
| --- | --- | --- |
| General formula for the M.S.E. of an estimator $\delta$ of $g(\theta)$? | $E_\theta[(\delta-g(\theta))^2]$. | p.521; definition |
| If $\delta$ is unbiased, what does its M.S.E. equal? | Its variance, $Var_\theta(\delta)$. | p.521; formula |

## MSE Bias-Variance Decomposition
| Front | Back | Notes |
| --- | --- | --- |
| Corollary 8.7.1: M.S.E. of $\delta$ (finite variance) in terms of its variance and bias? | $MSE(\delta) = Var_\theta(\delta) + [\text{bias}(\delta)]^2$ | p.521; formula |
| Yes or no, and why: does an unbiased estimator with high variance necessarily give estimates close to $g(\theta)$? | No; unbiasedness alone doesn't guarantee low M.S.E. A widely spread-out but unbiased estimator can be far from $g(\theta)$ with high probability. | p.521; concept |

## Unbiased Estimation of the Mean
| Front | Back | Notes |
| --- | --- | --- |
| For $g(\theta)=E_\theta(X_1)$, what is the M.S.E. of the sample mean $X_n$ as an estimator? | $Var_\theta(X_1)/n$. | p.524; formula |

## Unbiased Estimator of the Variance
| Front | Back | Notes |
| --- | --- | --- |
| Theorem 8.7.1: unbiased estimator $\hat\sigma_1^2$ of $Var_\theta(X_1)$, for a general distribution? | $\hat\sigma_1^2 = \dfrac{1}{n-1}\sum_{i=1}^n (X_i-X_n)^2$ | p.523; formula |
| What is $E(\hat\sigma_0^2)$ for the divide-by-$n$ sample variance $\hat\sigma_0^2=\frac1n\sum(X_i-X_n)^2$? | $\dfrac{n-1}{n}\sigma^2$; i.e. $\hat\sigma_0^2$ is biased low. | p.524; formula |
| How do you convert the biased $\hat\sigma_0^2$ into the unbiased $\hat\sigma_1^2$? | Multiply by $n/(n-1)$. | p.524; procedure |
| $\hat\sigma_0^2$ vs $\hat\sigma_1^2$: which is the M.L.E. for a normal sample, and which is unbiased for a general distribution? | $\hat\sigma_0^2$ (divide by $n$) is the M.L.E. for the normal case; $\hat\sigma_1^2$ (divide by $n-1$) is unbiased for the variance of any distribution with finite variance. | p.524; discrimination |

## Minimum MSE Estimator of the Normal Variance
| Front | Back | Notes |
| --- | --- | --- |
| For a normal sample, $T_c=c\sum(X_i-X_n)^2$: formulas for $E(T_c)$ and $Var(T_c)$? | $E(T_c)=(n-1)c\sigma^2$, $Var(T_c)=2(n-1)c^2\sigma^4$ | p.525; formula |
| Which value of $c$ minimizes the M.S.E. of $T_c$ for every possible $\mu,\sigma^2$? | $c=1/(n+1)$. | p.525; formula |
| Yes or no, and why: does the M.S.E.-minimizing $T_{1/(n+1)}$ beat both $\hat\sigma_0^2$ ($c=1/n$) and $\hat\sigma_1^2$ ($c=1/(n-1)$)? | Yes, strictly smaller M.S.E. than both, for every $\mu,\sigma^2$ (though Stein 1964 later showed even $T_{1/(n+1)}$ is inadmissible). | p.525-526; concept |

## Limitations of Unbiased Estimation
| Front | Back | Notes |
| --- | --- | --- |
| Yes or no, and why: can a biased estimator ever have smaller M.S.E. than every unbiased estimator, for every $\theta$? | Yes; e.g. $T_{1/(n+1)}$ for the normal variance beats every $T_c$ including the unbiased $\hat\sigma_1^2$, for all $\mu,\sigma^2$. | p.526; concept |
| Yes or no, and why: nonexistence limitation: for $n$ Bernoulli($p$) trials, does an unbiased estimator of $p^{1/2}$ exist? | No; no unbiased estimator of $\sqrt p$ exists, even though $X_n$ unbiasedly estimates $p$ itself. | p.526; concept |
| Inappropriate-estimator limitation: for the geometric($p$) distribution based on one observation $X$, what is the only unbiased estimator of $p$? | $\delta(X)=1$ if $X=0$, $\delta(X)=0$ if $X>0$: a degenerate, unreasonable-looking rule. | p.526; concept |
| Ignoring-information limitation: in the truncated-voltmeter example, why must the unbiased estimator change even though the actual observed reading (2.5V) is untouched by truncation? | Because possible truncation changes the sample space and distribution of $X$, so the unbiased-estimator formula for $\theta$ must change, even though this particular observed value was unaffected. | p.527; concept |

## Electronic Components Bias and MSE Comparison
| Front | Back | Notes |
| --- | --- | --- |
| Electronic components: $\hat\theta=3/T$ (M.L.E.) has $E(\hat\theta)=3\theta/2$, $Var(\hat\theta)=9\theta^2/4$; unbiased alt $\delta=2/T$; also $\delta^*=1/T$ with $Var=[\text{bias}]^2=\theta^2/4$. Key move to rank them by M.S.E.? | $MSE=Var+bias^2$. $MSE(\hat\theta)=9\theta^2/4+\theta^2/4=5\theta^2/2$ (worst); $MSE(\delta)=\theta^2+0=\theta^2$ (unbiased); $MSE(\delta^*)=\theta^2/4+\theta^2/4=\theta^2/2$ (best, despite being biased). | p.522-523; problem |

## Poisson Combined Unbiased Estimator
| Front | Back | Notes |
| --- | --- | --- |
| Poisson sample: both $X_n$ and $\hat\sigma_1^2$ are unbiased for $\theta$ (mean = variance). Key move to build a whole family of unbiased estimators from them? | Any combination $\alpha X_n+(1-\alpha)\hat\sigma_1^2$ for constant $\alpha$ is unbiased for $\theta$, since $E[\alpha X_n+(1-\alpha)\hat\sigma_1^2]=\alpha\theta+(1-\alpha)\theta=\theta$. | p.524-525; problem |

# Node map
```json
[
 {
  "name": "Unbiased Estimator",
  "type": "concept",
  "existing": false,
  "parent": "Estimators",
  "prereqs": [
   "Estimators",
   "Estimator vs Estimate"
  ],
  "uses": [],
  "page": 521,
  "summary": "$\\delta(X)$ is an unbiased estimator of $g(\\theta)$ if $E_\\theta[\\delta(X)]=g(\\theta)$ for every $\\theta$; the bias is $E_\\theta[\\delta(X)]-g(\\theta)$."
 },
 {
  "name": "Mean Squared Error (MSE)",
  "type": "concept",
  "existing": false,
  "parent": "Estimators",
  "prereqs": [
   "Unbiased Estimator",
   "Expectation and Variance"
  ],
  "uses": [],
  "page": 521,
  "summary": "The M.S.E. of an estimator $\\delta$ of $g(\\theta)$ is $E_\\theta[(\\delta-g(\\theta))^2]$; equals the variance when $\\delta$ is unbiased."
 },
 {
  "name": "MSE Bias-Variance Decomposition",
  "type": "concept",
  "existing": false,
  "parent": "Estimators",
  "prereqs": [
   "Mean Squared Error (MSE)",
   "Unbiased Estimator"
  ],
  "uses": [],
  "page": 521,
  "summary": "For any estimator with finite variance, $MSE(\\delta)=Var_\\theta(\\delta)+[\\text{bias}(\\delta)]^2$ (Corollary 8.7.1)."
 },
 {
  "name": "Unbiased Estimation of the Mean",
  "type": "concept",
  "existing": false,
  "parent": "Estimators",
  "prereqs": [
   "Unbiased Estimator",
   "Sample Mean"
  ],
  "uses": [],
  "page": 524,
  "summary": "The sample mean $X_n$ is unbiased for $E_\\theta(X_1)$ for any distribution with finite mean/variance, with M.S.E. $Var_\\theta(X_1)/n$."
 },
 {
  "name": "Unbiased Estimator of the Variance",
  "type": "concept",
  "existing": false,
  "parent": "Estimators",
  "prereqs": [
   "Unbiased Estimator",
   "Sample Mean and Sample Variance"
  ],
  "uses": [],
  "page": 523,
  "summary": "$\\hat\\sigma_1^2=\\frac{1}{n-1}\\sum(X_i-X_n)^2$ is unbiased for $Var_\\theta(X_1)$ for a general distribution; the divide-by-$n$ version $\\hat\\sigma_0^2$ is biased low by a factor $(n-1)/n$."
 },
 {
  "name": "Minimum MSE Estimator of the Normal Variance",
  "type": "concept",
  "existing": false,
  "parent": "Estimators",
  "prereqs": [
   "Unbiased Estimator of the Variance",
   "MSE Bias-Variance Decomposition",
   "Chi-Square Distribution"
  ],
  "uses": [],
  "page": 525,
  "summary": "Among estimators $T_c=c\\sum(X_i-X_n)^2$ for a normal sample, $c=1/(n+1)$ minimizes the M.S.E. for every $\\mu,\\sigma^2$, beating both $\\hat\\sigma_0^2$ and $\\hat\\sigma_1^2$."
 },
 {
  "name": "Limitations of Unbiased Estimation",
  "type": "concept",
  "existing": false,
  "parent": "Estimators",
  "prereqs": [
   "Unbiased Estimator",
   "MSE Bias-Variance Decomposition"
  ],
  "uses": [],
  "page": 526,
  "summary": "Unbiasedness can be beaten in M.S.E. by biased estimators, can fail to exist (e.g. for $p^{1/2}$), can force silly/degenerate estimators, and can force ignoring relevant information."
 },
 {
  "name": "Electronic Components Bias and MSE Comparison",
  "type": "problem",
  "existing": false,
  "parent": "Estimators",
  "prereqs": [],
  "uses": [
   "Unbiased Estimator",
   "MSE Bias-Variance Decomposition"
  ],
  "page": 522,
  "summary": "Compares the M.L.E. $3/T$, the unbiased $2/T$, and the biased $1/T$ as estimators of a failure rate $\\theta$ by M.S.E."
 },
 {
  "name": "Poisson Combined Unbiased Estimator",
  "type": "problem",
  "existing": false,
  "parent": "Estimators",
  "prereqs": [],
  "uses": [
   "Unbiased Estimation of the Mean",
   "Unbiased Estimator of the Variance",
   "Poisson Distribution"
  ],
  "page": 524,
  "summary": "Since $X_n$ and $\\hat\\sigma_1^2$ are both unbiased for a Poisson mean, any linear combination $\\alpha X_n+(1-\\alpha)\\hat\\sigma_1^2$ is also unbiased."
 }
]
```

# Frankenstein problems

**Problem 1.** Let $X_1,\dots,X_8$ be a random sample from a normal distribution with unknown mean $\mu$ and unknown variance $\sigma^2$. The observed sum of squared deviations is $s_n^2=\sum(x_i-x_n)^2=56$.
(a) Give the unbiased estimate of $\sigma^2$.
(b) Consider $T_c=c\cdot s_n^2$. Find the value $c^*$ that minimizes the M.S.E. of $T_c$ for every $\mu,\sigma^2$, and compute the numeric value of $T_{c^*}$.
(c) Express the bias of $T_{c^*}$ as an estimator of $\sigma^2$ in terms of $\sigma^2$.

*Concepts tested:* Unbiased Estimator of the Variance, Minimum MSE Estimator of the Normal Variance, MSE Bias-Variance Decomposition, Mean Squared Error (MSE).

*Solution.*
(a) $\hat\sigma_1^2 = s_n^2/(n-1) = 56/7 = 8$.
(b) $c^*=1/(n+1)=1/9$. $T_{c^*}=56/9 = 6.222$.
(c) $E(T_{c^*})=(n-1)c^*\sigma^2 = 7(1/9)\sigma^2 = (7/9)\sigma^2$. Bias $= (7/9)\sigma^2-\sigma^2 = -(2/9)\sigma^2$ (biased low).

**Problem 2.** Let $X_1,\dots,X_5$ be i.i.d. Bernoulli($p$). Let $\delta(X)=X_5$ (sample mean, i.e. the proportion of successes) and let $\delta'(X)=\dfrac{X_5+1}{2}$ be a shrinkage-toward-1 alternative. Evaluate both estimators of $p$ at $p=0.5$: find the bias and M.S.E. of each, and say which is better at that value of $p$.

*Concepts tested:* Unbiased Estimator, MSE Bias-Variance Decomposition, Mean Squared Error (MSE), Bernoulli Distribution.

*Solution.* $Var(X_5)=p(1-p)/n=0.25/5=0.05$.
$\delta$ is unbiased, so $MSE(\delta)=Var(\delta)=0.05$.
$E(\delta')=(p+1)/2$, so bias $=(1-p)/2=0.25$; $Var(\delta')=Var(X_5)/4=0.0125$; $MSE(\delta')=0.0125+0.25^2=0.075$.
At $p=0.5$, the unbiased estimator $\delta$ has the smaller M.S.E. (0.05 vs 0.075): the shrinkage toward 1 adds more squared bias than it saves in variance here.
