---
type: concept
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "Lec 1 §2; Reading 1 §1.8"
week: 1
prereqs:
  - "[[What Is Statistical Inference]]"
retention_band: cold
---
# Probability vs. inference

> That reversal from using a probability to anticipate data, to using data to learn about a probability, is the move from probability theory to statistical inference.

The same model is used in opposite directions.

- **Probability:** the model and parameter are known, the data are uncertain. With a fair coin, $P(6\text{ heads in }10) = \binom{10}{6}0.5^{10} \approx 0.205$.
- **Inference:** the data are known, the parameter is uncertain. We saw 8/10 heads. Is $p=0.5$ still plausible? The estimate is $\hat p = 0.8$, but $P(X\ge 8 \mid p=.5)\approx 0.055$, so a fair coin can plausibly do this.

Pipeline: population model → random sample → [[Statistic (inference)]] → inference about the population.
