---
type: reference
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "Kernels"
tags:
  - decks
---
# STAT 132 Cards - Kernels

> [!info] Learn this first
> Read [[STAT 132 Kernels]]. A kernel is the pdf or pmf with every factor that doesn't contain the variable thrown away. Professor (Oct 1): memorize the kernels, not the constants.

## Kernel of a Distribution
| Front | Back | Notes |
| --- | --- | --- |
| What is the kernel of a pdf or pmf? | What is left after dropping every multiplied factor that does not contain the variable. | kernels; concept |
| Why is the kernel enough to name a posterior? | It fixes the shape; the dropped constant only rescales the area to 1. | kernels; concept |
| In a likelihood, which letter is the variable whose factors you keep? | The parameter: the data are fixed numbers. | kernels; concept |

## Beta Distribution
| Front | Back | Notes |
| --- | --- | --- |
| Kernel of Beta($\alpha$, $\beta$) in $\theta$? | $\theta^{\alpha-1}(1-\theta)^{\beta-1}$ on $0 \le \theta \le 1$. *Read aloud: "theta to the alpha minus 1, times 1 minus theta to the beta minus 1."* | kernels; memorize |
| $\theta^{8}(1-\theta)^{2}$ is the kernel of which distribution? | Beta(9, 3): add 1 to each exponent. | kernels; match |
| $\theta^{3}(1-\theta)^{6}$ is the kernel of which distribution? | Beta(4, 7). | kernels; match |
| A kernel is $\theta^{a}(1-\theta)^{b}$. What are its Beta parameters in general? | Beta($a+1$, $b+1$). | kernels; match rule |

## Gamma Distribution
| Front | Back | Notes |
| --- | --- | --- |
| Kernel of Gamma($\alpha$, $\beta$) (rate) in $\theta$? | $\theta^{\alpha-1}e^{-\beta\theta}$ for $\theta > 0$. *Read aloud: "theta to the alpha minus 1, times e to the minus beta theta."* | kernels; memorize |
| $\lambda^{4}e^{-7\lambda}$ is the kernel of which distribution? | Gamma(5, 7). | kernels; match |
| A kernel is $\theta^{a}e^{-b\theta}$. What are its Gamma parameters in general? | Gamma($a+1$, $b$): add 1 to the power, keep the rate. | kernels; match rule |

## Exponential distribution
| Front | Back | Notes |
| --- | --- | --- |
| Kernel of the Exponential($\beta$) pdf in $x$? | $e^{-\beta x}$ for $x > 0$. | kernels; memorize |
| Exponential likelihood kernel in $\beta$ for $n$ data points? | $\beta^{n}e^{-\beta\sum x_i}$. *Read aloud: "beta to the n, times e to the minus beta times the sum of the x's."* | kernels; likelihood |

## Normal distribution
| Front | Back | Notes |
| --- | --- | --- |
| Kernel of Normal($\mu$, $\sigma^2$) in $x$? | $e^{-\frac{(x-\mu)^2}{2\sigma^2}}$. *Read aloud: "e to the minus x minus mu squared over 2 sigma squared."* | kernels; memorize |

## Uniform distribution
| Front | Back | Notes |
| --- | --- | --- |
| Kernel of Uniform($a$, $b$) in $x$? | A constant (flat, 1) on $a \le x \le b$, and 0 outside. | kernels; memorize |

## Bernoulli Distribution
| Front | Back | Notes |
| --- | --- | --- |
| Bernoulli likelihood kernel in $\theta$ for $n$ data points? | $\theta^{\sum x_i}(1-\theta)^{n-\sum x_i}$: successes up top, failures on $(1-\theta)$. | kernels; likelihood |

## Poisson Distribution
| Front | Back | Notes |
| --- | --- | --- |
| Poisson likelihood kernel in $\lambda$ for $n$ data points? | $\lambda^{\sum x_i}e^{-n\lambda}$. The $\prod x_i!$ is dropped: it has no $\lambda$. | kernels; likelihood |
| Which kernel shape do the Poisson likelihood and the Gamma prior share? | $\lambda^{\text{power}}e^{-\text{rate}\cdot\lambda}$. | kernels; conjugacy |

## Conjugate Prior
| Front | Back | Notes |
| --- | --- | --- |
| Uniform prior (kernel 1) and 8 heads in 10 flips. Which posterior? | $\theta^{8}(1-\theta)^{2}$, so Beta(9, 3). | kernels; check |
| Gamma(3, 2) prior, one hour with 3 arrivals (Poisson). Multiply the kernels. | $\lambda^{2}e^{-2\lambda} \times \lambda^{3}e^{-\lambda} = \lambda^{5}e^{-3\lambda}$. *Read aloud: "lambda to the 5, times e to the minus 3 lambda."* | kernels; step |
| Name the posterior with kernel $\lambda^{5}e^{-3\lambda}$. | Gamma(6, 3). | kernels; check |
| Gamma($\alpha$, $b$) prior on an Exponential rate $\beta$, data total $y$ over $n$ points. Which posterior? | Gamma($\alpha+n$, $b+y$). | kernels; check |

# Node map
```json
[
 {"name": "Kernel of a Distribution", "type": "concept", "existing": true, "parent": "", "prereqs": [], "summary": ""},
 {"name": "Beta Distribution", "type": "concept", "existing": true, "parent": "", "prereqs": [], "summary": ""},
 {"name": "Gamma Distribution", "type": "concept", "existing": true, "parent": "", "prereqs": [], "summary": ""},
 {"name": "Exponential distribution", "type": "concept", "existing": true, "parent": "", "prereqs": [], "summary": ""},
 {"name": "Normal distribution", "type": "concept", "existing": true, "parent": "", "prereqs": [], "summary": ""},
 {"name": "Uniform distribution", "type": "concept", "existing": true, "parent": "", "prereqs": [], "summary": ""},
 {"name": "Bernoulli Distribution", "type": "concept", "existing": true, "parent": "", "prereqs": [], "summary": ""},
 {"name": "Poisson Distribution", "type": "concept", "existing": true, "parent": "", "prereqs": [], "summary": ""},
 {"name": "Conjugate Prior", "type": "concept", "existing": true, "parent": "", "prereqs": [], "summary": ""}
]
```

# Frankenstein problems
None: see the check cards.
