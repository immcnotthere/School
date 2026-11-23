---
aliases:
  - "Discussion 4 Stats132"
  - "STAT 132 Discussion 4"
  - "Stats132 Disc 4"
type: study
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
item_type: discussion-worked-trace
discussion: 4
worksheet_year: 2025
status: not-started
problems: 5
completed_problems: []
source: "STAT132/files/homework/STAT132 Discussion 04 (W25 worksheet).pdf"
retention_input: "System/reps.csv"
retention_words: "System/rep-words.jsonl"
retention_output: "System/index/memory.json"
created: 2026-11-22
---
# Discussion 4 Stats132

**Original:** [Discussion 4 W25 worksheet](https://github.com/immcnotthere/School/blob/main/STAT132/files/homework/STAT132%20Discussion%2004%20%28W25%20worksheet%29.pdf). Rephrased mathematical prompts and solutions below are anchored to this worksheet. The worksheet is from Winter 2025; the study work is in 2026.

**How to study:** Hide each worked solution, attempt unaided, and find the *first* Mermaid step that stalls. The cue table points to reusable Obsidian concept notes; unresolved `[[wikilinks]]` are suggestions for missing notes. All 5 problems start **not assessed**. Reading solutions is not a completed attempt.

| Problem | Topic | Status |
|---|---|---|
| [[#Problem 1 — Uniform maximum sample-size guarantee|1]] | Uniform maximum sample-size guarantee | ☐ Not assessed |
| [[#Problem 2 — Normal mean mean-square precision|2]] | Normal mean mean-square precision | ☐ Not assessed |
| [[#Problem 3 — Normal mean 95% probability precision|3]] | Normal mean 95% probability precision | ☐ Not assessed |
| [[#Problem 4 — Sampling CDF of exponential rate MLE|4]] | Sampling CDF of exponential rate MLE | ☐ Not assessed |
| [[#Problem 5 — Bernoulli mean uniform MSE bound|5]] | Bernoulli mean uniform MSE bound | ☐ Not assessed |

---
## Problem 1 — Uniform maximum sample-size guarantee

### Mathematical restatement

$X_i$ iid Uniform$(0,\theta)$, $\theta>0$. Find smallest $n$ such that $P(|X_{(n)}-\theta|\le0.1\theta)\ge0.95$, where $X_{(n)}=\max X_i$.

### Worked solution

**S1 — Simplify the event using support.** Since $X_{(n)}\le\theta$, $|X_{(n)}-\theta|\le0.1\theta$ is just $X_{(n)}\ge0.9\theta$.

**S2 — Use the maximum CDF.** $P(X_{(n)}\le y)=P(X_1\le y,\ldots,X_n\le y)=(y/\theta)^n$ for $0\le y\le\theta$. Thus $P(X_{(n)}\ge0.9\theta)=1-0.9^n$.

**S3 — Solve the log inequality.** $1-0.9^n\ge0.95$ gives $0.9^n\le0.05$ and $n\ge\log(0.05)/\log(0.9)\approx28.433$. Therefore $\boxed{n_{\min}=29}$. The log denominator is negative, so dividing reverses the inequality.

### Mermaid decision route

~~~mermaid
flowchart TD
  A["P1: Uniform maximum sample-size guarantee"] --> B{"Is the estimator the sample maximum?"}
  B -->|"Yes"| N0["S1: Simplify the event using support"]
  B -->|"Not sure"| R["Review cue: use order statistics rather than CLT"]
  R --> N0
  N0 --> N1["S2: Use the maximum CDF"]
  N1 --> N2["S3: Solve the log inequality"]
  N2 --> Z["Deliver answer; check support and assumptions"]
  style R stroke:#777,stroke-dasharray:4 4
~~~

### Prerequisite and cue trace

| Step | General concept links | Recognition cue | Required move |
|---|---|---|---|
| S1 | [[Uniform Distribution (Continuous)]]; [[Support (Probability)]] | Maximum can't exceed theta | Remove absolute value using support |
| S2 | [[Distribution of the Sample Maximum]]; [[Independence of Random Variables]] | At least one high observation | Use Fmax(x)=F(x)^n |
| S3 | [[Natural logarithms]]; [[Inequalities]] | Solve probability threshold | Watch direction when dividing by negative log |

**When to stop:** minimum n is 29.

**Attempt record:** Not assessed; no learner failure or time has been inferred. At the next actual attempt record: `problem=P1`, the first stalled `step=S#`, the general prerequisite `node`, the observed outcome, and the learner's *exact original words* in quotes. Distinguish a cue-recognition miss from a calculation miss.

---

## Problem 2 — Normal mean mean-square precision

### Mathematical restatement

$X_i$ iid $N(\mu,4)$ with unknown mean. Find minimum $n$ with $E[|\bar X-\mu|^2]\le0.1$.

### Worked solution

**S1 — Recognize squared error as variance.** $\bar X$ is unbiased: $E[\bar X]=\mu$. Therefore $E[(\bar X-\mu)^2]=\operatorname{Var}(\bar X)$.

**S2 — Use sample-mean variance.** $\operatorname{Var}(\bar X)=\sigma^2/n=4/n$. The normality assumption is stronger than necessary for this equality.

**S3 — Solve the bound.** $4/n\le0.1$ means $n\ge40$. Hence $\boxed{n_{\min}=40}$.

### Mermaid decision route

~~~mermaid
flowchart TD
  A["P2: Normal mean mean-square precision"] --> B{"Is the mean unbiased?"}
  B -->|"Yes"| N0["S1: Recognize squared error as variance"]
  B -->|"Not sure"| R["Review cue: do not introduce a normal quantile for an expectation"]
  R --> N0
  N0 --> N1["S2: Use sample-mean variance"]
  N1 --> N2["S3: Solve the bound"]
  N2 --> Z["Deliver answer; check support and assumptions"]
  style R stroke:#777,stroke-dasharray:4 4
~~~

### Prerequisite and cue trace

| Step | General concept links | Recognition cue | Required move |
|---|---|---|---|
| S1 | [[Mean Squared Error (MSE)]]; [[Unbiased Estimator]] | Expectation of squared difference | Recognize bias² plus variance |
| S2 | [[Variance of the Sample Mean]] | Independent observations | Use sigma²/n |
| S3 | [[Equivalent equations]] | Bound on mean squared error | Rearrange 4/n≤0.1 |

**When to stop:** minimum n is 40.

**Attempt record:** Not assessed; no learner failure or time has been inferred. At the next actual attempt record: `problem=P2`, the first stalled `step=S#`, the general prerequisite `node`, the observed outcome, and the learner's *exact original words* in quotes. Distinguish a cue-recognition miss from a calculation miss.

---

## Problem 3 — Normal mean 95% probability precision

### Mathematical restatement

$X_i$ iid $N(\mu,4)$. Find minimum $n$ with $P(|\bar X-\mu|\le0.1)\ge0.95$.

### Worked solution

**S1 — Standardize the sample mean.** $Z=\sqrt n(\bar X-\mu)/2\sim N(0,1)$. Thus $P(|\bar X-\mu|\le0.1)=P(|Z|\le0.05\sqrt n)$.

**S2 — Use a two-sided standard-normal quantile.** Requirement is $0.05\sqrt n\ge z_{0.975}\approx1.959964$, since $P(|Z|\le z_{0.975})=0.95$.

**S3 — Solve and round sample size up.** $n\ge(1.959964/0.05)^2\approx1536.584$, so $\boxed{n_{\min}=1537}$. Distinguish this **probability guarantee** from Q2's **mean-squared-error** guarantee.

### Mermaid decision route

~~~mermaid
flowchart TD
  A["P3: Normal mean 95% probability precision"] --> B{"Does the question constrain a probability rather than E(error²)?"}
  B -->|"Yes"| N0["S1: Standardize the sample mean"]
  B -->|"Not sure"| R["Review cue: avoid reusing Q2's n=40"]
  R --> N0
  N0 --> N1["S2: Use a two-sided standard-normal quantile"]
  N1 --> N2["S3: Solve and round sample size up"]
  N2 --> Z["Deliver answer; check support and assumptions"]
  style R stroke:#777,stroke-dasharray:4 4
~~~

### Prerequisite and cue trace

| Step | General concept links | Recognition cue | Required move |
|---|---|---|---|
| S1 | [[Sample Mean]]; [[Standard Normal Distribution]] | Absolute sample-mean error | Standardize by 2/sqrt n |
| S2 | [[Standard Normal CDF (Φ)]]; [[Quantile Function]] | Two-sided 95 percent interval | Use z0.975, not z0.95 |
| S3 | [[Inequalities]] | Choose n integer | Square and take ceiling |

**When to stop:** minimum n is 1537.

**Attempt record:** Not assessed; no learner failure or time has been inferred. At the next actual attempt record: `problem=P3`, the first stalled `step=S#`, the general prerequisite `node`, the observed outcome, and the learner's *exact original words* in quotes. Distinguish a cue-recognition miss from a calculation miss.

---

## Problem 4 — Sampling CDF of exponential rate MLE

### Mathematical restatement

For $X_i$ iid exponential with **rate** $\lambda>0$, find the CDF of $\hat\lambda_{\rm MLE}$. Here the rate convention is $f(x|\lambda)=\lambda e^{-\lambda x}$; check class notation if parameterized by the mean instead.

### Worked solution

**S1 — Derive the MLE.** $L(\lambda)=\lambda^n e^{-\lambda T}$ with $T=\sum_i X_i$. Differentiate $\ell=n\log\lambda-\lambda T$ to obtain $\hat\lambda=n/T$.

**S2 — Identify the distribution of the sum.** $T\sim\operatorname{Gamma}(n,\lambda)$ in shape–rate notation, equivalently $2\lambda T\sim\chi^2_{2n}$.

**S3 — Transform the inequality carefully.** For $t>0$, $F_{\hat\lambda}(t)=P(n/T\le t)=P(T\ge n/t)$. Because $T$ is positive, the direction switches upon inversion.

**S4 — Write the exact CDF.** With integer Gamma shape $n$, $\boxed{F_{\hat\lambda}(t)=e^{-n\lambda/t}\sum_{k=0}^{n-1}\frac{(n\lambda/t)^k}{k!}}$ for $t>0$, and $0$ for $t\le0$. Equivalently $1-F_{\chi^2_{2n}}(2n\lambda/t)$.

### Mermaid decision route

~~~mermaid
flowchart TD
  A["P4: Sampling CDF of exponential rate MLE"] --> B{"Is theta the exponential rate rather than mean?"}
  B -->|"Yes"| N0["S1: Derive the MLE"]
  B -->|"Not sure"| R["Review cue: do not forget positive support or inequality reversal"]
  R --> N0
  N0 --> N1["S2: Identify the distribution of the sum"]
  N1 --> N2["S3: Transform the inequality carefully"]
  N2 --> N3["S4: Write the exact CDF"]
  N3 --> Z["Deliver answer; check support and assumptions"]
  style R stroke:#777,stroke-dasharray:4 4
~~~

### Prerequisite and cue trace

| Step | General concept links | Recognition cue | Required move |
|---|---|---|---|
| S1 | [[Maximum Likelihood Estimation]]; [[Exponential Distribution]] | Find CDF of MLE | First get the estimator as a function of data |
| S2 | [[Gamma Distribution]]; [[Chi-Square Distribution]] | Sum of independent exponentials | Recognize sum as Gamma |
| S3 | [[Transformation of a Continuous Random Variable (CDF Method)]]; [[Inequalities]] | Estimator is a reciprocal of a positive sum | Invert event with inequality direction |
| S4 | [[Gamma Distribution]]; [[Cumulative Distribution Function]] | CDF of rate MLE | Use upper Gamma tail |

**When to stop:** CDF is the upper Gamma tail evaluated at n/t.

**Attempt record:** Not assessed; no learner failure or time has been inferred. At the next actual attempt record: `problem=P4`, the first stalled `step=S#`, the general prerequisite `node`, the observed outcome, and the learner's *exact original words* in quotes. Distinguish a cue-recognition miss from a calculation miss.

---

## Problem 5 — Bernoulli mean uniform MSE bound

### Mathematical restatement

$X_i\sim\operatorname{Bernoulli}(p)$ iid with $p$ unknown. Find a sample size guaranteeing $E[(\bar X-p)^2]\le0.01$ **without knowing $p$**.

### Worked solution

**S1 — Use unbiasedness.** $E[\bar X]=p$, so $E[(\bar X-p)^2]=\operatorname{Var}(\bar X)=p(1-p)/n$.

**S2 — Find the worst parameter value.** For $0\le p\le1$, $p(1-p)\le1/4$, with equality at $p=1/2$. This maximizes risk over unknown $p$.

**S3 — Solve uniform guarantee.** Require $(1/4)/n\le0.01$, or $n\ge25$. So $\boxed{n_{\min}=25}$ for **all** $p$.

### Mermaid decision route

~~~mermaid
flowchart TD
  A["P5: Bernoulli mean uniform MSE bound"] --> B{"Must the bound hold regardless of p?"}
  B -->|"Yes"| N0["S1: Use unbiasedness"]
  B -->|"Not sure"| R["Review cue: do not insert an invented p"]
  R --> N0
  N0 --> N1["S2: Find the worst parameter value"]
  N1 --> N2["S3: Solve uniform guarantee"]
  N2 --> Z["Deliver answer; check support and assumptions"]
  style R stroke:#777,stroke-dasharray:4 4
~~~

### Prerequisite and cue trace

| Step | General concept links | Recognition cue | Required move |
|---|---|---|---|
| S1 | [[Bernoulli Distribution]]; [[Variance of the Sample Mean]] | Unknown success probability | Use Var(Xbar)=p(1-p)/n |
| S2 | [[Quadratic functions]]; [[Maximum]] | Guarantee without knowing p | Bound p(1-p) by 1/4 |
| S3 | [[Inequalities]] | Uniform guarantee | Solve 1/(4n)≤0.01 |

**When to stop:** minimum n is 25.

**Attempt record:** Not assessed; no learner failure or time has been inferred. At the next actual attempt record: `problem=P5`, the first stalled `step=S#`, the general prerequisite `node`, the observed outcome, and the learner's *exact original words* in quotes. Distinguish a cue-recognition miss from a calculation miss.

---

## Shared concept map

~~~mermaid
flowchart LR
  A1["Uniform Distribution (Continuous)"] --> P1["P1: Uniform maximum sample-size guarantee"]
  A2["Mean Squared Error (MSE)"] --> P2["P2: Normal mean mean-square precision"]
  A3["Sample Mean"] --> P3["P3: Normal mean 95% probability precision"]
  A4["Maximum Likelihood Estimation"] --> P4["P4: Sampling CDF of exponential rate MLE"]
  A5["Bernoulli Distribution"] --> P5["P5: Bernoulli mean uniform MSE bound"]
~~~

## Dated attempt history (embedded CSV; intentionally empty)

The four-column concept/step trace used in the prerequisite tables is a study aid. The CSV below is a human-readable audit *inside this Markdown*, **not** `System/reps.csv` and not input to brain/FSRS until an actual attempt is logged through `brain study log`. No attempts have been observed in this note.

```csv
date,problem,step,node,outcome,ledger_ref,ledger_status,said,agent_note
```

When a real attempt occurs, preserve `said` **verbatim and in full**, with your agent's interpretation only in `agent_note`. Attach a real `ref` returned by brain; never manufacture timestamps, FSRS outcomes or copied attempts. `System/index/memory.json` is generated output and must not be hand-edited.

**Checkpoint:** 0/5 independently completed in this note; consult the student's separately maintained records for other progress.
