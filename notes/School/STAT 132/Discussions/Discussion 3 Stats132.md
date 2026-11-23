---
aliases:
  - "Discussion 3 Stats132"
  - "STAT 132 Discussion 3"
  - "Stats132 Disc 3"
type: study
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
item_type: discussion-worked-trace
discussion: 3
worksheet_year: 2025
status: not-started
problems: 5
completed_problems: []
source: "STAT132/files/homework/STAT132 Discussion 03 (W25 worksheet).pdf"
retention_input: "System/reps.csv"
retention_words: "System/rep-words.jsonl"
retention_output: "System/index/memory.json"
created: 2026-11-22
---
# Discussion 3 Stats132

**Original:** [Discussion 3 W25 worksheet](https://github.com/immcnotthere/School/blob/main/STAT132/files/homework/STAT132%20Discussion%2003%20%28W25%20worksheet%29.pdf). Rephrased mathematical prompts and solutions below are anchored to this worksheet. The worksheet is from Winter 2025; the study work is in 2026.

**How to study:** Hide each worked solution, attempt unaided, and find the *first* Mermaid step that stalls. The cue table points to reusable Obsidian concept notes; unresolved `[[wikilinks]]` are suggestions for missing notes. All 5 problems start **not assessed**. Reading solutions is not a completed attempt.

| Problem | Topic | Status |
|---|---|---|
| [[#Problem 1 — MLE of Normal mean and variance|1]] | MLE of Normal mean and variance | ☐ Not assessed |
| [[#Problem 2 — MLE of Pareto tail parameter|2]] | MLE of Pareto tail parameter | ☐ Not assessed |
| [[#Problem 3 — MLEs of Uniform endpoints|3]] | MLEs of Uniform endpoints | ☐ Not assessed |
| [[#Problem 4 — MLE of the exponential median|4]] | MLE of the exponential median | ☐ Not assessed |
| [[#Problem 5 — MLE of the Normal 95th percentile|5]] | MLE of the Normal 95th percentile | ☐ Not assessed |

---
## Problem 1 — MLE of Normal mean and variance

### Mathematical restatement

$X_1,\ldots,X_n\overset{\mathrm{iid}}{\sim}N(\mu,\sigma^2)$, both $\mu$ and $\sigma^2$ unknown. Find the joint MLEs.

### Worked solution

**S1 — Construct and log the likelihood.** $\ell(\mu,\sigma^2)=-\frac n2\log(2\pi)-\frac n2\log\sigma^2-\frac1{2\sigma^2}\sum_i(x_i-\mu)^2$. Treat both parameters as unknown.

**S2 — Optimize the mean.** $\partial\ell/\partial\mu=\sum_i(x_i-\mu)/\sigma^2=0$ gives $\boxed{\hat\mu=\bar X}$.

**S3 — Optimize the variance.** Set $v=\sigma^2>0$. Then $\partial\ell/\partial v=-n/(2v)+\sum_i(x_i-\hat\mu)^2/(2v^2)=0$, giving $\boxed{\hat\sigma^2_{\mathrm{MLE}}=\frac1n\sum_i(X_i-\bar X)^2}$. **Denominator is $n$**, not the unbiased-estimator denominator $n-1$. For nondegenerate samples, this maximizes the likelihood.

### Mermaid decision route

~~~mermaid
flowchart TD
  A["P1: MLE of Normal mean and variance"] --> B{"Are both mu and variance free parameters?"}
  B -->|"Yes"| N0["S1: Construct and log the likelihood"]
  B -->|"Not sure"| R["Review cue: do not use n-1 automatically"]
  R --> N0
  N0 --> N1["S2: Optimize the mean"]
  N1 --> N2["S3: Optimize the variance"]
  N2 --> Z["Deliver answer; check support and assumptions"]
  style R stroke:#777,stroke-dasharray:4 4
~~~

### Prerequisite and cue trace

| Step | General concept links | Recognition cue | Required move |
|---|---|---|---|
| S1 | [[Normal Distribution]]; [[Likelihood Function]] | Unknown mean AND variance | Write joint normal likelihood |
| S2 | [[Derivative]]; [[Sample Mean]] | Find maximum with respect to mu | Differentiate and solve mu equation |
| S3 | [[Variance]]; [[Maximum Likelihood Estimation]] | MLE variance requested | Differentiate in variance v and use denominator n |

**When to stop:** MLEs are xbar and average squared deviations using n.

**Attempt record:** Not assessed; no learner failure or time has been inferred. At the next actual attempt record: `problem=P1`, the first stalled `step=S#`, the general prerequisite `node`, the observed outcome, and the learner's *exact original words* in quotes. Distinguish a cue-recognition miss from a calculation miss.

---

## Problem 2 — MLE of Pareto tail parameter

### Mathematical restatement

Given $x>1$ and $f(x\mid\theta)=\theta/x^{\theta+1}$ for $\theta>0$, observe $X_1,\ldots,X_n$ iid. Find $\hat\theta_{\mathrm{MLE}}$.

### Worked solution

**S1 — Multiply densities and log.** $L(\theta)=\theta^n\prod_i x_i^{-(\theta+1)}$ (all observed $x_i>1$). Thus $\ell(\theta)=n\log\theta-(\theta+1)\sum_i\log x_i$.

**S2 — Differentiate.** $\ell'(\theta)=n/\theta-\sum_i\log x_i$. Set to zero: $\boxed{\hat\theta=n/\sum_i\log X_i}$.

**S3 — Check it is a maximum.** $\ell''(\theta)=-n/\theta^2<0$. Since $\log X_i>0$, $\hat\theta>0$ satisfies the parameter domain.

### Mermaid decision route

~~~mermaid
flowchart TD
  A["P2: MLE of Pareto tail parameter"] --> B{"Are all observations greater than one?"}
  B -->|"Yes"| N0["S1: Multiply densities and log"]
  B -->|"Not sure"| R["Review cue: do not mistakenly differentiate x instead of theta"]
  R --> N0
  N0 --> N1["S2: Differentiate"]
  N1 --> N2["S3: Check it is a maximum"]
  N2 --> Z["Deliver answer; check support and assumptions"]
  style R stroke:#777,stroke-dasharray:4 4
~~~

### Prerequisite and cue trace

| Step | General concept links | Recognition cue | Required move |
|---|---|---|---|
| S1 | [[Likelihood Function]]; [[Independence of Random Variables]] | Density has variable exponent theta | Take log of product |
| S2 | [[Log-Likelihood]]; [[Derivative]] | Theta appears in exponent and prefactor | Differentiate n log theta and linear term |
| S3 | [[Maximum Likelihood Estimation]]; [[Parameter Space]] | Stationary solution found | Verify concavity and theta>0 |

**When to stop:** MLE is n over sum log observations.

**Attempt record:** Not assessed; no learner failure or time has been inferred. At the next actual attempt record: `problem=P2`, the first stalled `step=S#`, the general prerequisite `node`, the observed outcome, and the learner's *exact original words* in quotes. Distinguish a cue-recognition miss from a calculation miss.

---

## Problem 3 — MLEs of Uniform endpoints

### Mathematical restatement

$X_1,\ldots,X_n$ iid Uniform$[\theta_1,\theta_2]$ with both endpoints unknown and $\theta_1<\theta_2$. Find both MLEs.

### Worked solution

**S1 — Include support in likelihood.** $L(\theta_1,\theta_2)=(\theta_2-\theta_1)^{-n}\mathbf1\{\theta_1\le X_{(1)},\,\theta_2\ge X_{(n)}\}$, where $X_{(1)}=\min_iX_i$, $X_{(n)}=\max_iX_i$.

**S2 — Shrink the allowed interval.** For any parameters containing all observations, the likelihood increases when interval width $\theta_2-\theta_1$ decreases. The smallest allowed interval is $[X_{(1)},X_{(n)}]$.

**S3 — Report endpoints and boundary caution.** $\boxed{\hat\theta_1=X_{(1)},\quad\hat\theta_2=X_{(n)}}$ for nonidentical observations. The derivative-only interior critical-point method does **not** find this boundary maximum; support is essential.

### Mermaid decision route

~~~mermaid
flowchart TD
  A["P3: MLEs of Uniform endpoints"] --> B{"Does the parameter determine the support interval?"}
  B -->|"Yes"| N0["S1: Include support in likelihood"]
  B -->|"Not sure"| R["Review cue: do not drop indicator and look only for derivative zero"]
  R --> N0
  N0 --> N1["S2: Shrink the allowed interval"]
  N1 --> N2["S3: Report endpoints and boundary caution"]
  N2 --> Z["Deliver answer; check support and assumptions"]
  style R stroke:#777,stroke-dasharray:4 4
~~~

### Prerequisite and cue trace

| Step | General concept links | Recognition cue | Required move |
|---|---|---|---|
| S1 | [[Uniform Distribution (Continuous)]]; [[Support (Probability)]] | Unknown support endpoints | Include indicator constraints |
| S2 | [[Order Statistics]]; [[Likelihood Function]] | Likelihood proportional to width^{-n} | Maximize by shrinking width |
| S3 | [[Maximum Likelihood Estimation]]; [[Parameter Space]] | Support depends on parameter | Check boundary, not derivative |

**When to stop:** MLEs are observed min and max.

**Attempt record:** Not assessed; no learner failure or time has been inferred. At the next actual attempt record: `problem=P3`, the first stalled `step=S#`, the general prerequisite `node`, the observed outcome, and the learner's *exact original words* in quotes. Distinguish a cue-recognition miss from a calculation miss.

---

## Problem 4 — MLE of the exponential median

### Mathematical restatement

Iid exponential observations with an unknown distribution parameter. Find the MLE for the **population median** rather than for the parameter itself.

### Worked solution

**S1 — Write the median equation.** For rate $\lambda$, $F(x)=1-e^{-\lambda x}$. The median $m$ solves $F(m)=1/2$, so $m=\log 2/\lambda$.

**S2 — Find the exponential MLE.** $L(\lambda)\propto\lambda^n e^{-\lambda\sum X_i}$ gives $\hat\lambda=n/\sum X_i=1/\bar X$.

**S3 — Apply the invariance property.** Plug the rate MLE into the median: $\boxed{\hat m=\frac{\log2}{\hat\lambda}=\bar X\log2}$. If the parameter is instead the **mean/scale**, its MLE is $\bar X$ and the final median MLE is still $\bar X\log2$.

### Mermaid decision route

~~~mermaid
flowchart TD
  A["P4: MLE of the exponential median"] --> B{"Is the target a function of the unknown parameter?"}
  B -->|"Yes"| N0["S1: Write the median equation"]
  B -->|"Not sure"| R["Review cue: find parameter MLE first, then transform"]
  R --> N0
  N0 --> N1["S2: Find the exponential MLE"]
  N1 --> N2["S3: Apply the invariance property"]
  N2 --> Z["Deliver answer; check support and assumptions"]
  style R stroke:#777,stroke-dasharray:4 4
~~~

### Prerequisite and cue trace

| Step | General concept links | Recognition cue | Required move |
|---|---|---|---|
| S1 | [[Exponential Distribution]]; [[Cumulative Distribution Function]] | Asked for the median | Solve F(m)=0.5 |
| S2 | [[Likelihood Function]]; [[Maximum Likelihood Estimation]] | Unknown exponential parameter | Find the MLE of rate or mean |
| S3 | [[Invariance Property of MLEs]]; [[Quantile Function]] | Target is a function of parameter | Plug the MLE into median formula |

**When to stop:** mhat is Xbar log2.

**Attempt record:** Not assessed; no learner failure or time has been inferred. At the next actual attempt record: `problem=P4`, the first stalled `step=S#`, the general prerequisite `node`, the observed outcome, and the learner's *exact original words* in quotes. Distinguish a cue-recognition miss from a calculation miss.

---

## Problem 5 — MLE of the Normal 95th percentile

### Mathematical restatement

$X_i$ iid $N(\mu,\sigma^2)$ with both parameters unknown. Find MLE of the population value $a$ such that $P(X<a)=0.95$.

### Worked solution

**S1 — Write the population quantile.** Standardize $P(X<a)=\Phi((a-\mu)/\sigma)=0.95$. Therefore $a=\mu+z_{0.95}\sigma$, $z_{0.95}=\Phi^{-1}(0.95)\approx1.64485$.

**S2 — Find Normal MLE ingredients.** $\hat\mu=\bar X$, $\hat\sigma^2=\frac1n\sum_i(X_i-\bar X)^2$, and $\hat\sigma=\sqrt{\hat\sigma^2}$.

**S3 — Apply invariance.** $\boxed{\hat a=\bar X+1.64485\sqrt{\frac1n\sum_i(X_i-\bar X)^2}}$. For this **MLE** use $n$ in the variance, not $n-1$.

### Mermaid decision route

~~~mermaid
flowchart TD
  A["P5: MLE of the Normal 95th percentile"] --> B{"Does the target use both mu and sigma?"}
  B -->|"Yes"| N0["S1: Write the population quantile"]
  B -->|"Not sure"| R["Review cue: do not use unbiased sample variance"]
  R --> N0
  N0 --> N1["S2: Find Normal MLE ingredients"]
  N1 --> N2["S3: Apply invariance"]
  N2 --> Z["Deliver answer; check support and assumptions"]
  style R stroke:#777,stroke-dasharray:4 4
~~~

### Prerequisite and cue trace

| Step | General concept links | Recognition cue | Required move |
|---|---|---|---|
| S1 | [[Standard Normal Distribution]]; [[Quantile Function]] | 0.95 quantile | Solve a=mu+z sigma |
| S2 | [[Normal Distribution]]; [[Maximum Likelihood Estimation]] | Both parameters unknown | Find MLEs for mu and sigma |
| S3 | [[Invariance Property of MLEs]]; [[Sample Mean and Sample Variance]] | Estimator of quantile is requested | Plug MLEs into target expression |

**When to stop:** quantile estimator is xbar plus 1.645 times MLE sd.

**Attempt record:** Not assessed; no learner failure or time has been inferred. At the next actual attempt record: `problem=P5`, the first stalled `step=S#`, the general prerequisite `node`, the observed outcome, and the learner's *exact original words* in quotes. Distinguish a cue-recognition miss from a calculation miss.

---

## Shared concept map

~~~mermaid
flowchart LR
  A1["Normal Distribution"] --> P1["P1: MLE of Normal mean and variance"]
  A2["Likelihood Function"] --> P2["P2: MLE of Pareto tail parameter"]
  A3["Uniform Distribution (Continuous)"] --> P3["P3: MLEs of Uniform endpoints"]
  A4["Exponential Distribution"] --> P4["P4: MLE of the exponential median"]
  A5["Standard Normal Distribution"] --> P5["P5: MLE of the Normal 95th percentile"]
~~~

## Dated attempt history (embedded CSV; intentionally empty)

The four-column concept/step trace used in the prerequisite tables is a study aid. The CSV below is a human-readable audit *inside this Markdown*, **not** `System/reps.csv` and not input to brain/FSRS until an actual attempt is logged through `brain study log`. No attempts have been observed in this note.

```csv
date,problem,step,node,outcome,ledger_ref,ledger_status,said,agent_note
```

When a real attempt occurs, preserve `said` **verbatim and in full**, with your agent's interpretation only in `agent_note`. Attach a real `ref` returned by brain; never manufacture timestamps, FSRS outcomes or copied attempts. `System/index/memory.json` is generated output and must not be hand-edited.

**Checkpoint:** 0/5 independently completed in this note; consult the student's separately maintained records for other progress.
