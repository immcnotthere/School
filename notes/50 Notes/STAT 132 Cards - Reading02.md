---
type: reference
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "Reading02"
tags:
  - decks
---
# STAT 132 Cards - Reading02 Frequentist and Bayesian Inference

## Population
| Front | Back | Notes |
| --- | --- | --- |
| Why must a population be defined carefully, e.g. "college students"? | A vague population (which students, currently enrolled vs. ever enrolled) makes it unclear what the data represent; conclusions only apply to the population the data can reasonably represent. | p.1; definition |

## Selection bias
| Front | Back | Notes |
| --- | --- | --- |
| Define selection bias. | Some members of a population are more likely to be included in a sample than others, in a way related to the measurement of interest. | p.2; definition |
| A study estimates time spent on campus by surveying only students leaving the library at 11 p.m. What kind of error results? | Selection bias: late-library students likely spend more time on campus than typical students, so the sample overrepresents high-campus-time students. | p.2; procedure |

## Random Sampling
| Front | Back | Notes |
| --- | --- | --- |
| How does random sampling address selection bias? | It gives every population member a known mechanism (probability) of being selected, rather than letting inclusion depend on the trait being measured. | p.2; definition |
| What does random sampling make possible for describing sample-to-sample variation, even though it doesn't guarantee any one sample matches the population? | It allows probability theory to describe how much samples should vary. | p.2; definition |

