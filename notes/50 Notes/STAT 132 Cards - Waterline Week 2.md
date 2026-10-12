---
type: reference
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "Waterline Week 2"
tags:
  - decks
---
# STAT 132 Cards - Waterline Week 2 Distribution skills for Quiz 1, HW1 and Lecture 3

> [!important] What this deck is for (2026-09-30)
> Homework 1, Discussion 1 and Lecture 3 all run on the same few skills: writing each distribution's formula, solving for its parameters from a mean and variance, writing a likelihood, checking a prior's support, and recognizing a kernel. One fact per card, in dependency order, starting from the ground floor: what each letter means, then exponent rules, then pmf/pdf, then formulas. Each distribution starts with what it models and a plug-in example; if a card doesn't make sense, open [[STAT 132 Distribution Sheets]] to that distribution, read its sheet, then come back. Do it top to bottom, and hold each card 5 to 15 seconds before you flip it.

## Common Distributions
| Front | Back | Notes |
| --- | --- | --- |
| What is a parameter of a distribution? %%dk:t:3aidi5%% | A number you set that picks one specific version of it, like the $p$ of a coin. | ground floor |
| Bernoulli: what is $X$? %%dk:t:ojkfsd%% | The result of one yes/no trial: 1 for yes (success), 0 for no. | ground floor |
| Bernoulli: what does $p$ stand for? %%dk:t:sngnb1%% | The probability that $X = 1$ (success). It is defined that way; nothing is calculated. | ground floor |
| Bernoulli: if P(success) = $p$, what is P(failure)? %%dk:t:9215wu%% | $1 - p$ | ground floor |
| Why must P(failure) be $1 - p$? %%dk:t:gbrlzs%% | There are only two outcomes, and their probabilities must add to 1. | ground floor |
| Binomial: what is $X$? %%dk:t:2jeeo2%% | How many successes you got in $n$ tries. | ground floor |
| Binomial: what do $n$ and $p$ stand for? %%dk:t:31n5q3%% | $n$ = number of tries; $p$ = chance of success on each try. | ground floor |
| Poisson: what is $X$? %%dk:t:4rludk%% | A count of events in a fixed window (0, 1, 2, ..., no upper limit). | ground floor |
| Exponential: what is $X$? %%dk:t:zeapfw%% | A waiting time: how long until the next event. | ground floor |
| Exponential: what does the rate $\beta$ stand for? %%dk:t:5g74td%% | How many events happen per unit of time, on average. | ground floor |
| Normal: what do $\mu$ and $\sigma$ stand for? %%dk:t:smfrs2%% | $\mu$ = the center; $\sigma$ = the spread (standard deviation). | ground floor |
| Uniform$(a, b)$: what do $a$ and $b$ stand for? %%dk:t:h3tlid%% | The lowest and highest possible values. | ground floor |
| Gamma and Beta in this course: what is the random quantity? %%dk:t:et55ii%% | Usually a parameter you're unsure about (a rate, or a probability $p$): they describe your belief about it. | ground floor |

## Exponent Rules
| Front | Back | Notes |
| --- | --- | --- |
| $a^1 = ?$ %%dk:t:287zoo%% | $a$ | ground floor |
| $a^0 = ?$ (for $a \ne 0$) %%dk:t:l04ww3%% | $1$ | ground floor |
| $0.3^0 \times 0.7^1 = ?$ %%dk:t:9d3vo5%% | $1 \times 0.7 = 0.7$ | ground floor |
| $a^m \cdot a^n = ?$ %%dk:t:1hdga1%% | $a^{m+n}$: same base, add the exponents. | ground floor |
| $p \cdot p \cdot p = ?$ (as one power) %%dk:t:tdt6qc%% | $p^3$ | ground floor |
| $p^3 \cdot (1-p) \cdot p^5 \cdot (1-p) = ?$ %%dk:t:b30t7k%% | $p^8(1-p)^2$ | ground floor |
| Exponent rule: $\prod_{i=1}^n a^{x_i}$ as a single power? %%dk:t:hmlr7c%% | $a^{\sum x_i}$ | algebra; formula |
| $\prod_{i=1}^n e^{-\lambda}$ as a single term? %%dk:t:2ljiw2%% | $e^{-n\lambda}$ | algebra; formula |

