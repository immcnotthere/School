---
type: concept
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "Reading 2 §3.4; DS 7.3"
week: 2
prereqs:
  - "[[Conjugate Prior]]"
  - "[[Gamma and Beta Functions]]"
  - "[[Bernoulli Distribution]]"
  - "[[Beta Distribution]]"
retention_band: cold
---
# Beta–Bernoulli update

Prior $p\sim\text{Beta}(\alpha,\beta)$, with $s$ successes in $n$ trials:
$$p\mid\mathbf x\sim\text{Beta}(\alpha+s,\ \beta+n-s)$$
Add the successes to $\alpha$ and the failures to $\beta$. This works because $p^s(1-p)^{n-s}\cdot p^{\alpha-1}(1-p)^{\beta-1}$ is a Beta kernel.

Example: prior Beta(5,5), 21/30 yes → Beta(26,14). Posterior mean $26/40=.65$, between the prior .5 and $\hat p$=.7. Var ≈ .00555.
Posterior mean $=\frac{\alpha+s}{\alpha+\beta+n}$, a weighted blend of the prior mean and $s/n$.
Practice: Disc 1 Q1 (find a Beta from its mean and var), Disc 2 Q1.
