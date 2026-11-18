---
type: lecture
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
lecture: 6
week: 4
source: "70 Files/Courses/stat132/stat132-lec06.pdf"
status: draft
mastery: 0
aliases:
  - "STAT 132 L6"
  - "STAT 132 Lecture 6"
prereqs:
  - "[[STAT 132 Lecture 5 - Maximum Likelihood Estimation]]"
  - "[[Maximum Likelihood Estimation (MLE)]]"
  - "[[Expectation and Variance]]"
related:
  - "[[Invariance Property of MLEs]]"
  - "[[Consistency of the MLE]]"
  - "[[Bias of an Estimator]]"
  - "[[STAT 132 Reading 04 - MLE Properties and Sampling Distributions]]"
  - "[[STAT 132 Week 4]]"
---
# STAT 132 Lecture 6: Maximum Likelihood Properties

Handout: [[stat132-lec06.pdf]] (4 pages). The same material, with numbers and R code, is chapter 6 of [[STAT 132 Reading 04 - MLE Properties and Sampling Distributions|Reading 04]]. Week hub: [[STAT 132 Week 4]]. Midterm 1, Tue 10-20.

How to use this: quote blocks (>) are the handout, copied word for word and checked against the page images. Anything labelled **Claude** is mine, not the handout. Each has a `My correction` slot under it for you to overwrite me. Answers are folded: do the example on paper, then open the fold. The code runs on this laptop (section 5).

**The question the lecture answers:** you already have an MLE $\hat\theta$ from [[STAT 132 Lecture 5 - Maximum Likelihood Estimation|Lecture 5]]. Three follow-ups:
1. Can I get the MLE of something *built from* $\theta$ (a mean, a variance, a median) without redoing the calculus? **Invariance: yes.**
2. Does $\hat\theta$ get close to the truth with more data? **Consistency: yes.**
3. Is $\hat\theta$ right *on average* at a fixed $n$? **Bias: not always.**

---

## 0. The whole lecture as code (Claude)
If you think in functions, this is the lecture:

```python
theta_hat = mle(data)              # Lecture 5: argmax of the likelihood. Returns ONE number.

# 1.1 Invariance: to estimate g(theta), pipe theta_hat through g. No new argmax.
mle_of_g = g(theta_hat)            # e.g. g = lambda lam: 1/lam   (mean of an exponential)

# 1.2 Consistency: a statement about running mle() on bigger and bigger samples.
for n in [5, 20, 50, 200]:
    error_chance(n) = P(|mle(sample_of_size(n)) - theta_true| > eps)   # -> 0 as n grows

# 1.3 Bias: a statement about running mle() on MANY samples of the SAME size n.
bias = mean(mle(sample_of_size(n)) for many samples) - theta_true   # may be != 0
```

Words that have a note behind them: [[Estimator vs Estimate]] (the function vs the number it returns), [[Statistic (inference)]], [[Parameters]], [[Expectation and Variance]] ($E$ is "average over many samples").

> [!note]- My correction
> 

---

## 1. Maximum Likelihood
> Maximum likelihood estimators have some nice properties that make them a valuable estimator. We will explore these properties below.

### 1.1 Invariance
> **Theorem 1.1.** *Let $\hat\theta$ be a maximum likelihood estimate of some parameter $\theta$. Also let $g(\theta)$ be any function of the parameter $\theta$. Then the maximum likelihood estimate of $g(\theta)$ is $g(\hat\theta)$.*
>
> This means that as long as we can compute an MLE for the parameter $\theta$, we get the MLE of any function of the parameter for "free". For example, medians and other quantiles are typically a function of the distribution parameters.

**Claude's explanation:** $g$ is any rule that turns the parameter into the quantity you care about. Write down $g$ (how the quantity depends on $\theta$), then plug $\hat\theta$ into it. The work is all in step 1: knowing the formula that links the quantity to the parameter (mean of an [[Exponential distribution]], median of a [[Uniform distribution]], a [[Quantile Function|quantile]] of a [[Normal distribution]]). Concept note: [[Invariance Property of MLEs]].

The recipe, as data moving through steps:

| Step | Given | What you do | You now have |
|---|---|---|---|
| 1 | the model, e.g. $X_i \sim \text{Exp}(\lambda)$ | look up / derive the quantity as a function of the parameter | $g(\lambda) = 1/\lambda$ |
| 2 | the data | find the MLE of the parameter (Lecture 5 procedure) | $\hat\lambda$ |
| 3 | $g$ and $\hat\lambda$ | plug in | $\widehat{g(\lambda)} = g(\hat\lambda)$ |

> [!note]- My correction
> 

