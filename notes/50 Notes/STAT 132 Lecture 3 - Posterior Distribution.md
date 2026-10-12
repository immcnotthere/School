---
type: lecture
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "~/Documents/STATS132/Lectures/STAT132 Lecture 03 - Posterior distribution and conjugate priors.pdf"
---
# STAT 132 Lecture 3: The Posterior Distribution

The full text of the Lecture 3 handout (7 pages), with the math rewritten so it renders, and room under every section for your own notes and your questions.
- **Your notes** go in the `> [!note] My notes` boxes.
- **Questions for Claude** go in the `> [!question] Ask Claude` boxes. Write the question, then tell Claude "answer the questions in Lecture 3"; the answer will go right under it.
- The lecture leaves the examples and proofs blank (they are done in class). Worked versions are below each one, **folded**: try first, then click to open.

## The dogma (every Bayesian problem in this course)
> [!abstract] Six rules
> 1. **Read the story, pick the data model** with the decision tree (make or miss: Bernoulli).
> 2. **Put the unknown in the model's slot:** $X_i \sim \text{Family}(\theta)$. A known second setting goes in as a number: Binomial($n = 5$, $\theta$), Normal($\theta$, $\sigma^2 = 100$).
> 3. **The prior is a distribution on $\theta$'s possible values**, never on the data.
> 4. **Likelihood:** plug the observed data into the model's formula, multiply over the data points, read it as a function of $\theta$. Order of the data doesn't matter; only counts or totals do.
> 5. **Posterior $\propto$ prior $\times$ likelihood**, then normalize (sum, integrate, or recognize the kernel).
> 6. **The answer is a distribution over $\theta$**, never "the true $\theta$".

## Before you start: what a problem gives you, and what you find

> [!important] The shape of every problem in this lecture
> You are **given three things** and you **find one**.
>
> | Given | What it looks like in the problem | Example (Example 1.2) |
> | --- | --- | --- |
> | 1. **The data model** (likelihood family) | a sentence about how the data are made: "Bernoulli", "flips of a coin", "Poisson arrivals", "normal with known variance" | each flip is Bernoulli($p$) |
> | 2. **The prior** for the unknown parameter, with its numbers | "the prior is Beta(1, 1)", "a gamma prior with $\alpha = 3$, $\beta = 2$", or a mean and variance you turn into $\alpha, \beta$ | Uniform = Beta(1, 1) |
> | 3. **The data** | either every value ($x_1, \dots, x_n$) or a summary: $n$ and the total $\sum x_i$, or $n$ and the average $\bar x$ | 10 flips, 8 heads |
>
> **You find:** the **posterior** $\pi(\theta \mid x_1, \dots, x_n)$: which family, and its new parameter numbers. Then, if asked, its mean, variance, or a probability.
>
> **Two corrections to "we find $\theta$ by asking what prior led to this":**
> - You don't find $\theta$ as one number. You find a whole **distribution** for $\theta$ (the posterior). If someone wants one number, the usual pick is the **posterior mean** (that is Lecture 4 territory: Bayes estimators).
> - You are usually **handed** the prior. The direction is prior + data → posterior. ("Which prior would have led to this posterior?" is a rarer reverse puzzle, like DeGroot 7.3 Exercise 4.)
>
> **The summary each pair needs from the data:**
>
> | Data model | Prior | You need from the data | Posterior |
> | --- | --- | --- | --- |
> | Bernoulli($p$) | Beta($\alpha$, $\beta$) | $n$ and $\sum x_i$ (number of 1s) | Beta($\alpha + \sum x_i$, $\beta + n - \sum x_i$) |
> | Poisson($\lambda$) | Gamma($\alpha$, $\beta$) | $n$ and $\sum x_i$ (total count) | Gamma($\alpha + \sum x_i$, $\beta + n$) |
> | Normal($\mu$, $\sigma^2$ known) | Normal($\mu_0$, $\sigma_0^2$) | $n$ and $\bar x$ | Normal($\mu_1$, $\sigma_1^2$), formulas in 1.7 |

> [!question] Ask Claude
> 

---

