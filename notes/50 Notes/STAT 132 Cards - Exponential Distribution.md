---
type: reference
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "Exponential Distribution"
tags:
  - decks
---
# STAT 132 Cards - Exponential Distribution (waiting time)

## Exponential distribution
| Front | Back | Notes |
| --- | --- | --- |
| What story does an Exponential random variable tell? | **How long until the next event, when events arrive steadily and independently at rate $\beta$.** *Side note, not tested: Bus waits, lamp lifetimes.* | Lecture_01 p.3; definition |
| What values can an Exponential variable take? | **Any number above 0.** | Lecture_01 p.3; definition |
| What is the parameter of Exponential$(\beta)$ in this course? | **The rate $\beta > 0$, events per unit of time.** | Lecture_01 p.3; definition |
| Write the Exponential PDF (rate form). | $f(x) = \beta e^{-\beta x}$ for $x > 0$. | Lecture_01 p.3; formula |
| Where is the Exponential PDF highest? | **At x = 0: short waits are the most common.** | Distribution Sheets; motivation |
| For an Exponential$(\beta)$ wait, what is $\mathbb{P}(X > t)$? | $e^{-\beta t}$. | Distribution Sheets; formula |
| Buses come at 4 per hour. What is the average wait? | **$1/4$ hour = 15 minutes.** | worked example |
| Buses come at 4 per hour. What is the chance of waiting more than an hour? | $e^{-4} \approx 0.018$. | worked example |
| What does "memoryless" mean for the Exponential? | **Having already waited does not change the wait still to come**: $\mathbb{P}(X > s + t \mid X > s) = \mathbb{P}(X > t)$. | Distribution Sheets; definition |
| What is the Exponential likelihood kernel for waits $x_1, \dots, x_n$? | $\beta^n e^{-\beta \sum x_i}$: number of waits in the power, total time in the exponent. | Kernels Table 2; formula; dep: [[Bayes Update Algorithm]] |
| With a Gamma$(\alpha, b)$ prior and Exponential waits $x_1, \dots, x_n$, what is the posterior? | **Gamma$(\alpha + n, b + \sum x_i)$.** | Kernels Table 3; assembly; dep: [[Bayes Update Algorithm]] |
| Exponential vs Poisson: which one measures a time? | **Exponential: the time between events. Poisson: the number of events in a window.** | discrimination |
| Which Gamma equals Exponential$(\beta)$? | **Gamma$(1, \beta)$.** | Distribution Sheets; assembly |
# Node map
```json
[
 {
  "name": "Exponential distribution",
  "uses": [],
  "type": "concept",
  "existing": true,
  "parent": "Common Distributions",
  "prereqs": [],
  "page": 3,
  "summary": "Waiting time until the next event at rate $\\beta$: $\\beta e^{-\\beta x}$, mean $1/\\beta$, memoryless."
 }
]
```

# Frankenstein problems

None yet.
