---
type: reference
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "DeGroot 9.1 Testing Hypotheses"
tags:
  - decks
---
# STAT 132 Cards - DeGroot 9.1 Testing Hypotheses

## Null and Alternative Hypotheses
| Front | Back | Notes |
| --- | --- | --- |
| What is the null hypothesis $H_0$? | The hypothesis that $\theta \in \Theta_0$. | p.546; definition |
| What does "reject $H_0$" mean? | Deciding that $\theta \in \Theta_1$, the alternative. | p.546; definition |
| What does "do not reject $H_0$" mean about our belief in $H_0$? | Only that the data landed in $S_0$; it does not mean we believe $H_0$ is true. | p.560; discrimination |

## Simple and Composite Hypotheses
| Front | Back | Notes |
| --- | --- | --- |
| When is a hypothesis $H_i$ simple? | When $\Theta_i$ contains exactly one value of $\theta$. | p.547; definition |
| When is a hypothesis composite? | When $\Theta_i$ contains more than one value of $\theta$. | p.547; definition |

## One-Sided and Two-Sided Hypotheses
| Front | Back | Notes |
| --- | --- | --- |
| Give the form of a one-sided null hypothesis. | $H_0: \theta \le \theta_0$ or $H_0: \theta \ge \theta_0$. | p.547; definition |
| If $H_0$ is simple ($\theta=\theta_0$), what form does $H_1$ usually take? | Two-sided: $H_1: \theta \neq \theta_0$. | p.547; definition |

## Critical Region
| Front | Back | Notes |
| --- | --- | --- |
| Define the critical region $S_1$ of a test. | The subset of the sample space for which we reject $H_0$. | p.547; definition |
| What is $S_0$, the complement of the critical region? | The set of data values for which we do not reject $H_0$. | p.548; definition |

## Test Statistic and Rejection Region
| Front | Back | Notes |
| --- | --- | --- |
| Define a test statistic $T$ and its rejection region $R$. | $T=r(X)$ is the test statistic; the test rejects $H_0$ when $T \in R$, and $R$ is the rejection region. | p.548; definition |
| If a test rejects $H_0$ when $T \ge c$, what is $R$? | $R=[c,\infty)$. | p.548; procedure |

## Power Function
| Front | Back | Notes |
| --- | --- | --- |
| Define the power function $\pi(\theta\mid\delta)$. | $\pi(\theta\mid\delta)=\Pr(X\in S_1\mid\theta)$, the probability the test rejects $H_0$ when the true parameter is $\theta$. | p.549; definition |
| What would the ideal power function look like? | $\pi(\theta\mid\delta)=0$ for every $\theta\in\Theta_0$ and $\pi(\theta\mid\delta)=1$ for every $\theta\in\Theta_1$. | p.549; definition |
| How should a good power function behave as $\theta$ moves from $\Theta_0$ into $\Theta_1$? | It should increase, since power should be higher on $\Theta_1$ than on $\Theta_0$. | p.554; discrimination |

## Type I and Type II Error
| Front | Back | Notes |
| --- | --- | --- |
| Define a Type I error. | Rejecting $H_0$ when it is true (an error of the first kind). | p.550; definition |
| Define a Type II error. | Not rejecting $H_0$ when it is false (an error of the second kind). | p.550; definition |
| For $\theta\in\Theta_1$, what does $1-\pi(\theta\mid\delta)$ represent? | The probability of a Type II error at that $\theta$. | p.550; formula |

## Level and Size of a Test
| Front | Back | Notes |
| --- | --- | --- |
| Define the size $\alpha(\delta)$ of a test. | $\alpha(\delta)=\sup_{\theta\in\Theta_0}\pi(\theta\mid\delta)$, the largest Type I error probability over $\Theta_0$. | p.551; formula |
| When is a test called a level $\alpha_0$ test? | When its size satisfies $\alpha(\delta)\le\alpha_0$. | p.551; definition |
| If $H_0$ is simple ($\theta=\theta_0$), how does the size formula simplify? | $\alpha(\delta)=\pi(\theta_0\mid\delta)$. | p.551; formula |
| Given a test's size, what range of values counts as a valid level of significance for it? | Every number from the size up to 1. | p.560; discrimination |

## p-value
| Front | Back | Notes |
| --- | --- | --- |
| Define the p-value of observed data. | The smallest level $\alpha_0$ at which we would reject $H_0$ with the observed data. | p.553; definition |
| For a test that rejects $H_0$ when $T\ge c$, give the formula for the p-value when $T=t$ is observed. | $\sup_{\theta\in\Theta_0}\Pr(T\ge t\mid\theta)$. | p.554; formula |
| Given a p-value of 0.0054, at which levels $\alpha_0$ is $H_0$ rejected? | Every level $\alpha_0 \ge 0.0054$. | p.553; discrimination |