## Visualizing a Sample
| Front | Back | Notes |
| --- | --- | --- |
| Why should you graph a sample before fitting a model or calculating an estimate? | A graph can reveal features, such as skew or outliers, that are hidden by a single numerical summary. | p.2; definition |
| In a right-skewed sample of wait times, is the sample mean larger or smaller than the sample median, and why? | Larger; a few unusually long waits pull the mean to the right, while the median (a typical customer's position in the ordered data) is less affected. | p.3; discrimination |

## Population parameter
| Front | Back | Notes |
| --- | --- | --- |
| Are the values of population parameters typically known or unknown, given that the parameters themselves are fixed features of the population? | Unknown; parameters are fixed features of the population whose values we do not know. | p.4; definition |

## Quantity of Interest
| Front | Back | Notes |
| --- | --- | --- |
| Must a quantity of interest be one of a model's named parameters? Give an example that is not. | No; under a normal model with parameters $\mu,\sigma^2$, the proportion of values above 60 minutes is a quantity of interest calculable from $\mu,\sigma^2$ but is not one of the model's two named parameters. | p.4; procedure |

## Likelihood Function
| Front | Back | Notes |
| --- | --- | --- |
| Why is it wrong to interpret the height $L(\theta)$ as the probability that $\theta$ is the true parameter? | A likelihood generally does not integrate or sum to 1 over the parameter space, so it is not a probability distribution for $\theta$; only the ratio $L(\theta_1)/L(\theta_2)$, the relative support, is meaningful. | p.11; definition |

## Log-Likelihood
| Front | Back | Notes |
| --- | --- | --- |
| Write the log-likelihood $\ell(\theta)$. | $\ell(\theta) = \log L(\theta) = \sum_{i=1}^n \log f(x_i \mid \theta)$ | p.11; formula |
| Why do statisticians use the log-likelihood instead of the raw likelihood for computation? | Likelihoods multiply many probabilities and can become extremely small; the logarithm turns the product into a sum, which is easier for a computer to handle. | p.12; definition |

## Prior Distribution
| Front | Back | Notes |
| --- | --- | --- |
| Name two acceptable sources of prior information. | Any two of: results from earlier studies, historical data collected under similar conditions, established scientific knowledge, or the judgment of subject-matter experts. | p.12; procedure |
| Beta(30,20) and Beta(6,4) are both centered near 0.60. Which represents greater prior confidence that $p$ is near 0.60, and why? | Beta(30,20); it is more concentrated (narrower), representing greater confidence. | p.14; discrimination |

## Conjugate Prior
| Front | Back | Notes |
| --- | --- | --- |
| Match each sampling model to its conjugate prior and posterior family: Bernoulli, Poisson, Normal (known $\sigma^2$). | Bernoulli: Beta/Beta. Poisson: Gamma/Gamma. Normal (known $\sigma^2$): Normal/Normal. | p.22; formula |

## Normal-Normal Update
| Front | Back | Notes |
| --- | --- | --- |
| If $X_i \mid \mu \sim N(\mu,\sigma^2)$ (known $\sigma^2$) and $\mu \sim N(\mu_0,\sigma_0^2)$, what family is the posterior, and what is the posterior-precision identity? | Normal; posterior precision equals prior precision plus data precision, $1/\sigma_1^2 = 1/\sigma_0^2 + n/\sigma^2$, where precision is $1/\text{variance}$. | p.29; formula |
| Write the posterior mean $\mu_1$ as a precision-weighted average. | $\mu_1 = \dfrac{(1/\sigma_0^2)\mu_0 + (n/\sigma^2)\bar x}{1/\sigma_0^2 + n/\sigma^2}$ | p.29; formula |
| In Normal-Normal updating, a highly concentrated prior pulls $\mu_1$ toward which value, and a large low-variance sample pulls it toward which value? | A concentrated prior pulls $\mu_1$ toward $\mu_0$; a large or low-variance sample pulls it toward $\bar x$: the source with greater precision receives more weight. | p.29; discrimination |

## Prior Influence and Sample Size
| Front | Back | Notes |
| --- | --- | --- |
| Name the three factors that determine how strongly the posterior mean is pulled toward the prior mean versus the sample mean. | Prior location (where it is centered), prior variance (more concentrated means more influence), and sample size (larger $n$ increases data precision). | p.31; definition |
| Why can a large dataset still give a misleading answer, even though more data reduce posterior uncertainty about a parameter? | More data do not correct sampling bias, lack of independence, or a poor probability model; a large dataset can give a very precise answer to the wrong question. | p.34; definition |

## On-Time Bus Arrivals
| Front | Back | Notes |
| --- | --- | --- |
| A bus arrives within 5 minutes on 12 of 20 mornings. Write the likelihood $L(p)$ for the probability $p$ of an on-time arrival, and give the value of $p$ that maximizes it. | $L(p) \propto p^{12}(1-p)^8$ for $0 \le p \le 1$; maximized at $p = 12/20 = 0.60$, the sample proportion. | p.9-10; procedure |

## Reusable Container Participation
| Front | Back | Notes |
| --- | --- | --- |
| Prior $p \sim \mathrm{Beta}(5,5)$; in a sample of 30 customers, 21 say they would participate. Find the posterior distribution and posterior mean. | $p \mid \mathbf{x} \sim \mathrm{Beta}(5+21,\ 5+9) = \mathrm{Beta}(26,14)$; posterior mean $=26/40=0.65$. | p.23-24; procedure |

## Evening Bicycle Repairs
| Front | Back | Notes |
| --- | --- | --- |
| Prior $\lambda \sim \mathrm{Gamma}(8,2)$; five evenings give counts 3, 6, 4, 7, 5 (total 25). Find the posterior distribution and posterior mean. | $\lambda \mid \mathbf{x} \sim \mathrm{Gamma}(8+25,\ 2+5) = \mathrm{Gamma}(33,7)$; posterior mean $=33/7\approx4.71$. | p.27; procedure |

## Device Charging Time
| Front | Back | Notes |
| --- | --- | --- |
| Prior $\mu \sim N(52, 6^2)$; known data sd $=8$; a sample of 16 devices has mean 48. Find the posterior mean and sd. | Prior precision $=1/36$, data precision $=16/64=0.25$; posterior mean $=\dfrac{(1/36)(52)+0.25(48)}{1/36+0.25}=48.4$, posterior variance $=1/(1/36+0.25)=3.6$, so posterior sd $\approx1.897$. | p.30; procedure |

## Interpretation of Confidence Intervals
| Front | Back | Notes |
| --- | --- | --- |
| State the correct frequentist interpretation of a 95% confidence interval. | If we repeatedly sampled the same way and built an interval from each sample using this method, about 95% of those intervals would contain the true population mean. | p.5; definition |

# Node map
```json
[
 {
  "name": "Population",
  "type": "concept",
  "existing": false,
  "parent": "Populations and Samples",
  "prereqs": [],
  "uses": [],
  "page": 1,
  "summary": "The full collection of units or outcomes we want to study; must be defined precisely because conclusions only apply to the population the data can reasonably represent."
 },
 {
  "name": "Sample in statistics",
  "type": "concept",
  "existing": true,
  "parent": "Populations and Samples",
  "prereqs": [
   "Population"
  ],
  "uses": [],
  "page": 1,
  "summary": "The part of the population that is actually observed; used because observing the entire population is often impractical."
 },
 {
  "name": "Selection bias",
  "type": "concept",
  "existing": true,
  "parent": "Populations and Samples",
  "prereqs": [
   "Sample in statistics"
  ],
  "uses": [],
  "page": 2,
  "summary": "Occurs when some population members are more likely to be included in a sample than others in a way related to the trait being measured."
 },
 {
  "name": "Random Sampling",
  "type": "concept",
  "existing": false,
  "parent": "Populations and Samples",
  "prereqs": [
   "Selection bias"
  ],
  "uses": [],
  "page": 2,
  "summary": "Giving every population member a known probability of selection; reduces selection bias and lets probability theory describe sample-to-sample variation."
 },
 {
  "name": "Visualizing a Sample",
  "type": "concept",
  "existing": false,
  "parent": "Populations and Samples",
  "prereqs": [
   "Sample in statistics"
  ],
  "uses": [],
  "page": 2,
  "summary": "Graphing a sample before modeling reveals shape, spread, and unusual observations hidden by a single summary statistic, such as skew that separates the mean and median."
 },
 {
  "name": "Population parameter",
  "type": "concept",
  "existing": true,
  "parent": "Parameters",
  "prereqs": [
   "Population"
  ],
  "uses": [],
  "page": 4,
  "summary": "A fixed but generally unknown numerical quantity that describes a population or a statistical model for it, e.g. $\\mu$ and $\\sigma^2$ for a normal model."
 },
 {
  "name": "Quantity of Interest",
  "type": "concept",
  "existing": false,
  "parent": "Parameters",
  "prereqs": [
   "Population parameter"
  ],
  "uses": [],
  "page": 4,
  "summary": "A population feature we care about, which does not have to be one of a model's named parameters; it can instead be calculated from them."
 },
 {
  "name": "Frequentist Approach",
  "type": "concept",
  "existing": true,
  "parent": "Two Approaches to Uncertainty",
  "prereqs": [
   "Population parameter"
  ],
  "uses": [],
  "page": 5,
  "summary": "Treats the parameter as fixed but unknown; probability statements describe the long-run behavior of procedures under repeated sampling, e.g. a 95% CI's coverage rate."
 },
 {
  "name": "Bayesian Approach",
  "type": "concept",
  "existing": true,
  "parent": "Two Approaches to Uncertainty",
  "prereqs": [
   "Population parameter"
  ],
  "uses": [],
  "page": 8,
  "summary": "Represents uncertainty about a parameter with a probability distribution, allowing direct probability statements such as a 95% posterior interval."
 },
 {
  "name": "Likelihood Function",
  "type": "concept",
  "existing": true,
  "parent": "Likelihood",
  "prereqs": [],
  "uses": [],
  "page": 9,
  "summary": "$L(\\theta)=\\prod_{i=1}^n f(x_i\\mid\\theta)$; views the observed data as fixed and asks which parameter values make them most compatible with the model. It is not a probability distribution for $\\theta$."
 },
 {
  "name": "Log-Likelihood",
  "type": "concept",
  "existing": true,
  "parent": "Likelihood",
  "prereqs": [
   "Likelihood Function"
  ],
  "uses": [],
  "page": 11,
  "summary": "$\\ell(\\theta)=\\log L(\\theta)=\\sum_{i=1}^n \\log f(x_i\\mid\\theta)$; turns a product into a sum for easier computation and shares the same maximizer as $L(\\theta)$."
 },
 {
  "name": "Prior Distribution",
  "type": "concept",
  "existing": true,
  "parent": "Bayesian Inference Components",
  "prereqs": [
   "Bayesian Approach"
  ],
  "uses": [],
  "page": 12,
  "summary": "$\\pi(\\theta)$ describes uncertainty about a parameter before observing the current data; its shape and concentration reflect the strength of prior information."
 },
 {
  "name": "Bayes' Theorem for Distributions",
  "type": "concept",
  "existing": false,
  "parent": "Bayesian Inference Components",
  "prereqs": [
   "Prior Distribution",
   "Likelihood Function",
   "Bayes' Rule"
  ],
  "uses": [],
  "page": 19,
  "summary": "$\\pi(\\theta\\mid\\mathbf{x})=\\dfrac{f(\\mathbf{x}\\mid\\theta)\\pi(\\theta)}{m_n(\\mathbf{x})}$; the marginal $m_n(\\mathbf{x})$ normalizes the likelihood-times-prior into a valid posterior distribution."
 },
 {
  "name": "Posterior Distribution",
  "type": "concept",
  "existing": true,
  "parent": "Bayesian Inference Components",
  "prereqs": [
   "Bayes' Theorem for Distributions"
  ],
  "uses": [],
  "page": 18,
  "summary": "The conditional distribution of $\\theta$ given the data, $\\pi(\\theta\\mid\\mathbf{x}) \\propto L(\\theta)\\pi(\\theta)$; describes which parameter values remain plausible after observing the data."
 },
 {
  "name": "Conjugate Prior",
  "type": "concept",
  "existing": true,
  "parent": "Conjugate Families",
  "prereqs": [
   "Prior Distribution",
   "Posterior Distribution"
  ],
  "uses": [],
  "page": 22,
  "summary": "A prior whose posterior stays in the same distribution family for a given likelihood; e.g. Beta-Bernoulli, Gamma-Poisson, Normal-Normal."
 },
 {
  "name": "Beta-Bernoulli Update",
  "type": "concept",
  "existing": true,
  "parent": "Conjugate Families",
  "prereqs": [
   "Conjugate Prior"
  ],
  "uses": [],
  "page": 23,
  "summary": "With prior $p\\sim\\mathrm{Beta}(\\alpha,\\beta)$ and $s$ successes in $n$ Bernoulli trials, the posterior is $\\mathrm{Beta}(\\alpha+s,\\beta+n-s)$."
 },
 {
  "name": "Gamma-Poisson Update",
  "type": "concept",
  "existing": true,
  "parent": "Conjugate Families",
  "prereqs": [
   "Conjugate Prior"
  ],
  "uses": [],
  "page": 26,
  "summary": "With prior $\\lambda\\sim\\mathrm{Gamma}(\\alpha,\\beta)$ and $n$ Poisson counts, the posterior is $\\mathrm{Gamma}(\\alpha+\\sum x_i,\\beta+n)$."
 },
 {
  "name": "Normal-Normal Update",
  "type": "concept",
  "existing": true,
  "parent": "Conjugate Families",
  "prereqs": [
   "Conjugate Prior"
  ],
  "uses": [],
  "page": 29,
  "summary": "With known-variance normal data and a normal prior on $\\mu$, the posterior is normal with mean equal to a precision-weighted average of the prior mean and sample mean."
 },
 {
  "name": "Prior Influence and Sample Size",
  "type": "concept",
  "existing": true,
  "parent": "Conjugate Families",
  "prereqs": [
   "Normal-Normal Update",
   "Beta-Bernoulli Update",
   "Gamma-Poisson Update"
  ],
  "uses": [],
  "page": 31,
  "summary": "Prior location, prior variance, and sample size jointly determine how much the posterior is pulled toward the prior versus the data; more data reduce but do not eliminate this influence, and cannot fix a bad sample or model."
 },
 {
  "name": "On-Time Bus Arrivals",
  "type": "problem",
  "existing": false,
  "parent": "Likelihood",
  "prereqs": [
   "Likelihood Function"
  ],
  "uses": [
   "Likelihood Function"
  ],
  "page": 9,
  "summary": "Worked example deriving the likelihood for a binomial on-time-arrival probability and identifying its maximizing value."
 },
 {
  "name": "Reusable Container Participation",
  "type": "problem",
  "existing": false,
  "parent": "Conjugate Families",
  "prereqs": [
   "Prior Distribution",
   "Beta-Bernoulli Update",
   "Posterior Distribution"
  ],
  "uses": [
   "Prior Distribution",
   "Beta-Bernoulli Update",
   "Posterior Distribution"
  ],
  "page": 23,
  "summary": "Worked Beta-Bernoulli update for a participation proportion, from Beta(5,5) prior to Beta(26,14) posterior."
 },
 {
  "name": "Evening Bicycle Repairs",
  "type": "problem",
  "existing": false,
  "parent": "Conjugate Families",
  "prereqs": [
   "Prior Distribution",
   "Gamma-Poisson Update",
   "Posterior Distribution"
  ],
  "uses": [
   "Prior Distribution",
   "Gamma-Poisson Update",
   "Posterior Distribution"
  ],
  "page": 27,
  "summary": "Worked Gamma-Poisson update for an average repair rate, from Gamma(8,2) prior to Gamma(33,7) posterior."
 },
 {
  "name": "Device Charging Time",
  "type": "problem",
  "existing": false,
  "parent": "Conjugate Families",
  "prereqs": [
   "Prior Distribution",
   "Normal-Normal Update",
   "Posterior Distribution"
  ],
  "uses": [
   "Prior Distribution",
   "Normal-Normal Update",
   "Posterior Distribution"
  ],
  "page": 30,
  "summary": "Worked Normal-Normal update for a mean charging time using precision weighting."
 },
 {
  "name": "Interpretation of Confidence Intervals",
  "type": "concept",
  "existing": true,
  "parent": "",
  "prereqs": [],
  "summary": ""
 }
]
```

# Frankenstein problems

**Problem 1: New payment app adoption**

A campus food pantry wants to estimate $p$, the proportion of students who would use a new prepayment app. Based on adoption of similar apps at peer campuses, the prior is $p \sim \mathrm{Beta}(4,6)$ (prior mean 0.40). In a random sample of 25 students, 15 say they would use the app.

*Concepts tested:* Prior Distribution, Likelihood Function, Beta-Bernoulli Update, Posterior Distribution.

Solution:
1. Successes $s=15$, trials $n=25$, so failures $n-s=10$.
2. Likelihood: $L(p) \propto p^{15}(1-p)^{10}$.
3. Beta-Bernoulli update: $p \mid \mathbf{x} \sim \mathrm{Beta}(4+15,\ 6+10) = \mathrm{Beta}(19,16)$.
4. Posterior mean: $19/(19+16) = 19/35 \approx 0.5429$.
5. Posterior variance: $\dfrac{19 \cdot 16}{35^2 \cdot 36} = \dfrac{304}{44100} \approx 0.00689$.

Check: $4+15=19$ and $6+10=16$ (arithmetic verified twice); $19+16=35$; $19/35=0.542857\ldots$; $19\times16=304$, $35^2=1225$, $1225\times36=44100$, $304/44100=0.0068934\ldots$. The posterior mean (0.543) sits between the prior mean (0.40) and the sample proportion (15/25 = 0.60), as expected.

**Problem 2: Sleep hours after a stress workshop**

A campus wellness study estimates $\mu$, the mean nightly sleep (hours) of graduate students after a new stress-reduction workshop. Based on last year's cohort, the prior is $\mu \sim N(6.5,\ 0.8^2)$. Individual sleep times are modeled as normal with a known population sd $\sigma = 1.2$ hours. A new sample of $n=9$ students has a sample mean of 7.4 hours.

(a) Find the posterior distribution for $\mu$.
(b) Give the correct Bayesian interpretation of a resulting 95% posterior interval, and contrast it with what a 95% frequentist confidence interval would mean.
(c) If the sample size had instead been $n=100$ (same sample mean), would the posterior mean move closer to the prior mean or the sample mean? Explain using precision.

*Concepts tested:* Normal-Normal Update, Bayesian Approach, Frequentist Approach, Prior Influence and Sample Size.

Solution:
1. Prior precision: $1/0.8^2 = 1/0.64 = 1.5625$.
2. Data precision: $9/1.2^2 = 9/1.44 = 6.25$.
3. Posterior precision: $1.5625 + 6.25 = 7.8125$, so posterior variance $=1/7.8125 = 0.128$ and posterior sd $=\sqrt{0.128}\approx0.3578$.
4. Posterior mean: $\dfrac{1.5625(6.5) + 6.25(7.4)}{7.8125} = \dfrac{10.15625 + 46.25}{7.8125} = \dfrac{56.40625}{7.8125} = 7.22$.
   So $\mu \mid \mathbf{x} \sim N(7.22,\ 0.3578^2)$.
5. (b) Bayesian: given the model, prior, and data, there is a 95% probability that $\mu$ lies within the resulting interval. Frequentist: if we repeated this sampling procedure many times and built an interval the same way each time, about 95% of those intervals would contain the true $\mu$; the probability statement applies to the procedure, not to this one computed interval.
6. (c) With $n=100$, data precision $=100/1.44 \approx 69.44$, which is far larger than the prior precision of 1.5625. Since precision-weighted averaging gives more weight to the more precise source, the posterior mean would sit very close to the sample mean of 7.4 (roughly $0.0223(6.5)+0.9777(7.4)\approx7.38$), much closer to the data than in part (a).

Check: $0.8^2=0.64$, $1/0.64=1.5625$; $1.2^2=1.44$, $9/1.44=6.25$; sum $=7.8125$; $1/7.8125=0.128$ exactly ($7.8125\times0.128=1$); $1.5625\times6.5=10.15625$; $6.25\times7.4=46.25$; sum $=56.40625$; $56.40625/7.8125=7.22$ exactly ($7.8125\times7.22=56.40625$). Arithmetic verified twice.
