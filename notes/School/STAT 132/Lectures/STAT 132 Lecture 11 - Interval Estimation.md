---
type: lecture
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
lecture: 11
week: 6
source: "School/STAT 132/Lectures/stat132-lec11.pdf"
status: draft
mastery: 0
aliases:
  - "STAT 132 L11"
  - "STAT 132 Lecture 11"
prereqs:
  - "[[t Distribution of the Sample Mean]]"
  - "[[Sample Variance Chi-Square Distribution]]"
  - "[[Quantile Function]]"
related:
  - "[[Confidence Interval]]"
  - "[[Pivotal Quantity]]"
  - "[[Confidence Interval from a Pivotal]]"
  - "[[Interpretation of Confidence Intervals]]"
  - "[[Confidence Interval for the Mean of a Normal Distribution]]"
  - "[[Point Estimate vs Interval Estimate]]"
  - "[[Posterior Distribution]]"
  - "[[STAT 132 Discussion 6]]"
---
# STAT 132 Lecture 11: Interval Estimation

Handout: [[stat132-lec11.pdf]] (8 pages). Practice set: [[STAT 132 Discussion 6]] (4 problems, all on this lecture). **Midterm 2 is Tue 11-10.**

How to use this: quote blocks (>) are the handout, copied word for word and checked against the page images (handout typos kept, flagged by Claude). Anything labelled **Claude** is mine, not the handout. Each has a `My correction` slot under it. Answers are folded: do the example on paper, then open the fold.

---

## New skills from this lecture (the checklist)

Before L11 you could produce a **point estimate**: one number ($\bar X$, an MLE, a posterior mean). L11 turns that into an **interval**. These are the things you now have to be able to *do*. Tick one off when you can do it on paper without looking.

| #   | Skill: given...                                                  | ...you produce                                                                                                                                                                                             | Practice                | Built on (old skill)                                                        |
| --- | ---------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- | --------------------------------------------------------------------------- |
| 1   | a confidence level like 95%                                      | $\alpha = 0.05$, $\alpha/2 = 0.025$, $1-\alpha/2 = 0.975$                                                                                                                                                  | every example           | arithmetic                                                                  |
| 2   | a level and a distribution ($N(0,1)$, $t_{n-1}$, $\chi^2_{n-1}$) | the quantile you need: $z_{0.975}=1.96$, $t_{25,\,0.975}=2.060$, $\chi^2_{25,\,0.025}=13.12$, $\chi^2_{25,\,0.975}=40.65$. Also read $\Phi^{-1}\!\left(\frac{1+\gamma}{2}\right)$ as the same $z$          | Ex 2.1, 2.2, 4.2, D6 Q2 | [[Quantile Function]], [[Standard Normal CDF (Φ)]]                          |
| 3   | $\bar X$, known $\sigma^2$, $n$                                  | **z-interval** $\bar X \pm z_{1-\alpha/2}\,\sigma/\sqrt n$ (turn variance into sd first!)                                                                                                                  | Ex 2.1                  | [[Standard Error]], [[Variance of the Sample Mean]]                         |
| 4   | $\bar X$, $S^2$, $n$ (σ unknown)                                 | **t-interval** $\bar X \pm t_{n-1,1-\alpha/2}\,S/\sqrt n$, df $= n-1$                                                                                                                                      | Ex 2.2                  | [[t Distribution of the Sample Mean]]                                       |
| 5   | a statement $P(-c < Q < c) = 1-\alpha$                           | rearrange the inequality until $\theta$ is alone in the middle (the proofs of Thm 2.1, 2.2)                                                                                                                | Proofs, D6 Q2           | algebra on inequalities                                                     |
| 6   | a computed interval like $(1.11, 1.49)$                          | the correct sentence: "95% of intervals built this way cover $\mu$", NOT "$P(\mu \in (1.11,1.49)) = 0.95$"                                                                                                 | Section 3, R code       | [[Interpretation of Confidence Intervals]]                                  |
| 7   | a model and a parameter                                          | a **pivotal quantity** $Q(\boldsymbol X,\theta)$ whose distribution has no $\theta$ in it                                                                                                                  | Def 4.1, D6 Q4          | [[Pivotal Quantity]]                                                        |
| 8   | the pivot $\frac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1}$          | a **CI for $\sigma^2$**: $\left(\frac{(n-1)S^2}{\chi^2_{n-1,1-\alpha/2}},\ \frac{(n-1)S^2}{\chi^2_{n-1,\alpha/2}}\right)$. Note the ends SWAP when you take reciprocals, and the interval is not symmetric | Ex 4.1, 4.2             | [[Sample Variance Chi-Square Distribution]]                                 |
| 9   | exponential data with mean $\mu$                                 | pivot $\frac1\mu\sum X_i \sim \text{Gamma}(n,1)$ and the CI $\left(\frac{\sum X_i}{g_{1-\alpha/2}}, \frac{\sum X_i}{g_{\alpha/2}}\right)$                                                                  | D6 Q4                   | [[Gamma Distribution]], [[Exponential distribution]]                        |
| 10  | a target interval length                                         | the sample size $n$: solve $2 z\,\sigma/\sqrt n < \text{length}$ for $n$, round UP                                                                                                                         | D6 Q3                   | algebra                                                                     |
| 11  | independent normals                                              | a $t$ variable: $\dfrac{Z}{\sqrt{V/k}} \sim t_k$ with $Z \sim N(0,1)$, $V \sim \chi^2_k$; scale sums so they are standard                                                                                  | D6 Q1                   | [[t Distribution]], [[Sum of Squares of iid Standard Normal Is Chi-Square]] |
| 12  | a posterior $\pi(\theta \mid \boldsymbol X)$                     | a **credible interval**: its $\alpha/2$ and $1-\alpha/2$ quantiles. Here "95% chance $\theta$ is inside" IS allowed                                                                                        | Section 5               | [[Posterior Distribution]]                                                  |
| 13  | the R code in section 3                                          | say what each line does (`qt`, `rnorm`, `replicate`, `colMeans`) and why ~5 of 100 lines are red                                                                                                           | Section 3               | R basics                                                                    |

