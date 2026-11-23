---
type: problem
parent: "[[Posterior Distribution]]"
domain: stats
course: "STAT 132"
status: draft
source: "Lecture_03 p.3"
uses:
  - "[[Bayes' Rule]]"
  - "[[Beta-Bernoulli Update]]"
retention_band: cold
---
# Defective Items Posterior

A Uniform(0,1) prior on a defect proportion $\theta$ combined with Bernoulli data yields, via $\pi(\theta\mid x)\propto f(x\mid\theta)\pi(\theta)$, a Beta$(1+\sum x_i,\,1+n-\sum x_i)$ posterior.

Cards: [[STAT 132 Cards - Lecture_03#Defective Items Posterior]]