## Likelihood Ratio Test
| Front | Back | Notes |
| --- | --- | --- |
| Define the likelihood ratio statistic $\Lambda(x)$. | $\Lambda(x)=\dfrac{\sup_{\theta\in\Theta_0} f_n(x\mid\theta)}{\sup_{\theta\in\Theta} f_n(x\mid\theta)}$. | p.558; formula |
| When does a likelihood ratio test reject $H_0$? | When $\Lambda(x)\le k$ for a chosen constant $k$. | p.558; definition |
| If $H_0$ fixes $k$ coordinates of $\theta$, what is the large-sample limiting distribution of $-2\log\Lambda(X)$ under $H_0$? | Chi-square with $k$ degrees of freedom. | p.559; formula |

## Confidence Set
| Front | Back | Notes |
| --- | --- | --- |
| Define a coefficient $\gamma$ confidence set for $g(\theta)$. | A random set $\omega(X)$ with $\Pr[g(\theta_0)\in\omega(X)\mid\theta=\theta_0]\ge\gamma$ for all $\theta_0$. | p.556; definition |
| Given level $\alpha_0$ tests $\delta_{g_0}$ of $H_{0,g_0}:g(\theta)=g_0$ (with $\gamma=1-\alpha_0$), how is the matching confidence set built? | $\omega(x)=\{g_0 : \delta_{g_0}$ does not reject $H_{0,g_0}$ at $x\}$. | p.556; formula |

## Egyptian Skulls
| Front | Back | Notes |
| --- | --- | --- |
| In the Egyptian Skulls example, why is $H_0:\mu\ge 140$ chosen over $H_0:\mu\le140$ when testing whether skull breadth decreased over time? | So that falsely confirming the theory ($\mu<140$) becomes the Type I error, the one held to a tight significance level. | p.550; procedure |

## Z Test for Normal Mean (Known Variance)
| Front | Back | Notes |
| --- | --- | --- |
| For testing $H_0:\mu=\mu_0$ with known $\sigma^2$, what test statistic and rejection rule give an exact level $\alpha_0$ test? | $Z=\sqrt n\,(\bar X_n-\mu_0)/\sigma$; reject $H_0$ if $\vert Z\vert \ge \Phi^{-1}(1-\alpha_0/2)$. | p.552; formula |

## Bernoulli Test Rejection Threshold
| Front | Back | Notes |
| --- | --- | --- |
| Testing $H_0:p\le0.3$ vs $H_1:p>0.3$ with $Y\sim\text{Binomial}(10,0.3)$, rejecting when $Y\ge c$, and wanting $\alpha_0=0.1$: what is the smallest valid $c$ and the resulting size? | $c=6$; size $=\Pr(Y\ge6\mid p=0.3)=0.0473$. | p.554; procedure |
# Node map
```json
[
 {
  "name": "Null and Alternative Hypotheses",
  "type": "concept",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [],
  "uses": [],
  "page": 546,
  "summary": "$H_0:\\theta\\in\\Theta_0$ and $H_1:\\theta\\in\\Theta_1$ partition the parameter space; rejecting $H_0$ means deciding $\\theta\\in\\Theta_1$."
 },
 {
  "name": "Simple and Composite Hypotheses",
  "type": "concept",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [
   "Null and Alternative Hypotheses"
  ],
  "uses": [],
  "page": 547,
  "summary": "A hypothesis is simple if its parameter set has one point, composite if it has more than one."
 },
 {
  "name": "One-Sided and Two-Sided Hypotheses",
  "type": "concept",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [
   "Null and Alternative Hypotheses"
  ],
  "uses": [],
  "page": 547,
  "summary": "One-sided hypotheses use $\\le$ or $\\ge$; when $H_0$ is simple the alternative is usually two-sided ($\\neq$)."
 },
 {
  "name": "Critical Region",
  "type": "concept",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [
   "Null and Alternative Hypotheses"
  ],
  "uses": [],
  "page": 547,
  "summary": "The subset $S_1$ of the sample space on which the test rejects $H_0$."
 },
 {
  "name": "Test Statistic and Rejection Region",
  "type": "concept",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [
   "Critical Region"
  ],
  "uses": [],
  "page": 548,
  "summary": "A test statistic $T=r(X)$ with rejection region $R$ defines the test: reject $H_0$ if $T\\in R$."
 },
 {
  "name": "Power Function",
  "type": "concept",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [
   "Test Statistic and Rejection Region"
  ],
  "uses": [],
  "page": 549,
  "summary": "$\\pi(\\theta\\mid\\delta)=\\Pr(X\\in S_1\\mid\\theta)$ is the probability a test rejects $H_0$ as a function of $\\theta$."
 },
 {
  "name": "Type I and Type II Error",
  "type": "concept",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [
   "Power Function"
  ],
  "uses": [],
  "page": 550,
  "summary": "Type I error rejects a true $H_0$; Type II error fails to reject a false $H_0$."
 },
 {
  "name": "Level and Size of a Test",
  "type": "concept",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [
   "Power Function",
   "Type I and Type II Error"
  ],
  "uses": [],
  "page": 551,
  "summary": "The size $\\alpha(\\delta)=\\sup_{\\theta\\in\\Theta_0}\\pi(\\theta\\mid\\delta)$; a level $\\alpha_0$ test has size at most $\\alpha_0$."
 },
 {
  "name": "p-value",
  "type": "concept",
  "existing": true,
  "parent": "Hypothesis Testing",
  "prereqs": [
   "Level and Size of a Test"
  ],
  "uses": [],
  "page": 553,
  "summary": "The smallest significance level at which the observed data would lead to rejecting $H_0$."
 },
 {
  "name": "Likelihood Ratio Test",
  "type": "concept",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [
   "Likelihood Function",
   "Level and Size of a Test"
  ],
  "uses": [],
  "page": 558,
  "summary": "Rejects $H_0$ when the likelihood ratio $\\Lambda(x)=\\sup_{\\Theta_0}f_n/\\sup_{\\Theta}f_n$ is small; $-2\\log\\Lambda$ is asymptotically chi-square."
 },
 {
  "name": "Confidence Set",
  "type": "concept",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [
   "Confidence Intervals",
   "Level and Size of a Test"
  ],
  "uses": [],
  "page": 556,
  "summary": "A coefficient $\\gamma$ confidence set for $g(\\theta)$ is the dual object to a family of level $1-\\gamma$ tests."
 },
 {
  "name": "Egyptian Skulls",
  "type": "problem",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [],
  "uses": [
   "Null and Alternative Hypotheses",
   "One-Sided and Two-Sided Hypotheses",
   "Type I and Type II Error"
  ],
  "page": 550,
  "summary": "Choosing which hypothesis is null so that the more serious error (falsely confirming the theory) is Type I."
 },
 {
  "name": "Z Test for Normal Mean (Known Variance)",
  "type": "problem",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [],
  "uses": [
   "Test Statistic and Rejection Region",
   "Power Function",
   "Level and Size of a Test"
  ],
  "page": 552,
  "summary": "Deriving the exact level $\\alpha_0$ two-sided Z test for a normal mean with known variance."
 },
 {
  "name": "Bernoulli Test Rejection Threshold",
  "type": "problem",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [],
  "uses": [
   "Test Statistic and Rejection Region",
   "Level and Size of a Test"
  ],
  "page": 554,
  "summary": "Finding the smallest integer threshold $c$ for a Binomial test statistic that keeps size at or below $\\alpha_0$."
 }
]
```