**The one idea under skills 3, 4, 8, 9 (Claude):** every interval in this lecture is the same three-step recipe. (1) find a quantity with a known, $\theta$-free distribution, (2) cut off $\alpha/2$ in each tail with quantiles, (3) solve the inequality for $\theta$. Learn the recipe once; the four intervals are just four pivots.

> [!note]- My correction
> 

---

## 1. Background and Definition
> So far, the only type of estimates that we have talked about are point estimates. Point estimates can serve as a good guess for the population parameter, but they will almost never actually be equal to the true population parameter due to the randomness of the sample.
>
> Today, we will talk about interval estimates, specifically confidence intervals. The basic idea is to construct an interval with lower and upper bounds that are likely to contain the parameter value.

### 1.1 Definition
> **Definition 1.1.** Let $X_1, \dots, X_n$ be a random sample from some population that depends on the parameter $\theta$. Let $L$ and $U$ be two statistics calculated from the data (with $L < U$). Then if
> $$\mathbb{P}(L < \theta < U) = 1 - \alpha$$
> the random interval $(L, U)$ is called a $1 - \alpha$ confidence interval. For example, if $\alpha = 0.05$, this would result in a 0.95 or 95% confidence interval.

**Claude's explanation:** read the probability carefully: $\theta$ is a fixed number, $L$ and $U$ are the random things (they are statistics, so they change from sample to sample). The statement says "the random interval lands on top of $\theta$ with probability $1-\alpha$." Concept notes: [[Confidence Interval]], [[Point Estimate vs Interval Estimate]].

> [!note]- My correction
> 

---

## 2. Confidence Intervals for the Mean of a Normal Distribution
### 2.1 Known Variance
> **Theorem 2.1.** Let $X_1, X_2, \dots, X_n \overset{iid}{\sim} N(\mu, \sigma^2)$ with known $\sigma$. Then a $1 - \alpha$ confidence interval for $\mu$ can be constructed as
> $$\bar X \pm z_{1-\alpha/2} \cdot \frac{\sigma}{\sqrt n},$$
> where $z_{1-\alpha/2}$ is the $1 - \alpha$ quantile of the standard normal distribution.

**Claude (handout typo):** it should say the $1-\alpha/2$ quantile. For 95%, you want $z_{0.975} = 1.96$, not $z_{0.95} = 1.645$. Half of $\alpha$ goes in each tail.

