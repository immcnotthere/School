---
aliases:
  - "Discussion 7 Stats132"
  - "STAT 132 Discussion 7"
  - "Stats132 Disc 7"
type: study
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
item_type: discussion-worked-trace
discussion: 7
worksheet_year: 2025
status: not-started
problems: 4
completed_problems: []
source: "STAT132/files/homework/STAT132 Discussion 07 (W25 worksheet).pdf"
retention_input: "System/reps.csv"
retention_words: "System/rep-words.jsonl"
retention_output: "System/index/memory.json"
created: 2026-11-22
---
# Discussion 7 Stats132

**Source:** [Discussion 7 W25 worksheet](https://github.com/immcnotthere/School/blob/main/STAT132/files/homework/STAT132%20Discussion%2007%20%28W25%20worksheet%29.pdf). Prompts preserve the source's mathematical task, but are typeset afresh for readable Obsidian Markdown.

**Method:** Start with the prompt (without reading the solution), identify the first applicable cue, follow the Mermaid branch, and solve. The concept links in each cue table point to existing notes or intentionally unresolved Obsidian notes for future creation. **Nothing is marked complete until an independent attempt is reported.**

| Question | Focus | Status |
|---|---|---|
| [[#Problem 1 — Unbiasedness of sample raw moments|1]] | Unbiasedness of sample raw moments | ☐ Not assessed |
| [[#Problem 2 — Unbiased estimator of squared population mean|2]] | Unbiased estimator of squared population mean | ☐ Not assessed |
| [[#Problem 3 — Optimal unbiased weighting of two samples|3]] | Optimal unbiased weighting of two samples | ☐ Not assessed |
| [[#Problem 4 — Unbiased correction of Uniform sample maximum|4]] | Unbiased correction of Uniform sample maximum | ☐ Not assessed |

---

## Problem 1 — Unbiasedness of sample raw moments

### Mathematical restatement

For iid $X_1,\ldots,X_n$ from an unknown distribution with finite moments, show $\hat m_k=\frac1n\sum_iX_i^k$ is unbiased for $m_k=E(X^k)$ for integers $k\ge1$.

### Worked solution

**S1 — Write expected value of the proposed estimator.** $E[\hat m_k]=E[\frac1n\sum_iX_i^k]$. No distribution formula is needed if the moments exist.

**S2 — Apply linearity and identical distribution.** $E[\hat m_k]=\frac1n\sum_iE[X_i^k]=\frac1n\cdot n E[X^k]=E[X^k]$.

**S3 — State the conclusion.** $\boxed{E[\hat m_k]=m_k}$; therefore $\hat m_k$ is unbiased. Independence is part of iid sampling but **linearity of expectation does not itself require independence**.

### Mermaid decision route

~~~mermaid
flowchart TD
  A["P1: Unbiasedness of sample raw moments"] --> B{"Does the expectation exist?"}
  B -->|"Yes"| N0["S1: Write expected value of the proposed estimator"]
  B -->|"Unclear"| R["Review cue: do not assume a named distribution"]
  R --> N0
  N0 --> N1["S2: Apply linearity and identical distribution"]
  N1 --> N2["S3: State the conclusion"]
  N2 --> Z["Check result and assumptions"]
  style R stroke:#777,stroke-dasharray:4 4
~~~

### Prerequisite and cue trace

| Step | General concept links | Recognition cue | Required move |
|---|---|---|---|
| S1 | [[Unbiased Estimator]]; [[Moments and Central Moments]] | Show unbiased for raw moment | Take expectation of estimator |
| S2 | [[Linearity of Expectation]]; [[Expectation of Independent Random Variables]] | Average of k-th powers | Move expectation inside sum |
| S3 | [[Unbiased Estimator]] | Expected value matches target | Conclude unbiasedness |

**Answer checkpoint:** yes for all finite k-th moments.

**Failure-trace hook:** None observed yet. On an actual attempt, mark the *first* broken S-step, the exact general prerequisite skill, the cue missed, and the student's complete unedited words in the embedded log. Do not infer an FSRS rep from reading the walkthrough.

---

## Problem 2 — Unbiased estimator of squared population mean

### Mathematical restatement

For iid sample with finite moments and unknown distribution, find an estimator unbiased for $\{E[X]\}^2=\mu^2$; assume $n\ge2$.

### Worked solution

**S1 — Start with the tempting biased estimator.** $E[\bar X^2]=\operatorname{Var}(\bar X)+\mu^2=\sigma^2/n+\mu^2$. Thus $\bar X^2$ is **not** unbiased except in the degenerate zero-variance case.

**S2 — Estimate and subtract the bias.** With $S^2=\sum_i(X_i-\bar X)^2/(n-1)$, $E[S^2]=\sigma^2$. Therefore $\boxed{\widehat{\mu^2}=\bar X^2-S^2/n}$ is unbiased.

**S3 — Check an alternative pairwise form.** Equivalently, $\widehat{\mu^2}=\frac{1}{n(n-1)}\sum_{i\ne j}X_iX_j$. Independence gives $E[X_iX_j]=\mu^2$ for distinct indices.

### Mermaid decision route

~~~mermaid
flowchart TD
  A["P2: Unbiased estimator of squared population mean"] --> B{"Is the target square of the mean, not second moment?"}
  B -->|"Yes"| N0["S1: Start with the tempting biased estimator"]
  B -->|"Unclear"| R["Review cue: do not confuse E(X²) and [E(X)]²"]
  R --> N0
  N0 --> N1["S2: Estimate and subtract the bias"]
  N1 --> N2["S3: Check an alternative pairwise form"]
  N2 --> Z["Check result and assumptions"]
  style R stroke:#777,stroke-dasharray:4 4
~~~

### Prerequisite and cue trace

| Step | General concept links | Recognition cue | Required move |
|---|---|---|---|
| S1 | [[Variance of the Sample Mean]]; [[Properties of Variance]] | Estimate a square of expectation | Distinguish E(Xbar²) from (E Xbar)² |
| S2 | [[Unbiased Estimator of the Variance]]; [[Unbiased Estimator]] | Can estimate sigma² without bias | Subtract S²/n |
| S3 | [[Independence of Random Variables]]; [[Linearity of Expectation]] | Want an independent check | Pair distinct observations |

**Answer checkpoint:** Xbar² - S²/n is unbiased.

**Failure-trace hook:** None observed yet. On an actual attempt, mark the *first* broken S-step, the exact general prerequisite skill, the cue missed, and the student's complete unedited words in the embedded log. Do not infer an FSRS rep from reading the walkthrough.

---

## Problem 3 — Optimal unbiased weighting of two samples

### Mathematical restatement

Independent samples A ($m$ observations) and B ($n$ observations) have common mean $\theta$; response variance is $\operatorname{Var}(A)=4\operatorname{Var}(B)$. For $\hat\theta=\alpha\bar X_m+(1-\alpha)\bar Y_n$, (a) when is it unbiased? (b) choose $\alpha$ to minimize variance for fixed $m,n$.

### Worked solution

**S1 — Check unbiasedness for arbitrary alpha.** $E[\hat\theta]=\alpha\theta+(1-\alpha)\theta=\theta$ for every real $\alpha$ and positive sample sizes $m,n$ (given finite means). Unbiasedness does **not** determine $\alpha$ here.

**S2 — Write variance using independence.** Let $\operatorname{Var}(B)=v$, so $\operatorname{Var}(\bar X_m)=4v/m$ and $\operatorname{Var}(\bar Y_n)=v/n$. Then $\operatorname{Var}(\hat\theta)=4v\alpha^2/m+v(1-\alpha)^2/n$.

**S3 — Differentiate the quadratic.** $d\operatorname{Var}/d\alpha=8v\alpha/m-2v(1-\alpha)/n=0$ gives $\boxed{\alpha^\star=m/(m+4n)}$. The second derivative $8v/m+2v/n>0$ ensures a minimum. The B weight is $1-\alpha^\star=4n/(m+4n)$.

### Mermaid decision route

~~~mermaid
flowchart TD
  A["P3: Optimal unbiased weighting of two samples"] --> B{"Are the samples independent with equal mean?"}
  B -->|"Yes"| N0["S1: Check unbiasedness for arbitrary alpha"]
  B -->|"Unclear"| R["Review cue: do not put 4 in numerator of A weight"]
  R --> N0
  N0 --> N1["S2: Write variance using independence"]
  N1 --> N2["S3: Differentiate the quadratic"]
  N2 --> Z["Check result and assumptions"]
  style R stroke:#777,stroke-dasharray:4 4
~~~

### Prerequisite and cue trace

| Step | General concept links | Recognition cue | Required move |
|---|---|---|---|
| S1 | [[Unbiased Estimator]]; [[Linearity of Expectation]] | Both sample populations share theta | Check coefficients sum to 1 |
| S2 | [[Variance of a Sum of Independent Random Variables]]; [[Variance of the Sample Mean]] | Different precisions and independent samples | Sum weighted variances, square weights |
| S3 | [[Derivative]]; [[Quadratic functions]] | Minimum variance for alpha | Differentiate, solve and verify curvature |

**Answer checkpoint:** any alpha is unbiased; optimal alpha=m/(m+4n).

**Failure-trace hook:** None observed yet. On an actual attempt, mark the *first* broken S-step, the exact general prerequisite skill, the cue missed, and the student's complete unedited words in the embedded log. Do not infer an FSRS rep from reading the walkthrough.

---

## Problem 4 — Unbiased correction of Uniform sample maximum

### Mathematical restatement

$X_i$ iid Uniform$[0,\theta]$, $Y=\max_iX_i$. Show $\hat\theta=\frac{n+1}{n}Y$ is unbiased for $\theta$.

### Worked solution

**S1 — Derive maximum CDF.** For $0\le y\le\theta$, $F_Y(y)=P(\max_i X_i\le y)=P(X_1\le y,\ldots,X_n\le y)=(y/\theta)^n$.

**S2 — Differentiate to find density.** $f_Y(y)=n y^{n-1}/\theta^n$ on $(0,\theta)$. Then $E[Y]=\int_0^\theta y f_Y(y)\,dy=\frac{n}{n+1}\theta$.

**S3 — Apply bias-correction factor.** $E[\frac{n+1}{n}Y]=\frac{n+1}{n}E[Y]=\theta$. Thus $\boxed{\hat\theta=(n+1)Y/n}$ is unbiased.

### Mermaid decision route

~~~mermaid
flowchart TD
  A["P4: Unbiased correction of Uniform sample maximum"] --> B{"Does the estimator depend on the maximum?"}
  B -->|"Yes"| N0["S1: Derive maximum CDF"]
  B -->|"Unclear"| R["Review cue: do not confuse max expectation with sample mean"]
  R --> N0
  N0 --> N1["S2: Differentiate to find density"]
  N1 --> N2["S3: Apply bias-correction factor"]
  N2 --> Z["Check result and assumptions"]
  style R stroke:#777,stroke-dasharray:4 4
~~~

### Prerequisite and cue trace

| Step | General concept links | Recognition cue | Required move |
|---|---|---|---|
| S1 | [[Uniform Distribution (Continuous)]]; [[Distribution of the Sample Maximum]] | Estimator is maximum of iid Uniform | CDF of max is F^n |
| S2 | [[Cumulative Distribution Function]]; [[Expectation of a Continuous Random Variable]] | Want E[max] | Differentiate and integrate |
| S3 | [[Unbiased Estimator]]; [[Linearity of Expectation]] | Given a multiplicative correction | Move constant outside expectation |

**Answer checkpoint:** E[max]=n theta/(n+1).

**Failure-trace hook:** None observed yet. On an actual attempt, mark the *first* broken S-step, the exact general prerequisite skill, the cue missed, and the student's complete unedited words in the embedded log. Do not infer an FSRS rep from reading the walkthrough.

---

## Shared concept dependency map

~~~mermaid
flowchart LR
  C1["Unbiased Estimator"] --> Q1["Problem 1: Unbiasedness of sample raw moments"]
  C2["Variance of the Sample Mean"] --> Q2["Problem 2: Unbiased estimator of squared population mean"]
  C3["Unbiased Estimator"] --> Q3["Problem 3: Optimal unbiased weighting of two samples"]
  C4["Uniform Distribution (Continuous)"] --> Q4["Problem 4: Unbiased correction of Uniform sample maximum"]
~~~

## Dated review and failure log — CSV inside this note

**No attempts recorded.** Add rows below only for actual study attempts, using actual dates and exact verbatim student wording. This Markdown log is not automatically read by FSRS.

```csv
date,problem,step,node,outcome,ledger_ref,ledger_status,said,agent_note
```

**Retention contract:** Live attempt data originates in the vault's `System/reps.csv` via `brain study log`; `System/rep-words.jsonl` joins the user's *unmodified* `said` to the returned attempt `ref`. The model writes `System/index/memory.json`, which is output and should not be edited. A new concept link is **not** evidence of failure. A local handwritten CSV row here does **not** update the memory curve.

**Review target:** 4 problems remain unassessed in this guide.