# Frankenstein problems

**Problem 1**
A quality engineer models a machine's output as $X_1,\dots,X_{25}$ i.i.d. Normal with unknown mean $\mu$ and known $\sigma=4$. She tests $H_0:\mu=50$ vs $H_1:\mu\neq50$ at level $\alpha_0=0.05$ and observes $\bar x_{25}=51.6$.

a. Give the test statistic and rejection region.
b. Compute the observed statistic and state the decision.
c. Compute the p-value.
d. Which type of error is possible given this decision?

**Solution**

a. $Z=\sqrt{25}(\bar X_{25}-50)/4$; reject $H_0$ if $|Z|\ge\Phi^{-1}(0.975)=1.96$.

b. $Z=5(51.6-50)/4=5(1.6)/4=8/4=2.0$. Since $|2.0|\ge1.96$, reject $H_0$.

c. p-value $=2(1-\Phi(2.0))=2(1-0.9772)=2(0.0228)=0.0456$.

d. Since $H_0$ was rejected, the possible error is a Type I error (rejecting a true $H_0$).

Concepts used: Test Statistic and Rejection Region, Power Function, Level and Size of a Test, Type I and Type II Error, p-value.

**Problem 2**
For $n=10$ Bernoulli trials with $Y$ the number of successes, an analyst tests $H_0:\theta=0.3$ vs $H_1:\theta\neq0.3$ using the likelihood ratio statistic $\Lambda(y)$. From Table 9.1, the smallest values of $\Lambda(y)$ occur at $y=10,9,8,7,0$, with $\Pr(Y=y\mid\theta=0.3)$ summing to $0.039$ over that set (the next smallest, adding $y=6$, would push the sum to $0.076$).

a. State whether $H_0$ and $H_1$ are each simple or composite.
b. Find the rejection set for a level $\alpha_0=0.05$ likelihood ratio test and its exact size.
c. If $Y=9$ is observed, state the decision and which type of error is possible.

**Solution**

a. $H_0:\theta=0.3$ is simple (one point); $H_1:\theta\neq0.3$ is composite (all other values in $[0,1]$).

b. Since $0.039\le0.05$ but adding $y=6$ gives $0.076>0.05$, the rejection set is $\{0,7,8,9,10\}$, with exact size $0.039$.

c. $Y=9$ is in $\{0,7,8,9,10\}$, so $H_0$ is rejected. The possible error is a Type I error (rejecting a true $H_0$).

Concepts used: Simple and Composite Hypotheses, Likelihood Ratio Test, Level and Size of a Test, Type I and Type II Error.
