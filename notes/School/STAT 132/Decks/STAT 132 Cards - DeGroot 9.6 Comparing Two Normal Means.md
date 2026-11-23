---
type: reference
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "DeGroot 9.6 Comparing Two Normal Means"
tags:
  - decks
---
# STAT 132 Cards - DeGroot 9.6 Comparing Two Normal Means

## Two-Sample t Statistic
| Front | Back | Notes |
| --- | --- | --- |
| Define the two-sample t statistic $U$ for comparing two normal means with a common unknown variance. | $U=\dfrac{(m+n-2)^{1/2}(\bar X_m-\bar Y_n)}{\left(\frac1m+\frac1n\right)^{1/2}(S_X^2+S_Y^2)^{1/2}}$. | p.602; formula |
| What is the distribution of $U$ when $\mu_1=\mu_2$? | The $t$ distribution with $m+n-2$ degrees of freedom. | p.602; formula |

## Two-Sample t Test
| Front | Back | Notes |
| --- | --- | --- |
| For $H_0:\mu_1\le\mu_2$ vs $H_1:\mu_1>\mu_2$ at level $\alpha_0$, give the rejection rule. | Reject $H_0$ if $U\ge T_{m+n-2}^{-1}(1-\alpha_0)$. | p.604; procedure |
| For $H_0:\mu_1\ge\mu_2$ vs $H_1:\mu_1<\mu_2$ at level $\alpha_0$, give the rejection rule. | Reject $H_0$ if $U\le -T_{m+n-2}^{-1}(1-\alpha_0)$. | p.604; procedure |
| For $H_0:\mu_1=\mu_2$ vs $H_1:\mu_1\neq\mu_2$ at level $\alpha_0$, give the rejection rule. | Reject $H_0$ if $\vert U\vert \ge T_{m+n-2}^{-1}(1-\alpha_0/2)$. | p.606; procedure |

## p-values for Two-Sample t Tests
| Front | Back | Notes |
| --- | --- | --- |
| For $H_0:\mu_1\le\mu_2$, give the p-value formula for observed $u$. | $1-T_{m+n-2}(u)$. | p.604; formula |
| For the two-sided hypotheses $H_0:\mu_1=\mu_2$, give the p-value formula for observed $u$. | $2[1-T_{m+n-2}(\vert u\vert )]$. | p.606; formula |

## Power of Two-Sample t Test
| Front | Back | Notes |
| --- | --- | --- |
| What is the noncentrality parameter $\psi$ for the two-sample t statistic? | $\psi=\dfrac{\mu_1-\mu_2}{\sigma\left(\frac1m+\frac1n\right)^{1/2}}$. | p.605; formula |
| What distribution does $U$ follow when $\mu_1\neq\mu_2$? | The noncentral $t$ distribution with $m+n-2$ degrees of freedom and noncentrality $\psi$. | p.605; formula |

## Two-Sample t Test as a Likelihood Ratio Test
| Front | Back | Notes |
| --- | --- | --- |
| For $H_0:\mu_1\le\mu_2$, what does $\Lambda(x,y)$ equal when $\bar x_m\le\bar y_n$? | $\Lambda(x,y)=1$, since the unrestricted MLEs already satisfy $H_0$. | p.607; formula |
| What does $\Lambda(x,y)$ equal when $\bar x_m>\bar y_n$, in terms of $v=(\bar x_m-\bar y_n)\big/\left[\left(\frac1m+\frac1n\right)^{1/2}(s_x^2+s_y^2)^{1/2}\right]$? | $\Lambda(x,y)=(1+v^2)^{-(m+n)/2}$. | p.607; formula |
| Why is the two-sample t test a likelihood ratio test? | Because $\Lambda(x,y)\le k$ is equivalent to $v\ge k'$, and $(m+n-2)^{1/2}v$ is exactly the observed $U$, so $\Lambda\le k \iff U\ge c$. | p.607; discrimination |

