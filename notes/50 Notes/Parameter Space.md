---
type: concept
parent: "[[Statistical Model]]"
prereqs:
  - "[[Parameters]]"
contrasts_with:
  - "[[Sample Space]]"
domain: stats
course: "STAT 132"
status: draft
mastery: 0
retention_band: cold
---
# Parameter Space

The set of values the unknown parameter can take, as opposed to the sample space (values one result X can take). Step 1 sets X's values; the model then fixes the parameter's range (Bernoulli/Binomial θ in 0 to 1; Poisson λ above 0; Exponential β above 0; Normal μ any number).

Example: help desk calls X in {0,1,2,...} (counted) but λ is any number above 0 (measured); 3.5 calls per hour is a valid λ though no hour has 3.5 calls.

Procedure: [[Bayes Update Algorithm]] step 2a.