## PMF, PDF and CDF
| Front | Back | Notes |
| --- | --- | --- |
| What is a pmf, in plain words? %%dk:t:nyc44j%% | A list of the possible values and the probability of each: $f(x) = P(X = x)$. | sheet 0; foundation |
| Fair die: what is $f(3)$? %%dk:t:mel52r%% | $\frac{1}{6}$ | sheet 0; foundation |
| What must a pmf's values add up to? %%dk:t:pmn6uv%% | 1 | sheet 0; foundation |
| Which kind of variable gets a pmf: discrete or continuous? %%dk:t:qm4fjr%% | Discrete: values you can count, like 0, 1, 2, ... | sheet 0; foundation |
| Which kind of variable gets a pdf? %%dk:t:ow1bxx%% | Continuous: any value in a range, like a waiting time. | sheet 0; foundation |
| For a pdf, what gives you a probability? %%dk:t:y5y3ck%% | The area under $f$ over a range; $f(x)$ itself is not a probability. | sheet 0; foundation |
| Bernoulli's pmf $p^x(1-p)^{1-x}$ written as a two-value list? %%dk:t:vxcit3%% | $f(0) = 1 - p$, $f(1) = p$ | sheet 0; foundation |

## Bernoulli Distribution
| Front | Back | Notes |
| --- | --- | --- |
| Bernoulli$(p)$: what does it model? %%dk:t:mb2geh%% | One yes/no trial that succeeds with probability $p$ (e.g. one coin flip). | sheet; understanding |
| Bernoulli pmf $p^x(1-p)^{1-x}$: plug in $x = 1$. What do you get? %%dk:t:wsh2ey%% | $p^1(1-p)^0 = p$ | sheet; understanding |
| Bernoulli pmf $p^x(1-p)^{1-x}$: plug in $x = 0$. What do you get? %%dk:t:q12jmh%% | $p^0(1-p)^1 = 1 - p$ | sheet; understanding |
| Bernoulli$(p)$: what is the mean? %%dk:t:1d92m0%% | $p$, because $0 \cdot (1-p) + 1 \cdot p = p$. | sheet; understanding |
| Bernoulli$(p)$: what is the variance? %%dk:t:nilbvg%% | $p(1-p)$ | sheet; understanding |
| Bernoulli$(p)$: write its pmf as one formula. %%dk:t:a7jqzb%% | $f(x) = p^x(1-p)^{1-x}$ for $x \in \{0, 1\}$ | Reading01 1.6; formula |

## Binomial Distribution
| Front | Back | Notes |
| --- | --- | --- |
| Binomial$(n, p)$: what does it count? %%dk:t:rz3cyw%% | The number of successes in $n$ independent yes/no trials. | sheet; understanding |
| Binomial$(n, p)$: write its pmf. %%dk:t:tbv200%% | $\binom{n}{x} p^x (1-p)^{n-x}$ for $x = 0, 1, \dots, n$ | sheet; understanding |
| In the Binomial pmf, what is $\binom{n}{x}$ for? %%dk:t:ufsukb%% | Counting the orders the $x$ successes can come in. | sheet; understanding |
| Binomial$(3, 0.5)$: what is $P(X = 2)$? %%dk:t:m2gqhx%% | $3 \times 0.5^2 \times 0.5 = 0.375$ | sheet; understanding |
| Binomial$(n, p)$: what is the mean? %%dk:t:7fha41%% | $np$ | sheet; understanding |
| Binomial$(n, p)$: what is the variance? %%dk:t:sk268t%% | $np(1-p)$ | sheet; understanding |

## Poisson Distribution
| Front | Back | Notes |
| --- | --- | --- |
| Poisson$(\lambda)$: what does it count? %%dk:t:li3n%% | How many times something happens in a fixed window of time or space. | sheet; understanding |
| Poisson: what does $\lambda$ stand for? %%dk:t:nklz3f%% | The average count per window. | sheet; understanding |
| Poisson$(2)$: what is $P(X = 0)$? %%dk:t:j0fz9%% | $e^{-2} \approx 0.135$ | sheet; understanding |
| Poisson$(\lambda)$: what is the mean? %%dk:t:s3h9wm%% | $\lambda$ | sheet; understanding |
| Poisson$(\lambda)$: what is the variance? | $\lambda$, the same as the mean. | sheet; understanding |
| Poisson$(\lambda)$: write its pmf. %%dk:t:olc00b%% | $f(x) = \dfrac{e^{-\lambda}\lambda^x}{x!}$ for $x = 0, 1, 2, \dots$ | Reading01 1.6.2; formula |
| Poisson$(\lambda)$: what values can $\lambda$ take? %%dk:t:vtx1m4%% | $\lambda > 0$ | Reading01 1.6.2; definition |