## Known Ratio of Variances t Test
| Front | Back | Notes |
| --- | --- | --- |
| If $\sigma_2^2=k\sigma_1^2$ for known $k$, give the modified statistic $U$ that has the $t_{m+n-2}$ distribution when $\mu_1=\mu_2$. | $U=\dfrac{(m+n-2)^{1/2}(\bar X_m-\bar Y_n)}{\left(\frac1m+\frac{k}{n}\right)^{1/2}\left(S_X^2+\frac{S_Y^2}{k}\right)^{1/2}}$. | p.608; formula |

## Behrens-Fisher Problem
| Front | Back | Notes |
| --- | --- | --- |
| What is the Behrens-Fisher problem? | Testing equality of two normal means when both variances are unknown and their ratio is also unknown; even the likelihood ratio statistic has no known distribution. | p.608; definition |

## Welch's t Approximation
| Front | Back | Notes |
| --- | --- | --- |
| Define Welch's statistic $V$ for comparing two means without assuming equal variances. | $V=\dfrac{\bar X_m-\bar Y_n}{\left(\frac{S_X^2}{m(m-1)}+\frac{S_Y^2}{n(n-1)}\right)^{1/2}}$. | p.608; formula |
| What does Welch's procedure do with the distribution of $V$? | Approximates it by a $t$ distribution with estimated (Welch-Satterthwaite) degrees of freedom $\nu$. | p.609; procedure |
| Give the Welch-Satterthwaite degrees of freedom formula $\nu$. | $\nu=\dfrac{\left(\frac{s_x^2}{m(m-1)}+\frac{s_y^2}{n(n-1)}\right)^2}{\frac{1}{(m-1)^3}\left(\frac{s_x^2}{m}\right)^2+\frac{1}{(n-1)^3}\left(\frac{s_y^2}{n}\right)^2}$. | p.609; formula |

## Rain from Seeded Clouds Two-Sample t Test
| Front | Back | Notes |
| --- | --- | --- |
| Seeded vs unseeded clouds: $m=n=26$, $\bar x=5.13$, $\bar y=3.99$, $S_X^2=63.96$, $S_Y^2=67.39$; testing $H_0:\mu_1\le\mu_2$ at $\alpha_0=0.01$ ($T_{50}^{-1}(0.99)=2.403$). Compute $U$ and state the decision. | $U=\dfrac{50^{1/2}(5.13-3.99)}{\left(\frac{1}{26}+\frac{1}{26}\right)^{1/2}(63.96+67.39)^{1/2}}=2.544$; since $2.544>2.403$, reject $H_0$. | p.605; procedure |

## Roman Pottery One-Sided t Test
| Front | Back | Notes |
| --- | --- | --- |
| Llanederyn ($m=14$) vs Ashley Rails ($n=5$) aluminum oxide percentages give observed $U=-6.302$, testing $H_0:\mu_1\ge\mu_2$ with 17 df ($T_{17}^{-1}(0.995)=2.898$). State the decision and the smallest level at which $H_0$ is rejected. | Since $U=-6.302<-2.898$, reject $H_0$ at any level $\alpha_0\ge0.005$. | p.605; procedure |

## Comparing Copper Ores Two-Sided t Test
| Front | Back | Notes |
| --- | --- | --- |
| Copper ore comparison: $m=8$, $n=10$, observed $U=3.442$, 16 df ($T_{16}^{-1}(0.995)=2.921$). Testing $H_0:\mu_1=\mu_2$, what is the decision and the smallest level at which $H_0$ is rejected? | Since $\vert 3.442\vert >2.921$, reject $H_0$ at any level $\alpha_0\ge0.01$. | p.606; procedure |

