---
type: problem
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "School/STAT 132/Discussions/stat132-disc06-w25.pdf"
uses:
  - "[[t Distribution]]"
  - "[[Sum of Squares of iid Standard Normal Is Chi-Square]]"
  - "[[Linear Transformation Property of the Normal Distribution]]"
  - "[[Confidence Interval for the Mean of a Normal Distribution]]"
  - "[[Standard Normal CDF (Φ)]]"
  - "[[Quantile Function]]"
  - "[[Pivotal Quantity]]"
  - "[[Confidence Interval from a Pivotal]]"
  - "[[Gamma Distribution]]"
  - "[[Exponential distribution]]"
---
# STAT 132 Discussion 6

Discussion worksheet (Winter 2025 set), [[stat132-disc06-w25.pdf]], 1 page. Practice for [[STAT 132 Lecture 11 - Interval Estimation|Lecture 11]] (skills 2, 5, 9, 10, 11 in its checklist). Quote blocks are verbatim from the sheet; answers are Claude's, folded, numbers checked in scipy.

| Q | What it asks | Concepts |
|---|---|---|
| 1 | c so that c(X1+X2)/sqrt(X3^2+X4^2+X5^2) is t | [[t Distribution]], [[Sum of Squares of iid Standard Normal Is Chi-Square]], [[Linear Transformation Property of the Normal Distribution]] |
| 2 | show (Xbar -/+ Phi^-1((1+gamma)/2) sigma/sqrt n) is a gamma CI | [[Confidence Interval for the Mean of a Normal Distribution]], [[Standard Normal CDF (Φ)]], [[Quantile Function]] |
| 3 | n so a 95% CI for mu has length < 0.01 sigma | [[Confidence Interval for the Mean of a Normal Distribution]] |
| 4 | CI for an exponential mean via the pivot (1/mu) sum X_i | [[Pivotal Quantity]], [[Confidence Interval from a Pivotal]], [[Gamma Distribution]], [[Exponential distribution]] |

---

> **1.** Suppose that five random variables $X_1, \dots, X_5$ are independently sampled from a standard normal distribution. Find a value for the constant $c$ such that the random variable
> $$U = \frac{c(X_1 + X_2)}{\sqrt{X_3^2 + X_4^2 + X_5^2}}$$
> will have a $t$ distribution.

> [!example]- Answer (Claude)
> - Target shape: $t_k = \dfrac{Z}{\sqrt{V/k}}$, $Z \sim N(0,1)$, $V \sim \chi^2_k$, independent.
> - Top: $X_1 + X_2 \sim N(0, 2)$, so $Z = \dfrac{X_1+X_2}{\sqrt 2} \sim N(0,1)$.
> - Bottom: $V = X_3^2+X_4^2+X_5^2 \sim \chi^2_3$, independent of $Z$ (different $X$'s).
> - $t_3 = \dfrac{(X_1+X_2)/\sqrt2}{\sqrt{V/3}} = \dfrac{\sqrt3}{\sqrt2}\cdot\dfrac{X_1+X_2}{\sqrt V}$.
> - So $c = \sqrt{3/2} \approx 1.225$, and $U \sim t_3$.

> [!note]- My correction
> 

> **2.** Suppose that $X_1, \dots, X_n$ form a random sample from the normal distribution with unknown mean $\mu$ and known variance $\sigma^2$. Let $\Phi(\cdot)$ stand for the CDF of the standard normal distribution, and let $\Phi^{-1}(\cdot)$ be its inverse. Show that the following interval is a $1 - \alpha = \gamma$ confidence interval for $\mu$:
> $$\left(\bar X - \Phi^{-1}\!\left(\frac{1+\gamma}{2}\right)\frac{\sigma}{\sqrt n},\ \bar X + \Phi^{-1}\!\left(\frac{1+\gamma}{2}\right)\frac{\sigma}{\sqrt n}\right)$$

> [!example]- Answer (Claude)
> - Translate: $\frac{1+\gamma}{2} = \frac{2-\alpha}{2} = 1-\frac\alpha2$. So $c = \Phi^{-1}\!\left(\frac{1+\gamma}{2}\right)$ is just $z_{1-\alpha/2}$ in new clothes.
> - $Z = \sqrt n(\bar X - \mu)/\sigma \sim N(0,1)$.
> - $\mathbb P(-c < Z < c) = \Phi(c) - \Phi(-c) = 2\Phi(c) - 1 = 2\cdot\frac{1+\gamma}{2} - 1 = \gamma$. (Uses symmetry: $\Phi(-c) = 1 - \Phi(c)$.)
> - Rearrange $-c < \sqrt n(\bar X-\mu)/\sigma < c$ for $\mu$ (same steps as the Thm 2.1 proof in Lecture 11): $\bar X - c\sigma/\sqrt n < \mu < \bar X + c\sigma/\sqrt n$, with probability $\gamma$. $\square$

> [!note]- My correction
> 

> **3.** Suppose that $X_1, \dots, X_n$ form a random sample from the normal distribution with unknown mean $\mu$ and known variance $\sigma^2$. How large a random sample must be taken in order to be sure that a 95% confidence interval for $\mu$ will have length less than $0.01\sigma$?

> [!example]- Answer (Claude)
> - Length of the z-interval = upper minus lower $= 2 \cdot 1.96 \cdot \dfrac{\sigma}{\sqrt n}$.
> - Want $\dfrac{3.92\,\sigma}{\sqrt n} < 0.01\,\sigma$. The $\sigma$ cancels: $\sqrt n > 392$, so $n > 153{,}664$.
> - Answer: $n = 153{,}665$ (with $z = 1.96$). With the exact $z = 1.95996$, $n \ge 153{,}659$. Either is fine; say which $z$ you used. Round UP: a smaller $n$ fails.

> [!note]- My correction
> 

> **4.** Suppose that $X_1, \dots, X_n$ form a random sample from the exponential distribution with unknown mean $\mu$. Describe a method for constructing a $1 - \alpha$ confidence interval for $\mu$. *Hint:* Use $\frac1\mu\sum_{i=1}^n X_i$ as a pivotal quantity.

> [!example]- Answer (Claude)
> - Each $X_i \sim \text{Exp}$ with mean $\mu$, i.e. $\text{Gamma}(1, \text{rate } 1/\mu)$. A sum of $n$ independent ones: $\sum X_i \sim \text{Gamma}(n, \text{rate } 1/\mu)$.
> - Scaling by $1/\mu$ multiplies the rate by $\mu$: $Q = \frac1\mu\sum X_i \sim \text{Gamma}(n, 1)$. No $\mu$ left, so $Q$ is a pivot.
> - Quantiles: let $g_{\alpha/2}$, $g_{1-\alpha/2}$ be the Gamma$(n,1)$ quantiles (R: `qgamma(c(a/2, 1-a/2), n, 1)`). Equivalent: $2Q \sim \chi^2_{2n}$, so $g_p = \chi^2_{2n,p}/2$.
> - $\mathbb P\!\left(g_{\alpha/2} \le \frac{\sum X_i}{\mu} \le g_{1-\alpha/2}\right) = 1-\alpha$. Solving for $\mu$ flips the ends (reciprocal):
> $$\left(\frac{\sum X_i}{g_{1-\alpha/2}},\ \frac{\sum X_i}{g_{\alpha/2}}\right)$$
> - Checked by simulation ($n=10$, $\mu=3$): covers $\mu$ 95.0% of the time.

> [!note]- My correction
> 
