---
type: study
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
exam: "STAT 132 Midterm 2 (Tue 2026-11-10, 3:20pm)"
---
# STAT 132 Midterm 2 Review

**Exam:** Tuesday Nov 10, 3:20pm, Porter 144. Closed book, one single-sided handwritten sheet.

**Solutions:** the worked solution sits directly under each problem (see *How to read the solutions* below). The same solutions are also collected in [[STAT 132 Midterm 2 Solutions]].

**How this was built.** Every problem below is copied verbatim from the course handouts (symbols checked against the page images). The order is **Homework first, then Discussion, then Lecture**. Scope comes from the *Midterm 2 Review Guide* (`Review_2.pdf`): a problem is in only if it tests one of the guide's five headings. Each problem is tagged with the heading it tests, written as **§1 to §5**.

Sources: `HW_3.pdf`, `HW_4.pdf`, `Disc_6.pdf` (Downloads); `stat132-disc04-w25.pdf`, `stat132-disc05-w25.pdf`, `stat132-lec07.pdf` to `stat132-lec11.pdf` (vault `70 Files/Courses/stat132`).
Lecture transcripts (auto-captions, Oct 22 to Nov 5): `~/Documents/STAT132/Recordings/STAT132 Transcript <date>.pdf`.
Your worked answers already on disk: `~/Downloads/Disc_6_notes.pdf` (your handwritten Discussion 6 solutions), `~/Downloads/STAT132_HW4_Solutions.docx`.

## The guide's five headings (the filter)

| § | Review guide heading | Homework | Discussion | Lecture |
|---|---|---|---|---|
| §1 | Sampling Distributions | HW3 #4 | Disc 4 #1 to #5 | L7 Ex 1.1 to 1.3, L7 §1.4 |
| §2 | The $\chi^2$ Distribution | HW3 #1 to #4 | Disc 5 #1 to #5 | L8 Ex 1.1, 2.1 to 2.3 |
| §3 | Sample Mean and Sample Variance for a Normal Population | HW3 #1, #5; HW4 #4 | Disc 5 #4, #5 | L9 proofs, L9 Ex 1.1 to 1.3 |
| §4 | The $t$ Distribution | HW4 #1, #3 | Disc 6 #1 | L10 Thm 2.1, Ex 3.1 to 3.4 |
| §5 | Interval Estimation | HW4 #2 to #5 | Disc 6 #2 to #4 | L11 Thm 2.1, 2.2, Ex 2.1, 2.2, 4.1, 4.2, §3 |

The "know how" lines from the guide, verbatim:

> - Be able to find the sampling distribution for different MLEs such as the mean of a normal distribution, the upper bound of a uniform distribution, etc.
> - Know how to use the $\chi^2$ table to determine probabilities or quantiles.
> - Know how to use the $t$ table to determine probabilities or quantiles.
> - Know how to find confidence intervals for other parameters such as the variance of a normal distribution.
> - Understand the long-run frequency interpretation of the confidence interval.

**Left out (not under any guide heading):** Discussion 7 and Lecture 12 (unbiased estimators), Lecture 13 (hypothesis testing), Lecture 11 §5 (Bayesian credible intervals), Discussions 1 to 3 and Lectures 1 to 6 (Midterm 1 material).

## What the professor said about this exam (lecture transcripts)

Quoted verbatim from the auto-captions (caption errors kept, e.g. "kai squared" for $\chi^2$).

**Cutoff** (Nov 5):
> That's up to everything that will be included on the exam. Today I'm going to give one more lecture on unbiased estimators. This will not be on the exam, but I'll talk a bit about the exam at the end.

**Format** (Nov 5):
> Same as last time, four questions, multiple subparts.

**Tables you get** (Nov 5):
> So I will give you the same table from last time, but there won't be any new distributions on it. And I will give you the kai squared and T probability tables that were in the lecture notes. But I won't give you any new PDFs, for example.

**No separate normal table** (Oct 29):
> I don't give you a separate standard normal probability table. You can use this row of the T table for any probabilities involving the standard normal distribute.

(Nov 5: "the t table I gave you has a row for degrees of freedom infinity, which is the standard normal.")

**Proofs** (Nov 5):
> Any proofs that I've given you in class you should be familiar with.

**Cumulative** (Nov 5):
> So it's focusing on the topic since midterm one, but the material is cumulative in the sense that it builds on itself. We're using the properties from earlier. So you still want to be familiar with those.

**Sampling distributions** (Nov 5):
> Anything could come up when we talk about sampling distributions, but I can't say which one or ones would show up or not.

**How to study** (Nov 5):
> I don't post any old exams. Yeah, so if you want study material, I recommend first going through the course notes that we do in class, specifically all the examples that we do, then the discussion section problems, then homework problems, and then if you want more problems, you can look through textbook problems, but I think that's sufficient without that.

Note: his suggested order is lecture examples, then discussion, then homework. This review keeps your order (homework first); every part is here either way.

**Note sheet** (Nov 5):
> Don't forget to make your note sheet. One side, standard paper size, handwritten notes.

The full recap he gave is in the **Appendix** at the end.

### Which transcript covers which problems

| Lecture day | Transcript file (Downloads) | What was worked out loud |
|---|---|---|
| Thu Oct 22 | `16982032_English.pdf` | L7 recap; L8 $\chi^2$ table, Ex 2.1 to 2.3; extra-credit quiz 1 |
| Tue Oct 27 | `17030082_English.pdf` | L8 recap; L9 sample mean and variance |
| Thu Oct 29 | `17054530_English.pdf` | L9 to L10: $t$ table, Ex 3.1 to 3.4; extra-credit quiz 2 |
| Tue Nov 3 | `17102235_English.pdf` | L11: CIs for a normal mean (known and unknown variance), interpretation, CI for a variance |
| Thu Nov 5 | `17124220_English.pdf` | L11 recap; L12 unbiased estimators (not on exam); exam recap |

## How to read the solutions

Every problem below is followed by its worked solution (Claude's, not the professor's). Numbers use the exam tables ($\chi^2$ and $t$ from the lecture notes); exact software values are in brackets where they differ.

**Notation used throughout**
- $\widehat{\sigma^2} = \frac{1}{n}\sum (X_i - \bar X)^2$ (MLE, divide by $n$); $S^2 = \frac{1}{n-1}\sum (X_i - \bar X)^2$ (divide by $n-1$). Note $n\widehat{\sigma^2} = (n-1)S^2$.
- $\chi^2_{m,p}$ and $t_{m,p}$ are the $p$ quantiles: $\mathbb{P}(X \le \chi^2_{m,p}) = p$. That is how the tables read.
- $z_p$ is the standard normal $p$ quantile, read from the $t$ table's $\infty$ row ($z_{0.95} = 1.645$, $z_{0.975} = 1.960$, $z_{0.995} = 2.576$).
- $\text{Gamma}(\alpha, \beta)$ uses the rate $\beta$: density $\frac{\beta^\alpha}{\Gamma(\alpha)}x^{\alpha-1}e^{-\beta x}$. So $\chi^2_m = \text{Gamma}(m/2, 1/2)$.

**The five facts almost every problem uses** (review guide §2 to §4)
1. $Z \sim N(0,1) \Rightarrow Z^2 \sim \chi^2_1$, and independent $\chi^2$'s add: $Z_1^2 + \cdots + Z_m^2 \sim \chi^2_m$.
2. $X \sim \chi^2_m \Rightarrow cX \sim \text{Gamma}\left(\frac{m}{2}, \frac{1}{2c}\right)$.
3. Normal sample: $\bar X \sim N\left(\mu, \frac{\sigma^2}{n}\right)$, $\frac{n\widehat{\sigma^2}}{\sigma^2} = \frac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1}$, and $\bar X$ is independent of $\widehat{\sigma^2}$.
4. $Z \sim N(0,1)$ independent of $Y \sim \chi^2_m \Rightarrow \frac{Z}{\sqrt{Y/m}} \sim t_m$. Hence $\frac{\sqrt n(\bar X - \mu)}{S} \sim t_{n-1}$.
5. Confidence interval recipe: find a pivotal $Q$, write $\mathbb{P}(c_1 \le Q \le c_2) = 1 - \alpha$ with table quantiles, then solve the inequality for the parameter.

---

# Part 1: Homework

## Homework 3

### HW3 #1 · §2, §3
> Suppose that you observe a random sample, $X_1, \ldots, X_n$, from the normal distribution with mean $\mu$ and variance $\sigma^2$. Find the distribution of
> $$\frac{n(\bar{X} - \mu)^2}{\sigma^2}.$$

^hw3-q1

#### Solution

**Given:** $X_i \overset{iid}{\sim} N(\mu, \sigma^2)$.
**Idea:** the expression is the square of a standard normal.

1. $\bar X \sim N\left(\mu, \frac{\sigma^2}{n}\right)$ (fact 3).
2. Standardize: $Z = \frac{\bar X - \mu}{\sigma/\sqrt n} = \frac{\sqrt n(\bar X - \mu)}{\sigma} \sim N(0,1)$. *Why:* subtract the mean, divide by the standard deviation.
3. Square it: $Z^2 = \frac{n(\bar X - \mu)^2}{\sigma^2}$. That is exactly the expression.
4. $Z^2 \sim \chi^2_1$ (fact 1).

**Answer:** $\dfrac{n(\bar X - \mu)^2}{\sigma^2} \sim \chi^2_1$.

### HW3 #2 · §2
> Suppose that a point $(X, Y, Z)$ is to be chosen at random in three-dimensional space, where $X$, $Y$, and $Z$ are independent random variables, each following a standard normal distribution. What is the probability that the distance from the origin to the random point will be less than 1?

^hw3-q2

#### Solution

**Given:** $X, Y, Z \overset{iid}{\sim} N(0,1)$.
**Idea:** distance less than 1 is the same as squared distance less than 1, and squared distance is a sum of three squared standard normals.

1. Distance from origin $= \sqrt{X^2 + Y^2 + Z^2}$.
2. $\sqrt{W} < 1 \iff W < 1$ since both sides are nonnegative. So we need $\mathbb{P}(X^2 + Y^2 + Z^2 < 1)$.
3. $W = X^2 + Y^2 + Z^2 \sim \chi^2_3$ (fact 1, three independent squared standard normals).
4. From the $\chi^2_3$ row: $\chi^2_{3,0.10} = 0.584$ and $\chi^2_{3,0.25} = 1.213$, so $\mathbb{P}(W < 1)$ is between 0.10 and 0.25, about 0.2.

