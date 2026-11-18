---
type: concept
parent: "[[Posterior Distribution]]"
prereqs:
  - "[[Prior as Pretend Data]]"
  - "[[Gamma-Poisson Update]]"
  - "[[Beta-Bernoulli Update]]"
domain: stats
course: "STAT 132"
status: draft
mastery: 0
---
# Posterior Mean as a Weighted Average

The posterior's settings are pretend data plus real data, so its mean is the prior belief and the data's average weighted by how much each is worth; it always lands between them, and more data pulls it toward the data.

Example: (2 hours × 3 + 4 hours × 3.5)/6 = 3.33 = 20/6.

Procedure: [[Bayes Update Algorithm]] step 6.
