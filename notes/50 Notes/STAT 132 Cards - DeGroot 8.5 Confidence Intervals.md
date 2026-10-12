---
type: reference
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "DeGroot 8.5 Confidence Intervals"
tags:
  - decks
---
# STAT 132 Cards - DeGroot 8.5 Confidence Intervals

## Confidence Interval
| Front | Back | Notes |
| --- | --- | --- |
| What must statistics $A \le B$ satisfy for $(A,B)$ to be a coefficient $\gamma$ confidence interval for $g(\theta)$? | $Pr(A < g(\theta) < B) \ge \gamma$ for all values of $\theta$. | p.501; definition |
| When is a confidence interval called "exact"? | When $Pr(A < g(\theta) < B) = \gamma$ exactly, for all $\theta$ (not just $\ge \gamma$). | p.501; definition |
| What is the "observed value" of a confidence interval $(A,B)$? | The interval $(a,b)$ obtained by plugging the observed data into the statistics $A$ and $B$. | p.501; definition |
| Confidence interval $(A,B)$ vs its observed value $(a,b)$: what is the key difference? | $(A,B)$ are random variables with a probability statement about their joint sampling distribution before data is observed; $(a,b)$ are fixed numbers computed after data is observed. | p.500-501; discrimination |

## Confidence Interval for the Mean of a Normal Distribution
| Front | Back | Notes |
| --- | --- | --- |
| Formula for a two-sided coefficient $\gamma$ CI for $\mu$, normal sample, $\sigma$ unknown? | $X_n \pm T_{n-1}^{-1}\left(\dfrac{1+\gamma}{2}\right)\dfrac{\hat\sigma}{\sqrt n}$ | p.501; formula |
| Which quantile of the $t_{n-1}$ distribution gives the multiplier $c$ for a two-sided $\gamma$ CI for $\mu$? | The $(1+\gamma)/2$ quantile of $T_{n-1}$. | p.500; formula |
| Why does this CI use the $t$ distribution instead of the standard normal? | Because $\sigma$ is unknown and estimated by $\hat\sigma$, so $\sqrt n (X_n-\mu)/\hat\sigma$ has the $t_{n-1}$ distribution, not the standard normal. | p.499-500; discrimination |

## Interpretation of Confidence Intervals
| Front | Back | Notes |
| --- | --- | --- |
| Before data is observed, what probability statement holds for a $\gamma$ CI $(A,B)$ for $\theta$? | $Pr(A<\theta<B)=\gamma$: a statement about the joint sampling distribution of the random variables $A$ and $B$, given fixed $\theta$. | p.505-506; definition |
| Yes or no, and why: after computing the observed interval $(a,b)$, can you say $Pr(\theta \in (a,b)) = \gamma$? | Not in general; $\theta$ is a fixed unknown, not random, so statisticians say there is "confidence $\gamma$" rather than "probability $\gamma$" that $\theta \in (a,b)$. | p.505-506; discrimination |
| What must you add to compute an actual probability that $\theta$ lies in the observed interval $(a,b)$? | Assign a prior distribution to $\theta$, then use the resulting posterior probability that $\theta \in (a,b)$. | p.506; procedure |

## One-Sided Confidence Intervals
| Front | Back | Notes |
| --- | --- | --- |
| Defining probability property of a one-sided $\gamma$ lower confidence limit $A$ for $g(\theta)$? | $Pr(A < g(\theta)) \ge \gamma$ for all $\theta$; the interval $(A,\infty)$ is the one-sided $\gamma$ CI. | p.503-504; definition |
| Formula for a one-sided $\gamma$ lower confidence limit for $\mu$ (normal, $\sigma$ unknown)? | $X_n - T_{n-1}^{-1}(\gamma)\dfrac{\hat\sigma}{\sqrt n}$ | p.504; formula |
| Two-sided $\gamma$ CI for $\mu$ uses the $(1+\gamma)/2$ quantile of $t_{n-1}$; which quantile does the one-sided $\gamma$ lower limit use? | The $\gamma$ quantile (not $(1+\gamma)/2$). | p.504; discrimination |

