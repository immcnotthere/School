---
type: reference
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "Binomial Distribution"
tags:
  - decks
---
# STAT 132 Cards - Binomial Distribution (number of successes in n tries)

## Binomial Distribution
| Front | Back | Notes |
| --- | --- | --- |
| What story does a Binomial random variable tell? | **Count the successes in n independent tries, each with the same chance p.** *Side note, not tested: Example: heads in 10 flips.* | Lecture_01 p.3; definition |
| What values can a Binomial$(n, p)$ variable take? | **Whole numbers 0, 1, ..., n.** *Side note, not tested: It has a fixed maximum.* | Lecture_01 p.3; definition |
| What are the parameters of a Binomial and their allowed values? | **n, a positive whole number (number of tries); p, between 0 and 1 (chance of success).** | Lecture_01 p.3; definition |
| Write the Binomial PMF. | $\mathbb{P}(X = x) = \binom{n}{x} p^x (1-p)^{n-x}$. *Read aloud: "n choose x, times p to the x, times one minus p to the n minus x."* | Lecture_01 p.3; formula |
| In the Binomial PMF, what is $p^x$ doing? | **The x successes, each with chance p, multiplied together.** | Lecture_01 p.3; motivation |
| In the Binomial PMF, what is $(1-p)^{n-x}$ doing? | **The n minus x failures, each with chance 1 minus p.** | Lecture_01 p.3; motivation |
| In the Binomial PMF, what is $\binom{n}{x}$ doing? | **Counting the orders the x successes could come in** (HHT, HTH, THH are 3 orders for 2 heads in 3). | Lecture_01 p.3; motivation |
| Why is the Binomial mean np? | **It is n Bernoulli tries, each with mean p; means add.** | Lecture_01 p.3; motivation |
| Why does the Binomial variance add up as $np(1-p)$? | **The n tries are independent, so their variances $p(1-p)$ add.** | Lecture_01 p.3; motivation |
| Flip a fair coin 3 times. What is $\mathbb{P}(\text{exactly 2 heads})$? | $\binom{3}{2}(0.5)^2(0.5)^1 = 3 \times 0.125 = 0.375$. | worked example |
| Binomial with n = 5, p = 0.2: what is $\mathbb{P}(X = 0)$? | $(0.8)^5 \approx 0.328$. | worked example |
| What is the mean of a Binomial with n = 10, p = 0.3? | $10(0.3) = 3$. | worked example |
| What is the variance of a Binomial with n = 10, p = 0.3? | $10(0.3)(0.7) = 2.1$. | worked example |
| How is a Bernoulli related to a Binomial? | **A Bernoulli is a Binomial with n = 1.** | Distribution Sheets; assembly |
| When is a Binomial close to a Poisson? | **When n is huge and p is tiny, with $np = \lambda$.** Then Binomial$(n, p) \approx$ Poisson$(\lambda)$. | Distribution Sheets; assembly |
| What is the Binomial likelihood kernel in p for x successes out of n? | $p^x (1-p)^{n-x}$. *Side note, not tested: $\binom{n}{x}$ has no p, so it is dropped.* | Kernels Table 2; formula; dep: [[Bayes Update Algorithm]] |
| With a Beta$(\alpha, \beta)$ prior, what is the posterior after x successes in n Binomial tries? | **Beta$(\alpha + x, \beta + n - x)$.** | Kernels Table 3; assembly; dep: [[Bayes Update Algorithm]] |
| Binomial vs Poisson: which has a fixed maximum count? | **Binomial** (at most n). *Side note, not tested: The Poisson count has no upper limit.* | discrimination |
# Node map
```json
[
 {
  "name": "Binomial Distribution",
  "uses": [],
  "type": "concept",
  "existing": true,
  "parent": "Common Distributions",
  "prereqs": [
   "Bernoulli Distribution"
  ],
  "page": 3,
  "summary": "Number of successes in n independent tries with the same chance p: $\\binom{n}{x}p^x(1-p)^{n-x}$, mean np, variance np(1-p)."
 }
]
```

# Frankenstein problems

None yet.
