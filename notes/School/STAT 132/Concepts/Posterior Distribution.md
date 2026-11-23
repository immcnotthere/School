---
type: concept
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "Reading 2 §2.6.3, ch. 3 §3.1–3.2; DS 7.2"
week: [1, 2]
prereqs:
  - "[[Bayes' Rule]]"
  - "[[Likelihood Function]]"
  - "[[Prior Distribution]]"
  - "[[Bayes' Theorem for Distributions]]"
retention_band: cold
---
# Posterior distribution

$$\pi(\theta\mid\mathbf x)=\frac{f(\mathbf x\mid\theta)\pi(\theta)}{m_n(\mathbf x)},\qquad m_n(\mathbf x)=\int_\Theta f(\mathbf x\mid\theta)\pi(\theta)\,d\theta$$
$$\pi(\theta\mid\mathbf x)\propto L(\theta)\,\pi(\theta)$$
The marginal $m_n$ is just the normalizing constant (it has no $\theta$).

**Workflow:** multiply the [[Likelihood Function]] by the [[Prior Distribution]], keep only the $\theta$ terms, and **recognize the kernel** (see [[Conjugate Prior]]).
Summaries: posterior mean $E[\theta\mid\mathbf x]$, variance $\mathrm{Var}(\theta\mid\mathbf x)$, quantiles, and credible intervals.