## Pivotal Quantity
| Front | Back | Notes |
| --- | --- | --- |
| Definition of a pivotal quantity $V(X,\theta)$? | A random variable, a function of the data and the parameter, whose probability distribution is the same for every value of $\theta$. | p.505; definition |
| Give an example of a pivotal quantity for a normal sample with unknown $\mu,\sigma$. | $U=\sqrt n (X_n-\mu)/\hat\sigma$, which has the $t_{n-1}$ distribution regardless of the values of $\mu$ and $\sigma$. | p.505; formula |

## Confidence Interval from a Pivotal
| Front | Back | Notes |
| --- | --- | --- |
| Given pivotal $V$ with continuous cdf $G$ and $r(V,X)=g(\theta)$ strictly increasing in $v$, formula for endpoints $A,B$ of a $\gamma$ CI ($\gamma_2-\gamma_1=\gamma$)? | $A=r(G^{-1}(\gamma_1),X)$, $B=r(G^{-1}(\gamma_2),X)$ | p.506; formula |
| If $r(v,x)$ is strictly decreasing in $v$ instead of increasing, what changes in the construction? | Swap the definitions of $A$ and $B$. | p.506; procedure |
| What two conditions must hold to invert a pivotal $V$ into a confidence interval for $g(\theta)$? | The cdf $G$ of $V$ must be continuous, and $r(v,x)$ must be strictly monotonic in $v$ with $r(V(X,\theta),X)=g(\theta)$. | p.505-506; definition |

## Confidence Intervals Can Ignore Extra Information
| Front | Back | Notes |
| --- | --- | --- |
| Yes or no, and why: does the confidence coefficient $\gamma$ of a CI change based on the specific observed sample values? | No; $\gamma$ is fixed by the construction and does not depend on the observed data, even if the data suggest more or less certainty. | p.509-510; concept |
| In the length-one uniform example, what happens to certainty that $\theta \in (y_1,y_2)$ as the observed range $y_2-y_1$ approaches $1/2$? | Certainty increases (approaches certainty that $\theta$ is inside), even though the stated confidence coefficient stays $1/2$. | p.509-510; concept |

## Rain from Seeded Clouds Confidence Interval
| Front | Back | Notes |
| --- | --- | --- |
| Rain from seeded clouds: $n=26$, $X_n=5.134$, $\hat\sigma=1.600$, want a 95% CI for $\mu$. Key move? | Look up $c=T_{25}^{-1}(0.975)=2.060$; margin $=c\hat\sigma/\sqrt{26}=0.646$; CI $=5.134\pm0.646=(4.488,5.780)$. | p.502; problem |

## Acid Concentration in Cheese Confidence Interval
| Front | Back | Notes |
| --- | --- | --- |
| Cheese acid: $n=10$, $X_n=1.379$, $\hat\sigma=0.3277$, want a 90% CI for $\mu$. Key move? | $c=T_9^{-1}(0.95)=1.833$; margin $=1.833(0.3277)/\sqrt{10}=0.190$; CI $=(1.189,1.569)$. | p.502-503; problem |

## Electronic Components Upper Confidence Limit
| Front | Back | Notes |
| --- | --- | --- |
| $\theta T \sim \text{Gamma}(3,1)$ is a pivotal for the failure rate $\theta$; want a 98% upper confidence limit $B$. Key move? | Find $G^{-1}(0.98)=7.516$ from the Gamma(3,1) cdf; the upper limit is $B=7.516/T$. | p.504-505; problem |