## Exponential distribution
| Front | Back | Notes |
| --- | --- | --- |
| Exponential$(\beta)$: what does it measure? %%dk:t:nvmxjt%% | A waiting time until the next event, when events come at rate $\beta$. | sheet; understanding |
| Buses arrive at rate $\beta = 4$ per hour. What is the average wait? %%dk:t:90nex2%% | $1/4$ hour, i.e. 15 minutes. | sheet; understanding |
| Exponential$(\beta)$: what is the mean? %%dk:t:u1mk25%% | $1/\beta$ | sheet; understanding |
| Exponential$(\beta)$: what is the variance? %%dk:t:8bipwf%% | $1/\beta^2$ | sheet; understanding |
| Exponential$(\lambda)$ with rate $\lambda$: write its pdf. %%dk:t:onv4r5%% | $f(x) = \lambda e^{-\lambda x}$ for $x > 0$ | Reading01 1.6.4; formula |
| Exponential$(\lambda)$ is which Gamma distribution? %%dk:t:namzck%% | Gamma$(1, \lambda)$ | Reading01 1.6.5; relation |

## Gamma Distribution
| Front | Back | Notes |
| --- | --- | --- |
| In this course, what is the Gamma distribution mostly used for? %%dk:t:s9tb7x%% | A prior for a positive parameter, like a Poisson rate $\lambda$. | sheet; understanding |
| In the Gamma pdf, which part is the constant that makes the area 1? %%dk:t:bplp5w%% | $\dfrac{\beta^\alpha}{\Gamma(\alpha)}$ | sheet; understanding |
| Gamma$(\alpha, \beta)$ with rate $\beta$: write its pdf. %%dk:t:5y6scp%% | $f(x) = \dfrac{\beta^\alpha}{\Gamma(\alpha)}x^{\alpha-1}e^{-\beta x}$ for $x > 0$ | Reading01 1.6.5; formula |
| Gamma$(\alpha, \beta)$: what is the mean? %%dk:t:5use3p%% | $\alpha / \beta$ | Reading01 1.6.5; formula |
| Gamma$(\alpha, \beta)$: what is the variance? %%dk:t:27snnd%% | $\alpha / \beta^2$ | Reading01 1.6.5; formula |
| Gamma$(\alpha, \beta)$: what values can $x$ take? %%dk:t:gcwcwm%% | $x > 0$ | Reading01 1.6.5; definition |

## Beta Distribution
| Front | Back | Notes |
| --- | --- | --- |
| In this course, what is the Beta distribution mostly used for? %%dk:t:jm10zw%% | A prior for a probability $p$, since its values lie between 0 and 1. | sheet; understanding |
| In the Beta pdf, which part is the constant that makes the area 1? %%dk:t:9u8f6n%% | $\dfrac{1}{B(\alpha, \beta)}$ | sheet; understanding |
| Beta$(3, 6)$: what is the mean? %%dk:t:v6v0zx%% | $\dfrac{3}{3+6} = \dfrac{1}{3}$ | sheet; understanding |
| Beta$(\alpha, \beta)$ with $\alpha > \beta$: which way does it lean? %%dk:t:shpb6u%% | Toward 1. | sheet; understanding |
| Beta$(\alpha, \beta)$: write its pdf. %%dk:t:l6b6eg%% | $f(x) = \dfrac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha, \beta)}$ for $0 < x < 1$ | Reading01 1.6.6; formula |
| Beta$(\alpha, \beta)$: what is the mean? %%dk:t:6awhaq%% | $\dfrac{\alpha}{\alpha + \beta}$ | Reading01 1.6.6; formula |
| Beta$(\alpha, \beta)$: what is the variance? %%dk:t:ttt8e6%% | $\dfrac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}$ | Reading01 1.6.6; formula |
| Beta: write the variance using only the mean $m$ and $s = \alpha + \beta$. %%dk:t:pwai0k%% | $\dfrac{m(1-m)}{s+1}$ | derived; formula |
| Uniform$(0, 1)$ is which Beta distribution? %%dk:t:m1decc%% | Beta$(1, 1)$ | Reading01 1.6.6; relation |