## Comparing Copper Ores Welch Approximation
| Front | Back | Notes |
| --- | --- | --- |
| Using the copper ore data with unequal variances, Welch's method gives $V=3.321$ and $\nu=12.49$. What is the two-sided p-value? | $2[1-T_{12.49}(3.321)]=0.0058$. | p.609; procedure |
# Node map
```json
[
 {
  "name": "Two-Sample t Statistic",
  "type": "concept",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [
   "t-statistic",
   "Sample Mean and Sample Variance"
  ],
  "uses": [],
  "page": 602,
  "summary": "$U=(m+n-2)^{1/2}(\\bar X_m-\\bar Y_n)/[(1/m+1/n)^{1/2}(S_X^2+S_Y^2)^{1/2}]$ has the $t_{m+n-2}$ distribution when $\\mu_1=\\mu_2$ and variances are equal."
 },
 {
  "name": "Two-Sample t Test",
  "type": "concept",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [
   "Two-Sample t Statistic"
  ],
  "uses": [],
  "page": 604,
  "summary": "One- and two-sided level $\\alpha_0$ tests comparing two normal means with common variance, based on the two-sample t statistic."
 },
 {
  "name": "p-values for Two-Sample t Tests",
  "type": "concept",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [
   "Two-Sample t Test",
   "p-value"
  ],
  "uses": [],
  "page": 604,
  "summary": "One-sided p-value is $1-T_{m+n-2}(u)$; two-sided p-value is $2[1-T_{m+n-2}(|u|)]$."
 },
 {
  "name": "Power of Two-Sample t Test",
  "type": "concept",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [
   "Two-Sample t Statistic"
  ],
  "uses": [],
  "page": 605,
  "summary": "Under $\\mu_1\\neq\\mu_2$, U has the noncentral t distribution with $m+n-2$ df and noncentrality $\\psi=(\\mu_1-\\mu_2)/[\\sigma(1/m+1/n)^{1/2}]$."
 },
 {
  "name": "Two-Sample t Test as a Likelihood Ratio Test",
  "type": "concept",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [
   "Two-Sample t Test",
   "Likelihood Function"
  ],
  "uses": [],
  "page": 607,
  "summary": "The two-sample t test is exactly the likelihood ratio test for comparing two normal means with common variance."
 },
 {
  "name": "Known Ratio of Variances t Test",
  "type": "concept",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [
   "Two-Sample t Statistic"
  ],
  "uses": [],
  "page": 608,
  "summary": "When $\\sigma_2^2=k\\sigma_1^2$ for known $k$, a rescaled statistic still has the $t_{m+n-2}$ distribution under $\\mu_1=\\mu_2$."
 },
 {
  "name": "Behrens-Fisher Problem",
  "type": "concept",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [
   "Known Ratio of Variances t Test"
  ],
  "uses": [],
  "page": 608,
  "summary": "Comparing two normal means when both variances and their ratio are unknown; no exact test exists."
 },
 {
  "name": "Welch's t Approximation",
  "type": "concept",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [
   "Behrens-Fisher Problem"
  ],
  "uses": [],
  "page": 608,
  "summary": "Approximates the distribution of $V=(\\bar X_m-\\bar Y_n)/[S_X^2/(m(m-1))+S_Y^2/(n(n-1))]^{1/2}$ by a t distribution with Welch-Satterthwaite degrees of freedom."
 },
 {
  "name": "Rain from Seeded Clouds Two-Sample t Test",
  "type": "problem",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [],
  "uses": [
   "Two-Sample t Statistic",
   "Two-Sample t Test"
  ],
  "page": 605,
  "summary": "Testing whether seeded clouds have higher mean log-rainfall than unseeded clouds."
 },
 {
  "name": "Roman Pottery One-Sided t Test",
  "type": "problem",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [],
  "uses": [
   "Two-Sample t Test",
   "p-values for Two-Sample t Tests"
  ],
  "page": 605,
  "summary": "One-sided comparison of aluminum oxide percentages between two pottery sites with unequal sample sizes."
 },
 {
  "name": "Comparing Copper Ores Two-Sided t Test",
  "type": "problem",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [],
  "uses": [
   "Two-Sample t Test",
   "p-values for Two-Sample t Tests"
  ],
  "page": 606,
  "summary": "Two-sided two-sample t test comparing mean copper content at two mine locations, assuming equal variances."
 },
 {
  "name": "Comparing Copper Ores Welch Approximation",
  "type": "problem",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [],
  "uses": [
   "Welch's t Approximation"
  ],
  "page": 609,
  "summary": "Redoing the copper ore comparison without assuming equal variances, using Welch's V and estimated degrees of freedom."
 }
]
```

