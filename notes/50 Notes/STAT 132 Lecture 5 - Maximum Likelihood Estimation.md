---
type: lecture
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
lecture: 5
week: 3
source: "70 Files/Courses/stat132/stat132-lec05.pdf"
status: draft
mastery: 0
aliases:
  - "STAT 132 L5"
  - "STAT 132 Lecture 5"
prereqs:
  - "[[Likelihood Function]]"
  - "[[Estimator vs Estimate]]"
related:
  - "[[Maximum Likelihood Estimation (MLE)]]"
  - "[[Bayes Update Algorithm]]"
---
# STAT 132 Lecture 5: Maximum Likelihood Estimation

Handout: [[stat132-lec05.pdf]] (5 pages). The handout leaves blank space under every example, so the worked solutions below are what goes in that space. Midterm 1, Tue 10-20.

How to use this: text in quote blocks (>) and the example statements are copied from the handout as closely as the PDF text allows. Anything labelled **Claude's explanation** or **Where this comes from**, the answers, and the **Fill in** lines are not in the handout. Cover the folded answers, do each example yourself on paper, then open the answer and compare.

**The question the lecture answers:** you have data and no prior. Which value of the parameter makes the data you saw the most likely?

---

## 0. What changed from Lectures 2 to 4
> We will now turn away from Bayesian inference and look at a common frequentist method for point estimation. Note that we will no longer use a prior distribution, and we are no longer viewing the parameters of interest as random variables. Instead, these are fixed unknown values.

**Claude's comparison (not in the handout):**

|                                         | Bayesian (Lectures 2 to 4)              | Maximum likelihood (Lecture 5)                     |
| --------------------------------------- | --------------------------------------- | -------------------------------------------------- |
| The parameter θ is                      | a random variable with a prior          | one fixed unknown number                           |
| What you build                          | prior × likelihood, then name the curve | the likelihood only                                |
| What you get                            | a whole curve for θ (the posterior)     | one number, θ̂                                     |
| Steps of the [[Bayes Update Algorithm]] | 1 to 6, plus 7 for a point estimate     | 1, 3, 4, and then the calculus below (skip step 2) |

> [!note]- My correction
> 

**Fill in, in my words:** why does the lecture say "turn away from" Bayesian inference, and what is the one thing MLE does not need?
- 

---

## 1. Definition
> **Definition 1.1 (Maximium Likelihood Estimator).** The **maximum likelihood estimator** is defined as
> $$\hat\theta(\boldsymbol{X}) = \arg_\theta \max L(\theta \mid \boldsymbol{X}),$$
> provided it exists. After $\boldsymbol{X} = \boldsymbol{x}$ is observed, $\hat\theta(\boldsymbol{x})$ is called the **maximum likelihood estimate** of $\theta$.
>
> **Note:** We will often abbreviate "maximum likelihood estimate" as MLE.

**Claude's explanation:** read it as "the θ that makes L biggest." argmax returns the **input** that wins, not the winning height.

> [!note]- My correction
>  We have a likelihood function, we don't really care about the way we get to it, we just want the value of theta to be our best guess.


**Fill in:** estimator vs estimate (one line each). Which one has a capital X in it, and why?
- Estimator: 
- Estimate: 

**Fill in:** what does argmax return, and how is it different from max?
- 

---

## 2. Procedure
> Because logarithms are [[Monotonicity|monotonically]] increasing, the argument that maximizes the likelihood is the same as the argument that maximizes the log likelihood. Working with the log likelihood will often be mathematically convenient. This results in the following procedure that often works for finding an MLE.
>
> 1. Compute the log likelihood function: $\ell(\theta \mid \boldsymbol{x}) = \log\left[L(\theta \mid \boldsymbol{X})\right]$
> 2. Differentiate the log likelihood with respect to $\theta$ and set this equal to zero: $\dfrac{d}{d\theta}\ell(\theta \mid \boldsymbol{x}) = 0$
> 3. Solve this expression for $\theta$ - this is your candidate MLE ($\hat\theta$)
> 4. Check that $\left.\dfrac{d^2}{d\theta^2}\ell(\theta \mid \boldsymbol{x})\right|_{\hat\theta} < 0$ to ensure that this is a maximum and not a minimum

