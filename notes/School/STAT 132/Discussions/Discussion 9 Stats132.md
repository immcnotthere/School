---
aliases:
  - "Discussion 9 Stats132"
  - "STAT 132 Discussion 9"
  - "Stats132 Disc 9"
type: study
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
item_type: discussion-worked-trace
discussion: 9
worksheet_year: 2025
status: not-started
problems: 3
completed_problems: []
source: "STAT132/files/homework/STAT132 Discussion 09 (W25 worksheet).pdf"
retention_input: "System/reps.csv"
retention_words: "System/rep-words.jsonl"
retention_output: "System/index/memory.json"
created: 2026-11-22
---
# Discussion 9 Stats132

[[Discussions Stats132|All discussions]] · [[Discussion 8 Stats132|Previous discussion]]

**Source:** [Discussion 9 W25 worksheet](https://github.com/immcnotthere/School/blob/main/STAT132/files/homework/STAT132%20Discussion%2009%20%28W25%20worksheet%29.pdf). Prompts preserve the source's mathematical task, but are typeset afresh for readable Obsidian Markdown.

**Method:** Start with the prompt (without reading the solution), identify the first applicable cue, follow the Mermaid branch, and solve. The concept links in each cue table point to existing notes or intentionally unresolved Obsidian notes for future creation. **Nothing is marked complete until an independent attempt is reported.**

| Question | Focus | Status |
|---|---|---|
| [[#Problem 1 — One- vs two-sided t tests\|1]] | One- vs two-sided t tests | ☐ Not assessed |
| [[#Problem 2 — Two-sided t test from raw sums\|2]] | Two-sided t test from raw sums | ☐ Not assessed |
| [[#Problem 3 — Pooled two-sample t test for two drugs\|3]] | Pooled two-sample t test for two drugs | ☐ Not assessed |

---

## Problem 1 — One- vs two-sided t tests

### Mathematical restatement

Nine normal observations with unknown $\mu,\sigma^2$ give $\bar X=22$, $\sum_i(X_i-\bar X)^2=72$. At 5% significance, test (a) $H_0:\mu\le20$ versus $H_1:\mu>20$ and (b) $H_0:\mu=20$ versus $H_1:\mu\ne20$.

### Worked solution

**S1 — Estimate sample standard deviation.** $n=9$, $s^2=72/(9-1)=9$, so $s=3$, $\mathrm{SE}=s/\sqrt9=1$. The denominator is **n-1** for the unbiased sample variance entering a t-test.

**S2 — Calculate t with correct df.** $t=(22-20)/(3/\sqrt9)=2$, with $\nu=n-1=8$ degrees of freedom.

**S3 — Perform both hypothesis tests.** (a) Upper-tail $p=P(t_8\ge2)\approx0.04026<0.05$: **reject $H_0$**. (b) Two-sided $p=2P(t_8\ge2)\approx0.08052>0.05$: **do not reject**. The statistic is identical; alternative changes the tail calculation.

### Mermaid decision route

~~~mermaid
flowchart TD
  A["P1: One- vs two-sided t tests"] --> B{"Is population variance unknown?"}
  B -->|"Yes"| N0["S1: Estimate sample standard deviation"]
  B -->|"Unclear"| R["Review cue: do not treat one-tailed p as two-tailed"]
  R --> N0
  N0 --> N1["S2: Calculate t with correct df"]
  N1 --> N2["S3: Perform both hypothesis tests"]
  N2 --> Z["Check result and assumptions"]
  style R stroke:#777,stroke-dasharray:4 4
~~~

### Prerequisite and cue trace

| Step | General concept links | Recognition cue | Required move |
|---|---|---|---|
| S1 | [[Sample Mean and Sample Variance]]; [[Unbiased Estimator of the Variance]] | Sum squared deviations given | Divide by n-1 to obtain s² |
| S2 | [[t Distribution]]; [[Degrees of Freedom]] | Unknown sigma in Normal mean test | Use student t with n-1 df |
| S3 | [[Hypothesis Testing]]; [[p-value]] | Same data, different alternatives | One-sided vs two-sided p-value |

**Answer checkpoint:** t=2, df=8; reject a, not b.

**Failure-trace hook:** None observed yet. On an actual attempt, mark the *first* broken S-step, the exact general prerequisite skill, the cue missed, and the student's complete unedited words in the embedded log. Do not infer an FSRS rep from reading the walkthrough.

**Next task:** [[#Problem 2 — Two-sided t test from raw sums|Problem 2]].

---

## Problem 2 — Two-sided t test from raw sums

### Mathematical restatement

Eight normal observations with unknown mean and variance: $\sum_iX_i=11.2$, $\sum_iX_i^2=43.7$. Test $H_0:\mu=0$ versus $H_1:\mu\ne0$ at significance 0.10.

### Worked solution

**S1 — Recover the sample mean.** $\bar X=11.2/8=1.4$.

**S2 — Recover corrected sample variance.** $\sum_i(X_i-\bar X)^2=\sum X_i^2-(\sum X_i)^2/n=43.7-11.2^2/8=28.02$. Hence $s^2=28.02/7\approx4.00286$.

**S3 — Construct the t statistic.** $t=(1.4-0)/\sqrt{s^2/8}\approx1.97919$ with 7 df.

**S4 — Compare with the two-sided 10% threshold.** $p=2P(t_7\ge1.97919)\approx0.08829<0.10$. Therefore $\boxed{\text{reject }H_0}$ at 10%. Equivalently $|t|>t_{7,0.95}\approx1.89458$.

### Mermaid decision route

~~~mermaid
flowchart TD
  A["P2: Two-sided t test from raw sums"] --> B{"Can you compute residual SS from the two raw sums?"}
  B -->|"Yes"| N0["S1: Recover the sample mean"]
  B -->|"Unclear"| R["Review cue: do not divide sum Xi² directly by n-1 without centering"]
  R --> N0
  N0 --> N1["S2: Recover corrected sample variance"]
  N1 --> N2["S3: Construct the t statistic"]
  N2 --> N3["S4: Compare with the two-sided 10% threshold"]
  N3 --> Z["Check result and assumptions"]
  style R stroke:#777,stroke-dasharray:4 4
~~~

### Prerequisite and cue trace

| Step | General concept links | Recognition cue | Required move |
|---|---|---|---|
| S1 | [[Sample Mean]] | Only sum Xi given | Divide by n |
| S2 | [[Sample Variance]]; [[Equivalent equations]] | Sum Xi² given instead of residual sum | Use SS=sum x²-(sum x)²/n |
| S3 | [[t Distribution]]; [[Degrees of Freedom]] | Unknown population variance | Studentize sample mean with df7 |
| S4 | [[p-value]]; [[Significance Level]] | Two-sided alpha=.10 | Use both tails or t0.95 cutoff |

**Answer checkpoint:** reject; p about .0883.

**Failure-trace hook:** None observed yet. On an actual attempt, mark the *first* broken S-step, the exact general prerequisite skill, the cue missed, and the student's complete unedited words in the embedded log. Do not infer an FSRS rep from reading the walkthrough.

**Next task:** [[#Problem 3 — Pooled two-sample t test for two drugs|Problem 3]].

---

## Problem 3 — Pooled two-sample t test for two drugs

### Mathematical restatement

Independent Normal samples of concentrations: A ($n_A=8$): $1.23,1.42,1.41,1.62,1.55,1.51,1.60,1.76$; B ($n_B=6$): $1.76,1.41,1.87,1.49,1.67,1.81$. Assume **common unknown variance**. Test $H_0:\mu_A\ge\mu_B$ versus $H_1:\mu_B>\mu_A$ at 10%.

### Worked solution

**S1 — Compute separate sample summaries.** $\bar X_A=1.5125$, $\bar X_B\approx1.66833$, $s_A^2\approx0.0258214$, $s_B^2\approx0.0335367$. The hypothesized direction is **B minus A**, not A minus B.

**S2 — Pool variances with df weights.** $s_p^2=\frac{(n_A-1)s_A^2+(n_B-1)s_B^2}{n_A+n_B-2}=\frac{7s_A^2+5s_B^2}{12}\approx0.0290361$. Degrees of freedom $8+6-2=12$.

**S3 — Construct pooled standard-error t.** $t=\frac{\bar X_B-\bar X_A}{s_p\sqrt{1/8+1/6}}\approx\boxed{1.69335}$, using $s_p\approx0.17040$.

**S4 — Apply upper-tail test at .10.** $p=P(t_{12}\ge1.69335)\approx0.05808<0.10$. Thus $\boxed{\text{reject }H_0}$ in favor of greater population mean concentration for drug B. This is a statistical conclusion conditional on the model, not a clinical benefit claim.

### Mermaid decision route

~~~mermaid
flowchart TD
  A["P3: Pooled two-sample t test for two drugs"] --> B{"Does the problem assume common variance?"}
  B -->|"Yes"| N0["S1: Compute separate sample summaries"]
  B -->|"Unclear"| R["Review cue: do not use unequal-variance Welch formula here"]
  R --> N0
  N0 --> N1["S2: Pool variances with df weights"]
  N1 --> N2["S3: Construct pooled standard-error t"]
  N2 --> N3["S4: Apply upper-tail test at .10"]
  N3 --> Z["Check result and assumptions"]
  style R stroke:#777,stroke-dasharray:4 4
~~~

### Prerequisite and cue trace

| Step | General concept links | Recognition cue | Required move |
|---|---|---|---|
| S1 | [[Sample Mean and Sample Variance]]; [[Normal Distribution]] | Two independent groups with separate data | Compute means and unbiased variances |
| S2 | [[Pooled Variance]]; [[Degrees of Freedom]] | Common unknown variance is explicit | Pool with (nA-1), (nB-1) weights |
| S3 | [[Two-Sample t Test]]; [[t Distribution]] | Compare difference in means | Use pooled SE and df=nA+nB-2 |
| S4 | [[Null Hypothesis]]; [[p-value]] | Alternative B mean greater than A | Upper-tail p-value and alpha=.10 |

**Answer checkpoint:** t~1.693, p~.058, reject at .10.

**Failure-trace hook:** None observed yet. On an actual attempt, mark the *first* broken S-step, the exact general prerequisite skill, the cue missed, and the student's complete unedited words in the embedded log. Do not infer an FSRS rep from reading the walkthrough.

**Next task:** [[Discussions Stats132|All discussions]].

---

## Shared concept dependency map

~~~mermaid
flowchart LR
  C1["Sample Mean and Sample Variance"] --> Q1["Problem 1: One- vs two-sided t tests"]
  C2["Sample Mean"] --> Q2["Problem 2: Two-sided t test from raw sums"]
  C3["Sample Mean and Sample Variance"] --> Q3["Problem 3: Pooled two-sample t test for two drugs"]
~~~

## Dated review and failure log — CSV inside this note

**No attempts recorded.** Add rows below only for actual study attempts, using actual dates and exact verbatim student wording. This Markdown log is not automatically read by FSRS.

```csv
date,problem,step,node,outcome,ledger_ref,ledger_status,said,agent_note
```

**Retention contract:** Live attempt data originates in the vault's `System/reps.csv` via `brain study log`; `System/rep-words.jsonl` joins the user's *unmodified* `said` to the returned attempt `ref`. The model writes `System/index/memory.json`, which is output and should not be edited. A new concept link is **not** evidence of failure. A local handwritten CSV row here does **not** update the memory curve.

**Review target:** 3 problems remain unassessed in this guide.