**Answer:** $\mathbb{P}(\chi^2_3 < 1) \approx 0.20$ [exact 0.1987].

### HW3 #3 · §2 !CHECK
> If a random variable $X$ follows a $\chi^2$ distribution with $m$ degrees of freedom, then the distribution of $X^{1/2}$ is called a chi ($\chi$) distribution with $m$ degrees of freedom. Determine the mean of this chi distribution.

^hw3-q3

#### Solution

**Given:** $X \sim \chi^2_m$ with density $f(x) = \frac{1}{2^{m/2}\Gamma(m/2)}x^{m/2-1}e^{-x/2}$, $x > 0$.
**Idea:** $E(X^{1/2}) = \int x^{1/2} f(x)\,dx$, and the integrand is an unnormalized gamma density, so use the gamma integral $\int_0^\infty x^{a-1}e^{-x/2}dx = \Gamma(a)\,2^{a}$.

1. $E(X^{1/2}) = \frac{1}{2^{m/2}\Gamma(m/2)}\int_0^\infty x^{\frac{m+1}{2}-1}e^{-x/2}\,dx$. *Why:* $x^{1/2}\cdot x^{m/2-1} = x^{(m+1)/2 - 1}$.
2. The integral is the gamma integral with $a = \frac{m+1}{2}$: it equals $\Gamma\left(\frac{m+1}{2}\right)2^{(m+1)/2}$.
3. Divide: $\frac{2^{(m+1)/2}}{2^{m/2}} = \sqrt 2$.

**Answer:**
$$E\left(X^{1/2}\right) = \frac{\sqrt 2\,\Gamma\left(\frac{m+1}{2}\right)}{\Gamma\left(\frac{m}{2}\right)}.$$
Check with $m = 1$: $\sqrt2\,\Gamma(1)/\Gamma(1/2) = \sqrt{2/\pi} \approx 0.798 = E|Z|$, which is right since $X^{1/2} = |Z|$.

### HW3 #4 · §2 (and §1: CLT)
> Suppose that $X$ has the $\chi^2$ distribution with 200 degrees of freedom. Explain why the central limit theorem can be used to determine the approximate value of $\mathbb{P}(160 < X < 240)$ and find this approximate value.

^hw3-q4

#### Solution

**Given:** $X \sim \chi^2_{200}$.
**Idea:** a $\chi^2_{200}$ is a sum of 200 iid pieces, so the CLT says it is roughly normal.

1. *Why the CLT applies:* $X$ has the same distribution as $\sum_{i=1}^{200} Z_i^2$ with $Z_i^2 \overset{iid}{\sim} \chi^2_1$. Each piece has mean 1 and variance 2 (finite), and 200 is large, so the sum is approximately normal.
2. Mean and variance: $E(X) = m = 200$, $\text{Var}(X) = 2m = 400$, so $SD = 20$.
3. Standardize the endpoints: $\frac{160 - 200}{20} = -2$, $\frac{240 - 200}{20} = 2$.
4. $\mathbb{P}(160 < X < 240) \approx \mathbb{P}(-2 < Z < 2) = 2\Phi(2) - 1 = 2(0.9772) - 1$.

**Answer:** $\approx 0.954$ [exact $\chi^2$ value 0.955].

### HW3 #5 · §3 (uses the $\chi^2$ table, §2)
> Let $X_1, \ldots, X_n$ be a random sample from the normal distribution with mean $\mu$ and variance $\sigma^2$. Also let $\widehat{\sigma^2}$ denote the sample variance. Find the smallest value of $n$ for which the below expression is satisfied:
> $$\mathbb{P}\left(\frac{\widehat{\sigma^2}}{\sigma^2} \le 1.5\right) \ge 0.95$$

^hw3-q5

#### Solution

**Given:** normal sample, $\widehat{\sigma^2}$ = sample variance (MLE form, divide by $n$).
**Idea:** turn $\widehat{\sigma^2}/\sigma^2$ into the $\chi^2$ quantity, then search the table.

1. Multiply inside by $n$: $\frac{\widehat{\sigma^2}}{\sigma^2} \le 1.5 \iff \frac{n\widehat{\sigma^2}}{\sigma^2} \le 1.5n$. *Why:* multiplying both sides by $n > 0$ keeps the inequality.
2. $\frac{n\widehat{\sigma^2}}{\sigma^2} \sim \chi^2_{n-1}$ (fact 3). So the condition is $\mathbb{P}(\chi^2_{n-1} \le 1.5n) \ge 0.95$, i.e. $1.5n \ge \chi^2_{n-1,\,0.95}$.
3. Search the 0.95 column:

| $n$ | $1.5n$ | $\chi^2_{n-1,0.95}$ | OK? |
|---|---|---|---|
| 19 | 28.5 | 28.87 | no |
| 20 | 30.0 | 30.14 | no |
| 21 | 31.5 | 31.41 | yes |

**Answer:** $n = 21$.

## Homework 4

### HW4 #1 · §4
> Suppose that six random variables $X_1, \ldots, X_6$ are independently sampled from a standard normal distribution. Find a value for the constant $c$ such that the random variable
> $$U = \frac{c(X_1 - X_2)}{\sqrt{X_3^2 + X_4^2 + X_5^2 + X_6^2}}$$
> will have a $t$ distribution. What will be the degrees of freedom parameter for the $t$ distribution?

^hw4-q1

#### Solution

**Given:** $X_1, \ldots, X_6 \overset{iid}{\sim} N(0,1)$.
**Idea:** build the $t$ recipe $\frac{Z}{\sqrt{Y/m}}$ (fact 4): numerator a standard normal, denominator a $\chi^2$ divided by its df.

