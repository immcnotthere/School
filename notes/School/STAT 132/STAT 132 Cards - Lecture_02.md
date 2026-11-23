---
type: reference
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "Lecture_02"
tags:
  - decks
---
# STAT 132 Cards - Lecture_02 Frequentist vs Bayesian Inference

## Population
| Front | Back | Notes |
| --- | --- | --- |
| What is a population, in statistics? %%dk:t:qe7qvv%% | The full set of units that we are interested in studying. | p.2; definition |
| Is "all possible poker hands" a population or a sample? %%dk:t:4p83gq%% | A population; it is the complete set of possible hands, not a measured subset of them. | p.2; discrimination |

## Sample in statistics
| Front | Back | Notes |
| --- | --- | --- |
| What is a sample, in statistics? %%dk:t:vjcbzs%% | A subset of the units in a population for which we have measurements or data. | p.2; definition |
| Population vs sample: which one do we actually have data from? %%dk:t:cxusr0%% | The sample; the population is the full set we want to learn about, and it is not fully observed. | p.2; discrimination |

## Population parameter
| Front | Back | Notes |
| --- | --- | --- |
| What is a (population) parameter? %%dk:t:7exyv%% | A numerical measurement that describes some characteristic of a population. | p.2; definition |

## Frequentist Approach
| Front | Back | Notes |
| --- | --- | --- |
| In the frequentist approach, are parameters fixed or random? %%dk:t:21nrv9%% | Fixed but unknown constants. | p.4; definition |
| Why can't a frequentist say "there is a 95% probability the parameter is in this confidence interval"? | Because the parameter is a fixed constant: it is either inside the interval or not, we just don't know which, so no probability statement about it is meaningful. | p.4; discrimination |
| What kind of result does frequentist statistics focus on instead of probability statements about the parameter? | Long run, asymptotic results, e.g. the proportion of confidence intervals that would cover the true parameter if the sampling procedure were repeated many times. | p.4; definition |

## Bayesian Approach
| Front | Back | Notes |
| --- | --- | --- |
| In the Bayesian framework, how is a parameter $\theta$ treated? | As a random variable with its own probability distribution. | p.4; definition |
| In the Bayesian framework, what do the "prior" and "posterior" represent? | The prior is the distribution reflecting uncertainty about $\theta$ before seeing data; the posterior is that distribution updated after data becomes available. | p.4; definition |
| Frequentist vs Bayesian: which approach allows a direct probability statement about the parameter itself? | Bayesian, because $\theta$ is treated as a random variable whose distribution characterizes our state of knowledge. | p.4 to 5; discrimination |

## Likelihood Function
| Front | Back | Notes |
| --- | --- | --- |
| For a random sample $X_1,\dots,X_n$ with pdf/pmf $f(x\mid\theta)$, what is the likelihood function $L(\theta)$? | $L(\theta)=\prod_{i=1}^n f(X_i\mid\theta)$ | p.5; formula |
| In ordinary probability theory $f(x\mid\theta)$ is viewed as a function of the data $x$; in the likelihood function, what is it viewed as a function of? | The unknown parameter $\theta$, since the data has already been observed. | p.5; discrimination |
| How do you incorporate a constraint on the parameter space into a likelihood function? | Multiply by an indicator function that encodes the constraint. | p.5; procedure |

## Prior Distribution
| Front | Back | Notes |
| --- | --- | --- |
| With no prior information about a parameter known to lie in $[0,1]$, what prior is a common default choice? | A uniform distribution on $[0,1]$. | p.7; procedure |
| How does having more prior information, e.g. from past experiments, typically affect a prior's standard deviation? | It typically makes the standard deviation smaller, i.e. lower uncertainty. | p.7; discrimination |

## Posterior Distribution
| Front | Back | Notes |
| --- | --- | --- |
| What is the posterior distribution? | The distribution of a parameter $\theta$ obtained by updating the prior after observing data. | p.4; definition |

## Coin Flips Likelihood
| Front | Back | Notes |
| --- | --- | --- |
| 10 independent coin flips give 8 heads; $p=P(\text{heads})$ is unknown. What is $L(p)$? | $L(p)=\binom{10}{8}p^8(1-p)^2$ | p.5 to 6; problem |

## Test Scores Likelihood
| Front | Back | Notes |
| --- | --- | --- |
| Scores 45, 55, 50 are drawn iid from $N(\mu,10^2)$ with $\mu$ unknown. What is $L(\mu)$? | $L(\mu)=\displaystyle\prod_{i=1}^{3}\frac{1}{10\sqrt{2\pi}}\exp\!\left(-\frac{(x_i-\mu)^2}{200}\right)$ for $x_1=45,x_2=55,x_3=50$ | p.6; problem |

