---
type: concept
parent: "[[Maximum Likelihood Estimation (MLE)]]"
domain: stats
course: "STAT 132"
status: draft
source: "DeGroot and Schervish 4e, Sec. 7.6, Example 7.6.12"
prereqs:
  - "[[Poisson Distribution]]"
  - "[[Sample Mean]]"
  - "[[Central Limit Theorem]]"
  - "[[Standardization (math)]]"
approximates:
  - "[[Poisson Distribution]]"
mastery: 0
retention_band: cold
---
# Normal Approximation to the Poisson Sample Mean

If $X_1,\dots,X_n$ are i.i.d. Poisson($\theta$), the sample mean $\bar X_n$ (which is also the M.L.E. of $\theta$) is approximately $N(\theta, \theta/n)$ for large $n$, by the central limit theorem. To get probabilities, standardize: $Z=(\bar X_n-\theta)/\sqrt{\theta/n}\approx N(0,1)$.

Why it needs Z-scores: the CLT only says the *standardized* mean is approximately standard normal, so every probability statement about $\bar X_n$ goes through a Z-score.

Cards: [[STAT 132 Cards - DeGroot 7.6#Normal Approximation to the Poisson Sample Mean]]
