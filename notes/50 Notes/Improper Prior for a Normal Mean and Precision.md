---
type: concept
parent: "[[Bayesian Inference]]"
domain: stats
course: "STAT 132"
status: draft
source: "DeGroot 8.6 Bayesian Normal Samples p.517"
prereqs:
  - "[[Improper Prior]]"
  - "[[Normal-Gamma Posterior Update]]"
mastery: 0
retention_band: cold
---
# Improper Prior for a Normal Mean and Precision

The usual improper prior for $(\mu,\tau)$ is $\xi(\mu,\tau)\propto 1/\tau$; plugging pretend hyperparameters $\mu_0=\lambda_0=\beta_0=0,\alpha_0=-1/2$ into the normal-gamma update gives posterior $\mu_1=\bar x_n,\lambda_1=n,\alpha_1=(n-1)/2,\beta_1=s_n^2/2$.

Cards: [[STAT 132 Cards - DeGroot 8.6 Bayesian Normal Samples#Improper Prior for a Normal Mean and Precision]]