## Normal distribution
| Front | Back | Notes |
| --- | --- | --- |
| In the Normal pdf, what does $(x - \mu)^2$ measure? %%dk:t:v4wzdj%% | The squared distance of $x$ from the center $\mu$. | sheet; understanding |
| $N(\mu, \sigma^2)$: what is the mean? %%dk:t:wd6a61%% | $\mu$ | sheet; understanding |
| $N(\mu, \sigma^2)$: what is the variance? %%dk:t:9uwrsj%% | $\sigma^2$ (the SD is $\sigma$) | sheet; understanding |
| $N(\mu, \sigma^2)$: write its pdf. %%dk:t:h2vgvh%% | $f(x) = \dfrac{1}{\sqrt{2\pi\sigma^2}}e^{-(x-\mu)^2/(2\sigma^2)}$ for all real $x$ | Reading01 1.6.3; formula |

## Uniform distribution
| Front | Back | Notes |
| --- | --- | --- |
| Uniform$(a, b)$: write its pdf. %%dk:t:dqd2jf%% | $\dfrac{1}{b-a}$ on $[a, b]$ | sheet; understanding |
| Uniform$(0, 10)$: what is the height of the pdf? %%dk:t:5qo335%% | $0.1$ | sheet; understanding |
| Uniform$(a, b)$: what is the mean? %%dk:t:xiat6z%% | $\dfrac{a+b}{2}$ | sheet; understanding |

## Prior Parameters from Mean and Variance
| Front | Back | Notes |
| --- | --- | --- |
| A Gamma prior has mean $m$ and variance $v$. Formula for $\beta$? %%dk:t:a244fy%% | $\beta = m / v$ (divide the mean $\alpha/\beta$ by the variance $\alpha/\beta^2$) | HW1-type; procedure |
| A Gamma prior has mean $m$ and variance $v$. Formula for $\alpha$? %%dk:t:g9z7ja%% | $\alpha = m^2 / v$ (that is, $m\beta$) | HW1-type; procedure |
| A Beta prior has mean $m$ and variance $v$. What do you solve for first? %%dk:t:5kl9pu%% | $s = \alpha + \beta$, from $v = \dfrac{m(1-m)}{s+1}$ | HW1-type; procedure |
| Beta prior: once you have $m$ and $s = \alpha + \beta$, what is $\alpha$? %%dk:t:dt9i0a%% | $\alpha = m s$ | HW1-type; procedure |
| Beta prior: once you have $m$ and $s = \alpha + \beta$, what is $\beta$? %%dk:t:tv46r6%% | $\beta = (1 - m)s$ | HW1-type; procedure |
| Beta with mean $1/3$ and variance $1/45$: what is $s = \alpha + \beta$? %%dk:t:58xyyn%% | $s + 1 = \dfrac{(1/3)(2/3)}{1/45} = 10$, so $s = 9$ | Discussion 1 Q1; worked |
| Beta with mean $1/3$ and $s = 9$: what are $\alpha$ and $\beta$? %%dk:t:kckqfw%% | $\alpha = 3$, $\beta = 6$ | Discussion 1 Q1; worked |
| You're given a prior's standard deviation, not its variance. First step? %%dk:t:1zqn3c%% | Square it: variance = SD squared. | class 9/29; transcript |
| Lamp lifetimes: Gamma prior with mean 0.0002 and SD 0.0001. What are $\alpha$ and $\beta$? %%dk:t:tp4gnf%% | $\alpha = 4$, $\beta = 20{,}000$ | class 9/29; transcript |
| Lamp example: write the prior pdf $\pi(\theta)$. %%dk:t:er0o2y%% | $\frac{20000^4}{3!}\theta^3 e^{-20000\theta}$ for $\theta > 0$ | class 9/29; transcript |

