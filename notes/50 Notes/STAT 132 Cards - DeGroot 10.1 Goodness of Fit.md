---
type: reference
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "DeGroot 10.1 Goodness of Fit"
tags:
  - decks
---
# STAT 132 Cards - DeGroot 10.1 Goodness of Fit

## Nonparametric Problem
| Front | Back | Notes |
| --- | --- | --- |
| What distinguishes a nonparametric problem from a parametric one? | The data's distribution is not assumed to come from a specific parametric family; inferences are made without specifying the distribution's exact form. | p.639; definition |

## Chi-Square Goodness-of-Fit Statistic
| Front | Back | Notes |
| --- | --- | --- |
| Define the chi-square goodness-of-fit statistic $Q$ for $k$ categories with hypothesized probabilities $p_i^0$. | $Q=\displaystyle\sum_{i=1}^k \frac{(N_i-np_i^0)^2}{np_i^0}$, where $N_i$ is the observed count and $n$ the sample size. | p.641; formula |
| As $n\to\infty$ under $H_0$, what is the limiting distribution of $Q$ for $k$ categories? | The $\chi^2$ distribution with $k-1$ degrees of freedom. | p.641; formula |
| What general form do all chi-square test statistics in this chapter share? | $\sum(\text{observed}-\text{expected})^2/\text{expected}$, with expected counts computed assuming $H_0$ is true. | p.641; discrimination |
| What rule of thumb ensures the $\chi^2$ approximation for $Q$ is good? | Each expected count $np_i^0$ should be at least 5 (satisfactory if at least 1.5). | p.642; procedure |

## Chi-Square Test of Goodness-of-Fit
| Front | Back | Notes |
| --- | --- | --- |
| At level $\alpha_0$, when does the $\chi^2$ goodness-of-fit test reject $H_0$? | When $Q\ge c$, where $c$ is the $1-\alpha_0$ quantile of the $\chi^2_{k-1}$ distribution. | p.641; procedure |
| Give the p-value formula for the $\chi^2$ goodness-of-fit test, in terms of the $\chi^2_{k-1}$ c.d.f. $X^2_{k-1}$. | $1-X^2_{k-1}(Q)$. | p.642; formula |

## Continuous Distribution Goodness-of-Fit
| Front | Back | Notes |
| --- | --- | --- |
| How do you adapt the $\chi^2$ goodness-of-fit test to a hypothesized continuous distribution? | Partition the line into $k$ disjoint intervals, compute each interval's hypothesized probability $p_i^0$, count observations $N_i$ falling in each interval, then apply the usual $Q$ statistic with $k-1$ df. | p.643; procedure |
| When choosing subintervals for a continuous goodness-of-fit test, what is the general policy? | Make the expected counts roughly equal across intervals, and use as many intervals as possible without letting any expected count get too small. | p.645; discrimination |

## Likelihood Ratio Test for Multinomial Proportions
| Front | Back | Notes |
| --- | --- | --- |
| For testing $H_0:p=p^{(0)}$ in a multinomial model, give the large-sample likelihood ratio test statistic. | $-2\log\Lambda(x)=-2\displaystyle\sum_{i=1}^k N_i\log\!\left(\frac{np_i^{(0)}}{N_i}\right)$. | p.645; formula |
| What is the large-sample rejection rule for this likelihood ratio test at level $\alpha_0$? | Reject $H_0$ if $-2\log\Lambda(x)$ exceeds the $1-\alpha_0$ quantile of the $\chi^2_{k-1}$ distribution. | p.645; procedure |

## Composite Null Hypothesis Goodness-of-Fit
| Front | Back | Notes |
| --- | --- | --- |
| In a composite goodness-of-fit hypothesis, how are the category probabilities $p_i$ restricted? | Each $p_i$ must equal a function $\pi_i(\theta)$ of a lower-dimensional parameter vector $\theta$ of length $s<k-1$. | p.649; definition |

## Chi-Square Test for Composite Null
| Front | Back | Notes |
| --- | --- | --- |
| Give the modified $\chi^2$ statistic $Q$ for a composite null hypothesis, using the MLE $\hat\theta$. | $Q=\displaystyle\sum_{i=1}^k \frac{[N_i-n\pi_i(\hat\theta)]^2}{n\pi_i(\hat\theta)}$. | p.649; formula |
| As $n\to\infty$ under this composite $H_0$, what is the limiting distribution of $Q$? | The $\chi^2$ distribution with $k-1-s$ degrees of freedom, where $s$ is the number of estimated parameters. | p.649; formula |
| Why does estimating parameters reduce the degrees of freedom compared to the simple-hypothesis case? | Each estimated parameter uses up one degree of freedom, since the expected counts are no longer fully specified by $H_0$ alone. | p.649; discrimination |

