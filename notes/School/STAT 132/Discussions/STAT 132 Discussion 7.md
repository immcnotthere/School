---
type: problem
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "School/STAT 132/Discussions/stat132-disc07-w25.pdf"
uses:
  - "[[Unbiased Estimator]]"
  - "[[Linearity of Expectation]]"
  - "[[Moments and Central Moments]]"
  - "[[Sample Mean]]"
  - "[[Properties of Variance]]"
  - "[[Variance of the Sample Mean]]"
  - "[[Unbiased Estimator of the Variance]]"
  - "[[Expectation of Independent Random Variables]]"
  - "[[Variance of a Sum of Independent Random Variables]]"
  - "[[Derivative]]"
  - "[[Uniform Distribution (Continuous)]]"
  - "[[Cumulative Distribution Function (CDF)]]"
  - "[[Independence of Random Variables]]"
  - "[[Expectation of a Continuous Random Variable]]"
---
# STAT 132 Discussion 7

Discussion worksheet (Winter 2025 set), all four problems on unbiased estimators. The question table below is what
the assignment viewer and `System/index/Assignment maps.md` read.

| Q | What it asks | Concepts |
|---|---|---|
| 1 | the k-th sample moment (1/n) sum X_i^k is unbiased for E(X^k) | [[Unbiased Estimator]], [[Linearity of Expectation]], [[Moments and Central Moments]], [[Sample Mean]] |
| 2 | an unbiased estimator of [E(X)]^2 (hint: E(Xbar^2) = Var(Xbar) + [E(X)]^2) | [[Unbiased Estimator]], [[Properties of Variance]], [[Variance of the Sample Mean]], [[Unbiased Estimator of the Variance]], [[Expectation of Independent Random Variables]] |
| 3 | theta-hat = a Xbar_m + (1 - a) Ybar_n: (a) when unbiased, (b) the a with minimum variance when Var(A) = 4 Var(B) | [[Unbiased Estimator]], [[Linearity of Expectation]], [[Variance of a Sum of Independent Random Variables]], [[Properties of Variance]], [[Variance of the Sample Mean]], [[Derivative]] |
| 4 | Y = max(X_1..X_n) from Uniform[0, theta]: show (n+1)/n Y is unbiased | [[Unbiased Estimator]], [[Uniform Distribution (Continuous)]], [[Cumulative Distribution Function (CDF)]], [[Independence of Random Variables]], [[Expectation of a Continuous Random Variable]], [[Distribution of the Sample Maximum]] |

[[Distribution of the Sample Maximum]] has no note yet: P(Y <= y) = P(all X_i <= y) = F(y)^n by independence,
so the pdf is n F(y)^(n-1) f(y). For Uniform[0, theta] that is n y^(n-1) / theta^n on [0, theta].