**Fill in, in my words:** why is this "free"? What step from Lecture 5 do I skip?
- 

> **Example 1.1.** Suppose you observe a random sample, $X_1, \ldots, X_n$, of wait times for a customer support center. These wait times are modeled as coming from an exponential distribution with parameter $\lambda$. What is the MLE of the average wait time?

> [!example]- Worked answer (Claude, not in the handout)
> **Step 1. Given:** $X_i \overset{iid}{\sim} \text{Exp}(\lambda)$, rate form (DeGroot, your course): $f(x \mid \lambda) = \lambda e^{-\lambda x}$ for $x \ge 0$. ([[iid (Independent and Identically Distributed)|iid]] = independent, same distribution.)
> **Do:** the average wait time is $E[X_i]$. For the rate form, $E[X_i] = \dfrac{1}{\lambda}$.
> **Get:** $g(\lambda) = \dfrac{1}{\lambda}$.
>
> **Step 2. Given:** the data. **Do:** Lecture 5 procedure.
> - Likelihood (multiply the $n$ densities, see [[Product Notation (Pi)]]): $L(\lambda \mid \boldsymbol{x}) = \prod_{i=1}^n \lambda e^{-\lambda x_i} = \lambda^n e^{-\lambda \sum_{i=1}^n x_i}$
> - Log ([[Log-Likelihood]]): $\ell(\lambda) = n \log\lambda - \lambda \sum_{i=1}^n x_i$
> - Derivative set to 0: $\dfrac{n}{\lambda} - \sum x_i = 0 \;\Rightarrow\; \lambda = \dfrac{n}{\sum x_i}$
> - Second derivative $-\dfrac{n}{\lambda^2} < 0$, so it is a max.
>
> **Get:** $\hat\lambda = \dfrac{n}{\sum_{i=1}^n x_i} = \dfrac{1}{\bar{x}}$
>
> **Step 3. Plug in:** $\widehat{E[X_i]} = g(\hat\lambda) = \dfrac{1}{\hat\lambda} = \bar{x}$.
>
> **Answer:** the MLE of the average wait time is the sample mean $\bar X$.
> Numbers (Reading 04, verified by the script): waits $2, 4, 1, 3, 5$ give $\hat\lambda = 5/15 = 1/3$ per minute, so the average wait estimate is $3$ minutes.

> [!note]- My correction
> 

> **Example 1.2.** Suppose you observe a random sample, $X_1, \ldots, X_n$, of wait times for a customer support center. These wait times are modeled as coming from an exponential distribution with parameter $\lambda$. What is the MLE of the variance of the waiting times?

> [!example]- Worked answer (Claude, not in the handout)
> **Step 1.** For the rate form, $\text{Var}(X_i) = \dfrac{1}{\lambda^2}$, so $g(\lambda) = \dfrac{1}{\lambda^2}$.
> **Step 2.** Same MLE as Example 1.1: $\hat\lambda = 1/\bar{x}$. (Same data, same model, so same $\hat\lambda$. Only $g$ changed.)
> **Step 3.** $\widehat{\text{Var}(X_i)} = \dfrac{1}{\hat\lambda^2} = \bar{x}^2$.
>
> **Answer:** $\bar X^2$. With the waits above, $3^2 = 9$ square minutes.
>
> **Trap:** this is NOT the usual sample variance $s^2 = \frac{1}{n-1}\sum (x_i - \bar x)^2$ (that gives $2.5$ for the same data). The MLE uses the model's rule "variance = mean squared". **Change the model and the answer changes.**

> [!note]- My correction
> 

> **Example 1.3.** Suppose that $X_1, \ldots, X_n$ form a random sample from the uniform distribution on $[0, \theta]$, where $\theta > 0$ is unknown. Find the MLE of the median of the distribution.

> [!example]- Worked answer (Claude, not in the handout)
> **Step 1.** The median of $U(0, \theta)$ splits $[0, \theta]$ in half: $m = g(\theta) = \dfrac{\theta}{2}$.
>
> **Step 2. MLE of $\theta$.** The calculus procedure fails here; reason directly.
> - Each density is $f(x_i \mid \theta) = \dfrac{1}{\theta}$ if $0 \le x_i \le \theta$, and $0$ otherwise. Written with an [[Indicator Function]]: $\dfrac{1}{\theta} I(0 \le x_i \le \theta)$.
> - Multiply: $L(\theta \mid \boldsymbol{x}) = \dfrac{1}{\theta^n} \, I(\theta \ge \max_i x_i)$. (All $n$ indicators are 1 only if $\theta$ is at least as big as every $x_i$, i.e. at least the biggest one.)
> - Read it like code: `L(theta) = theta**(-n) if theta >= max(x) else 0`. For $\theta$ below $\max x_i$ it is 0. Above, $\theta^{-n}$ *shrinks* as $\theta$ grows. So the best allowed value is the smallest one: $\theta = \max x_i$.
> - Get: $\hat\theta = M_n = \max(X_1, \ldots, X_n)$. (Setting a derivative to 0 cannot find this: $-n/\theta^{n+1}$ is never 0. The max sits at the edge.)
>
> **Step 3.** $\hat m = g(\hat\theta) = \dfrac{\max(X_1, \ldots, X_n)}{2}$.
>
> **Answer:** half the sample maximum. Numbers (Reading 04): data $2, 7, 4, 9$ give $\hat\theta = 9$, $\hat m = 4.5$. The sample median of that data is $5.5$, a different rule.

