---
type: study
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
item_type: discussion-worked-trace
discussion: 1
week: 2
worksheet_year: 2025
status: in-progress
problems: 5
source: "STAT132/files/homework/STAT132 Discussion 01 - priors and likelihoods (W25 worksheet).pdf"
source_repository: "immcnotthere/School"
review_policy: "Do not create attempts from reading this note; only brain study log writes System/reps.csv"
retention_input: "System/reps.csv"
retention_words: "System/rep-words.jsonl"
retention_output: "System/index/memory.json"
last_authored: 2026-11-22
---
# STAT 132 — Discussion 1: Priors and Likelihoods (W25)

> **Purpose:** One traceable worked example per question: mathematical restatement → worked solution → decision flow → atomic prerequisite concepts → recognition cues. The diagrams describe a *solution route*, not evidence that the student has performed it.

**Source:** [Original 2025 worksheet](https://github.com/immcnotthere/School/blob/main/STAT132/files/homework/STAT132%20Discussion%2001%20-%20priors%20and%20likelihoods%20%28W25%20worksheet%29.pdf). This worksheet was written in Winter 2025 and is being studied in 2026. Descriptions below retain its numerical specifications and mathematical intent; wording is normalized into readable Markdown.

**Progress convention:** "Walkthrough provided" ≠ "independently solved." Q1 has a documented algebraic failure point; Q2–Q5 are not assigned scores by this note. Retention attempts must not be fabricated or appended directly to a CSV.

## Quick index

| Problem | Target | Principal cues | Outcome of worked example |
|---|---|---|---|
| 1 | Determine a Beta prior PDF from mean and variance | "Beta", given moments, "prior pdf" | $\pi(\theta)=168\theta^2(1-\theta)^5$ on $(0,1)$ |
| 2 | Likelihood and sketch for exponential observations | "rate", independent data, "likelihood" | $L(\lambda)=\lambda^3e^{-7.5\lambda}$; peak $\lambda=0.4$ |
| 3 | Assess proposed Uniform prior on exponential rate | "prior reasonable?", rate vs duration | Proper prior, but often implausible; explain support and implications |
| 4 | Write a prior for two possible defect rates | "either 0.1 or 0.2" | Two-point PMF; e.g. probabilities $1/2$, $1/2$ |
| 5 | Find moments of a triangular prior density | Given $\pi(p)$; "prior mean and variance" | $E[p]=1/3$, $\mathrm{Var}(p)=1/18$ |

---

## Problem 1 — Recover a Beta PDF from its moments

### 1. Mathematical statement

A parameter $\theta$ has prior $\operatorname{Beta}(\alpha,\beta)$, with

$$
E(\theta)=\frac13,\qquad \operatorname{Var}(\theta)=\frac1{45}.
$$

Determine the prior density $\pi(\theta)$.

**Unknowns:** $\alpha>0,\beta>0$. **Deliverable:** the *density in $\theta$*, not merely the two shape parameters.

### 2. Worked solution

**S1 — Recognize the Beta family's moment equations.**

$$
E(\theta)=\frac{\alpha}{\alpha+\beta},
\qquad
\operatorname{Var}(\theta)=
\frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}.
$$

**S2 — Turn the mean condition into a simple equation.** Multiply both sides by $3(\alpha+\beta)$:

$$
\frac{\alpha}{\alpha+\beta}=\frac13
\quad\Longrightarrow\quad
3\alpha=\alpha+\beta.
$$

This is *clearing a denominator* (equivalent to cross multiplication); it does not yet require calculus or properties of the Beta PDF.

**S3 — Collect like terms and choose the easy variable to eliminate.**

$$
3\alpha-\alpha=\beta
\quad\Longrightarrow\quad
\boxed{\beta=2\alpha}.
$$

It is equally valid to isolate $\alpha=\beta/2$. By contrast, $\alpha=(\alpha+\beta)/3$ is a true rearrangement but **does not isolate $\alpha$**: it still occurs on the right side.

**S4 — Substitute into the variance equation.**

$$
\frac1{45}
=\frac{\alpha(2\alpha)}{(3\alpha)^2(3\alpha+1)}
=\frac{2}{9(3\alpha+1)}.
$$

**S5 — Solve for the two shape parameters.**

