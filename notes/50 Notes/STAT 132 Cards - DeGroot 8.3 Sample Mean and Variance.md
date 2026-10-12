---
type: reference
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "DeGroot 8.3 Sample Mean and Variance"
tags:
  - decks
---
# STAT 132 Cards - DeGroot 8.3 Sample Mean and Variance

## Independence of Sample Mean and Sample Variance
| Front | Back | Notes |
| --- | --- | --- |
| Yes or no, and why: for a random sample from a normal distribution, are the sample mean $\bar X_n$ and the sample variance independent? | Yes, they are independent random variables (Theorem 8.3.1). | p.474; formula |
| Yes or no, and why: does the independence of $\bar X_n$ and the sample variance hold for samples from any distribution? | No, it holds only when sampling from a normal distribution. | p.474; discrimination |

## Sample Variance Chi-Square Distribution
| Front | Back | Notes |
| --- | --- | --- |
| For a normal sample $X_1,\dots,X_n$, what is the distribution of $\sum_{i=1}^n (X_i-\bar X_n)^2/\sigma^2$? | Chi-square with $n-1$ degrees of freedom. | p.474; formula |
| Why does replacing $\mu$ with $\bar X_n$ drop the degrees of freedom from $n$ to $n-1$? | Estimating $\mu$ from the data itself uses up one degree of freedom. | p.474; discrimination |

## Orthogonal Matrix
| Front | Back | Notes |
| --- | --- | --- |
| What does it mean for an $n\times n$ matrix $A$ to be orthogonal? | $A^{-1} = A^T$, equivalently $AA^T = A^TA = I$. | p.476; definition |
| In row and column terms, when is a matrix orthogonal? | Each row (and column) has sum of squares 1, and the sum of products of entries between any two different rows (or columns) is 0. | p.476; formula |
| If $A$ is orthogonal, what is $\lvert\det A\rvert$? | $1$ | p.476; formula |

## Orthogonal Transformation Preserves Squared Length
| Front | Back | Notes |
| --- | --- | --- |
| If $\mathbf Y = A\mathbf X$ with $A$ orthogonal, how do $\sum Y_i^2$ and $\sum X_i^2$ compare? | They are equal: $\sum Y_i^2 = \sum X_i^2$. | p.476-477; formula |
| Geometrically, what does multiplying a vector by an orthogonal matrix do? | Rotates it, possibly flipping some signs, so its length is unchanged and the transformation's Jacobian has absolute value 1. | p.477; discrimination |

## Orthogonal Transformation of iid Standard Normals
| Front | Back | Notes |
| --- | --- | --- |
| If $X_1,\dots,X_n$ are iid standard normal and $\mathbf Y = A\mathbf X$ for orthogonal $A$, what is the joint distribution of $Y_1,\dots,Y_n$? | Also iid standard normal. | p.477; formula |
| In the proof of Theorem 8.3.1, why is the first row of $A$ chosen as $(1/\sqrt n,\dots,1/\sqrt n)$? | So $Y_1 = \sqrt n\,\bar X_n$, which separates the sample mean from $Y_2,\dots,Y_n$, independent of $Y_1$ and carrying $\sum(X_i-\bar X_n)^2$. | p.477-478; procedure |

## Chi-Square Quantile for Sample Variance
| Front | Back | Notes |
| --- | --- | --- |
| With $n=26$, $\hat\sigma^2=\sum(X_i-\bar X_n)^2/26$, and the $\chi^2(25)$ 0.25 quantile equal to 19.94, how do you find $\Pr(\hat\sigma^2 \le 0.77\sigma^2)$? | Set $U=26\hat\sigma^2/\sigma^2\sim\chi^2(25)$, so $\Pr(U\le 19.94)=0.25$; since $19.94/26\approx0.77$, this equals $\Pr(\hat\sigma^2\le0.77\sigma^2)=0.25$. | p.474-475; procedure |

