---
type: reference
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "DeGroot 9.5 The t Test"
tags:
  - decks
---
# STAT 132 Cards - DeGroot 9.5 The t Test

## t-statistic
| Front | Back | Notes |
| --- | --- | --- |
| Define the t test statistic $U$ for a normal mean with unknown variance. | $U=\sqrt n\,(\bar X_n-\mu_0)/\hat\sigma$, where $\hat\sigma^2=\frac{1}{n-1}\sum(X_i-\bar X_n)^2$. | p.591; formula |

## One-Sided t Test
| Front | Back | Notes |
| --- | --- | --- |
| For $H_0:\mu\le\mu_0$ vs $H_1:\mu>\mu_0$, give the level $\alpha_0$ t test rejection rule. | Reject $H_0$ if $U\ge T_{n-1}^{-1}(1-\alpha_0)$. | p.592; procedure |
| For $H_0:\mu\ge\mu_0$ vs $H_1:\mu<\mu_0$, give the level $\alpha_0$ t test rejection rule. | Reject $H_0$ if $U\le T_{n-1}^{-1}(\alpha_0)$. | p.592; procedure |
| For the one-sided t test of $H_0:\mu\le\mu_0$, what does the power function equal exactly at $\mu=\mu_0$? | $\alpha_0$; the test has exact size $\alpha_0$ and is unbiased. | p.592; formula |

## Two-Sided t Test
| Front | Back | Notes |
| --- | --- | --- |
| For $H_0:\mu=\mu_0$ vs $H_1:\mu\neq\mu_0$, give the level $\alpha_0$ t test rejection rule. | Reject $H_0$ if $\vert U\vert \ge T_{n-1}^{-1}(1-\alpha_0/2)$. | p.596; procedure |
| Why might the same data reject a one-sided $H_0:\mu\le\mu_0$ but fail to reject the two-sided $H_0:\mu=\mu_0$ at the same level? | The two-sided test splits $\alpha_0$ across both tails, so it needs a larger $\vert U\vert $ to reject than the one-sided test needs. | p.596; discrimination |

## p-values for t Tests
| Front | Back | Notes |
| --- | --- | --- |
| For $H_0:\mu\le\mu_0$ (reject if $U\ge c$), give the p-value formula for observed $u$. | $1-T_{n-1}(u)$. | p.593; formula |
| For $H_0:\mu\ge\mu_0$ (reject if $U\le c$), give the p-value formula for observed $u$. | $T_{n-1}(u)$. | p.593; formula |
| For the two-sided hypotheses $H_0:\mu=\mu_0$, give the p-value formula for observed $u$. | $2[1-T_{n-1}(\vert u\vert )]$. | p.598; formula |

## Noncentral t Distribution
| Front | Back | Notes |
| --- | --- | --- |
| Define the noncentral $t$ distribution with $m$ degrees of freedom and noncentrality $\psi$. | The distribution of $X=W/\sqrt{Y/m}$, where $W\sim N(\psi,1)$ and $Y\sim\chi^2_m$ are independent. | p.594; definition |
| For the t-statistic $U$, what is the noncentrality parameter $\psi$ when the true mean is $\mu$? | $\psi=\sqrt n\,(\mu-\mu_0)/\sigma$. | p.594; formula |

## Power of the t Test
| Front | Back | Notes |
| --- | --- | --- |
| In terms of the noncentral t c.d.f. $T_{n-1}(\cdot\mid\psi)$, give the power of the test that rejects $H_0:\mu\le\mu_0$ when $U\ge c$. | $\pi(\mu,\sigma^2\mid\delta)=1-T_{n-1}(c\mid\psi)$. | p.594; formula |
| Why can't you answer "what is the power when $\mu=5.5$" without more information? | Power depends on $\mu$ only through $\psi=\sqrt n(\mu-\mu_0)/\sigma$, so $\sigma$ (or the distance from $\mu_0$ in units of $\sigma$) must also be given. | p.595; discrimination |
| How can the power function of a t test guide a choice of sample size? | Find the noncentrality parameter $\psi$ needed for the desired power from the power curves, then solve $\psi=\sqrt n(\mu-\mu_0)/\sigma$ for $n$. | p.596; procedure |

## Paired t Test
| Front | Back | Notes |
| --- | --- | --- |
| How do you turn a two-condition, same-subject experiment into a one-sample t test? | Subtract the two measurements for each subject and treat the differences as a random sample from a normal distribution; test the mean difference. | p.596; procedure |

