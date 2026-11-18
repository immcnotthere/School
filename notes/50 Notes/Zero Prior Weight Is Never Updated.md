---
type: concept
parent: "[[Prior Distribution]]"
prereqs:
  - "[[Prior Distribution]]"
  - "[[Posterior Proportionality]]"
qualifies:
  - "[[List Prior vs Curve Prior]]"
domain: stats
course: "STAT 132"
status: draft
mastery: 0
---
# Zero Prior Weight Is Never Updated

A value with prior weight 0 has posterior 0 whatever the data, since 0 × likelihood = 0. So "about 3" must be a curve, not {3: 1.0}, and two-candidate lists can never discover a value outside the list.

Example: the free-throw list could never find a 65% shooter.

Procedure: [[Bayes Update Algorithm]] step 2c.