1. Numerator: $X_1 - X_2 \sim N(0, 1 + 1) = N(0, 2)$. *Why:* variances of independent variables add, even for a difference. So $Z = \frac{X_1 - X_2}{\sqrt 2} \sim N(0,1)$.
2. Denominator: $Y = X_3^2 + X_4^2 + X_5^2 + X_6^2 \sim \chi^2_4$, independent of $Z$ (different $X$'s).
3. $t$ variable: $T = \frac{Z}{\sqrt{Y/4}} = \frac{(X_1 - X_2)/\sqrt2}{\sqrt Y/2} = \frac{2}{\sqrt 2}\cdot\frac{X_1 - X_2}{\sqrt Y} = \sqrt2\,\frac{X_1 - X_2}{\sqrt Y}$.
4. Match with $U = \frac{c(X_1 - X_2)}{\sqrt Y}$.

**Answer:** $c = \sqrt 2$, and $U \sim t_4$ (4 degrees of freedom).

### HW4 #2 · §5
> A pharmaceutical company is testing the effectiveness of a new drug. The measured reduction in blood pressure (in mmHg) of patients follows a normal distribution with unknown mean $\mu$ and known variance $\sigma^2 = 4$. To ensure that their 99% confidence interval for the average reduction in blood pressure has a total length no greater than 1 mmHg, how many patients must be included in the study?

^hw4-q2

#### Solution

**Given:** $\sigma^2 = 4$ known, so $\sigma = 2$; 99% CI; length $\le 1$.
**Idea:** known-variance CI $\bar X \pm z_{1-\alpha/2}\frac{\sigma}{\sqrt n}$ has length $2z_{1-\alpha/2}\frac{\sigma}{\sqrt n}$, which does not depend on the data. Solve for $n$.

1. 99% means $\alpha = 0.01$, so $z_{0.995} = 2.576$.
2. Length $= 2(2.576)\frac{2}{\sqrt n} = \frac{10.304}{\sqrt n} \le 1$.
3. $\sqrt n \ge 10.304 \Rightarrow n \ge 106.17$.
4. $n$ must be a whole number and the length must not exceed 1, so round **up**.

**Answer:** $n = 107$ patients.

### HW4 #3 · §5 (uses the $t$ table, §4)
> Suppose that a random sample of eight observations is taken from the normal distribution with unknown mean $\mu$ and unknown variance $\sigma^2$, and that the observed values are 3.1, 3.5, 2.6, 3.4, 3.8, 3.0, 2.9, and 2.2. Find the following:
>
> (a) A 90% equal-tailed confidence interval for $\mu$
> (b) A 95% equal-tailed confidence interval for $\mu$
> (c) A 99% equal-tailed confidence interval for $\mu$

^hw4-q3

#### Solution

**Given:** $n = 8$, $\mu$ and $\sigma^2$ unknown.
**Idea:** unknown variance, so use $\bar X \pm t_{n-1,1-\alpha/2}\frac{S}{\sqrt n}$ with $n - 1 = 7$.

1. $\bar x = \frac{24.5}{8} = 3.0625$.
2. $\sum x_i^2 = 76.87$, so $S^2 = \frac{\sum x_i^2 - n\bar x^2}{n-1} = \frac{76.87 - 8(3.0625)^2}{7} = \frac{1.83875}{7} = 0.26268$, $S = 0.5125$.
3. Standard error: $\frac{S}{\sqrt 8} = 0.1812$.
4. Quantiles from the $t_7$ row: $t_{7,0.95} = 1.895$, $t_{7,0.975} = 2.365$, $t_{7,0.995} = 3.499$. *Why these columns:* a $1-\alpha$ interval puts $\alpha/2$ in each tail, so you read the $1 - \alpha/2$ column.

| level | quantile | half-width | interval |
|---|---|---|---|
| 90% | 1.895 | 0.343 | $(2.719,\ 3.406)$ |
| 95% | 2.365 | 0.429 | $(2.634,\ 3.491)$ |
| 99% | 3.499 | 0.634 | $(2.428,\ 3.697)$ |

**Answer:** (a) $(2.719, 3.406)$; (b) $(2.634, 3.491)$; (c) $(2.428, 3.697)$. Higher confidence means a wider interval.

### HW4 #4 · §5, §3
> Suppose that $X_1, \ldots, X_5$ form a random sample from a normal distribution with unknown mean $\mu$ and unknown variance $\sigma^2$. Let $L$ be the random variable representing the length of a 95% equal-tailed confidence interval for $\mu$. Find $E(L^2)$.

^hw4-q4

#### Solution

**Given:** $n = 5$, 95% $t$ interval.
**Idea:** the length is $2t\frac{S}{\sqrt n}$, a constant times $S$, so $E(L^2)$ only needs $E(S^2)$.

1. $L = 2\,t_{4,0.975}\frac{S}{\sqrt 5}$ with $t_{4,0.975} = 2.776$.
2. $L^2 = \frac{4\,t_{4,0.975}^2}{5}S^2$.
3. $E(S^2) = \sigma^2$. *Why:* $\frac{4S^2}{\sigma^2} \sim \chi^2_4$ has mean 4, so $E(S^2) = \frac{\sigma^2}{4}\cdot 4 = \sigma^2$.
4. $E(L^2) = \frac{4(2.776)^2}{5}\sigma^2 = \frac{4(7.706)}{5}\sigma^2$.

**Answer:** $E(L^2) \approx 6.165\,\sigma^2$.

### HW4 #5 · §5 (CI for a variance)
> A company produces glass bottles, and the thickness of the bottles is known to follow a normal distribution with an unknown variance $\sigma^2$. The company wants to ensure that the thickness does not vary too much between bottles. A random sample of 15 bottles is taken, and the sample variance is found to be $S^2 = 0.0225$ cm². Construct a 95% confidence interval for the population variance $\sigma^2$.

^hw4-q5

#### Solution

**Given:** $n = 15$, $S^2 = 0.0225$.
**Idea:** pivotal $Q = \frac{(n-1)S^2}{\sigma^2} \sim \chi^2_{14}$; its distribution has no $\sigma^2$ in it.

1. $\mathbb{P}\left(\chi^2_{14,0.025} \le \frac{14S^2}{\sigma^2} \le \chi^2_{14,0.975}\right) = 0.95$, with $\chi^2_{14,0.025} = 5.629$, $\chi^2_{14,0.975} = 26.12$.
2. Solve for $\sigma^2$. Taking reciprocals flips the inequalities: $\frac{14S^2}{26.12} \le \sigma^2 \le \frac{14S^2}{5.629}$. *Why the flip:* $1/x$ is decreasing for $x > 0$, so the big quantile goes to the lower bound.
3. $14S^2 = 0.315$.

**Answer:** $\left(\frac{0.315}{26.12},\ \frac{0.315}{5.629}\right) = (0.01206,\ 0.05596)$ cm⁴ (units of thickness squared).

---

# Part 2: Discussion problems

## Discussion Section 4 (Sampling distributions)

### Disc 4 #1 · §1 (MLE of a uniform upper bound)
> Suppose that a random sample $X_1, \ldots, X_n$ is to be taken from the uniform distribution on the interval $[0, \theta]$ where $\theta > 0$ is unknown. How large must the sample size be to ensure that
> $$\mathbb{P}(|\max\{X_1, \ldots, X_n\} - \theta| \le 0.1\theta) \ge 0.95?$$

^disc-4-q1

#### Solution

**Given:** $X_i \overset{iid}{\sim} U[0,\theta]$, $Y = \max X_i$.
**Idea:** $Y \le \theta$ always, so the absolute value only has one side to worry about. Then use the CDF of the max (L7 Ex 1.3).

1. $Y \le \theta$, so $|Y - \theta| = \theta - Y$, and $\theta - Y \le 0.1\theta \iff Y \ge 0.9\theta$.
2. $\mathbb{P}(Y \le y) = \left(\frac{y}{\theta}\right)^n$. *Why:* the max is below $y$ only if every $X_i$ is, and they are independent.
3. $\mathbb{P}(Y \ge 0.9\theta) = 1 - 0.9^n \ge 0.95 \iff 0.9^n \le 0.05$.
4. Take logs (log of a number below 1 is negative, so the inequality flips): $n \ge \frac{\ln 0.05}{\ln 0.9} = \frac{-2.996}{-0.1054} = 28.43$.

**Answer:** $n = 29$.

### Disc 4 #2 · §1
> Suppose that a random sample is to be taken from the normal distribution with unknown mean $\mu$ and known variance $\sigma^2 = 4$. How large must the sample size be to ensure that
> $$\mathbb{E}\left(|\bar{X}_n - \mu|^2\right) \le 0.1?$$

^disc-4-q2

#### Solution

**Idea:** $E|\bar X_n - \mu|^2$ is the definition of $\text{Var}(\bar X_n)$, because $E(\bar X_n) = \mu$.

1. $E|\bar X_n - \mu|^2 = \text{Var}(\bar X_n) = \frac{\sigma^2}{n} = \frac{4}{n}$.
2. $\frac{4}{n} \le 0.1 \iff n \ge 40$.

**Answer:** $n = 40$.

### Disc 4 #3 · §1
> Suppose that a random sample is to be taken from the normal distribution with unknown mean $\mu$ and known variance $\sigma^2 = 4$. How large must the sample size be to ensure that
> $$\mathbb{P}(|\bar{X}_n - \mu| \le 0.1) \ge 0.95?$$

^disc-4-q3

#### Solution

**Idea:** standardize $\bar X_n$, then use the normal quantile.

1. $\frac{\bar X_n - \mu}{2/\sqrt n} = Z \sim N(0,1)$.
2. $|\bar X_n - \mu| \le 0.1 \iff |Z| \le \frac{0.1\sqrt n}{2} = 0.05\sqrt n$.
3. $\mathbb{P}(|Z| \le a) \ge 0.95 \iff a \ge z_{0.975} = 1.96$. *Why 0.975:* 0.95 in the middle leaves 0.025 in each tail.
4. $0.05\sqrt n \ge 1.96 \Rightarrow \sqrt n \ge 39.2 \Rightarrow n \ge 1536.64$.

**Answer:** $n = 1537$.

### Disc 4 #4 · §1
> Let $X_1, \ldots, X_n$ be a random sample from the exponential distribution with parameter $\lambda$. Find the CDF for the sampling distribution of the MLE of $\lambda$.

^disc-4-q4

#### Solution

**Given:** $X_i \overset{iid}{\sim} \text{Exp}(\lambda)$ (rate $\lambda$, mean $1/\lambda$).
**Idea:** the MLE is $\hat\lambda = 1/\bar X$. Its CDF comes from the distribution of $\sum X_i$, which is gamma.

1. MLE: $\ell(\lambda) = n\ln\lambda - \lambda\sum x_i$, $\ell'(\lambda) = \frac{n}{\lambda} - \sum x_i = 0 \Rightarrow \hat\lambda = \frac{n}{\sum X_i} = \frac{1}{\bar X}$.
2. $T = \sum X_i \sim \text{Gamma}(n, \lambda)$. *Why:* a sum of $n$ independent $\text{Gamma}(1,\lambda)$ is $\text{Gamma}(n,\lambda)$.
3. For $t > 0$: $\mathbb{P}(\hat\lambda \le t) = \mathbb{P}\left(\frac{n}{T} \le t\right) = \mathbb{P}\left(T \ge \frac{n}{t}\right)$. *Why it flips:* $n/T$ is decreasing in $T$.
4. Write it out:
$$F_{\hat\lambda}(t) = \int_{n/t}^{\infty}\frac{\lambda^n}{\Gamma(n)}y^{n-1}e^{-\lambda y}\,dy = \sum_{k=0}^{n-1}e^{-n\lambda/t}\frac{(n\lambda/t)^k}{k!},\quad t > 0.$$
The sum form uses the gamma and Poisson link: a $\text{Gamma}(n,\lambda)$ waiting time exceeds $y$ exactly when fewer than $n$ Poisson events happen by time $y$.

**Answer:** $F_{\hat\lambda}(t) = \mathbb{P}\left(\text{Gamma}(n,\lambda) \ge \frac{n}{t}\right)$ as above, and $0$ for $t \le 0$.

### Disc 4 #5 · §1
> Suppose that $X_1, \ldots, X_n$ are a random sample from the Bernoulli distribution with unknown parameter $p$. How large must the sample size be to ensure that
> $$\mathbb{E}(|\bar{X}_n - p|^2) \le 0.01?$$

^disc-4-q5

#### Solution

**Idea:** same as Q2, but the variance depends on the unknown $p$, so plan for the worst $p$.

1. $E|\bar X_n - p|^2 = \text{Var}(\bar X_n) = \frac{p(1-p)}{n}$.
2. $p(1-p)$ is largest at $p = \frac12$, where it equals $\frac14$. *Why:* it is a downward parabola with its peak at $\frac12$.
3. Need $\frac{p(1-p)}{n} \le 0.01$ for every $p$: $\frac{1/4}{n} \le 0.01 \iff n \ge 25$.

**Answer:** $n = 25$.

## Discussion Section 5 ($\chi^2$ and the sample variance)

### Disc 5 #1 · §2
> Find the mode of the $\chi^2_m$ distribution for $m = 1, 2, \ldots$

^disc-5-q1

#### Solution

**Idea:** the mode is where the density is largest. Maximize $\ln f$.

1. $\ln f(x) = \text{const} + \left(\frac m2 - 1\right)\ln x - \frac x2$.
2. $\frac{d}{dx}\ln f = \frac{m/2 - 1}{x} - \frac12 = 0 \Rightarrow x = m - 2$.
3. This is a maximum only if $m - 2 > 0$. For $m = 1$ the density decreases from $+\infty$ at $0$; for $m = 2$ it is $\frac12e^{-x/2}$, decreasing from $x = 0$. Either way the peak is at $0$.

**Answer:** mode $= m - 2$ for $m \ge 3$; mode $= 0$ for $m = 1, 2$. In one line: $\max(m-2, 0)$.

### Disc 5 #2 · §2
> Suppose that a point $(X, Y)$ is to be chosen at random in the $xy$-plane, where $X$ and $Y$ are independent random variables and each has the standard normal distribution. If a circle is drawn in the $xy$-plane with its center at the origin, what is the radius of the smallest circle that can be chosen in order for there to be probability 0.99 that the point $(X, Y)$ will lie inside the circle?

^disc-5-q2

#### Solution

**Idea:** inside a circle of radius $r$ means $X^2 + Y^2 \le r^2$, and $X^2 + Y^2 \sim \chi^2_2$.

1. $\mathbb{P}(X^2 + Y^2 \le r^2) = 0.99 \Rightarrow r^2 = \chi^2_{2,0.99} = 9.210$.
2. Check by hand: $\chi^2_2 = \text{Exp}(1/2)$, so $1 - e^{-r^2/2} = 0.99 \Rightarrow r^2 = 2\ln 100 = 9.210$.
3. $r = \sqrt{9.210}$.

**Answer:** $r \approx 3.035$.

### Disc 5 #3 · §2
> Suppose that six random variables $X_1, \ldots, X_6$ form a random sample from the standard normal distribution, and let
> $$Y = (X_1 + X_2 + X_3)^2 + (X_4 + X_5 + X_6)^2.$$
> Determine a value of $c$ such that the random variable $cY$ will have a $\chi^2$ distribution.

^disc-5-q3

#### Solution

**Idea:** each bracket is a normal with variance 3. Scale each to a standard normal, and the sum of squares becomes $\chi^2_2$.

1. $X_1 + X_2 + X_3 \sim N(0, 3)$, so $\frac{X_1 + X_2 + X_3}{\sqrt3} \sim N(0,1)$. Same for $X_4 + X_5 + X_6$, and the two are independent (no shared $X$'s).
2. $\frac{(X_1 + X_2 + X_3)^2}{3} + \frac{(X_4 + X_5 + X_6)^2}{3} = \frac{Y}{3} \sim \chi^2_2$.

**Answer:** $c = \frac13$, and $\frac{Y}{3} \sim \chi^2_2$.

### Disc 5 #4 · §2, §3
> Assume that $X_1, \ldots, X_n$ form a random sample from the normal distribution with mean $\mu$ and variance $\sigma^2$. Show that $\widehat{\sigma^2}$ has the gamma distribution with parameters $(n-1)/2$ and $n/(2\sigma^2)$.

^disc-5-q4

#### Solution

**Idea:** $\widehat{\sigma^2}$ is a constant times a $\chi^2_{n-1}$; use fact 2.

1. $W = \frac{n\widehat{\sigma^2}}{\sigma^2} \sim \chi^2_{n-1}$ (fact 3).
2. So $\widehat{\sigma^2} = cW$ with $c = \frac{\sigma^2}{n}$.
3. Fact 2: $cW \sim \text{Gamma}\left(\frac{n-1}{2},\ \frac{1}{2c}\right) = \text{Gamma}\left(\frac{n-1}{2},\ \frac{n}{2\sigma^2}\right)$. *Why fact 2 holds:* $\chi^2_{n-1} = \text{Gamma}\left(\frac{n-1}{2}, \frac12\right)$, and multiplying a gamma by $c$ divides its rate by $c$.

**Answer:** shown: $\widehat{\sigma^2} \sim \text{Gamma}\left(\frac{n-1}{2}, \frac{n}{2\sigma^2}\right)$. $\blacksquare$

### Disc 5 #5 · §3, §2
> Suppose that $X_1, \ldots, X_n$ form a random sample from the normal distribution with mean $\mu$ and variance $\sigma^2$. Assuming that the sample size $n = 16$, determine the values of the following probabilities:
>
> (a) $$\mathbb{P}\left(\frac{\sigma^2}{2} \le \frac{1}{n}\sum_{i=1}^{n}(X_i - \mu)^2 \le 2\sigma^2\right)$$
>
> (b) $$\mathbb{P}\left(\frac{\sigma^2}{2} \le \frac{1}{n}\sum_{i=1}^{n}(X_i - \bar{X})^2 \le 2\sigma^2\right)$$

^disc-5-q5

#### Solution

**Idea:** multiply through by $\frac{n}{\sigma^2} = \frac{16}{\sigma^2}$ to get a $\chi^2$ in the middle. The only difference between (a) and (b) is the degrees of freedom: $\mu$ known gives 16, $\bar X$ estimated gives 15.

**(a)** $W = \frac{1}{\sigma^2}\sum(X_i - \mu)^2 = \sum Z_i^2 \sim \chi^2_{16}$.
1. $\frac{\sigma^2}{2} \le \frac{1}{16}\sum(X_i-\mu)^2 \le 2\sigma^2 \iff 8 \le W \le 32$.
2. $\chi^2_{16}$ row: $\chi^2_{16,0.99} = 32.00$ and $\chi^2_{16,0.05} = 7.962$, so $\mathbb{P} \approx 0.99 - 0.05$.

**(b)** $V = \frac{1}{\sigma^2}\sum(X_i - \bar X)^2 = \frac{n\widehat{\sigma^2}}{\sigma^2} \sim \chi^2_{15}$.
1. Same algebra: $8 \le V \le 32$.
2. $\chi^2_{15}$ row: 32 is between $\chi^2_{15,0.99} = 30.58$ and $\chi^2_{15,0.995} = 32.80$, so $F(32) \approx 0.994$; 8 is between $\chi^2_{15,0.05} = 7.261$ and $\chi^2_{15,0.10} = 8.547$, so $F(8) \approx 0.076$.

**Answer:** (a) $\approx 0.94$ [0.939]; (b) $\approx 0.92$ [0.917]. Losing a degree of freedom shifts the distribution left, so a bit more mass falls below 8.

## Discussion Section 6 ($t$ distribution and confidence intervals)

Your handwritten solutions: `~/Downloads/Disc_6_notes.pdf`.

### Disc 6 #1 · §4
> Suppose that five random variables $X_1, \ldots, X_5$ are independently sampled from a standard normal distribution. Find a value for the constant $c$ such that the random variable
> $$U = \frac{c(X_1 + X_2)}{\sqrt{X_3^2 + X_4^2 + X_5^2}}$$
> will have a $t$ distribution.

^disc-6-q1

#### Solution

**Idea:** same as HW4 Q1 with 3 df.

1. $Z = \frac{X_1 + X_2}{\sqrt2} \sim N(0,1)$; $Y = X_3^2 + X_4^2 + X_5^2 \sim \chi^2_3$, independent.
2. $\frac{Z}{\sqrt{Y/3}} = \frac{\sqrt3}{\sqrt2}\cdot\frac{X_1 + X_2}{\sqrt Y}$.

**Answer:** $c = \sqrt{3/2} \approx 1.225$, and $U \sim t_3$.

### Disc 6 #2 · §5
> Suppose that $X_1, \ldots, X_n$ form a random sample from the normal distribution with unknown mean $\mu$ and known variance $\sigma^2$. Let $\Phi(\cdot)$ stand for the CDF of the standard normal distribution, and let $\Phi^{-1}(\cdot)$ be its inverse. Show that the following interval is a $1 - \alpha = \gamma$ confidence interval for $\mu$:
> $$\left(\bar{X} - \Phi^{-1}\!\left(\frac{1+\gamma}{2}\right)\frac{\sigma}{\sqrt{n}},\ \bar{X} + \Phi^{-1}\!\left(\frac{1+\gamma}{2}\right)\frac{\sigma}{\sqrt{n}}\right)$$

^disc-6-q2

#### Solution

**Idea:** show the probability that the interval covers $\mu$ equals $\gamma$. Write $a = \Phi^{-1}\left(\frac{1+\gamma}{2}\right)$.

1. Pivotal: $Z = \frac{\sqrt n(\bar X - \mu)}{\sigma} \sim N(0,1)$.
2. $\mathbb{P}(-a \le Z \le a) = \Phi(a) - \Phi(-a) = 2\Phi(a) - 1$. *Why:* symmetry, $\Phi(-a) = 1 - \Phi(a)$.
3. $\Phi(a) = \frac{1+\gamma}{2}$ by definition of $a$, so $2\Phi(a) - 1 = (1 + \gamma) - 1 = \gamma$.
4. Rearrange $-a \le \frac{\sqrt n(\bar X - \mu)}{\sigma} \le a$: multiply by $\frac{\sigma}{\sqrt n}$, subtract $\bar X$, multiply by $-1$ (flips): $\bar X - a\frac{\sigma}{\sqrt n} \le \mu \le \bar X + a\frac{\sigma}{\sqrt n}$.
5. Same event, so same probability $\gamma$.

**Answer:** $\mathbb{P}\left(\bar X - a\frac{\sigma}{\sqrt n} \le \mu \le \bar X + a\frac{\sigma}{\sqrt n}\right) = \gamma$, so it is a $\gamma$ confidence interval. $\blacksquare$ (This is L11 Theorem 2.1 with $a = z_{1-\alpha/2}$.)

### Disc 6 #3 · §5
> Suppose that $X_1, \ldots, X_n$ form a random sample from the normal distribution with unknown mean $\mu$ and known variance $\sigma^2$. How large a random sample must be taken in order to be sure that a 95% confidence interval for $\mu$ will have length less than $0.01\sigma$?

^disc-6-q3

#### Solution

1. Length $= 2z_{0.975}\frac{\sigma}{\sqrt n} = \frac{3.92\sigma}{\sqrt n}$.
2. $\frac{3.92\sigma}{\sqrt n} < 0.01\sigma \iff \sqrt n > 392 \iff n > 153{,}664$. *Why $\sigma$ cancels:* the target length is stated in units of $\sigma$.

**Answer:** $n = 153{,}665$ (with $z = 1.96$ from the table).

### Disc 6 #4 · §5 (pivotal quantity)
> Suppose that $X_1, \ldots, X_n$ form a random sample from the exponential distribution with unknown mean $\mu$. Describe a method for constructing a $1 - \alpha$ confidence interval for $\mu$. Hint: Use $\frac{1}{\mu}\sum_{i=1}^{n} X_i$ as a pivotal quantity.

^disc-6-q4

#### Solution

**Given:** $X_i \overset{iid}{\sim}$ exponential with mean $\mu$.
**Idea:** $Q = \frac1\mu\sum X_i$ has a distribution free of $\mu$ (pivotal), so recipe fact 5 applies.

1. $\frac{X_i}{\mu} \sim \text{Exp}(1) = \text{Gamma}(1,1)$. *Why:* dividing by the mean rescales to mean 1.
2. $Q = \frac1\mu\sum X_i \sim \text{Gamma}(n, 1)$. No $\mu$, so it is pivotal.
3. Table-friendly version: $2Q = \frac{2}{\mu}\sum X_i \sim \text{Gamma}\left(n, \frac12\right) = \chi^2_{2n}$.
4. $\mathbb{P}\left(\chi^2_{2n,\alpha/2} \le \frac{2\sum X_i}{\mu} \le \chi^2_{2n,1-\alpha/2}\right) = 1 - \alpha$.
5. Solve for $\mu$ (reciprocals flip):

**Answer:**
$$\left(\frac{2\sum X_i}{\chi^2_{2n,\,1-\alpha/2}},\ \frac{2\sum X_i}{\chi^2_{2n,\,\alpha/2}}\right)$$
is a $1-\alpha$ CI for $\mu$. With gamma quantiles $g_p$ of $\text{Gamma}(n,1)$ instead: $\left(\frac{\sum X_i}{g_{1-\alpha/2}}, \frac{\sum X_i}{g_{\alpha/2}}\right)$.

---

# Part 3: Lecture problems (in-class examples and proofs)

Items marked **(R demo)** were simulations shown in class, not problems to solve. They are kept because they are in-class examples; read them for the idea they show.

## Lecture 7: Sampling Distributions (§1)

### L7 Example 1.1 · §1
> Suppose we want to estimate the proportion $p$ of patients who do not relapse after treatment with a drug. If $X_1, X_2, \ldots, X_n$ are i.i.d. Bernoulli random variables representing relapse (1 = no relapse, 0 = relapse), the sample proportion $T = \frac{1}{n}\sum_{i=1}^{n} X_i$ is a statistic that can be used to estimate $p$. What is the sampling distribution of $T$?

^l7-ex-1-1

#### Solution

**Idea:** $nT = \sum X_i$ counts the successes, so it is binomial.

1. $\sum X_i \sim \text{Bin}(n, p)$ (sum of $n$ independent Bernoulli($p$)).
2. $T$ takes values $0, \frac1n, \ldots, 1$ with $\mathbb{P}\left(T = \frac kn\right) = \binom nk p^k(1-p)^{n-k}$.
3. $E(T) = p$, $\text{Var}(T) = \frac{p(1-p)}{n}$; by the CLT, $T \approx N\left(p, \frac{p(1-p)}{n}\right)$ for large $n$.

**Answer:** $nT \sim \text{Bin}(n,p)$, i.e. the PMF above.

### L7 Example 1.2 (Normal Data) · §1
> Suppose $X_1, X_2, \ldots, X_n$ are i.i.d. random variables from $N(\mu, \sigma^2)$, where $\mu$ is unknown but $\sigma^2 > 0$ is known. Find the sampling distribution of $\hat{\mu}$, the MLE of $\mu$.

^l7-ex-1-2

#### Solution

1. The MLE of $\mu$ is $\hat\mu = \bar X$.
2. A linear combination of independent normals is normal: $E(\bar X) = \mu$, $\text{Var}(\bar X) = \frac{1}{n^2}\cdot n\sigma^2 = \frac{\sigma^2}{n}$.

**Answer:** $\hat\mu = \bar X \sim N\left(\mu, \frac{\sigma^2}{n}\right)$. Standard error $\frac{\sigma}{\sqrt n}$, shrinking as $n$ grows.

### L7 Example 1.3 (Uniform Data) · §1
> Suppose $X_1, X_2, \ldots, X_n$ are i.i.d. from the uniform distribution over the interval $[0, \theta]$. Find the sampling distribution of $\hat{\theta} = \max(X_1, X_2, \ldots, X_n)$, the MLE of $\theta$. What is the mean of this sampling distribution?

^l7-ex-1-3

#### Solution

1. CDF: $\mathbb{P}(\hat\theta \le t) = \prod \mathbb{P}(X_i \le t) = \left(\frac t\theta\right)^n$, $0 \le t \le \theta$.
2. PDF: differentiate, $f(t) = \frac{n t^{n-1}}{\theta^n}$, $0 \le t \le \theta$.
3. Mean: $E(\hat\theta) = \int_0^\theta t\cdot\frac{nt^{n-1}}{\theta^n}dt = \frac{n}{\theta^n}\cdot\frac{\theta^{n+1}}{n+1} = \frac{n}{n+1}\theta$.

**Answer:** $F(t) = (t/\theta)^n$, $f(t) = nt^{n-1}/\theta^n$, $E(\hat\theta) = \frac{n\theta}{n+1}$. It is always a bit below $\theta$, but it approaches $\theta$ as $n$ grows.

### L7 §1.4 Visualizing a Sampling Distribution · §1 (R demo)
> Below we consider different sample sizes (5, 10, 30, and 50) and different true values for $p$ (0.1, 0.3, and 0.5). We plot the PMF of the sampling distribution of $T$ as red dots, and we plot a normal approximation based on the CLT as the blue curve.

^l7-sec-1-4

#### Solution

**What to notice (R demo):** the PMF of $T$ is lumpy and skewed for small $n$ or $p$ near 0, and it lines up with the normal curve $N\left(p, \frac{p(1-p)}{n}\right)$ as $n$ grows. Two guide bullets in one picture: the CLT, and the spread shrinking with $n$.

## Lecture 8: The $\chi^2$ Distribution (§2)

### L8 Example 1.1 · §2 (R demo)
> Below, we simulate 10,000 instances of $Y = X_1^2 + X_2^2 + X_3^2$, where $X_i \overset{iid}{\sim} N(0, 1)$, and compare the histogram to the theoretical $\chi^2_3$ density.

^l8-ex-1-1

#### Solution

**What to notice (R demo):** the histogram of $X_1^2 + X_2^2 + X_3^2$ matches the $\chi^2_3$ density. That is fact 1 checked by simulation.

### L8 Example 2.1 (Variance Estimation) · §2
> Suppose that $X_1, \ldots, X_n$ form a random sample from a normal distribution with known mean $\mu$ and unknown variance $\sigma^2$. Then, the MLE for $\sigma^2$ is
> $$\widehat{\sigma^2} = \frac{1}{n}\sum_{i=1}^{n}(X_i - \mu)^2.$$
> Find the distribution of $n\widehat{\sigma^2}/\sigma^2$.

^l8-ex-2-1

#### Solution

1. $\frac{n\widehat{\sigma^2}}{\sigma^2} = \sum_{i=1}^n\left(\frac{X_i - \mu}{\sigma}\right)^2$.
2. Each $\frac{X_i - \mu}{\sigma} \sim N(0,1)$, independent, so the sum of their squares is $\chi^2_n$.

**Answer:** $\frac{n\widehat{\sigma^2}}{\sigma^2} \sim \chi^2_n$. It is $n$ df, not $n-1$, because $\mu$ is known and nothing is estimated.

### L8 Example 2.2 · §2
> Consider the same setup as the previous example. Now, find the sampling distribution of $\widehat{\sigma^2}$.

^l8-ex-2-2

#### Solution

1. $\widehat{\sigma^2} = \frac{\sigma^2}{n}W$ with $W \sim \chi^2_n$.
2. Fact 2 with $c = \frac{\sigma^2}{n}$: $\text{Gamma}\left(\frac n2, \frac{n}{2\sigma^2}\right)$.

**Answer:** $\widehat{\sigma^2} \sim \text{Gamma}\left(\frac n2, \frac{n}{2\sigma^2}\right)$. Check: mean $= \frac{n/2}{n/(2\sigma^2)} = \sigma^2$.

### L8 Example 2.3 (Sampling Distribution of Variance) · §2
> A manufacturer measures the weights $X_1, \ldots, X_n$ of $n = 10$ boxes of cereal. It is known that the cereal boxes are normally distributed and have a mean weight of $\mu = 12$ ounces. The manufacturer is interested in estimating the variance of this distribution. Accordingly, they calculated the MLE:
> $$\widehat{\sigma^2} = \frac{1}{10}\sum_{i=1}^{10}(X_i - 12)^2.$$
> Suppose that the true variance was actually $\sigma^2 = 0.25$. Find the probability that the MLE is between 0.2 and 0.4.

^l8-ex-2-3

#### Solution

1. From Ex 2.1: $W = \frac{10\widehat{\sigma^2}}{0.25} = 40\widehat{\sigma^2} \sim \chi^2_{10}$.
2. Multiply the inequality by 40: $0.2 \le \widehat{\sigma^2} \le 0.4 \iff 8 \le W \le 16$.
3. $\mathbb{P} = F_{10}(16) - F_{10}(8)$. Table: $\chi^2_{10,0.90} = 15.99$, so $F(16) \approx 0.90$; 8 is between $\chi^2_{10,0.25} = 6.737$ and $\chi^2_{10,0.50} = 9.342$, so $F(8) \approx 0.37$ by interpolating.

**Answer:** $\approx 0.90 - 0.37 = 0.53$ [exact 0.529].

## Lecture 9: The Joint Distribution of the Sample Mean and Variance (§3)

### L9 Proof of Theorem 1.2 · §2, §3
> **Theorem 1.2.** Suppose $Z_1, \ldots, Z_n$ are i.i.d. standard normal random variables. Then
> $$\sum_{i=1}^{n}(Z_i - \bar{Z})^2 \sim \chi^2_{n-1}$$
> where $\bar{Z} = \frac{1}{n}\sum_{i=1}^{n} Z_i$.

^l9-thm-1-2

#### Solution

**The class proof (Oct 27 lecture).** Uses the helpful fact: if $X \sim \chi^2_n$, $X = Y + W$, $Y \sim \chi^2_1$ and $Y$ is independent of $W$, then $W \sim \chi^2_{n-1}$.

1. Split the sum of squares: $\sum Z_i^2 = \sum(Z_i - \bar Z)^2 + n\bar Z^2$. *Why:* expand $\sum(Z_i - \bar Z)^2 = \sum Z_i^2 - 2\bar Z\sum Z_i + n\bar Z^2$, and $\sum Z_i = n\bar Z$, so it equals $\sum Z_i^2 - n\bar Z^2$.
2. Left side: $X = \sum Z_i^2 \sim \chi^2_n$.
3. $Y = n\bar Z^2 = (\sqrt n\,\bar Z)^2$, and $\sqrt n\,\bar Z \sim N(0,1)$ (since $\bar Z \sim N(0, 1/n)$), so $Y \sim \chi^2_1$.
4. Independence: $\text{Cov}(\bar Z, Z_i - \bar Z) = \text{Cov}(\bar Z, Z_i) - \text{Var}(\bar Z) = \frac1n - \frac1n = 0$. For jointly normal variables, zero covariance means independent. So $\bar Z$ is independent of every deviation $Z_i - \bar Z$, and functions of independent things are independent: $Y = n\bar Z^2$ is independent of $W = \sum(Z_i - \bar Z)^2$.
5. Apply the helpful fact.

**Conclusion:** $\sum(Z_i - \bar Z)^2 \sim \chi^2_{n-1}$. $\blacksquare$ The lost degree of freedom is the $n\bar Z^2$ piece, used up by estimating the center.

### L9 §1.2 Proof (Distribution of the Sample Mean) · §3
> Suppose $X_1, X_2, \ldots, X_n$ are i.i.d. random variables from $N(\mu, \sigma^2)$. Show that $\bar{X} \sim N\left(\mu, \frac{\sigma^2}{n}\right)$.

^l9-sec-1-2-proof

#### Solution

1. $\bar X = \sum \frac1n X_i$ is a linear combination of independent normals, so it is normal. (MGF version: $M_{\bar X}(s) = \prod M_{X_i}(s/n) = \left(e^{\mu s/n + \sigma^2s^2/(2n^2)}\right)^n = e^{\mu s + \frac{\sigma^2}{n}\frac{s^2}{2}}$, the $N(\mu, \sigma^2/n)$ MGF.)
2. $E(\bar X) = \frac1n\cdot n\mu = \mu$.
3. $\text{Var}(\bar X) = \frac{1}{n^2}\cdot n\sigma^2 = \frac{\sigma^2}{n}$, since independence lets variances add.

**Conclusion:** $\bar X \sim N\left(\mu, \frac{\sigma^2}{n}\right)$. $\blacksquare$

### L9 Example 1.1 · §3 (R demo)
> Below we take repeated samples of size $n = 10$ from a $N(50, 4)$ distribution, and compute the sample mean each time. We then create a histogram of these sample means. This is compared the the PDF of a $N(50, 4/10)$ distribution, which is the true sampling distribution of the sample mean.

^l9-ex-1-1

#### Solution

**What to notice (R demo):** the histogram of 10,000 sample means sits on the $N(50, 0.4)$ curve: centered at $\mu = 50$ with variance $\sigma^2/n = 4/10$.

### L9 §1.3 Proof (Distribution of the Sample Variance) · §3
> Suppose $X_1, X_2, \ldots, X_n$ are i.i.d. random variables from $N(\mu, \sigma^2)$. Show that $\frac{\widehat{n\sigma^2}}{\sigma^2} \sim \chi^2_{n-1}$.

^l9-sec-1-3-proof

#### Solution

1. Standardize: $Z_i = \frac{X_i - \mu}{\sigma} \overset{iid}{\sim} N(0,1)$, so $X_i = \mu + \sigma Z_i$ and $\bar X = \mu + \sigma\bar Z$.
2. Then $X_i - \bar X = \sigma(Z_i - \bar Z)$. *Why:* the $\mu$'s cancel.
3. $\frac{n\widehat{\sigma^2}}{\sigma^2} = \frac{\sum(X_i - \bar X)^2}{\sigma^2} = \sum(Z_i - \bar Z)^2$.
4. Thm 1.2: that is $\chi^2_{n-1}$.

**Conclusion:** $\frac{n\widehat{\sigma^2}}{\sigma^2} \sim \chi^2_{n-1}$ (same as $\frac{(n-1)S^2}{\sigma^2}$). $\blacksquare$

### L9 Example 1.2 · §3 (R demo)
> Below we take repeated samples of size $n = 15$ from a $N(20, 9)$ distribution. For each sample, we compute the statistics $T = \frac{15}{9}\widehat{\sigma^2}$, where $\widehat{\sigma^2} = \frac{1}{n}\sum_{i=1}^{n}(X_i - \bar{X})^2$. We plot a histogram of the samples from $T$, along with the PDF of a $\chi^2_{14}$ distribution.

^l9-ex-1-2

#### Solution

**What to notice (R demo):** $T = \frac{15}{9}\widehat{\sigma^2} = \frac{n\widehat{\sigma^2}}{\sigma^2}$ with $n = 15$, $\sigma^2 = 9$. Its histogram matches $\chi^2_{14}$, not $\chi^2_{15}$: one df is lost.

### L9 §1.4 Proof (Independence) · §3
> Suppose $X_1, X_2, \ldots, X_n$ are i.i.d. random variables from $N(\mu, \sigma^2)$. Show that $\bar{X}$ and $\widehat{\sigma^2}$ are independent.

^l9-sec-1-4-proof

#### Solution

1. $\text{Cov}(\bar X, X_i - \bar X) = \text{Cov}(\bar X, X_i) - \text{Var}(\bar X)$.
2. $\text{Cov}(\bar X, X_i) = \frac1n\text{Cov}(X_i, X_i) = \frac{\sigma^2}{n}$. *Why:* only the $i$th term of $\bar X$ is correlated with $X_i$.
3. So the covariance is $\frac{\sigma^2}{n} - \frac{\sigma^2}{n} = 0$.
4. $\bar X$ and all deviations $X_i - \bar X$ are linear combinations of the same independent normals, so they are jointly normal. For jointly normal variables, zero covariance means independent.
5. $\widehat{\sigma^2} = \frac1n\sum(X_i - \bar X)^2$ is a function of the deviations only, so it is independent of $\bar X$.

**Conclusion:** $\bar X$ and $\widehat{\sigma^2}$ are independent. $\blacksquare$ (This is special to the normal; for other populations it fails.)

### L9 Example 1.3 · §3 (R demo)
> Below we take repeated samples of size $n = 10$ from a $N(10, 4)$ distribution, and compute the sample mean and sample variance each time. We then create a scatterplot of the sample means and variances. We can see there is no relationship between the two random variables.

^l9-ex-1-3

#### Solution

**What to notice (R demo):** the scatterplot of $(\bar X, S^2)$ pairs is a shapeless cloud, with no trend, which is what independence looks like.

## Lecture 10: The $t$ Distribution (§4)

### L10 Proof of Theorem 2.1 · §4
> **Theorem 2.1.** Suppose that $X_1, \ldots, X_n$ form a random sample from a normal distribution with mean $\mu$ and variance $\sigma^2$. Let $\bar{X}$ denote the sample mean and define
> $$S^2 = \frac{1}{n-1}\sum_{i=1}^{n}(X_i - \bar{X})^2.$$
> Then, the quantity
> $$U = \frac{\sqrt{n}(\bar{X} - \mu)}{\sqrt{S^2}}$$
> will follow the $t$ distribution with $n - 1$ degrees of freedom.

^l10-thm-2-1

#### Solution

1. $Z = \frac{\sqrt n(\bar X - \mu)}{\sigma} \sim N(0,1)$ (L9 Sec 1.2).
2. $Y = \frac{(n-1)S^2}{\sigma^2} = \frac{n\widehat{\sigma^2}}{\sigma^2} \sim \chi^2_{n-1}$ (L9 Sec 1.3).
3. $Z$ is a function of $\bar X$ and $Y$ is a function of $S^2$, which are independent (L9 Sec 1.4).
4. Fact 4: $\frac{Z}{\sqrt{Y/(n-1)}} \sim t_{n-1}$.
5. Simplify: $\frac{\sqrt n(\bar X - \mu)/\sigma}{\sqrt{S^2/\sigma^2}} = \frac{\sqrt n(\bar X - \mu)}{\sqrt{S^2}} = U$. The unknown $\sigma$ cancels, which is the whole point.

**Conclusion:** $U \sim t_{n-1}$. $\blacksquare$

### L10 Example 3.1 · §4
> For $T \sim t_5$, find $P(-2 \le T \le 2)$.

^l10-ex-3-1

#### Solution

1. Symmetry: $\mathbb{P}(-2 \le T \le 2) = \mathbb{P}(T \le 2) - \mathbb{P}(T \le -2) = 2\mathbb{P}(T \le 2) - 1$.
2. $t_5$ row: the 0.95 column is 2.015, close to 2, so $\mathbb{P}(T \le 2) \approx 0.95$.

**Answer:** $\approx 2(0.95) - 1 = 0.90$ [exact 0.898]. This is the professor's lookup from the Oct 29 lecture.

### L10 Example 3.2 · §4
> Let $X_1, \ldots, X_{10} \sim N(50, 4)$. Compute the distribution of $\frac{\sqrt{10}(\bar{X} - 50)}{S}$.

^l10-ex-3-2

#### Solution

By L10 Thm 2.1 with $n = 10$, $\mu = 50$: $\frac{\sqrt{10}(\bar X - 50)}{S} \sim t_9$.

**Answer:** $t_9$. The known $\sigma^2 = 4$ is not used, since $S$ replaces $\sigma$.

### L10 Example 3.3 · §4
> Suppose that a random sample of $n = 26$ rainfall measurements, $X_1, \ldots, X_n$, is taken from a normal distribution with unknown mean $\mu$ and unknown variance $\sigma^2$. We are interested in how far the sample mean $\bar{X}$ will be from the true mean $\mu$. We will use the quantity
> $$U = \frac{\sqrt{n}(\bar{X} - \mu)}{\sqrt{S^2}}$$
> here. Find the 90th percentile of $\bar{X}$ in terms of $\mu$ and $S^2$.

^l10-ex-3-3

#### Solution

**Idea:** the 90th percentile of $\bar X$ is the value $x$ with $\mathbb{P}(\bar X \le x) = 0.90$. Turn the event into one about $U \sim t_{25}$.

1. $\bar X \le x \iff U = \frac{\sqrt{26}(\bar X - \mu)}{\sqrt{S^2}} \le \frac{\sqrt{26}(x - \mu)}{\sqrt{S^2}}$.
2. Set the right side equal to $t_{25,0.90} = 1.316$.
3. Solve: $x = \mu + \frac{1.316}{\sqrt{26}}\sqrt{S^2} = \mu + 0.258\sqrt{S^2}$.

**Answer:** 90th percentile $= \mu + 0.258\sqrt{S^2}$.

### L10 Example 3.4 · §4
> Suppose that we observe $n = 20$ cheese chunks with lactic acid concentrations $X_1, \ldots, X_n$ coming from a normal distribution with unknown mean $\mu$ and variance $\sigma^2$. Find a value of $c$ such that
> $$\mathbb{P}\left(\bar{X} \le \mu + c\sqrt{S^2}\right)$$

^l10-ex-3-4

*The handout leaves the probability off. In class (Oct 29 transcript) the professor said: "find the value c should actually say that this probability is equal to 0.95 so go ahead and add that". So the target is* $\mathbb{P}\left(\bar{X} \le \mu + c\sqrt{S^2}\right) = 0.95$.

#### Solution

**Given:** $n = 20$, target probability 0.95 (the professor's correction in class).

1. $\bar X \le \mu + c\sqrt{S^2} \iff \frac{\sqrt{20}(\bar X - \mu)}{\sqrt{S^2}} \le c\sqrt{20}$, i.e. $U \le c\sqrt{20}$ with $U \sim t_{19}$.
2. $\mathbb{P}(U \le c\sqrt{20}) = 0.95 \Rightarrow c\sqrt{20} = t_{19,0.95} = 1.729$.
3. $c = \frac{1.729}{\sqrt{20}} = \frac{1.729}{4.472}$.

**Answer:** $c \approx 0.3866$ (matches the lecture).

## Lecture 11: Interval Estimation (§5)

### L11 Proof of Theorem 2.1 · §5
> **Theorem 2.1.** Let $X_1, X_2, \ldots, X_n \overset{iid}{\sim} N(\mu, \sigma^2)$ with known $\sigma$. Then a $1 - \alpha$ confidence interval for $\mu$ can be constructed as
> $$\bar{X} \pm z_{1-\alpha/2} \cdot \frac{\sigma}{\sqrt{n}},$$
> where $z_{1-\alpha/2}$ is the $1 - \alpha$ quantile of the standard normal distribution.

^l11-thm-2-1

#### Solution

1. Pivotal: $Z = \frac{\sqrt n(\bar X - \mu)}{\sigma} \sim N(0,1)$, with no $\mu$ in its distribution.
2. $\mathbb{P}\left(-z_{1-\alpha/2} \le Z \le z_{1-\alpha/2}\right) = (1 - \tfrac\alpha2) - \tfrac\alpha2 = 1 - \alpha$.
3. Rearrange (as in Disc 6 Q2): $\bar X - z_{1-\alpha/2}\frac{\sigma}{\sqrt n} \le \mu \le \bar X + z_{1-\alpha/2}\frac{\sigma}{\sqrt n}$.

**Conclusion:** $\bar X \pm z_{1-\alpha/2}\frac{\sigma}{\sqrt n}$ is a $1-\alpha$ CI. $\blacksquare$

### L11 Example 2.1 · §5
> Suppose $X_1, \ldots, X_n$ represent a random sample of daily rainfall measurements for Santa Cruz in the month of February, where $n = 26$. After collecting the data, you calculate $\bar{X} = 1.3$ inches. Suppose you know that rainfall in February is normally distributed with a variance of $\frac{1}{4}$, but you don't know what the daily average rainfall is. Use this information to construct a 95% confidence interval for the average daily rainfall in February.

^l11-ex-2-1

#### Solution

**Given:** $n = 26$, $\bar x = 1.3$, $\sigma^2 = \frac14$ known so $\sigma = \frac12$; 95%.

1. $z_{0.975} = 1.96$.
2. Half-width: $1.96\cdot\frac{0.5}{\sqrt{26}} = \frac{0.98}{5.099} = 0.192$.

**Answer:** $1.3 \pm 0.192 = (1.108,\ 1.492)$ inches.

### L11 Proof of Theorem 2.2 · §5
> **Theorem 2.2.** Let $X_1, X_2, \ldots, X_n \overset{iid}{\sim} N(\mu, \sigma^2)$ with unknown $\sigma$. Then a $1 - \alpha$ confidence interval for $\mu$ can be constructed as
> $$\bar{X} \pm t_{n-1,1-\alpha/2} \cdot \frac{S}{\sqrt{n}}.$$
> where $t_{n-1,1-\alpha/2}$ is the $1 - \alpha$ quantile of the t-distribution with $n - 1$ degrees of freedom, and
> $$S = \sqrt{S^2} = \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(X_i - \bar{X})^2}.$$

^l11-thm-2-2

#### Solution

1. Pivotal: $U = \frac{\sqrt n(\bar X - \mu)}{S} \sim t_{n-1}$ (L10 Thm 2.1), with no $\mu$ or $\sigma$ in its distribution.
2. The $t$ is symmetric, so $\mathbb{P}\left(-t_{n-1,1-\alpha/2} \le U \le t_{n-1,1-\alpha/2}\right) = 1 - \alpha$.
3. Rearrange as before, with $S$ in place of $\sigma$.

**Conclusion:** $\bar X \pm t_{n-1,1-\alpha/2}\frac{S}{\sqrt n}$ is a $1-\alpha$ CI. $\blacksquare$ It is wider than the $z$ interval because $t$ quantiles are bigger (heavier tails) to pay for estimating $\sigma$.

### L11 Example 2.2 · §5
> Suppose $X_1, \ldots, X_n$ represent a random sample of daily rainfall measurements for Santa Cruz in the month of February, where $n = 26$. After collecting the data, you calculate $\bar{X} = 1.3$ inches and $S^2 = 0.45$. Suppose you know that rainfall in February is normally distributed but you don't know what the daily average rainfall is or the variance. Use this information to construct a 95% confidence interval for the average daily rainfall in February.

^l11-ex-2-2

#### Solution

**Given:** $n = 26$, $\bar x = 1.3$, $S^2 = 0.45$ so $S = 0.6708$; 95%; $\sigma$ unknown.

1. $t_{25,0.975} = 2.060$.
2. Half-width: $2.060\cdot\frac{0.6708}{\sqrt{26}} = 2.060\cdot0.1316 = 0.271$.

**Answer:** $1.3 \pm 0.271 = (1.029,\ 1.571)$ inches.

### L11 §3 Interpretation of Confidence Intervals · §5 (R demo: 100 simulated 95% intervals, $n = 26$, $\mu = 5.1$, $\sigma = 1.6$)
> - $P(L < \theta < U) = 1 - \alpha$ is a statement about the random variables $L$ and $U$.
> - Once we have computed specific values using the data, $L = l$ and $U = u$, these are no longer random.
>   - After computing the specific interval ($L = l$, $U = u$), we can no longer make probability statements about the interval. It either contains the parameter or it doesn't (it is no longer random).
> - Instead, we can interpret the long run frequency of intervals that cover the parameter (if we took many different samples and computed confidence intervals for each sample, we would expect about $1 - \alpha$ percent of these to cover the true parameter).

^l11-sec-3

#### Solution

**The point to say on an exam:** "95% confident" is about the *procedure*. Before sampling, $(L, U)$ is random and covers $\theta$ with probability 0.95. After you compute $(1.03, 1.57)$, nothing is random: it either contains $\mu$ or it does not. Over many repeated samples, about 95% of the intervals built this way contain $\mu$. In the R demo, about 95 of the 100 simulated intervals cross the dashed line at $\mu = 5.1$.

**Wrong phrasing to avoid:** "there is a 95% probability that $\mu$ is in $(1.03, 1.57)$."

### L11 Example 4.1 · §5 (CI for a variance)
> Suppose that $X_1, \ldots, X_n$ form a random sample from the normal distribution with unknown mean $\mu$ and unknown variance $\sigma^2$. Find a $1 - \alpha$ confidence interval for $\sigma^2$.

^l11-ex-4-1

#### Solution

1. Pivotal: $Q = \frac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1}$.
2. $\mathbb{P}\left(\chi^2_{n-1,\alpha/2} \le \frac{(n-1)S^2}{\sigma^2} \le \chi^2_{n-1,1-\alpha/2}\right) = 1 - \alpha$ (equal tails).
3. Take reciprocals (flip) and multiply by $(n-1)S^2$.

**Answer:**
$$\left(\frac{(n-1)S^2}{\chi^2_{n-1,\,1-\alpha/2}},\ \frac{(n-1)S^2}{\chi^2_{n-1,\,\alpha/2}}\right).$$
Not symmetric around $S^2$, because the $\chi^2$ is skewed.

### L11 Example 4.2 · §5 (CI for a variance)
> Suppose $X_1, \ldots, X_n$ represent a random sample of daily rainfall measurements for Santa Cruz in the month of February, where $n = 26$. After collecting the data, you calculate $\bar{X} = 1.3$ inches and $S^2 = 0.45$. Suppose you know that rainfall in February is normally distributed but you don't know what the daily average rainfall is or the variance. Use this information to construct a 95% confidence interval for the variance of daily rainfall in February.

^l11-ex-4-2

#### Solution

1. $(n-1)S^2 = 25(0.45) = 11.25$.
2. $\chi^2_{25,0.025} = 13.12$, $\chi^2_{25,0.975} = 40.65$.
3. $\left(\frac{11.25}{40.65}, \frac{11.25}{13.12}\right)$.

**Answer:** $(0.277,\ 0.857)$ square inches.

## In-class extra-credit quizzes (spoken in lecture, from transcripts)

These were never handed out; the wording is the professor's, read aloud. A clean restatement (mine) follows each.

### Quiz 1 (Thu Oct 22) · §2
> So we have a researcher collecting a random sample, size 15. that's our sample size. Observations from a normal population. Variants, sigma squared, is unknown, but the mean, mu, is known. It's known to be 10, and they compute the sample variance or the MLE for the variance. Some of the squared deviations around the known mean divided by the sample size 15. So this is the same exact setup as like the last example that we did in the notes. And now we're asked what's the approximate probability that this MLE for the variance falls between these two boundaries, 0.8 and 0.5, given, or under the assumption, that the true variance, sigma squared, is 1.

^quiz-1

*Restatement (Claude's, not the professor's; the caption's "0.8 and 0.5" is 0.8 and 1.5 in his worked answer):* $X_1, \ldots, X_{15} \overset{iid}{\sim} N(10, \sigma^2)$, $\widehat{\sigma^2} = \frac{1}{15}\sum_{i=1}^{15}(X_i - 10)^2$, $\sigma^2 = 1$. Find $\mathbb{P}(0.8 \le \widehat{\sigma^2} \le 1.5)$.

> [!success]- Answer given in class
> $\mathbb{P}(12 \le Y \le 22.5)$ with $Y \sim \chi^2_{15}$, which is $\mathbb{P}(Y \le 22.5) - \mathbb{P}(Y \le 12) \approx 0.9 - 0.3 = 0.6$: choice (C).

#### Solution

1. $\mu = 10$ known, so $W = \frac{15\widehat{\sigma^2}}{\sigma^2} = 15\widehat{\sigma^2} \sim \chi^2_{15}$ (L8 Ex 2.1; $n$ df since nothing is estimated).
2. Multiply by 15: $0.8 \le \widehat{\sigma^2} \le 1.5 \iff 12 \le W \le 22.5$.
3. $\chi^2_{15}$ row: $\chi^2_{15,0.90} = 22.31$, so $F(22.5) \approx 0.90$; 12 is between $\chi^2_{15,0.25} = 11.04$ and $\chi^2_{15,0.50} = 14.34$, so $F(12) \approx 0.3$.

**Answer:** $\approx 0.9 - 0.3 = 0.6$, choice (C) [exact 0.584]. The professor's point after the quiz: subtracting the *true* mean 10 is what makes each $\frac{X_i - 10}{\sigma}$ a standard normal.

### Quiz 2 (Thu Oct 29) · §4 (same idea as HW4 #4)
> Okay, so suppose we have a random sample, size 5, from a normal distribution with mean, mu, invariance, and squared, looking at this quantity, U here, we're asked what's the expectation of U squared.

^quiz-2

*Restatement (Claude's):* $X_1, \ldots, X_5 \overset{iid}{\sim} N(\mu, \sigma^2)$, $U = \frac{\sqrt{5}(\bar{X} - \mu)}{\sqrt{S^2}}$. Find $E(U^2)$.

> [!success]- Answer given in class
> $U \sim t_4$, mean 0, so $E(U^2) = \mathrm{Var}(U) = \frac{m}{m-2} = \frac{4}{2} = 2$: choice (B).

#### Solution

1. $U \sim t_4$ (L10 Thm 2.1, $n - 1 = 4$).
2. $E(U^2) = \text{Var}(U) + [E(U)]^2$, and $E(U) = 0$ (the $t$ is symmetric and $m > 1$).
3. $\text{Var}(t_m) = \frac{m}{m-2}$ for $m > 2$: $\frac42 = 2$.

**Answer:** $E(U^2) = 2$, choice (B).

---

# Appendix: the professor's Midterm 2 recap, verbatim (Thu Nov 5)

Auto-captions from `17124220_English.pdf`, unedited (caption errors kept; student questions are mixed in where he answers them).

> Okay, and then last thing for today, I just want to do a quick recap of kind of the important topics to study for this exam. Things we've covered since exam one that weren't covered on exam one. So the first main topic is this idea of sampling distributions. So we're dealing with some statistic or some function of the data. It's a function of the data. The data is random, so the statistic is random. if it's random, it will have some probability distribution, and we call that the sampling distribution of the statistic T, usually an estimator.

> So this sampling distribution gives us insight into the variability of the statistic. It gives us a way to determine if the statistic's unbiased. So these are all the things we've been doing with sampling distribution. We said the standard deviation of the sampling distribution is what we call the standard error. It's just a name that we use for that standard deviation of that distribution. As the sample size and increases, many statistics become closer to the normal distribution and sampling distribution. That's the result of the central limit theorem.

> As the sample size increases, the sampling distribution of many statistics has lower variances as well. Yeah. The standard error or the variance of that sampling distribution, as you collect more and more data, usually that standard error gets smaller and smaller or the distribution is getting more and more concentrated. It's another way to think about that. We introduced a new distribution, the kai squared distribution. So the kai squared is a continuous distribution, has a single parameter. We call it the degrees of freedom or m.

> This is the PDF for the kai square distribution. We don't typically work with the PDF. We work with either statistical software or the kai squared table that I gave you to find probabilities or to integrate this PDF. Properties of this distribution, as we saw today, it's expectation or its mean is the degrees of freedom parameter m. its variance is 2M. It has this very nice addativity property. So if we have X1 following a chi-squared distribution with some degrees of freedom, M-1, X2, kai- squared with some degrees of freedom, M-2, and these two things are independent, then there's sum also follows a kai-squared distribution, and its degrees of freedom is the sum of the two degrees of freedom.

> It's related to the standard normal distribution, so if Z is a standard-normal distribution or standard normal random variable, the square of that random variable, z squared, will follow a kai squared distribution with one degree of freedom. And then when you combine this property with the addativity property, we basically say if we take multiple independent standard normal random variables, we square them and add them together, that will also be kai squared with m degrees of freedom, m being the number of standard normals we had, the number of things we squared in our sum. And we saw this relation to the gamma distribution, So if x is kai squared, and we have some constant c, the constant c times that kai square random variable, we'll follow a gamma distribution, or m the degrees of freedom, and c, that constant, both enter the parameters of the gamma. So be familiar with this distribution, how to use the kai squared table that I gave you, find probabilities or quantiles for this distribution. No, because the t table I gave you has a row for degrees of freedom infinity, which is the standard normal. Because there's no varying parameters for the standard normal distribution, its mean is always zero, its variance is always one. There's only one standard normal distribution.

> There's many kai squared distributions. There's many t distributions. We talked about the joint distribution of the sample mean and the sample variance. Recall that lecture was basically just centered on these three facts. These are the three important points from that lecture. You're dealing with high ID random variables from a normal population, mean mean variance sigma squared. And we saw the sample mean x bar has a normal sampling distribution centered around the true mean mu, and its variance is sigma squared over n.

> That's the first fact. MLE of the variance, dividing by n, satisfies this property, n times sigma squared hat over sigma squared, kai squared has a kai square distribution with n minus one degrees of freedom. We're losing a degree of freedom by plugging in this estimated mean x bar rather than the true mean. mu. And we could do the same thing for the sample variance. We could have n minus 1 times the sample variance in the numerator, and it's the same thing, right? Because in either case, it's just the sum of the square deviations around the sample B.

> By multiplying by n or multiplying by n minus 1, we're getting rid of that term in the denominator. That's the second fact. And then the third fact from that lecture was the x bar and sigma squared hat are independent. So those are the three points from that lecture on the joint sampling distribution. Then we introduced another new distribution, the T distribution. We gave this constructive definition for the T distribution. So if we have a standard normal random variable Z, kai squared random variable Y, M degrees of freedom, and these are independent, then this construction, Z over the square root of Y over its degrees of freedom, follows a T distribution, specifically a T distribution with M degrees of freedom.

> So M is the parameter of the T distribution. We call it a degrees of freedom parameter. This distribution is symmetric about zero. It's always symmetric about zero. We saw, if the degrees of freedom is one, the mean does not exist. But for degrees of freedom greater than one, the mean does exist, and it is zero. For M greater than two, the variance exists, and it's M over M minus two.

> We saw that this T distribution has heavier tails than the normal distribution, right? But as this degrees of freedom parameter goes to infinity, this T distribution converges to the standard normal distribution. So I will give you the same table from last time, but there won't be any new distributions on it. And I will give you the kai squared and T probability tables that were in the lecture notes. But I won't give you any new PDFs, for example. Not the PDFs. You'll get the tables themselves.

> Yeah. Any proofs that I've given you in class you should be familiar with. So it's focusing on the topic since midterm one, but the material is cumulative in the sense that it builds on itself. We're using the properties from earlier. So you still want to be familiar with those. Same as last time, four questions, multiple subparts. Yeah, it would just depend on the question.

> Anything could come up when we talk about sampling distributions, but I can't say which one or ones would show up or not. I wouldn't write a question just having you do that, but it could be like something you need to do to solve something related to what we're talking about here. I don't post any old exams. Yeah, so if you want study material, I recommend first going through the course notes that we do in class, specifically all the examples that we do, then the discussion section problems, then homework problems, and then if you want more problems, you can look through textbook problems, but I think that's sufficient without that. High squared distribution is a special case of the gamma, but the same doesn't apply to the T distribution? No, the T distribution is not a special case of the gamma. They don't have the same support, so gamma is supported on the positive real line, T is supported on the entire real line.

> You can think of the standard normal distribution. I wouldn't necessarily call it a special case of the T, but it's a limiting case of the T, the limiting case when the degrees of freedom goes to infinity. So there's that connection. Here's the PDF of the T distribution, but again, we work with the table. This is not very fun to integrate, so we work with the table or maybe numerical software to find probabilities for this distribution. Talk about the sample variance, dividing by n minus one. There's this connection to normal sampling for the T distribution.

> So this quantity here, n bar, or square of n times x bar minus m u over the square root of the sample variance this quantity follows a t distribution n minus one degrees of freedom and then again be familiar with this this distribution the table how to use the table to find probabilities or quantiles like we did in the examples in class and then the last major topic on the exam is interval estimation what we talked about on tuesday we recap this earlier this lecture but this is our definition right we have these two statistics L and U, they're random, their functions of the data, right? But if this probability inequality holds, the probability that the fixed unknown parameter theta is between these two bounds, the net interval LDU called a 1 minus alpha confidence interval. And we looked at some important cases. We looked at a confidence interval for a normal mean, where the variance, sigma squared is known. It's this case. We looked at the confidence interval for a normal mean, where the variance is unknown or estimated. It's this case, right?

> So the difference is using this standard normal quantile versus this T quantile. But also generally be familiar with this concept of finding confidence intervals, things like the variance of the normal distribution, and the way we do that is with a pivotal quantity. We have a pivotal quantity, we write down a probability and a quality, and we solve for the parameter of interest in the middle. Yeah, so when we think of L and U, when we say they're random, they're random before we observe a specific data set. Once we observe a specific data set and say the lower bound is 5 and the upper bound is 10, that thing is no longer random. The interval 5 to 10 is not random. It's this concept of taking a sample and getting random intervals that makes this hold.

> And so that relates to this last point. I understand this long-run frequency interpretation of the confidence. When we talk about probabilities, it's over the long run. It's not for any given interval. that you've calculated for a data set that you think it's on Canvas. If it's not, let me know and I'll put it on there. Well, we'll stop there.

> I'll stick around for a bit if there's questions. Otherwise, good luck on Tuesday. Don't forget to make your note sheet.
