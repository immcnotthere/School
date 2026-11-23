---
type: concept
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "Reading 2 §3.7"
week: 2
prereqs:
  - "[[Normal-Normal Update]]"
  - "[[Beta-Bernoulli Update]]"
retention_band: cold
---
# How much does the prior matter?

- **Location:** it pulls the posterior mean toward $\mu_0$.
- **Concentration:** a small prior variance means strong pull (prior SD 2 keeps the posterior near 45; SD 12 lets it move toward $\bar x$=54).
- **Sample size:** as $n$ grows, the data precision $n/\sigma^2$ dominates and reasonable priors converge.

More data does **not** fix bias, dependence, or a wrong model: "a very precise answer to the wrong question."
See [[Normal-Normal Update]], [[Beta-Bernoulli Update]].
