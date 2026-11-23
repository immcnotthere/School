---
type: reference
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "Normal Distribution"
tags:
  - decks
---
# STAT 132 Cards - Normal Distribution (the bell curve)

## Normal distribution
| Front | Back | Notes |
| --- | --- | --- |
| What story does a Normal random variable tell? | **Measurements that cluster around a center**, and averages or sums of many things (Central Limit Theorem). | Lecture_01 p.3; definition |
| What values can a Normal variable take? | **Any real number.** | Lecture_01 p.3; definition |
| What are the parameters of $N(\mu, \sigma^2)$ and their allowed values? | **$\mu$ any real number (center); $\sigma^2 > 0$ (spread).** | Lecture_01 p.3; definition |
| Write the Normal PDF. | $f(x) = \dfrac{1}{\sqrt{2\pi\sigma^2}}\, e^{-\frac{(x-\mu)^2}{2\sigma^2}}$. | Lecture_01 p.3; formula |
| In the Normal PDF, what does $(x - \mu)^2$ measure? | **The squared distance of x from the center.** | Distribution Sheets; motivation |
| In the Normal PDF, why divide $(x-\mu)^2$ by $2\sigma^2$? | **A bigger spread makes the same distance matter less**, so the curve is wider. | Distribution Sheets; motivation |
| In the Normal PDF, what does $e^{-(\cdot)}$ do? | **Shrinks the density the farther x is from the center.** | Distribution Sheets; motivation |
| In the Normal PDF, what job does $\frac{1}{\sqrt{2\pi\sigma^2}}$ do? | **It is the constant that makes the total area 1.** | Distribution Sheets; motivation |
| A problem says $N(50, 100)$. What is the SD? | **10.** *Side note, not tested: the second number is the variance, so take its square root.* | worked example |
| How do you standardize a Normal value x? | $z = \dfrac{x - \mu}{\sigma}$: how many SDs x sits from the mean. | Distribution Sheets; formula |
| If X is $N(\mu, \sigma^2)$, what distribution does $Z = (X - \mu)/\sigma$ have? | **$N(0, 1)$, the standard normal.** | Distribution Sheets; definition |
| What share of a Normal falls within 1, 2 and 3 SDs of the mean? | **About 68%, 95% and 99.7%.** | Distribution Sheets; formula |
| IQ is $N(100, 15^2)$. About what share scores above 130? | **About 2.5%**: 130 is 2 SDs up, and 5% lies beyond 2 SDs, split between two tails. | worked example |
| What is the Normal likelihood kernel in $\mu$ (with $\sigma^2$ known)? | $e^{-\frac{n(\mu - \bar x)^2}{2\sigma^2}}$: it depends on the data only through $\bar x$. | Kernels Table 2; formula; dep: [[Bayes Update Algorithm]] |
| Which prior is the partner of Normal data with known variance? | **A Normal prior on $\mu$**; the posterior is Normal again. | Kernels Table 3; assembly; dep: [[Bayes Update Algorithm]] |
| Why does the Normal show up for sample means even when the data are not Normal? | **The Central Limit Theorem:** for large n, $\bar X$ is approximately Normal. | assembly |
# Node map
```json
[
 {
  "name": "Normal distribution",
  "uses": [],
  "type": "concept",
  "existing": true,
  "parent": "Common Distributions",
  "prereqs": [],
  "page": 3,
  "summary": "Bell curve with center $\\mu$ and variance $\\sigma^2$; $\\frac{1}{\\sqrt{2\\pi\\sigma^2}}e^{-(x-\\mu)^2/(2\\sigma^2)}$."
 }
]
```

# Frankenstein problems

None yet.
