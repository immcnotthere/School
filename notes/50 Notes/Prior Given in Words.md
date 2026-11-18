---
type: concept
parent: "[[Prior Distribution]]"
prereqs:
  - "[[Prior Distribution]]"
contrasts_with:
  - "[[Prior Given as Numbers]]"
  - "[[Prior Not Given (Choose Equal Weights)]]"
domain: stats
course: "STAT 132"
status: draft
mastery: 0
retention_band: cold
---
# Prior Given in Words

The problem describes the prior in words, and you translate the words into numbers.

Example: "the friend's claim and my guess are equally likely" with $\theta \in \{0.8, 0.5\}$ means $\pi(0.8) = \pi(0.5) = 0.5$.
Continuous version: "$\theta$ is uniform on [0, 1]" means every $\theta$ in [0, 1] is equally plausible. That is Beta(1, 1).

Do the translation first, then treat it like a prior given as numbers. The 5 shots with 4 makes and 1 miss come after. The prior is fixed in step 2 of the Bayes workflow, before looking at the data.

Compare: [[Prior Given as Numbers]], [[Prior Not Given (Choose Equal Weights)]]. Part of [[Prior Distribution]]; it feeds [[Posterior Distribution]].
