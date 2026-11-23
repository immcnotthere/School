---
type: reference
parent: "[[Kernel of a Distribution]]"
domain: stats
course: "STAT 132"
status: draft
---
# STAT 132 Kernels: memorize these

Your professor (Oct 1): "You may not need to remember the constants, but always memorize the kernels." Cards: [[STAT 132 Cards - Kernels]].

## What a kernel is
The **kernel** is the pdf or pmf with every multiplied factor that does **not** contain the variable you care about thrown away.

Beta pdf, written in $\theta$:
$$\underbrace{\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}}_{\text{no } \theta:\ \text{drop}} \ \underbrace{\theta^{\alpha-1}(1-\theta)^{\beta-1}}_{\text{kernel}}$$

Why it's enough: the dropped part only makes the total area 1 (the normalizing constant). The kernel alone fixes the **shape**, and the shape tells you the family. Write "$\propto$" ("proportional to") when you drop constants.

> [!warning] The kernel depends on which letter is the variable
> In a likelihood, the data are fixed numbers and the **parameter** is the variable, so you keep what contains the parameter. In a pdf of the data, $x$ is the variable. Always ask: "a function of what?"

## Table 1: kernels to recognize a posterior (variable = the parameter)
These are the shapes you match at the end of every Lecture 3 problem.

| Family | Kernel in $\theta$ | Where it lives | Read the parameters off |
| --- | --- | --- | --- |
| Beta($\alpha$, $\beta$) | $\theta^{\alpha-1}(1-\theta)^{\beta-1}$ | $0 \le \theta \le 1$ | $\theta^{a}(1-\theta)^{b}$ is Beta($a+1$, $b+1$) |
| Gamma($\alpha$, $\beta$), rate | $\theta^{\alpha-1}e^{-\beta\theta}$ | $\theta > 0$ | $\theta^{a}e^{-b\theta}$ is Gamma($a+1$, $b$) |
| Exponential($\beta$) | $e^{-\beta\theta}$ | $\theta > 0$ | Gamma(1, $\beta$) |
| Normal($\mu$, $\sigma^2$) | $e^{-\frac{(\theta-\mu)^2}{2\sigma^2}}$ | any $\theta$ | center $\mu$, variance $\sigma^2$ |
| Uniform($a$, $b$) | $1$ (flat) | $a \le \theta \le b$ | the ends |

*Read aloud, Beta: "theta to the alpha minus 1, times 1 minus theta to the beta minus 1." Gamma: "theta to the alpha minus 1, times e to the minus beta theta."*

**The minus-1 trap:** the exponent is one **less** than the parameter. $\theta^{8}(1-\theta)^{2}$ is Beta(9, 3), not Beta(8, 2).

## Table 2: likelihood kernels (variable = the parameter, data fixed)
For a random sample $x_1, \dots, x_n$. Multiply the $n$ factors; same bases add exponents.

| Data model | Likelihood kernel | Summary of the data it uses |
| --- | --- | --- |
| Bernoulli($\theta$) | $\theta^{\sum x_i}(1-\theta)^{n-\sum x_i}$ | number of 1s, $\sum x_i$ |
| Binomial($m$, $\theta$), one count $x$ | $\theta^{x}(1-\theta)^{m-x}$ | successes $x$ out of $m$ |
| Poisson($\lambda$) | $\lambda^{\sum x_i}e^{-n\lambda}$ | total count $\sum x_i$ |
| Exponential($\beta$) | $\beta^{n}e^{-\beta\sum x_i}$ | total time $\sum x_i$ |
| Normal($\mu$, $\sigma^2$ known) | $e^{-\frac{n(\mu-\bar x)^2}{2\sigma^2}}$ | sample mean $\bar x$ |

Dropped as constants: $\binom{m}{x}$ in the Binomial, $\prod x_i!$ in the Poisson, the $\frac{1}{\sqrt{2\pi\sigma^2}}$ factors in the Normal.

## Table 3: the pairs (kernel × kernel = same kernel)
| Prior kernel | × likelihood kernel | = posterior kernel | Posterior |
| --- | --- | --- | --- |
| $\theta^{\alpha-1}(1-\theta)^{\beta-1}$ | $\theta^{y}(1-\theta)^{n-y}$ | $\theta^{\alpha+y-1}(1-\theta)^{\beta+n-y-1}$ | Beta($\alpha+y$, $\beta+n-y$) |
| $\lambda^{\alpha-1}e^{-\beta\lambda}$ | $\lambda^{y}e^{-n\lambda}$ | $\lambda^{\alpha+y-1}e^{-(\beta+n)\lambda}$ | Gamma($\alpha+y$, $\beta+n$) |
| $\beta^{\alpha-1}e^{-b\beta}$ (Gamma prior on an Exponential rate) | $\beta^{n}e^{-\beta y}$ | $\beta^{\alpha+n-1}e^{-(b+y)\beta}$ | Gamma($\alpha+n$, $b+y$) |

Here $y = \sum x_i$. The Normal-Normal pair also works, but matching it needs completing the square; use the formulas in [[STAT 132 Lecture 3 - Posterior Distribution]] §1.7.

## Two worked matches
1. Uniform prior (kernel 1), 8 heads in 10: $1 \times \theta^{8}(1-\theta)^{2} = \theta^{8}(1-\theta)^{2}$. Exponents 8 and 2, add 1 to each: **Beta(9, 3)**.
2. Gamma(3, 2) prior, one hour with 3 customers: $\lambda^{2}e^{-2\lambda} \times \lambda^{3}e^{-\lambda} = \lambda^{5}e^{-3\lambda}$. Power 5, add 1; rate 3: **Gamma(6, 3)**.

## Self-test (cover the tables)
1. Kernel of Beta($\alpha$, $\beta$)?
2. Kernel of Gamma($\alpha$, $\beta$)?
3. $\theta^{3}(1-\theta)^{6}$ is which distribution?
4. $\lambda^{4}e^{-7\lambda}$ is which distribution?
5. Poisson likelihood kernel for $n$ data points?

> [!success]- Answers
> 1. $\theta^{\alpha-1}(1-\theta)^{\beta-1}$. 2. $\theta^{\alpha-1}e^{-\beta\theta}$. 3. Beta(4, 7). 4. Gamma(5, 7). 5. $\lambda^{\sum x_i}e^{-n\lambda}$.
