---
type: concept
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "Lec 1 Table 1; Reading 1 §1.6"
week: 1
prereqs:
  - "[[PMF, PDF and CDF]]"
  - "[[Expectation and Variance]]"
retention_band: cold
---
# Common distributions

| Dist | PMF / PDF | Mean | Var | Use |
|---|---|---|---|---|
| Bin$(n,p)$ | $\binom nx p^x(1-p)^{n-x}$ | $np$ | $np(1-p)$ | # successes in $n$ indep. trials |
| Poisson$(\lambda)$ | $\lambda^x e^{-\lambda}/x!$ | $\lambda$ | $\lambda$ | counts per interval |
| $N(\mu,\sigma^2)$ | $\frac{1}{\sqrt{2\pi\sigma^2}}e^{-(x-\mu)^2/2\sigma^2}$ | $\mu$ | $\sigma^2$ | symmetric measurement error |
| Exp$(\lambda)$ | $\lambda e^{-\lambda x}$ | $1/\lambda$ | $1/\lambda^2$ | waiting time |
| Gamma$(\alpha,\beta)$ | $\frac{\beta^\alpha}{\Gamma(\alpha)}x^{\alpha-1}e^{-\beta x}$ | $\alpha/\beta$ | $\alpha/\beta^2$ | positive, right-skewed; Exp is $\alpha=1$ |
| Beta$(\alpha,\beta)$ | $\frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha,\beta)}$ | $\frac{\alpha}{\alpha+\beta}$ | $\frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}$ | proportions on $(0,1)$ |
| $U(a,b)$ | $1/(b-a)$ | $(a+b)/2$ | $(b-a)^2/12$ | no preferred value in the window |

⚠ Gamma here is the **rate** form ($\beta$ = rate). Check which form DS and the homework use.
Poisson has Var = mean. If count data have a much bigger variance, Poisson is the wrong model.
See [[Gamma and Beta Functions]].
