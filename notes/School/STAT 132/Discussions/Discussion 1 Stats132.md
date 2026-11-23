---
aliases:
  - "Discussion 1 Stats132"
  - "STAT 132 Discussion 1"
  - "Stats132 Disc 1"
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
completed_problems: [1]
remaining_problems: 4
completed_problem_1_on: 2026-11-22
completion_recorded_at: 2026-11-22T19:28:54-08:00
completion_basis: user-reported
source: "STAT132/files/homework/STAT132 Discussion 01 - priors and likelihoods (W25 worksheet).pdf"
source_repository: "immcnotthere/School"
review_policy: "Do not create attempts from reading this note; only brain study log writes System/reps.csv"
retention_input: "System/reps.csv"
retention_words: "System/rep-words.jsonl"
retention_output: "System/index/memory.json"
last_authored: 2026-11-22
---
# Discussion 1 Stats132

> **Purpose:** One traceable worked example per question: mathematical restatement → worked solution → decision flow → atomic prerequisite concepts → recognition cues. The diagrams describe a *solution route*, not evidence that the student has performed it.

**Source:** [Original 2025 worksheet](https://github.com/immcnotthere/School/blob/main/STAT132/files/homework/STAT132%20Discussion%2001%20-%20priors%20and%20likelihoods%20%28W25%20worksheet%29.pdf). This worksheet was written in Winter 2025 and is being studied in 2026. Descriptions below retain its numerical specifications and mathematical intent; wording is normalized into readable Markdown.

**Progress convention:** "Walkthrough provided" ≠ "independently solved." Q1 has a documented algebraic failure point; Q2–Q5 are not assigned scores by this note. Retention attempts must not be fabricated or appended directly to a CSV.

## Completion and workload tracking

| Problem | Completion status | Date | Basis |
|---|---|---|---|
| **P1** | **Completed** | **2026-11-22** | Student explicitly confirmed completion after obtaining Beta(3,6), with prior correction of intermediate algebra and a permitted formula lookup |
| P2 | Not yet marked complete | — | No completion claim |
| P3 | Not yet marked complete | — | No completion claim |
| P4 | Not yet marked complete | — | No completion claim |
| P5 | Not yet marked complete | — | No completion claim |

**Discussion 1:** 1/5 complete; **4 problems remain**. Across W25 Discussion 1–9, the worksheets contain 41 numbered top-level problems (5, 5, 5, 5, 5, 4, 4, 5, 3). That is **40 minus any other independently completed problems** across Discussions 2–9, whose personal completion has not been verified here; subsections (a), (b), etc. are counted as parts of their numbered problem.

**Time accounting:** Earliest available P1 attempt timestamp from brain's existing reference is 2026-11-22 18:34:25 −08:00; completion was recorded at 19:28:54 −08:00. This is **54 minutes 29 seconds between recorded points**, *not measured focused study time* or a reliable full start-to-finish duration: the actual start predates the logged difficulty, and the conversation included repository, note, and study-system administration. No active-duration value was supplied to or added to brain's ledger.

**Scope:** This is a progress marker in Markdown, **not** an FSRS attempt. No synthetic `brain study log` result, `System/reps.csv` row, or attempt timestamp has been invented. The allowed reference-sheet lookup remains recorded only as a recall observation.

---

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

**S4a — Square every factor inside parentheses.**

$
(3\alpha)^2=3^2\alpha^2=9\alpha^2 \ne 3\alpha^2.
$

This was an observed missed exponent-law step; the original $3\alpha^2$ denominator was corrected before the later fraction manipulation.

**S5 — Solve for the two shape parameters.** One clean route is to cross-multiply:

$
9(3\alpha+1)=90
\ \Longrightarrow\
3\alpha+1=10
\ \Longrightarrow\
\boxed{\alpha=3,\quad\beta=6}.
$

**S5a — Check the algebra if you simplify the fraction first.** Cancelling $\alpha^2$ in S4 and then multiplying by $9/2$ correctly gives

$
\frac1{45}=\frac{2}{9(3\alpha+1)}
\quad\Longrightarrow\quad
\frac1{10}=\frac1{3\alpha+1}.
$

The next legitimate move is to take **reciprocals of the whole nonzero quantities**, giving $10=3\alpha+1$, then subtract 1 and divide by 3. The expression $3\alpha+1$ is *one denominator*. **Multiplying both sides by 3** would give $3/10=3/(3\alpha+1)$, **not** $3/10=1/(\alpha+1)$. If you instead factor out 3 from the denominator, $3\alpha+1=3(\alpha+1/3)$: the constant must be divided too.

**S6 — Retrieve the Beta PDF.** Lecture 1 supplies the formula, and consulting it is permitted for this assignment and the final exam. The student needed to look it up; unaided recall is a worthwhile optional memory goal, **not a solution failure**. The earlier Gamma/Beta slip was a momentary misreading, **not** an observed general distribution-recognition weakness.

**S6a — Formula recall cue.** The family is explicitly given as Beta; refer to [[Beta Distribution]] and optionally practice [[Recall a distribution's PDF|recalling the formula]] without a reference sheet.

**S6b — Normalize the selected Beta density.** Its general formula is

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
  F --> G["S4: Substitute beta into variance"]
  G --> G0{"S4a: Did square apply to BOTH 3 and alpha?"}
  G0 -->|"No: used 3alpha²"| G1["FAILURE 2: Squaring a product"]
  G1 --> G2["REPAIR: (3alpha)² = 9alpha²; cancel alpha²"]
  G0 -->|"Yes"| G2
  G2 --> H0["S5a: Simplify to 1/10 = 1/(3alpha+1)"]
  H0 --> H1{"S5a: Does the operation affect the ENTIRE denominator?"}
  H1 -->|"No: rewrote as 3/10 = 1/(alpha+1)"| H2["FAILURE 2: Changed only 3alpha, not the +1"]
  H2 --> H3["REPAIR: Reciprocal gives 10 = 3alpha+1"]
  H1 -->|"Yes: reciprocal of whole sides"| H3
  H3 --> H["S5: alpha=3, beta=6"]
  H --> I0{"S6a: Can I recall the Beta PDF without notes?"}
  I0 -->|"No: consult allowed Lecture 1 reference"| I1["FORMULA RECALL GAP: optional memory drill"]
  I0 -->|"Yes"| I["S6b: Write and normalize Beta PDF"]
  I1 --> I
  I --> J["Output PDF and support; check moments"]
  style E stroke:#b45309,stroke-width:3px
  style G1 stroke:#b45309,stroke-width:3px
  style H2 stroke:#b45309,stroke-width:3px
  style I1 stroke:#b45309,stroke-width:2px
~~~

**Known observed breaks:** **S3** — becoming committed to isolating $\alpha$ while it remained on both sides. **S4a** — squaring $\alpha$ but not the coefficient 3 in $(3\alpha)^2$. **S5a** — after the correct simplification to $1/10=1/(3\alpha+1)$, treating multiplication by 3 as though it could change just the $3\alpha$ term and leave $+1$ unaffected. The three earlier failures concern elementary algebra. **S6a** records only the allowed reference-sheet lookup and an optional unaided-recall goal. The student clarified that the Gamma/Beta mix-up was a simple misreading; it is **not** recorded as a distribution-recognition failure.

### 4. Dependency and cue trace

| Step | Atomic prerequisite concept (general-purpose node) | Cue to notice | What to do / failure test |
|---|---|---|---|
| S1 | [[Beta Distribution]]; [[Expectation and Variance\|Expected value]]; [[Expectation and Variance\|Variance]] | "Beta", "mean", "variance" | Retrieve the *two* equations linking moments to shape parameters |
| S2 | [[Clearing denominators]]; [[Equivalent equations]] | Fraction equals $1/3$ | Multiply by the denominator on both sides |
| **S3** | **[[Collect like terms]]; [[Isolate a variable]]; [[Substitution strategy]]** | The same symbol on both sides; two unknowns and two equations | Move like terms; isolate whichever variable yields the simplest one-variable substitute |
| S4 | [[Substitution strategy\|Algebraic substitution]]; [[Exponent laws\|Powers and cancellation]] | Known relationship $\beta=2\alpha$ | Replace *every* $\beta$ in the variance equation, including sums and products |
| **S4a** | [[Exponent laws]]; [[Squaring a product]] | $(3\alpha)^2$ has a coefficient **and** a variable inside parentheses | Square both: $(3\alpha)^2=9\alpha^2$, not $3\alpha^2$ |
| **S5a** | **[[Equivalent equations]]; [[Fractions with compound denominators]]; [[Distributive Law\|Distributive property]]** | $1/10=1/(3\alpha+1)$ and the urge to "multiply by 3" | Treat $3\alpha+1$ as one unit; a factor removed from a sum must apply to **both** terms. Easier cue: take reciprocals first. |
| S5 | [[Solving linear equations]]; [[Fractions and Decimals\|Multiplication/division]] | One equation, one unknown after reciprocal | Subtract 1, then divide by 3; check positivity |
| **S6a** | [[Beta Distribution]]; [[Recall a distribution's PDF]] | Allowed formula sheet available, but no unaided retrieval | Consult Lecture 1 as permitted; separately drill tabula-rasa recall |
| S6b | [[Beta Distribution\|Beta PDF]]; [[Gamma and Beta Functions\|Gamma function]]; [[Factorial\|Factorials]] | Asked for the "prior pdf", not just $\alpha,\beta$ | Substitute into Beta density, give support, check moments |

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

#### Failure point 2 — P1.S4a: Squaring a product

- **Date observed:** 2026-11-22. Exact time of this specific chat attempt is not established.
- **Position:** P1.S4a, after correctly substituting $\beta=2\alpha$.
- **General skill:** [[Squaring a product]]; [[Exponent laws]].
- **Missed cue:** Parentheses around a product: $(3\alpha)^2$ squares both 3 and $\alpha$.
- **Student's exact words (full and unedited):**

> Okay, so back to the problem. So we substitute in beta is equivalent to two alpha. And then we have the problem as two alpha squared, three alpha squared over, excuse me, two alpha squared over three alpha squared times three alpha plus one. Is that correct?

- **Agent note:** The denominator was stated with $3\alpha^2$, omitting the square on the coefficient 3. The student was otherwise correctly substituting $\beta=2\alpha$.
- **Brain ledger status:** Not logged here. No attempt ref exists for this observation; retain only the date and quote until an actual brain study log event is created.

#### Failure point 3 — P1.S5a: Operating on a compound denominator

- **Problem position:** P1 → S5a, after cancellation and the correct step $1/10=1/(3\alpha+1)$.
- **Observed concept to drill:** **Distributive property** (related: **Equivalent equations**, **Fractions with compound denominators**).
- **Classification:** Selective operation on part of a sum / failure to preserve equality while manipulating a denominator. Do not classify as an error in Beta moments, substitution, or cancelling $\alpha^2$: those were performed correctly.
- **Cue missed:** Parentheses in $1/(3\alpha+1)$ mean that $3\alpha+1$ is a single denominator; an operation on that denominator must affect **both terms**. From $1/10=1/(3\alpha+1)$, reciprocal of both sides immediately gives $10=3\alpha+1$.
- **Student's exact words (verbatim, full statement; no editorial edits):**

> Did we get seven over three? I don't think that's right. Here's my math. We have two over nine after we cancel out the alpha squares. I just say when I get rid of them for now. So we multiply by nine and we get nine over forty-five. Then we divide by two. We divide by two. We get nine over ninety. That gives us one tenth. We then have one over three alpha plus one. We then multiply the entire equation by three. We get three tenths. And then we have three tenths is equivalent to one over alpha plus one. We take the reciprocal of both. So now we have ten over three is equivalent to alpha plus one. We subtract one from both sides, giving us seven over three is equivalent to alpha

- **Agent note (interpretation, separate from student's words):** The student correctly reached $1/10=1/(3\alpha+1)$ but then inferred $3/10=1/(\alpha+1)$. Multiplying the entire equality by 3 would instead yield $3/10=3/(3\alpha+1)$; factoring $3$ from $3\alpha+1$ gives $3(\alpha+1/3)$, not $3(\alpha+1)$. The shortest correction is to take reciprocals, then collect like terms.
- **Retention status:** Diagnostic failure documented **in this Markdown trace only**; **no new** brain study log event or System/reps.csv row has been created. If a logged event is added with brain locally, use its actual returned ref when attaching these exact words in System/rep-words.jsonl; do not invent a timestamp or reference.
- **Unscored remedial drill:** Transform $1/7=1/(2x+3)$, $4/(6x+2)=1/5$, and $1/(4x+2)=1/10$ using whole-expression operations. Distinguish multiplying a fraction from dividing a sum by a constant.
#### Formula lookup and optional recall — P1.S6a

- **Date observed:** 2026-11-22; the precise time of the utterance is not established.
- **Position:** P1.S6a only: retrieval of the named Beta density.
- **General skill:** [[Recall a distribution's PDF]]. Needed to look up the density in Lecture 1; **lookup is permitted**, so this is an independent-recall observation rather than an error.
- **Student clarification:** The Gamma/Beta mix-up was a momentary misreading, not a general failure to distinguish distribution families. **Do not log it as distribution recognition.**
- **Student's exact original words (full, unchanged):**

> Okay, so I did have to look at lecture one to get the distribution, which is allowed because I will have those distributions provided to me on the final on all homeworks. But it's still good to have it memorized. So just list the fact that I wasn't able to auto-generate that information. I inputted six to the third x three minus one, so two. And then e to the x six over the gamma of three, or gamma function of three, which is proportional to x squared e minus six x, or e to the minus, or the negative six x. And then that six to the third is, let's see, 36 times six is 18 216. So 216. That's a scalar if there ever was one. But it's six to the three. I think I've gotten that right, haven't I?

- **Agent note (interpretation, not student's words):** Consulting the allowed reference establishes only that unaided recall was not demonstrated. The student's later correct Beta kernel $x^2(1-x)^5$ confirms the requested PDF form. The earlier misreading is deliberately **excluded** from the failed-skill ledger.
- **Retention status:** Documented here only; no new brain study log entry or System/reps.csv row created.

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
| S1 | [[Exponential Distribution]]; [[Exponential Distribution\|Rate versus mean]]; [[Support (Probability)\|Parameter support]] | Says "rate parameter" | Use $\lambda e^{-\lambda x}$ rather than $e^{-x/\lambda}/\lambda$ |
| S2 | [[Conditional PDF\|Conditional density]]; [[Independence of Random Variables\|Independence]]; [[Likelihood Function\|Likelihood]] | Three separately observed students | Multiply densities, not sum them |
| S3 | [[Exponent laws]]; [[Sigma and product notation]] | Repeated $e^{-\lambda x_i}$ | Combine exponents; turn $\lambda\lambda\lambda$ into $\lambda^3$ |
| S4 | [[Natural logarithms]]; [[Log-Likelihood\|Product rule or log differentiation]]; [[Basic Derivative Formulas\|First and second derivatives]] | "Sketch" and non-monotone positive function | Identify intercept/limits and stationary point |
| Finish | [[Likelihood Function\|Likelihood versus probability density]] | Horizontal axis is unknown parameter | Sketch *relative support for parameter values*, not an area-one posterior |

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
| S1 | [[Exponential Distribution\|Exponential mean]]; [[Dimensional analysis]] | "Rate parameter" | Translate $\lambda$ to $E[X\mid\lambda]=1/\lambda$ |
| S2 | [[Uniform Distribution (Continuous)\|Uniform density]]; [[Support (Probability)\|Continuous support]]; [[Conditional expectation]] | Suggested prior interval | Check normalization; convert endpoints and intermediate values to hours |
| S3 | [[Prior Distribution\|Prior plausibility]]; [[Prior predictive reasoning]]; [[Improper expectations]] | "reasonable prior?" | Decide scientific plausibility separately from mathematical validity |
| Finish | [[Model criticism versus calculation]] | No observed samples in prompt | Explain in words; no posterior calculation required |

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
| S1 | [[Sample Space]]; [[Parameter Space]]; [[Discrete vs Continuous Random Variable\|Discrete versus continuous]] | "Either 0.1 or 0.2" | Restrict support to precisely those two values |
| S2 | [[Probability Mass Function]]; [[Prior Distribution\|Subjective prior]]; [[Symmetry]] | No prior preference provided | Choose nonnegative weights summing to 1 |
| S3 | [[Piecewise functions]]; [[Normalizing Constant\|Normalization]] | "Write $\pi(p)$" | Include "otherwise 0" and check total mass |
| Finish | [[Data Model vs Prior Model\|Prior vs likelihood vs posterior]] | No sample data supplied | Stop at prior; do not calculate a posterior |

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
| S1 | [[PMF, PDF and CDF\|PDF normalization]]; [[Definite integration]]; [[Support (Probability)\|Support]] | Piecewise density on $[0,1]$ | Integrate density, confirm area 1 |
| S2 | [[Expectation of a Continuous Random Variable\|Expected value of continuous RV]]; [[Polynomial integration]] | "prior mean" | Integrate $p\pi(p)$ |
| S3 | [[Moments and Central Moments\|Raw moments]]; [[Power rule for integration]] | "variance" | Integrate $p^2\pi(p)$ separately |
| S4 | [[Expectation and Variance\|Variance identity]]; [[Fractions and Decimals\|Fractions]] | Have $E[p]$ and $E[p^2]$ | Compute $E[p^2]-(E[p])^2$ |
| Alternative | [[Beta Distribution\|Beta distribution recognition]]; [[Prior Parameters from Mean and Variance\|Beta moments]] | PDF proportional to $p^{0}(1-p)^1$ | Recognize $\operatorname{Beta}(1,2)$ as a speed check |

**No observed failure recorded for P5.** Do not confuse the second *raw moment* $E[p^2]$ with the variance.

---

## Obsidian prerequisite links and missing-note queue

Every skill in the five step-level prerequisite tables above is an **Obsidian wikilink**. A blue link opens a concept note when present; an unresolved link offers to create that **general, reusable** concept note in Obsidian. This does not mean the student has failed that skill; only observed failures are counted in the attempt trace.

**Existing concept notes referenced (24):** [[Basic Derivative Formulas]], [[Beta Distribution]], [[Conditional PDF]], [[Data Model vs Prior Model]], [[Discrete vs Continuous Random Variable]], [[Distributive Law]], [[Expectation and Variance]], [[Expectation of a Continuous Random Variable]], [[Factorial]], [[Fractions and Decimals]], [[Gamma and Beta Functions]], [[Independence of Random Variables]], [[Likelihood Function]], [[Log-Likelihood]], [[Moments and Central Moments]], [[Normalizing Constant]], [[PMF, PDF and CDF]], [[Parameter Space]], [[Prior Distribution]], [[Prior Parameters from Mean and Variance]], [[Probability Mass Function]], [[Sample Space]], [[Support (Probability)]], [[Uniform Distribution (Continuous)]].

**Concept links awaiting dedicated notes (22):** [[Clearing denominators]], [[Collect like terms]], [[Conditional expectation]], [[Definite integration]], [[Dimensional analysis]], [[Equivalent equations]], [[Exponent laws]], [[Exponential Distribution]], [[Fractions with compound denominators]], [[Improper expectations]], [[Isolate a variable]], [[Model criticism versus calculation]], [[Natural logarithms]], [[Piecewise functions]], [[Polynomial integration]], [[Power rule for integration]], [[Prior predictive reasoning]], [[Sigma and product notation]], [[Solving linear equations]], [[Squaring a product]], [[Substitution strategy]], [[Symmetry]].

**Highest-priority missing notes, based on demonstrated breakdowns:** [[Collect like terms]] → [[Equivalent equations]] → [[Fractions with compound denominators]], plus [[Squaring a product]] and [[Recall a distribution's PDF]]. The repository already has [[Distributive Law]]; use that established general concept for the S5a failure rather than inventing a second near-duplicate.

**How to create notes:** Click an unresolved wikilink in Obsidian; make the concept reusable across courses, add `aliases` in its YAML frontmatter, and add its own prerequisite links. Do **not** create another note named after a specific Problem 1 step.

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

## Embedded dated failure history (CSV)

This is the **in-document CSV trace**, not the live FSRS input file. Each row identifies the **general skill**, the exact problem and flowchart step, the observed outcome, the date, a ledger reference *only when actually known*, the student's **complete unedited words** in `said`, and the separate agent interpretation in `agent_note`. No original attempt time has been invented for S4a, S5a, or S6a/S6.

```csv
date,problem,step,node,outcome,ledger_ref,ledger_status,said,agent_note
2026-11-22,P1,S3,Collect like terms,failed,brain:2026-11-22T18:34:25-08:00:218357,existing brain record; do not duplicate,what would the failure of intuition to have around once in 3a=a+b solving for b bc I was tryna get a by itself for some stupid reaason and so had a = a+b/3 and was puzzled why my substitution didn't work,Isolated alpha only partially and overlooked beta=2alpha when collecting like terms from 3alpha=alpha+beta.
2026-11-22,P1,S4a,Squaring a product,failed,,markdown only; not logged,"Okay, so back to the problem. So we substitute in beta is equivalent to two alpha. And then we have the problem as two alpha squared, three alpha squared over, excuse me, two alpha squared over three alpha squared times three alpha plus one. Is that correct?",After substituting beta=2alpha the denominator used 3alpha-squared where (3alpha)^2 requires squaring both factors to get 9alpha-squared.
2026-11-22,P1,S5a,Distributive Law,failed,,markdown only; not logged,"Did we get seven over three? I don't think that's right. Here's my math. We have two over nine after we cancel out the alpha squares. I just say when I get rid of them for now. So we multiply by nine and we get nine over forty-five. Then we divide by two. We divide by two. We get nine over ninety. That gives us one tenth. We then have one over three alpha plus one. We then multiply the entire equation by three. We get three tenths. And then we have three tenths is equivalent to one over alpha plus one. We take the reciprocal of both. So now we have ten over three is equivalent to alpha plus one. We subtract one from both sides, giving us seven over three is equivalent to alpha","Correctly simplified to 1/10=1/(3alpha+1) but rewrote 3/10=1/(alpha+1), selectively altering a term inside the denominator; the valid shortcut is to take reciprocals."
2026-11-22,P1,S6a,Recall a distribution's PDF,reference consulted (permitted); independent recall not demonstrated,,markdown only; not logged,"Okay, so I did have to look at lecture one to get the distribution, which is allowed because I will have those distributions provided to me on the final on all homeworks. But it's still good to have it memorized. So just list the fact that I wasn't able to auto-generate that information. I inputted six to the third x three minus one, so two. And then e to the x six over the gamma of three, or gamma function of three, which is proportional to x squared e minus six x, or e to the minus, or the negative six x. And then that six to the third is, let's see, 36 times six is 18 216. So 216. That's a scalar if there ever was one. But it's six to the three. I think I've gotten that right, haven't I?","Allowed reference consulted; unaided PDF recall was not demonstrated. Student clarified Gamma/Beta slip was a simple misreading, not a general distribution-recognition failure; student later correctly supplied the Beta kernel x^2(1-x)^5."
```

**How to use:** Keep this table in the present Markdown note as an audit and transcription record. The one previously logged attempt (**P1.S3**) has its real brain `ref` and must not be entered twice. **P1.S4a** and **P1.S5a** are algebra difficulties; **P1.S6a** is a reference-sheet lookup observation, not a failure. None has been logged via brain here; the momentary Gamma/Beta misreading is excluded. to affect the forgetting curve, record each actual attempt through the local `brain study log` workflow and associate its returned reference with verbatim words. Simply displaying these CSV rows inside Obsidian does **not** update `System/reps.csv` or `System/index/memory.json`. Do not copy these rows directly into the ledger: their schema is richer than brain's input and exact original timestamps are missing.

**Skill linkage:** [[Collect like terms]] (S3), [[Squaring a product]] (S4a), [[Distributive Law|Distributive property]] + [[Fractions with compound denominators]] (S5a), and [[Recall a distribution's PDF]] (S6a). Each corresponds to a specific decision node in the P1 Mermaid chart and can be drilled across assignments.

---

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
| P1 | S4a | Squaring a product | omitted square on coefficient; observed in chat, not logged | none — no attempt ref |
| P1 | S5a | Distributive property | selectively changed a compound denominator; documented, not logged | none — needs an actual brain study log event |
| P1 | S6a | Recall a distribution's PDF | allowed formula lookup; no family-recognition failure recorded | none — documented only |
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
