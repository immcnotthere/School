---
type: study
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
exam: "STAT 132 Midterm 2 (Tue 2026-11-10, 3:20pm)"
---
# STAT 132 Midterm 2 Solutions

Worked solutions for every problem in [[STAT 132 Midterm 2 Review]]. Each section shows the problem (embedded from the review), then **Given**, **Idea**, the steps with the reason for each, and the **Answer**. The "back to problem" link returns you to the review.

All solutions are Claude's, not the professor's. Numbers are worked with the exam tables (the $\chi^2$ and $t$ tables from the lecture notes); exact software values are given in brackets where they differ.

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

## HW3 Q1
![[STAT 132 Midterm 2 Review#^hw3-q1]]

**Given:** $X_i \overset{iid}{\sim} N(\mu, \sigma^2)$.
**Idea:** the expression is the square of a standard normal.

1. $\bar X \sim N\left(\mu, \frac{\sigma^2}{n}\right)$ (fact 3).
2. Standardize: $Z = \frac{\bar X - \mu}{\sigma/\sqrt n} = \frac{\sqrt n(\bar X - \mu)}{\sigma} \sim N(0,1)$. *Why:* subtract the mean, divide by the standard deviation.
3. Square it: $Z^2 = \frac{n(\bar X - \mu)^2}{\sigma^2}$. That is exactly the expression.
4. $Z^2 \sim \chi^2_1$ (fact 1).

**Answer:** $\dfrac{n(\bar X - \mu)^2}{\sigma^2} \sim \chi^2_1$.

[[STAT 132 Midterm 2 Review#^hw3-q1|↩ back to problem]]

## HW3 Q2
![[STAT 132 Midterm 2 Review#^hw3-q2]]

**Given:** $X, Y, Z \overset{iid}{\sim} N(0,1)$.
**Idea:** distance less than 1 is the same as squared distance less than 1, and squared distance is a sum of three squared standard normals.

1. Distance from origin $= \sqrt{X^2 + Y^2 + Z^2}$.
2. $\sqrt{W} < 1 \iff W < 1$ since both sides are nonnegative. So we need $\mathbb{P}(X^2 + Y^2 + Z^2 < 1)$.
3. $W = X^2 + Y^2 + Z^2 \sim \chi^2_3$ (fact 1, three independent squared standard normals).
4. From the $\chi^2_3$ row: $\chi^2_{3,0.10} = 0.584$ and $\chi^2_{3,0.25} = 1.213$, so $\mathbb{P}(W < 1)$ is between 0.10 and 0.25, about 0.2.

**Answer:** $\mathbb{P}(\chi^2_3 < 1) \approx 0.20$ [exact 0.1987].

[[STAT 132 Midterm 2 Review#^hw3-q2|↩ back to problem]]

## HW3 Q3
![[STAT 132 Midterm 2 Review#^hw3-q3]]

**Given:** $X \sim \chi^2_m$ with density $f(x) = \frac{1}{2^{m/2}\Gamma(m/2)}x^{m/2-1}e^{-x/2}$, $x > 0$.
**Idea:** $E(X^{1/2}) = \int x^{1/2} f(x)\,dx$, and the integrand is an unnormalized gamma density, so use the gamma integral $\int_0^\infty x^{a-1}e^{-x/2}dx = \Gamma(a)\,2^{a}$.

1. $E(X^{1/2}) = \frac{1}{2^{m/2}\Gamma(m/2)}\int_0^\infty x^{\frac{m+1}{2}-1}e^{-x/2}\,dx$. *Why:* $x^{1/2}\cdot x^{m/2-1} = x^{(m+1)/2 - 1}$.
2. The integral is the gamma integral with $a = \frac{m+1}{2}$: it equals $\Gamma\left(\frac{m+1}{2}\right)2^{(m+1)/2}$.
3. Divide: $\frac{2^{(m+1)/2}}{2^{m/2}} = \sqrt 2$.

**Answer:**
$$E\left(X^{1/2}\right) = \frac{\sqrt 2\,\Gamma\left(\frac{m+1}{2}\right)}{\Gamma\left(\frac{m}{2}\right)}.$$
Check with $m = 1$: $\sqrt2\,\Gamma(1)/\Gamma(1/2) = \sqrt{2/\pi} \approx 0.798 = E|Z|$, which is right since $X^{1/2} = |Z|$.

[[STAT 132 Midterm 2 Review#^hw3-q3|↩ back to problem]]

## HW3 Q4
![[STAT 132 Midterm 2 Review#^hw3-q4]]

**Given:** $X \sim \chi^2_{200}$.
**Idea:** a $\chi^2_{200}$ is a sum of 200 iid pieces, so the CLT says it is roughly normal.

1. *Why the CLT applies:* $X$ has the same distribution as $\sum_{i=1}^{200} Z_i^2$ with $Z_i^2 \overset{iid}{\sim} \chi^2_1$. Each piece has mean 1 and variance 2 (finite), and 200 is large, so the sum is approximately normal.
2. Mean and variance: $E(X) = m = 200$, $\text{Var}(X) = 2m = 400$, so $SD = 20$.
3. Standardize the endpoints: $\frac{160 - 200}{20} = -2$, $\frac{240 - 200}{20} = 2$.
4. $\mathbb{P}(160 < X < 240) \approx \mathbb{P}(-2 < Z < 2) = 2\Phi(2) - 1 = 2(0.9772) - 1$.

**Answer:** $\approx 0.954$ [exact $\chi^2$ value 0.955].

[[STAT 132 Midterm 2 Review#^hw3-q4|↩ back to problem]]

## HW3 Q5
![[STAT 132 Midterm 2 Review#^hw3-q5]]

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

[[STAT 132 Midterm 2 Review#^hw3-q5|↩ back to problem]]

## HW4 Q1
![[STAT 132 Midterm 2 Review#^hw4-q1]]

**Given:** $X_1, \ldots, X_6 \overset{iid}{\sim} N(0,1)$.
**Idea:** build the $t$ recipe $\frac{Z}{\sqrt{Y/m}}$ (fact 4): numerator a standard normal, denominator a $\chi^2$ divided by its df.

1. Numerator: $X_1 - X_2 \sim N(0, 1 + 1) = N(0, 2)$. *Why:* variances of independent variables add, even for a difference. So $Z = \frac{X_1 - X_2}{\sqrt 2} \sim N(0,1)$.
2. Denominator: $Y = X_3^2 + X_4^2 + X_5^2 + X_6^2 \sim \chi^2_4$, independent of $Z$ (different $X$'s).
3. $t$ variable: $T = \frac{Z}{\sqrt{Y/4}} = \frac{(X_1 - X_2)/\sqrt2}{\sqrt Y/2} = \frac{2}{\sqrt 2}\cdot\frac{X_1 - X_2}{\sqrt Y} = \sqrt2\,\frac{X_1 - X_2}{\sqrt Y}$.
4. Match with $U = \frac{c(X_1 - X_2)}{\sqrt Y}$.

**Answer:** $c = \sqrt 2$, and $U \sim t_4$ (4 degrees of freedom).

[[STAT 132 Midterm 2 Review#^hw4-q1|↩ back to problem]]

## HW4 Q2
![[STAT 132 Midterm 2 Review#^hw4-q2]]

**Given:** $\sigma^2 = 4$ known, so $\sigma = 2$; 99% CI; length $\le 1$.
**Idea:** known-variance CI $\bar X \pm z_{1-\alpha/2}\frac{\sigma}{\sqrt n}$ has length $2z_{1-\alpha/2}\frac{\sigma}{\sqrt n}$, which does not depend on the data. Solve for $n$.

1. 99% means $\alpha = 0.01$, so $z_{0.995} = 2.576$.
2. Length $= 2(2.576)\frac{2}{\sqrt n} = \frac{10.304}{\sqrt n} \le 1$.
3. $\sqrt n \ge 10.304 \Rightarrow n \ge 106.17$.
4. $n$ must be a whole number and the length must not exceed 1, so round **up**.

**Answer:** $n = 107$ patients.

[[STAT 132 Midterm 2 Review#^hw4-q2|↩ back to problem]]

## HW4 Q3
![[STAT 132 Midterm 2 Review#^hw4-q3]]

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

[[STAT 132 Midterm 2 Review#^hw4-q3|↩ back to problem]]

## HW4 Q4
![[STAT 132 Midterm 2 Review#^hw4-q4]]

**Given:** $n = 5$, 95% $t$ interval.
**Idea:** the length is $2t\frac{S}{\sqrt n}$, a constant times $S$, so $E(L^2)$ only needs $E(S^2)$.

1. $L = 2\,t_{4,0.975}\frac{S}{\sqrt 5}$ with $t_{4,0.975} = 2.776$.
2. $L^2 = \frac{4\,t_{4,0.975}^2}{5}S^2$.
3. $E(S^2) = \sigma^2$. *Why:* $\frac{4S^2}{\sigma^2} \sim \chi^2_4$ has mean 4, so $E(S^2) = \frac{\sigma^2}{4}\cdot 4 = \sigma^2$.
4. $E(L^2) = \frac{4(2.776)^2}{5}\sigma^2 = \frac{4(7.706)}{5}\sigma^2$.

**Answer:** $E(L^2) \approx 6.165\,\sigma^2$.

[[STAT 132 Midterm 2 Review#^hw4-q4|↩ back to problem]]

## HW4 Q5
![[STAT 132 Midterm 2 Review#^hw4-q5]]

**Given:** $n = 15$, $S^2 = 0.0225$.
**Idea:** pivotal $Q = \frac{(n-1)S^2}{\sigma^2} \sim \chi^2_{14}$; its distribution has no $\sigma^2$ in it.

1. $\mathbb{P}\left(\chi^2_{14,0.025} \le \frac{14S^2}{\sigma^2} \le \chi^2_{14,0.975}\right) = 0.95$, with $\chi^2_{14,0.025} = 5.629$, $\chi^2_{14,0.975} = 26.12$.
2. Solve for $\sigma^2$. Taking reciprocals flips the inequalities: $\frac{14S^2}{26.12} \le \sigma^2 \le \frac{14S^2}{5.629}$. *Why the flip:* $1/x$ is decreasing for $x > 0$, so the big quantile goes to the lower bound.
3. $14S^2 = 0.315$.

**Answer:** $\left(\frac{0.315}{26.12},\ \frac{0.315}{5.629}\right) = (0.01206,\ 0.05596)$ cm⁴ (units of thickness squared).

[[STAT 132 Midterm 2 Review#^hw4-q5|↩ back to problem]]

---

# Part 2: Discussion problems

## Disc 4 Q1
![[STAT 132 Midterm 2 Review#^disc-4-q1]]

**Given:** $X_i \overset{iid}{\sim} U[0,\theta]$, $Y = \max X_i$.
**Idea:** $Y \le \theta$ always, so the absolute value only has one side to worry about. Then use the CDF of the max (L7 Ex 1.3).

1. $Y \le \theta$, so $|Y - \theta| = \theta - Y$, and $\theta - Y \le 0.1\theta \iff Y \ge 0.9\theta$.
2. $\mathbb{P}(Y \le y) = \left(\frac{y}{\theta}\right)^n$. *Why:* the max is below $y$ only if every $X_i$ is, and they are independent.
3. $\mathbb{P}(Y \ge 0.9\theta) = 1 - 0.9^n \ge 0.95 \iff 0.9^n \le 0.05$.
4. Take logs (log of a number below 1 is negative, so the inequality flips): $n \ge \frac{\ln 0.05}{\ln 0.9} = \frac{-2.996}{-0.1054} = 28.43$.

**Answer:** $n = 29$.

[[STAT 132 Midterm 2 Review#^disc-4-q1|↩ back to problem]]

## Disc 4 Q2
![[STAT 132 Midterm 2 Review#^disc-4-q2]]

**Idea:** $E|\bar X_n - \mu|^2$ is the definition of $\text{Var}(\bar X_n)$, because $E(\bar X_n) = \mu$.

1. $E|\bar X_n - \mu|^2 = \text{Var}(\bar X_n) = \frac{\sigma^2}{n} = \frac{4}{n}$.
2. $\frac{4}{n} \le 0.1 \iff n \ge 40$.

**Answer:** $n = 40$.

[[STAT 132 Midterm 2 Review#^disc-4-q2|↩ back to problem]]

## Disc 4 Q3
![[STAT 132 Midterm 2 Review#^disc-4-q3]]

**Idea:** standardize $\bar X_n$, then use the normal quantile.

1. $\frac{\bar X_n - \mu}{2/\sqrt n} = Z \sim N(0,1)$.
2. $|\bar X_n - \mu| \le 0.1 \iff |Z| \le \frac{0.1\sqrt n}{2} = 0.05\sqrt n$.
3. $\mathbb{P}(|Z| \le a) \ge 0.95 \iff a \ge z_{0.975} = 1.96$. *Why 0.975:* 0.95 in the middle leaves 0.025 in each tail.
4. $0.05\sqrt n \ge 1.96 \Rightarrow \sqrt n \ge 39.2 \Rightarrow n \ge 1536.64$.

**Answer:** $n = 1537$.

[[STAT 132 Midterm 2 Review#^disc-4-q3|↩ back to problem]]

## Disc 4 Q4
![[STAT 132 Midterm 2 Review#^disc-4-q4]]

**Given:** $X_i \overset{iid}{\sim} \text{Exp}(\lambda)$ (rate $\lambda$, mean $1/\lambda$).
**Idea:** the MLE is $\hat\lambda = 1/\bar X$. Its CDF comes from the distribution of $\sum X_i$, which is gamma.

1. MLE: $\ell(\lambda) = n\ln\lambda - \lambda\sum x_i$, $\ell'(\lambda) = \frac{n}{\lambda} - \sum x_i = 0 \Rightarrow \hat\lambda = \frac{n}{\sum X_i} = \frac{1}{\bar X}$.
2. $T = \sum X_i \sim \text{Gamma}(n, \lambda)$. *Why:* a sum of $n$ independent $\text{Gamma}(1,\lambda)$ is $\text{Gamma}(n,\lambda)$.
3. For $t > 0$: $\mathbb{P}(\hat\lambda \le t) = \mathbb{P}\left(\frac{n}{T} \le t\right) = \mathbb{P}\left(T \ge \frac{n}{t}\right)$. *Why it flips:* $n/T$ is decreasing in $T$.
4. Write it out:
$$F_{\hat\lambda}(t) = \int_{n/t}^{\infty}\frac{\lambda^n}{\Gamma(n)}y^{n-1}e^{-\lambda y}\,dy = \sum_{k=0}^{n-1}e^{-n\lambda/t}\frac{(n\lambda/t)^k}{k!},\quad t > 0.$$
The sum form uses the gamma and Poisson link: a $\text{Gamma}(n,\lambda)$ waiting time exceeds $y$ exactly when fewer than $n$ Poisson events happen by time $y$.

**Answer:** $F_{\hat\lambda}(t) = \mathbb{P}\left(\text{Gamma}(n,\lambda) \ge \frac{n}{t}\right)$ as above, and $0$ for $t \le 0$.

[[STAT 132 Midterm 2 Review#^disc-4-q4|↩ back to problem]]

## Disc 4 Q5
![[STAT 132 Midterm 2 Review#^disc-4-q5]]

**Idea:** same as Q2, but the variance depends on the unknown $p$, so plan for the worst $p$.

1. $E|\bar X_n - p|^2 = \text{Var}(\bar X_n) = \frac{p(1-p)}{n}$.
2. $p(1-p)$ is largest at $p = \frac12$, where it equals $\frac14$. *Why:* it is a downward parabola with its peak at $\frac12$.
3. Need $\frac{p(1-p)}{n} \le 0.01$ for every $p$: $\frac{1/4}{n} \le 0.01 \iff n \ge 25$.

**Answer:** $n = 25$.

[[STAT 132 Midterm 2 Review#^disc-4-q5|↩ back to problem]]

## Disc 5 Q1
![[STAT 132 Midterm 2 Review#^disc-5-q1]]

**Idea:** the mode is where the density is largest. Maximize $\ln f$.

1. $\ln f(x) = \text{const} + \left(\frac m2 - 1\right)\ln x - \frac x2$.
2. $\frac{d}{dx}\ln f = \frac{m/2 - 1}{x} - \frac12 = 0 \Rightarrow x = m - 2$.
3. This is a maximum only if $m - 2 > 0$. For $m = 1$ the density decreases from $+\infty$ at $0$; for $m = 2$ it is $\frac12e^{-x/2}$, decreasing from $x = 0$. Either way the peak is at $0$.

**Answer:** mode $= m - 2$ for $m \ge 3$; mode $= 0$ for $m = 1, 2$. In one line: $\max(m-2, 0)$.

[[STAT 132 Midterm 2 Review#^disc-5-q1|↩ back to problem]]

## Disc 5 Q2
![[STAT 132 Midterm 2 Review#^disc-5-q2]]

**Idea:** inside a circle of radius $r$ means $X^2 + Y^2 \le r^2$, and $X^2 + Y^2 \sim \chi^2_2$.

1. $\mathbb{P}(X^2 + Y^2 \le r^2) = 0.99 \Rightarrow r^2 = \chi^2_{2,0.99} = 9.210$.
2. Check by hand: $\chi^2_2 = \text{Exp}(1/2)$, so $1 - e^{-r^2/2} = 0.99 \Rightarrow r^2 = 2\ln 100 = 9.210$.
3. $r = \sqrt{9.210}$.

**Answer:** $r \approx 3.035$.

[[STAT 132 Midterm 2 Review#^disc-5-q2|↩ back to problem]]

## Disc 5 Q3
![[STAT 132 Midterm 2 Review#^disc-5-q3]]

**Idea:** each bracket is a normal with variance 3. Scale each to a standard normal, and the sum of squares becomes $\chi^2_2$.

1. $X_1 + X_2 + X_3 \sim N(0, 3)$, so $\frac{X_1 + X_2 + X_3}{\sqrt3} \sim N(0,1)$. Same for $X_4 + X_5 + X_6$, and the two are independent (no shared $X$'s).
2. $\frac{(X_1 + X_2 + X_3)^2}{3} + \frac{(X_4 + X_5 + X_6)^2}{3} = \frac{Y}{3} \sim \chi^2_2$.

**Answer:** $c = \frac13$, and $\frac{Y}{3} \sim \chi^2_2$.

[[STAT 132 Midterm 2 Review#^disc-5-q3|↩ back to problem]]

## Disc 5 Q4
![[STAT 132 Midterm 2 Review#^disc-5-q4]]

**Idea:** $\widehat{\sigma^2}$ is a constant times a $\chi^2_{n-1}$; use fact 2.

1. $W = \frac{n\widehat{\sigma^2}}{\sigma^2} \sim \chi^2_{n-1}$ (fact 3).
2. So $\widehat{\sigma^2} = cW$ with $c = \frac{\sigma^2}{n}$.
3. Fact 2: $cW \sim \text{Gamma}\left(\frac{n-1}{2},\ \frac{1}{2c}\right) = \text{Gamma}\left(\frac{n-1}{2},\ \frac{n}{2\sigma^2}\right)$. *Why fact 2 holds:* $\chi^2_{n-1} = \text{Gamma}\left(\frac{n-1}{2}, \frac12\right)$, and multiplying a gamma by $c$ divides its rate by $c$.

**Answer:** shown: $\widehat{\sigma^2} \sim \text{Gamma}\left(\frac{n-1}{2}, \frac{n}{2\sigma^2}\right)$. $\blacksquare$

[[STAT 132 Midterm 2 Review#^disc-5-q4|↩ back to problem]]

## Disc 5 Q5
![[STAT 132 Midterm 2 Review#^disc-5-q5]]

**Idea:** multiply through by $\frac{n}{\sigma^2} = \frac{16}{\sigma^2}$ to get a $\chi^2$ in the middle. The only difference between (a) and (b) is the degrees of freedom: $\mu$ known gives 16, $\bar X$ estimated gives 15.

**(a)** $W = \frac{1}{\sigma^2}\sum(X_i - \mu)^2 = \sum Z_i^2 \sim \chi^2_{16}$.
1. $\frac{\sigma^2}{2} \le \frac{1}{16}\sum(X_i-\mu)^2 \le 2\sigma^2 \iff 8 \le W \le 32$.
2. $\chi^2_{16}$ row: $\chi^2_{16,0.99} = 32.00$ and $\chi^2_{16,0.05} = 7.962$, so $\mathbb{P} \approx 0.99 - 0.05$.

**(b)** $V = \frac{1}{\sigma^2}\sum(X_i - \bar X)^2 = \frac{n\widehat{\sigma^2}}{\sigma^2} \sim \chi^2_{15}$.
1. Same algebra: $8 \le V \le 32$.
2. $\chi^2_{15}$ row: 32 is between $\chi^2_{15,0.99} = 30.58$ and $\chi^2_{15,0.995} = 32.80$, so $F(32) \approx 0.994$; 8 is between $\chi^2_{15,0.05} = 7.261$ and $\chi^2_{15,0.10} = 8.547$, so $F(8) \approx 0.076$.

**Answer:** (a) $\approx 0.94$ [0.939]; (b) $\approx 0.92$ [0.917]. Losing a degree of freedom shifts the distribution left, so a bit more mass falls below 8.

[[STAT 132 Midterm 2 Review#^disc-5-q5|↩ back to problem]]

## Disc 6 Q1
![[STAT 132 Midterm 2 Review#^disc-6-q1]]

**Idea:** same as HW4 Q1 with 3 df.

1. $Z = \frac{X_1 + X_2}{\sqrt2} \sim N(0,1)$; $Y = X_3^2 + X_4^2 + X_5^2 \sim \chi^2_3$, independent.
2. $\frac{Z}{\sqrt{Y/3}} = \frac{\sqrt3}{\sqrt2}\cdot\frac{X_1 + X_2}{\sqrt Y}$.

**Answer:** $c = \sqrt{3/2} \approx 1.225$, and $U \sim t_3$.

[[STAT 132 Midterm 2 Review#^disc-6-q1|↩ back to problem]]

## Disc 6 Q2
![[STAT 132 Midterm 2 Review#^disc-6-q2]]

**Idea:** show the probability that the interval covers $\mu$ equals $\gamma$. Write $a = \Phi^{-1}\left(\frac{1+\gamma}{2}\right)$.

1. Pivotal: $Z = \frac{\sqrt n(\bar X - \mu)}{\sigma} \sim N(0,1)$.
2. $\mathbb{P}(-a \le Z \le a) = \Phi(a) - \Phi(-a) = 2\Phi(a) - 1$. *Why:* symmetry, $\Phi(-a) = 1 - \Phi(a)$.
3. $\Phi(a) = \frac{1+\gamma}{2}$ by definition of $a$, so $2\Phi(a) - 1 = (1 + \gamma) - 1 = \gamma$.
4. Rearrange $-a \le \frac{\sqrt n(\bar X - \mu)}{\sigma} \le a$: multiply by $\frac{\sigma}{\sqrt n}$, subtract $\bar X$, multiply by $-1$ (flips): $\bar X - a\frac{\sigma}{\sqrt n} \le \mu \le \bar X + a\frac{\sigma}{\sqrt n}$.
5. Same event, so same probability $\gamma$.

**Answer:** $\mathbb{P}\left(\bar X - a\frac{\sigma}{\sqrt n} \le \mu \le \bar X + a\frac{\sigma}{\sqrt n}\right) = \gamma$, so it is a $\gamma$ confidence interval. $\blacksquare$ (This is L11 Theorem 2.1 with $a = z_{1-\alpha/2}$.)

[[STAT 132 Midterm 2 Review#^disc-6-q2|↩ back to problem]]

## Disc 6 Q3
![[STAT 132 Midterm 2 Review#^disc-6-q3]]

1. Length $= 2z_{0.975}\frac{\sigma}{\sqrt n} = \frac{3.92\sigma}{\sqrt n}$.
2. $\frac{3.92\sigma}{\sqrt n} < 0.01\sigma \iff \sqrt n > 392 \iff n > 153{,}664$. *Why $\sigma$ cancels:* the target length is stated in units of $\sigma$.

**Answer:** $n = 153{,}665$ (with $z = 1.96$ from the table).

[[STAT 132 Midterm 2 Review#^disc-6-q3|↩ back to problem]]

## Disc 6 Q4
![[STAT 132 Midterm 2 Review#^disc-6-q4]]

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

[[STAT 132 Midterm 2 Review#^disc-6-q4|↩ back to problem]]

---

# Part 3: Lecture problems

## L7 Ex 1.1
![[STAT 132 Midterm 2 Review#^l7-ex-1-1]]

**Idea:** $nT = \sum X_i$ counts the successes, so it is binomial.

1. $\sum X_i \sim \text{Bin}(n, p)$ (sum of $n$ independent Bernoulli($p$)).
2. $T$ takes values $0, \frac1n, \ldots, 1$ with $\mathbb{P}\left(T = \frac kn\right) = \binom nk p^k(1-p)^{n-k}$.
3. $E(T) = p$, $\text{Var}(T) = \frac{p(1-p)}{n}$; by the CLT, $T \approx N\left(p, \frac{p(1-p)}{n}\right)$ for large $n$.

**Answer:** $nT \sim \text{Bin}(n,p)$, i.e. the PMF above.

[[STAT 132 Midterm 2 Review#^l7-ex-1-1|↩ back to problem]]

## L7 Ex 1.2
![[STAT 132 Midterm 2 Review#^l7-ex-1-2]]

1. The MLE of $\mu$ is $\hat\mu = \bar X$.
2. A linear combination of independent normals is normal: $E(\bar X) = \mu$, $\text{Var}(\bar X) = \frac{1}{n^2}\cdot n\sigma^2 = \frac{\sigma^2}{n}$.

**Answer:** $\hat\mu = \bar X \sim N\left(\mu, \frac{\sigma^2}{n}\right)$. Standard error $\frac{\sigma}{\sqrt n}$, shrinking as $n$ grows.

[[STAT 132 Midterm 2 Review#^l7-ex-1-2|↩ back to problem]]

## L7 Ex 1.3
![[STAT 132 Midterm 2 Review#^l7-ex-1-3]]

1. CDF: $\mathbb{P}(\hat\theta \le t) = \prod \mathbb{P}(X_i \le t) = \left(\frac t\theta\right)^n$, $0 \le t \le \theta$.
2. PDF: differentiate, $f(t) = \frac{n t^{n-1}}{\theta^n}$, $0 \le t \le \theta$.
3. Mean: $E(\hat\theta) = \int_0^\theta t\cdot\frac{nt^{n-1}}{\theta^n}dt = \frac{n}{\theta^n}\cdot\frac{\theta^{n+1}}{n+1} = \frac{n}{n+1}\theta$.

**Answer:** $F(t) = (t/\theta)^n$, $f(t) = nt^{n-1}/\theta^n$, $E(\hat\theta) = \frac{n\theta}{n+1}$. It is always a bit below $\theta$, but it approaches $\theta$ as $n$ grows.

[[STAT 132 Midterm 2 Review#^l7-ex-1-3|↩ back to problem]]

## L7 Sec 1.4
![[STAT 132 Midterm 2 Review#^l7-sec-1-4]]

**What to notice (R demo):** the PMF of $T$ is lumpy and skewed for small $n$ or $p$ near 0, and it lines up with the normal curve $N\left(p, \frac{p(1-p)}{n}\right)$ as $n$ grows. Two guide bullets in one picture: the CLT, and the spread shrinking with $n$.

[[STAT 132 Midterm 2 Review#^l7-sec-1-4|↩ back to problem]]

## L8 Ex 1.1
![[STAT 132 Midterm 2 Review#^l8-ex-1-1]]

**What to notice (R demo):** the histogram of $X_1^2 + X_2^2 + X_3^2$ matches the $\chi^2_3$ density. That is fact 1 checked by simulation.

[[STAT 132 Midterm 2 Review#^l8-ex-1-1|↩ back to problem]]

## L8 Ex 2.1
![[STAT 132 Midterm 2 Review#^l8-ex-2-1]]

1. $\frac{n\widehat{\sigma^2}}{\sigma^2} = \sum_{i=1}^n\left(\frac{X_i - \mu}{\sigma}\right)^2$.
2. Each $\frac{X_i - \mu}{\sigma} \sim N(0,1)$, independent, so the sum of their squares is $\chi^2_n$.

**Answer:** $\frac{n\widehat{\sigma^2}}{\sigma^2} \sim \chi^2_n$. It is $n$ df, not $n-1$, because $\mu$ is known and nothing is estimated.

[[STAT 132 Midterm 2 Review#^l8-ex-2-1|↩ back to problem]]

## L8 Ex 2.2
![[STAT 132 Midterm 2 Review#^l8-ex-2-2]]

1. $\widehat{\sigma^2} = \frac{\sigma^2}{n}W$ with $W \sim \chi^2_n$.
2. Fact 2 with $c = \frac{\sigma^2}{n}$: $\text{Gamma}\left(\frac n2, \frac{n}{2\sigma^2}\right)$.

**Answer:** $\widehat{\sigma^2} \sim \text{Gamma}\left(\frac n2, \frac{n}{2\sigma^2}\right)$. Check: mean $= \frac{n/2}{n/(2\sigma^2)} = \sigma^2$.

[[STAT 132 Midterm 2 Review#^l8-ex-2-2|↩ back to problem]]

## L8 Ex 2.3
![[STAT 132 Midterm 2 Review#^l8-ex-2-3]]

1. From Ex 2.1: $W = \frac{10\widehat{\sigma^2}}{0.25} = 40\widehat{\sigma^2} \sim \chi^2_{10}$.
2. Multiply the inequality by 40: $0.2 \le \widehat{\sigma^2} \le 0.4 \iff 8 \le W \le 16$.
3. $\mathbb{P} = F_{10}(16) - F_{10}(8)$. Table: $\chi^2_{10,0.90} = 15.99$, so $F(16) \approx 0.90$; 8 is between $\chi^2_{10,0.25} = 6.737$ and $\chi^2_{10,0.50} = 9.342$, so $F(8) \approx 0.37$ by interpolating.

**Answer:** $\approx 0.90 - 0.37 = 0.53$ [exact 0.529].

[[STAT 132 Midterm 2 Review#^l8-ex-2-3|↩ back to problem]]

## L9 Thm 1.2
![[STAT 132 Midterm 2 Review#^l9-thm-1-2]]

**The class proof (Oct 27 lecture).** Uses the helpful fact: if $X \sim \chi^2_n$, $X = Y + W$, $Y \sim \chi^2_1$ and $Y$ is independent of $W$, then $W \sim \chi^2_{n-1}$.

1. Split the sum of squares: $\sum Z_i^2 = \sum(Z_i - \bar Z)^2 + n\bar Z^2$. *Why:* expand $\sum(Z_i - \bar Z)^2 = \sum Z_i^2 - 2\bar Z\sum Z_i + n\bar Z^2$, and $\sum Z_i = n\bar Z$, so it equals $\sum Z_i^2 - n\bar Z^2$.
2. Left side: $X = \sum Z_i^2 \sim \chi^2_n$.
3. $Y = n\bar Z^2 = (\sqrt n\,\bar Z)^2$, and $\sqrt n\,\bar Z \sim N(0,1)$ (since $\bar Z \sim N(0, 1/n)$), so $Y \sim \chi^2_1$.
4. Independence: $\text{Cov}(\bar Z, Z_i - \bar Z) = \text{Cov}(\bar Z, Z_i) - \text{Var}(\bar Z) = \frac1n - \frac1n = 0$. For jointly normal variables, zero covariance means independent. So $\bar Z$ is independent of every deviation $Z_i - \bar Z$, and functions of independent things are independent: $Y = n\bar Z^2$ is independent of $W = \sum(Z_i - \bar Z)^2$.
5. Apply the helpful fact.

**Conclusion:** $\sum(Z_i - \bar Z)^2 \sim \chi^2_{n-1}$. $\blacksquare$ The lost degree of freedom is the $n\bar Z^2$ piece, used up by estimating the center.

[[STAT 132 Midterm 2 Review#^l9-thm-1-2|↩ back to problem]]

## L9 Sec 1.2 Proof
![[STAT 132 Midterm 2 Review#^l9-sec-1-2-proof]]

1. $\bar X = \sum \frac1n X_i$ is a linear combination of independent normals, so it is normal. (MGF version: $M_{\bar X}(s) = \prod M_{X_i}(s/n) = \left(e^{\mu s/n + \sigma^2s^2/(2n^2)}\right)^n = e^{\mu s + \frac{\sigma^2}{n}\frac{s^2}{2}}$, the $N(\mu, \sigma^2/n)$ MGF.)
2. $E(\bar X) = \frac1n\cdot n\mu = \mu$.
3. $\text{Var}(\bar X) = \frac{1}{n^2}\cdot n\sigma^2 = \frac{\sigma^2}{n}$, since independence lets variances add.

**Conclusion:** $\bar X \sim N\left(\mu, \frac{\sigma^2}{n}\right)$. $\blacksquare$

[[STAT 132 Midterm 2 Review#^l9-sec-1-2-proof|↩ back to problem]]

## L9 Ex 1.1
![[STAT 132 Midterm 2 Review#^l9-ex-1-1]]

**What to notice (R demo):** the histogram of 10,000 sample means sits on the $N(50, 0.4)$ curve: centered at $\mu = 50$ with variance $\sigma^2/n = 4/10$.

[[STAT 132 Midterm 2 Review#^l9-ex-1-1|↩ back to problem]]

## L9 Sec 1.3 Proof
![[STAT 132 Midterm 2 Review#^l9-sec-1-3-proof]]

1. Standardize: $Z_i = \frac{X_i - \mu}{\sigma} \overset{iid}{\sim} N(0,1)$, so $X_i = \mu + \sigma Z_i$ and $\bar X = \mu + \sigma\bar Z$.
2. Then $X_i - \bar X = \sigma(Z_i - \bar Z)$. *Why:* the $\mu$'s cancel.
3. $\frac{n\widehat{\sigma^2}}{\sigma^2} = \frac{\sum(X_i - \bar X)^2}{\sigma^2} = \sum(Z_i - \bar Z)^2$.
4. Thm 1.2: that is $\chi^2_{n-1}$.

**Conclusion:** $\frac{n\widehat{\sigma^2}}{\sigma^2} \sim \chi^2_{n-1}$ (same as $\frac{(n-1)S^2}{\sigma^2}$). $\blacksquare$

[[STAT 132 Midterm 2 Review#^l9-sec-1-3-proof|↩ back to problem]]

## L9 Ex 1.2
![[STAT 132 Midterm 2 Review#^l9-ex-1-2]]

**What to notice (R demo):** $T = \frac{15}{9}\widehat{\sigma^2} = \frac{n\widehat{\sigma^2}}{\sigma^2}$ with $n = 15$, $\sigma^2 = 9$. Its histogram matches $\chi^2_{14}$, not $\chi^2_{15}$: one df is lost.

[[STAT 132 Midterm 2 Review#^l9-ex-1-2|↩ back to problem]]

## L9 Sec 1.4 Proof
![[STAT 132 Midterm 2 Review#^l9-sec-1-4-proof]]

1. $\text{Cov}(\bar X, X_i - \bar X) = \text{Cov}(\bar X, X_i) - \text{Var}(\bar X)$.
2. $\text{Cov}(\bar X, X_i) = \frac1n\text{Cov}(X_i, X_i) = \frac{\sigma^2}{n}$. *Why:* only the $i$th term of $\bar X$ is correlated with $X_i$.
3. So the covariance is $\frac{\sigma^2}{n} - \frac{\sigma^2}{n} = 0$.
4. $\bar X$ and all deviations $X_i - \bar X$ are linear combinations of the same independent normals, so they are jointly normal. For jointly normal variables, zero covariance means independent.
5. $\widehat{\sigma^2} = \frac1n\sum(X_i - \bar X)^2$ is a function of the deviations only, so it is independent of $\bar X$.

**Conclusion:** $\bar X$ and $\widehat{\sigma^2}$ are independent. $\blacksquare$ (This is special to the normal; for other populations it fails.)

[[STAT 132 Midterm 2 Review#^l9-sec-1-4-proof|↩ back to problem]]

## L9 Ex 1.3
![[STAT 132 Midterm 2 Review#^l9-ex-1-3]]

**What to notice (R demo):** the scatterplot of $(\bar X, S^2)$ pairs is a shapeless cloud, with no trend, which is what independence looks like.

[[STAT 132 Midterm 2 Review#^l9-ex-1-3|↩ back to problem]]

## L10 Thm 2.1
![[STAT 132 Midterm 2 Review#^l10-thm-2-1]]

1. $Z = \frac{\sqrt n(\bar X - \mu)}{\sigma} \sim N(0,1)$ (L9 Sec 1.2).
2. $Y = \frac{(n-1)S^2}{\sigma^2} = \frac{n\widehat{\sigma^2}}{\sigma^2} \sim \chi^2_{n-1}$ (L9 Sec 1.3).
3. $Z$ is a function of $\bar X$ and $Y$ is a function of $S^2$, which are independent (L9 Sec 1.4).
4. Fact 4: $\frac{Z}{\sqrt{Y/(n-1)}} \sim t_{n-1}$.
5. Simplify: $\frac{\sqrt n(\bar X - \mu)/\sigma}{\sqrt{S^2/\sigma^2}} = \frac{\sqrt n(\bar X - \mu)}{\sqrt{S^2}} = U$. The unknown $\sigma$ cancels, which is the whole point.

**Conclusion:** $U \sim t_{n-1}$. $\blacksquare$

[[STAT 132 Midterm 2 Review#^l10-thm-2-1|↩ back to problem]]

## L10 Ex 3.1
![[STAT 132 Midterm 2 Review#^l10-ex-3-1]]

1. Symmetry: $\mathbb{P}(-2 \le T \le 2) = \mathbb{P}(T \le 2) - \mathbb{P}(T \le -2) = 2\mathbb{P}(T \le 2) - 1$.
2. $t_5$ row: the 0.95 column is 2.015, close to 2, so $\mathbb{P}(T \le 2) \approx 0.95$.

**Answer:** $\approx 2(0.95) - 1 = 0.90$ [exact 0.898]. This is the professor's lookup from the Oct 29 lecture.

[[STAT 132 Midterm 2 Review#^l10-ex-3-1|↩ back to problem]]

## L10 Ex 3.2
![[STAT 132 Midterm 2 Review#^l10-ex-3-2]]

By L10 Thm 2.1 with $n = 10$, $\mu = 50$: $\frac{\sqrt{10}(\bar X - 50)}{S} \sim t_9$.

**Answer:** $t_9$. The known $\sigma^2 = 4$ is not used, since $S$ replaces $\sigma$.

[[STAT 132 Midterm 2 Review#^l10-ex-3-2|↩ back to problem]]

## L10 Ex 3.3
![[STAT 132 Midterm 2 Review#^l10-ex-3-3]]

**Idea:** the 90th percentile of $\bar X$ is the value $x$ with $\mathbb{P}(\bar X \le x) = 0.90$. Turn the event into one about $U \sim t_{25}$.

1. $\bar X \le x \iff U = \frac{\sqrt{26}(\bar X - \mu)}{\sqrt{S^2}} \le \frac{\sqrt{26}(x - \mu)}{\sqrt{S^2}}$.
2. Set the right side equal to $t_{25,0.90} = 1.316$.
3. Solve: $x = \mu + \frac{1.316}{\sqrt{26}}\sqrt{S^2} = \mu + 0.258\sqrt{S^2}$.

**Answer:** 90th percentile $= \mu + 0.258\sqrt{S^2}$.

[[STAT 132 Midterm 2 Review#^l10-ex-3-3|↩ back to problem]]

## L10 Ex 3.4
![[STAT 132 Midterm 2 Review#^l10-ex-3-4]]

**Given:** $n = 20$, target probability 0.95 (the professor's correction in class).

1. $\bar X \le \mu + c\sqrt{S^2} \iff \frac{\sqrt{20}(\bar X - \mu)}{\sqrt{S^2}} \le c\sqrt{20}$, i.e. $U \le c\sqrt{20}$ with $U \sim t_{19}$.
2. $\mathbb{P}(U \le c\sqrt{20}) = 0.95 \Rightarrow c\sqrt{20} = t_{19,0.95} = 1.729$.
3. $c = \frac{1.729}{\sqrt{20}} = \frac{1.729}{4.472}$.

**Answer:** $c \approx 0.3866$ (matches the lecture).

[[STAT 132 Midterm 2 Review#^l10-ex-3-4|↩ back to problem]]

## L11 Thm 2.1
![[STAT 132 Midterm 2 Review#^l11-thm-2-1]]

1. Pivotal: $Z = \frac{\sqrt n(\bar X - \mu)}{\sigma} \sim N(0,1)$, with no $\mu$ in its distribution.
2. $\mathbb{P}\left(-z_{1-\alpha/2} \le Z \le z_{1-\alpha/2}\right) = (1 - \tfrac\alpha2) - \tfrac\alpha2 = 1 - \alpha$.
3. Rearrange (as in Disc 6 Q2): $\bar X - z_{1-\alpha/2}\frac{\sigma}{\sqrt n} \le \mu \le \bar X + z_{1-\alpha/2}\frac{\sigma}{\sqrt n}$.

**Conclusion:** $\bar X \pm z_{1-\alpha/2}\frac{\sigma}{\sqrt n}$ is a $1-\alpha$ CI. $\blacksquare$

[[STAT 132 Midterm 2 Review#^l11-thm-2-1|↩ back to problem]]

## L11 Ex 2.1
![[STAT 132 Midterm 2 Review#^l11-ex-2-1]]

**Given:** $n = 26$, $\bar x = 1.3$, $\sigma^2 = \frac14$ known so $\sigma = \frac12$; 95%.

1. $z_{0.975} = 1.96$.
2. Half-width: $1.96\cdot\frac{0.5}{\sqrt{26}} = \frac{0.98}{5.099} = 0.192$.

**Answer:** $1.3 \pm 0.192 = (1.108,\ 1.492)$ inches.

[[STAT 132 Midterm 2 Review#^l11-ex-2-1|↩ back to problem]]

## L11 Thm 2.2
![[STAT 132 Midterm 2 Review#^l11-thm-2-2]]

1. Pivotal: $U = \frac{\sqrt n(\bar X - \mu)}{S} \sim t_{n-1}$ (L10 Thm 2.1), with no $\mu$ or $\sigma$ in its distribution.
2. The $t$ is symmetric, so $\mathbb{P}\left(-t_{n-1,1-\alpha/2} \le U \le t_{n-1,1-\alpha/2}\right) = 1 - \alpha$.
3. Rearrange as before, with $S$ in place of $\sigma$.

**Conclusion:** $\bar X \pm t_{n-1,1-\alpha/2}\frac{S}{\sqrt n}$ is a $1-\alpha$ CI. $\blacksquare$ It is wider than the $z$ interval because $t$ quantiles are bigger (heavier tails) to pay for estimating $\sigma$.

[[STAT 132 Midterm 2 Review#^l11-thm-2-2|↩ back to problem]]

## L11 Ex 2.2
![[STAT 132 Midterm 2 Review#^l11-ex-2-2]]

**Given:** $n = 26$, $\bar x = 1.3$, $S^2 = 0.45$ so $S = 0.6708$; 95%; $\sigma$ unknown.

1. $t_{25,0.975} = 2.060$.
2. Half-width: $2.060\cdot\frac{0.6708}{\sqrt{26}} = 2.060\cdot0.1316 = 0.271$.

**Answer:** $1.3 \pm 0.271 = (1.029,\ 1.571)$ inches.

[[STAT 132 Midterm 2 Review#^l11-ex-2-2|↩ back to problem]]

## L11 Sec 3
![[STAT 132 Midterm 2 Review#^l11-sec-3]]

**The point to say on an exam:** "95% confident" is about the *procedure*. Before sampling, $(L, U)$ is random and covers $\theta$ with probability 0.95. After you compute $(1.03, 1.57)$, nothing is random: it either contains $\mu$ or it does not. Over many repeated samples, about 95% of the intervals built this way contain $\mu$. In the R demo, about 95 of the 100 simulated intervals cross the dashed line at $\mu = 5.1$.

**Wrong phrasing to avoid:** "there is a 95% probability that $\mu$ is in $(1.03, 1.57)$."

[[STAT 132 Midterm 2 Review#^l11-sec-3|↩ back to problem]]

## L11 Ex 4.1
![[STAT 132 Midterm 2 Review#^l11-ex-4-1]]

1. Pivotal: $Q = \frac{(n-1)S^2}{\sigma^2} \sim \chi^2_{n-1}$.
2. $\mathbb{P}\left(\chi^2_{n-1,\alpha/2} \le \frac{(n-1)S^2}{\sigma^2} \le \chi^2_{n-1,1-\alpha/2}\right) = 1 - \alpha$ (equal tails).
3. Take reciprocals (flip) and multiply by $(n-1)S^2$.

**Answer:**
$$\left(\frac{(n-1)S^2}{\chi^2_{n-1,\,1-\alpha/2}},\ \frac{(n-1)S^2}{\chi^2_{n-1,\,\alpha/2}}\right).$$
Not symmetric around $S^2$, because the $\chi^2$ is skewed.

[[STAT 132 Midterm 2 Review#^l11-ex-4-1|↩ back to problem]]

## L11 Ex 4.2
![[STAT 132 Midterm 2 Review#^l11-ex-4-2]]

1. $(n-1)S^2 = 25(0.45) = 11.25$.
2. $\chi^2_{25,0.025} = 13.12$, $\chi^2_{25,0.975} = 40.65$.
3. $\left(\frac{11.25}{40.65}, \frac{11.25}{13.12}\right)$.

**Answer:** $(0.277,\ 0.857)$ square inches.

[[STAT 132 Midterm 2 Review#^l11-ex-4-2|↩ back to problem]]

## Quiz 1
![[STAT 132 Midterm 2 Review#^quiz-1]]

1. $\mu = 10$ known, so $W = \frac{15\widehat{\sigma^2}}{\sigma^2} = 15\widehat{\sigma^2} \sim \chi^2_{15}$ (L8 Ex 2.1; $n$ df since nothing is estimated).
2. Multiply by 15: $0.8 \le \widehat{\sigma^2} \le 1.5 \iff 12 \le W \le 22.5$.
3. $\chi^2_{15}$ row: $\chi^2_{15,0.90} = 22.31$, so $F(22.5) \approx 0.90$; 12 is between $\chi^2_{15,0.25} = 11.04$ and $\chi^2_{15,0.50} = 14.34$, so $F(12) \approx 0.3$.

**Answer:** $\approx 0.9 - 0.3 = 0.6$, choice (C) [exact 0.584]. The professor's point after the quiz: subtracting the *true* mean 10 is what makes each $\frac{X_i - 10}{\sigma}$ a standard normal.

[[STAT 132 Midterm 2 Review#^quiz-1|↩ back to problem]]

## Quiz 2
![[STAT 132 Midterm 2 Review#^quiz-2]]

1. $U \sim t_4$ (L10 Thm 2.1, $n - 1 = 4$).
2. $E(U^2) = \text{Var}(U) + [E(U)]^2$, and $E(U) = 0$ (the $t$ is symmetric and $m > 1$).
3. $\text{Var}(t_m) = \frac{m}{m-2}$ for $m > 2$: $\frac42 = 2$.

**Answer:** $E(U^2) = 2$, choice (B).

[[STAT 132 Midterm 2 Review#^quiz-2|↩ back to problem]]