## t Test as a Likelihood Ratio Test
| Front | Back | Notes |
| --- | --- | --- |
| For $H_0:\mu\le\mu_0$, what is the likelihood ratio statistic $\Lambda(x)$ when $\bar x_n>\mu_0$? | $\Lambda(x)=(\hat\sigma^2/\hat\sigma_0^2)^{n/2}$, where $\hat\sigma_0^2$ is the MLE of $\sigma^2$ with $\mu$ forced to $\mu_0$. | p.599; formula |
| What does $\Lambda(x)$ equal for $H_0:\mu\le\mu_0$ when $\bar x_n\le\mu_0$? | $\Lambda(x)=1$, since the unrestricted MLE of $\mu$ already satisfies $H_0$. | p.599; formula |
| The condition $\Lambda(x)\le k$ turns out equivalent to what condition on the t-statistic? | $U\ge c$ for some constant $c$; the likelihood ratio test for this problem is exactly a t test. | p.600; formula |

## Nursing Homes t Test
| Front | Back | Notes |
| --- | --- | --- |
| Nursing home in-patient days: $n=18$, $\bar x=182.17$, $\hat\sigma=72.22$, testing $H_0:\mu\ge200$ vs $H_1:\mu<200$ at $\alpha_0=0.1$ ($T_{17}^{-1}(0.1)=-1.333$). Compute $U$ and state the decision. | $U=\sqrt{17}(182.17-200)/72.22=-1.018$; since $-1.018>-1.333$, do not reject $H_0$. | p.593; procedure |

## Lengths of Fibers One-Sided vs Two-Sided
| Front | Back | Notes |
| --- | --- | --- |
| Yes or no, and why: fiber lengths: $n=15$, observed $U=1.833$. At $\alpha_0=0.05$, is $H_0:\mu\le5.2$ rejected? Is $H_0:\mu=5.2$ rejected? | One-sided: $1.833>T_{14}^{-1}(0.95)=1.761$, reject. Two-sided: $1.833<T_{14}^{-1}(0.975)=2.145$, do not reject. | pp.593,596; discrimination |

## Crash Test Dummies Paired t Test
| Front | Back | Notes |
| --- | --- | --- |
| Paired head-injury log differences: $n=164$, $\bar x=0.2199$, $\hat\sigma=0.5342$, testing $H_0:\mu\le0$ vs $H_1:\mu>0$ at $\alpha_0=0.01$ ($T_{163}^{-1}(0.99)=2.35$). Compute $U$ and state the decision. | $U=\sqrt{164}(0.2199)/0.5342\approx5.271$; since $5.271>2.35$, reject $H_0$. | p.596; procedure |

## Egyptian Skulls Two-Sided t Test
| Front | Back | Notes |
| --- | --- | --- |
| Egyptian skulls: $n=30$, $\bar x=131.37$, $\hat\sigma=5.129$, testing $H_0:\mu=140$ at $\alpha_0=0.05$ ($T_{29}^{-1}(0.975)=2.045$). Compute $U$ and state the decision. | $U=\sqrt{30}(131.37-140)/5.129\approx-9.219$; since $\vert -9.219\vert >2.045$, reject $H_0$. | p.597; procedure |

## t Distribution of the Sample Mean
| Front | Back | Notes |
| --- | --- | --- |
| What is the distribution of $U$ when $\mu=\mu_0$? | The $t$ distribution with $n-1$ degrees of freedom, regardless of $\sigma^2$. | p.591; formula |