## Uniform Interval Length One Confidence Interval
| Front | Back | Notes |
| --- | --- | --- |
| Two uniforms on $(\theta-\tfrac12,\theta+\tfrac12)$, $Y_1=\min$, $Y_2=\max$. Key move to get the confidence coefficient of $(Y_1,Y_2)$, and when is $\theta \in (y_1,y_2)$ certain? | $Pr(Y_1<\theta<Y_2)=Pr(X_1<\theta<X_2)+Pr(X_2<\theta<X_1)=\tfrac12$; but if the observed $y_2-y_1>\tfrac12$, then $y_1<\theta<y_2$ with certainty. | p.507-509; problem |
# Node map
```json
[
 {
  "name": "Confidence Interval",
  "type": "concept",
  "existing": false,
  "parent": "Confidence Intervals",
  "prereqs": [
   "Estimators"
  ],
  "uses": [],
  "page": 501,
  "summary": "Statistics $A \\le B$ with $Pr(A<g(\\theta)<B)\\ge\\gamma$ for all $\\theta$; $(A,B)$ is a coefficient $\\gamma$ confidence interval for $g(\\theta)$, exact if equality holds."
 },
 {
  "name": "Confidence Interval for the Mean of a Normal Distribution",
  "type": "concept",
  "existing": false,
  "parent": "Confidence Intervals",
  "prereqs": [
   "Confidence Interval",
   "t Distribution",
   "Sample Mean"
  ],
  "uses": [],
  "page": 501,
  "summary": "For a normal sample with unknown $\\sigma$, $X_n \\pm T_{n-1}^{-1}((1+\\gamma)/2)\\hat\\sigma/\\sqrt n$ is an exact coefficient $\\gamma$ CI for $\\mu$."
 },
 {
  "name": "Interpretation of Confidence Intervals",
  "type": "concept",
  "existing": false,
  "parent": "Confidence Intervals",
  "prereqs": [
   "Confidence Interval"
  ],
  "uses": [],
  "page": 505,
  "summary": "The probability statement $Pr(A<\\theta<B)=\\gamma$ applies to the random interval before data is observed; once observed, one has 'confidence' not 'probability' that $\\theta \\in (a,b)$ unless a prior is assigned."
 },
 {
  "name": "One-Sided Confidence Intervals",
  "type": "concept",
  "existing": false,
  "parent": "Confidence Intervals",
  "prereqs": [
   "Confidence Interval",
   "t Distribution"
  ],
  "uses": [],
  "page": 503,
  "summary": "A one-sided coefficient $\\gamma$ CI has the form $(A,\\infty)$ or $(-\\infty,B)$; for a normal mean, $A = X_n - T_{n-1}^{-1}(\\gamma)\\hat\\sigma/\\sqrt n$."
 },
 {
  "name": "Pivotal Quantity",
  "type": "concept",
  "existing": false,
  "parent": "Confidence Intervals",
  "prereqs": [],
  "uses": [],
  "page": 505,
  "summary": "A pivotal is a random variable $V(X,\\theta)$ whose distribution is the same for every value of $\\theta$, used to construct confidence intervals."
 },
 {
  "name": "Confidence Interval from a Pivotal",
  "type": "concept",
  "existing": false,
  "parent": "Confidence Intervals",
  "prereqs": [
   "Pivotal Quantity",
   "Confidence Interval"
  ],
  "uses": [],
  "page": 505,
  "summary": "Given a pivotal $V$ with continuous cdf $G$ and invertible $r(v,x)$ with $r(V,X)=g(\\theta)$, the endpoints $A=r(G^{-1}(\\gamma_1),X)$, $B=r(G^{-1}(\\gamma_2),X)$ form a coefficient $\\gamma=\\gamma_2-\\gamma_1$ CI."
 },
 {
  "name": "Confidence Intervals Can Ignore Extra Information",
  "type": "concept",
  "existing": false,
  "parent": "Confidence Intervals",
  "prereqs": [
   "Confidence Interval"
  ],
  "uses": [],
  "page": 509,
  "summary": "The stated confidence coefficient $\\gamma$ is fixed by construction and does not adjust for extra information in the observed sample that might make a specific interval more or less likely to contain $\\theta$."
 },
 {
  "name": "Rain from Seeded Clouds Confidence Interval",
  "type": "problem",
  "existing": false,
  "parent": "Confidence Intervals",
  "prereqs": [],
  "uses": [
   "Confidence Interval for the Mean of a Normal Distribution",
   "t Distribution"
  ],
  "page": 502,
  "summary": "Computes a 95% CI for mean log-rainfall from $n=26$ seeded-cloud observations using the t-based normal-mean CI formula."
 },
 {
  "name": "Acid Concentration in Cheese Confidence Interval",
  "type": "problem",
  "existing": false,
  "parent": "Confidence Intervals",
  "prereqs": [],
  "uses": [
   "Confidence Interval for the Mean of a Normal Distribution",
   "t Distribution"
  ],
  "page": 502,
  "summary": "Computes a 90% CI for mean lactic acid concentration from $n=10$ cheese measurements using the t-based normal-mean CI formula."
 },
 {
  "name": "Electronic Components Upper Confidence Limit",
  "type": "problem",
  "existing": false,
  "parent": "Confidence Intervals",
  "prereqs": [],
  "uses": [
   "Pivotal Quantity",
   "Confidence Interval from a Pivotal",
   "Gamma Distribution"
  ],
  "page": 504,
  "summary": "Uses the pivotal $\\theta T \\sim \\text{Gamma}(3,1)$ to construct a 98% upper confidence limit for a component failure rate."
 },
 {
  "name": "Uniform Interval Length One Confidence Interval",
  "type": "problem",
  "existing": false,
  "parent": "Confidence Intervals",
  "prereqs": [],
  "uses": [
   "Confidence Interval",
   "Confidence Intervals Can Ignore Extra Information"
  ],
  "page": 507,
  "summary": "Shows $(Y_1,Y_2)$ from two uniforms on an interval of length 1 has confidence coefficient 1/2, yet a wide observed range can make containment of $\\theta$ certain."
 }
]
```

