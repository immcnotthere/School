---
type: reference
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "DeGroot 8.4 t Distributions"
tags:
  - decks
---
# STAT 132 Cards - DeGroot 8.4 t Distributions

## t Distribution
| Front | Back | Notes |
| --- | --- | --- |
| Define the t distribution with $m$ degrees of freedom in terms of $Y$ and $Z$. | $X = \dfrac{Z}{(Y/m)^{1/2}}$, where $Z$ has the standard normal distribution and $Y$ has the $\chi^2$ distribution with $m$ df, $Y$ and $Z$ independent. | p.482; definition |
| What distribution is the t distribution with 1 degree of freedom? | The Cauchy distribution. | p.483; discrimination |
| What does the t distribution with $m$ degrees of freedom converge to as $m \to \infty$? | The standard normal distribution (its pdf converges pointwise to $\phi(x)$). | p.483; discrimination |
| How does the shape of the t distribution's pdf compare to the standard normal's? | Both are symmetric, bell shaped, centered at 0, but the t distribution's tails approach 0 more slowly (heavier tails). | p.483; concept |

## t Distribution PDF
| Front | Back | Notes |
| --- | --- | --- |
| Give the pdf of the t distribution with $m$ degrees of freedom. | $g(x) = \dfrac{\Gamma\left(\frac{m+1}{2}\right)}{(m\pi)^{1/2}\Gamma\left(\frac{m}{2}\right)}\left(1+\dfrac{x^2}{m}\right)^{-(m+1)/2}$, for $-\infty < x < \infty$. | p.482; formula |
| Over what domain is the t distribution pdf defined? | All real $x$, $-\infty < x < \infty$. | p.482; definition |

## Moments of the t Distribution
| Front | Back | Notes |
| --- | --- | --- |
| For what values of $m$ does the mean of the t distribution exist, and what is its value? | Exists for $m > 1$; the value is always 0 by symmetry. | p.482; formula |
| Give the variance of the t distribution with $m$ degrees of freedom (when it exists). | $\mathrm{Var}(X) = \dfrac{m}{m-2}$, for $m > 2$. | p.483; formula |
| For which $k$ is $E(\vert X\vert ^k)$ finite for a t distribution with $m$ degrees of freedom? | $E(\vert X\vert ^k) < \infty$ for $k < m$, and $E(\vert X\vert ^k) = \infty$ for $k \ge m$; consequently the m.g.f. of $X$ does not exist. | p.483; concept |

## t Distribution of the Sample Mean
| Front | Back | Notes |
| --- | --- | --- |
| $X_1,\dots,X_n$ iid $N(\mu,\sigma^2)$. State the distribution of $n^{1/2}(\bar{X}_n-\mu)/\check\sigma$. | It has the t distribution with $n-1$ degrees of freedom, where $\check\sigma = \left[\frac{1}{n-1}\sum_{i=1}^n (X_i-\bar{X}_n)^2\right]^{1/2}$. | p.483; formula (Theorem 8.4.2) |
| How is $\check\sigma$ (used to studentize $\bar X_n$) defined? | $\check\sigma = \left[\dfrac{1}{n-1}\sum_{i=1}^n (X_i-\bar X_n)^2\right]^{1/2}$. | p.483; definition |
| How does $\check\sigma$ relate to the M.L.E. $\hat\sigma$? | $\check\sigma = \left(\dfrac{n}{n-1}\right)^{1/2}\hat\sigma$; they are close for large $n$. | p.484; discrimination |
| Why replace $\sigma$ with $\check\sigma$ (rather than $\hat\sigma$) in $Z=n^{1/2}(\bar X_n-\mu)/\sigma$? | Doing so gives a statistic $U$ whose value and distribution do not depend on the unknown $\sigma$ at all; that is what Theorem 8.4.2 guarantees. | p.484; concept |

## Rain from Seeded Clouds, t Quantile
| Front | Back | Notes |
| --- | --- | --- |
| $n=26$ so $U=n^{1/2}(\bar X_n-\mu)/\check\sigma \sim t_{25}$, and the $0.9$ quantile of $t_{25}$ is $1.316$. Find $c$ such that $\Pr(\bar X_n \le \mu + c\check\sigma) = 0.9$. | $c = 1.316/\sqrt{26} \approx 0.2581$. | p.484; procedure (key move) |

