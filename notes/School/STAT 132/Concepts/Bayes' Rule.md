---
type: concept
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "Lec 1 §1.1; Reading 1 §1.2.1; DS 2.3"
week: 1
prereqs:
  - "[[Conditional Probability]]"
retention_band: cold
---
# Bayes' rule

$$P(A\mid B)=\frac{P(B\mid A)P(A)}{P(B\mid A)P(A)+P(B\mid A^c)P(A^c)}$$

- $P(A)$: prior plausibility
- $P(B\mid A)$: how compatible the observation is with $A$
- $P(A\mid B)$: posterior plausibility

**The base rate matters.** Suppose 2% of papers are copied, the detector catches 90%, and it falsely flags 5%.
$P(\text{copied}\mid\text{flag}) = \frac{.9(.02)}{.9(.02)+.05(.98)} \approx 0.27$.

For distributions this becomes [[Posterior Distribution]] ∝ [[Likelihood Function]] × [[Prior Distribution]].
