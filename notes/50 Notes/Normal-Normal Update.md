---
type: concept
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "Reading 2 §3.6; DS 7.3"
week: 2
prereqs:
  - "[[Conjugate Prior]]"
  - "[[Normal distribution]]"
retention_band: cold
---
# Normal–Normal update ($\sigma^2$ known)

$X_i\mid\mu\sim N(\mu,\sigma^2)$ and $\mu\sim N(\mu_0,\sigma_0^2)$ give $\mu\mid\mathbf x\sim N(\mu_1,\sigma_1^2)$, where
$$\frac1{\sigma_1^2}=\frac1{\sigma_0^2}+\frac n{\sigma^2},\qquad
\mu_1=\frac{\mu_0/\sigma_0^2+n\bar x/\sigma^2}{1/\sigma_0^2+n/\sigma^2}=\frac{\sigma^2\mu_0+n\sigma_0^2\bar x}{\sigma^2+n\sigma_0^2}$$
**Posterior precision = prior precision + data precision.** The mean is a precision-weighted average.

Example: $\mu_0=52,\sigma_0=6,\sigma=8,n=16,\bar x=48$ gives $\mu_1=48.4$, $\sigma_1\approx1.90$.
It only depends on the data through $\bar x$. Unknown $\sigma^2$ is a different calculation.
