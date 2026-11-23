---
type: concept
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "Lec 1 Aside 1.1; Reading 1 §1.6.5–6"
week: 1
retention_band: cold
prereqs:
  - "[[Factorial]]"
---
# Gamma and Beta functions

$\Gamma(x)=\int_0^\infty t^{x-1}e^{-t}dt$, and $\Gamma(n)=(n-1)!$. Useful: $\Gamma(x+1)=x\Gamma(x)$.

$B(\alpha,\beta)=\dfrac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}=\int_0^1 x^{\alpha-1}(1-x)^{\beta-1}dx$

In a density they are just **normalizing constants**. That is why [[Conjugate Prior]] problems can drop them and then recognize the kernel.