## Coin Prior (Fair or Two-Headed)
| Front | Back | Notes |
| --- | --- | --- |
| A coin is known to be either fair or two-headed; $\theta=P(\text{heads})$. What is an appropriate prior for $\theta$? | A discrete prior on two points, e.g. $\pi(0.5)=\pi(1)=0.5$ if both are considered equally plausible; one point mass at $\theta=0.5$, the other at $\theta=1$. | p.7; problem |

## Defective iPhones Uniform Prior
| Front | Back | Notes |
| --- | --- | --- |
| With no prior information about a defect proportion $\theta\in[0,1]$, what prior would you choose? | A Uniform$(0,1)$ prior for $\theta$. | p.7; problem |

## Lamp Lifetime Gamma Prior
| Front | Back | Notes |
| --- | --- | --- |
| A gamma prior for $\theta$ has mean 0.0002 and sd 0.0001, using mean $=\alpha/\beta$ and var $=\alpha/\beta^2$. Find $\alpha,\beta$. | $\beta=\text{mean}/\text{var}=0.0002/(0.0001)^2=20000$; $\alpha=\text{mean}\times\beta=0.0002\times20000=4$; so $\theta\sim\text{gamma}(4,20000)$. | p.7; problem |

## Quantity of Interest
| Front | Back | Notes |
| --- | --- | --- |
| Yes or no, and why: if we model IQ as normal, is "mean IQ" always the parameter we actually care about? %%dk:t:46v4ix%% | Not necessarily; mean is one parameter of the chosen distribution, but the parameter of interest, e.g. $P(\text{IQ}>140)$, can be a different quantity derived from the model. | p.3; discrimination |

# Node map

```json
[
 {
  "name": "Population",
  "type": "concept",
  "existing": false,
  "parent": "Basic Definitions",
  "prereqs": [],
  "uses": [],
  "page": 2,
  "summary": "A population is the full set of units that we are interested in studying."
 },
 {
  "name": "Sample in statistics",
  "type": "concept",
  "existing": true,
  "parent": "Basic Definitions",
  "prereqs": [
   "Population"
  ],
  "uses": [],
  "page": 2,
  "summary": "A sample is a subset of the units in a population for which we have measurements or data."
 },
 {
  "name": "Population parameter",
  "type": "concept",
  "existing": true,
  "parent": "Basic Definitions",
  "prereqs": [
   "Population"
  ],
  "uses": [],
  "page": 2,
  "summary": "A numerical measurement describing some characteristic of a population; may differ from the parameter of interest even after a distribution is chosen to model that population."
 },
 {
  "name": "Frequentist Approach",
  "type": "concept",
  "existing": true,
  "parent": "Frequentist vs Bayesian Statistics",
  "prereqs": [
   "Population parameter"
  ],
  "uses": [],
  "page": 4,
  "summary": "Parameters are considered fixed but unknown constants, so probability statements are made about long run procedures (e.g. confidence interval coverage), not about the parameter itself."
 },
 {
  "name": "Bayesian Approach",
  "type": "concept",
  "existing": true,
  "parent": "Frequentist vs Bayesian Statistics",
  "prereqs": [
   "Population parameter"
  ],
  "uses": [],
  "page": 4,
  "summary": "Parameters are treated as random variables with their own probability distribution (a prior, updated to a posterior after data), enabling direct probability statements about the parameter."
 },
 {
  "name": "Likelihood Function",
  "type": "concept",
  "existing": true,
  "parent": "The Likelihood",
  "prereqs": [
   "Population parameter",
   "Sample in statistics",
   "Probability density function"
  ],
  "uses": [],
  "page": 5,
  "summary": "For iid data $X_1,\\dots,X_n$ with pdf/pmf $f(x\\mid\\theta)$, $L(\\theta)=\\prod_{i=1}^n f(X_i\\mid\\theta)$, viewed as a function of $\\theta$ given the observed data; it is not itself a probability distribution."
 },
 {
  "name": "Prior Distribution",
  "type": "concept",
  "existing": true,
  "parent": "Bayesian Inference",
  "prereqs": [
   "Bayesian Approach"
  ],
  "uses": [],
  "page": 7,
  "summary": "The distribution $\\pi(\\theta)$ assigned to a parameter $\\theta$, treated as random, before observing any data."
 },
 {
  "name": "Posterior Distribution",
  "type": "concept",
  "existing": true,
  "parent": "Bayesian Inference",
  "prereqs": [
   "Prior Distribution",
   "Likelihood Function"
  ],
  "uses": [],
  "page": 4,
  "summary": "The updated distribution of $\\theta$ obtained after incorporating observed data into the prior."
 },
 {
  "name": "Coin Flips Likelihood",
  "type": "problem",
  "existing": false,
  "parent": "The Likelihood",
  "prereqs": [
   "Likelihood Function"
  ],
  "uses": [
   "Likelihood Function"
  ],
  "page": 5,
  "summary": "Derives $L(p)=\\binom{10}{8}p^8(1-p)^2$ for 10 coin flips with 8 observed heads."
 },
 {
  "name": "Test Scores Likelihood",
  "type": "problem",
  "existing": false,
  "parent": "The Likelihood",
  "prereqs": [
   "Likelihood Function"
  ],
  "uses": [
   "Likelihood Function"
  ],
  "page": 6,
  "summary": "Writes the likelihood function for 3 normal test scores (45, 55, 50) with known sd 10 and unknown mean."
 },
 {
  "name": "Coin Prior (Fair or Two-Headed)",
  "type": "problem",
  "existing": false,
  "parent": "Bayesian Inference",
  "prereqs": [
   "Prior Distribution"
  ],
  "uses": [
   "Prior Distribution"
  ],
  "page": 7,
  "summary": "Chooses a discrete two-point prior for a coin known to be either fair or two-headed."
 },
 {
  "name": "Defective iPhones Uniform Prior",
  "type": "problem",
  "existing": false,
  "parent": "Bayesian Inference",
  "prereqs": [
   "Prior Distribution"
  ],
  "uses": [
   "Prior Distribution"
  ],
  "page": 7,
  "summary": "Chooses a Uniform(0,1) prior for a defect proportion when no prior information is available."
 },
 {
  "name": "Lamp Lifetime Gamma Prior",
  "type": "problem",
  "existing": false,
  "parent": "Bayesian Inference",
  "prereqs": [
   "Prior Distribution"
  ],
  "uses": [
   "Prior Distribution"
  ],
  "page": 7,
  "summary": "Solves for gamma prior parameters $\\alpha=4,\\beta=20000$ from a given prior mean and standard deviation."
 },
 {
  "name": "Quantity of Interest",
  "type": "concept",
  "existing": true,
  "parent": "",
  "prereqs": [],
  "summary": ""
 }
]
```

