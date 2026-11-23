---
type: concept
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "Lec 1 §1.6; Reading 1 §1.7.2"
week: 1
prereqs:
  - "[[Expectation and Variance]]"
  - "[[Law of Large Numbers]]"
  - "[[Standardization (math)]]"
  - "[[Sample Mean]]"
  - "[[Normal distribution]]"
  - "[[Independence of Random Variables]]"
retention_band: cold
---
# Central limit theorem

If the population has mean $\mu$ and finite SD $\sigma$, then for large $n$
$$\bar X \;\dot\sim\; N\!\left(\mu,\ \sigma^2/n\right),\qquad \mathrm{SD}(\bar X)=\sigma/\sqrt n.$$
This holds even when the population is skewed (e.g. Exp).
It does **not** say the data become normal. It describes the **sampling distribution** of the [[Statistic (inference)]] $\bar X$ over repeated samples.