## Blood Types Chi-Square Test
| Front | Back | Notes |
| --- | --- | --- |
| Blood type counts $(2162,738,228,2876)$ vs. expected $(2001.3,750.5,250.2,3002.0)$, $n=6004$, $k=4$. Compute $Q$ and its p-value using $\chi^2_3$. | $Q=20.37$; p-value $=1-X_3^2(20.37)=1.42\times10^{-4}$. | p.642; procedure |

## Montana Outlook Poll
| Front | Back | Notes |
| --- | --- | --- |
| A survey of 189 people splits 58/64/67 across three responses; test $H_0:$ each probability is $1/3$. Compute $Q$ and state the decision at $\alpha_0=0.05$. | $Q=0.6667$, only the 0.283 quantile of $\chi^2_2$; do not reject $H_0$ (would only reject at levels $>0.717$). | p.642; procedure |

## Testing a Proportion via Chi-Square
| Front | Back | Notes |
| --- | --- | --- |
| Testing $H_0:p=0.1$ with $n=100$ and 16 observed defectives. Compute $Q$ and its p-value using $\chi^2_1$. | $Q=4$; p-value $\approx0.0455$. | p.643; procedure |

## Ball Bearings Normal Fit
| Front | Back | Notes |
| --- | --- | --- |
| Testing whether 23 log-lifetimes fit $N(3.912,0.25)$ using 4 equal-probability intervals with observed counts $(3,4,8,8)$. Compute $Q$ and its p-value. | $Q=3.609$ on 3 df; p-value $=0.307$. | p.644; procedure |

## Blood Types Likelihood Ratio Test
| Front | Back | Notes |
| --- | --- | --- |
| For the blood type data, the large-sample LRT gives $-2\log\Lambda(x)=20.16$ on 3 df. How does this compare to the chi-square test's p-value from the same data? | Nearly identical: LRT p-value $=1.57\times10^{-4}$ vs. chi-square p-value $=1.42\times10^{-4}$. | p.646; discrimination |
# Node map
```json
[
 {
  "name": "Nonparametric Problem",
  "type": "concept",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [],
  "uses": [],
  "page": 639,
  "summary": "A problem where the observations' distribution is not restricted to a specific parametric family."
 },
 {
  "name": "Chi-Square Goodness-of-Fit Statistic",
  "type": "concept",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [
   "Chi-Square Distribution"
  ],
  "uses": [],
  "page": 641,
  "summary": "$Q=\\sum(N_i-np_i^0)^2/np_i^0$ converges to $\\chi^2_{k-1}$ under $H_0$; expected counts should be at least 5."
 },
 {
  "name": "Chi-Square Test of Goodness-of-Fit",
  "type": "concept",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [
   "Chi-Square Goodness-of-Fit Statistic"
  ],
  "uses": [],
  "page": 641,
  "summary": "Rejects $H_0:p_i=p_i^0$ when $Q$ exceeds a $\\chi^2_{k-1}$ quantile; p-value is $1-X^2_{k-1}(Q)$."
 },
 {
  "name": "Continuous Distribution Goodness-of-Fit",
  "type": "concept",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [
   "Chi-Square Test of Goodness-of-Fit"
  ],
  "uses": [],
  "page": 643,
  "summary": "Bins a hypothesized continuous distribution into intervals so the chi-square test can be applied to interval counts."
 },
 {
  "name": "Likelihood Ratio Test for Multinomial Proportions",
  "type": "concept",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [
   "Likelihood Function",
   "Chi-Square Test of Goodness-of-Fit"
  ],
  "uses": [],
  "page": 645,
  "summary": "Large-sample LRT of $H_0:p=p^{(0)}$ using $-2\\log\\Lambda=-2\\sum N_i\\log(np_i^{(0)}/N_i)$, compared to $\\chi^2_{k-1}$."
 },
 {
  "name": "Composite Null Hypothesis Goodness-of-Fit",
  "type": "concept",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [
   "Chi-Square Test of Goodness-of-Fit"
  ],
  "uses": [],
  "page": 649,
  "summary": "Tests whether $p_1,\\dots,p_k$ can be written as functions $\\pi_i(\\theta)$ of a smaller parameter vector $\\theta$."
 },
 {
  "name": "Chi-Square Test for Composite Null",
  "type": "concept",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [
   "Composite Null Hypothesis Goodness-of-Fit"
  ],
  "uses": [],
  "page": 649,
  "summary": "$Q=\\sum[N_i-n\\pi_i(\\hat\\theta)]^2/n\\pi_i(\\hat\\theta)$ converges to $\\chi^2_{k-1-s}$, losing one df per estimated parameter."
 },
 {
  "name": "Blood Types Chi-Square Test",
  "type": "problem",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [],
  "uses": [
   "Chi-Square Goodness-of-Fit Statistic",
   "Chi-Square Test of Goodness-of-Fit"
  ],
  "page": 642,
  "summary": "Testing whether observed blood-type counts match hypothesized probabilities."
 },
 {
  "name": "Montana Outlook Poll",
  "type": "problem",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [],
  "uses": [
   "Chi-Square Goodness-of-Fit Statistic",
   "Chi-Square Test of Goodness-of-Fit"
  ],
  "page": 642,
  "summary": "Testing whether survey responses are uniformly distributed across three categories."
 },
 {
  "name": "Testing a Proportion via Chi-Square",
  "type": "problem",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [],
  "uses": [
   "Chi-Square Goodness-of-Fit Statistic",
   "Chi-Square Test of Goodness-of-Fit"
  ],
  "page": 643,
  "summary": "Using the two-category chi-square test as an alternative to the one-proportion z test."
 },
 {
  "name": "Ball Bearings Normal Fit",
  "type": "problem",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [],
  "uses": [
   "Continuous Distribution Goodness-of-Fit"
  ],
  "page": 644,
  "summary": "Binning log-lifetime data into four equal-probability intervals to test normality."
 },
 {
  "name": "Blood Types Likelihood Ratio Test",
  "type": "problem",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [],
  "uses": [
   "Likelihood Ratio Test for Multinomial Proportions"
  ],
  "page": 646,
  "summary": "Comparing the LRT statistic to the chi-square statistic on the same blood-type data."
 }
]
```