# Frankenstein problems

**Problem 1.** A quality engineer studies the proportion of defective phones coming off a production line. The population is all phones manufactured this month; the parameter of interest is $\theta$, the true proportion defective. She takes a sample of 15 phones and finds 3 defective, modeling each phone's defect status as an independent Bernoulli($\theta$) trial.

(a) Identify the population, the sample, and the parameter.
(b) Write the likelihood function $L(\theta)$.

*Concepts tested: Population, Sample in statistics, Population parameter, Likelihood Function.*

Solution:
(a) Population: all phones manufactured this month. Sample: the 15 inspected phones. Parameter: $\theta$, the true proportion of defective phones in the population.
(b) With 3 defective out of 15 and each trial iid Bernoulli($\theta$), the number defective is Binomial(15, $\theta$), so
$$L(\theta) = \binom{15}{3}\theta^3(1-\theta)^{12}.$$
Check: $\binom{15}{3} = \dfrac{15\cdot14\cdot13}{3\cdot2\cdot1} = \dfrac{2730}{6} = 455$, so $L(\theta) = 455\,\theta^3(1-\theta)^{12}$.

**Problem 2.** A researcher wants to estimate $\theta$, the probability a new vaccine causes a mild side effect. With no prior information, she uses $\pi(\theta) = \text{Uniform}(0,1)$. She then observes 4 side effects out of 10 patients (iid Bernoulli($\theta)$ trials), giving likelihood $L(\theta) = \binom{10}{4}\theta^4(1-\theta)^6$.

(a) Contrast how a frequentist and a Bayesian would each treat $\theta$ in this setup.
(b) What is the unnormalized posterior for $\theta$ proportional to, and does it depend on the prior chosen here?
(c) Between the prior and the posterior, which one incorporates the observed data?

*Concepts tested: Frequentist Approach, Bayesian Approach, Prior Distribution, Posterior Distribution, Likelihood Function.*

Solution:
(a) A frequentist would treat $\theta$ as a fixed but unknown constant, so it is meaningless to assign it a probability; only long run properties of a procedure (e.g. coverage of a confidence interval for $\theta$) could be discussed. A Bayesian treats $\theta$ as a random variable with a distribution representing the researcher's uncertainty about it, so direct probability statements about $\theta$ are meaningful.
(b) The unnormalized posterior is proportional to prior times likelihood: since $\pi(\theta)=1$ on $[0,1]$, the posterior is proportional to $L(\theta) = \binom{10}{4}\theta^4(1-\theta)^6 \propto \theta^4(1-\theta)^6$. Because the uniform prior is constant, it does not change the shape here; the posterior's shape is driven entirely by the likelihood.
(c) The posterior; the prior is fixed before any data is seen, while the posterior is formed by updating that prior with the observed data through the likelihood.