**Where this comes from (Claude's explanation, not in the handout):** the log turns products into sums, which are easier to differentiate. Step 1 is your Bayes step 4 (the likelihood), then take the log. The same product of lookups, just stored as a sum.

> [!note]- My correction
> 

%%
Why do we care when we have monotonic, it helps computation. Logs help to prevent underflow, they're sums so nicer, there are computational and mathematical log, 

We will call our first derivative set to 0, our candidate MLE, we'll need to check this always. 

For most of our functions, we 

By monotonicity, we just are sayign that we get the property of X's being greater than or less than in a predictable way. None of those properties are conferred onto theta inherently, just the way in which we might simplify the operations by logging them. It's legit just saying we can do this and it isnt wrong if there are differences then they'll be preserved.

%%
**Fill in, in my words:**
- Why take the log? 
- Why is step 4 needed? What would a positive second derivative mean?
- Which part of the likelihood does the log delete for free? (Hint: the constants with no θ.)
- 

**Fill in:** write the procedure for any Poisson sample $x_1, \dots, x_n$ with unknown λ. Do all four steps in letters, no numbers.
- 

> [!check]- Answer (Poisson in letters)
> $L(\lambda) = \prod \frac{e^{-\lambda}\lambda^{x_i}}{x_i!}$, so $\ell = -n\lambda + (\sum x_i)\ln\lambda - \sum \ln x_i!$. Differentiate: $\ell' = -n + \frac{\sum x_i}{\lambda} = 0$, so $\hat\lambda = \bar x$. Check: $\ell'' = -\frac{\sum x_i}{\lambda^2} < 0$. ✓
> [!note]- My correction
> 


---

## 3. Examples

### Example 1.1: Exponential, three observations
> Suppose you observe a random sample of size 3 from an exponential distribution with parameter θ. The observed data are $X_1 = 3$, $X_2 = 1.5$, and $X_3 = 2.1$. Compute the MLE of θ.

**Fill in:**
- Model (rate form, as in DeGroot): $f(x \mid \theta) =$ 
- Likelihood: $L(\theta) = \prod f(x_i \mid \theta) =$ 
- Sum of the data: $\sum x_i =$ ___ , and $n =$ ___
- Log likelihood: $\ell(\theta) =$ 
- Derivative set to zero, solve: 
- Second derivative check: 
- $\hat\theta =$ 

> [!check]- Answer 1.1
> $f(x \mid \theta) = \theta e^{-\theta x}$. $L = \theta^3 e^{-\theta \sum x_i}$ with $\sum x_i = 6.6$.
> $\ell = 3\ln\theta - 6.6\,\theta$. $\ell' = \frac{3}{\theta} - 6.6 = 0$, so $\hat\theta = \frac{3}{6.6} = \frac{5}{11} \approx \mathbf{0.4545}$.
> $\ell'' = -\frac{3}{\theta^2} < 0$ ✓. Note $\hat\theta = \frac{1}{\bar x} = \frac{1}{2.2}$: the rate is one over the average wait.

[!note]- My correction
> It's expo so it has the first equation $f(x \mid \theta) = \theta e^{-\theta x}$.
> Now we write down our likelihood function, which is in our case a product of the liklihood functions (not written down by Claude so add later but it simplifies to the following) $L = \theta^3 e^{-\theta \sum x_i}$ with $\sum x_i = 6.6$. we'll take the log as it's easier to work with ergo $\ell = 3\ln\theta - 6.6\,\theta$ 
> Next we get the liklihood function after dif. which claude wrote heavily simplified so pls just know you'll have to go from the function to do some math, it's not read and send

### Example 1.2: Bernoulli, general n
> Suppose that $X_1, \dots, X_n$ are a random sample from the Bernoulli distribution with parameter $p$. Find the maximum likelihood estimator for $p$?

**Fill in:**
- One observation: $f(x \mid p) =$ 
- Likelihood with $y = \sum x_i$ successes: $L(p) =$ 
- Log likelihood: $\ell(p) =$ 
- Derivative set to zero: 
- Solve: $\hat p =$ 
- Second derivative check: 
- In words, what is $\hat p$?
- 

> [!check]- Answer 1.2
> $f(x \mid p) = p^x (1-p)^{1-x}$. $L = p^{y}(1-p)^{n-y}$. $\ell = y\ln p + (n-y)\ln(1-p)$.
> $\ell' = \frac{y}{p} - \frac{n-y}{1-p} = 0 \Rightarrow y(1-p) = p(n-y) \Rightarrow y = np$, so $\hat p = \frac{y}{n} = \bar x$.
> $\ell'' = -\frac{y}{p^2} - \frac{n-y}{(1-p)^2} < 0$ ✓. The MLE is the **sample proportion of successes**.
> This is HW1 Q3 in disguise: 60 heads in 100 flips gives $\hat p = 0.6$, exactly the peak of the likelihood you were asked to sketch.
> [!note]- My correction
> 


### Example 1.3: Normal, unknown mean, known variance
> Suppose that $X_1, \dots, X_n$ are a random sample from the Normal distribution with unknown mean μ and known variance σ². Find the maximum likelihood estimator for μ?

**Fill in:**
- One observation: $f(x \mid \mu) =$ 
- Likelihood: $L(\mu) =$ 
- Log likelihood: $\ell(\mu) =$ 
- Which terms have no μ in them, so disappear when you differentiate?
- Derivative set to zero, solve: $\hat\mu =$ 
- Second derivative check: 
- Why does it matter that σ² is known?
- 

> [!check]- Answer 1.3
> $f(x \mid \mu) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{-(x-\mu)^2/(2\sigma^2)}$.
> $\ell(\mu) = -\frac{n}{2}\ln(2\pi\sigma^2) - \frac{1}{2\sigma^2}\sum (x_i - \mu)^2$. The first term has no μ and drops out.
> $\ell' = \frac{1}{\sigma^2}\sum (x_i - \mu) = 0 \Rightarrow \sum x_i = n\mu$, so $\hat\mu = \bar x$.
> $\ell'' = -\frac{n}{\sigma^2} < 0$ ✓. Because σ² is known, there's one unknown and one derivative to solve. If both were unknown you would have two equations.
> [!note]- My correction
> 


### Example 1.4: Poisson failures
> The number of failures in a computer system in a day follows a Poisson distribution with parameter λ. You observe failures on 7 consecutive days: 3,2,4,3,5,2,3. Find the MLE for λ.

**Fill in:**
- Sum of the data: ___ , and $n =$ ___
- Log likelihood with these numbers: $\ell(\lambda) =$ 
- Derivative set to zero, solve: $\hat\lambda =$ 
- Second derivative check: 
- Matches the general answer from section 2? 

> [!check]- Answer 1.4
> $\sum x_i = 3 + 2 + 4 + 3 + 5 + 2 + 3 = 22$, $n = 7$.
> $\ell = 22\ln\lambda - 7\lambda - \sum\ln x_i!$. $\ell' = \frac{22}{\lambda} - 7 = 0$, so $\hat\lambda = \frac{22}{7} \approx \mathbf{3.14}$ failures per day.
> $\ell'' = -\frac{22}{\lambda^2} < 0$ ✓. This is the general result $\hat\lambda = \bar x$ with numbers.
> [!note]- My correction
> 


---

## 4. Edge cases
> In some cases, there may not be a local maximum within the parameter space. In other cases, there may be a local maximum within the parameter space, but a global maximum could lie on the edge of the parameter space. In this case, the previous procedure for finding the MLE will fail. Thus, it is good practice to consider the edges of the parameter space if applicable.

**The tell (Claude's explanation):** the likelihood only exists on part of the number line (the data limits θ), or the derivative is never zero.

> [!note]- My correction
> 


**Fill in, in my words:** what is the warning sign that calculus will fail, and what do you do instead?
- 

### Example 1.5: Uniform on [0, θ]
> Suppose that $X_1, \dots, X_n$ form a random sample from the uniform distribution on $[0, \theta]$, where θ > 0 is unknown. Find the MLE of θ.

**Fill in:**
- One observation: $f(x \mid \theta) =$ ___ for $0 \le x \le \theta$, and 0 otherwise
- If $\theta$ is smaller than the biggest observation, what is the likelihood? Why?
- If $\theta \ge \max x_i$, the likelihood is $L(\theta) =$ 
- Try calculus: $\ell(\theta) =$ ___ , $\ell'(\theta) =$ ___ . Can it equal zero?
- Is $L$ going up or down as θ grows past $\max x_i$?
- So the best θ is: $\hat\theta =$ 
- Draw $L(\theta)$ against θ (a sketch is enough): where does it jump, and where is the peak?
- 

> [!check]- Answer 1.5
> $f(x \mid \theta) = \frac{1}{\theta}$ on $[0, \theta]$. If $\theta < \max x_i$, one observation is outside the allowed range, so its density is 0 and the **whole product is 0**. 
> For $\theta \ge \max x_i$: $L(\theta) = \theta^{-n}$. $\ell = -n\ln\theta$, $\ell' = -\frac{n}{\theta}$, which is **never zero** for any θ > 0. Calculus finds nothing.
> $\theta^{-n}$ is **decreasing** in θ, so you want θ as small as the data allows: $\hat\theta = \mathbf{\max(X_1, \dots, X_n)}$.
> Sketch: zero until $\theta = \max x_i$, then a jump up to its highest value at that point, then a decaying curve.

> [!note]- My correction
> Uniform distributions has to integrate to 1 ergo the dist. is 1/theta
> So our likelihood is the raw definition : n product i=1 f(x_i|theta)
> =n pi i=1 1/theta indicator (x_i greaterthan or eql theta)
> We can call this true for all that are therefore less than just one data point, so we'll do arg max 






### Example 1.6: Triangular density
> A random variable $X$ is modeled using the following PDF:
> $$f(x \mid \theta) = \frac{2}{\theta^2}\,x \quad \text{for } 0 \le x \le \theta.$$
> Suppose you observe the random sample $X_1, \dots, X_n$. What is the MLE of $\theta$?

**Fill in:**
- Check it's a real pdf: $\int_0^\theta \frac{2}{\theta^2}x\,dx =$ 
- Likelihood for $\theta \ge \max x_i$: $L(\theta) =$ 
- Which factors have θ in them? Which are constants?
- Log likelihood and its derivative: $\ell' =$ 
- Can $\ell' = 0$? 
- So the MLE is: $\hat\theta =$ 
- What does this share with Example 1.5?
- 

> [!check]- Answer 1.6
> Check: $\int_0^\theta \frac{2x}{\theta^2}dx = \frac{2}{\theta^2}\cdot\frac{\theta^2}{2} = 1$ ✓.
> $L(\theta) = \prod \frac{2x_i}{\theta^2} = 2^n \left(\prod x_i\right)\theta^{-2n}$ for $\theta \ge \max x_i$, and 0 otherwise. Only $\theta^{-2n}$ involves θ.
> $\ell = \text{const} - 2n\ln\theta$, $\ell' = -\frac{2n}{\theta} \ne 0$. No solution, calculus fails again.
> $\theta^{-2n}$ decreases in θ, so take the smallest allowed θ: $\hat\theta = \mathbf{\max(X_1, \dots, X_n)}$.
> Same shape as 1.5: the **range depends on θ**, so the maximum is on the edge set by the largest observation.
> [!note]- My correction
> 


---

## 5. Which method when (Claude's summary, not in the handout)
**Fill in:** the one-line test for each, in your words
- Use the four-step calculus when: 
- Check the edges instead when: 

**Fill in:** a table of every MLE from today.

| Model | Unknown | MLE | In words |
| --- | --- | --- | --- |
| Exponential (rate θ) | θ | | |
| Bernoulli | p | | |
| Normal, σ² known | μ | | |
| Poisson | λ | | |
| Uniform(0, θ) | θ | | |
| 2x/θ² on [0, θ] | θ | | |

> [!check]- Answer
> | Model | Unknown | MLE | In words |
> | --- | --- | --- | --- |
> | Exponential (rate θ) | θ | $1/\bar x$ | one over the average wait |
> | Bernoulli | p | $\bar x$ | the sample proportion |
> | Normal, σ² known | μ | $\bar x$ | the sample mean |
> | Poisson | λ | $\bar x$ | the sample mean |
> | Uniform(0, θ) | θ | $\max x_i$ | the largest observation |
> | 2x/θ² on [0, θ] | θ | $\max x_i$ | the largest observation |
> [!note]- My correction
> 


**Fill in:** four of these are the sample mean or a function of it. Why is that not a coincidence for these particular models?
- 

---

> [!note]- My correction
> 

## 6. Tie it to the Bayes algorithm (Claude's addition, not in the handout)
- MLE is the Bayes algorithm with **step 2 removed**: no prior, so no step 5 or 6. You only do 1, 3, 4, then maximize.
- The likelihood step 4c matters here. When you only compare values of θ, you may drop constants (that's why the log makes the constants vanish).
- Step 7 gave a point estimate from the posterior (mean under squared error loss). MLE gives a point estimate with no posterior at all.

**Fill in:** compare the Bayes estimate and the MLE for the same coin data: 60 heads in 100 flips.
- MLE: $\hat p =$ 
- Bayes with a Beta(1, 1) prior and squared error loss: posterior is Beta(___ , ___ ), mean = 
- Why are they close here? When would they be far apart?
- 

> [!check]- Answer
> MLE = 0.6. Beta(1, 1) posterior: Beta(61, 41), mean = 61/102 ≈ **0.598**. They're close because 100 flips overwhelms 2 pretend trials. With 3 flips and a strong prior they'd be far apart. Large n lets the data outvote the prior.
> [!note]- My correction
> 

> [!note]- My correction
> 

## My questions for lecture or office hours
- 

## Related
Concept note: [[Maximum Likelihood Estimation (MLE)]] · Previous: [[STAT 132 Lecture 4 - Loss Functions and Bayes Estimators]] · Method: [[Bayes Update Algorithm]] · Course hub: [[STAT 132]]
