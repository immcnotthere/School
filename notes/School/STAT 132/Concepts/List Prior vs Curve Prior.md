---
type: concept
parent: "[[Prior Distribution]]"
prereqs:
  - "[[Prior Distribution]]"
  - "[[Parameter Space]]"
domain: stats
course: "STAT 132"
status: draft
mastery: 0
---
# List Prior vs Curve Prior

A prior is a list (named candidate values, each with a weight) or a curve (every value in the parameter space gets a weight). Test: does the problem name possible values of the parameter, each with a weight? List: step 6 adds and divides. Curve: step 6 names the curve. Works for every data model.

Example: free throws {0.8: 0.3, 0.5: 0.7} is a list; "about 3 calls per hour, as sure as 6 calls in 2 hours" is a curve, Gamma(6, 2); "λ is 2 or 4, equally likely" would be a Poisson list.

Procedure: [[Bayes Update Algorithm]] step 2c.