## 1 Posterior Distribution
Recall that the prior distribution $\pi(\theta)$ expresses our state of knowledge for the parameter $\theta$ **before** observing any data. However, we actually want to know what our state of knowledge is **after** observing data.

> [!note] My notes
> 

### 1.1 Definition
> [!definition] Definition 1.1 (Posterior)
> Consider a statistical inference problem with parameter $\theta$ and random variables $X_1, \dots, X_n$ to be observed. The conditional distribution of $\theta$ given $X_1, \dots, X_n$ is called the **posterior distribution** of $\theta$. The conditional pdf or pmf of $\theta$ given $X_1 = x_1, \dots, X_n = x_n$ is called the **posterior pdf** or **posterior pmf** of $\theta$ and is typically denoted
> $$\pi(\theta \mid x_1, \dots, x_n).$$

*Read aloud: "pi of theta given x 1 through x n."* Capital $X_i$ = the data before you see them (random); lowercase $x_i$ = the numbers you actually got.

The posterior distribution expresses our state of knowledge about the parameter after observing the data. This is a probability distribution, so we can freely calculate things like the mean and variance of this distribution.
- **High posterior variance** means that we still are not very certain what a likely value is for the parameter.
- **Low posterior variance** means we have little uncertainty about the likely values for the parameter.

> [!note] My notes
> 

> [!question] Ask Claude
> 

### 1.2 Bayesian Inference
Bayesian inference is centered around the posterior distribution. The main goal is to find or calculate this distribution.

