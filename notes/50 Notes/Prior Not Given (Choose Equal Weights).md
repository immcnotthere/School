---
type: concept
parent: "[[Prior Distribution]]"
prereqs:
  - "[[Prior Distribution]]"
contrasts_with:
  - "[[Prior Given as Numbers]]"
  - "[[Prior Given in Words]]"
domain: stats
course: "STAT 132"
status: draft
mastery: 0
retention_band: cold
---
# Prior Not Given (Choose Equal Weights)

The problem gives no prior, so you must choose one. The usual default is equal weights over the candidates (uniform, flat).

Example: with $\theta \in \{0.8, 0.5\}$ and nothing said, choose $\pi(0.8) = \pi(0.5) = 0.5$. Say that you chose it.
Caution: flat is not the same as no information. It is still a choice, and it can change the answer (see [[Prior Distribution]]).

The prior is fixed in step 2 of the Bayes workflow, before looking at the data (5 shots, 4 makes, 1 miss).

Compare: [[Prior Given as Numbers]], [[Prior Given in Words]]. It feeds [[Posterior Distribution]].