> **Proof.** Thm. 2.1
> *(blank in the handout: done in class)*

**Claude's proof (fill-in for the blank):**
1. Given: $\bar X \sim N\!\left(\mu, \frac{\sigma^2}{n}\right)$ ([[Variance of the Sample Mean]]). Standardize: $Z = \dfrac{\sqrt n(\bar X - \mu)}{\sigma} \sim N(0,1)$. This is the pivot: no $\mu$ in $N(0,1)$.
2. Cut the tails: by symmetry of $N(0,1)$, $\mathbb P\!\left(-z_{1-\alpha/2} < Z < z_{1-\alpha/2}\right) = 1-\alpha$.
3. What changes: substitute $Z$ and solve for $\mu$, one operation at a time:
$$-z_{1-\alpha/2} < \frac{\sqrt n(\bar X-\mu)}{\sigma} < z_{1-\alpha/2}$$
$$\xrightarrow{\ \times\,\sigma/\sqrt n\ } \quad -z_{1-\alpha/2}\frac{\sigma}{\sqrt n} < \bar X - \mu < z_{1-\alpha/2}\frac{\sigma}{\sqrt n}$$
$$\xrightarrow{\ -\bar X\ } \quad -\bar X - z_{1-\alpha/2}\frac{\sigma}{\sqrt n} < -\mu < -\bar X + z_{1-\alpha/2}\frac{\sigma}{\sqrt n}$$
$$\xrightarrow{\ \times(-1),\ \text{flip both signs}\ } \quad \bar X - z_{1-\alpha/2}\frac{\sigma}{\sqrt n} < \mu < \bar X + z_{1-\alpha/2}\frac{\sigma}{\sqrt n}$$
4. The event did not change, only its description, so its probability is still $1-\alpha$. So $L = \bar X - z\,\sigma/\sqrt n$, $U = \bar X + z\,\sigma/\sqrt n$. $\square$

> [!note]- My correction
> 

> **Example 2.1.** Suppose $X_1, \dots, X_n$ represent a random sample of daily rainfall measurements for Santa Cruz in the month of February, where $n = 26$. After collecting the data, you calculate $\bar X = 1.3$ inches. Suppose you know that rainfall in February is normally distributed with a variance of $\frac14$, but you don't know what the daily average rainfall is. Use this information to construct a 95% confidence interval for the average daily rainfall in February.

> [!example]- Answer (Claude, checked in scipy)
> - $\alpha = 0.05$, so $z_{0.975} = 1.960$.
> - Trap: the handout gives the **variance** $\frac14$. So $\sigma = \sqrt{1/4} = 0.5$.
> - Standard error: $\dfrac{\sigma}{\sqrt n} = \dfrac{0.5}{\sqrt{26}} = \dfrac{0.5}{5.099} = 0.0981$.
> - Margin: $1.960 \times 0.0981 = 0.192$.
> - Interval: $1.3 \pm 0.192 = (1.108,\ 1.492)$ inches.

> [!note]- My correction
> 

### 2.2 Unknown Variance
> **Theorem 2.2.** Let $X_1, X_2, \dots, X_n \overset{iid}{\sim} N(\mu, \sigma^2)$ with unknown $\sigma$. Then a $1 - \alpha$ confidence interval for $\mu$ can be constructed as
> $$\bar X \pm t_{n-1,1-\alpha/2} \cdot \frac{S}{\sqrt n}.$$
> where $t_{n-1,1-\alpha/2}$ is the $1 - \alpha$ quantile of the t-distribution with $n - 1$ degrees of freedom, and
> $$S = \sqrt{S^2} = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(X_i - \bar X)^2}.$$

**Claude:** same typo as Thm 2.1: it is the $1-\alpha/2$ quantile. And note $S^2$ divides by $n-1$ (the unbiased one), not $n$ (the MLE from L5/L6).

> **Proof.** Thm. 2.2
> *(blank in the handout)*

**Claude's proof:** identical to 2.1 with one swap. Since $\sigma$ is unknown you cannot compute $Z$, so replace $\sigma$ by $S$. That changes the distribution: $T = \dfrac{\sqrt n(\bar X - \mu)}{S} \sim t_{n-1}$ ([[t Distribution of the Sample Mean]], which uses [[Independence of Sample Mean and Sample Variance]]). $t_{n-1}$ is symmetric and has no $\mu$ or $\sigma$ in it, so the same four algebra steps give $\bar X \pm t_{n-1,1-\alpha/2}\,S/\sqrt n$. $\square$

