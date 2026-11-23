---
type: reference
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "Beta Distribution"
tags:
  - decks
---
# STAT 132 Cards - Beta Distribution (an unknown proportion)

## Beta Distribution
| Front | Back | Notes |
| --- | --- | --- |
| What story does the Beta distribution tell in this course? | **A random number between 0 and 1; mostly the prior for a probability p** (coin bias, defect rate). | Lecture_01 p.3; definition |
| What values can a Beta variable take? | **Numbers strictly between 0 and 1.** | Lecture_01 p.3; definition |
| What are the parameters of Beta$(\alpha, \beta)$ and their allowed values? | **$\alpha > 0$ and $\beta > 0$, both shapes.** *Side note, not tested: this $\beta$ is not a rate.* | Lecture_01 p.3; definition |
| Write the Beta PDF. | $f(x) = \dfrac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha, \beta)}$ for $0 < x < 1$. | Lecture_01 p.3; formula; if stuck: Gamma and Beta Functions deck |
| What is the Beta kernel? | $x^{\alpha-1}(1-x)^{\beta-1}$. | Kernels Table 1; formula; dep: [[Bayes Update Algorithm]] |
| Why is the distribution called Beta? | **It is named after the Beta function $B(\alpha, \beta)$ in its constant**, not after the letter. | Distribution Sheets; motivation; if stuck: Gamma and Beta Functions deck |
| What is the mean of Beta$(\alpha, \beta)$? | $\dfrac{\alpha}{\alpha + \beta}$. | Lecture_01 p.3; formula |
| What is the variance of Beta$(\alpha, \beta)$, in the easy form? | $\dfrac{m(1-m)}{s+1}$ with $m$ the mean and $s = \alpha + \beta$. | Distribution Sheets; formula |
| What is the mean of Beta(3, 6)? | $3/9 = 1/3$. | worked example |
| What is the variance of Beta(3, 6)? | $\dfrac{(1/3)(2/3)}{3 + 6 + 1} = \dfrac{1}{45}$. | worked example |
| Which way does Beta$(\alpha, \beta)$ lean when $\alpha > \beta$? | **Toward 1.** *Side note, not tested: $\alpha < \beta$ leans toward 0; $\alpha = \beta$ is symmetric about 0.5.* | Distribution Sheets; definition |
| Read $p^8(1-p)^2$ as a Beta. | **Beta(9, 3)**: add 1 to each exponent (the minus-1 trap). | worked example; dep: [[Bayes Update Algorithm]] |
| A Beta prior has mean m and variance v. How do you find its settings? | **Solve $v = \frac{m(1-m)}{s+1}$ for s, then $\alpha = ms$ and $\beta = (1-m)s$.** | Distribution Sheets; formula |
| How do you read Beta$(\alpha, \beta)$ as pretend data? | **$\alpha$ pretend successes and $\beta$ pretend failures.** | assembly; dep: [[Bayes Update Algorithm]] |
| Which Beta is the Uniform(0, 1)? | **Beta(1, 1)**, the "I know nothing" prior for p. | Distribution Sheets; assembly |
| With a Beta prior and x successes in n Bernoulli trials, what is the posterior? | **Beta$(\alpha + x, \beta + n - x)$** (DeGroot Theorem 7.3.1). | Kernels Table 3; assembly; dep: [[Bayes Update Algorithm]] |
| Flat Beta(1, 1) prior, 4 makes in 5 shots: what is the posterior? | **Beta(5, 2)**, mean $5/7 \approx 0.71$. | worked example; dep: [[Bayes Update Algorithm]] |
# Node map
```json
[
 {
  "name": "Beta Distribution",
  "uses": [],
  "type": "concept",
  "existing": true,
  "parent": "Common Distributions",
  "prereqs": [
   "Gamma and Beta Functions"
  ],
  "page": 3,
  "summary": "Random proportion on 0 to 1: $x^{\\alpha-1}(1-x)^{\\beta-1}/B(\\alpha,\\beta)$, mean $\\alpha/(\\alpha+\\beta)$."
 }
]
```

# Frankenstein problems

None yet.
