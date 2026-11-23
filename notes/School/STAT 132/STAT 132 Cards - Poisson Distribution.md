---
type: reference
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "Poisson Distribution"
tags:
  - decks
---
# STAT 132 Cards - Poisson Distribution (counts in a fixed window)

## Poisson Distribution
| Front | Back | Notes |
| --- | --- | --- |
| What story does a Poisson random variable tell? | **How many times something happens in a fixed window of time or space, at average rate $\lambda$.** *Side note, not tested: Calls per hour, typos per page.* | Lecture_01 p.3; definition |
| What values can a Poisson variable take? | **0, 1, 2, ... with no upper limit.** | Lecture_01 p.3; definition |
| What is the parameter of a Poisson and its allowed values? | **$\lambda > 0$, the average count per window.** | Lecture_01 p.3; definition |
| Write the Poisson PMF. | $\mathbb{P}(X = x) = \dfrac{e^{-\lambda}\lambda^x}{x!}$. *Read aloud: "e to the minus lambda, times lambda to the x, over x factorial."* | Lecture_01 p.3; formula |
| In the Poisson PMF, what does $e^{-\lambda}$ equal on its own? | **$\mathbb{P}(X = 0)$**, the chance of no events; it is also the constant that makes the chances add to 1. | Distribution Sheets; motivation |
| In the Poisson PMF, what does $\lambda^x / x!$ do as x grows? | **Rises, then falls:** counts near $\lambda$ are the likely ones. | Distribution Sheets; motivation |
| What is the Poisson's signature that you can check against data? | **Mean equals variance.** If the data's variance is far above its mean, a Poisson fits badly. | discrimination |
| Poisson with $\lambda = 2$: what is $\mathbb{P}(X = 0)$? | $e^{-2} \approx 0.135$. | worked example |
| Poisson with $\lambda = 2$: what is $\mathbb{P}(X = 1)$? | $2e^{-2} \approx 0.271$. | worked example |
| Poisson with $\lambda = 2$: what is $\mathbb{P}(X \ge 1)$? | $1 - e^{-2} \approx 0.865$ (one minus the chance of none). | worked example |
| What is the Poisson likelihood kernel in $\lambda$ for counts $x_1, \dots, x_n$? | $\lambda^{\sum x_i} e^{-n\lambda}$: total count in the power, number of windows in the exponent. | Kernels Table 2; formula; dep: [[Bayes Update Algorithm]] |
| With a Gamma$(\alpha, \beta)$ prior and Poisson counts $x_1, \dots, x_n$, what is the posterior? | **Gamma$(\alpha + \sum x_i, \beta + n)$.** | Kernels Table 3; assembly; dep: [[Bayes Update Algorithm]] |
| Help desk: prior Gamma(6, 2), calls 3, 5, 2, 4 in four hours. What is the posterior? | **Gamma(20, 6)**, mean $20/6 \approx 3.33$ calls per hour. | worked example; dep: [[Bayes Update Algorithm]] |
| How are the Poisson and the Exponential linked? | **Same stream of events: Poisson counts events in a window; Exponential measures the gap between events.** | Distribution Sheets; assembly |
| A Binomial with n = 1000 and p = 0.002 is close to which Poisson? | **Poisson(2)**, since $\lambda = np = 2$. | worked example |
# Node map
```json
[
 {
  "name": "Poisson Distribution",
  "uses": [],
  "type": "concept",
  "existing": true,
  "parent": "Common Distributions",
  "prereqs": [],
  "page": 3,
  "summary": "Count of events in a fixed window at average rate $\\lambda$: $e^{-\\lambda}\\lambda^x/x!$, mean and variance both $\\lambda$."
 }
]
```

# Frankenstein problems

None yet.
