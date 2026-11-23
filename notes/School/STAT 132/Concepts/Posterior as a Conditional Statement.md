---
type: concept
parent: "[[Posterior Distribution]]"
prereqs:
  - "[[Posterior Distribution]]"
domain: stats
course: "STAT 132"
status: draft
mastery: 0
---
# Posterior as a Conditional Statement

A posterior is an if-then: if the model, independence, the shared parameter and the prior all hold, then this is the updated belief. The parameter is one fixed number; the posterior measures belief about it. A wrong assumption makes it the answer to a different question.

Example: "53% the friend is an 80% shooter" assumes θ is only 0.8 or 0.5; with a flat Beta(1,1) prior the same 4 of 5 gives Beta(5, 2), and the most likely region is 0.5 to 0.8 (0.55).

Procedure: [[Bayes Update Algorithm]] step 6.
