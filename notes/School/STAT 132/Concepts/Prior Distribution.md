---
type: concept
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "Reading 2 §2.6; DS 7.2"
week: 1
prereqs:
  - "[[Bayesian Approach]]"
  - "[[Parameters]]"
retention_band: cold
---
# Prior distribution $\pi(\theta)$

It describes uncertainty about $\theta$ **before** the current data. It must live on the [[Parameters]] (Beta for $p$, Gamma for a rate).
Sources: earlier studies, historical data, science, expert judgment, weak "rule-out-absurd" info. Justify the choice, and never pick it to get a desired answer.

The shape encodes strength. Beta(1,1) is flat; Beta(6,4) and Beta(30,20) both have mean .6, but the second is far more confident.
"Flat" ≠ "no information": uniform on $p$ is not uniform on a transform of $p$.

## Three ways a prior reaches you
- Given as numbers, use as is: [[Prior Given as Numbers]]
- Given in words, translate to numbers: [[Prior Given in Words]]
- Not given, choose equal weights: [[Prior Not Given (Choose Equal Weights)]]

Whichever way, the prior is set before you look at the data.
Map: [[Prior Sources.canvas]]