## Likelihood Function
| Front | Back | Notes |
| --- | --- | --- |
| Bernoulli sample $x_1, \dots, x_n$: simplified likelihood $L(p)$? %%dk:t:brbon1%% | $p^{\sum x_i}(1-p)^{n - \sum x_i}$ | Lecture 2; procedure |
| Poisson sample $x_1, \dots, x_n$: simplified likelihood $L(\lambda)$? %%dk:t:zavtkb%% | $\dfrac{e^{-n\lambda}\lambda^{\sum x_i}}{\prod x_i!}$ | HW1-type; procedure |
| Exponential sample $x_1, \dots, x_n$: simplified likelihood $L(\lambda)$? %%dk:t:lacytt%% | $\lambda^n e^{-\lambda \sum x_i}$ | Discussion 1 Q2; procedure |
| Coin, 8 heads in 10 flips: likelihood $L(p)$? %%dk:t:cl1t3k%% | $p^8(1-p)^2$ | Lecture 2 Example 2.1; worked |
| The likelihood is a function of which: the data or the parameter? %%dk:t:8zamc7%% | The parameter; the data are fixed numbers now. | Lecture 2; key move |
| What does an indicator like $I(0 \le p \le 1)$ do in a likelihood? %%dk:t:a5d3u5%% | Makes the likelihood 0 for any parameter value outside the parameter space. | class 9/29; transcript |
| Poisson likelihood: which indicator goes on it? %%dk:t:qqfti4%% | $I(\lambda > 0)$ | class 9/29; transcript |
| When can you leave the indicator off a likelihood? %%dk:t:qhj4nz%% | When the parameter is unrestricted, like a normal mean $\mu$: the indicator is always 1. | class 9/29; transcript |
| 8 heads in 10, modeled as one Binomial instead of 10 Bernoullis: how does the likelihood change? %%dk:t:u8ulmo%% | Only by the constant $\binom{10}{8}$; the shape in $p$ is the same. | class 9/29; transcript |
| $\int_0^1 p^8(1-p)^2\,dp$ = ? %%dk:t:f89ltk%% | $B(9,3) = \frac{1}{495}$, not 1: a likelihood is not a probability distribution. | class 9/29; transcript |
| Normal with $\sigma = 10$, scores 45, 55, 50: likelihood $L(\mu)$? %%dk:t:1ft84p%% | $(2\pi \cdot 100)^{-3/2}\exp\left(-\frac{\sum (x_i - \mu)^2}{200}\right)$ | class 9/29; transcript |

## Support (Probability)
| Front | Back | Notes |
| --- | --- | --- |
| What makes a prior reasonable, in terms of where it puts probability? %%dk:t:bsbrwj%% | Its support matches the parameter space: no probability on impossible values, none missing from possible ones. | HW1 Q5 / Discussion 1 Q3; key move |
| Why is a normal prior a poor choice for a Poisson rate $\lambda$? %%dk:t:lmuicb%% | It puts probability on $\lambda < 0$, and a rate can't be negative. | HW1 Q5-type; key move |
| A prior gives zero probability to some value. What will the posterior give it? %%dk:t:5x0777%% | Zero, whatever the data say. | Lecture 3 preview; key move |

## Kernel of a Distribution
| Front | Back | Notes |
| --- | --- | --- |
| What is the kernel of a pdf? %%dk:t:4n0gsl%% | The part that depends on the variable, with every constant factor dropped. | Lecture 3 preview; definition |
| The Beta$(\alpha, \beta)$ kernel in $p$? %%dk:t:erwfbj%% | $p^{\alpha-1}(1-p)^{\beta-1}$ | Lecture 3 preview; formula |
| The Gamma$(\alpha, \beta)$ kernel in $\lambda$? %%dk:t:675j6r%% | $\lambda^{\alpha-1}e^{-\beta\lambda}$ | Lecture 3 preview; formula |
| $p^8(1-p)^2$ is the kernel of which Beta? %%dk:t:huvo2g%% | Beta$(9, 3)$: add 1 to each exponent. | Lecture 3 preview; worked |

