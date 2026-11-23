---
type: reference
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "DeGroot 9.8 Bayes Test Procedures"
tags:
  - decks
---
# STAT 132 Cards - DeGroot 9.8 Bayes Test Procedures

## Bayes Test Procedure
| Front | Back | Notes |
| --- | --- | --- |
| With prior probabilities $\xi_0,\xi_1$ and error losses $w_0,w_1$, define the expected loss $r(\delta)$ of a test $\delta$. | $r(\delta)=\xi_0 w_0\alpha(\delta)+\xi_1 w_1\beta(\delta)$, where $\alpha(\delta)$ and $\beta(\delta)$ are the Type I and Type II error probabilities. | p.621; formula |
| What is a Bayes test procedure? | A test $\delta$ that minimizes the expected loss $r(\delta)=\xi_0w_0\alpha(\delta)+\xi_1w_1\beta(\delta)$. | p.621; definition |
| For simple hypotheses $H_0:\theta=\theta_0$ vs $H_1:\theta=\theta_1$, when does the Bayes test reject $H_0$? | When $\xi_0 w_0 f_0(x) < \xi_1 w_1 f_1(x)$. | p.621; procedure |
| Why does the Bayes test depend only on the ratio $w_1/w_0$, not on $w_0,w_1$ individually? | Minimizing $r(\delta)$ is unaffected by rescaling both losses by the same positive constant. | p.621; discrimination |

## Bayes Test via Posterior Probability
| Front | Back | Notes |
| --- | --- | --- |
| With loss $w_0$ for a Type I error and $w_1$ for a Type II error, when does the Bayes test reject $H_0$ based on the posterior? | When $\Pr(H_0\text{ true}\mid x)\le \dfrac{w_1}{w_0+w_1}$. | p.623; formula |
| What is the posterior expected loss of not rejecting $H_0$ (decision $d_0$)? | $r(d_0\mid x)=w_1[1-\Pr(H_0\text{ true}\mid x)]$. | p.622; formula |
| What is the posterior expected loss of rejecting $H_0$ (decision $d_1$)? | $r(d_1\mid x)=w_0\Pr(H_0\text{ true}\mid x)$. | p.622; formula |

## Bayes One-Sided Test
| Front | Back | Notes |
| --- | --- | --- |
| If $f_n(x\mid\theta)$ has a monotone likelihood ratio in $T=r(X)$, $H_0:\theta\le\theta_0$, and losses $w_0,w_1$ are constants, what form does the Bayes test take? | Reject $H_0$ when $T\ge c$ for some constant $c$, the same form as the classical one-sided test. | p.623; procedure |

## Bayes Tests as t Tests
| Front | Back | Notes |
| --- | --- | --- |
| For a normal mean with unknown variance and an improper prior, how does the Bayes test of $H_0:\mu\le\mu_0$ relate to the classical t test? | It is identical to the level $\alpha_0$ one-sided t test, with $\alpha_0=w_1/(w_0+w_1)$. | p.626; discrimination |
| Under this equivalence, how do the p-value and the posterior probability of $H_0$ relate? | They are numerically equal. | p.626; discrimination |
| For comparing two normal means with common variance and improper priors, what does the Bayes procedure for $H_0:\mu_1\le\mu_2$ reduce to? | The level $\alpha_0$ two-sample t test from Sec. 9.6, with $\alpha_0=w_1/(w_0+w_1)$. | p.628; discrimination |

## Two-Sample Bayes Test
| Front | Back | Notes |
| --- | --- | --- |
| With improper priors $\xi(\mu_1,\mu_2,\tau)=1/\tau$, what is the posterior distribution of $(m+n-2)^{1/2}\dfrac{\mu_1-\mu_2-(\bar x_m-\bar y_n)}{\left(\frac1m+\frac1n\right)^{1/2}(s_x^2+s_y^2)^{1/2}}$? | The $t$ distribution with $m+n-2$ degrees of freedom. | p.627; formula |

## Two-Sided Bayes Testing (Posterior Interval Plot)
| Front | Back | Notes |
| --- | --- | --- |
| Why does testing $H_0:\theta=\theta_0$ against a two-sided alternative fail under a continuous posterior? | The posterior probability that $\theta$ equals any single point is 0, so $H_0$ would always be rejected regardless of the data. | p.625; discrimination |
| What is the practical Bayesian alternative to testing a sharp null $\theta=\theta_0$? | Test $H_0:\vert \theta-\theta_0\vert \le d$ for a chosen meaningful difference $d$, or plot $\Pr(\vert \theta-\theta_0\vert \le d\mid x)$ against $d$. | p.625; procedure |