# Frankenstein problems

**Problem 1**
A die is rolled $n=120$ times to test whether it is fair ($H_0:p_i=1/6$ for $i=1,\dots,6$). Observed counts: $25,15,20,18,24,18$.

a. Compute the expected count under $H_0$ for each face.
b. Compute $Q$.
c. At $\alpha_0=0.05$, with $\chi_5^{2,-1}(0.95)=11.07$, state the decision.
d. Which type of error is possible given this decision?

**Solution**

a. Expected count $=120/6=20$ for each face.

b. $Q=\dfrac{(25-20)^2}{20}+\dfrac{(15-20)^2}{20}+\dfrac{(20-20)^2}{20}+\dfrac{(18-20)^2}{20}+\dfrac{(24-20)^2}{20}+\dfrac{(18-20)^2}{20}$
$=\dfrac{25+25+0+4+16+4}{20}=\dfrac{74}{20}=3.7$.

c. Since $3.7<11.07$, do not reject $H_0$.

d. Since $H_0$ was not rejected, the possible error is a Type II error (failing to reject a false $H_0$).

Concepts used: Chi-Square Goodness-of-Fit Statistic, Chi-Square Test of Goodness-of-Fit, p-value, Type I and Type II Error.

**Problem 2**
In a genetics study with two alleles, the three genotype probabilities are $p_1=\theta^2$, $p_2=2\theta(1-\theta)$, $p_3=(1-\theta)^2$. A sample of $n=200$ gives counts $N_1=50$, $N_2=100$, $N_3=50$. The MLE for this model is $\hat\theta=(2N_1+N_2)/(2n)$.

a. Find $\hat\theta$.
b. Compute the expected counts $n\pi_i(\hat\theta)$.
c. Compute $Q$.
d. How many degrees of freedom does $Q$ have here, and why?

**Solution**

a. $\hat\theta=\dfrac{2(50)+100}{2(200)}=\dfrac{200}{400}=0.5$.

b. $\pi_1=\hat\theta^2=0.25$, $\pi_2=2\hat\theta(1-\hat\theta)=0.5$, $\pi_3=(1-\hat\theta)^2=0.25$.
Expected counts: $200(0.25)=50$, $200(0.5)=100$, $200(0.25)=50$.

c. $Q=\dfrac{(50-50)^2}{50}+\dfrac{(100-100)^2}{100}+\dfrac{(50-50)^2}{50}=0$.

d. $k-1-s=3-1-1=1$ degree of freedom, since one parameter ($\theta$) was estimated from the data.

Concepts used: Composite Null Hypothesis Goodness-of-Fit, Chi-Square Test for Composite Null, Chi-Square Goodness-of-Fit Statistic, Likelihood Function.