> [!note]- My notes
> You should know how to find the median of a dist, and the median is m isuch thtat int m to 0 f (x|theta) dx = 1/2
> so we get x/theta for m to 0 = n / theta for 1/2 and we get m=theta/2 so that becomes our g(theta)=theta/2
> 
> I feel iffy about remembering from rote the median but I got fs that theta/2 makes sense, i would likely forget the max detail and the theta hat
> 




**Fill in:** the pattern in Examples 1.1 to 1.3. What changed between them, and what stayed the same?
- 

---

### 1.2 Consistency
> **Theorem 1.2.** *Let $\hat\theta_n$ be the maximum likelihood estimate for some parameter $\theta$ using a sample size of $n$. Also, let $\theta_T$ represent the true unknown parameter value. Then, as $n \to \infty$, we have that $\hat\theta_n \xrightarrow{P} \theta_T$.*
>
> This tells us that if you have a large enough sample size, the MLE will get very close to the true value of the parameter you're trying to estimate. In other words, as you collect more and more data, the MLE becomes a better and better approximation of the true parameter. In the limit (as the sample size becomes infinite), the MLE will give us the correct "answer".

**Claude's explanation.** Notation first:
- $\hat\theta_n$: the MLE computed from $n$ data points. The subscript $n$ is the sample size.
- $\theta_T$: the true value. $T$ = "true".
- $\xrightarrow{P}$: [[Convergence in Probability|converges in probability]]. It means: pick any error size $\varepsilon > 0$ you like. The chance that $\hat\theta_n$ misses $\theta_T$ by more than $\varepsilon$ goes to 0 as $n$ grows:
$$P\big(|\hat\theta_n - \theta_T| > \varepsilon\big) \to 0 \quad \text{as } n \to \infty.$$

What it does NOT say (Reading 04 6.2): it does not say every extra data point moves the estimate closer, and it does not promise a small error at any particular $n$. It is a statement about the chance of a big miss.

Concrete case (Reading 04 6.2.1, run in section 5): $U(0, 10)$, MLE = max, tolerance $\varepsilon = 1$. The chance of missing by more than 1 is $0.9^n$:

| $n$ | $P(\lvert M_n - 10\rvert > 1)$ |
|---|---|
| 5 | 0.590 |
| 20 | 0.122 |
| 50 | 0.005 |

Related notes: [[Consistency of the MLE]], [[Consistent Estimator]], [[Law of Large Numbers]] (the reason $\bar X$ is consistent).

> [!note]- My notes
> Sub n is saying the sample size is n, bc this is an asymptotic result? This for some reason justfies a differnt sample size? So as n tends towards inf that theta hat converges to 
> However I do not recall what it means to converge in probability upon, the definition is that the limit n-> pr (P |thetahat - theta_t| < epsilon ) = 1 for any positive value of epsilon
> The core of this is to say that as n grows we grow towards perfection. This says nothing about YOUR data, it just says that its preferable that as n grows towards infinity it tends towards perfection not another outcome


**Fill in:** consistency in one sentence, no symbols.
- 

---

### 1.3 Is the MLE unbiased?
> One desirable property of estimators is unbiasedness. What exactly does this mean?
> The **bias** of an estimator is the difference between its expected value (on average, what it estimates) and the true value of the parameter. Formally, for an estimator $\hat\theta$ of a parameter $\theta$, the bias is:
> $$\text{Bias}(\hat\theta) = \mathbb{E}[\hat\theta] - \theta.$$
> - If $\text{Bias}(\hat\theta) = 0$, the estimator is **unbiased**.
> - If $\text{Bias}(\hat\theta) \neq 0$, the estimator is **biased**.
>
> It turns out that the MLE is not always unbiased, especially for small sample sizes. However we saw previously that the MLE is consistent, meaning it converges to the true value of the parameter as the sample size grows. This means that the bias tends to zero as the sample size grows.

