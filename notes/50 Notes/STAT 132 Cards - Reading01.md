---
type: reference
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "Reading01"
tags:
  - decks
---
# STAT 132 Cards - Reading01 Probability Foundations for Inference

## Conditional Probability
| Front | Back | Notes |
| --- | --- | --- |
| In the campus survey ($P(C)=0.40$, $P(E)=0.50$, $P(C \cap E)=0.25$), why does $P(C \mid E) = 0.50$ differ from $P(E \mid C) = 0.625$? | They condition on different events; restricting to $E$ gives one answer and restricting to $C$ gives another, so "probability a commuter has an 8am class" is not the same question as "probability an 8am student commutes." | p.3-4; discrimination |

## Random Variable
| Front | Back | Notes |
| --- | --- | --- |
| What is a random variable? | A function $X: \Omega \rightarrow \mathbb{R}$ that assigns a numerical value to each outcome; it is a numerical measurement determined by a random outcome. | p.5; definition |
| By convention, what do uppercase $X$ and lowercase $x$ each represent? | $X$ denotes the random variable itself, before the experiment is performed; $x$ denotes a possible or observed value it can take. | p.5; concept |

## PMF, PDF and CDF
| Front | Back | Notes |
| --- | --- | --- |
| How does a PDF represent probability for a continuous random variable, and what is $P(X=x)$ for one exact value? | Probability is the area under the curve, $P(a \le X \le b) = \int_a^b f(x)\,dx$; the curve's height is not itself a probability, and $P(X=x)=0$ for any single value since a zero-width interval has zero area. | p.7; concept |
| What is the cumulative distribution function (CDF), and what are its two key properties? | $F(x) = P(X \le x)$, defined for both discrete and continuous random variables; a CDF never decreases, starts at 0 on the far left, and approaches 1 on the far right. | p.7; formula |

## Binomial Distribution
| Front | Back | Notes |
| --- | --- | --- |
| What is the PMF of $X \sim \text{Bin}(n,p)$, and what must be true of the trials? | $P(X=x) = \binom{n}{x} p^x (1-p)^{n-x}$ for $x = 0,1,\dots,n$; requires $n$ independent trials, two categorized outcomes each, and a constant success probability $p$. | p.11; formula |
| What are $E[X]$ and $\text{Var}(X)$ for $X \sim \text{Bin}(n,p)$? | $E[X] = np$ and $\text{Var}(X) = np(1-p)$. | p.11; formula |

## Poisson Distribution
| Front | Back | Notes |
| --- | --- | --- |
| What is the PMF of $X \sim \text{Poisson}(\lambda)$, and what is distinctive about its mean and variance? | $P(X=x) = \dfrac{\lambda^x e^{-\lambda}}{x!}$ for $x=0,1,2,\dots$; $E[X] = \text{Var}(X) = \lambda$, a recognizable feature of the Poisson model. | p.11; formula |

## Normal Distribution
| Front | Back | Notes |
| --- | --- | --- |
| For $X \sim N(\mu, \sigma^2)$, what do $\mu$ and $\sigma^2$ represent, and when is a normal model a poor choice? | $\mu$ sets the center, $E[X]=\mu$, and $\sigma^2$ controls the spread, $\text{Var}(X)=\sigma^2$, of a symmetric bell-shaped curve; it is a poor model for strongly right-skewed variables like income or waiting time. | p.12; concept |

## Exponential Distribution
| Front | Back | Notes |
| --- | --- | --- |
| What are $E[X]$ and $\text{Var}(X)$ for $X \sim \text{Exp}(\lambda)$, and what does it typically model? | $E[X] = \dfrac{1}{\lambda}$ and $\text{Var}(X) = \dfrac{1}{\lambda^2}$; it models waiting times when events occur at a constant average rate. | p.12; formula |

## Gamma Distribution
| Front | Back | Notes |
| --- | --- | --- |
| What are $E[X]$ and $\text{Var}(X)$ for a Gamma distribution with shape $\alpha$ and rate $\beta$, and how does it relate to the exponential? | $E[X] = \dfrac{\alpha}{\beta}$ and $\text{Var}(X) = \dfrac{\alpha}{\beta^2}$; the exponential distribution is the special case $\alpha = 1$. | p.13; formula |

