---
type: concept
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "Reading 2 §2.5.4"
week: 1
prereqs:
  - "[[Likelihood Function]]"
retention_band: cold
---
# Log-likelihood

$\ell(\theta)=\log L(\theta)=\sum_i \log f(x_i\mid\theta)$
- It turns the product into a sum, which avoids numerical underflow and makes derivatives easy.
- log is increasing, so $\arg\max \ell = \arg\max L$. This is how MLEs are found: solve $\ell'(\theta)=0$.
From [[Likelihood Function]].