$$
9(3\alpha+1)=90
\ \Longrightarrow\
3\alpha+1=10
\ \Longrightarrow\
\boxed{\alpha=3,\quad\beta=6}.
$$

**S6 — Write and normalize the Beta density.** Its general formula is

$$
\pi(\theta)=
\frac{\Gamma(\alpha+\beta)}
{\Gamma(\alpha)\Gamma(\beta)}
\theta^{\alpha-1}(1-\theta)^{\beta-1},\quad 0<\theta<1.
$$

With $\Gamma(n)=(n-1)!$ for positive integers,

$$
\frac{\Gamma(9)}{\Gamma(3)\Gamma(6)}
=\frac{8!}{2!\,5!}=168.
$$

**Answer:**

$$
\boxed{
\pi(\theta)=
\begin{cases}
168\theta^2(1-\theta)^5,&0<\theta<1,\\
0,&\text{otherwise.}
\end{cases}}
$$

Check: $3/(3+6)=1/3$ and $18/(9^2\cdot 10)=1/45$.

### 3. Mermaid solution route

~~~mermaid
flowchart TD
  A["P1: Beta prior, mean and variance given"] --> B["S1: Retrieve Beta moment formulas"]
  B --> C["S2: Clear denominator in alpha/(alpha+beta)=1/3"]
  C --> D{"S3: Has a variable actually been isolated?"}
  D -->|"No: alpha still on RHS"| E["REPAIR: collect like terms; 3alpha-alpha=beta"]
  E --> F["beta=2alpha"]
  D -->|"Yes"| F
  F --> G["S4: Substitute into variance"]
  G --> H["S5: Solve alpha=3, beta=6"]
  H --> I["S6: Beta normalizing constant, Gamma/factorials"]
  I --> J["Output PDF and support; check moments"]
  style E stroke:#b45309,stroke-width:3px
~~~

**Known observed break:** At **S3**, becoming committed to isolating $\alpha$ and stopping at an equation where $\alpha$ remained on both sides. The relevant repair is elementary algebra, **not** memorizing a new Beta formula. The diagram marks the precise decision point.

### 4. Dependency and cue trace

| Step | Atomic prerequisite concept (general-purpose node) | Cue to notice | What to do / failure test |
|---|---|---|---|
| S1 | Beta distribution; Expected value; Variance | "Beta", "mean", "variance" | Retrieve the *two* equations linking moments to shape parameters |
| S2 | Clearing denominators; Equivalent equations | Fraction equals $1/3$ | Multiply by the denominator on both sides |
| **S3** | **Collect like terms; Isolate a variable; Substitution strategy** | The same symbol on both sides; two unknowns and two equations | Move like terms; isolate whichever variable yields the simplest one-variable substitute |
| S4 | Algebraic substitution; Powers and cancellation | Known relationship $\beta=2\alpha$ | Replace *every* $\beta$ in the variance equation, including sums and products |
| S5 | Solving linear equations; Multiplication/division | One equation, one unknown | Solve and check positivity |
| S6 | Beta PDF; Gamma function; Factorials | Asked for the "prior pdf", not just $\alpha,\beta$ | Substitute into density, give support, check moments |

**Remediation drill (unscored until attempted independently):** Solve $5a=a+b$, $2a=(a+b)/4$, and $a/(a+b)=2/5$ for whichever variable gives the easiest substitution. State aloud why $a=(a+b)/3$ does *not* isolate $a$.

### 5. Failure-point and retention trace

- **Problem position:** P1 → S3, after $3\alpha=\alpha+\beta$.
- **Observed failure concept:** **Collect like terms** (with adjacent skill: **Choose a substitution variable**).
- **Classification:** Incomplete variable isolation / local goal fixation; *not* an error in Beta-distribution identification.
- **Source of evidence:** The student's earlier words in this conversation (verbatim; original spelling preserved):

> what would the failure of intuition to have around once in 3a=a+b solving for b bc I was tryna get a by itself for some stupid reaason and so had a = a+b/3 and was puzzled why my substitution didn't work