## Beta Distribution
| Front | Back | Notes |
| --- | --- | --- |
| What is the support of Beta$(\alpha,\beta)$, and what is it typically used to model? | $0 < x < 1$; it is especially useful for proportions and probabilities, and can be symmetric, skewed, or concentrated near the middle or endpoints depending on $\alpha,\beta$. | p.13-14; concept |

## Uniform Distribution
| Front | Back | Notes |
| --- | --- | --- |
| What are $E[X]$ and $\text{Var}(X)$ for $X \sim U(a,b)$? | $E[X] = \dfrac{a+b}{2}$ and $\text{Var}(X) = \dfrac{(b-a)^2}{12}$. | p.14; formula |

## Law of Large Numbers
| Front | Back | Notes |
| --- | --- | --- |
| What is a common misconception about what the law of large numbers implies for individual observations? | It is mistaken to think individual observations become less variable as $n$ grows; they remain just as unpredictable. The law only says the average becomes more stable as more data points are included. | p.17; discrimination |

## Central Limit Theorem
| Front | Back | Notes |
| --- | --- | --- |
| What does the central limit theorem (CLT) say about the sample mean $\bar{X}$? | As $n$ grows, the sampling distribution of $\bar{X}$ becomes approximately $N\!\left(\mu, \dfrac{\sigma^2}{n}\right)$, even if the original population is not normal. | p.17; concept |

## Sample in statistics
| Front | Back | Notes |
| --- | --- | --- |
| What is a sample, and why do we use one instead of measuring the whole population? | A sample is the subset we actually observe; we use it because measuring the entire population may be too costly, too slow, impossible, or conceptually inappropriate, such as when the population includes future outcomes. | p.20; definition |

## Statistical Model
| Front | Back | Notes |
| --- | --- | --- |
| What is a statistical model? | A set of probability distributions proposed as plausible descriptions of how the data were generated; it connects the population question to the mathematics of probability and always simplifies reality to some degree. | p.20; definition |

## Parametric vs Nonparametric
| Front | Back | Notes |
| --- | --- | --- |
| What does "nonparametric" actually mean, if not "no parameters" or "no assumptions"? | It means the population distribution is not restricted to a family indexed by a fixed, finite set of parameters, as when the sample median estimates the population median without assuming a shape. | p.21; discrimination |

## Statistic (inference)
| Front | Back | Notes |
| --- | --- | --- |
| What is a statistic? | Any function of the observed data, $T = t(X_1,\dots,X_n)$, that does not depend on an unknown parameter; before data collection it is a random variable, after collection it has a realized value. | p.22; definition |

## Point Estimate vs Interval Estimate
| Front | Back | Notes |
| --- | --- | --- |
| How does a point estimate differ from an interval estimate? | A point estimate is a single best guess for a parameter, such as $\hat p = 84/120 = 0.70$; an interval estimate gives a range of supported values with a measure of uncertainty, since a sample can't usually pin down the parameter exactly. | p.23; discrimination |

## Prediction (statistics)
| Front | Back | Notes |
| --- | --- | --- |
| How does prediction differ from estimation? | Estimation asks about a fixed feature of the population process, such as average enrollment; prediction concerns an unobserved or future outcome, such as next year's enrollment, which adds year-to-year variation on top of model uncertainty. | p.23; discrimination |

## Plagiarism Screening Tool
| Front | Back | Notes |
| --- | --- | --- |
| A plagiarism tool flags 90% of copied papers and 5% of clean papers, and 2% of papers are actually copied. What is $P(\text{copied} \mid \text{flagged})$? | $P(C \mid F) = \dfrac{(0.90)(0.02)}{(0.90)(0.02) + (0.05)(0.98)} \approx 0.269$; apply Bayes' rule with the law of total probability in the denominator. | p.5; procedure |

## Fair Coin Eight Heads Check
| Front | Back | Notes |
| --- | --- | --- |
| A coin is tossed 10 times and shows 8 heads. What is $P(X \ge 8)$ under $p=0.5$, and what does it say about $p=0.5$ still being plausible? | With $X \sim \text{Bin}(10,0.5)$, $P(X \ge 8) \approx 0.0547$; this is not extremely small, so 8 heads is not strong evidence against a fair coin. | p.19-20; procedure |