**Claude's explanation.** $\mathbb{E}[\hat\theta]$ is the average of the estimator over many imaginary repeats of the whole study at the same $n$, with the true $\theta$ held fixed. Bias = that average minus the truth. Positive = too high on average, negative = too low. See [[Bias of an Estimator]], [[Unbiased Estimator]], and [[Mean Squared Error (MSE)]] (bias is one of its two parts).

Consistency vs unbiasedness, which are easy to mix up:

| | Question | Holds $n$ fixed? |
|---|---|---|
| Unbiased | Is the *average* over repeats equal to $\theta$? | yes, one $n$ |
| Consistent | Does the chance of a big miss go to 0 as $n$ grows? | no, $n \to \infty$ |

> [!note]- My notes
> Bias is the difference bteween ON AVG the truth (our data) and what we expect. So the long run average of the estimator and our truth (theta). The bias going to 0 alone does not make it consistent. However certainly, if bias is not 0 it cannot be consistent. 
> The MLE is NOT always unbiased, it depends on the model used and the n if small; however, see example on bias

> **Example 1.4.** Suppose $X_1, X_2, \ldots, X_n$ are i.i.d. random variables from $U(0, \theta)$, where $\theta > 0$ is the unknown maximum. The MLE for $\theta$ is:
> $$\hat\theta = \max(X_1, X_2, \ldots, X_n).$$
> Is $\hat\theta$ Unbiased? Calculate the expected value of $\hat\theta$.

> [!example]- Worked answer (Claude, not in the handout)
> To get $E[\max]$ you need the distribution of the max. Get its CDF first, then the pdf, then integrate. (Method note: [[Distribution of the Sample Maximum and Minimum]].)
>
> **Step 1. CDF of the max.** Given: each $X_i \sim U(0,\theta)$, so $P(X_i \le m) = \dfrac{m}{\theta}$ for $0 \le m \le \theta$.
> Do: "the max is $\le m$" is the same event as "every $X_i \le m$". Independence lets you multiply.
> $$F_{M_n}(m) = P(M_n \le m) = P(X_1 \le m, \ldots, X_n \le m) = \prod_{i=1}^n P(X_i \le m) = \left(\frac{m}{\theta}\right)^n$$
>
> **Step 2. pdf.** Do: differentiate the CDF in $m$ (power rule, $\theta$ is a constant).
> $$f_{M_n}(m) = \frac{n\, m^{n-1}}{\theta^n}, \quad 0 < m < \theta$$
>
> **Step 3. Expectation.** Do: $E[M_n] = \int m \, f(m)\, dm$ ([[Expectation of a Continuous Random Variable]]).
> $$E[M_n] = \int_0^\theta m \cdot \frac{n m^{n-1}}{\theta^n}\, dm = \frac{n}{\theta^n}\int_0^\theta m^n\, dm = \frac{n}{\theta^n}\cdot\frac{\theta^{n+1}}{n+1} = \frac{n}{n+1}\,\theta$$
>
> **Step 4. Bias.** $\text{Bias} = \dfrac{n}{n+1}\theta - \theta = -\dfrac{\theta}{n+1}$.
>
> **Answer:** No, $\hat\theta$ is biased low. It can never be above $\theta$, so it falls short on average by $\theta/(n+1)$. The bias goes to 0 as $n$ grows, which fits the consistency theorem. So this estimator is **biased and consistent**.
>
> **Fix (Reading 04 6.4.3):** $\tilde\theta = \dfrac{n+1}{n} M_n$ has $E[\tilde\theta] = \theta$, so it is unbiased. It is *not* the MLE.
>
> Check with $\theta = 10$ (formula and a 20,000-sample simulation, section 5):
>
> | $n$ | $E[M_n]$ | bias | average of $\frac{n+1}{n}M_n$ |
> |---|---|---|---|
> | 5 | 8.33 | -1.67 | 10.00 |
> | 20 | 9.52 | -0.48 | 10.00 |
> | 100 | 9.90 | -0.10 | 10.00 |

