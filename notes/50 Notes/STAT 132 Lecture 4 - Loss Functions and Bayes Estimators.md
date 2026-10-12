---
type: lecture
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
lecture: 4
week: 3
source: "70 Files/Courses/stat132/stat132-lec04.pdf"
status: draft
mastery: 0
aliases:
  - "STAT 132 L4"
  - "STAT 132 Lecture 4"
prereqs:
  - "[[STAT 132 Lecture 3 - Posterior Distribution]]"
  - "[[Estimator vs Estimate]]"
related:
  - "[[Loss Function]]"
  - "[[Squared Error Loss]]"
  - "[[Absolute Error Loss]]"
  - "[[Bayes Estimator]]"
  - "[[Bayes Update Algorithm]]"
---
# STAT 132 Lecture 4: Loss Functions and Bayes Estimators

Handout: [[stat132-lec04.pdf]] (5 pages). The handout leaves blank space under every example, so the worked solutions below are what goes in that space. Midterm 1, Tue 10-20. This is the lecture behind step 7 of the [[Bayes Update Algorithm]].

How to use this: text in quote blocks (>) and the example statements are copied from the handout as closely as the PDF text allows. Anything labelled **Claude's explanation**, the answers, the tables, and the **Fill in** lines are not in the handout. Cover the folded answers, do each example yourself on paper, then open the answer and compare.

**The question the lecture answers:** the posterior is a whole curve, but someone wants one number. Which number should you give them?

---

## 1. Point estimation
> We now understand the general idea behind Bayesian inference and the flow from prior to posterior distribution. However, we often want a point estimate for a parameter.
>
> **Definition 1.1 (Point Estimator).** Let $X_1, \dots, X_n$ be observable data whose joint distribution is indexed by a parameter θ taking values in a subset Θ of the real line. A point estimator of the parameter θ is a real-valued function $\delta(X_1, \dots, X_n)$. If $X_1 = x_1, \dots, X_n = x_n$ are observed, then $\delta(x_1, \dots, x_n)$ is called the point estimate of θ.
>
> We almost always would like our estimator $\delta(\boldsymbol{x})$ to give an estimate that is close to the true value of the parameter. Generally, the further away an estimate is from the truth, the less valuable the estimate is to us.

**Fill in:** estimator vs estimate, using a coin as the example
- Estimator (a rule, before the data): 
- Estimate (a number, after the data): 
- Same distinction you saw in Lecture 5 (MLE).

**Fill in, in my words:** why can't the posterior curve alone answer "what is p?" What more does the person asking need?
- 

---

## 2. Loss functions
> **Definition 1.2 (Loss Function).** A loss function is a real-valued function of two variables, $L(\theta, a)$, where θ ∈ Θ and $a$ is a real number. The interpretation is that the statistician "loses" by $L(\theta, a)$ if the parameter equals θ and the estimate equals $a$.
>
> **Note:** We never actually know the true parameter value, so we don't know what the loss will be...if we did, we could just set the estimator to be the true value for zero loss. However, when we view the parameter as a random variable with a distribution, we can find the expected loss. For example, the expected prior loss is
> $$\mathbb{E}\left[L(\theta, a)\right] = \int_\Theta L(\theta, a)\,\pi(\theta)\,d\theta.$$
>
> In practice, we are probably more interested in finding a good estimate after observing the data. In this case, we can consider the expected posterior loss
> $$\mathbb{E}\left[L(\theta, a) \mid \boldsymbol{x}\right] = \int_\Theta L(\theta, a)\,\pi(\theta \mid \boldsymbol{x})\,d\theta.$$
> Our goal will be to minimize this expected loss.

**Fill in, in my words:**
- Which one does the curve in the integral come from, the prior or the posterior, in each line?
- 
- Why do we use the posterior version in practice?
- 

**Fill in:** a story with stakes. A store owner has to order stock for a week and needs one number for her average customers per hour. Who loses what if the number is too high? Too low? Which loss would she prefer, big misses punished a lot or all misses punished in proportion?
- 

---

## 3. Bayes estimators
> **Definition 1.3 (Bayes Estimator).** Let $L(\theta, a)$ be a loss function. For each possible value $x$, let $\delta^*(\boldsymbol{x}) = a$ be such that $\mathbb{E}\left[L(\theta, a) \mid \boldsymbol{x}\right]$ is minimized. Then $\delta^*(\boldsymbol{x})$ is called a **Bayes estimator** of $\theta$. Once $\boldsymbol{X} = \boldsymbol{x}$ is observed, $\delta^*(\boldsymbol{x})$ is called a **Bayes estimate** of $\theta$.

**Claude's explanation:** read it as of all numbers $a$ you could announce, pick the one with the smallest average loss under the posterior.

> [!note]- My correction
> 