> [!note]- My correction
> 

> **Example 2.2.** Suppose $X_1, \dots, X_n$ represent a random sample of daily rainfall measurements for Santa Cruz in the month of February, where $n = 26$. After collecting the data, you calculate $\bar X = 1.3$ inches and $S^2 = 0.45$. Suppose you know that rainfall in February is normally distributed but you don't know what the daily average rainfall is or the variance. Use this information to construct a 95% confidence interval for the average daily rainfall in February.

> [!example]- Answer (Claude, checked in scipy)
> - df $= n - 1 = 25$, $t_{25,\,0.975} = 2.060$ (R: `qt(0.975, 25)`).
> - $S = \sqrt{0.45} = 0.6708$. Standard error $= 0.6708/\sqrt{26} = 0.1316$.
> - Margin: $2.060 \times 0.1316 = 0.271$.
> - Interval: $1.3 \pm 0.271 = (1.029,\ 1.571)$ inches.
> - Compare with Ex 2.1: wider, because $t$ has fatter tails than $z$ (2.060 > 1.960) and here $S > \sigma$.

> [!note]- My correction
> 

---

## 3. Interpretation of Confidence Intervals
> - $\mathbb P(L < \theta < U) = 1 - \alpha$ is a statement about the random variables $L$ and $U$.
> - Once we have computed specific values using the data, $L = l$ and $U = u$, these are no longer random.
>     - After computing the specific interval $(L = l, U = u)$, we can no longer make probability statements about the interval. It either contains the parameter or it doesn't (it is no longer random).
> - Instead, we can interpret the long run frequency of intervals that cover the parameter—if we took many different samples and computed confidence intervals for each sample, we would expect about $1 - \alpha$ percent of these to cover the true parameter.

```r
set.seed(123)
n <- 26 # Sample size
mu <- 5.1      # True mean
sigma <- 1.6       # True standard deviation
num_sim <- 100

# Simulating confidence intervals
samples <- replicate(num_sim, rnorm(n, mean = mu, sd = sigma))
sample_means <- colMeans(samples)
sample_sds <- apply(samples, 2, sd)
margin_of_error <- qt(0.975, df=n-1) * sample_sds / sqrt(n)

# Creating data frame
ci_data <- data.frame(
  lower = sample_means - margin_of_error,
  upper = sample_means + margin_of_error,
  contains_mu = (sample_means - margin_of_error <= mu) & (sample_means +
    margin_of_error >= mu)
)

# Plot
library(ggplot2)
ggplot(ci_data, aes(y=1:num_sim, x=lower, xend=upper, color=contains_mu)) +
  geom_segment(aes(yend=1:num_sim), size=1) +
  geom_vline(xintercept=mu, linetype="dashed") +
  labs(title="Simulated 95% Confidence Intervals", x="Mean", y="Sample") +
  theme_minimal()
```
*(Handout figure: 100 horizontal intervals around a dashed line at $\mu = 5.1$; a handful are red, `contains_mu = FALSE`.)*

**Claude, line by line:** `replicate(100, rnorm(26, ...))` makes a 26 by 100 matrix, one column per pretend sample. `colMeans` gives 100 values of $\bar X$; `apply(..., 2, sd)` gives 100 values of $S$. `qt(0.975, df=25)` is $t_{25,0.975}$, so `margin_of_error` is the Thm 2.2 margin for each sample. `contains_mu` asks "is $l \le \mu \le u$?" for each one. Expect about 5 of 100 FALSE. The point: the 95% belongs to the **procedure** (the code), not to any one red or blue line. Concept note: [[Interpretation of Confidence Intervals]].

> [!note]- My correction
> 

---