# Frankenstein problems

**Problem 1**
Two fertilizers are compared: $m=12$ plots with fertilizer A give $\bar x=48.5$, $S_X^2=180$; $n=15$ plots with fertilizer B give $\bar y=45.2$, $S_Y^2=210$. Assume equal variances and test $H_0:\mu_1\le\mu_2$ vs $H_1:\mu_1>\mu_2$ at $\alpha_0=0.05$, where $T_{25}^{-1}(0.95)=1.708$.

a. Compute $U$.
b. State the decision.
c. Give the p-value formula (do not evaluate it numerically).
d. Which type of error is possible given this decision?

**Solution**

a. $m+n-2=25$, $\sqrt{25}=5$. $\bar x-\bar y=3.3$, so numerator $=5(3.3)=16.5$.
$\frac1{12}+\frac1{15}=\frac{5+4}{60}=0.15$, $\sqrt{0.15}=0.3873$.
$S_X^2+S_Y^2=390$, $\sqrt{390}=19.748$.
Denominator $=0.3873\times19.748=7.649$.
$U=16.5/7.649\approx2.157$.

b. Since $2.157>1.708$, reject $H_0$.

c. p-value $=1-T_{25}(2.157)$.

d. Since $H_0$ was rejected, the possible error is a Type I error.

Concepts used: Two-Sample t Statistic, Two-Sample t Test, p-values for Two-Sample t Tests, Type I and Type II Error.

**Problem 2**
Two labs measure a chemical concentration. Lab 1: $m=9$, $\bar x=10.2$, $S_X^2=14.4$. Lab 2: $n=9$, $\bar y=9.0$, $S_Y^2=28.8$, and it is known that $\sigma_2^2=2\sigma_1^2$ (so $k=2$). Test $H_0:\mu_1=\mu_2$ vs $H_1:\mu_1\neq\mu_2$ at $\alpha_0=0.05$, where $T_{16}^{-1}(0.975)=2.120$.

a. Compute the modified statistic $U$ for the known variance ratio.
b. State the decision.
c. If $k$ were instead unknown, which named problem applies, and what statistic would be used?
d. What is the noncentrality parameter $\psi$ for this test if the true difference is $\mu_1-\mu_2=2$ and $\sigma_1=3$?

**Solution**

a. $m+n-2=16$, $\sqrt{16}=4$. $\bar x-\bar y=1.2$, numerator $=4(1.2)=4.8$.
$\frac1m+\frac{k}{n}=\frac19+\frac29=\frac39=0.3333$, $\sqrt{0.3333}=0.5774$.
$S_X^2+\frac{S_Y^2}{k}=14.4+\frac{28.8}{2}=14.4+14.4=28.8$, $\sqrt{28.8}=5.3666$.
Denominator $=0.5774\times5.3666=3.099$.
$U=4.8/3.099\approx1.549$.

b. Since $|1.549|<2.120$, do not reject $H_0$.

c. This is the Behrens-Fisher problem; use Welch's statistic $V$ with the Welch-Satterthwaite degrees of freedom instead.

d. $\psi=\dfrac{\mu_1-\mu_2}{\sigma_1\left(\frac1m+\frac{k}{n}\right)^{1/2}}=\dfrac{2}{3(0.5774)}=\dfrac{2}{1.732}\approx1.155$.

Concepts used: Known Ratio of Variances t Test, Two-Sample t Test, Behrens-Fisher Problem, Power of Two-Sample t Test.