## Derivation of the t Distribution PDF
| Front | Back | Notes |
| --- | --- | --- |
| To derive the t pdf, set $W=Y$ and transform $(Y,Z)\to(X,W)$ via $Z=X(W/m)^{1/2}$, $Y=W$. What is the Jacobian of this transformation? | $(w/m)^{1/2}$. | p.485; procedure (key move) |
# Node map
```json
[
 {
  "name": "t Distribution",
  "type": "concept",
  "existing": false,
  "parent": "Common Distributions",
  "prereqs": [
   "Standard Normal Distribution",
   "Random variable"
  ],
  "uses": [],
  "page": 482,
  "summary": "X has the t distribution with m degrees of freedom if $X = Z/(Y/m)^{1/2}$ where Z is standard normal and Y is chi-square with m df, independent of Z."
 },
 {
  "name": "t Distribution PDF",
  "type": "concept",
  "existing": false,
  "parent": "Common Distributions",
  "prereqs": [
   "t Distribution",
   "Probability density function",
   "Degree of Freedom"
  ],
  "uses": [],
  "page": 482,
  "summary": "The pdf of the t distribution with m df is $g(x)=\\Gamma(\\frac{m+1}{2})/[(m\\pi)^{1/2}\\Gamma(\\frac{m}{2})]\\,(1+x^2/m)^{-(m+1)/2}$."
 },
 {
  "name": "Moments of the t Distribution",
  "type": "concept",
  "existing": false,
  "parent": "Common Distributions",
  "prereqs": [
   "Mean",
   "Variance (Math)",
   "t Distribution"
  ],
  "uses": [],
  "page": 482,
  "summary": "The t distribution's mean is 0 when it exists (m>1); its variance is m/(m-2) for m>2; E|X|^k is finite only for k<m, so the mgf does not exist."
 },
 {
  "name": "t Distribution of the Sample Mean",
  "type": "concept",
  "existing": false,
  "parent": "Statistical Inference",
  "prereqs": [
   "t Distribution",
   "Sample Mean and Sample Variance",
   "Sample Mean"
  ],
  "uses": [],
  "page": 483,
  "summary": "For an iid normal sample, $n^{1/2}(\\bar X_n-\\mu)/\\check\\sigma$ has the t distribution with n-1 df, where $\\check\\sigma$ uses an n-1 denominator; this removes dependence on the unknown sigma."
 },
 {
  "name": "Rain from Seeded Clouds, t Quantile",
  "type": "problem",
  "existing": false,
  "parent": "Statistical Inference",
  "prereqs": [
   "t Distribution of the Sample Mean"
  ],
  "uses": [
   "t Distribution of the Sample Mean",
   "t Distribution"
  ],
  "page": 484,
  "summary": "Uses n=26 and the 0.9 quantile of t_25 (1.316) to bound how far the sample mean can be above mu in terms of check-sigma."
 },
 {
  "name": "Derivation of the t Distribution PDF",
  "type": "problem",
  "existing": false,
  "parent": "Common Distributions",
  "prereqs": [
   "Transformation of random variables",
   "Jacobian",
   "Change of variables formula",
   "Joint probability distribution"
  ],
  "uses": [
   "Transformation of random variables",
   "Jacobian",
   "Change of variables formula",
   "Joint probability distribution",
   "t Distribution"
  ],
  "page": 485,
  "summary": "Derives the t pdf by transforming the independent (Y,Z) pair to (X,W=Y) with Jacobian (w/m)^{1/2}, forming the joint pdf, then integrating out w."
 }
]
```

# Frankenstein problems

**FP1.** A sample of $n=17$ iid observations from a normal distribution has $\bar X_n = 12.4$ and $\check\sigma = 3.2$ (using the $n-1$ denominator). The $0.95$ quantile of the t distribution with 16 degrees of freedom is $1.746$.

(a) What is the distribution of $U = n^{1/2}(\bar X_n-\mu)/\check\sigma$?
(b) What is $\mathrm{Var}(U)$?
(c) Find a two-sided interval that contains $\mu$ with probability 0.90.

*Concepts used: t Distribution, t Distribution of the Sample Mean, Moments of the t Distribution.*

**Solution.**
(a) $n-1 = 16$, so $U$ has the t distribution with 16 degrees of freedom.
(b) $\mathrm{Var}(U) = m/(m-2) = 16/14 = 8/7 \approx 1.1429$.
(c) By symmetry, $\Pr(-1.746 \le U \le 1.746) = 0.90$. Solving $-1.746 \le \sqrt{17}(12.4-\mu)/3.2 \le 1.746$ for $\mu$:
margin $= 1.746 \times 3.2/\sqrt{17} = 1.746 \times 0.7761 \approx 1.355$.
So the interval is $(12.4 - 1.355,\ 12.4 + 1.355) = (11.045,\ 13.755)$.

**FP2.** Consider a t distribution with $m=1$ df and one with $m=50$ df.

(a) Which of the two has a defined mean and variance, and what are the values (where defined)?
(b) The standard normal's 0.95 quantile is 1.645. Explain why this is a reasonable approximation to the 0.95 quantile of $t_{50}$, but not of $t_1$.
(c) Why does the mean fail to exist for $m=1$ specifically (in terms of $E(|X|^k)$)?

*Concepts used: t Distribution, t Distribution PDF, Moments of the t Distribution, Standard Normal Distribution.*

**Solution.**
(a) $m=1$ is the Cauchy distribution: mean and variance do not exist. $m=50 > 2$: mean $=0$, variance $= 50/48 = 25/24 \approx 1.0417$.
(b) As $m\to\infty$ the t pdf converges pointwise to the standard normal pdf, and $m=50$ is large, so $t_{50}$ is close to standard normal and 1.645 is a good approximation to its 0.95 quantile. $t_1$ (Cauchy) has much heavier tails and is far from normal, so 1.645 would badly underestimate its 0.95 quantile.
(c) For $m=1$, $E(|X|^k) < \infty$ only for $k < 1$; since the mean requires $k=1 \ge m$, $E(|X|)=\infty$, so the mean does not exist.
