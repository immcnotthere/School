---
type: concept
parent: "[[Posterior Proportionality]]"
prereqs:
  - "[[Posterior Proportionality]]"
  - "[[Normalizing Constant]]"
qualifies:
  - "[[Posterior Proportionality]]"
domain: stats
course: "STAT 132"
status: draft
mastery: 0
---
# When Not to Drop Constants

Drop a factor only if it has no θ and you are comparing values of θ (posterior shape, MLE): it scales every θ the same and normalizing cancels it (free throws ×1000 gives the same 0.531/0.469). Keep it when asked for an actual chance of the data at a specific θ (P(X = 3) if λ = 2) or an actual height/probability from the posterior; then use the posterior's own constant from its named curve, never the dropped one.

Example: 1/34,560 = 1/(3!·5!·2!·4!) dropped from the help-desk likelihood.

Procedure: [[Bayes Update Algorithm]] step 4c.
