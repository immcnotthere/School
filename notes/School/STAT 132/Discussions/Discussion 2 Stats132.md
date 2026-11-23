---
aliases:
  - "Discussion 2 Stats132"
  - "STAT 132 Discussion 2"
  - "Stats132 Disc 2"
type: study
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
item_type: discussion-worked-trace
discussion: 2
worksheet_year: 2025
status: not-started
problems: 5
completed_problems: []
source: "STAT132/files/homework/STAT132 Discussion 02 (W25 worksheet).pdf"
retention_input: "System/reps.csv"
retention_words: "System/rep-words.jsonl"
retention_output: "System/index/memory.json"
created: 2026-11-22
---
# Discussion 2 Stats132

**Original:** [Discussion 2 W25 worksheet](https://github.com/immcnotthere/School/blob/main/STAT132/files/homework/STAT132%20Discussion%2002%20%28W25%20worksheet%29.pdf). Rephrased mathematical prompts and solutions below are anchored to this worksheet. The worksheet is from Winter 2025; the study work is in 2026.

**How to study:** Hide each worked solution, attempt unaided, and find the *first* Mermaid step that stalls. The cue table points to reusable Obsidian concept notes; unresolved `[[wikilinks]]` are suggestions for missing notes. All 5 problems start **not assessed**. Reading solutions is not a completed attempt.

| Problem | Topic | Status |
|---|---|---|
| [[#Problem 1 — Beta–binomial posterior|1]] | Beta–binomial posterior | ☐ Not assessed |
| [[#Problem 2 — Normal posterior spread bound|2]] | Normal posterior spread bound | ☐ Not assessed |
| [[#Problem 3 — Gamma–exponential posterior|3]] | Gamma–exponential posterior | ☐ Not assessed |
| [[#Problem 4 — Posterior mean as weighted average|4]] | Posterior mean as weighted average | ☐ Not assessed |
| [[#Problem 5 — Poisson–Gamma Bayes estimator|5]] | Poisson–Gamma Bayes estimator | ☐ Not assessed |

---
## Problem 1 — Beta–binomial posterior

### Mathematical restatement

Prior defect proportion $\theta\sim\operatorname{Beta}(2,200)$. In 100 sampled items, 3 are defective. Determine $\pi(\theta\mid x)$.

### Worked solution

**S1 — Identify the data model.** For $X\mid\theta\sim\operatorname{Binomial}(100,\theta)$, the observed likelihood is $L(\theta)\propto\theta^3(1-\theta)^{97}$. The $3$ is a **success count** (defectives); $97$ is the remainder.

**S2 — Multiply by the prior kernel.** The Beta prior contributes $\pi(\theta)\propto\theta^{2-1}(1-\theta)^{200-1}$. Thus $\pi(\theta\mid x)\propto \theta^{(2-1)+3}(1-\theta)^{(200-1)+97}$.

**S3 — Identify the posterior family.** Add successes to $\alpha$ and failures to $\beta$: $\boxed{\theta\mid x\sim\operatorname{Beta}(5,297)}$. The updated shapes remain positive and total $302$. Value of the binomial coefficient is irrelevant to the kernel.

### Mermaid decision route

~~~mermaid
flowchart TD
  A["P1: Beta–binomial posterior"] --> B{"Does Beta prior pair with a binomial sample?"}
  B -->|"Yes"| N0["S1: Identify the data model"]
  B -->|"Not sure"| R["Review cue: check whether data represent binary success/failure"]
  R --> N0
  N0 --> N1["S2: Multiply by the prior kernel"]
  N1 --> N2["S3: Identify the posterior family"]
  N2 --> Z["Deliver answer; check support and assumptions"]
  style R stroke:#777,stroke-dasharray:4 4
~~~

### Prerequisite and cue trace

| Step | General concept links | Recognition cue | Required move |
|---|---|---|---|
| S1 | [[Beta Distribution]]; [[Binomial Distribution]]; [[Conjugate Prior]] | Beta prior + binary counts | Choose Beta–binomial conjugacy |
| S2 | [[Likelihood Function]]; [[Independence of Random Variables]] | 3 of 100 defective | Count 3 successes and 97 failures |
| S3 | [[Conjugate Prior]]; [[Posterior Distribution]] | Prior and likelihood are both powers of theta | Add exponents and normalize |

**When to stop:** posterior has the Beta family.

**Attempt record:** Not assessed; no learner failure or time has been inferred. At the next actual attempt record: `problem=P1`, the first stalled `step=S#`, the general prerequisite `node`, the observed outcome, and the learner's *exact original words* in quotes. Distinguish a cue-recognition miss from a calculation miss.

---

## Problem 2 — Normal posterior spread bound

### Mathematical restatement

For $n=100$, $X_i\sim N(\mu,4)$ with unknown $\mu$. The prior for $\mu$ is $N(\mu_0,\tau^2)$. Prove $\operatorname{SD}(\mu\mid\mathbf X)<1/5$ for every finite $\tau>0$.

### Worked solution

**S1 — Identify the sample precision.** Known observation variance is $\sigma^2=4$, so the sample mean has variance $\sigma^2/n=4/100=1/25$, or data precision $25$.

**S2 — Add normal precisions.** Normal–normal conjugacy yields $v_{\text{post}}=\left(1/\tau^2+n/\sigma^2\right)^{-1}=\left(1/\tau^2+25\right)^{-1}$.

**S3 — Apply the strict inequality.** Since $1/\tau^2>0$ for any finite prior standard deviation, $v_{\text{post}}<1/25$, hence $\boxed{\operatorname{SD}(\mu\mid \mathbf X)<1/5}$. Equality is approached, never attained, as $\tau\to\infty$.

### Mermaid decision route

~~~mermaid
flowchart TD
  A["P2: Normal posterior spread bound"] --> B{"Are both prior and likelihood Normal?"}
  B -->|"Yes"| N0["S1: Identify the sample precision"]
  B -->|"Not sure"| R["Review cue: rewrite the target in terms of precision"]
  R --> N0
  N0 --> N1["S2: Add normal precisions"]
  N1 --> N2["S3: Apply the strict inequality"]
  N2 --> Z["Deliver answer; check support and assumptions"]
  style R stroke:#777,stroke-dasharray:4 4
~~~

### Prerequisite and cue trace

| Step | General concept links | Recognition cue | Required move |
|---|---|---|---|
| S1 | [[Normal Distribution]]; [[Sample Mean]] | Known sigma=2 and n=100 | Recognize variance of sample mean |
| S2 | [[Conjugate Prior]]; [[Normal Distribution]] | Normal prior and normal likelihood | Add prior and data precision |
| S3 | [[Equivalent equations]]; [[Variance]] | Show strict upper bound | Compare denominators before taking square roots |

**When to stop:** posterior spread stays below 0.2.

**Attempt record:** Not assessed; no learner failure or time has been inferred. At the next actual attempt record: `problem=P2`, the first stalled `step=S#`, the general prerequisite `node`, the observed outcome, and the learner's *exact original words* in quotes. Distinguish a cue-recognition miss from a calculation miss.

---

## Problem 3 — Gamma–exponential posterior

### Mathematical restatement

Service time $X_i$ is exponential with unknown **rate** $\theta$. Prior for $\theta$ is Gamma with mean $0.2$ and SD $1$. For $n=20$, observed sample mean $\bar x=3.8$ minutes. Determine posterior, using Gamma(shape, **rate**).

### Worked solution

**S1 — Recover prior hyperparameters from moments.** For $\theta\sim\operatorname{Gamma}(a,b)$ with rate $b$, $E\theta=a/b=0.2$ and $\operatorname{Var}(\theta)=a/b^2=1$. Therefore $b=0.2$ and $a=0.04$. This prior is concentrated near zero with a long right tail.

**S2 — Reduce the observations.** For exponential rate $\theta$, $L(\theta)=\theta^n e^{-\theta\sum x_i}$. The sample sum is $T=n\bar x=20(3.8)=76$.

**S3 — Update Gamma shape and rate.** The kernel is $\theta^{a+n-1}e^{-(b+T)\theta}$. Hence $\boxed{\theta\mid x\sim\operatorname{Gamma}(20.04,76.2)}$ (shape–rate). A scale-parameter Gamma convention would have different second-coordinate notation.

### Mermaid decision route

~~~mermaid
flowchart TD
  A["P3: Gamma–exponential posterior"] --> B{"Is the Gamma second parameter a rate?"}
  B -->|"Yes"| N0["S1: Recover prior hyperparameters from moments"]
  B -->|"Not sure"| R["Review cue: confirm the PDF uses rate b rather than scale"]
  R --> N0
  N0 --> N1["S2: Reduce the observations"]
  N1 --> N2["S3: Update Gamma shape and rate"]
  N2 --> Z["Deliver answer; check support and assumptions"]
  style R stroke:#777,stroke-dasharray:4 4
~~~

### Prerequisite and cue trace

| Step | General concept links | Recognition cue | Required move |
|---|---|---|---|
| S1 | [[Gamma Distribution]]; [[Expectation and Variance]] | Gamma prior specified by mean and SD | Square SD; solve for shape and rate |
| S2 | [[Exponential Distribution]]; [[Likelihood Function]] | Rate exponential with a sample mean | Convert mean to sample sum |
| S3 | [[Gamma-Exponential Update]]; [[Conjugate Prior]] | Product contains power times decaying exponential | Add n to shape and T to rate |

**When to stop:** posterior shape and rate are 20.04 and 76.2.

**Attempt record:** Not assessed; no learner failure or time has been inferred. At the next actual attempt record: `problem=P3`, the first stalled `step=S#`, the general prerequisite `node`, the observed outcome, and the learner's *exact original words* in quotes. Distinguish a cue-recognition miss from a calculation miss.

---

## Problem 4 — Posterior mean as weighted average

### Mathematical restatement

In $n$ Bernoulli trials with unknown $\theta$, let prior $\theta\sim\operatorname{Beta}(a,b)$ have prior mean $\mu_0=a/(a+b)$. Show $E[\theta\mid X]=\varepsilon_n\bar X+(1-\varepsilon_n)\mu_0$ and $\varepsilon_n\to1$.

### Worked solution

**S1 — Write the Beta posterior mean.** With $S=\sum_i X_i=n\bar X$, $\theta\mid X\sim\operatorname{Beta}(a+S,b+n-S)$, so $E[\theta\mid X]=(a+n\bar X)/(a+b+n)$.

**S2 — Separate data and prior weights.** Since $a=(a+b)\mu_0$, rewrite $\frac{a+n\bar X}{a+b+n}=\frac{n}{n+a+b}\bar X+\frac{a+b}{n+a+b}\mu_0$.

**S3 — Verify the limit.** Set $\boxed{\varepsilon_n=n/(n+a+b)}$. Then $\varepsilon_n\in(0,1)$ and $\lim_{n\to\infty}\varepsilon_n=1$ for fixed finite $a,b>0$. The data weight grows with $n$.

### Mermaid decision route

~~~mermaid
flowchart TD
  A["P4: Posterior mean as weighted average"] --> B{"Are the two weights nonnegative and summing to one?"}
  B -->|"Yes"| N0["S1: Write the Beta posterior mean"]
  B -->|"Not sure"| R["Review cue: rewrite prior shape a using mu0"]
  R --> N0
  N0 --> N1["S2: Separate data and prior weights"]
  N1 --> N2["S3: Verify the limit"]
  N2 --> Z["Deliver answer; check support and assumptions"]
  style R stroke:#777,stroke-dasharray:4 4
~~~

### Prerequisite and cue trace

| Step | General concept links | Recognition cue | Required move |
|---|---|---|---|
| S1 | [[Beta-Bernoulli Update]]; [[Sample Mean]] | Bernoulli likelihood; Beta prior | Write updated shapes and posterior mean |
| S2 | [[Prior as Pretend Data]]; [[Equivalent equations]] | Question explicitly says weighted average | Identify coefficients of Xbar and mu0 |
| S3 | [[Convergence]]; [[Prior Influence and Sample Size]] | Show epsilon_n tends to one | Divide by n and take limit |

**When to stop:** posterior mean has requested weighted-average form.

**Attempt record:** Not assessed; no learner failure or time has been inferred. At the next actual attempt record: `problem=P4`, the first stalled `step=S#`, the general prerequisite `node`, the observed outcome, and the learner's *exact original words* in quotes. Distinguish a cue-recognition miss from a calculation miss.

---

## Problem 5 — Poisson–Gamma Bayes estimator

### Mathematical restatement

Roll defect counts $X_i\mid\theta\sim\operatorname{Poisson}(\theta)$ for five rolls: $2,2,6,0,3$. Prior $\theta\sim\operatorname{Gamma}(3,1)$ (shape–rate). Find the Bayes estimator under squared-error loss.

### Worked solution

**S1 — Identify posterior sufficient statistics.** There are $n=5$ rolls and total defects $S=2+2+6+0+3=13$. The Poisson likelihood in $\theta$ is proportional to $\theta^{13}e^{-5\theta}$.

**S2 — Conjugately update.** Multiplying by the Gamma prior $\theta^{3-1}e^{-1\theta}$ yields $\boxed{\theta\mid x\sim\operatorname{Gamma}(16,6)}$.

**S3 — Choose the estimator from the loss function.** **Squared error** means the posterior mean, not the posterior mode: $\boxed{\hat\theta_B=E[\theta\mid x]=16/6=8/3\approx2.667}$ defects per roll.

### Mermaid decision route

~~~mermaid
flowchart TD
  A["P5: Poisson–Gamma Bayes estimator"] --> B{"Does the wording name squared-error loss?"}
  B -->|"Yes"| N0["S1: Identify posterior sufficient statistics"]
  B -->|"Not sure"| R["Review cue: do not accidentally choose the posterior mode"]
  R --> N0
  N0 --> N1["S2: Conjugately update"]
  N1 --> N2["S3: Choose the estimator from the loss function"]
  N2 --> Z["Deliver answer; check support and assumptions"]
  style R stroke:#777,stroke-dasharray:4 4
~~~

### Prerequisite and cue trace

| Step | General concept links | Recognition cue | Required move |
|---|---|---|---|
| S1 | [[Poisson Distribution]]; [[Likelihood Function]] | Counts per roll and Poisson model | Sum counts and observations |
| S2 | [[Gamma-Poisson Update]]; [[Conjugate Prior]] | Gamma prior on Poisson mean | Update shape by total and rate by sample count |
| S3 | [[Loss Functions]]; [[Posterior Mean as a Weighted Average]] | Square error loss | Use posterior mean as Bayes action |

**When to stop:** posterior mean is 8/3.

**Attempt record:** Not assessed; no learner failure or time has been inferred. At the next actual attempt record: `problem=P5`, the first stalled `step=S#`, the general prerequisite `node`, the observed outcome, and the learner's *exact original words* in quotes. Distinguish a cue-recognition miss from a calculation miss.

---

## Shared concept map

~~~mermaid
flowchart LR
  A1["Beta Distribution"] --> P1["P1: Beta–binomial posterior"]
  A2["Normal Distribution"] --> P2["P2: Normal posterior spread bound"]
  A3["Gamma Distribution"] --> P3["P3: Gamma–exponential posterior"]
  A4["Beta-Bernoulli Update"] --> P4["P4: Posterior mean as weighted average"]
  A5["Poisson Distribution"] --> P5["P5: Poisson–Gamma Bayes estimator"]
~~~

## Dated attempt history (embedded CSV; intentionally empty)

The four-column concept/step trace used in the prerequisite tables is a study aid. The CSV below is a human-readable audit *inside this Markdown*, **not** `System/reps.csv` and not input to brain/FSRS until an actual attempt is logged through `brain study log`. No attempts have been observed in this note.

```csv
date,problem,step,node,outcome,ledger_ref,ledger_status,said,agent_note
```

When a real attempt occurs, preserve `said` **verbatim and in full**, with your agent's interpretation only in `agent_note`. Attach a real `ref` returned by brain; never manufacture timestamps, FSRS outcomes or copied attempts. `System/index/memory.json` is generated output and must not be hand-edited.

**Checkpoint:** 0/5 independently completed in this note; consult the student's separately maintained records for other progress.