## Posterior Distribution
| Front | Back | Notes |
| --- | --- | --- |
| The posterior is proportional to what? %%dk:t:nmutuz%% | Likelihood times prior: $\pi(\theta \mid x) \propto f(x \mid \theta)\pi(\theta)$ | Lecture 3 1.2; formula |
| Why can the denominator $m_n(x)$ be dropped? %%dk:t:7ekzxs%% | It doesn't depend on $\theta$, so it's just a constant. | Lecture 3 1.2; key move |
| Coin with 8 heads in 10 flips and a Uniform$(0,1)$ prior: what is the posterior? %%dk:t:xqmx0n%% | Beta$(9, 3)$, since $p^8(1-p)^2 \times 1$ is its kernel. | Lecture 3 Example 1.2; worked |

## Beta-Bernoulli Update
| Front | Back | Notes |
| --- | --- | --- |
| Beta$(\alpha, \beta)$ prior with Bernoulli data: what is the posterior? %%dk:t:gpw8a2%% | Beta$(\alpha + \sum x_i,\ \beta + n - \sum x_i)$: add the successes and the failures. | Lecture 3 1.5; formula |

## Gamma-Poisson Update
| Front | Back | Notes |
| --- | --- | --- |
| Gamma$(\alpha, \beta)$ prior with Poisson data: what is the posterior? %%dk:t:yj2b46%% | Gamma$(\alpha + \sum x_i,\ \beta + n)$: add the total count and the number of observations. | Lecture 3 1.6; formula |

## Probability distribution
| Front | Back | Notes |
| --- | --- | --- |
| What is a distribution, in plain words? %%dk:t:cx5n0q%% | Which values a random quantity can take, and how likely each one is. | ground floor |

## Gamma and Beta Functions
| Front | Back | Notes |
| --- | --- | --- |
| $\Gamma(4) = ?$ %%dk:t:k3h4p2%% | $3! = 6$ | sheet; understanding |

## Prior Distribution
| Front | Back | Notes |
| --- | --- | --- |
| The parameter can only take a few values (e.g. $p$ is 0.1 or 0.2). What kind of prior? %%dk:t:txh0m9%% | A discrete prior: a pmf over the allowed values. | class 9/29; transcript |
| No prior information about $p$ in $[0,1]$: the standard choice of prior? %%dk:t:5z6kbj%% | Uniform$(0,1)$, which is flat and adds no beliefs of your own. | class 9/29; transcript |