> [!theorem] Theorem 1.1 (Bayes' Theorem)
> Suppose that the $n$ random variables $X_1, \dots, X_n$ form a random sample from a distribution for which the pdf or pmf is $f(x \mid \theta)$. Suppose also that the value of the parameter $\theta$ is unknown and the prior pdf or pmf of $\theta$ is $\pi(\theta)$, with parameter space $\theta \in \Theta$. Then the posterior pdf or pmf of $\theta$ is
> $$\pi(\theta \mid x_1, \dots, x_n) = \frac{f(x_1 \mid \theta) \cdots f(x_n \mid \theta)\, \pi(\theta)}{m_n(x_1, \dots, x_n)}$$
> where $m_n(x_1, \dots, x_n)$ is the joint marginal distribution of the data, $x_1, \dots, x_n$.

*Read aloud: "pi of theta given the data equals f of x 1 given theta, times ... times f of x n given theta, times pi of theta, all over m n of the data."* The top is **likelihood × prior**; the bottom is a normalizing constant.

Notice that because the data are all independent (random sample) coming from the same distribution, we have that
$$f(x_1, \dots, x_n \mid \theta) = f(\mathbf{x} \mid \theta) = f(x_1 \mid \theta) \cdots f(x_n \mid \theta) = \prod_{i=1}^n f(x_i \mid \theta).$$

The marginal distribution of the data can be found by integrating out the parameter
$$m_n(x_1, \dots, x_n) = m_n(\mathbf{x}) = \int_\Theta f(\mathbf{x} \mid \theta)\, \pi(\theta)\, d\theta.$$

- After integrating out the parameter, the marginal is no longer a function of the parameter ($\theta$).
- Since the marginal is not a function of $\theta$, it can be thought of as a constant term that shows up in the posterior distribution, and is usually ignored.
- In this case, we write $\pi(\theta \mid \mathbf{x}) \propto f(\mathbf{x} \mid \theta)\, \pi(\theta)$, where the symbol $\propto$ means "proportional to".
- **The posterior distribution is then proportional to the likelihood times the prior distribution!**

> [!tip] Why dropping $m_n$ is safe
> $m_n(\mathbf{x})$ is just the number that makes the posterior's total area 1 (the normalizing constant, Ladder 04). You can leave it out, look at the **shape** in $\theta$, recognize which family has that shape, and the family's own constant puts it back.

> [!note] My notes
> 

> [!question] Ask Claude
> 

### 1.3 Example
Since $\pi(\theta \mid \mathbf{x}) \propto f(\mathbf{x} \mid \theta)\, \pi(\theta)$, if we recognize $f(\mathbf{x} \mid \theta)\, \pi(\theta)$ as corresponding to a specific family of distributions, then we know what our posterior distribution is.

> [!example] Example 1.1
> Suppose that the proportion $\theta$ of defective items in a large manufactured lot is unknown and that the prior distribution for $\theta$ is a uniform distribution on the interval $[0, 1]$. Suppose also that a random sample of $n$ items is taken from the lot, and for $i = 1, \dots, n$, let $X_i = 1$ if the $i$th item is defective, and let $X_i = 0$ otherwise. Determine the posterior distribution of $\theta$.

> [!note] My work
> 

> [!success]- Worked solution (try first)
> 1. **Given:** data model Bernoulli($\theta$): $f(x_i \mid \theta) = \theta^{x_i}(1-\theta)^{1-x_i}$. Prior Uniform[0, 1]: $\pi(\theta) = 1$ for $0 \le \theta \le 1$. Data: $x_1, \dots, x_n$, summarized by $y = \sum x_i$ (number defective).
> 2. **Likelihood:** multiply the $n$ factors; exponents add: $\prod_i \theta^{x_i}(1-\theta)^{1-x_i} = \theta^{y}(1-\theta)^{n-y}$.
> 3. **Likelihood × prior:** $\theta^{y}(1-\theta)^{n-y} \times 1$.
> 4. **Recognize the shape:** a Beta($\alpha$, $\beta$) pdf is proportional to $\theta^{\alpha-1}(1-\theta)^{\beta-1}$. Match exponents: $\alpha - 1 = y$, $\beta - 1 = n - y$.
> 5. **Answer:** $\theta \mid \mathbf{x} \sim \text{Beta}(y + 1,\ n - y + 1)$.
>
> Links: [[Defective Items Posterior]], [[Posterior Proportionality]].

> [!question] Ask Claude
> 

---

### 1.4 Conjugate Priors
> [!definition] Definition 1.2 (Conjugate Prior)
> For a given likelihood, if the prior and posterior distribution belong to the same family, this is said to be a **conjugate prior distribution**. In this case, posterior updating can be done simply by updating the parameters that correspond to the family.

Example 1.1 is one: Uniform is Beta(1, 1), and the posterior was again a Beta. See [[Conjugate Prior]].

> [!note] My notes
> 

> [!question] Ask Claude
> 

### 1.5 Bernoulli Sampling
> [!theorem] Theorem 1.2 (Beta-Bernoulli Updating)
> Suppose that $X_1, \dots, X_n$ form a random sample from the Bernoulli distribution with parameter $p$, which is unknown ($0 < p < 1$). Suppose also that the prior distribution of $p$ is the beta distribution with parameters $\alpha > 0$ and $\beta > 0$. Then the posterior distribution of $p$ given $x_1, \dots, x_n$ is the beta distribution with parameters
> $$\alpha + \sum_{i=1}^n x_i \quad \text{and} \quad \beta + n - \sum_{i=1}^n x_i.$$

*In words:* add the number of successes to $\alpha$ and the number of failures to $\beta$. See [[Beta-Bernoulli Update]].

> [!success]- Proof (left blank in the handout)
> Write $y = \sum x_i$. Likelihood: $p^{y}(1-p)^{n-y}$. Prior: $\pi(p) \propto p^{\alpha-1}(1-p)^{\beta-1}$ (the constant $\frac{\Gamma(\alpha+\beta)}{\Gamma(\alpha)\Gamma(\beta)}$ is dropped).
> Product: $p^{y}(1-p)^{n-y} \cdot p^{\alpha-1}(1-p)^{\beta-1} = p^{(\alpha + y) - 1}(1-p)^{(\beta + n - y) - 1}$ (same base, exponents add).
> That is the Beta($\alpha + y$, $\beta + n - y$) shape, so that is the posterior. $\blacksquare$

> [!example] Example 1.2
> Suppose you have observed 10 independent flips of a coin, and observed 8 heads. Your prior distribution for $p$, the probability of heads, is a uniform distribution (i.e., Beta(1, 1)). What is the posterior distribution for $p$? What is the posterior mean? What is the posterior variance?

> [!note] My work
> 

> [!success]- Worked solution (try first)
> - **Given:** Bernoulli($p$) flips; prior Beta(1, 1); $n = 10$, $\sum x_i = 8$.
> - **Posterior:** Beta($1 + 8$, $1 + 10 - 8$) = **Beta(9, 3)**.
> - **Mean:** $\frac{\alpha}{\alpha + \beta} = \frac{9}{12} = 0.75$.
> - **Variance:** $\frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)} = \frac{9 \cdot 3}{12^2 \cdot 13} = \frac{27}{1872} = \frac{3}{208} \approx 0.0144$.
> - **Read it:** before, any $p$ was equally likely (mean 0.5); after 8 of 10, the belief centers near 0.75, but with SD $\approx 0.12$ it's still fairly spread.
>
> Link: [[Coin Flip Posterior]].

