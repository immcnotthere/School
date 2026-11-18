---
type: concept
parent: "[[Prior Distribution]]"
prereqs:
  - "[[Prior Distribution]]"
contrasts_with:
  - "[[Prior Given in Words]]"
  - "[[Prior Not Given (Choose Equal Weights)]]"
domain: stats
course: "STAT 132"
status: draft
mastery: 0
retention_band: cold
---
# Prior Given as Numbers

The problem states the prior as numbers, so you use it as is. Nothing to translate and nothing to choose.

Example: your friend claims an 80% shooter and you say 50%. So $\theta \in \{0.8, 0.5\}$, and the problem says $\pi(0.8) = 0.3$ and $\pi(0.5) = 0.7$. Write those down and go.

The data (5 shots, 4 makes, 1 miss) comes later. The prior is fixed in step 2 of the Bayes workflow, before looking at the data.

Compare: [[Prior Given in Words]], [[Prior Not Given (Choose Equal Weights)]]. Part of [[Prior Distribution]]; it feeds [[Posterior Distribution]].