## 4. Confidence Intervals for Other Parameters
> Notice that when constructing a confidence interval for $\mu$ using data from a normal population, we used one of the following facts:
> - For $\sigma^2$ known – $\dfrac{\sqrt n(\bar X - \mu)}{\sqrt{\sigma^2}} \sim \mathrm N(0, 1)$
> - For $\sigma^2$ known – $\dfrac{\sqrt n(\bar X - \mu)}{\sqrt{S^2}} \sim t_{n-1}$
>
> Notice that both of these distributions do not depend on the population parameter $\mu$! This allowed us to find appropriate quantiles of the distribution, and then rearrange the probability inequality to isolate $\mu$. This same general strategy can work for finding many other confidence intervals.

**Claude (handout typo):** the second bullet should say "For $\sigma^2$ **unknown**".

> **Definition 4.1.** Let $\boldsymbol X = (X_1, \dots, X_n)$ be a random sample from some population that depends on the parameter $\theta$. If $Q(\boldsymbol X, \theta)$ is a function of the data/parameter with a distribution does not depend on $\theta$ (i.e., the distribution is the same for any value of $\theta$), then $Q(\boldsymbol X, \theta)$ is called a pivotal quantity.
>
> If you can find a pivotal quantity involving your parameter of interest, this gives you a way to construct a confidence interval.
> 1. Find $c_1$ and $c_2$ such that $\mathbb P(c_1 \le Q(\boldsymbol X, \theta) \le c_2) = 1-\alpha$. These will correspond to quantiles of the distribution of $Q(\boldsymbol X, \theta)$.
> 2. Find a way to isolate the parameter $\theta$ from the pivotal quantity. In other words find $g(\cdot)$ such that $g(Q(\boldsymbol X, \theta)) = \theta$.
> 3. Rearrange your probability statement to result in a confidence interval: $\mathbb P(g(c_1) \le g(Q(\boldsymbol X, \theta) \le g(c_2)) = \mathbb P(g(c_1) \le \theta \le g(c_2)) = 1 - \alpha$
>
> Note: The constants $c_1$ and $c_2$ are not unique. In practice, we often let $c_1$ correspond to the $\frac{\alpha}{2}$ quantile of the distribution and $c_2$ correspond to the $1 - \frac{\alpha}{2}$ quantile. This results in what is called an equal tailed interval.

**Claude's explanation:**
- A pivot contains $\theta$ (so it can be solved for $\theta$) but its *distribution* does not (so you can look up its quantiles without knowing $\theta$). Both conditions are needed. $\bar X$ alone is not a pivot: its distribution $N(\mu, \sigma^2/n)$ has $\mu$ in it.
- Step 3 as printed is only right when $g$ is **increasing**. If $g$ is decreasing (like $g(q) = \frac{(n-1)S^2}{q}$ in Ex 4.1), the inequality flips and you get $g(c_2) \le \theta \le g(c_1)$. This is exactly where exam answers go wrong.
- Concept notes: [[Pivotal Quantity]], [[Confidence Interval from a Pivotal]].

> [!note]- My correction
> 

> **Example 4.1.** Suppose that $X_1, \dots, X_n$ form a random sample from the normal distribution with unknown mean $\mu$ and unknown variance $\sigma^2$. Find a $1 - \alpha$ confidence interval for $\sigma^2$.

> [!example]- Answer (Claude)
> 1. **Pivot:** $Q = \dfrac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1}$ ([[Sample Variance Chi-Square Distribution]], Lecture 8). No $\sigma^2$ in $\chi^2_{n-1}$.
> 2. **Quantiles:** $\mathbb P\!\left(\chi^2_{n-1,\alpha/2} \le \dfrac{(n-1)S^2}{\sigma^2} \le \chi^2_{n-1,1-\alpha/2}\right) = 1-\alpha$. $\chi^2$ is not symmetric, so you need two different numbers, not $\pm c$.
> 3. **Isolate $\sigma^2$:** take reciprocals (all positive, so the inequalities flip):
> $$\frac{1}{\chi^2_{n-1,1-\alpha/2}} \le \frac{\sigma^2}{(n-1)S^2} \le \frac{1}{\chi^2_{n-1,\alpha/2}}$$
> then multiply by $(n-1)S^2 > 0$:
> $$\boxed{\left(\frac{(n-1)S^2}{\chi^2_{n-1,\,1-\alpha/2}},\ \frac{(n-1)S^2}{\chi^2_{n-1,\,\alpha/2}}\right)}$$
> The **upper** quantile goes in the **lower** endpoint.

> [!note]- My correction
> 