## Addition Rule
| Front | Back | Notes |
| --- | --- | --- |
| Why can't you always compute $P(A \cup B)$ as $P(A) + P(B)$? | The addition rule only holds for disjoint events; if $A$ and $B$ overlap, adding the probabilities double-counts the shared outcomes, like "roll even" and "roll greater than 3" both containing 4 and 6. | p.2; discrimination |

## Interpretations of Probability
| Front | Back | Notes |
| --- | --- | --- |
| If an event has probability 0.30, what does that mean over many repetitions? | It should occur on roughly 30% of repetitions in the long run; it does not mean it must occur in exactly 3 of any particular 10 trials, since short run variation is normal. | p.2; concept |

## Standard Deviation
| Front | Back | Notes |
| --- | --- | --- |
| What is $SD(X)$, and why report it instead of $\text{Var}(X)$? | $SD(X) = \sqrt{\text{Var}(X)}$; variance is in squared units, like squared minutes, while the standard deviation is back in the original units, like minutes. | p.10; concept |

## Standard Error
| Front | Back | Notes |
| --- | --- | --- |
| What is the formula for $SD(\bar{X})$, and what does it explain? | $SD(\bar{X}) = \dfrac{\sigma}{\sqrt{n}}$; it explains why sample averages become less variable as sample size grows. | p.17; formula |

## Null and Alternative Hypotheses
| Front | Back | Notes |
| --- | --- | --- |
| What do $H_0$ and $H_1$ represent, and what does a hypothesis test not do? | $H_0$ is the specific claim being assessed, such as $\mu = 100$, and $H_1$ represents the departures of interest, such as $\mu \ne 100$; a test does not prove a statement true, since data contain randomness and decisions can be wrong. | p.23-24; concept |

# Node map

