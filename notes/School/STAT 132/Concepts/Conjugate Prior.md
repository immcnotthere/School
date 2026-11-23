---
type: concept
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "Reading 2 §3.3; DS 7.3"
week: 2
prereqs:
  - "[[Posterior Distribution]]"
  - "[[Common Distributions]]"
qualifies:
  - "[[Posterior Distribution]]"
retention_band: cold
---
# Conjugate prior

A prior is conjugate to a likelihood if the posterior is in the **same family**; only the hyperparameters update.

| Data model | Parameter | Prior → Posterior |
|---|---|---|
| Bernoulli / Binomial | $p$ | Beta → Beta: [[Beta-Bernoulli Update]] |
| Poisson | $\lambda$ | Gamma → Gamma: [[Gamma-Poisson Update]] |
| Normal, $\sigma^2$ known | $\mu$ | Normal → Normal: [[Normal-Normal Update]] |

It is convenient and transparent, but convenience alone isn't a reason; the prior must still be reasonable.