**Fill in:** where this plugs into the Bayes update algorithm
- Steps 1 to 6 give: 
- Step 7 gives: 

---

## 4. Common loss functions
> Once we have determined an appropriate loss function, we can find our Bayes estimator. Some common loss functions are given below.
>
> **Definition 1.4 (Squared Error Loss).** The loss function
> $$L(\theta, a) = (\theta - a)^2$$
> is called **squared error loss**.
>
> **Note:** Squared error loss is by far the most commonly used loss function.
>
> **Definition 1.5 (Absolute Error Loss).** The loss function
> $$L(\theta, a) = |\theta - a|$$
> is called **absolute error loss**.
>
> **Note:** Absolute error loss does not penalize extreme deviations as much as squared error loss.

**Fill in:** a miss of 1, a miss of 3, a miss of 10. Compute the loss under each rule.

| Miss (how far off) | Squared | Absolute |
| --- | --- | --- |
| 1 | | |
| 3 | | |
| 10 | | |

> [!check]- Answer
> Squared: 1, 9, 100. Absolute: 1, 3, 10. Squared error treats a miss of 10 as 100 times worse than a miss of 1. Absolute error treats it as 10 times worse.
> [!note]- My correction
> 


**Fill in, in my words:** when would you want each? (Think of a miss you can't afford vs. misses that cost in proportion.)
- Squared error: 
- Absolute error: 

---

## 5. Finding Bayes estimators

### 5.1 Squared error loss gives the posterior mean
> **Theorem 2.1 (Bayes Estimator for Squared Error Loss).** Let θ be a real-valued parameter. Suppose that the squared error loss function is used and that the posterior mean of $\theta$, $\mathbb{E}(\theta \mid \boldsymbol{x})$, is finite. Then, the Bayes estimator of $\theta$ is $\delta(\boldsymbol{X}) = \mathbb{E}(\theta \mid \boldsymbol{X})$.

**Why (Claude's explanation, not in the handout).** Let $m = \mathbb{E}(\theta \mid \boldsymbol{x})$. Expand around it:
$$\mathbb{E}[(\theta - a)^2 \mid \boldsymbol{x}] = \operatorname{Var}(\theta \mid \boldsymbol{x}) + (m - a)^2$$
The first term doesn't depend on $a$. The second is smallest (zero) when $a = m$.

> [!note]- My correction
> 

**Fill in:** redo the expansion yourself. Start from $(\theta - a)^2 = ((\theta - m) + (m - a))^2$ and show the cross term disappears.
- 

> [!check]- Answer
> $((\theta - m) + (m - a))^2 = (\theta - m)^2 + 2(\theta - m)(m - a) + (m - a)^2$. Take the posterior expectation. The cross term is $2(m - a)\,\mathbb{E}(\theta - m \mid \boldsymbol{x}) = 2(m - a)\cdot 0 = 0$, because $m$ is the mean. What's left is $\operatorname{Var}(\theta \mid \boldsymbol{x}) + (m - a)^2$.
> [!note]- My correction
> 


**Fill in:** in the Bayes update algorithm, step 7a says squared error means ___ , and 7b reads it off the named curve. Write the mean for each:
- Gamma(α, β): 
- Beta(α, β): 
- Normal(m, v): 

### Example 2.1: Bernoulli with a Beta prior, in letters
> Let the random sample $X_1, \dots, X_n$ be taken from the Bernoulli distribution with parameter $p$, which is unknown and must be estimated. Let the prior distribution of $p$ be the beta distribution with parameters α > 0 and β > 0. Suppose that the squared error loss function is used. Determine the Bayes estimator of $p$.

**Fill in:**
- Step 1, model for X: 
- Step 2, prior and its kernel: 
- Step 3, data: $y = \sum x_i =$ 
- Step 4, likelihood kernel: 
- Step 5, multiply: 
- Step 6, name the posterior: 
- Step 7, the loss gives: $\delta^*(X) =$ 
- Rewrite it as a weighted average of $\bar X$ and the prior mean $\frac{\alpha}{\alpha+\beta}$: 

> [!check]- Answer 2.1
> 1. Bernoulli(p). 2. Prior kernel $p^{\alpha-1}(1-p)^{\beta-1}$. 3. $y$ = total successes out of $n$. 4. Likelihood kernel $p^{y}(1-p)^{n-y}$.
> 5. Product: $p^{\alpha + y - 1}(1-p)^{\beta + n - y - 1}$. 6. **Beta(α + y, β + n − y).**
> 7. Posterior mean: $\delta^*(X) = \dfrac{\alpha + y}{\alpha + \beta + n}$.
> As a weighted average: $\dfrac{n}{\alpha+\beta+n}\,\bar X + \dfrac{\alpha+\beta}{\alpha+\beta+n}\cdot\dfrac{\alpha}{\alpha+\beta}$. The weights are real data size $n$ against pretend data size $\alpha + \beta$. This is the same node as [[Posterior Mean as a Weighted Average]].
> [!note]- My correction
> 


### Example 2.2: Coin, 8 heads in 10, uniform prior
> Suppose you have observed 10 independent flips of a coin, and observed 8 heads. Your prior distribution for $p$, the probability of heads is a uniform distribution. What is the Bayes estimate of $p$ under squared error loss?

**Fill in:**
- A Uniform(0, 1) prior is the same as Beta( ___ , ___ )
- Plug into Example 2.1: posterior is Beta( ___ , ___ )
- Bayes estimate: 
- Compare with the MLE for the same data (Lecture 5): 
- Why is the estimate pulled toward 0.5?
- 

> [!check]- Answer 2.2
> Uniform(0, 1) = Beta(1, 1). Posterior: Beta(1 + 8, 1 + 2) = **Beta(9, 3)**. Estimate: $\frac{9}{9 + 3} = \frac{9}{12} = \mathbf{0.75}$.
> The MLE is $\frac{8}{10} = 0.8$. The Bayes estimate is lower because the uniform prior is worth 2 pretend flips (1 head, 1 tail), which pulls the answer toward 0.5.
> [!note]- My correction
> 


### Example 2.3: Calorie differences, Normal prior and Normal data
> Allison, Heshka, Sepulveda, and Heymsfield (1993) sampled 20 nationally prepared foods and compared the stated calorie contents per gram from the labels to calorie contents determined in the laboratory. Suppose that we model the conditional distribution of the differences given μ as the normal distribution with mean μ and variance 100. We will use a prior distribution for μ that is the normal distribution with mean 0 and a variance of 60. The data comprise the collection of 20 differences whose average is 0.125. Under squared error loss, what is the Bayes estimate of μ?

**Fill in:** list the givens first
- Data model: variance of one observation $\sigma^2 =$ ___ , $n =$ ___ , $\bar x =$ ___
- Prior: mean $\mu_0 =$ ___ , variance $\tau^2 =$ ___
- Steps 1 and 2 (models): 
- Precision means one over variance. Prior precision = ___ . Data precision (n copies of one observation's) = $n/\sigma^2$ = ___
- Posterior precision = prior precision + data precision = ___
- Posterior variance = 1 / that = 
- Posterior mean = (prior precision × $\mu_0$ + data precision × $\bar x$) / posterior precision = 
- Bayes estimate under squared error: 

> [!check]- Answer 2.3
> $\sigma^2 = 100$, $n = 20$, $\bar x = 0.125$, $\mu_0 = 0$, $\tau^2 = 60$.
> Prior precision $= \frac{1}{60} \approx 0.01667$. Data precision $= \frac{20}{100} = 0.2$. Posterior precision $\approx 0.21667$, so posterior variance $\approx \mathbf{4.615}$ (exactly $\frac{6000}{1300}$).
> Posterior mean $= \dfrac{0.01667 \times 0 + 0.2 \times 0.125}{0.21667} = \dfrac{0.025}{0.21667} \approx \mathbf{0.1154}$ (exactly $\frac{150}{1300}$).
> So the posterior is **Normal(0.1154, 4.615)** and the Bayes estimate is **0.1154**.
> Equivalent formula: $\dfrac{\sigma^2\mu_0 + n\tau^2\bar x}{\sigma^2 + n\tau^2} = \dfrac{100(0) + 20(60)(0.125)}{100 + 1200}$. The data weight is $\frac{1200}{1300} \approx 92\%$.
> [!note]- My correction
> 


**Fill in:** in one sentence, why is the answer almost the sample mean?
- 

### Example 2.4: Store arrivals, Poisson with a Gamma prior
> A store owner models customer arrivals as Poisson with unknown rate λ per hour. She assigns λ a gamma prior distribution with parameters α = 3 and β = 2. Let X be the number of customers that arrive in a specific one-hour period. If X = 3 is observed, find the Bayes estimate of λ under squared error loss.

**Fill in:**
- Step 1, model for X: 
- Step 2, prior kernel: 
- Step 4, likelihood kernel from one observation, $x = 3$: 
- Step 5, product: 
- Step 6, posterior: 
- Pretend data plus real data: the prior is worth ___ pretend customers in ___ pretend hours. The real data is ___ customers in ___ hour.
- Step 7, the mean: 
- Is the estimate between the prior mean and the data? Which are they?
- 

> [!check]- Answer 2.4
> 1. Poisson(λ). 2. Prior kernel $\lambda^{2}e^{-2\lambda}$. 4. Likelihood kernel $\lambda^{3}e^{-\lambda}$ (one hour, three customers).
> 5. Product: $\lambda^{5}e^{-3\lambda}$. 6. Match $\lambda^{\alpha-1}e^{-\beta\lambda}$: **Gamma(6, 3)** (watch the minus 1: $\lambda^5$ means α = 6).
> 7. Mean = $\frac{6}{3} = \mathbf{2}$ customers per hour.
> Prior worth 3 customers in 2 hours (mean 1.5). Data: 3 customers in 1 hour (mean 3). The answer, 2, sits between them, closer to the prior because 2 pretend hours outweighs 1 real hour.
> [!note]- My correction
> 


---

### 5.2 Absolute error loss gives the posterior median
> **Theorem 2.2 (Bayes Estimator for Absolute Error Loss).** Let θ be a real-valued parameter. Suppose that the absolute error loss function is used. Then, the Bayes estimator of θ is the posterior median.

The **median** is the value with half of the posterior's area on each side. You find it by solving $P(\theta \le a \mid \boldsymbol{x}) = \tfrac{1}{2}$.

**Fill in, in my words:** why does punishing misses in proportion lead to the middle of the distribution (half the weight on each side) and not the average?
- 

**Fill in:** where the mean and median agree, and where they don't
- They're equal when the posterior is: 
- For a right-skewed curve (Gamma), the median is smaller / larger than the mean (circle one): 

### Example 2.5: Calorie differences, absolute error loss
> Allison, Heshka, Sepulveda, and Heymsfield (1993) sampled 20 nationally prepared foods and compared the stated calorie contents per gram from the labels to calorie contents determined in the laboratory. Suppose that we model the conditional distribution of the differences given μ as the normal distribution with mean μ and variance 100. We will use a prior distribution for μ that is the normal distribution with mean 0 and a variance of 60. The data comprise the collection of 20 differences whose average is 0.125. Under absolute error loss, what is the Bayes estimate of μ?

**Fill in:**
- Posterior (from 2.3): Normal( ___ , ___ )
- Is a Normal symmetric? So its median equals its ___ 
- Bayes estimate under absolute error loss: 
- So the two losses give the same / different answer here: 

> [!check]- Answer 2.5
> The posterior is Normal(0.1154, 4.615). A Normal is symmetric, so its median equals its mean: **0.1154**. Same answer as 2.3. For a symmetric posterior the two losses agree. The choice of loss only matters when the posterior is skewed.
> [!note]- My correction
> 


**Fill in:** a case where the losses disagree. Take the Gamma(6, 3) posterior from Example 2.4. Mean = ___ . The median is a bit lower, about 1.89, because a right-skewed curve's long tail pulls the mean up.
- Squared error estimate: 
- Absolute error estimate: 
- Which would you announce if overshooting by a lot costs her far more than undershooting? (Think about which loss the question implies.)
- 

---

## 6. Summary tables (Claude's, not in the handout)

**Fill in:** every estimate from today.

| Example | Model | Prior | Posterior | Loss | Estimate |
| --- | --- | --- | --- | --- | --- |
| 2.1 | Bernoulli | Beta(α, β) | | squared | |
| 2.2 | Bernoulli, 8 of 10 | Uniform = Beta(1, 1) | | squared | |
| 2.3 | Normal(μ, 100), n = 20 | Normal(0, 60) | | squared | |
| 2.4 | Poisson, x = 3 | Gamma(3, 2) | | squared | |
| 2.5 | Normal(μ, 100), n = 20 | Normal(0, 60) | | absolute | |

> [!check]- Answer
> | Example | Posterior | Estimate |
> | --- | --- | --- |
> | 2.1 | Beta(α + y, β + n − y) | $\frac{\alpha + y}{\alpha + \beta + n}$ |
> | 2.2 | Beta(9, 3) | 0.75 |
> | 2.3 | Normal(0.1154, 4.615) | 0.1154 |
> | 2.4 | Gamma(6, 3) | 2 |
> | 2.5 | Normal(0.1154, 4.615) | 0.1154 (median) |
> [!note]- My correction
> 


**Fill in, in my words:** the whole lecture in three lines
1. 
2. 
3. 

> [!note]- My correction
> 

## 7. Where this shows up in the homework (Claude's note)
HW1 has no loss function question, but the Bayes update steps 1 to 6 are used in every example above. If a later question says "Bayes estimate" or "squared error loss", run steps 1 to 6 and finish with step 7 using the table in section 5.

> [!note]- My correction
> 

## My questions for lecture or office hours
- 

## Related
Concept notes: [[Loss Function]], [[Squared Error Loss]], [[Absolute Error Loss]], [[Bayes Estimator]], [[Estimator vs Estimate]] · Previous: [[STAT 132 Lecture 3 - Posterior Distribution]] · Next: [[STAT 132 Lecture 5 - Maximum Likelihood Estimation]] · Method: [[Bayes Update Algorithm]] · Course hub: [[STAT 132]]
