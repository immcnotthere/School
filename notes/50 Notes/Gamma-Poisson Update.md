---
type: concept
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "Reading 2 §3.5; DS 7.3"
week: 2
prereqs:
  - "[[Conjugate Prior]]"
  - "[[Gamma and Beta Functions]]"
  - "[[Poisson Distribution]]"
  - "[[Gamma Distribution]]"
retention_band: cold
---
# Gamma–Poisson update

Prior $\lambda\sim\text{Gamma}(\alpha,\beta)$ (rate form), data $X_i\sim$ Poisson($\lambda$) iid:
$$\lambda\mid\mathbf x\sim\text{Gamma}\Big(\alpha+\sum x_i,\ \beta+n\Big)$$
The shape adds the total events and the rate adds the exposure units.

Example: Gamma(8,2) with counts 3,6,4,7,5 → Gamma(33,7). Mean 4.71, between the prior 4 and $\bar x$=5.
This assumes equal exposure per observation; otherwise you must model the exposure.
