---
type: concept
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "Lec 1 §1.3; Reading 1 §1.4"
week: 1
prereqs:
  - "[[Random variable]]"
retention_band: cold
---
# PMF, PDF, CDF

- **PMF** (discrete): $f(x)=P(X=x)$. It is nonnegative and sums to 1.
- **PDF** (continuous): $P(a\le X\le b)=\int_a^b f(x)\,dx$. The *height is not a probability*, and $P(X=x)=0$.
- **CDF** (both): $F(x)=P(X\le x)$. It is non-decreasing and runs from 0 to 1. $P(a<X\le b)=F(b)-F(a)$.

R: `d*` = PMF/PDF, `p*` = CDF, `q*` = quantile, `r*` = random draws (e.g. `pnorm(30,25,6)` ≈ 0.798).
