---
type: concept
parent: "[[Bayesian Inference]]"
prereqs:
  - "[[Statistical Model]]"
  - "[[Prior Distribution]]"
contrasts_with:
  - "[[Likelihood Function]]"
domain: stats
course: "STAT 132"
status: draft
mastery: 0
---
# Data Model vs Prior Model

Two separate models: the data model describes one result X (Poisson, Bernoulli); the prior describes your belief about the parameter (Gamma, Beta). X's dictionary never contains the prior; they meet only when multiplied in step 5.

Example: X ~ Poisson(λ), prior λ ~ Gamma(6, 2); the Poisson formula e^(−λ) λ^x / x! has no Gamma in it.

Procedure: [[Bayes Update Algorithm]] step steps 1, 2 and 5.
