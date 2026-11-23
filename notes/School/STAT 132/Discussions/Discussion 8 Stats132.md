---
aliases:
  - "Discussion 8 Stats132"
  - "STAT 132 Discussion 8"
  - "Stats132 Disc 8"
type: study
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
item_type: discussion-worked-trace
discussion: 8
worksheet_year: 2025
status: not-started
problems: 5
completed_problems: []
source: "STAT132/files/homework/STAT132 Discussion 08 (W25 worksheet).pdf"
retention_input: "System/reps.csv"
retention_words: "System/rep-words.jsonl"
retention_output: "System/index/memory.json"
created: 2026-11-22
---
# Discussion 8 Stats132

**Source:** [Discussion 8 W25 worksheet](https://github.com/immcnotthere/School/blob/main/STAT132/files/homework/STAT132%20Discussion%2008%20%28W25%20worksheet%29.pdf). Prompts preserve the source's mathematical task, but are typeset afresh for readable Obsidian Markdown.

**Method:** Start with the prompt (without reading the solution), identify the first applicable cue, follow the Mermaid branch, and solve. The concept links in each cue table point to existing notes or intentionally unresolved Obsidian notes for future creation. **Nothing is marked complete until an independent attempt is reported.**

| Question | Focus | Status |
|---|---|---|
| [[#Problem 1 — Power and level of exponential threshold test|1]] | Power and level of exponential threshold test | ☐ Not assessed |
| [[#Problem 2 — Power and level of Uniform-maximum test|2]] | Power and level of Uniform-maximum test | ☐ Not assessed |
| [[#Problem 3 — Two-sided Normal test rejection threshold|3]] | Two-sided Normal test rejection threshold | ☐ Not assessed |
| [[#Problem 4 — Power increasing in Normal mean and 5% cutoff|4]] | Power increasing in Normal mean and 5% cutoff | ☐ Not assessed |
| [[#Problem 5 — Neyman–Pearson test for two exponential rates|5]] | Neyman–Pearson test for two exponential rates | ☐ Not assessed |

---

## Problem 1 — Power and level of exponential threshold test

### Mathematical restatement

One $X$ has exponential **rate** $\beta>0$. Test $H_0:\beta\ge1$ versus $H_1:\beta<1$ by rejecting when $X\ge1$. Find (a) power function and (b) test level.

### Worked solution

**S1 — Write power as rejection probability.** $\pi(\beta)=P_\beta(X\ge1)$. For exponential rate, $P_\beta(X\ge t)=e^{-\beta t}$.

**S2 — Evaluate at threshold.** $\boxed{\pi(\beta)=e^{-\beta}}$. Power **decreases** as rate increases, so it is higher in the alternative $\beta<1$.

**S3 — Maximize rejection probability under H0.** $\text{level}=\sup_{\beta\ge1}e^{-\beta}=e^{-1}\approx\boxed{0.3679}$. Take supremum at the boundary $\beta=1$, not over the alternative.

### Mermaid decision route

~~~mermaid
flowchart TD
  A["P1: Power and level of exponential threshold test"] --> B{"Does beta denote the rate (so the tail is exp(-beta x))?"}
  B -->|"Yes"| N0["S1: Write power as rejection probability"]
  B -->|"Unclear"| R["Review cue: do not compute power at a single beta then call it the function"]
  R --> N0
  N0 --> N1["S2: Evaluate at threshold"]
  N1 --> N2["S3: Maximize rejection probability under H0"]
  N2 --> Z["Check result and assumptions"]
  style R stroke:#777,stroke-dasharray:4 4
~~~

### Prerequisite and cue trace

| Step | General concept links | Recognition cue | Required move |
|---|---|---|---|
| S1 | [[Exponential Distribution]]; [[Power Function]] | Reject if X>=1 | Compute exponential survival probability |
| S2 | [[Power Function]]; [[Monotonicity]] | Unknown parameter beta | Write probability as function of beta |
| S3 | [[Significance Level]]; [[Null Hypothesis]] | Find level of composite H0 | Take supremum over beta>=1 |

**Answer checkpoint:** power e^{-beta}, level e^{-1}.

**Failure-trace hook:** None observed yet. On an actual attempt, mark the *first* broken S-step, the exact general prerequisite skill, the cue missed, and the student's complete unedited words in the embedded log. Do not infer an FSRS rep from reading the walkthrough.

---

## Problem 2 — Power and level of Uniform-maximum test

### Mathematical restatement

$X_i$ iid Uniform$[0,\theta]$; $Y=\max X_i$. Test $H_0:\theta\ge2$ versus $H_1:\theta<2$ by rejecting when $Y\le1.5$. Find power and level.

### Worked solution

**S1 — Write CDF of maximum.** For $\theta>0$, $P_\theta(Y\le y)=1$ if $y\ge\theta$, and $(y/\theta)^n$ if $0\le y<\theta$.

**S2 — Evaluate rejection probability piecewise.** $\boxed{\pi(\theta)=\begin{cases}1,&0<\theta\le1.5,\\(1.5/\theta)^n,&\theta>1.5.\end{cases}}$ Parameter-dependent support requires both cases.

**S3 — Take supremum over the null region.** On $\theta\ge2$, $(1.5/\theta)^n$ decreases with $\theta$. Maximum occurs at $\theta=2$, giving $\boxed{\alpha_{\rm test}=(1.5/2)^n=(0.75)^n}$.

### Mermaid decision route

~~~mermaid
flowchart TD
  A["P2: Power and level of Uniform-maximum test"] --> B{"Does rejection depend on parameter-sensitive support?"}
  B -->|"Yes"| N0["S1: Write CDF of maximum"]
  B -->|"Unclear"| R["Review cue: don't apply (1.5/theta)^n when theta<1.5"]
  R --> N0
  N0 --> N1["S2: Evaluate rejection probability piecewise"]
  N1 --> N2["S3: Take supremum over the null region"]
  N2 --> Z["Check result and assumptions"]
  style R stroke:#777,stroke-dasharray:4 4
~~~

### Prerequisite and cue trace

| Step | General concept links | Recognition cue | Required move |
|---|---|---|---|
| S1 | [[Distribution of the Sample Maximum]]; [[Uniform Distribution (Continuous)]] | Rejection uses maximum Y | Use Fmax=F^n |
| S2 | [[Support (Probability)]]; [[Piecewise functions]] | Theta could be smaller than threshold | Distinguish theta<=1.5 and >1.5 |
| S3 | [[Power Function]]; [[Significance Level]] | Composite H0 theta>=2 | Maximize power over H0 |

**Answer checkpoint:** piecewise power and level .75^n.

**Failure-trace hook:** None observed yet. On an actual attempt, mark the *first* broken S-step, the exact general prerequisite skill, the cue missed, and the student's complete unedited words in the embedded log. Do not infer an FSRS rep from reading the walkthrough.

---

## Problem 3 — Two-sided Normal test rejection threshold

### Mathematical restatement

$X_1,\ldots,X_{25}$ iid $N(\mu,1)$. Test $H_0:\mu=\mu_0$ versus $H_1:\mu\ne\mu_0$ by rejecting if $|\bar X-\mu_0|\ge c$. Choose $c$ for level $\alpha=0.05$.

### Worked solution

**S1 — Standardize under the null.** $Z=\sqrt{25}(\bar X-\mu_0)=5(\bar X-\mu_0)\sim N(0,1)$ under $H_0$.

**S2 — Translate the two-sided region.** $P_{\mu_0}(|\bar X-\mu_0|\ge c)=P(|Z|\ge5c)=0.05$. Each tail is 0.025.

**S3 — Set critical value.** $5c=z_{0.975}=1.959964$; hence $\boxed{c=z_{0.975}/5\approx0.391993\approx0.392}$.

### Mermaid decision route

~~~mermaid
flowchart TD
  A["P3: Two-sided Normal test rejection threshold"] --> B{"Is the alternative two-sided?"}
  B -->|"Yes"| N0["S1: Standardize under the null"]
  B -->|"Unclear"| R["Review cue: avoid one-sided z0.95"]
  R --> N0
  N0 --> N1["S2: Translate the two-sided region"]
  N1 --> N2["S3: Set critical value"]
  N2 --> Z["Check result and assumptions"]
  style R stroke:#777,stroke-dasharray:4 4
~~~

### Prerequisite and cue trace

| Step | General concept links | Recognition cue | Required move |
|---|---|---|---|
| S1 | [[Standard Normal Distribution]]; [[Sample Mean]] | Known normal variance 1 | Standardize with sqrt25 |
| S2 | [[Null Hypothesis]]; [[Significance Level]] | Two-sided abs value | Split alpha into two tails |
| S3 | [[Quantile Function]]; [[Standard Normal CDF (Φ)]] | Critical c in original sample-mean units | Divide z0.975 by 5 |

**Answer checkpoint:** c approx 0.392.

**Failure-trace hook:** None observed yet. On an actual attempt, mark the *first* broken S-step, the exact general prerequisite skill, the cue missed, and the student's complete unedited words in the embedded log. Do not infer an FSRS rep from reading the walkthrough.

---

## Problem 4 — Power increasing in Normal mean and 5% cutoff

### Mathematical restatement

Iid $N(\mu,1)$ sample. Test $H_0:\mu\le\mu_0$ versus $H_1:\mu>\mu_0$; reject if $\sqrt n(\bar X-\mu_0)\ge c$. (a) Show power increases in $\mu$. (b) Choose $c$ for level 0.05.

### Worked solution

**S1 — Express statistic under arbitrary mean.** $Z=\sqrt n(\bar X-\mu)\sim N(0,1)$. Rejection means $Z\ge c-\sqrt n(\mu-\mu_0)$.

**S2 — Derive power and monotonicity.** $\pi(\mu)=1-\Phi(c-\sqrt n(\mu-\mu_0))$. Increasing $\mu$ decreases the $\Phi$ argument, so **power rises**; derivative $\pi'(\mu)=\sqrt n\,\phi(c-\sqrt n(\mu-\mu_0))>0$.

**S3 — Calibrate at least-favorable null boundary.** Since power rises, $\sup_{\mu\le\mu_0}\pi(\mu)=\pi(\mu_0)=1-\Phi(c)$. Set equal to 0.05: $\boxed{c=z_{0.95}\approx1.64485}$.

### Mermaid decision route

~~~mermaid
flowchart TD
  A["P4: Power increasing in Normal mean and 5% cutoff"] --> B{"Does increasing mu shift the standardized statistic rightward?"}
  B -->|"Yes"| N0["S1: Express statistic under arbitrary mean"]
  B -->|"Unclear"| R["Review cue: not z0.975 since test is one-sided"]
  R --> N0
  N0 --> N1["S2: Derive power and monotonicity"]
  N1 --> N2["S3: Calibrate at least-favorable null boundary"]
  N2 --> Z["Check result and assumptions"]
  style R stroke:#777,stroke-dasharray:4 4
~~~

### Prerequisite and cue trace

| Step | General concept links | Recognition cue | Required move |
|---|---|---|---|
| S1 | [[Sample Mean]]; [[Normal Distribution]] | Statistic centers on mu0 | Rewrite under true mu |
| S2 | [[Power Function]]; [[Standard Normal CDF (Φ)]] | Prove increasing power | Express tail and differentiate/monotonicity |
| S3 | [[Significance Level]]; [[Null Hypothesis]] | Composite one-sided null | Take supremum at mu0 |

**Answer checkpoint:** power increasing and c=1.645.

**Failure-trace hook:** None observed yet. On an actual attempt, mark the *first* broken S-step, the exact general prerequisite skill, the cue missed, and the student's complete unedited words in the embedded log. Do not infer an FSRS rep from reading the walkthrough.

---

## Problem 5 — Neyman–Pearson test for two exponential rates

### Mathematical restatement

$X_1,\ldots,X_n$ iid exponential with **rate** $\theta$, where $0<\theta_0<\theta_1$ are the only two possibilities. Find most-powerful level-$\alpha_0$ test of $H_0:\theta=\theta_0$ versus $H_1:\theta=\theta_1$.

### Worked solution

**S1 — Form simple-hypothesis likelihood ratio.** With $T=\sum_iX_i$, $\frac{L(\theta_1)}{L(\theta_0)}=(\theta_1/\theta_0)^n e^{-(\theta_1-\theta_0)T}$.

**S2 — Determine rejection direction.** Because $\theta_1>\theta_0$, the likelihood ratio is **decreasing in $T$**. Neyman–Pearson: reject $H_0$ for **small total observed time** $T\le c$.

**S3 — Choose cutoff from null probability.** Under $H_0$, $2\theta_0 T\sim\chi^2_{2n}$. Choose $P_{\theta_0}(T\le c)=\alpha_0$, giving $\boxed{\text{Reject if }2\theta_0\sum_iX_i\le\chi^2_{2n,\alpha_0}}$. Equivalently $c=\chi^2_{2n,\alpha_0}/(2\theta_0)$.

### Mermaid decision route

~~~mermaid
flowchart TD
  A["P5: Neyman–Pearson test for two exponential rates"] --> B{"Is theta a rate so larger theta means shorter durations?"}
  B -->|"Yes"| N0["S1: Form simple-hypothesis likelihood ratio"]
  B -->|"Unclear"| R["Review cue: if source uses mean-scale instead, direction reverses; check rate convention"]
  R --> N0
  N0 --> N1["S2: Determine rejection direction"]
  N1 --> N2["S3: Choose cutoff from null probability"]
  N2 --> Z["Check result and assumptions"]
  style R stroke:#777,stroke-dasharray:4 4
~~~

### Prerequisite and cue trace

| Step | General concept links | Recognition cue | Required move |
|---|---|---|---|
| S1 | [[Likelihood Ratio Test]]; [[Exponential Distribution]] | Both hypotheses give point parameter values | Write LR and cancel constants |
| S2 | [[Neyman-Pearson Lemma]]; [[Monotonicity]] | Alternative rate larger | Reject for small sample sum |
| S3 | [[Chi-Square Distribution]]; [[Significance Level]] | Enforce exact level alpha0 under H0 | Use lower-tail chi² quantile with 2n df |

**Answer checkpoint:** reject for sum Xi sufficiently small.

**Failure-trace hook:** None observed yet. On an actual attempt, mark the *first* broken S-step, the exact general prerequisite skill, the cue missed, and the student's complete unedited words in the embedded log. Do not infer an FSRS rep from reading the walkthrough.

---

## Shared concept dependency map

~~~mermaid
flowchart LR
  C1["Exponential Distribution"] --> Q1["Problem 1: Power and level of exponential threshold test"]
  C2["Distribution of the Sample Maximum"] --> Q2["Problem 2: Power and level of Uniform-maximum test"]
  C3["Standard Normal Distribution"] --> Q3["Problem 3: Two-sided Normal test rejection threshold"]
  C4["Sample Mean"] --> Q4["Problem 4: Power increasing in Normal mean and 5% cutoff"]
  C5["Likelihood Ratio Test"] --> Q5["Problem 5: Neyman–Pearson test for two exponential rates"]
~~~

## Dated review and failure log — CSV inside this note

**No attempts recorded.** Add rows below only for actual study attempts, using actual dates and exact verbatim student wording. This Markdown log is not automatically read by FSRS.

```csv
date,problem,step,node,outcome,ledger_ref,ledger_status,said,agent_note
```

**Retention contract:** Live attempt data originates in the vault's `System/reps.csv` via `brain study log`; `System/rep-words.jsonl` joins the user's *unmodified* `said` to the returned attempt `ref`. The model writes `System/index/memory.json`, which is output and should not be edited. A new concept link is **not** evidence of failure. A local handwritten CSV row here does **not** update the memory curve.

**Review target:** 5 problems remain unassessed in this guide.