> **Example 4.2.** Suppose $X_1, \dots, X_n$ represent a random sample of daily rainfall measurements for Santa Cruz in the month of February, where $n = 26$. After collecting the data, you calculate $\bar X = 1.3$ inches and $S^2 = 0.45$. Suppose you know that rainfall in February is normally distributed but you don't know what the daily average rainfall is or the variance. Use this information to construct a 95% confidence interval for the variance of daily rainfall in February.

> [!example]- Answer (Claude, checked in scipy)
> - $(n-1)S^2 = 25 \times 0.45 = 11.25$.
> - $\chi^2_{25,\,0.025} = 13.120$ and $\chi^2_{25,\,0.975} = 40.646$ (R: `qchisq(c(.025,.975), 25)`).
> - Interval: $\left(\dfrac{11.25}{40.646},\ \dfrac{11.25}{13.120}\right) = (0.277,\ 0.857)$ square inches.
> - Check: $S^2 = 0.45$ is inside, but not in the middle (the interval stretches right). That is normal for a $\chi^2$ interval.
> - For $\sigma$ (not $\sigma^2$): take square roots of both ends, $(0.526,\ 0.926)$ inches.

> [!note]- My correction
> 

---

## 5. Bayesian Credible Intervals
> Interval estimation in the Bayesian setting is straightforward. We can work directly with the posterior distribution to construct an interval that has $1 - \alpha$ for the parameter. In this case this is called a credible interval.
>
> **Definition 5.1.** Suppose that $\boldsymbol X = (X_1, \dots, X_n)$ form a random sample from some distribution with parameter $\theta$. Then, for values $L$ and $U$ such that
> $$\mathbb P(L \le \theta \le U \mid \boldsymbol X) = \int_L^U \pi(\theta \mid \boldsymbol X)\,d\theta = 1 - \alpha$$
> the interval $(L, U)$ is called a $1 - \alpha$ credible interval.
>
> Note: Again, the bounds $L$ and $U$ are not unique, but it is common to use equal-tail credible intervals.

**Claude's explanation:**
- In Bayes, $\theta$ is the random thing and the data are fixed (you have conditioned on them). So "there is a 95% probability $\theta$ is in $(L, U)$" is a correct sentence here, the exact sentence that is wrong for a confidence interval. That contrast is a likely exam question.
- Recipe: get the posterior (Lectures 2-3, [[Posterior Distribution]]), then take its $\alpha/2$ and $1-\alpha/2$ quantiles. Example: posterior $\text{Beta}(8, 4)$ gives the 95% equal-tail credible interval `qbeta(c(.025,.975), 8, 4)`.
- No pivot needed: the posterior already has a known distribution, so you skip steps 1-3 of section 4.

> [!note]- My correction
> 

---

## Midterm 2 quick sheet (Claude)
| Parameter | Pivot | Its distribution | 1 - α interval |
|---|---|---|---|
| $\mu$, σ known | $\dfrac{\sqrt n(\bar X-\mu)}{\sigma}$ | $N(0,1)$ | $\bar X \pm z_{1-\alpha/2}\dfrac{\sigma}{\sqrt n}$ |
| $\mu$, σ unknown | $\dfrac{\sqrt n(\bar X-\mu)}{S}$ | $t_{n-1}$ | $\bar X \pm t_{n-1,1-\alpha/2}\dfrac{S}{\sqrt n}$ |
| $\sigma^2$ | $\dfrac{(n-1)S^2}{\sigma^2}$ | $\chi^2_{n-1}$ | $\left(\dfrac{(n-1)S^2}{\chi^2_{n-1,1-\alpha/2}}, \dfrac{(n-1)S^2}{\chi^2_{n-1,\alpha/2}}\right)$ |
| exponential mean $\mu$ | $\dfrac{1}{\mu}\sum X_i$ | $\text{Gamma}(n, 1)$ | $\left(\dfrac{\sum X_i}{g_{1-\alpha/2}}, \dfrac{\sum X_i}{g_{\alpha/2}}\right)$ |
| any $\theta$ (Bayes) | none | posterior | posterior quantiles $\alpha/2$, $1-\alpha/2$ |

Interval length for the z-interval: $2 z_{1-\alpha/2}\,\sigma/\sqrt n$. Halving the length needs 4 times the data.