## Bayes Test for Variance Ratio
| Front | Back | Notes |
| --- | --- | --- |
| With improper priors, what is the posterior distribution of $\dfrac{s_x^2/[(m-1)\sigma_1^2]}{s_y^2/[(n-1)\sigma_2^2]}$? | The $F$ distribution with $m-1$ and $n-1$ degrees of freedom, the same as its sampling distribution. | p.629; formula |

## Service Times Simple Bayes Test
| Front | Back | Notes |
| --- | --- | --- |
| Two service-time models with $\xi_0=\xi_1=1/2$ and cost ratio $w_1/w_0=1$: what is the Bayes decision rule? | Reject $H_0$ (choose $f_1$) if $f_1(x)/f_0(x)>1$. | p.622; procedure |

## Calorie Counts One-Sided Bayes Test
| Front | Back | Notes |
| --- | --- | --- |
| Calorie differences have posterior $\theta\sim N(0.923\bar X_{20}, 4.62)$. Testing $H_0:\theta\le0$ vs $H_1:\theta>0$, give $\Pr(\theta\le0\mid x)$ in terms of $\Phi$. | $\Phi(-0.429\bar X_{20})$. | p.624; procedure |

## Pesticide Residue Bayes t Test
| Front | Back | Notes |
| --- | --- | --- |
| Celery pesticide data: $n=77$, $\bar x=50.23$, $s_n^2=34106$; testing $H_0:\mu\ge55$ vs $H_1:\mu<55$ with an improper prior, $u=\sqrt{77}(55-50.23)/\sqrt{34106/76}\approx1.974$. Give the posterior probability that $H_0$ is true. | $\Pr(\mu\ge55\mid x)=1-T_{76}(1.974)=0.026$. | p.627; procedure |

## Roman Pottery Two-Sided Posterior Interval
| Front | Back | Notes |
| --- | --- | --- |
| Roman pottery: the posterior of $\mu_1-\mu_2$ satisfies $1.33(\mu_1-\mu_2+4.76)\sim t_{17}$. Give $\Pr(\vert \mu_1-\mu_2\vert \le d\mid x)$ in terms of $T_{17}$. | $T_{17}(1.33(d+4.76))-T_{17}(1.33(-d+4.76))$. | p.629; formula |
# Node map
```json
[
 {
  "name": "Bayes Test Procedure",
  "type": "concept",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [
   "Prior Distribution",
   "Posterior Distribution"
  ],
  "uses": [],
  "page": 621,
  "summary": "Minimizes expected loss $r(\\delta)=\\xi_0w_0\\alpha(\\delta)+\\xi_1w_1\\beta(\\delta)$ over test procedures; depends only on the ratio $w_1/w_0$."
 },
 {
  "name": "Bayes Test via Posterior Probability",
  "type": "concept",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [
   "Bayes Test Procedure"
  ],
  "uses": [],
  "page": 623,
  "summary": "Rejects $H_0$ when its posterior probability is at most $w_1/(w_0+w_1)$."
 },
 {
  "name": "Bayes One-Sided Test",
  "type": "concept",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [
   "Bayes Test via Posterior Probability"
  ],
  "uses": [],
  "page": 623,
  "summary": "Under a monotone likelihood ratio family, the Bayes test of a one-sided hypothesis has the classical form: reject when $T\\ge c$."
 },
 {
  "name": "Bayes Tests as t Tests",
  "type": "concept",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [
   "Bayes One-Sided Test",
   "t-statistic"
  ],
  "uses": [],
  "page": 626,
  "summary": "With improper priors, Bayes tests of one-sided normal-mean hypotheses coincide exactly with the classical (one- and two-sample) t tests, and the p-value equals the posterior probability of $H_0$."
 },
 {
  "name": "Two-Sample Bayes Test",
  "type": "concept",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [
   "Bayes Test via Posterior Probability",
   "Two-Sample t Statistic"
  ],
  "uses": [],
  "page": 627,
  "summary": "With improper priors, the posterior of a standardized $\\mu_1-\\mu_2$ is exactly $t_{m+n-2}$."
 },
 {
  "name": "Two-Sided Bayes Testing (Posterior Interval Plot)",
  "type": "concept",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [
   "Bayes Test via Posterior Probability"
  ],
  "uses": [],
  "page": 625,
  "summary": "A sharp null has posterior probability 0 under a continuous posterior, so two-sided Bayes testing instead examines $\\Pr(|\\theta-\\theta_0|\\le d\\mid x)$ across $d$."
 },
 {
  "name": "Bayes Test for Variance Ratio",
  "type": "concept",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [
   "Bayes Test via Posterior Probability"
  ],
  "uses": [],
  "page": 629,
  "summary": "With improper priors, the posterior of the variance-ratio pivot is the same $F_{m-1,n-1}$ distribution as its sampling distribution."
 },
 {
  "name": "Service Times Simple Bayes Test",
  "type": "problem",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [],
  "uses": [
   "Bayes Test Procedure"
  ],
  "page": 622,
  "summary": "Choosing between two service-time models by comparing weighted likelihoods."
 },
 {
  "name": "Calorie Counts One-Sided Bayes Test",
  "type": "problem",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [],
  "uses": [
   "Bayes Test via Posterior Probability",
   "Bayes One-Sided Test"
  ],
  "page": 624,
  "summary": "Computing the posterior probability of a one-sided null for a normal mean with a normal prior."
 },
 {
  "name": "Pesticide Residue Bayes t Test",
  "type": "problem",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [],
  "uses": [
   "Bayes Tests as t Tests"
  ],
  "page": 627,
  "summary": "Applying the improper-prior Bayes t test equivalence to celery pesticide residue data."
 },
 {
  "name": "Roman Pottery Two-Sided Posterior Interval",
  "type": "problem",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [],
  "uses": [
   "Two-Sample Bayes Test",
   "Two-Sided Bayes Testing (Posterior Interval Plot)"
  ],
  "page": 629,
  "summary": "Plotting the posterior probability that two pottery-site means are within $d$ of each other."
 }
]
```