```json
[
 {
  "name": "Sample Space",
  "type": "concept",
  "existing": false,
  "parent": "Probability Theory",
  "prereqs": [],
  "uses": [],
  "page": 1,
  "summary": "The sample space $\\Omega$ is the set of every possible outcome an experiment is designed to record; an event is a subset of $\\Omega$."
 },
 {
  "name": "Axioms of Probability",
  "type": "concept",
  "existing": false,
  "parent": "Probability Theory",
  "prereqs": [
   "Sample Space"
  ],
  "uses": [],
  "page": 2,
  "summary": "A probability measure satisfies $0 \\le P(A) \\le 1$, $P(\\Omega)=1$, and additivity over disjoint events; probabilities are interpreted as long-run proportions."
 },
 {
  "name": "Conditional Probability",
  "type": "concept",
  "existing": true,
  "parent": "Conditional Probability Rules",
  "prereqs": [
   "Axioms of Probability"
  ],
  "uses": [],
  "page": 3,
  "summary": "$P(A \\mid B) = P(A \\cap B)/P(B)$ restricts attention to outcomes in $B$; the order of conditioning matters."
 },
 {
  "name": "Bayes' Rule",
  "type": "concept",
  "existing": true,
  "parent": "Conditional Probability Rules",
  "prereqs": [
   "Conditional Probability"
  ],
  "uses": [],
  "page": 4,
  "summary": "Bayes' rule reverses the direction of conditioning, $P(A\\mid B) = P(B\\mid A)P(A)/P(B)$, using the law of total probability in the denominator."
 },
 {
  "name": "Random Variable",
  "type": "concept",
  "existing": false,
  "parent": "Random variable",
  "prereqs": [
   "Sample Space"
  ],
  "uses": [],
  "page": 5,
  "summary": "A random variable is a function $X:\\Omega \\to \\mathbb{R}$ that assigns a number to each outcome."
 },
 {
  "name": "Discrete vs Continuous Random Variable",
  "type": "concept",
  "existing": false,
  "parent": "Random variable",
  "prereqs": [
   "Random Variable"
  ],
  "uses": [],
  "page": 6,
  "summary": "Discrete random variables take listable values; continuous random variables take any value in an interval, and probability is assigned differently in each case."
 },
 {
  "name": "PMF, PDF and CDF",
  "type": "concept",
  "existing": true,
  "parent": "Random variable",
  "prereqs": [
   "Discrete vs Continuous Random Variable"
  ],
  "uses": [],
  "page": 6,
  "summary": "The PMF $f(x)=P(X=x)$ describes discrete distributions, the PDF gives probability as area, and the CDF $F(x)=P(X\\le x)$ accumulates probability for either type."
 },
 {
  "name": "Expectation and Variance",
  "type": "concept",
  "existing": true,
  "parent": "Random variable",
  "prereqs": [
   "PMF, PDF and CDF"
  ],
  "uses": [],
  "page": 9,
  "summary": "Expectation is the probability-weighted average of a distribution; variance and its square root, the standard deviation, describe its spread."
 },
 {
  "name": "Binomial Distribution",
  "type": "concept",
  "existing": false,
  "parent": "Common Distributions",
  "prereqs": [
   "PMF, PDF and CDF"
  ],
  "uses": [],
  "page": 11,
  "summary": "$X \\sim \\text{Bin}(n,p)$ counts successes in $n$ independent trials with constant success probability $p$; $E[X]=np$, $\\text{Var}(X)=np(1-p)$."
 },
 {
  "name": "Poisson Distribution",
  "type": "concept",
  "existing": false,
  "parent": "Common Distributions",
  "prereqs": [
   "PMF, PDF and CDF"
  ],
  "uses": [],
  "page": 11,
  "summary": "$X \\sim \\text{Poisson}(\\lambda)$ models counts of events in a fixed interval, with $E[X]=\\text{Var}(X)=\\lambda$."
 },
 {
  "name": "Normal Distribution",
  "type": "concept",
  "existing": false,
  "parent": "Common Distributions",
  "prereqs": [
   "PMF, PDF and CDF"
  ],
  "uses": [],
  "page": 12,
  "summary": "$X \\sim N(\\mu,\\sigma^2)$ is a symmetric bell-shaped model with $E[X]=\\mu$, $\\text{Var}(X)=\\sigma^2$, unsuitable for strongly skewed data."
 },
 {
  "name": "Exponential Distribution",
  "type": "concept",
  "existing": false,
  "parent": "Common Distributions",
  "prereqs": [
   "PMF, PDF and CDF"
  ],
  "uses": [],
  "page": 12,
  "summary": "$X \\sim \\text{Exp}(\\lambda)$ models waiting times at a constant rate, with $E[X]=1/\\lambda$, $\\text{Var}(X)=1/\\lambda^2$."
 },
 {
  "name": "Gamma Distribution",
  "type": "concept",
  "existing": false,
  "parent": "Common Distributions",
  "prereqs": [
   "Exponential Distribution"
  ],
  "uses": [],
  "page": 13,
  "summary": "The Gamma$(\\alpha,\\beta)$ distribution generalizes the exponential ($\\alpha=1$) with $E[X]=\\alpha/\\beta$, $\\text{Var}(X)=\\alpha/\\beta^2$."
 },
 {
  "name": "Beta Distribution",
  "type": "concept",
  "existing": false,
  "parent": "Common Distributions",
  "prereqs": [
   "PMF, PDF and CDF"
  ],
  "uses": [],
  "page": 13,
  "summary": "Beta$(\\alpha,\\beta)$ is supported on $(0,1)$ and models proportions or probabilities."
 },
 {
  "name": "Uniform Distribution",
  "type": "concept",
  "existing": false,
  "parent": "Common Distributions",
  "prereqs": [
   "PMF, PDF and CDF"
  ],
  "uses": [],
  "page": 14,
  "summary": "$X \\sim U(a,b)$ has equal density on $[a,b]$, with $E[X]=(a+b)/2$, $\\text{Var}(X)=(b-a)^2/12$."
 },
 {
  "name": "Law of Large Numbers",
  "type": "concept",
  "existing": true,
  "parent": "Sample Mean",
  "prereqs": [
   "Expectation and Variance"
  ],
  "uses": [],
  "page": 17,
  "summary": "The sample mean converges toward the population mean as sample size grows, without making individual observations less variable."
 },
 {
  "name": "Central Limit Theorem",
  "type": "concept",
  "existing": true,
  "parent": "Sample Mean",
  "prereqs": [
   "Law of Large Numbers",
   "Normal Distribution"
  ],
  "uses": [],
  "page": 17,
  "summary": "The sampling distribution of the sample mean becomes approximately $N(\\mu,\\sigma^2/n)$ as $n$ grows, regardless of the population's shape."
 },
 {
  "name": "Probability vs Inference",
  "type": "concept",
  "existing": true,
  "parent": "Statistical Inference",
  "prereqs": [
   "Binomial Distribution"
  ],
  "uses": [],
  "page": 19,
  "summary": "Probability reasons from a known model to possible data; statistical inference reasons from observed data back to an unknown model or parameter."
 },
 {
  "name": "Population",
  "type": "concept",
  "existing": false,
  "parent": "Statistical Inference",
  "prereqs": [],
  "uses": [],
  "page": 20,
  "summary": "The population is the full collection a study wants to understand."
 },
 {
  "name": "Sample in statistics",
  "type": "concept",
  "existing": true,
  "parent": "Statistical Inference",
  "prereqs": [
   "Population"
  ],
  "uses": [],
  "page": 20,
  "summary": "A sample is the observed subset of the population, used because observing the whole population is often impossible or impractical."
 },
 {
  "name": "Statistical Model",
  "type": "concept",
  "existing": false,
  "parent": "Statistical Inference",
  "prereqs": [
   "Population"
  ],
  "uses": [],
  "page": 20,
  "summary": "A statistical model is a set of probability distributions proposed as plausible descriptions of how data were generated."
 },
 {
  "name": "Parametric vs Nonparametric",
  "type": "concept",
  "existing": true,
  "parent": "Statistical Inference",
  "prereqs": [
   "Statistical Model",
   "Normal Distribution"
  ],
  "uses": [],
  "page": 21,
  "summary": "A parametric model restricts the population to a family indexed by finitely many parameters; a nonparametric approach avoids that restriction, not all assumptions."
 },
 {
  "name": "Population parameter",
  "type": "concept",
  "existing": true,
  "parent": "Statistical Inference",
  "prereqs": [
   "Statistical Model"
  ],
  "uses": [],
  "page": 21,
  "summary": "A parameter is a fixed but unknown numerical feature of a population model, and its parameter space is the set of values it may legally take."
 },
 {
  "name": "Statistic (inference)",
  "type": "concept",
  "existing": true,
  "parent": "Statistical Inference",
  "prereqs": [
   "Population parameter"
  ],
  "uses": [],
  "page": 22,
  "summary": "A statistic is a function of the sample data alone, such as the sample mean or sample variance, and is itself random before data are collected."
 },
 {
  "name": "Point Estimate vs Interval Estimate",
  "type": "concept",
  "existing": false,
  "parent": "Goals of Inference",
  "prereqs": [
   "Statistic (inference)"
  ],
  "uses": [],
  "page": 23,
  "summary": "A point estimate is a single best guess for a parameter; an interval estimate gives a range with an attached measure of uncertainty."
 },
 {
  "name": "Prediction (statistics)",
  "type": "concept",
  "existing": false,
  "parent": "Goals of Inference",
  "prereqs": [
   "Point Estimate vs Interval Estimate"
  ],
  "uses": [],
  "page": 23,
  "summary": "Prediction targets an unobserved or future outcome rather than a fixed population parameter."
 },
 {
  "name": "Hypothesis Testing",
  "type": "concept",
  "existing": false,
  "parent": "Goals of Inference",
  "prereqs": [
   "Population parameter"
  ],
  "uses": [],
  "page": 23,
  "summary": "A hypothesis test uses sample data to evaluate a null claim $H_0$ against an alternative $H_1$ without proving either true."
 },
 {
  "name": "Plagiarism Screening Tool",
  "type": "problem",
  "existing": false,
  "parent": "Conditional Probability Rules",
  "prereqs": [],
  "uses": [
   "Bayes' Rule",
   "Conditional Probability"
  ],
  "page": 5,
  "summary": "Worked Bayes' rule example computing $P(\\text{copied}\\mid\\text{flagged}) \\approx 0.269$ from a low base rate and imperfect test."
 },
 {
  "name": "Fair Coin Eight Heads Check",
  "type": "problem",
  "existing": false,
  "parent": "Statistical Inference",
  "prereqs": [],
  "uses": [
   "Binomial Distribution",
   "Probability vs Inference"
  ],
  "page": 19,
  "summary": "Worked example checking whether 8 heads in 10 tosses is surprising under a fair coin using the binomial tail probability."
 },
 {
  "name": "Addition Rule",
  "type": "concept",
  "existing": true,
  "parent": "",
  "prereqs": [],
  "summary": ""
 },
 {
  "name": "Interpretations of Probability",
  "type": "concept",
  "existing": true,
  "parent": "",
  "prereqs": [],
  "summary": ""
 },
 {
  "name": "Standard Deviation",
  "type": "concept",
  "existing": true,
  "parent": "",
  "prereqs": [],
  "summary": ""
 },
 {
  "name": "Standard Error",
  "type": "concept",
  "existing": true,
  "parent": "",
  "prereqs": [],
  "summary": ""
 },
 {
  "name": "Null and Alternative Hypotheses",
  "type": "concept",
  "existing": true,
  "parent": "",
  "prereqs": [],
  "summary": ""
 }
]
```

