---
type: concept
parent: "[[Kernel of a Distribution]]"
prereqs:
  - "[[Kernel of a Distribution]]"
  - "[[Normalizing Constant]]"
  - "[[Conjugate Prior]]"
domain: stats
course: "STAT 132"
status: draft
mastery: 0
---
# Naming the Curve Normalizes (Kernel Matching)

With a partner prior, prior kernel × likelihood kernel has the partner's shape, because same bases add exponents. Match it to the shape, read off the settings, and that named curve's built-in constant makes the area 1, so nothing is computed. The named curve also gives the mean (Gamma α/β). Fails if the prior is not the partner or the shape matches nothing; then add (list) or find the area directly. Watch the minus-1 trap.

Example: λ^19 e^(−6λ) matches λ^(α−1) e^(−βλ), so Gamma(20, 6), mean 3.33.

Procedure: [[Bayes Update Algorithm]] step 6.
