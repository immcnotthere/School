---
type: lecture
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
week: 4
source: "School/STAT 132/Readings/stat132-reading04.pdf"
status: draft
mastery: 0
aliases:
  - "STAT 132 Reading 4"
  - "STAT 132 Reading04"
prereqs:
  - "[[Maximum Likelihood Estimation (MLE)]]"
  - "[[Binomial Distribution]]"
  - "[[Expectation and Variance]]"
related:
  - "[[STAT 132 Lecture 6 - Maximum Likelihood Properties]]"
  - "[[STAT 132 Lecture 7 - Sampling Distributions]]"
  - "[[Sampling Distribution]]"
  - "[[Standard Error]]"
  - "[[STAT 132 Week 4]]"
---
# STAT 132 Reading 04: MLE Properties (ch. 6) and Sampling Distributions (ch. 7)

Source: [[stat132-reading04.pdf]] (31 pages, book pages 98-128). Chapter 6 = [[STAT 132 Lecture 6 - Maximum Likelihood Properties|Lecture 6]]. Chapter 7 = [[STAT 132 Lecture 7 - Sampling Distributions|Lecture 7]]. Week hub: [[STAT 132 Week 4]].

How to use this: this is a tutorial, not a full copy. Quote blocks (>) are the reading's exact words, used for every definition and result. Everything labelled **Claude** is mine and has a `My correction` slot. Each R block from the reading is copied exactly, followed by the Python port that ran on this laptop and its real output. R is not installed here; to run the R as written, use `! sudo pacman -S r`.

---

## Chapter 6 in one screen
The full worked versions are in [[STAT 132 Lecture 6 - Maximum Likelihood Properties|Lecture 6]]. Here are the reading's own statements.

> Lecture 6 studies three properties that answer these questions: invariance, consistency, and bias. These properties describe different aspects of an estimator. An estimator can be consistent while still being biased for every finite sample size.

> The invariance property of maximum likelihood estimation says that an MLE of $\eta$ is
> $$\hat\eta = g(\hat\theta).$$

> An estimator is consistent if it approaches the true parameter in probability as the sample size increases. [...] for every fixed tolerance $\varepsilon > 0$,
> $$P_{\theta_T}\big(|\hat\theta_n - \theta_T| > \varepsilon\big) \longrightarrow 0 \quad \text{as } n \longrightarrow \infty.$$

> Consistency does not mean that every larger sample gives a closer estimate. Estimates can fluctuate as new observations arrive. It also does not mean that a particular finite sample size guarantees a small error.

> The bias of an estimator $\hat\theta$ is
> $$\text{Bias}_\theta(\hat\theta) = E_\theta[\hat\theta] - \theta.$$

> Unbiasedness does not mean that an estimate from one sample equals the true parameter. It describes the center of the estimator's sampling distribution.

> Maximum likelihood estimators need not be unbiased. Also, applying a nonlinear function to an unbiased estimator does not generally preserve unbiasedness. Invariance tells us how to find an MLE of a transformed parameter, but it does not tell us its expected value.

**Claude, notation the reading introduces:** $\eta$ (eta) = the quantity you want, $\eta = g(\theta)$. The subscript in $E_\theta$ and $P_{\theta_T}$ names *which true parameter the imaginary repeated samples come from*. It is not "given the data". In code, `E_theta[...]` is `mean(f(sample(theta)) for many samples)`, with `theta` passed in as an argument.

> [!note]- My correction
> 

### Reading's table 6.6 (exact)
| Property | Question it answers |
|---|---|
| Invariance | How do we find the MLE of a function of the parameter? |
| Consistency | Does the probability of a fixed estimation error tend to zero as the sample grows? |
| Unbiasedness | Does the estimator equal the parameter on average over repeated samples? |

> An unbiased estimator can also have substantial variability. When comparing estimators, we should consider both their average error and their spread.

That sentence is the lead-in to [[Mean Squared Error (MSE)]] and [[MSE Bias-Variance Decomposition]].