# Node map
```json
[
 {
  "name": "t-statistic",
  "type": "concept",
  "existing": true,
  "parent": "Hypothesis Testing",
  "prereqs": [
   "Sample Mean and Sample Variance"
  ],
  "uses": [],
  "page": 591,
  "summary": "$U=\\sqrt n(\\bar X_n-\\mu_0)/\\hat\\sigma$ has the $t$ distribution with $n-1$ df when $\\mu=\\mu_0$."
 },
 {
  "name": "One-Sided t Test",
  "type": "concept",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [
   "t-statistic"
  ],
  "uses": [],
  "page": 592,
  "summary": "Rejects a one-sided normal-mean hypothesis when $U$ (or $-U$) exceeds a t quantile; has exact size $\\alpha_0$ and is unbiased."
 },
 {
  "name": "Two-Sided t Test",
  "type": "concept",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [
   "t-statistic"
  ],
  "uses": [],
  "page": 596,
  "summary": "Rejects $H_0:\\mu=\\mu_0$ when $|U|\\ge T_{n-1}^{-1}(1-\\alpha_0/2)$."
 },
 {
  "name": "p-values for t Tests",
  "type": "concept",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [
   "One-Sided t Test",
   "Two-Sided t Test",
   "p-value"
  ],
  "uses": [],
  "page": 593,
  "summary": "One-sided p-values are $1-T_{n-1}(u)$ or $T_{n-1}(u)$; the two-sided p-value is $2[1-T_{n-1}(|u|)]$."
 },
 {
  "name": "Noncentral t Distribution",
  "type": "concept",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [
   "t Distribution",
   "t-statistic"
  ],
  "uses": [],
  "page": 594,
  "summary": "Distribution of $W/\\sqrt{Y/m}$ for $W\\sim N(\\psi,1)$, $Y\\sim\\chi^2_m$; governs the t-statistic's distribution when $\\mu\\neq\\mu_0$."
 },
 {
  "name": "Power of the t Test",
  "type": "concept",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [
   "Noncentral t Distribution"
  ],
  "uses": [],
  "page": 594,
  "summary": "Power is $1-T_{n-1}(c\\mid\\psi)$ (one-sided) or a two-tail analog, a function of $\\mu,\\sigma$ only through $\\psi=\\sqrt n(\\mu-\\mu_0)/\\sigma$; used to choose sample size."
 },
 {
  "name": "Paired t Test",
  "type": "concept",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [
   "One-Sided t Test"
  ],
  "uses": [],
  "page": 596,
  "summary": "Differences between paired measurements on the same unit are treated as a normal random sample and tested with a one-sample t test."
 },
 {
  "name": "t Test as a Likelihood Ratio Test",
  "type": "concept",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [
   "Likelihood Function",
   "One-Sided t Test"
  ],
  "uses": [],
  "page": 599,
  "summary": "The likelihood ratio test of a one-sided normal-mean hypothesis reduces exactly to a t test."
 },
 {
  "name": "Nursing Homes t Test",
  "type": "problem",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [],
  "uses": [
   "t-statistic",
   "One-Sided t Test"
  ],
  "page": 593,
  "summary": "Computing U and deciding a one-sided t test for nursing home in-patient days."
 },
 {
  "name": "Lengths of Fibers One-Sided vs Two-Sided",
  "type": "problem",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [],
  "uses": [
   "One-Sided t Test",
   "Two-Sided t Test"
  ],
  "page": 596,
  "summary": "Same data and U give opposite decisions for one-sided vs two-sided hypotheses at the same level."
 },
 {
  "name": "Crash Test Dummies Paired t Test",
  "type": "problem",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [],
  "uses": [
   "Paired t Test",
   "One-Sided t Test"
  ],
  "page": 596,
  "summary": "Testing whether paired head-injury measurements differ by seat, using a one-sided paired t test."
 },
 {
  "name": "Egyptian Skulls Two-Sided t Test",
  "type": "problem",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [],
  "uses": [
   "Two-Sided t Test",
   "t-statistic"
  ],
  "page": 597,
  "summary": "Testing $H_0:\\mu=140$ against a two-sided alternative for skull breadth data."
 },
 {
  "name": "t Distribution of the Sample Mean",
  "type": "concept",
  "existing": true,
  "parent": "",
  "prereqs": [],
  "summary": ""
 }
]
```

# Frankenstein problems

**Problem 1**
A lab measures reaction times (ms) for $n=20$ subjects, modeled as normal with unknown mean $\mu$ and variance. The sample gives $\bar x=245$, $\hat\sigma=18$. Test $H_0:\mu\le240$ vs $H_1:\mu>240$ at $\alpha_0=0.05$, where $T_{19}^{-1}(0.95)=1.729$.

a. Compute $U$.
b. State the decision.
c. Is the p-value greater than or less than 0.05? Explain.
d. Which type of error might have occurred?

**Solution**

a. $U=\sqrt{20}(245-240)/18 = (4.472)(5)/18 = 22.36/18 \approx 1.242$.

b. Since $1.242<1.729$, do not reject $H_0$.

c. The p-value is $1-T_{19}(1.242)$. Since $U=1.242$ is less than the critical value $1.729$ needed to reject at level 0.05, the p-value must be greater than 0.05.

d. Since $H_0$ was not rejected, the possible error is a Type II error (failing to reject a false $H_0$).

Concepts used: t-statistic, One-Sided t Test, p-values for t Tests, Type I and Type II Error.

**Problem 2**
A machine calibration check uses $n=10$ measurements, normal with unknown mean and variance, testing $H_0:\mu=50$ vs $H_1:\mu\neq50$ at $\alpha_0=0.05$, where $T_9^{-1}(0.975)=2.262$. Observed $\bar x=52$, $\hat\sigma=3$.

a. Compute $U$ and state the decision.
b. Give the two-sided p-value formula in terms of $T_9$, evaluated at this $U$.
c. What is the noncentrality parameter $\psi$ if the true mean is $\mu=53$?
d. In terms of $\psi$ and $T_9(\cdot\mid\psi)$, write the power of this test at $\mu=53$.

**Solution**

a. $U=\sqrt{10}(52-50)/3=(3.162)(2)/3\approx2.108$. Since $|2.108|<2.262$, do not reject $H_0$.

b. p-value $=2[1-T_9(|2.108|)]=2[1-T_9(2.108)]$.

c. $\psi=\sqrt{10}(53-50)/3=(3.162)(3)/3\approx3.162$.

d. Power $=T_9(-2.262\mid3.162)+1-T_9(2.262\mid3.162)$.

Concepts used: Two-Sided t Test, p-values for t Tests, Noncentral t Distribution, Power of the t Test.
