---
aliases:
  - "Discussion 5 Stats132"
  - "STAT 132 Discussion 5"
  - "Stats132 Disc 5"
type: study
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
item_type: discussion-worked-trace
discussion: 5
worksheet_year: 2025
status: not-started
problems: 5
completed_problems: []
source: "STAT132/files/homework/STAT132 Discussion 05 (W25 worksheet).pdf"
retention_input: "System/reps.csv"
retention_words: "System/rep-words.jsonl"
retention_output: "System/index/memory.json"
created: 2026-11-22
---
# Discussion 5 Stats132

[[Discussions Stats132|All discussions]] · [[Discussion 4 Stats132|Previous discussion]] · [[Discussion 6 Stats132|Next discussion]]

**Original:** [Discussion 5 W25 worksheet](https://github.com/immcnotthere/School/blob/main/STAT132/files/homework/STAT132%20Discussion%2005%20%28W25%20worksheet%29.pdf). Rephrased mathematical prompts and solutions below are anchored to this worksheet. The worksheet is from Winter 2025; the study work is in 2026.

**How to study:** Hide each worked solution, attempt unaided, and find the *first* Mermaid step that stalls. The cue table points to reusable Obsidian concept notes; unresolved `[[wikilinks]]` are suggestions for missing notes. All 5 problems start **not assessed**. Reading solutions is not a completed attempt.

| Problem | Topic | Status |
|---|---|---|
| [[#Problem 1 — Mode of chi-square distribution\|1]] | Mode of chi-square distribution | ☐ Not assessed |
| [[#Problem 2 — Smallest circle capturing 99 percent\|2]] | Smallest circle capturing 99 percent | ☐ Not assessed |
| [[#Problem 3 — Rescale squares of Normal sums\|3]] | Rescale squares of Normal sums | ☐ Not assessed |
| [[#Problem 4 — Gamma law of the Normal MLE variance\|4]] | Gamma law of the Normal MLE variance | ☐ Not assessed |
| [[#Problem 5 — Two chi-square probabilities (n=16)\|5]] | Two chi-square probabilities (n=16) | ☐ Not assessed |

---
## Problem 1 — Mode of chi-square distribution

### Mathematical restatement

Find the mode of $\chi_m^2$ for integers $m=1,2,\ldots$. The subscript $m$ is the **degrees of freedom**, not a factor $2m$.

### Worked solution

**S1 — Identify the chi-square density.** $f(x)=\frac{1}{2^{m/2}\Gamma(m/2)}x^{m/2-1}e^{-x/2}$, $x>0$, i.e. Gamma(shape $m/2$, scale 2).

**S2 — Optimize interior for m above 2.** $\frac{d}{dx}\log f(x)=\frac{m/2-1}{x}-\frac12=0$, hence $x=m-2$ when $m>2$.

**S3 — Check the boundary cases.** For $m=2$, $f$ decreases from its maximum at $0$; for $m=1$, it diverges at $0$ (boundary mode). Thus $\boxed{\operatorname{mode}(\chi_m^2)=\max(m-2,0)}$, with zero a boundary mode when $m\le2$.

### Mermaid decision route

~~~mermaid
flowchart TD
  A["P1: Mode of chi-square distribution"] --> B{"Does m exceed two?"}
  B -->|"Yes"| N0["S1: Identify the chi-square density"]
  B -->|"Not sure"| R["Review cue: do not report negative modes"]
  R --> N0
  N0 --> N1["S2: Optimize interior for m above 2"]
  N1 --> N2["S3: Check the boundary cases"]
  N2 --> Z["Deliver answer; check support and assumptions"]
  style R stroke:#777,stroke-dasharray:4 4
~~~

### Prerequisite and cue trace

| Step | General concept links | Recognition cue | Required move |
|---|---|---|---|
| S1 | [[Chi-Square Distribution]]; [[Gamma Distribution]] | Mode of chi square | Write Gamma-form PDF |
| S2 | [[Log-Likelihood]]; [[Derivative]] | Find interior mode | Differentiate log-density |
| S3 | [[Parameter Space]]; [[Maximum Likelihood Estimation]] | Degrees of freedom could be 1 or 2 | Check boundary separately |

**When to stop:** mode is max(m-2,0).

**Attempt record:** Not assessed; no learner failure or time has been inferred. At the next actual attempt record: `problem=P1`, the first stalled `step=S#`, the general prerequisite `node`, the observed outcome, and the learner's *exact original words* in quotes. Distinguish a cue-recognition miss from a calculation miss.

**Next task:** [[#Problem 2 — Smallest circle capturing 99 percent|Problem 2]].

---

## Problem 2 — Smallest circle capturing 99 percent

### Mathematical restatement

Independent $X,Y\sim N(0,1)$. Find smallest radius $r$ for centered circle with $P(X^2+Y^2\le r^2)=0.99$.

### Worked solution

**S1 — Convert geometry into squares.** Point lies inside radius $r$ iff $X^2+Y^2\le r^2$.

**S2 — Recognize chi-square.** By independence and standard normality, $V=X^2+Y^2\sim\chi^2_2$.

**S3 — Apply the quantile.** $r^2=\chi^2_{2,0.99}=-2\log(0.01)=9.21034$, so $\boxed{r\approx3.03485}$.

### Mermaid decision route

~~~mermaid
flowchart TD
  A["P2: Smallest circle capturing 99 percent"] --> B{"Is the event radial distance in 2D?"}
  B -->|"Yes"| N0["S1: Convert geometry into squares"]
  B -->|"Not sure"| R["Review cue: do not confuse radius with squared radius"]
  R --> N0
  N0 --> N1["S2: Recognize chi-square"]
  N1 --> N2["S3: Apply the quantile"]
  N2 --> Z["Deliver answer; check support and assumptions"]
  style R stroke:#777,stroke-dasharray:4 4
~~~

### Prerequisite and cue trace

| Step | General concept links | Recognition cue | Required move |
|---|---|---|---|
| S1 | [[Euclidean Norm]]; [[Chi-Square Distribution]] | Circle around origin | Square radius inequality |
| S2 | [[Independence of Random Variables]]; [[Chi-Square Distribution]] | Sum of squared standard normals | Use df=2 |
| S3 | [[Quantile Function]]; [[Natural logarithms]] | Probability inside is .99 | Take square root of 99th percentile |

**When to stop:** radius is about 3.035.

**Attempt record:** Not assessed; no learner failure or time has been inferred. At the next actual attempt record: `problem=P2`, the first stalled `step=S#`, the general prerequisite `node`, the observed outcome, and the learner's *exact original words* in quotes. Distinguish a cue-recognition miss from a calculation miss.

**Next task:** [[#Problem 3 — Rescale squares of Normal sums|Problem 3]].

---

## Problem 3 — Rescale squares of Normal sums

### Mathematical restatement

$X_1,\dots,X_6$ iid standard normal; $Y=(X_1+X_2+X_3)^2+(X_4+X_5+X_6)^2$. Find $c$ for $cY$ chi-square.

### Worked solution

**S1 — Find each sum variance.** $A=X_1+X_2+X_3\sim N(0,3)$ and $B=X_4+X_5+X_6\sim N(0,3)$ independently.

**S2 — Standardize both sums.** $Z_1=A/\sqrt3$, $Z_2=B/\sqrt3$ are independent $N(0,1)$.

**S3 — Match squared sum to chi-square.** $Y=3(Z_1^2+Z_2^2)=3\chi_2^2$. Hence $\boxed{c=1/3}$ and $cY\sim\chi^2_2$.

### Mermaid decision route

~~~mermaid
flowchart TD
  A["P3: Rescale squares of Normal sums"] --> B{"Are there two independent groups of three normals?"}
  B -->|"Yes"| N0["S1: Find each sum variance"]
  B -->|"Not sure"| R["Review cue: don't treat six raw Xi squares as six df"]
  R --> N0
  N0 --> N1["S2: Standardize both sums"]
  N1 --> N2["S3: Match squared sum to chi-square"]
  N2 --> Z["Deliver answer; check support and assumptions"]
  style R stroke:#777,stroke-dasharray:4 4
~~~

### Prerequisite and cue trace

| Step | General concept links | Recognition cue | Required move |
|---|---|---|---|
| S1 | [[Normal Distribution]]; [[Variance of a Sum of Independent Random Variables]] | Sums of 3 normals | Compute variance 3 each |
| S2 | [[Standard Normal Distribution]]; [[Linear Transformation Property of the Normal Distribution]] | Want squared standard normals | Divide each sum by sqrt3 |
| S3 | [[Chi-Square Distribution]]; [[Independence of Random Variables]] | Two independent squares | Use df=2 and c=1/3 |

**When to stop:** c equals 1/3.

**Attempt record:** Not assessed; no learner failure or time has been inferred. At the next actual attempt record: `problem=P3`, the first stalled `step=S#`, the general prerequisite `node`, the observed outcome, and the learner's *exact original words* in quotes. Distinguish a cue-recognition miss from a calculation miss.

**Next task:** [[#Problem 4 — Gamma law of the Normal MLE variance|Problem 4]].

---

## Problem 4 — Gamma law of the Normal MLE variance

### Mathematical restatement

$X_1,\ldots,X_n$ iid $N(\mu,\sigma^2)$. For $\hat\sigma^2=\frac1n\sum_i(X_i-\bar X)^2$, show the sampling distribution is Gamma with shape $(n-1)/2$ and **rate** $n/(2\sigma^2)$.

### Worked solution

**S1 — Invoke the Normal sum-of-squares pivot.** $Q=\sum_i(X_i-\bar X)^2/\sigma^2\sim\chi^2_{n-1}$. Estimating $\mu$ costs one degree of freedom.

**S2 — Relate pivot to estimator.** $\hat\sigma^2=(\sigma^2/n)Q$. Therefore $(n/\sigma^2)\hat\sigma^2\sim\chi^2_{n-1}$.

**S3 — Use chi-square–Gamma equivalence.** $\chi^2_\nu\equiv\operatorname{Gamma}(\nu/2,\text{ rate }1/2)$. Multiplying a Gamma random variable by $\sigma^2/n$ divides its rate by that scale factor: $\boxed{\hat\sigma^2\sim\operatorname{Gamma}((n-1)/2,\,n/(2\sigma^2))}$.

### Mermaid decision route

~~~mermaid
flowchart TD
  A["P4: Gamma law of the Normal MLE variance"] --> B{"Does the sum center on Xbar rather than mu?"}
  B -->|"Yes"| N0["S1: Invoke the Normal sum-of-squares pivot"]
  B -->|"Not sure"| R["Review cue: do not use n df after estimating mean"]
  R --> N0
  N0 --> N1["S2: Relate pivot to estimator"]
  N1 --> N2["S3: Use chi-square–Gamma equivalence"]
  N2 --> Z["Deliver answer; check support and assumptions"]
  style R stroke:#777,stroke-dasharray:4 4
~~~

### Prerequisite and cue trace

| Step | General concept links | Recognition cue | Required move |
|---|---|---|---|
| S1 | [[Sample Variance Chi-Square Distribution]]; [[Normal Distribution]] | Sum deviations from sample mean | Use n-1 df |
| S2 | [[Sample Mean and Sample Variance]] | MLE uses denominator n | Relate estimator to pivot |
| S3 | [[Gamma Distribution]]; [[Chi-Square Distribution]] | Question wants Gamma | Translate scaled chi-square to shape-rate Gamma |

**When to stop:** degrees of freedom are n-1.

**Attempt record:** Not assessed; no learner failure or time has been inferred. At the next actual attempt record: `problem=P4`, the first stalled `step=S#`, the general prerequisite `node`, the observed outcome, and the learner's *exact original words* in quotes. Distinguish a cue-recognition miss from a calculation miss.

**Next task:** [[#Problem 5 — Two chi-square probabilities (n=16)|Problem 5]].

---

## Problem 5 — Two chi-square probabilities (n=16)

### Mathematical restatement

For $n=16$ from $N(\mu,\sigma^2)$, evaluate $(a)\ P(\sigma^2/2\le\frac1{16}\sum(X_i-\mu)^2\le2\sigma^2)$ and $(b)$ the same with $X_i-\bar X$ in place of $X_i-\mu$.

### Worked solution

**S1 — Translate interval to a chi-square event.** Multiplying by $16/\sigma^2$ yields $8\le\sum_i(X_i-\text{center})^2/\sigma^2\le32$. The **bounds 8, 32** are the same in both parts.

**S2 — Choose degrees of freedom by center.** (a) Known population center $\mu$ gives $Q_a\sim\chi^2_{16}$. (b) Estimated center $\bar X$ gives $Q_b\sim\chi^2_{15}$; one df has been spent.

**S3 — Read chi-square CDF differences.** $\boxed{P_a=F_{\chi^2_{16}}(32)-F_{\chi^2_{16}}(8)\approx0.93887}$; $\boxed{P_b=F_{\chi^2_{15}}(32)-F_{\chi^2_{15}}(8)\approx0.91734}$. State both df before using a table or calculator.

### Mermaid decision route

~~~mermaid
flowchart TD
  A["P5: Two chi-square probabilities (n=16)"] --> B{"Does the sum use known mu or estimated Xbar?"}
  B -->|"Yes"| N0["S1: Translate interval to a chi-square event"]
  B -->|"Not sure"| R["Review cue: do not choose df by habit"]
  R --> N0
  N0 --> N1["S2: Choose degrees of freedom by center"]
  N1 --> N2["S3: Read chi-square CDF differences"]
  N2 --> Z["Deliver answer; check support and assumptions"]
  style R stroke:#777,stroke-dasharray:4 4
~~~

### Prerequisite and cue trace

| Step | General concept links | Recognition cue | Required move |
|---|---|---|---|
| S1 | [[Chi-Square Distribution]]; [[Inequalities]] | Probability for sample sum of squares | Standardize bounds |
| S2 | [[Degrees of Freedom]]; [[Sample Variance Chi-Square Distribution]] | Compare mu versus Xbar | Choose n or n-1 |
| S3 | [[Cumulative Distribution Function]]; [[Chi-Square Distribution]] | Interval probability | Subtract lower CDF from upper |

**When to stop:** use chi-square 16 in a and 15 in b.

**Attempt record:** Not assessed; no learner failure or time has been inferred. At the next actual attempt record: `problem=P5`, the first stalled `step=S#`, the general prerequisite `node`, the observed outcome, and the learner's *exact original words* in quotes. Distinguish a cue-recognition miss from a calculation miss.

**Next task:** [[Discussion 6 Stats132|Discussion 6]].

---

## Shared concept map

~~~mermaid
flowchart LR
  A1["Chi-Square Distribution"] --> P1["P1: Mode of chi-square distribution"]
  A2["Euclidean Norm"] --> P2["P2: Smallest circle capturing 99 percent"]
  A3["Normal Distribution"] --> P3["P3: Rescale squares of Normal sums"]
  A4["Sample Variance Chi-Square Distribution"] --> P4["P4: Gamma law of the Normal MLE variance"]
  A5["Chi-Square Distribution"] --> P5["P5: Two chi-square probabilities (n=16)"]
~~~

## Dated attempt history (embedded CSV; intentionally empty)

The four-column concept/step trace used in the prerequisite tables is a study aid. The CSV below is a human-readable audit *inside this Markdown*, **not** `System/reps.csv` and not input to brain/FSRS until an actual attempt is logged through `brain study log`. No attempts have been observed in this note.

```csv
date,problem,step,node,outcome,ledger_ref,ledger_status,said,agent_note
```

When a real attempt occurs, preserve `said` **verbatim and in full**, with your agent's interpretation only in `agent_note`. Attach a real `ref` returned by brain; never manufacture timestamps, FSRS outcomes or copied attempts. `System/index/memory.json` is generated output and must not be hand-edited.

**Checkpoint:** 0/5 independently completed in this note; consult the student's separately maintained records for other progress.
