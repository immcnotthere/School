---
type: concept
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "Lec 1 §5; Reading 1 §1.10.2"
week: 1
prereqs:
  - "[[Sample vs Population]]"
retention_band: cold
---
# Statistic

Any function of the data that **doesn't involve unknown parameters**: $T=t(X_1,\dots,X_n)$.
- $\bar X=\frac1n\sum X_i$
- $S^2=\frac{1}{n-1}\sum (X_i-\bar X)^2$ (note the $n-1$)

Before the data are collected, a statistic is a random variable with a *sampling distribution*. After collection, it is a number.
Test: $\bar X-\mu$ is **not** a statistic if $\mu$ is unknown.