# Frankenstein problems

**Problem 1.** A random sample of $n=16$ measurements is drawn from a normal population. The sample mean is $X_n = 50.2$ and the sample standard deviation is $\hat\sigma = 4.0$.
(a) Find a two-sided 95% confidence interval for $\mu$.
(b) Find a 95% one-sided lower confidence limit for $\mu$.

*Concepts tested:* Confidence Interval for the Mean of a Normal Distribution, One-Sided Confidence Intervals, t Distribution, Sample Mean.

*Solution.*
(a) $c = T_{15}^{-1}(0.975) = 2.131$. Margin $= c\hat\sigma/\sqrt{16} = 2.131(4.0)/4 = 2.131$. CI $= 50.2 \pm 2.131 = (48.069, 52.331)$.
(b) $c = T_{15}^{-1}(0.95) = 1.753$. Margin $= 1.753(4.0)/4 = 1.753$. Lower limit $A = 50.2 - 1.753 = 48.447$, giving $(48.447,\infty)$.

**Problem 2.** Let $X_1,\dots,X_5$ be i.i.d. Exponential($\theta$) lifetimes (failure rate $\theta$), and let $T=\sum_{i=1}^5 X_i$. It is known that $\theta T \sim \text{Gamma}(5,1)$, and that $2\theta T$ then has the chi-square distribution with 10 degrees of freedom (since a sum of $k$ unit-rate exponentials doubled is $\chi^2_{2k}$). Suppose we observe $T = 6.0$. Find an exact 95% two-sided confidence interval for $\theta$, using $\chi^2_{10,0.025}=3.247$ and $\chi^2_{10,0.975}=20.483$.

*Concepts tested:* Pivotal Quantity, Confidence Interval from a Pivotal, Chi-Square Distribution, Confidence Interval.

*Solution.* $2\theta T$ is pivotal with $\chi^2_{10}$ distribution, so $Pr(3.247 < 2\theta T < 20.483) = 0.95$. Solving for $\theta$: $\theta \in \left(\dfrac{3.247}{2T}, \dfrac{20.483}{2T}\right)$. With $T=6.0$: $\theta \in (3.247/12,\ 20.483/12) = (0.271, 1.707)$.
