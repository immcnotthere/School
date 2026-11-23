---
type: reference
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "DeGroot 8.2 Chi-Square Distributions"
tags:
  - decks
---
# STAT 132 Cards - DeGroot 8.2 Chi-Square Distributions

## Chi-Square Distribution
| Front | Back | Notes |
| --- | --- | --- |
| How is the chi-square distribution with $m$ degrees of freedom defined? | It is the gamma distribution with $\alpha = m/2$ and $\beta = 1/2$. | p.469; definition |
| What is the pdf of the chi-square distribution with $m$ df, for $x>0$? | $f(x) = \dfrac{1}{2^{m/2}\Gamma(m/2)} x^{(m/2)-1} e^{-x/2}$ | p.470; formula |
| The chi-square distribution with 2 degrees of freedom equals which familiar distribution? | The exponential distribution with parameter $1/2$ (mean 2). | p.470; discrimination |

## Chi-Square Distribution Mean Variance and MGF
| Front | Back | Notes |
| --- | --- | --- |
| If $X$ has the chi-square distribution with $m$ df, what is $E(X)$? | $E(X) = m$ | p.470; formula |
| If $X$ has the chi-square distribution with $m$ df, what is $\mathrm{Var}(X)$? | $\mathrm{Var}(X) = 2m$ | p.470; formula |
| What is the mgf of the chi-square distribution with $m$ df, and for what $t$? | $\psi(t) = (1-2t)^{-m/2}$ for $t < 1/2$ | p.470; formula |

## Chi-Square Additivity
| Front | Back | Notes |
| --- | --- | --- |
| If $X_1,\dots,X_k$ are independent with $X_i \sim \chi^2(m_i)$, what is the distribution of $X_1+\dots+X_k$? | Chi-square with $m_1+\dots+m_k$ degrees of freedom. | p.470; formula |
| $X \sim \chi^2(3)$ and $Y \sim \chi^2(5)$ are independent. What is the distribution of $X+Y$? | $\chi^2(8)$ | p.470; procedure |

## Square of a Standard Normal Is Chi-Square
| Front | Back | Notes |
| --- | --- | --- |
| If $X$ has the standard normal distribution, what is the distribution of $Y = X^2$? | Chi-square with 1 degree of freedom. | p.470; formula |
| What pdf results for $Y=X^2$ when $X \sim N(0,1)$, for $y>0$? | $f(y) = \dfrac{1}{\sqrt{2\pi}} y^{-1/2} e^{-y/2}$ | p.471; formula |

## Sum of Squares of iid Standard Normal Is Chi-Square
| Front | Back | Notes |
| --- | --- | --- |
| If $X_1,\dots,X_m$ are iid standard normal, what is the distribution of $X_1^2+\dots+X_m^2$? | Chi-square with $m$ degrees of freedom. | p.471; formula |
| Why is this corollary the main reason the chi-square distribution matters in statistics? | Normal-sample variance estimators are built from sums of squared standardized normals, so their sampling distributions are chi-square. | p.471; discrimination |

## MLE of Variance of a Normal Distribution
| Front | Back | Notes |
| --- | --- | --- |
| For a normal sample with known mean $\mu$, the MLE is $\hat\sigma_0^2 = \frac1n\sum(X_i-\mu)^2$. What is the distribution of $n\hat\sigma_0^2/\sigma^2$? | Chi-square with $n$ degrees of freedom, since $Z_i=(X_i-\mu)/\sigma$ are iid standard normal and $n\hat\sigma_0^2/\sigma^2 = \sum Z_i^2$. | p.469,471; procedure |