# Frankenstein problems

**Problem 1**
A researcher tests $H_0:\mu\le100$ vs $H_1:\mu>100$ for a normal population with unknown variance, using an improper prior. With $n=25$ (24 df), the observed t-statistic is $u=2.1$, and losses are $w_0=3$, $w_1=1$ (a Type I error is judged 3 times as costly as a Type II error).

a. What value of $\alpha_0$ does this loss ratio correspond to?
b. Write the classical one-sided p-value in terms of $T_{24}$.
c. Given $T_{24}(2.1)=0.977$, does the Bayes test reject $H_0$?
d. What is $\Pr(H_0\text{ true}\mid x)$ in this case?

**Solution**

a. $\alpha_0=w_1/(w_0+w_1)=1/(3+1)=0.25$.

b. p-value $=1-T_{24}(u)=1-T_{24}(2.1)$.

c. p-value $=1-0.977=0.023$, which is less than $\alpha_0=0.25$, so the Bayes test rejects $H_0$.

d. Since the Bayes test with an improper prior coincides with the t test, $\Pr(H_0\text{ true}\mid x)$ equals the p-value: $0.023$.

Concepts used: Bayes Test Procedure, Bayes Test via Posterior Probability, Bayes Tests as t Tests, p-values for t Tests.

**Problem 2**
Two production lines are compared with improper priors: $m=10$, $n=12$, $\bar x_m=52$, $\bar y_n=49$, $s_x^2=40$, $s_y^2=55$. Test $H_0:\mu_1\le\mu_2$ vs $H_1:\mu_1>\mu_2$ using losses $w_0=4$, $w_1=1$.

a. Compute the two-sample t statistic $U$.
b. What value of $\alpha_0$ corresponds to these losses?
c. Given $T_{20}^{-1}(0.8)\approx0.860$, does the Bayes test reject $H_0$?
d. What is the posterior probability $\Pr(\mu_1\le\mu_2\mid x,y)$ in terms of $T_{20}$ and $U$?

**Solution**

a. $m+n-2=20$, $\sqrt{20}=4.472$. $\bar x_m-\bar y_n=3$, numerator $=4.472\times3=13.416$.
$\frac1{10}+\frac1{12}=\frac{11}{60}=0.1833$, $\sqrt{0.1833}=0.4282$.
$s_x^2+s_y^2=95$, $\sqrt{95}=9.747$.
Denominator $=0.4282\times9.747=4.174$.
$U=13.416/4.174\approx3.214$.

b. $\alpha_0=w_1/(w_0+w_1)=1/5=0.2$.

c. Since $U=3.214>T_{20}^{-1}(0.8)=0.860$, the Bayes test rejects $H_0$ (equivalently, the posterior probability of $H_0$ is at most $\alpha_0$).

d. $\Pr(\mu_1\le\mu_2\mid x,y)=T_{20}(-U)=T_{20}(-3.214)$.

Concepts used: Two-Sample t Statistic, Two-Sample Bayes Test, Bayes Tests as t Tests, Bayes Test via Posterior Probability.