## Sample Size for Mean and SD Precision
| Front | Back | Notes |
| --- | --- | --- |
| To find the smallest $n$ with $\Pr(\lvert\hat\mu-\mu\rvert<\sigma/5)\Pr(\lvert\hat\sigma-\sigma\rvert<\sigma/5)\ge 1/2$, what do $p_1$ and $p_2$ become? | $p_1=\Pr(\lvert U\rvert<\sqrt n/5)$ for standard normal $U$, and $p_2=\Pr(0.64n<V<1.44n)$ for $V=n\hat\sigma^2/\sigma^2\sim\chi^2(n-1)$; trial values give $n=21$ ($p_1=0.64$, $p_2=0.78$). | p.475-476; procedure |

# Node map
```json
[
 {
  "name": "Independence of Sample Mean and Sample Variance",
  "type": "concept",
  "existing": false,
  "parent": "Sample Mean and Sample Variance",
  "prereqs": [
   "Sample Mean",
   "Independence of Random Variables"
  ],
  "uses": [],
  "page": "474",
  "summary": "For a random sample from a normal distribution, the sample mean and sample variance are independent; this fails for non-normal populations."
 },
 {
  "name": "Sample Variance Chi-Square Distribution",
  "type": "concept",
  "existing": false,
  "parent": "Sample Mean and Sample Variance",
  "prereqs": [
   "Sample Mean",
   "Chi-Square Distribution",
   "Independence of Sample Mean and Sample Variance"
  ],
  "uses": [],
  "page": "474,479",
  "summary": "For a normal sample, $\\sum(X_i-\\bar X_n)^2/\\sigma^2$ (equivalently $n\\hat\\sigma^2/\\sigma^2$) has the chi-square distribution with $n-1$ degrees of freedom."
 },
 {
  "name": "Orthogonal Matrix",
  "type": "concept",
  "existing": false,
  "parent": "Linear Algebra",
  "prereqs": [
   "Matrix Multiplication",
   "Transpose",
   "Determinant"
  ],
  "uses": [],
  "page": "476",
  "summary": "A matrix $A$ is orthogonal if $A^{-1}=A^T$; equivalently its rows (and columns) are unit length and pairwise orthogonal, and $\\lvert\\det A\\rvert=1$."
 },
 {
  "name": "Orthogonal Transformation Preserves Squared Length",
  "type": "concept",
  "existing": false,
  "parent": "Linear Algebra",
  "prereqs": [
   "Orthogonal Matrix",
   "Dot Product"
  ],
  "uses": [],
  "page": "476-477",
  "summary": "If $\\mathbf Y=A\\mathbf X$ for orthogonal $A$, then $\\sum Y_i^2=\\sum X_i^2$, since $A$ acts as a rotation or reflection."
 },
 {
  "name": "Orthogonal Transformation of iid Standard Normals",
  "type": "concept",
  "existing": false,
  "parent": "Sample Mean and Sample Variance",
  "prereqs": [
   "Orthogonal Matrix",
   "Orthogonal Transformation Preserves Squared Length",
   "Standard Normal Distribution",
   "Independence of Random Variables"
  ],
  "uses": [],
  "page": "477-478",
  "summary": "If $X_1,\\dots,X_n$ are iid standard normal and $\\mathbf Y=A\\mathbf X$ for orthogonal $A$, then $Y_1,\\dots,Y_n$ are also iid standard normal; choosing the first row as $1/\\sqrt n$ isolates $\\bar X_n$."
 },
 {
  "name": "Chi-Square Quantile for Sample Variance",
  "type": "problem",
  "existing": false,
  "parent": "Sample Mean and Sample Variance",
  "prereqs": [
   "Sample Variance Chi-Square Distribution",
   "Chi-Square Distribution"
  ],
  "uses": [
   "Sample Variance Chi-Square Distribution"
  ],
  "page": "474-475",
  "summary": "Scaling the sample variance by $n/\\sigma^2$ turns a probability about $\\hat\\sigma^2$ into a chi-square quantile lookup."
 },
 {
  "name": "Sample Size for Mean and SD Precision",
  "type": "problem",
  "existing": false,
  "parent": "Sample Mean and Sample Variance",
  "prereqs": [
   "Sample Variance Chi-Square Distribution",
   "Independence of Sample Mean and Sample Variance",
   "Standard Normal Distribution"
  ],
  "uses": [
   "Sample Variance Chi-Square Distribution",
   "Independence of Sample Mean and Sample Variance"
  ],
  "page": "475-476",
  "summary": "Independence lets a joint precision probability for $\\hat\\mu$ and $\\hat\\sigma$ factor into a normal-table probability times a chi-square-table probability."
 }
]
```