# Node map
```json
[
 {
  "name": "Common Distributions",
  "type": "concept",
  "existing": true,
  "parent": "Probability theory",
  "prereqs": [],
  "uses": [],
  "page": 10,
  "summary": "The standard families (Bernoulli, Binomial, Poisson, Exponential, Gamma, Beta, Normal, Uniform): what each models and what its parameters mean."
 },
 {
  "name": "Exponent Rules",
  "type": "concept",
  "existing": true,
  "parent": "Algebra",
  "prereqs": [],
  "uses": [],
  "page": 1,
  "summary": "$a^1 = a$, $a^0 = 1$, $a^m a^n = a^{m+n}$."
 },
 {
  "name": "PMF, PDF and CDF",
  "type": "concept",
  "existing": true,
  "parent": "Probability theory",
  "prereqs": [],
  "uses": [],
  "page": 6,
  "summary": "pmf: $f(x) = P(X=x)$ for discrete values; pdf: density whose area gives probability for continuous values; CDF: $F(x) = P(X \\le x)$."
 },
 {
  "name": "Bernoulli Distribution",
  "type": "concept",
  "existing": true,
  "parent": "Common Distributions",
  "prereqs": [],
  "uses": [],
  "page": 11,
  "summary": "One trial: $f(x) = p^x(1-p)^{1-x}$, $x \\in \\{0,1\\}$."
 },
 {
  "name": "Binomial Distribution",
  "type": "concept",
  "existing": true,
  "parent": "Common Distributions",
  "prereqs": [
   "Bernoulli Distribution"
  ],
  "uses": [],
  "page": 11,
  "summary": "Successes in $n$ independent trials: $\\binom{n}{x}p^x(1-p)^{n-x}$; mean $np$, variance $np(1-p)$."
 },
 {
  "name": "Poisson Distribution",
  "type": "concept",
  "existing": true,
  "parent": "Common Distributions",
  "prereqs": [],
  "uses": [],
  "page": 11,
  "summary": "Counts: $f(x) = e^{-\\lambda}\\lambda^x/x!$, $\\lambda > 0$."
 },
 {
  "name": "Exponential distribution",
  "type": "concept",
  "existing": true,
  "parent": "Common Distributions",
  "prereqs": [],
  "uses": [],
  "page": 12,
  "summary": "Waiting time: $f(x) = \\lambda e^{-\\lambda x}$, $x > 0$; Gamma$(1,\\lambda)$."
 },
 {
  "name": "Gamma Distribution",
  "type": "concept",
  "existing": true,
  "parent": "Common Distributions",
  "prereqs": [
   "Gamma and Beta Functions"
  ],
  "uses": [],
  "page": 13,
  "summary": "$f(x) = \\frac{\\beta^\\alpha}{\\Gamma(\\alpha)}x^{\\alpha-1}e^{-\\beta x}$, $x>0$; mean $\\alpha/\\beta$, variance $\\alpha/\\beta^2$."
 },
 {
  "name": "Beta Distribution",
  "type": "concept",
  "existing": true,
  "parent": "Common Distributions",
  "prereqs": [
   "Gamma and Beta Functions"
  ],
  "uses": [],
  "page": 13,
  "summary": "$f(x) = x^{\\alpha-1}(1-x)^{\\beta-1}/B(\\alpha,\\beta)$ on $(0,1)$; mean $\\alpha/(\\alpha+\\beta)$."
 },
 {
  "name": "Normal distribution",
  "type": "concept",
  "existing": true,
  "parent": "Common Distributions",
  "prereqs": [],
  "uses": [],
  "page": 12,
  "summary": "$f(x) = \\frac{1}{\\sqrt{2\\pi\\sigma^2}}e^{-(x-\\mu)^2/(2\\sigma^2)}$."
 },
 {
  "name": "Uniform distribution",
  "type": "concept",
  "existing": true,
  "parent": "Common Distributions",
  "prereqs": [],
  "uses": [],
  "page": 14,
  "summary": "$f(x) = 1/(b-a)$ on $[a,b]$; mean $(a+b)/2$, variance $(b-a)^2/12$."
 },
 {
  "name": "Prior Parameters from Mean and Variance",
  "type": "concept",
  "existing": false,
  "parent": "Prior Distribution",
  "prereqs": [
   "Gamma Distribution",
   "Beta Distribution"
  ],
  "uses": [],
  "page": 1,
  "summary": "Match the family's mean and variance formulas to the given numbers and solve. Gamma: $\\beta = m/v$, $\\alpha = m^2/v$. Beta: $s = \\alpha+\\beta$ from $v = m(1-m)/(s+1)$, then $\\alpha = ms$, $\\beta = (1-m)s$."
 },
 {
  "name": "Likelihood Function",
  "type": "concept",
  "existing": true,
  "parent": "Statistical Inference",
  "prereqs": [
   "Bernoulli Distribution",
   "Poisson Distribution",
   "Exponential distribution"
  ],
  "uses": [],
  "page": 5,
  "summary": "$L(\\theta) = \\prod f(x_i \\mid \\theta)$, simplified with exponent rules into powers of $\\sum x_i$."
 },
 {
  "name": "Support (Probability)",
  "type": "concept",
  "existing": true,
  "parent": "Continuous Random Variables",
  "prereqs": [],
  "uses": [],
  "page": 1,
  "summary": "The set of values with positive probability; a prior's support should equal the parameter space."
 },
 {
  "name": "Kernel of a Distribution",
  "type": "concept",
  "existing": false,
  "parent": "Posterior Distribution",
  "prereqs": [
   "Beta Distribution",
   "Gamma Distribution"
  ],
  "uses": [],
  "page": 1,
  "summary": "The part of a pdf that depends on the variable, constants dropped. Recognizing a kernel identifies the distribution: $p^{a}(1-p)^{b}$ is Beta$(a+1, b+1)$."
 },
 {
  "name": "Posterior Distribution",
  "type": "concept",
  "existing": true,
  "parent": "Bayesian Approach",
  "prereqs": [
   "Likelihood Function",
   "Prior Distribution",
   "Kernel of a Distribution"
  ],
  "uses": [],
  "page": 2,
  "summary": "$\\pi(\\theta \\mid x) \\propto f(x \\mid \\theta)\\pi(\\theta)$."
 },
 {
  "name": "Beta-Bernoulli Update",
  "type": "concept",
  "existing": true,
  "parent": "Conjugate Prior",
  "prereqs": [
   "Posterior Distribution"
  ],
  "uses": [],
  "page": 4,
  "summary": "Beta$(\\alpha,\\beta)$ prior plus Bernoulli data gives Beta$(\\alpha + \\sum x, \\beta + n - \\sum x)$."
 },
 {
  "name": "Gamma-Poisson Update",
  "type": "concept",
  "existing": true,
  "parent": "Conjugate Prior",
  "prereqs": [
   "Posterior Distribution"
  ],
  "uses": [],
  "page": 5,
  "summary": "Gamma$(\\alpha,\\beta)$ prior plus Poisson data gives Gamma$(\\alpha + \\sum x, \\beta + n)$."
 },
 {
  "name": "Probability distribution",
  "type": "concept",
  "existing": true,
  "parent": "",
  "prereqs": [],
  "summary": ""
 },
 {
  "name": "Gamma and Beta Functions",
  "type": "concept",
  "existing": true,
  "parent": "",
  "prereqs": [],
  "summary": ""
 },
 {
  "name": "Prior Distribution",
  "type": "concept",
  "existing": true,
  "parent": "",
  "prereqs": [],
  "summary": ""
 }
]
```

