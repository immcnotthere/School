---
aliases:
  - "Discussion 6 Stats132"
  - "STAT 132 Discussion 6"
  - "Stats132 Disc 6"
type: study
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
item_type: discussion-worked-trace
discussion: 6
worksheet_year: 2025
status: not-started
problems: 4
completed_problems: []
source: "STAT132/files/homework/STAT132 Discussion 06 (W25 worksheet).pdf"
retention_input: "System/reps.csv"
retention_words: "System/rep-words.jsonl"
retention_output: "System/index/memory.json"
created: 2026-11-22
---
# Discussion 6 Stats132

**Source:** [Discussion 6 W25 worksheet](https://github.com/immcnotthere/School/blob/main/STAT132/files/homework/STAT132%20Discussion%2006%20%28W25%20worksheet%29.pdf). Prompts preserve the source's mathematical task, but are typeset afresh for readable Obsidian Markdown.

**Method:** Start with the prompt (without reading the solution), identify the first applicable cue, follow the Mermaid branch, and solve. The concept links in each cue table point to existing notes or intentionally unresolved Obsidian notes for future creation. **Nothing is marked complete until an independent attempt is reported.**

| Question | Focus | Status |
|---|---|---|
| [[#Problem 1 — Make a t distribution from five normals|1]] | Make a t distribution from five normals | ☐ Not assessed |
| [[#Problem 2 — Prove a Normal-mean confidence interval|2]] | Prove a Normal-mean confidence interval | ☐ Not assessed |
| [[#Problem 3 — Sample size for a very short 95% CI|3]] | Sample size for a very short 95% CI | ☐ Not assessed |
| [[#Problem 4 — CI for an exponential mean using a pivot|4]] | CI for an exponential mean using a pivot | ☐ Not assessed |

---

## Problem 1 — Make a t distribution from five normals

### Mathematical restatement

$X_1,\ldots,X_5\overset{\rm iid}{\sim}N(0,1)$, and $U=c(X_1+X_2)/\sqrt{X_3^2+X_4^2+X_5^2}$. Find $c$ so $U$ has a $t$ distribution.

### Worked solution

**S1 — Standardize the numerator.** Since $X_1+X_2\sim N(0,2)$, $Z=(X_1+X_2)/\sqrt2\sim N(0,1)$.

**S2 — Recognize independent chi-square denominator.** $V=X_3^2+X_4^2+X_5^2\sim\chi^2_3$, independent of $Z$ because it uses different independent observations.

**S3 — Compare with t definition.** $t_3=Z/\sqrt{V/3}=\sqrt{3/2}(X_1+X_2)/\sqrt V$. Thus $\boxed{c=\sqrt{3/2}}$ and $U\sim t_3$.

### Mermaid decision route

~~~mermaid
flowchart TD
  A["P1: Make a t distribution from five normals"] --> B{"Do numerator and denominator involve independent normals?"}
  B -->|"Yes"| N0["S1: Standardize the numerator"]
  B -->|"Unclear"| R["Review cue: normalize numerator before reading t formula"]
  R --> N0
  N0 --> N1["S2: Recognize independent chi-square denominator"]
  N1 --> N2["S3: Compare with t definition"]
  N2 --> Z["Check result and assumptions"]
  style R stroke:#777,stroke-dasharray:4 4
~~~

### Prerequisite and cue trace

| Step | General concept links | Recognition cue | Required move |
|---|---|---|---|
| S1 | [[Normal Distribution]]; [[Linear Transformation Property of the Normal Distribution]] | Sum of two normals in numerator | Normalize its variance to one |
| S2 | [[Chi-Square Distribution]]; [[Independence of Random Variables]] | Three squared standard normals | Use chi² with 3 df |
| S3 | [[t Distribution]]; [[Degrees of Freedom]] | Standard normal divided by sqrt chi²/df | Match factors and solve c |

**Answer checkpoint:** c is sqrt(3/2), df=3.

**Failure-trace hook:** None observed yet. On an actual attempt, mark the *first* broken S-step, the exact general prerequisite skill, the cue missed, and the student's complete unedited words in the embedded log. Do not infer an FSRS rep from reading the walkthrough.

---

## Problem 2 — Prove a Normal-mean confidence interval

### Mathematical restatement

For iid $N(\mu,\sigma^2)$ with **known** $\sigma$, show $\left(\bar X-z_{(1+\gamma)/2}\frac{\sigma}{\sqrt n},\ \bar X+z_{(1+\gamma)/2}\frac{\sigma}{\sqrt n}\right)$ covers $\mu$ with probability $\gamma=1-\alpha$, where $z_q=\Phi^{-1}(q)$.

### Worked solution

**S1 — Identify the standard normal pivot.** $Z=(\bar X-\mu)/(\sigma/\sqrt n)\sim N(0,1)$ since the data are Normal and the variance is known.

**S2 — Choose symmetric tail probability.** For $z=z_{(1+\gamma)/2}$, $P(-z\le Z\le z)=\Phi(z)-\Phi(-z)=\gamma$. Each tail has probability $(1-\gamma)/2=\alpha/2$.

**S3 — Invert for the unknown mean.** $-z\le (\bar X-\mu)/(\sigma/\sqrt n)\le z$ is equivalent to $\bar X-z\sigma/\sqrt n\le\mu\le\bar X+z\sigma/\sqrt n$. Thus the displayed interval has $\boxed{P_\mu(\mu\in CI)=\gamma}$.

### Mermaid decision route

~~~mermaid
flowchart TD
  A["P2: Prove a Normal-mean confidence interval"] --> B{"Is the population standard deviation known?"}
  B -->|"Yes"| N0["S1: Identify the standard normal pivot"]
  B -->|"Unclear"| R["Review cue: use Z not t when sigma is given"]
  R --> N0
  N0 --> N1["S2: Choose symmetric tail probability"]
  N1 --> N2["S3: Invert for the unknown mean"]
  N2 --> Z["Check result and assumptions"]
  style R stroke:#777,stroke-dasharray:4 4
~~~

### Prerequisite and cue trace

| Step | General concept links | Recognition cue | Required move |
|---|---|---|---|
| S1 | [[Sample Mean]]; [[Standard Normal Distribution]] | Known sigma and normal data | Standardize Xbar |
| S2 | [[Standard Normal CDF (Φ)]]; [[Quantile Function]] | Two-sided coverage gamma | Allocate alpha/2 to each tail |
| S3 | [[Pivotal Quantity]]; [[Confidence Interval from a Pivotal]] | Prove coverage, not compute a point estimate | Algebraically solve the inequality for mu |

**Answer checkpoint:** coverage is 1-alpha=gamma.

**Failure-trace hook:** None observed yet. On an actual attempt, mark the *first* broken S-step, the exact general prerequisite skill, the cue missed, and the student's complete unedited words in the embedded log. Do not infer an FSRS rep from reading the walkthrough.

---

## Problem 3 — Sample size for a very short 95% CI

### Mathematical restatement

Under the same Normal mean model with known $\sigma$, find the smallest integer $n$ making the full length of a 95% CI for $\mu$ **strictly less** than $0.01\sigma$.

### Worked solution

**S1 — Write the full interval length.** The 95% Normal interval has half-width $z_{0.975}\sigma/\sqrt n$, so full length $L=2z_{0.975}\sigma/\sqrt n$. The factor 2 is essential.

**S2 — Solve the strict length inequality.** $2z_{0.975}\sigma/\sqrt n<0.01\sigma$ gives $\sqrt n>200z_{0.975}$ and $n>(200z_{0.975})^2\approx153658.35$.

**S3 — Round with exact quantile.** The smallest integer is $\boxed{n=153659}$ using $z_{0.975}\approx1.9599639845$. If a table rounds to $z=1.96$, a conservative strict-bound calculation yields $153665$; state the precision used.

### Mermaid decision route

~~~mermaid
flowchart TD
  A["P3: Sample size for a very short 95% CI"] --> B{"Is the requested width the FULL interval?"}
  B -->|"Yes"| N0["S1: Write the full interval length"]
  B -->|"Unclear"| R["Review cue: avoid dropping factor 2 or treating < as <="]
  R --> N0
  N0 --> N1["S2: Solve the strict length inequality"]
  N1 --> N2["S3: Round with exact quantile"]
  N2 --> Z["Check result and assumptions"]
  style R stroke:#777,stroke-dasharray:4 4
~~~

### Prerequisite and cue trace

| Step | General concept links | Recognition cue | Required move |
|---|---|---|---|
| S1 | [[Confidence Interval for the Mean of a Normal Distribution]]; [[Standard Normal CDF (Φ)]] | Question asks full CI length | Use 2 times margin of error |
| S2 | [[Inequalities]]; [[Quantile Function]] | Strictly less than 0.01 sigma | Cancel sigma and square |
| S3 | [[Sample Size Planning]] | Minimum integer n | Use exact quantile; handle strict inequality |

**Answer checkpoint:** exact quantile gives n=153659.

**Failure-trace hook:** None observed yet. On an actual attempt, mark the *first* broken S-step, the exact general prerequisite skill, the cue missed, and the student's complete unedited words in the embedded log. Do not infer an FSRS rep from reading the walkthrough.

---

## Problem 4 — CI for an exponential mean using a pivot

### Mathematical restatement

$X_i$ iid exponential with unknown **mean** $\mu$ (not rate). Construct a $1-\alpha$ CI for $\mu$ using the given pivotal statistic $\mu^{-1}\sum_iX_i$.

### Worked solution

**S1 — Identify the sum's distribution.** For exponential mean $\mu$, each observation has rate $1/\mu$, so $S/\mu=\sum_i X_i/\mu\sim\operatorname{Gamma}(n,\mathrm{rate}=1)$. Hence $V=2S/\mu\sim\chi^2_{2n}$.

**S2 — Bound the pivotal quantity with quantiles.** Let $q_L=\chi^2_{2n,\alpha/2}$ and $q_U=\chi^2_{2n,1-\alpha/2}$. Then $P(q_L\le2S/\mu\le q_U)=1-\alpha$.

**S3 — Invert inequalities for positive mu.** Because $S,\mu,q_L,q_U>0$, solving for $\mu$ reverses reciprocal bounds: $\boxed{CI_\mu=\left[\frac{2S}{q_U},\frac{2S}{q_L}\right]}$. Check that the larger chi-square quantile is in the **lower** endpoint denominator.

### Mermaid decision route

~~~mermaid
flowchart TD
  A["P4: CI for an exponential mean using a pivot"] --> B{"Does unknown parameter represent the mean rather than rate?"}
  B -->|"Yes"| N0["S1: Identify the sum's distribution"]
  B -->|"Unclear"| R["Review cue: reciprocal inversion changes endpoint order"]
  R --> N0
  N0 --> N1["S2: Bound the pivotal quantity with quantiles"]
  N1 --> N2["S3: Invert inequalities for positive mu"]
  N2 --> Z["Check result and assumptions"]
  style R stroke:#777,stroke-dasharray:4 4
~~~

### Prerequisite and cue trace

| Step | General concept links | Recognition cue | Required move |
|---|---|---|---|
| S1 | [[Exponential Distribution]]; [[Gamma Distribution]] | Pivotal hint uses sum divided by mean | Recognize Gamma(n, rate 1) and chi²2n |
| S2 | [[Chi-Square Distribution]]; [[Quantile Function]] | Desired 1-alpha central probability | Place alpha/2 in each tail |
| S3 | [[Confidence Interval from a Pivotal]]; [[Equivalent equations]] | Invert inequalities involving 1/mu | Put qU in lower endpoint denominator |

**Answer checkpoint:** interval is [2S/qU,2S/qL].

**Failure-trace hook:** None observed yet. On an actual attempt, mark the *first* broken S-step, the exact general prerequisite skill, the cue missed, and the student's complete unedited words in the embedded log. Do not infer an FSRS rep from reading the walkthrough.

---

## Shared concept dependency map

~~~mermaid
flowchart LR
  C1["Normal Distribution"] --> Q1["Problem 1: Make a t distribution from five normals"]
  C2["Sample Mean"] --> Q2["Problem 2: Prove a Normal-mean confidence interval"]
  C3["Confidence Interval for the Mean of a Normal Distribution"] --> Q3["Problem 3: Sample size for a very short 95% CI"]
  C4["Exponential Distribution"] --> Q4["Problem 4: CI for an exponential mean using a pivot"]
~~~

## Dated review and failure log — CSV inside this note

**No attempts recorded.** Add rows below only for actual study attempts, using actual dates and exact verbatim student wording. This Markdown log is not automatically read by FSRS.

```csv
date,problem,step,node,outcome,ledger_ref,ledger_status,said,agent_note
```

**Retention contract:** Live attempt data originates in the vault's `System/reps.csv` via `brain study log`; `System/rep-words.jsonl` joins the user's *unmodified* `said` to the returned attempt `ref`. The model writes `System/index/memory.json`, which is output and should not be edited. A new concept link is **not** evidence of failure. A local handwritten CSV row here does **not** update the memory curve.

**Review target:** 4 problems remain unassessed in this guide.