## Acid Concentration in Cheese
| Front | Back | Notes |
| --- | --- | --- |
| With $k$ chunks, $Y=\frac1k\sum\lvert X_i-\mu\rvert^2$ and $W=kY/\sigma^2$, how do you compute $\Pr(Y \le u^2)$? | Rewrite as $\Pr(W \le ku^2/\sigma^2)$ and read that value off the $\chi^2(k)$ table, e.g. $k=10,\sigma^2=0.09,u=0.3$ gives $\Pr(W\le 10)\approx 0.56$. | p.471-472; procedure |
# Node map
```json
[
 {
  "name": "Chi-Square Distribution",
  "type": "concept",
  "existing": false,
  "parent": "Common Distributions",
  "prereqs": [
   "Gamma Distribution"
  ],
  "uses": [],
  "page": "469-470",
  "summary": "The chi-square distribution with $m$ degrees of freedom is the gamma distribution with $\\alpha=m/2$, $\\beta=1/2$; its two-df case is the exponential distribution with mean 2."
 },
 {
  "name": "Chi-Square Distribution Mean Variance and MGF",
  "type": "concept",
  "existing": false,
  "parent": "Common Distributions",
  "prereqs": [
   "Chi-Square Distribution",
   "Moment Generating Function (MGF)"
  ],
  "uses": [],
  "page": "470",
  "summary": "For $X\\sim\\chi^2(m)$, $E(X)=m$, $\\mathrm{Var}(X)=2m$, and $\\psi(t)=(1-2t)^{-m/2}$ for $t<1/2$."
 },
 {
  "name": "Chi-Square Additivity",
  "type": "concept",
  "existing": false,
  "parent": "Common Distributions",
  "prereqs": [
   "Chi-Square Distribution",
   "Independence of Random Variables"
  ],
  "uses": [],
  "page": "470",
  "summary": "Independent chi-square variables add: if $X_i\\sim\\chi^2(m_i)$ independently, $\\sum X_i \\sim \\chi^2(\\sum m_i)$."
 },
 {
  "name": "Square of a Standard Normal Is Chi-Square",
  "type": "concept",
  "existing": false,
  "parent": "Common Distributions",
  "prereqs": [
   "Standard Normal Distribution",
   "Chi-Square Distribution"
  ],
  "uses": [],
  "page": "470-471",
  "summary": "If $X\\sim N(0,1)$, then $Y=X^2$ has the chi-square distribution with 1 degree of freedom."
 },
 {
  "name": "Sum of Squares of iid Standard Normal Is Chi-Square",
  "type": "concept",
  "existing": false,
  "parent": "Common Distributions",
  "prereqs": [
   "Square of a Standard Normal Is Chi-Square",
   "Chi-Square Additivity"
  ],
  "uses": [],
  "page": "471",
  "summary": "If $X_1,\\dots,X_m$ are iid standard normal, $\\sum X_i^2 \\sim \\chi^2(m)$; this is the main link between normal samples and the chi-square distribution."
 },
 {
  "name": "MLE of Variance of a Normal Distribution",
  "type": "problem",
  "existing": false,
  "parent": "Common Distributions",
  "prereqs": [
   "Chi-Square Distribution",
   "Sum of Squares of iid Standard Normal Is Chi-Square"
  ],
  "uses": [
   "Chi-Square Distribution",
   "Sum of Squares of iid Standard Normal Is Chi-Square"
  ],
  "page": "469,471",
  "summary": "The MLE of $\\sigma^2$ from a normal sample with known mean satisfies $n\\hat\\sigma_0^2/\\sigma^2\\sim\\chi^2(n)$."
 },
 {
  "name": "Acid Concentration in Cheese",
  "type": "problem",
  "existing": false,
  "parent": "Common Distributions",
  "prereqs": [
   "Chi-Square Distribution",
   "Sum of Squares of iid Standard Normal Is Chi-Square"
  ],
  "uses": [
   "Chi-Square Distribution",
   "Sum of Squares of iid Standard Normal Is Chi-Square"
  ],
  "page": "471-472",
  "summary": "Rescaling a mean-squared-deviation statistic by $k/\\sigma^2$ turns a probability question into a chi-square table lookup."
 }
]
```

# Frankenstein problems

**Problem 1.** Let $X_1,\dots,X_5$ be iid $N(0,4)$ and, independently, let $Y_1,Y_2,Y_3$ be iid $N(0,4)$. Define $U=\sum_{i=1}^5 (X_i/2)^2$ and $V=\sum_{j=1}^3 (Y_j/2)^2$.
(a) Find the distributions of $U$ and $V$.
(b) Find the distribution of $U+V$.
(c) Find $E(U+V)$ and $\mathrm{Var}(U+V)$.

*Solution.* Each $X_i$ has variance 4, so $X_i/2 \sim N(0,1)$; similarly $Y_j/2 \sim N(0,1)$.
(a) By Sum of Squares of iid Standard Normal Is Chi-Square, $U \sim \chi^2(5)$ and $V \sim \chi^2(3)$.
(b) $U$ and $V$ are built from independent groups of variables, so they are independent; by Chi-Square Additivity, $U+V \sim \chi^2(8)$.
(c) By Chi-Square Distribution Mean Variance and MGF with $m=8$: $E(U+V)=8$, $\mathrm{Var}(U+V)=2(8)=16$.

Concepts tested: Chi-Square Distribution, Sum of Squares of iid Standard Normal Is Chi-Square, Chi-Square Additivity, Chi-Square Distribution Mean Variance and MGF.

**Problem 2.** Let $Z_1,Z_2$ be iid $N(0,1)$ and let $W=Z_1^2+Z_2^2$.
(a) Identify the distribution of $W$.
(b) Show $W$ is also exponential and give its mean.
(c) Compute $E(W)$ and $\mathrm{Var}(W)$ two ways and confirm they agree.

*Solution.* (a) Each $Z_i^2 \sim \chi^2(1)$ (Square of a Standard Normal Is Chi-Square); since the $Z_i$ are independent, Chi-Square Additivity gives $W \sim \chi^2(2)$.
(b) By the Chi-Square Distribution note, $\chi^2(2)$ is the same distribution as exponential with parameter $1/2$, i.e. mean $1/(1/2)=2$.
(c) Chi-square route: $E(W)=m=2$, $\mathrm{Var}(W)=2m=4$. Exponential route ($\lambda=1/2$): $E(W)=1/\lambda=2$, $\mathrm{Var}(W)=1/\lambda^2=4$. Both routes agree: $E(W)=2$, $\mathrm{Var}(W)=4$.

Concepts tested: Square of a Standard Normal Is Chi-Square, Chi-Square Additivity, Chi-Square Distribution, Chi-Square Distribution Mean Variance and MGF.