# Frankenstein problems

**Problem 1: Widget Sensor Line**

A factory produces widgets, 3% of which are defective. An inspection sensor correctly flags 95% of defective widgets, but also falsely flags 4% of good widgets.

(a) A widget is flagged by the sensor. What is the probability it is actually defective?

(b) Treating each widget's defect status as independent with $p=0.03$, a batch of 10 widgets is inspected. What is the probability that at least 2 of the 10 are actually defective?

(c) Which of (a) and (b) is a "probability" computation (model to data) and which is closer to the reversal of conditioning used in inference?

*Concepts tested: Bayes' Rule, Binomial Distribution, Probability vs Inference.*

**Solution**

(a) Let $D$ = defective, $F$ = flagged. $P(D)=0.03$, $P(F\mid D)=0.95$, $P(F\mid D^c)=0.04$.

$$P(F) = P(F\mid D)P(D) + P(F\mid D^c)P(D^c) = (0.95)(0.03) + (0.04)(0.97) = 0.0285 + 0.0388 = 0.0673$$

$$P(D \mid F) = \frac{0.0285}{0.0673} \approx 0.4235$$

So about 42.4% of flagged widgets are actually defective.

(b) $X \sim \text{Bin}(10, 0.03)$. Using $0.97^{10} \approx 0.737424$ and $0.97^{9} \approx 0.760231$:

