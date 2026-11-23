---
type: concept
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
prereqs:
  - "[[Cumulative Distribution Function (CDF)]]"
  - "[[Independence of Random Variables]]"
  - "[[Probability density function]]"
source: "stat132-disc07-w25 p.1"
---
# Distribution of the Sample Maximum

For an iid sample $X_1,\dots,X_n$ with CDF $F$ and pdf $f$, the maximum $Y=\max(X_1,\dots,X_n)$ has

$$F_Y(y)=P(Y\le y)=P(X_1\le y,\dots,X_n\le y)=\prod_{i=1}^n P(X_i\le y)=F(y)^n,$$

$$f_Y(y)=\frac{d}{dy}F(y)^n=n\,F(y)^{n-1}f(y).$$

Why each step holds:
- **Given:** "the largest one is at most y" is the same event as "every one is at most y".
- **What changes:** the joint probability splits into a product because the $X_i$ are independent (this is the
  prerequisite [[Independence of Random Variables]]), and each factor is the same CDF because they are identically
  distributed ([[Cumulative Distribution Function (CDF)]]).
- **Next:** differentiate the CDF to get the pdf (chain rule on $F(y)^n$), the step that uses
  [[Probability density function]].

Example (STAT 132 Discussion 7, Problem 4): for Uniform$[0,\theta]$, $F(y)=y/\theta$ on $[0,\theta]$, so
$f_Y(y)=n y^{n-1}/\theta^n$ and $E[Y]=\int_0^\theta y\cdot n y^{n-1}/\theta^n\,dy=\frac{n}{n+1}\theta$.
Hence $\frac{n+1}{n}Y$ is an unbiased estimator of $\theta$ ([[Unbiased Estimator]]). $Y$ is also the MLE of
$\theta$ ([[MLE for Uniform Distribution]]), which is biased low; the factor $\frac{n+1}{n}$ removes the bias.