- **Agent note (interpretation, not the student's quoted words):** The retained transformation still has $a$ on the right. Collecting $3a-a=b$ and selecting $b=2a$ avoids a needless loop and makes substitution easier.
- **Existing external attempt reference provided by user:** brain:2026-11-22T18:34:25-08:00:218357. Do **not** append a second row for that event.
- **Mastery status:** not independently demonstrated in this document. Review by solving fresh algebra questions without the model.
- **If logging a future, real attempt:** general node = "Collect like terms"; location = "STAT 132 Discussion 1, Problem 1"; step = "P1.S3"; record actual outcome via brain study log; add exact *full* student words to rep-words.jsonl under brain's returned ref (no paraphrase).

---

## Problem 2 — Exponential likelihood and sketch

### 1. Mathematical statement

Weekly study time $X$ is modeled using an exponential distribution with unknown **rate** $\lambda>0$. Three independent observations are $2$, $2.5$, and $3$ hours. Write $L(\lambda\mid x_1,x_2,x_3)$ and sketch its shape.

$$
X_i\mid \lambda\sim\operatorname{Exp}(\lambda),
\quad f(x\mid\lambda)=\lambda e^{-\lambda x}\mathbf1_{\{x\ge0\}},
\quad \mathbf x=(2,2.5,3).
$$

### 2. Worked solution

**S1 — Identify the rate parameterization.** $\lambda$ has units $\mathrm{hours}^{-1}$; the exponential *mean* is $1/\lambda$.

**S2 — Use independence to multiply the individual densities.**

$$
L(\lambda\mid\mathbf x)
=\prod_{i=1}^3\lambda e^{-\lambda x_i}
=\lambda^3e^{-\lambda\sum_{i=1}^3x_i}.
$$

**S3 — Insert data.**

$$
\sum x_i=2+2.5+3=7.5
\quad\Longrightarrow\quad
\boxed{L(\lambda)=\lambda^3e^{-7.5\lambda}},\ \lambda>0.
$$

**S4 — Find a turning point to guide the sketch.** This optional optimization makes the sketch precise.

$$
\ell(\lambda)=\log L(\lambda)=3\log\lambda-7.5\lambda
$$

$$
\ell'(\lambda)=\frac3\lambda-7.5=0
\quad\Longrightarrow\quad \lambda=0.4.
$$

Since $\ell''(\lambda)=-3/\lambda^2<0$, it is the unique interior maximum.

**Answer/sketch:** $L$ starts at zero as $\lambda\to0^+$, increases to a peak at **$\lambda=0.4$**, then decreases toward zero as $\lambda\to\infty$. The sketch's vertical axis is *likelihood* (not probability of $\lambda$); horizontal axis is rate $\lambda$.

### 3. Mermaid solution route

~~~mermaid
flowchart TD
  A["P2: observed exponential times; asked for likelihood"] --> B{"Is lambda the RATE or mean?"}
  B -->|"Rate"| C["S1: f(x|lambda)=lambda exp(-lambda x)"]
  B -->|"Mean given instead"| D["Convert parameterization first"]
  D --> C
  C --> E["S2: independent observations -> product"]
  E --> F["S3: collect exponent, sum times=7.5"]
  F --> G["L=lambda^3 exp(-7.5lambda)"]
  G --> H["S4: log, differentiate, find maximum"]
  H --> I["Sketch: 0 -> peak at .4 -> 0"]
~~~

### 4. Dependency and cue trace

| Step | Atomic prerequisite concept | Cue | Action |
|---|---|---|---|
| S1 | Exponential distribution; Rate versus mean; Parameter support | Says "rate parameter" | Use $\lambda e^{-\lambda x}$ rather than $e^{-x/\lambda}/\lambda$ |
| S2 | Conditional density; Independence; Likelihood | Three separately observed students | Multiply densities, not sum them |
| S3 | Exponent laws; Sigma/product notation | Repeated $e^{-\lambda x_i}$ | Combine exponents; turn $\lambda\lambda\lambda$ into $\lambda^3$ |
| S4 | Natural logarithms; Product rule or log differentiation; First and second derivatives | "Sketch" and non-monotone positive function | Identify intercept/limits and stationary point |
| Finish | Likelihood versus probability density | Horizontal axis is unknown parameter | Sketch *relative support for parameter values*, not an area-one posterior |

**No observed failure recorded for P2.** Independently test whether the student can start at $f(x\mid\lambda)$, construct $\prod_i f(x_i\mid\lambda)$, and locate the peak.

---

## Problem 3 — Critique a Uniform prior on an exponential rate

### 1. Mathematical statement

$X\mid\lambda\sim\operatorname{Exp}(\lambda)$ for weekly study time. A friend proposes $\lambda\sim\operatorname{Uniform}(0,10)$. Is it a reasonable prior? Explain.

$$
\pi(\lambda)=\begin{cases}
1/10,&0<\lambda<10,\\
0,&\text{otherwise.}
\end{cases}
$$

### 2. Worked reasoning

**S1 — Identify what is being assigned a prior:** $\lambda$ is a *rate per hour*, **not** hours studied. In this model,

$$E[X\mid\lambda]=\frac1\lambda.$$

**S2 — Translate plausible parameter values into real-world implications.** $\lambda=10$ corresponds to mean weekly study time $0.1$ hour (6 minutes); $\lambda=1$ corresponds to 1 hour; $\lambda=0.01$ corresponds to 100 hours. As $\lambda\to0^+$, expected study time becomes arbitrarily large.

**S3 — Distinguish validity from plausibility.** This is a mathematically valid continuous prior; $\Pr(\lambda=0)=0$. Therefore **"it includes zero" is not by itself a valid reason to reject it**. But a uniform rate prior gives equal density near implausibly tiny rates and around much larger rates, and the upper cutoff 10 may be arbitrary.

A useful diagnostic is the implied prior predictive mean:

$$
E_\pi[E[X\mid\lambda]]
=\int_0^{10}\frac1\lambda\frac1{10}\,d\lambda
=\infty.
$$

It allows a sufficiently heavy prior tail on extremely long study times that the overall expected value diverges.

**Answer:** A valid prior, but **often not substantively reasonable** without evidence that the implied study times and hard rate cutoff match the student population. A more informed positive-rate prior (e.g., suitably calibrated Gamma) may be preferable. "Reasonable" is a modeling judgment, not a unique numeric answer.

### 3. Mermaid solution route

~~~mermaid
flowchart TD
  A["P3: Is Uniform(0,10) reasonable for lambda?"] --> B["S1: Lambda is rate, not study hours"]
  B --> C["Convert rate to mean duration: 1/lambda"]
  C --> D{"Does the prior normalize and respect support?"}
  D -->|"Yes"| E["S2: Translate lambda values into hours"]
  D -->|"No"| F["Reject as invalid"]
  E --> G{"Are implied durations and cutoff credible?"}
  G -->|"Questionable"| H["S3: Valid but potentially implausible"]
  G -->|"Supported by context"| I["Could be defensible"]
  H --> J["Explain why; suggest calibrated positive prior"]
  I --> J
~~~

### 4. Dependency and cue trace

| Step | Atomic prerequisite concept | Cue | Action |
|---|---|---|---|
| S1 | Exponential mean; Dimensional analysis | "Rate parameter" | Translate $\lambda$ to $E[X\mid\lambda]=1/\lambda$ |
| S2 | Uniform density; Continuous support; Conditional expectation | Suggested prior interval | Check normalization; convert endpoints and intermediate values to hours |
| S3 | Prior plausibility; Prior predictive reasoning; Improper expectations | "reasonable prior?" | Decide scientific plausibility separately from mathematical validity |
| Finish | Model criticism versus calculation | No observed samples in prompt | Explain in words; no posterior calculation required |

**No observed failure recorded for P3.** Drill: compare uniform-on-*rate* and uniform-on-*mean*, which are not equivalent.

---

## Problem 4 — A discrete prior for two possible defect proportions

### 1. Mathematical statement

The defect proportion $p$ can take **only two possible values**, $0.1$ or $0.2$. Propose a reasonable prior distribution and write $\pi(p)$.

$$p\in\{0.1,0.2\}.$$

### 2. Worked solution

**S1 — Read the parameter space literally.** Even though $p$ is a proportion, here its *prior* is **discrete**, supported on two points.

**S2 — Assign probabilities reflecting beliefs.** With no reason to prefer either possibility, an equal prior is a defensible choice:

$$
P(p=0.1)=\frac12,\qquad P(p=0.2)=\frac12.
$$

**S3 — Write the PMF and check it sums to one.**

$$
\boxed{
\pi(p)=
\begin{cases}
\frac12,&p=0.1,\\
\frac12,&p=0.2,\\
0,&\text{otherwise.}
\end{cases}}
$$

Both probabilities are nonnegative and sum to 1. Other weights $q$ and $1-q$ (for $0\le q\le1$) would also be valid if justified. A continuous $\operatorname{Beta}$ prior over all $0<p<1$ **does not respect this two-value parameter space**.

### 3. Mermaid solution route

~~~mermaid
flowchart TD
  A["P4: p is either .1 or .2"] --> B{"How many allowed values?"}
  B -->|"Two"| C["S1: discrete parameter support"]
  B -->|"Continuum"| D["A continuous prior might be appropriate elsewhere"]
  C --> E{"Evidence favors one value?"}
  E -->|"No"| F["S2: choose equal prior weights"]
  E -->|"Yes"| G["S2: choose justified q and 1-q"]
  F --> H["S3: write PMF pi(p)"]
  G --> H
  H --> I["Verify all mass on .1 or .2; sum=1"]
~~~

### 4. Dependency and cue trace

| Step | Atomic prerequisite concept | Cue | Action |
|---|---|---|---|
| S1 | Sample space; Parameter space; Discrete versus continuous | "Either 0.1 or 0.2" | Restrict support to precisely those two values |
| S2 | Probability mass function; Subjective prior; Symmetry | No prior preference provided | Choose nonnegative weights summing to 1 |
| S3 | Piecewise functions; Normalization | "Write $\pi(p)$" | Include "otherwise 0" and check total mass |
| Finish | Prior vs likelihood vs posterior | No sample data supplied | Stop at prior; do not calculate a posterior |

**No observed failure recorded for P4.** Recognition drill: a proportion need not have a continuous prior.

---

## Problem 5 — Mean and variance from a given prior density

### 1. Mathematical statement

A prior for an unknown defect proportion is given by

$$
\pi(p)=\begin{cases}
2(1-p),&0\le p\le1,\\
0,&\text{otherwise}.
\end{cases}
$$

Find the **prior mean** and **prior variance** of $p$.

### 2. Worked solution

**S1 — Identify the support and check the density is normalized.**

$$\int_0^1 2(1-p)\,dp=[2p-p^2]_0^1=1.$$

**S2 — Compute the first moment.**

$$
E[p]=\int_0^1 p\pi(p)\,dp
=2\int_0^1(p-p^2)\,dp
=2\left(\frac12-\frac13\right)
=\boxed{\frac13}.
$$

**S3 — Compute the second raw moment (not the variance yet).**

$$
E[p^2]=\int_0^1p^2\pi(p)\,dp
=2\int_0^1(p^2-p^3)\,dp
=2\left(\frac13-\frac14\right)
=\frac16.
$$

**S4 — Convert raw moments to variance.**

$$
\operatorname{Var}(p)=E[p^2]-\{E[p]\}^2
=\frac16-\frac19
=\boxed{\frac1{18}}.
$$

**Shortcut/check:** $2(1-p)$ is the density of $\operatorname{Beta}(1,2)$, whose moments also give $1/3$ and $1/18$.

### 3. Mermaid solution route

~~~mermaid
flowchart TD
  A["P5: given prior PDF, find mean and variance"] --> B["S1: read support 0 to 1; check normalization"]
  B --> C{"Recognize Beta(1,2) immediately?"}
  C -->|"Yes"| D["Use Beta moment formulas"]
  C -->|"No / need derivation"| E["S2: integrate p times PDF -> E[p]"]
  E --> F["S3: integrate p^2 times PDF -> E[p^2]"]
  F --> G["S4: Var=E[p^2]-(E[p])^2"]
  D --> H["Check both answers"]
  G --> H
~~~

### 4. Dependency and cue trace

| Step | Atomic prerequisite concept | Cue | Action |
|---|---|---|---|
| S1 | PDF normalization; Definite integration; Support | Piecewise density on $[0,1]$ | Integrate density, confirm area 1 |
| S2 | Expected value of continuous RV; Polynomial integration | "prior mean" | Integrate $p\pi(p)$ |
| S3 | Raw moments; Power rule for integration | "variance" | Integrate $p^2\pi(p)$ separately |
| S4 | Variance identity; Fractions | Have $E[p]$ and $E[p^2]$ | Compute $E[p^2]-(E[p])^2$ |
| Alternative | Beta distribution recognition; Beta moments | PDF proportional to $p^{0}(1-p)^1$ | Recognize $\operatorname{Beta}(1,2)$ as a speed check |

**No observed failure recorded for P5.** Do not confuse the second *raw moment* $E[p^2]$ with the variance.

---

## Shared prerequisite map — reuse these concept nodes across problems

~~~mermaid
flowchart LR
  subgraph Elementary["Elementary algebra"]
    A["Equivalent equations"] --> B["Clear denominators"]
    B --> C["Collect like terms"]
    C --> D["Isolate a variable"]
    D --> E["Substitute into another equation"]
    G["Exponent laws"] --> H["Logarithms"]
    F["Fractions and arithmetic"] --> C
  end
  subgraph Probability["Probability foundations"]
    I["Discrete vs continuous"] --> J["PMF vs PDF"]
    K["Expected value"] --> L["Variance and moments"]
    M["Independence"] --> N["Joint likelihood as a product"]
  end
  subgraph Model["Distribution knowledge"]
    O["Beta family"] --> P["Beta mean and variance"]
    Q["Gamma/factorial"] --> R["Beta normalization"]
    S["Exponential rate"] --> T["Mean duration = 1/rate"]
    S --> U["Exponential density"]
    V["Uniform family"] --> W["Prior plausibility"]
  end
  E --> P1["P1: Beta moment inversion"]
  P --> P1
  R --> P1
  U --> P2["P2: Exponential likelihood and sketch"]
  N --> P2
  G --> P2
  H --> P2
  T --> P3["P3: Prior critique"]
  W --> P3
  I --> P4["P4: Two-point prior"]
  J --> P4
  J --> P5["P5: Prior moments"]
  K --> P5
  L --> P5
  X["Polynomial integration"] --> P5
  style C stroke:#b45309,stroke-width:3px
~~~

**Trace semantics:** A problem depends on concepts through *steps*, not as one opaque success/failure. In particular, a miss at P1.S3 should point to "Collect like terms" and "Isolate a variable"; it should not automatically mark "Beta moments" as failed.

## Problem trace schema (for subsequent actual attempts)

Use this lightweight Markdown metadata under the corresponding problem after **each real independent attempt**. It is for human auditability; it is **not** a second learning ledger.

| Field | Meaning |
|---|---|
| problem | P1–P5 |
| step | S1, S2, …, the specific diagram node |
| node | Exact general-purpose concept name used by the vault graph |
| result | Successful, hint-assisted, or failed — only when actually observed |
| cue_observed | What in the wording/formula should have triggered the method |
| actual_behavior | Faithful description of what was attempted |
| student_words | If present, the student's complete verbatim utterance, in quotes — never a paraphrase |
| agent_note | Interpretation *clearly separate* from the student's words |
| brain_ref | Reference returned by the actual brain study log command, if logged |

### Known attempt record (reference only — do not duplicate)

| problem | step | concept | observed status | existing reference |
|---|---|---|---|---|
| P1 | S3 | Collect like terms | failed at isolating a convenient variable | brain:2026-11-22T18:34:25-08:00:218357 (user-provided) |
| P2–P5 | — | — | not assessed in this note | — |

**Single source of truth:** the vault's System/reps.csv receives each true attempt via brain study log. System/rep-words.jsonl stores exactly spoken or typed words, associated through the *same ref*. A failed problem can expose several candidate prerequisite weaknesses, but add only actually observed, concept-addressed attempt data; do not treat every edge in the dependency graph as a failed rep. System/index/memory.json is generated output from the FSRS-6 replay and should never be hand-edited to "make due dates."

**Review protocol:** (1) attempt the problem without notes, (2) locate the first step you could not independently complete, (3) state the exact recognition cue you missed and the general concept involved, (4) use brain study log to record the real outcome, (5) attach exact original student words in the separate words file using its returned ref, (6) rebuild the vault index using the supported local workflow. If brain is not available through this chat, stop at the worked solution and diagnostic notes; **do not simulate a logged attempt**.

## Recall questions (without viewing solutions)

1. If $\alpha/(\alpha+\beta)=1/3$, how do you choose the easiest variable to isolate? What proves that it is isolated?
2. Why does independence turn $f(x_i\mid\lambda)$ into a product rather than a sum? What happens to the exponents?
3. Why does "Uniform on rate" not mean "Uniform on expected hours"?
4. Why is the prior in P4 a PMF despite $p$ being a proportion?
5. Why must P5 calculate $E[p^2]$ before subtracting $E[p]^2$?

*Status as of 2026-11-22: reference solutions complete; independent mastery not inferred from document creation.*
