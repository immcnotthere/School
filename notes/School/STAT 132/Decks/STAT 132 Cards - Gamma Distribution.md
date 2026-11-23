---
type: reference
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "Gamma Distribution"
tags:
  - decks
---
# STAT 132 Cards - Gamma Distribution (a positive quantity, often a prior for a rate)

## Gamma Distribution
| Front | Back | Notes |
| --- | --- | --- |
| What two stories does the Gamma distribution tell in this course? | **The total wait for $\alpha$ events at rate $\beta$, and (mostly) a prior for a positive parameter like a Poisson $\lambda$.** | Lecture_01 p.3; definition |
| What values can a Gamma variable take? | **Any number above 0.** | Lecture_01 p.3; definition |
| What are the parameters of Gamma$(\alpha, \beta)$ in this course? | **Shape $\alpha > 0$ and rate $\beta > 0$.** *Side note, not tested: some books use a scale $1/\beta$ instead; check which.* | Lecture_01 p.3; definition |
| Write the Gamma PDF (rate form). | $f(x) = \dfrac{\beta^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\beta x}$ for $x > 0$. | Lecture_01 p.3; formula; if stuck: Gamma and Beta Functions deck |
| What is the Gamma kernel? | $x^{\alpha-1} e^{-\beta x}$: the power pushes up, the exponential pulls down. | Kernels Table 1; formula; dep: [[Bayes Update Algorithm]] |
| In the Gamma PDF, what job does $\beta^\alpha / \Gamma(\alpha)$ do? | **It makes the total area 1.** | motivation; if stuck: Gamma and Beta Functions deck |
| What is the mean of Gamma$(\alpha, \beta)$? | $\alpha / \beta$. | Lecture_01 p.3; formula |
| What is the variance of Gamma$(\alpha, \beta)$? | $\alpha / \beta^2$. | Lecture_01 p.3; formula |
| What is the mean of Gamma(3, 2)? | $3/2 = 1.5$. | worked example |
| What is the variance of Gamma(3, 2)? | $3/2^2 = 0.75$. | worked example |
| Read the posterior kernel $\lambda^{19} e^{-6\lambda}$ as a Gamma. | **Gamma(20, 6)**: power plus 1 gives $\alpha$; the number in front of $\lambda$ gives $\beta$. | worked example; dep: [[Bayes Update Algorithm]] |
| A Gamma prior has mean m and variance v. What are its $\beta$ and $\alpha$? | $\beta = m / v$, then $\alpha = m\beta$. | Distribution Sheets; formula |
| A Gamma prior has mean 0.0002 and SD 0.0001. What are $\alpha$ and $\beta$? | **Variance $10^{-8}$, so $\beta = 20{,}000$ and $\alpha = 4$.** | worked example |
| How do you read Gamma$(\alpha, \beta)$ as pretend data for a rate? | **$\alpha$ pretend events seen over $\beta$ pretend windows (or time).** | assembly; dep: [[Bayes Update Algorithm]] |
| Which Gamma is an Exponential? | **Gamma$(1, \beta)$ = Exponential$(\beta)$.** | Distribution Sheets; assembly |
| Which data models take a Gamma as their partner prior? | **Poisson (rate $\lambda$) and Exponential (rate $\beta$).** | Kernels Table 3; assembly; dep: [[Bayes Update Algorithm]] |
| Gamma vs Beta as a prior: how do you choose? | **Gamma for a parameter above 0 (a rate); Beta for a parameter between 0 and 1 (a probability).** | discrimination; dep: [[Bayes Update Algorithm]] |
# Node map
```json
[
 {
  "name": "Gamma Distribution",
  "uses": [],
  "type": "concept",
  "existing": true,
  "parent": "Common Distributions",
  "prereqs": [
   "Gamma and Beta Functions"
  ],
  "page": 3,
  "summary": "Positive quantity with shape $\\alpha$ and rate $\\beta$: $\\frac{\\beta^\\alpha}{\\Gamma(\\alpha)}x^{\\alpha-1}e^{-\\beta x}$, mean $\\alpha/\\beta$, variance $\\alpha/\\beta^2$."
 }
]
```

# Frankenstein problems

None yet.
