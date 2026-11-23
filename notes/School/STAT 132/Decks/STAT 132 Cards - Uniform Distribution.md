---
type: reference
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "Uniform Distribution"
tags:
  - decks
---
# STAT 132 Cards - Uniform Distribution (every value equally likely)

## Uniform Distribution (Continuous)
| Front | Back | Notes |
| --- | --- | --- |
| What story does a continuous Uniform$(a, b)$ tell? | **Any value between a and b is as likely as any other.** | Lecture_01 p.3; definition |
| What are the parameters of Uniform$(a, b)$ and their rule? | **The two ends a and b, with $a < b$.** | Lecture_01 p.3; definition |
| Write the Uniform$(a, b)$ PDF. | $f(x) = \dfrac{1}{b - a}$ for x in $[a, b]$, and 0 elsewhere. | Lecture_01 p.3; formula |
| Why is the Uniform height $1/(b-a)$? | **The area of a rectangle of width $b - a$ must be 1**, so the height is $1/(b-a)$. | motivation |
| What is the height of the Uniform(0, 10) PDF? | $1/10 = 0.1$. | worked example |
| What is the mean of Uniform(0, 10)? | **5**, the midpoint. | worked example |
| What is the variance of Uniform(0, 10)? | $100/12 \approx 8.33$. | worked example |
| Uniform(0, 10): what is $\mathbb{P}(2 \le X \le 5)$? | **$3 \times 0.1 = 0.3$** (width times height). | worked example |
| Which Beta equals Uniform(0, 1)? | **Beta(1, 1).** | Distribution Sheets; assembly |
| Why is a Uniform(0, 10) prior risky for a rate? | **It gives zero weight above 10, so the posterior can never go there**, whatever the data say. | Distribution Sheets; motivation; dep: [[Bayes Update Algorithm]] |
| Uniform vs Normal: which has a flat shape with hard edges? | **Uniform.** The Normal peaks at its center and never quite reaches zero. | discrimination |
# Node map
```json
[
 {
  "name": "Uniform Distribution (Continuous)",
  "uses": [],
  "type": "concept",
  "existing": true,
  "parent": "Common Distributions",
  "prereqs": [],
  "page": 3,
  "summary": "Every value in $[a, b]$ equally likely: height $1/(b-a)$, mean $(a+b)/2$, variance $(b-a)^2/12$."
 }
]
```

# Frankenstein problems

None yet.