> [!note]- My notes
> We want to know is our MLE theta hat unbiased
> We need E(thetahat) of our mle
> we know that theta hat is the max, so if we want the expectation, we need the dist of the data
> So we need to find the dist of theta hat or the maximum obsv. x values...
> We'll get that dist by starting with CDF: Let Y=max(data), we want the cdf of y
> We look at the cdf first, bc we know if we differentiate the cdf we get to the pdf, so its convienet and it relies on our property of ind. 
> Order statistics says this is the proepr way to do this
> The def of the CDF is F_y(y)=P(Y les than or equal to y), so if max is less than, every single little x is less than.... so we can say P(X_1<y,...,X_n<y) in plain words if the max is true, true for all...
> So now joint pr statement, bc independent, they multiply so we can call that term due to due to ind. the P(x_1 less than or equal to y)...probabilty of xn less than or equal to little y...
> bc iid they're all the same as well.
> How do we get the p of one then?
> 
> If we int. this statement we can get the individual pdf and we int from 0 to y for 1/theta dx to the nth power
> When we integrate we get y over theta to the nth power for y between 0 and theta
> little y is just notation for the cdf of the maximum btw an arbitrary realized valco
> Big Y is the max, little y is some arbit val that big Y could take
> 
> We're gonna dif ina  moment, but bc we had the cdf of y with a joint p statement... it factors into the internal model
> CDF for  max here we got that from the factor of independence
> 
> D of dy of the cdf 
> to the nth power, outside of that interval, we diff. to get the pdf of y 
> E(y)= int theta 0 y fy (y) dy = int theta to 0 n y ^ n over theta to the nth power dy = n/n+1 * 1/theta to the nth power for theta to the n+1 power which gives n for n+1 * theta
> 
> THIS SHOULD ALL BE P THEORY AND REVIEW FOR US, BC this is not stats, it relies on math details for stats 131 where we cheated to get to the MLE for the maxium, but all else is 131finite sample size it is biased bc any sample size is not theta
> 
> and now we can answer the question is unbiased we get (n/n+1)\*theta
> 
> IF bias is dif between expectation and theta so bias tends to 0 as data inc. but for any 
> 
> SO (n/n+1)theta =/= theta ergo biased 
> 
> You can account for this by adding the bias back in?
> 
> 




> 

**Fill in:** why can the max never overestimate $\theta$? What does that force about the sign of the bias?
- 

---

## 5. Run it locally (Claude)
Script: `70 Files/Courses/stat132/w4_ch6_mle_properties.py`. It computes every example above, checks them by simulation, and draws Figure 6.1 from the reading.

```bash
cd ~/Documents/"Second Brain"/"70 Files/Courses/stat132"
~/.local/share/stat132-venv/bin/python w4_ch6_mle_properties.py
```

Output (run 2026-10-13):
```text
=== Ex 1.1 / 6.1.1  average wait, Exponential(lambda) ===
given waits      [2, 4, 1, 3, 5]
lambda_hat       n/sum = 5/15 = 0.3333 per minute
mean = 1/lambda  -> MLE 3.0000 minutes (= x_bar)

=== Ex 1.2 / 6.1.2  variance of waits ===
var = 1/lambda^2 -> MLE 9.0000 square minutes (= x_bar^2)
compare: usual sample variance s^2 = 2.5000  (different rule, no model)

=== Ex 1.3 / 6.1.3  median of U(0, theta) ===
given sample     [2, 7, 4, 9]
theta_hat = max  9
median = theta/2 -> MLE 4.5
compare: sample median = 5.5  (different rule)

=== 6.2.1  consistency: P(|M_n - 10| > 1) = 0.9^n ===
n =    5  exact 0.5905
n =   20  exact 0.1216
n =   50  exact 0.0052
n =  200  exact 0.0000
simulation check (5000 samples each):
n =    5  simulated 0.5956
n =   20  simulated 0.1200
n =   50  simulated 0.0050

=== Ex 1.4 / 6.4  bias of theta_hat = max, theta = 10 ===
    n  E[M_n] formula  E[M_n] sim     bias  (n+1)/n * M_n sim
    5            8.33        8.33    -1.67              10.00
   20            9.52        9.52    -0.48              10.00
  100            9.90        9.90    -0.10              10.00
```

![[w4-fig6.1-uniform-max.png]]
*5,000 samples per panel. Dashed red = true $\theta = 10$; solid blue = $E[\max] = \frac{n}{n+1}\theta$. Gap between them = bias (shrinks with $n$). Width of the pile = spread (shrinks with $n$, which is consistency).*

Things to try: change `waits` to your own numbers; change `theta` or the `n` list; replace `lambda t: t / 2` with another $g$.

---

## Links
- Week hub and quiz: [[STAT 132 Week 4]]
- Reading: [[STAT 132 Reading 04 - MLE Properties and Sampling Distributions]] (chapter 6 = this lecture, with R code)
- Next: [[STAT 132 Lecture 7 - Sampling Distributions]]
- Practice: [[STAT 132 Discussion 3 - MLE practice]] (Q4 and Q5 are invariance problems)
- Cards that already exist: [[STAT 132 Cards - DeGroot 7.6 Properties of MLEs]]