> [!question] Ask Claude
> 

### 1.6 Poisson Sampling
> [!theorem] Theorem 1.3 (Gamma-Poisson Updating)
> Suppose that $X_1, \dots, X_n$ form a random sample from the Poisson distribution with parameter $\lambda$, which is unknown ($\lambda > 0$). Suppose also that the prior distribution of $\lambda$ is the gamma distribution with parameters $\alpha > 0$ and $\beta > 0$. Then the posterior distribution of $\lambda$ given $x_1, \dots, x_n$ is the gamma distribution with parameters
> $$\alpha + \sum_{i=1}^n x_i \quad \text{and} \quad \beta + n.$$

*In words:* add the total count to $\alpha$, and the number of windows observed to $\beta$ (rate form, as in DeGroot). See [[Gamma-Poisson Update]].

> [!success]- Proof (left blank in the handout)
> Write $y = \sum x_i$. Likelihood: $\prod_i \frac{e^{-\lambda}\lambda^{x_i}}{x_i!} \propto e^{-n\lambda}\lambda^{y}$ (the $x_i!$ don't involve $\lambda$, so they drop).
> Prior: $\pi(\lambda) \propto \lambda^{\alpha-1}e^{-\beta\lambda}$.
> Product: $\lambda^{(\alpha + y) - 1} e^{-(\beta + n)\lambda}$: the Gamma($\alpha + y$, $\beta + n$) shape. $\blacksquare$

> [!example] Example 1.3
> A store owner models customer arrivals as Poisson with unknown rate $\lambda$ per hour. She assigns a gamma prior distribution with parameters $\alpha = 3$ and $\beta = 2$. Let $X$ be the number of customers that arrive in a specific one-hour period. If $X = 3$ is observed, find the posterior distribution of $\lambda$. What is the prior variance? What is the posterior variance?

> [!note] My work
> 

> [!success]- Worked solution (try first)
> - **Given:** Poisson($\lambda$) per hour; prior Gamma(3, 2); one hour observed, so $n = 1$, $\sum x_i = 3$.
> - **Posterior:** Gamma($3 + 3$, $2 + 1$) = **Gamma(6, 3)**.
> - **Prior variance:** $\frac{\alpha}{\beta^2} = \frac{3}{4} = 0.75$ (prior mean $\frac{3}{2} = 1.5$ customers per hour).
> - **Posterior variance:** $\frac{6}{9} = \frac{2}{3} \approx 0.667$ (posterior mean $\frac{6}{3} = 2$).
> - **Read it:** seeing 3 customers pulled the belief up from 1.5 toward 3 and made it a little less uncertain.
>
> Link: [[Store Arrivals Posterior]].

> [!question] Ask Claude
> 

### 1.7 Normal Sampling
> [!theorem] Theorem 1.4 (Normal-Normal Updating)
> Suppose that $X_1, \dots, X_n$ form a random sample from a normal distribution for which the value of the mean $\mu$ is unknown and the value of the variance $\sigma^2 > 0$ is known. Suppose also that the prior distribution for $\mu$ is the normal distribution with mean $\mu_0$ and variance $\sigma_0^2$. Then the posterior distribution of $\mu$ given $x_1, \dots, x_n$ is the normal distribution with mean $\mu_1$ and variance $\sigma_1^2$, where
> $$\mu_1 = \frac{\sigma^2 \mu_0 + n\sigma_0^2\, \bar x_n}{\sigma^2 + n\sigma_0^2} \qquad \text{and} \qquad \sigma_1^2 = \frac{\sigma^2 \sigma_0^2}{\sigma^2 + n\sigma_0^2}.$$

*Read it:* $\mu_1$ is a **weighted average** of the prior mean $\mu_0$ and the sample mean $\bar x_n$. The weights are $\sigma^2$ (on the prior mean) and $n\sigma_0^2$ (on the data): more data, or a vaguer prior, puts more weight on $\bar x_n$. Symbols: $\sigma^2$ = the data's known variance; $\mu_0, \sigma_0^2$ = the prior's mean and variance; $\mu_1, \sigma_1^2$ = the posterior's. See [[Normal-Normal Update]].

> [!example] Example 1.4
> Allison, Heshka, Sepulveda, and Heymsfield (1993) sampled 20 nationally prepared foods and compared the stated calorie contents per gram from the labels to calorie contents determined in the laboratory. Suppose that we model the conditional distribution of the differences given $\mu$ as the normal distribution with mean $\mu$ and variance 100. We will use a prior distribution for $\mu$ that is the normal distribution with mean 0 and a variance of 60. The data comprise the collection of 20 differences whose average is 0.125. What is the posterior distribution of $\mu$?

> [!note] My work
> 

> [!success]- Worked solution (try first)
> - **Given:** $\sigma^2 = 100$ (known); prior $\mu_0 = 0$, $\sigma_0^2 = 60$; data $n = 20$, $\bar x_n = 0.125$.
> - **Denominator (used twice):** $\sigma^2 + n\sigma_0^2 = 100 + 20 \cdot 60 = 1300$.
> - **Posterior mean:** $\mu_1 = \frac{100 \cdot 0 + 1200 \cdot 0.125}{1300} = \frac{150}{1300} \approx 0.115$.
> - **Posterior variance:** $\sigma_1^2 = \frac{100 \cdot 60}{1300} = \frac{6000}{1300} \approx 4.62$.
> - **Answer:** $\mu \mid \mathbf{x} \sim \text{Normal}(0.115,\ 4.62)$.
>
> Link: [[Calorie Difference Posterior]] (DeGroot Example 7.3.12 gives the same numbers).

> [!question] Ask Claude
> 

### 1.8 Effect of the Prior
Consider the normal sampling case, where data points are sampled from a normal distribution with unknown mean $\mu$ and variance equal to 1. Suppose that 10 data points are sampled and the sample mean is 3. Consider three different normal prior distributions for $\mu$. All three priors are centered at zero, but the prior variances are $1/2$, $1$, and $5$ respectively. The plot (in the PDF, page 6) illustrates the effect of the prior variance.

The plot's numbers, from Theorem 1.4 with $\sigma^2 = 1$, $n = 10$, $\bar x = 3$, $\mu_0 = 0$:

| Prior variance $\sigma_0^2$ | Posterior mean $\mu_1 = \frac{10\sigma_0^2 \cdot 3}{1 + 10\sigma_0^2}$ | Posterior variance $\sigma_1^2 = \frac{\sigma_0^2}{1 + 10\sigma_0^2}$ |
| --- | --- | --- |
| 1/2 | 15/6 = 2.50 | 0.083 |
| 1 | 30/11 ≈ 2.73 | 0.091 |
| 5 | 150/51 ≈ 2.94 | 0.098 |

- When the sample size $n$ is small, the posterior mean will be closer to the prior mean.
- When the sample size is large, the posterior mean is pulled closer to the sample mean. This can be interpreted as giving more weight to the data.
- When the prior variance $\sigma_0^2$ is small, the prior has more influence on the posterior and the posterior mean will be pulled closer to the prior mean.
- As the sample size increases, the posterior variance decreases.

> [!note] My notes
> 

> [!question] Ask Claude
> 

---

## After class
> [!note] What the professor added that isn't in the handout
> 

> [!question] Still confused about
> 
