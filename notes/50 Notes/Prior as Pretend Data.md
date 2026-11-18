---
type: concept
parent: "[[Conjugate Prior]]"
prereqs:
  - "[[Beta Distribution]]"
  - "[[Gamma Distribution]]"
qualifies:
  - "[[Prior Influence and Sample Size]]"
domain: stats
course: "STAT 132"
status: draft
mastery: 0
---
# Prior as Pretend Data

A partner prior's two settings are pretend data: center = the prior mean, strength = how much pretend data it is worth. Use TOTALS. Beta(α, β): α pretend successes, β pretend failures, mean α/(α+β). Gamma(α, β) for a Poisson rate: α pretend events over β pretend windows, mean α/β. Check: the mean must equal the stated belief, not the data.

Example: "about 60%, as sure as 10 shots" = Beta(6, 4); "6 calls in 2 hours" = Gamma(6, 2), not Gamma(3, 1), which has the same center and half the strength.

Procedure: [[Bayes Update Algorithm]] step 2c-Cii.