# Frankenstein problems

Practice set: do these on paper, then check. Discussion 1 first (answers below), then Homework 1 (only final checks given, so the work stays yours).

**Discussion 1, Q1.** Beta prior with mean 1/3 and variance 1/45: find $\pi(\theta)$.
Answer: $s+1 = \frac{(1/3)(2/3)}{1/45} = 10$, so $s = 9$, $\alpha = 3$, $\beta = 6$. $\pi(\theta) = \frac{\theta^2(1-\theta)^5}{B(3,6)}$, with $B(3,6) = \frac{\Gamma(3)\Gamma(6)}{\Gamma(9)} = \frac{2 \cdot 120}{40320} = \frac{1}{168}$. So $\pi(\theta) = 168\,\theta^2(1-\theta)^5$ on $(0,1)$.

**Discussion 1, Q2.** Exponential study times 2, 2.5, 3 hours: likelihood for $\lambda$.
Answer: $L(\lambda) = \lambda^3 e^{-7.5\lambda}$ for $\lambda > 0$. Sketch: rises from 0, peaks at $\lambda = 3/7.5 = 0.4$, then decays toward 0.

**Discussion 1, Q3.** Uniform$[0, 10]$ prior for an exponential rate $\lambda$: reasonable?
Answer: partly. It correctly puts nothing on $\lambda \le 0$, but it gives zero probability to $\lambda > 10$, so no data could ever make the posterior go above 10. It's fine only if rates above 10 per hour are truly impossible.

**Discussion 1, Q4.** $p$ is either 0.1 or 0.2: a reasonable prior?
Answer: a discrete prior on two points, e.g. $\pi(0.1) = \pi(0.2) = 1/2$ (or other weights summing to 1), and $\pi(p) = 0$ elsewhere.

**Discussion 1, Q5.** $\pi(p) = 2(1-p)$ on $[0,1]$: prior mean and variance.
Answer: $E[p] = \int_0^1 2p(1-p)\,dp = 1 - \frac{2}{3} = \frac{1}{3}$. $E[p^2] = \int_0^1 2p^2(1-p)\,dp = \frac{2}{3} - \frac{1}{2} = \frac{1}{6}$. $Var = \frac{1}{6} - \frac{1}{9} = \frac{1}{18}$. (It's Beta$(1,2)$: check $\frac{1 \cdot 2}{9 \cdot 4} = \frac{1}{18}$.)

**Homework 1, checks only.**
- Q1 (Gamma, mean 5, variance 2): your $\beta$ should be 2.5 and your $\alpha$ 12.5.
- Q2 (Beta, mean 2/3, variance 1/48): your $s = \alpha + \beta$ should be $29/3$.
- Q3: the likelihood peaks at $p = 0.6$.
- Q4: your answer should contain $e^{-10\lambda}$ and $\lambda^{\sum x_i}$.
- Q5: think about the support.