### R code 6.5 (verbatim) and its Python port
```r
set.seed(132)
true_endpoint <- 10
sample_sizes <- c(5, 20, 100)

par(mfrow = c(1, 3))

for (n in sample_sizes) {
  maxima <- replicate(
    5000,
    max(runif(n, min = 0, max = true_endpoint))
  )

    hist(
      maxima,
      breaks = seq(0, 10, by = 0.25),
      probability = TRUE,
      col = "skyblue",
      border = "white",
      xlim = c(0, 10.5),
      xlab = "Estimated endpoint",
      main = paste("Sample size =", n)
    )
    abline(v = true_endpoint, col = "firebrick", lwd = 2, lty = 2)
    abline(v = n * true_endpoint / (n + 1), col = "steelblue", lwd = 2)
}

par(mfrow = c(1, 1))
```

**Claude, the R as plain steps:** `replicate(5000, ...)` = a for-loop that runs the `...` 5000 times and keeps each result. `runif(n, 0, 10)` = n random draws from $U(0,10)$. `max(...)` = the MLE. `hist(..., probability = TRUE)` = histogram scaled to a density. `abline(v = ...)` = a vertical line. In numpy, `rng.uniform(0, 10, size=(5000, n)).max(axis=1)` does the whole loop in one line: 5000 rows of n draws, max of each row. The run is in `w4_ch6_mle_properties.py` (see [[STAT 132 Lecture 6 - Maximum Likelihood Properties#5. Run it locally (Claude)|Lecture 6, section 5]]).

![[w4-fig6.1-uniform-max.png]]

> The simulation illustrates the properties, while the probability calculation and expectation calculation establish them mathematically.

---

## Chapter 7: Sampling Distributions

### 7.1 A statistic has a distribution
> A statistic is a function of the data and known quantities:
> $$T = t(X_1, X_2, \ldots, X_n).$$
> Before the data are observed, the observations are random. Applying a calculation to them produces another random quantity. The probability distribution of that quantity is the **sampling distribution** of the statistic.

> One way to picture a sampling distribution is to imagine the following process:
> 1. Keep the population model and its parameter values fixed.
> 2. Draw a random sample of size $n$.
> 3. Calculate the statistic from that sample.
> 4. Repeat with a new sample of the same size, recording one statistic each time.
>
> The distribution of the recorded statistics would approximate the sampling distribution.

**Claude, the same 4 steps as a function** (this is the core idea of the chapter; everything after it is one case):
```python
def sampling_distribution(draw_sample, statistic, reps, rng):
    # 1. the model is fixed inside draw_sample (parameters baked in)
    # 2. draw a sample   3. compute T   4. repeat, keep every T
    return [statistic(draw_sample(rng)) for _ in range(reps)]

# example: sample proportion of 24 Bernoulli(0.6) scans
props = sampling_distribution(lambda r: r.binomial(1, 0.6, 24), np.mean, 10_000, rng)
```
- Lowercase $t$ = the rule (the function). Capital $T$ = its random output. That is the same split as [[Estimator vs Estimate]].
- Concept notes: [[Statistic (inference)]], [[Sampling Distribution]].

> [!note]- My correction
> 

> A statistic cannot require an unknown parameter as an input to its calculation. We must be able to calculate it from the data. However, its sampling distribution can depend on an unknown parameter.

**Claude:** in code, `statistic(sample)` takes only data. `draw_sample` has the true $p$ or $\theta$ inside it. So the *output distribution* depends on that hidden argument even though the statistic never reads it.

#### The three distributions to keep separate (reading's table, exact)
| Distribution | What varies? | What does it describe? |
|---|---|---|
| Population or sampling model | An individual observation | The data-generating process under specified parameters |
| Sampling distribution of a statistic | The statistic across repeated samples | The behavior of an estimation or summary rule |
| Posterior distribution | The parameter, given observed data | Bayesian uncertainty about the parameter after updating |

> In a frequentist sampling distribution, the parameter is held fixed and the statistic varies. In a posterior distribution, the observed data are held fixed and uncertainty is described over parameter values.

Link back: [[Posterior Distribution]], [[Frequentist Approach]].

> [!note]- My correction
> 

**Fill in:** which of the three is a histogram of 0s and 1s from one sample, and which is a histogram of one $\hat p$ per sample?
- 

---

### 7.2 Example: first-pass barcode scans
> A library is testing a barcode scanner for its return station. Let $p$ be the probability that it reads a book's barcode on the first pass. Suppose the outcomes for independently selected books can be modeled as Bernoulli observations with the same probability $p$.
> An initial trial uses 16 books. The staff want to understand how often the observed first-pass rate would reach at least 14 out of 16 if the scanner's true success probability were 0.75.

**Claude, as a data pipeline:**

| Step | Given | Do | Get |
|---|---|---|---|
| 1 | $X_i \overset{iid}{\sim}$ [[Bernoulli Distribution\|Bernoulli]]$(p)$, 1 = scanned first try | add them up | $K = \sum_{i=1}^n X_i$ |
| 2 | $K$ is a sum of $n$ independent same-$p$ Bernoullis | name it | $K \sim$ [[Binomial Distribution\|Bin]]$(n, p)$ |
| 3 | $K$ | divide by $n$ | $T = \hat p = K/n$ |
| 4 | the pmf of $K$ | relabel each count $k$ as the proportion $k/n$; the probabilities stay | the pmf of $\hat p$ |

> $$P\left(T = \frac{k}{n}\right) = P(K = k) = \binom{n}{k} p^k (1-p)^{n-k}, \quad k = 0, 1, \ldots, n.$$
> This is the exact sampling distribution of $T$. Its possible values are
> $$0, \frac{1}{n}, \frac{2}{n}, \ldots, 1.$$

> For the scanner trial, the possible rates are multiples of $1/16 = 0.0625$. An observed rate of exactly 0.80 cannot occur in a sample of 16 books.

#### 7.2.1 The calculation
> $$P(\hat p \ge 0.875) = P(K \ge 14) = \sum_{k=14}^{16} \binom{16}{k} (0.75)^k (0.25)^{16-k} \approx 0.197.$$

```r
pbinom(13, size = 16, prob = 0.75, lower.tail = FALSE)
```
```text
[1] 0.197111
```

> The R calculation asks for the probability of more than 13 successes, which includes 14, 15, and 16.

**Claude, R to Python:** `pbinom(13, 16, 0.75, lower.tail = FALSE)` is $P(K > 13)$, which is `scipy.stats.binom.sf(13, 16, 0.75)` (`sf` = "survival function" = $1 - \text{CDF}$). Our run: `0.197111`. Matches.

> The calculation gives a probability for the sample outcome under an assumed $p$. It does not give the probability that $p$ equals 0.75.

> [!note]- My correction
> 

#### 7.2.2 Center and spread
> $$E[T] = E\left[\frac{K}{n}\right] = \frac{1}{n}E[K] = p, \qquad \text{Var}(T) = \text{Var}\left(\frac{K}{n}\right) = \frac{1}{n^2}\text{Var}(K) = \frac{p(1-p)}{n}.$$
> Recall that multiplying a random variable by a constant multiplies its mean by that constant and its variance by the square of the constant.

Rule used: [[Expectation and Variance]] ($E[cX] = cE[X]$, $\text{Var}(cX) = c^2\text{Var}(X)$). $E[T] = p$, so $\hat p$ is [[Unbiased Estimator|unbiased]].

---

### 7.3 Standard error
> The **standard error** of a statistic is the standard deviation of its sampling distribution. It measures how much the statistic varies from one sample to another under the model.
> $$\text{SE}(T) = \sqrt{\text{Var}(T)}.$$

> $$\text{SE}(\hat p) = \sqrt{\frac{p(1-p)}{n}}.$$
> For the scanner trial, if the true first-pass probability is $p = 0.75$ and $n = 16$, then
> $$\text{SE}(\hat p) = \sqrt{\frac{0.75(0.25)}{16}} \approx 0.108.$$

> For a sample mean or proportion, multiplying the sample size by four divides the standard error by two. Doubling sample size does not halve the standard error, because the denominator contains $\sqrt{n}$ rather than $n$.

> In practice, $p$ is usually unknown. A common estimate replaces it with the observed sample proportion:
> $$\widehat{\text{SE}}(\hat p) = \sqrt{\frac{\hat p(1-\hat p)}{n}}.$$
> If 14 of the 16 books scan successfully, then $\hat p = 0.875$ and the estimated standard error is
> $$\widehat{\text{SE}}(\hat p) = \sqrt{\frac{0.875(0.125)}{16}} \approx 0.083.$$

**Claude:**
- SD of one observation, $\sqrt{p(1-p)}$, describes how much single books differ. SE $= \text{SD}/\sqrt n$ describes how much whole-sample proportions differ. More data shrinks the second, never the first.
- $\text{SE}$ (no hat) uses the true $p$ and is a fixed number. $\widehat{\text{SE}}$ (hat) plugs in $\hat p$, so it changes from sample to sample. That is the invariance idea again: plug the estimate into the formula.
- Concept note: [[Standard Error]]. Related: [[Variance of the Sample Mean]].

Our run, $\sqrt n$ rule: $n = 16 \to 0.1083$, $n = 64 \to 0.0541$, $n = 256 \to 0.0271$.

> [!note]- My correction
> 

**Fill in:** why does $\widehat{\text{SE}}$ give 0 when $\hat p = 1$, and why is that misleading?
- 

---

### 7.4 Example: comparing two liquid dispensers
> The staff collect 16 fills from A and 25 from B. They will estimate the difference in population means by subtracting the two sample means.

> $$X_i \overset{iid}{\sim} N(\mu_A, \sigma_A^2), \qquad Y_j \overset{iid}{\sim} N(\mu_B, \sigma_B^2).$$
> Each sample mean has an exact normal sampling distribution:
> $$\bar X \sim N\left(\mu_A, \frac{\sigma_A^2}{n_A}\right), \qquad \bar Y \sim N\left(\mu_B, \frac{\sigma_B^2}{n_B}\right).$$

> $$D = \hat\Delta = \bar X - \bar Y.$$
> A difference of independent normal random variables is normal. Its mean is the difference of their means. Its variance is the sum of their variances:
> $$E[D] = \mu_A - \mu_B = \Delta, \qquad \text{Var}(D) = \text{Var}(\bar X) + \text{Var}(\bar Y) = \frac{\sigma_A^2}{n_A} + \frac{\sigma_B^2}{n_B}.$$

> $$\text{Var}(D) = \frac{2^2}{16} + \frac{3^2}{25} = 0.25 + 0.36 = 0.61, \qquad \text{SE}(D) = \sqrt{0.61} \approx 0.781 \text{ milliliters.}$$

**Claude: why the variances add even though you subtract.** $\text{Var}(-\bar Y) = (-1)^2\text{Var}(\bar Y) = \text{Var}(\bar Y)$. Both samples add noise to $D$, so the noise adds up. Rule: [[Variance of a Sum of Independent Random Variables]]. The $D = \bar X - \bar Y$ step uses invariance (chapter 6) on the pair $(\hat\mu_A, \hat\mu_B)$.

> [!note]- My correction
> 

#### 7.4.2 Could sampling reverse the order?
> Suppose, for a sampling calculation, that dispenser A's true mean exceeds dispenser B's by 1 milliliter. Then $\Delta = 1$ and
> $$D \sim N(1, 0.61).$$

```r
pnorm(0, mean = 1, sd = sqrt(0.61))
```
```text
[1] 0.1002077
```

> If both sample sizes are multiplied by four, the variance becomes 0.61/4 and the standard error is halved. With the same true difference of 1 milliliter, the chance of a negative estimated difference becomes about 0.0052.

**Claude, R to Python:** `pnorm(q, mean, sd)` = `scipy.stats.norm.cdf(q, mean, sd)` = $P(D \le q)$. **Trap:** $N(1, 0.61)$ lists the *variance* 0.61, but R and scipy want the *standard deviation*, so pass `sqrt(0.61)`. Our run: `0.1002077`, and `0.0052` with samples ×4. A simulation of 20,000 pairs gave mean 1.000, SD 0.786, $P(D<0) = 0.1016$.

![[w4-fig7.1-dispensers.png]]
*The area left of the red line at 0 is the chance of naming the wrong dispenser as bigger. Each ×4 in sample size halves the width.*

The reading's plotting code, verbatim (figure above is the Python port):
```r
possible_differences <- seq(-2, 4, length.out = 500)

plot(
  possible_differences,
  dnorm(possible_differences, mean = 1, sd = sqrt(0.61)),
  type = "l",
  col = "gray40",
  lwd = 2,
  ylim = c(0, 2.2),
  xlab = "Estimated difference (milliliters)",
  ylab = "Density",
  main = "Comparing two dispenser means"
)
lines(
  possible_differences,
  dnorm(possible_differences, mean = 1, sd = sqrt(0.61 / 4)),
  col = "darkorange", lwd = 2, lty = 2
)
lines(
  possible_differences,
  dnorm(possible_differences, mean = 1, sd = sqrt(0.61 / 16)),
  col = "steelblue", lwd = 2, lty = 3
)
abline(v = 0, col = "firebrick", lty = 2)
legend(
  "topright",
  legend = c("A: 16, B: 25", "A: 64, B: 100", "A: 256, B: 400"),
  col = c("gray40", "darkorange", "steelblue"),
  lwd = 2,
  lty = c(1, 2, 3),
  bty = "n"
)
```

---

### 7.5 Example: the earliest activation time (the sample MINIMUM)
> independent activation delays are uniformly distributed between an unknown earliest time $a$ and a known latest time $b = 20$ seconds. The staff observe seven activations and want to estimate the earliest possible activation time.

> $$L(a \mid \boldsymbol{x}) = \frac{1}{(b-a)^n}\, I\left(0 \le a \le \min_i x_i\right).$$
> Among the allowed values, increasing $a$ shortens the interval and increases the likelihood. Its maximum occurs at the smallest observed delay, so
> $$\hat a = W_n.$$

**Claude:** this mirrors the max case in Lecture 6, flipped. The [[Indicator Function]] $I(\cdot)$ is 1 if the condition is true and 0 if not. So the likelihood is 0 unless $a \le$ every delay, and among allowed $a$ it grows as $a$ grows. Push $a$ up to the smallest delay. Data 7.1, 10.4, 5.8, 13.2, 18.6, 9.5, 15.3 give $\hat a = 5.8$.

**The derivation as a pipeline** (method note: [[Distribution of the Sample Maximum and Minimum]]):

| Step | Given | Do | Get |
|---|---|---|---|
| 1 | one delay $\sim U(a,b)$ | area to the right of $w$ | $P(X_i > w) = \dfrac{b-w}{b-a}$ |
| 2 | "min $> w$" = "every $X_i > w$", independent | multiply $n$ copies ([[Product Notation (Pi)]]) | $P(W_n > w) = \left(\dfrac{b-w}{b-a}\right)^n$ |
| 3 | an upper tail | complement ([[Complement Rule and De Morgan]]) | $F_{W_n}(w) = 1 - \left(\dfrac{b-w}{b-a}\right)^n$ |
| 4 | the CDF | differentiate in $w$ (chain rule, the inside gives a $-1$) | $f_{W_n}(w) = \dfrac{n(b-w)^{n-1}}{(b-a)^n}$ |
| 5 | the pdf | $\int w f(w)\,dw$ | $E[W_n] = a + \dfrac{b-a}{n+1}$ |

> The expected estimate is above the lower endpoint, with bias
> $$\text{Bias}_a(W_n) = \frac{b-a}{n+1}.$$

> $$\text{Var}(W_n) = \frac{n(b-a)^2}{(n+1)^2(n+2)}.$$

> $$P(W_7 > 6) = \left(\frac{20-6}{20-4}\right)^7 = \left(\frac{14}{16}\right)^7 \approx 0.393.$$

> Larger samples give the minimum more opportunities to approach the lower endpoint. Its distribution concentrates near $a$ while retaining an asymmetric shape. It does not become a symmetric bell-shaped distribution.

Our run with $a = 4, b = 20, n = 7$: $E[W_7] = 6.0$, bias $2.0$, SE $1.764$, $P(W_7 > 6) = 0.393$; at $n = 28$, $0.024$. Simulation: mean 6.016, SD 1.790, $P = 0.395$.

> [!note]- My correction
> 

**Fill in:** the max is biased ___ (up/down) and the min is biased ___. Why, in one line each?
- 

---

### 7.6 Normal approximations and the CLT
> For independent observations from the same population with finite mean $\mu$ and positive, finite variance $\sigma^2$, the central limit theorem gives an approximately normal sampling distribution for the sample mean when $n$ is sufficiently large:
> $$\bar X \text{ is approximately } N\left(\mu, \frac{\sigma^2}{n}\right).$$

> $$\hat p \text{ is approximately } N\left(p, \frac{p(1-p)}{n}\right).$$
> This approximation is useful when the expected success count $np$ and expected failure count $n(1-p)$ are both reasonably large.

> The CLT is a result about sums and averages under its assumptions. It does not say that every statistic becomes normally distributed.

Concept note: [[Central Limit Theorem]]. **Claude:** $\hat p$ is a mean of 0s and 1s, so the CLT applies to it. The min and max are not means, so it does not.

> [!note]- My correction
> 

### 7.7 The proportion grid (Figure 7.2)
> To compare the normal curve with the probability masses, we multiply its density by this spacing. A density height times a narrow interval width approximates the probability over that interval.

**Claude:** red dots = exact `dbinom` probabilities, which sit on the grid $0, 1/n, \ldots, 1$. Blue curve = normal pdf × $(1/n)$, so the heights are comparable. Without the $/n$ the curve would be $n$ times too tall.

R, verbatim:
```r
sample_sizes <- c(8, 24, 60)
probabilities <- c(0.2, 0.6, 0.9)
proportion_grid <- seq(-0.2, 1.2, length.out = 600)

par(mfrow = c(3, 3), mar = c(4, 4, 2, 1))

for (n in sample_sizes) {
  for (p in probabilities) {
    possible_proportions <- (0:n) / n
    exact_probabilities <- dbinom(0:n, size = n, prob = p)
    standard_error <- sqrt(p * (1 - p) / n)
    normal_mass_approx <- dnorm(
      proportion_grid, mean = p, sd = standard_error
    ) / n

     plot(
       proportion_grid,
       normal_mass_approx,
       type = "l",
       col = "steelblue",
       lwd = 2,
       ylim = c(0, max(exact_probabilities, normal_mass_approx) * 1.1),
       xlab = "Sample proportion",
       ylab = "Probability mass",
       main = paste("n =", n, ", p =", p)
     )
     points(
       possible_proportions, exact_probabilities,
       col = "firebrick", pch = 16
     )
  }
}

par(mfrow = c(1, 1), mar = c(5.1, 4.1, 4.1, 2.1))
```

![[w4-fig7.2-proportion-grid.png]]

> - **Larger samples give less variable proportions.**
> - **Probabilities near a boundary produce skewness.** When $p = 0.9$ and $n = 8$, all eight scans succeeding is the most likely outcome.
> - **Probabilities farther from the boundaries produce more symmetric distributions.**
> - **The normal approximation can assign probability to impossible values.** Its tails can extend below 0 or above 1.

> The mean of the exact distribution is always $p$, but its most likely value need not equal $p$. For instance, $p = 0.9$ is not even an attainable sample proportion when $n = 8$.

### 7.8 Simulating repeated samples (Figure 7.3)
```r
set.seed(132)
n <- 24
p <- 0.6

sample_proportions <- replicate(
  10000,
  mean(rbinom(n, size = 1, prob = p))
)

hist(
  sample_proportions,
  breaks = seq(-0.5, n + 0.5, by = 1) / n,
  col = "skyblue",
  border = "white",
  xlim = c(0, 1),
  xlab = "Sample proportion",
  ylab = "Number of simulated samples",
  main = "One first-pass rate from each scanner trial"
)
abline(v = p, col = "firebrick", lwd = 2, lty = 2)
```
Our run: mean 0.6003 (theory 0.6), SD 0.1008 (theory $\sqrt{0.6 \cdot 0.4/24} = 0.10$).

![[w4-fig7.3-simulated-proportions.png]]

> Increasing the number of simulated samples makes the histogram a more stable picture of the same sampling distribution. Increasing the number of observations in each sample changes the sampling distribution itself.

**Claude:** in code, that is `reps` (10000) vs `n` (24). Raising `reps` sharpens the picture. Raising `n` changes the thing being pictured.

> [!note]- My correction
> 

---

## Run it locally (Claude)
```bash
cd ~/Documents/"Second Brain"/"School/Courses/stat132"
~/.local/share/stat132-venv/bin/python w4_ch7_sampling_distributions.py
```
Output (run 2026-10-13):
```text
=== 7.2.1  P(p_hat >= 14/16) when p = 0.75 ===
P(K >= 14) = P(K > 13) = 0.197111   (R: 0.197111)
=== 7.2.2 / 7.3  center, spread, standard error of p_hat ===
SE(p_hat) = sqrt(p(1-p)/n) = 0.1083   (reading: 0.108)
estimated SE using p_hat = 0.875: 0.0827   (reading: 0.083)
=== 7.4  difference of two sample means ===
Var(D) = 4/16 + 9/25 = 0.61;  SE(D) = 0.781
P(D < 0 | Delta = 1) = 0.1002077   (R: 0.1002077)
samples x4:  P(D < 0) = 0.0052
=== 7.5  earliest activation time ===
a_hat = min = 5.8
if a = 4: E[W_7] = 6.0, bias = 2.0, SE = 1.764
P(W_7 > 6) = (14/16)^7 = 0.393;  n = 28: 0.024
=== 7.8  10,000 simulated scanner trials, n = 24, p = 0.6 ===
mean 0.6003 (theory 0.6), sd 0.1008 (theory 0.1000)
```
(Trimmed; the script prints a few more lines.)

R function → Python lookup:

| R | Python (scipy / numpy) | Means |
|---|---|---|
| `dbinom(k, n, p)` | `binom.pmf(k, n, p)` | $P(K = k)$ |
| `pbinom(k, n, p)` | `binom.cdf(k, n, p)` | $P(K \le k)$ |
| `pbinom(k, n, p, lower.tail = FALSE)` | `binom.sf(k, n, p)` | $P(K > k)$ |
| `dnorm(x, m, s)` / `pnorm(q, m, s)` | `norm.pdf` / `norm.cdf` | density / $P(X \le q)$, **s is SD** |
| `runif(n, a, b)` / `rbinom(n, 1, p)` | `rng.uniform(a, b, n)` / `rng.binomial(1, p, n)` | random draws |
| `replicate(R, expr)` | list comprehension or a `size=(R, n)` array | repeat R times |

## Chapter summaries (exact)
> - By invariance, if $\hat\theta$ is an MLE of $\theta$, then $g(\hat\theta)$ is an MLE of $g(\theta)$.
> - For exponential waiting times parameterized by rate, the MLEs of the rate, mean, and variance are $1/\bar X$, $\bar X$, and $\bar X^2$.
> - For $U(0, \theta)$ observations, the MLEs of the endpoint and median are $M_n$ and $M_n/2$.
> - Consistency means that the probability of an error exceeding any fixed positive tolerance tends to zero as the sample size grows.
> - Bias is the estimator's expected value minus the true parameter, and MLEs need not be unbiased.
> - The uniform sample maximum has expectation $n\theta/(n+1)$ and bias $-\theta/(n+1)$.
> - Multiplying the uniform maximum by $(n+1)/n$ produces an unbiased estimator, but this corrected estimator is not the MLE.

> - A sampling distribution is the probability distribution of a statistic across repeated samples from a fixed population model.
> - A statistic is calculated from data, but its sampling distribution can depend on unknown population parameters.
> - The standard deviation of a sampling distribution is called the standard error.
> - A sample proportion is a binomial count divided by sample size. Its exact mean is $p$ and its variance is $p(1-p)/n$.
> - For two independent normal samples, the difference of sample means is exactly normal. Its variance is the sum $\sigma_A^2/n_A + \sigma_B^2/n_B$.
> - For uniform activation times on $[a, b]$ with known $b$, the sample minimum estimates $a$. Its mean is $a + (b-a)/(n+1)$, so it is biased upward.
> - Larger independent samples reduce the sampling variability in these examples, but a small standard error does not guarantee small bias.
> - The CLT supports normal approximations for sample means under its assumptions. It does not apply automatically to every statistic.
> - Normal approximations to sample proportions improve as both expected success and failure counts grow.

## Links
[[STAT 132 Week 4]] · [[STAT 132 Lecture 6 - Maximum Likelihood Properties]] · [[STAT 132 Lecture 7 - Sampling Distributions]] · [[STAT 132 Discussion 3 - MLE practice]] · Cards: [[STAT 132 Cards - DeGroot 8.1 Sampling Distributions]]