# Frankenstein problems

**Problem 1.** A random sample of size $n=17$ is drawn from a normal distribution with unknown mean $\mu$ and variance $\sigma^2$. Let $\hat\sigma^2=\frac1{17}\sum_{i=1}^{17}(X_i-\bar X_{17})^2$ be the MLE of $\sigma^2$.
(a) What is the distribution of $17\hat\sigma^2/\sigma^2$?
(b) Find $E(\hat\sigma^2)$ and $\mathrm{Var}(\hat\sigma^2)$ in terms of $\sigma^2$.
(c) Are $\bar X_{17}$ and $\hat\sigma^2$ independent? Justify.

*Solution.* (a) By Sample Variance Chi-Square Distribution, $W=17\hat\sigma^2/\sigma^2 \sim \chi^2(16)$ (degrees of freedom $n-1=16$).
(b) By Chi-Square Distribution Mean Variance and MGF, $E(W)=16$ and $\mathrm{Var}(W)=2(16)=32$. Since $\hat\sigma^2=(\sigma^2/17)W$: $E(\hat\sigma^2)=(\sigma^2/17)(16)=16\sigma^2/17$, and $\mathrm{Var}(\hat\sigma^2)=(\sigma^2/17)^2(32)=32\sigma^4/289$ (since $17^2=289$).
(c) Yes, by Independence of Sample Mean and Sample Variance, which holds because the sample is drawn from a normal distribution.

Concepts tested: Sample Variance Chi-Square Distribution, Chi-Square Distribution Mean Variance and MGF, Independence of Sample Mean and Sample Variance.

**Problem 2.** Let $A=\begin{pmatrix}0.6 & 0.8\\ -0.8 & 0.6\end{pmatrix}$, and let $X_1,X_2$ be iid $N(0,1)$ with $(Y_1,Y_2)^T = A(X_1,X_2)^T$.
(a) Verify $A$ is orthogonal.
(b) What is the distribution of $Y_1^2+Y_2^2$?
(c) What does this say about $X_1^2+X_2^2$, and why?

*Solution.* (a) Row sums of squares: $0.6^2+0.8^2=0.36+0.64=1$ and $(-0.8)^2+0.6^2=0.64+0.36=1$. Row dot product: $0.6(-0.8)+0.8(0.6)=-0.48+0.48=0$. Both Orthogonal Matrix conditions hold.
(b) By Orthogonal Transformation of iid Standard Normals, $Y_1,Y_2$ are also iid $N(0,1)$, so by Sum of Squares of iid Standard Normal Is Chi-Square, $Y_1^2+Y_2^2 \sim \chi^2(2)$.
(c) By Orthogonal Transformation Preserves Squared Length, $X_1^2+X_2^2=Y_1^2+Y_2^2$, so $X_1^2+X_2^2 \sim \chi^2(2)$ as well, consistent with applying the same corollary directly to $X_1,X_2$.

Concepts tested: Orthogonal Matrix, Orthogonal Transformation of iid Standard Normals, Orthogonal Transformation Preserves Squared Length, Sum of Squares of iid Standard Normal Is Chi-Square.
