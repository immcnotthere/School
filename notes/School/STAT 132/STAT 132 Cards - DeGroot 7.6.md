---
type: reference
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "DeGroot 7.6"
tags:
  - decks
---
# STAT 132 Cards - DeGroot 7.6

## Normal Approximation to the Poisson Sample Mean
| Front | Back | Notes |
| --- | --- | --- |
| $X_1,\dots,X_n$ i.i.d. Poisson($\theta$), $n$ large. Approximate distribution of $\bar X_n$? | $N(\theta,\ \theta/n)$, by the central limit theorem | DeGroot 7.6.12; formula |
| Z-score for the Poisson sample mean? | $Z=\dfrac{\bar X_n-\theta}{\sqrt{\theta/n}}\approx N(0,1)$ | DeGroot 7.6.12; formula |
| Why do you need standardization to use the CLT on a Poisson sample mean? | The CLT is a statement about the standardized mean, so probabilities for $\bar X_n$ are read off $\Phi$ after converting to a Z-score | DeGroot 7.6.12; discrimination |

# Node map
```json
[{"name": "Normal Approximation to the Poisson Sample Mean", "type": "concept", "existing": false, "parent": "Maximum Likelihood Estimation (MLE)", "prereqs": ["Poisson Distribution", "Sample Mean", "Central Limit Theorem", "Standardization (math)"], "uses": [], "page": "7.6", "summary": "Sample mean of i.i.d. Poisson(theta) is approximately N(theta, theta/n)."}]
```