$$P(X=0) = 0.97^{10} \approx 0.737424$$
$$P(X=1) = \binom{10}{1}(0.03)(0.97)^9 = 10(0.03)(0.760231) \approx 0.228069$$
$$P(X \ge 2) = 1 - P(X=0) - P(X=1) \approx 1 - 0.737424 - 0.228069 = 0.034507$$

So about 3.45% chance of 2 or more defective widgets in the batch.

(c) Part (b) is a probability computation: the model ($p=0.03$) is known and fixed, and we compute the chance of possible data. Part (a) uses Bayes' rule to reverse a conditional probability, which is the same logical move (going from what is known to what is uncertain in the other direction) that underlies statistical inference, though here the base rate itself is still assumed known rather than estimated from data.

---

**Problem 2: Battery Life Sampling Study**

A phone model's battery life has population mean $\mu = 20$ hours and standard deviation $\sigma = 4$ hours (the population shape is not assumed normal). A quality team draws a random sample of $n = 64$ phones and records the sample mean battery life $\bar{X}$.

(a) By the law of large numbers, what value should $\bar{X}$ be close to as $n$ grows?

(b) By the central limit theorem, what is the approximate sampling distribution of $\bar{X}$ for $n=64$?

(c) What is $SD(\bar{X})$?

(d) What is the approximate probability that $\bar{X}$ exceeds 21 hours?

*Concepts tested: Law of Large Numbers, Central Limit Theorem, Normal Distribution, Expectation and Variance.*

**Solution**

(a) By the law of large numbers, $\bar{X}$ should be close to the population mean $E[X] = \mu = 20$ hours.

(b) By the CLT, for $n=64$ (large enough for the approximation), $\bar{X}$ is approximately $N\!\left(\mu, \dfrac{\sigma^2}{n}\right) = N\!\left(20, \dfrac{16}{64}\right) = N(20, 0.25)$, regardless of the shape of the original battery-life distribution.

(c) $SD(\bar{X}) = \dfrac{\sigma}{\sqrt{n}} = \dfrac{4}{\sqrt{64}} = \dfrac{4}{8} = 0.5$ hours.

(d) Standardize: $Z = \dfrac{21 - 20}{0.5} = 2$.

$$P(\bar{X} > 21) \approx P(Z > 2) = 1 - \Phi(2) \approx 1 - 0.97725 = 0.02275$$

So there is approximately a 2.28% chance the sample mean exceeds 21 hours.
