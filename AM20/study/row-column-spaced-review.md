# AM 20 — Retrieval practice: row × column multiplication

Status: **Needs spaced review** (2026-11-18).

## Conceptual Step 02 — Matrix representation
- Step 01, converting second- and third-order homogeneous ODEs to first-order systems: **mastered in chat**.
- Step 02, translating the system to matrix form: **in progress**.
- Observed error: for x₁′ = x₂ and x₂′ = x₃, wrote rows [1,0,0] and [1,0,0] rather than [0,1,0] and [0,0,1]. Third row [-4,-3,-2] was correct.
- Underlying retrieval target: **row × column rule**: dot each matrix row with the vector, multiplying corresponding entries and summing.
- Do not mark mastered until independent cold recall.

## Spaced-retrieval prompts
1. Compute [2,3] · [4,5]ᵀ without hints.
2. Multiply a 2×3 matrix by a 3×1 column vector, writing both output entries.
3. Given x₁′=x₂, x₂′=x₃, x₃′=-4x₁-3x₂-2x₃, construct P in x′=Px.
4. Reverse the process: expand a supplied 3×3 P into three scalar equations.
5. Explain why row [0,1,0] selects x₂ rather than x₁.

## Mastery criteria
Two correct cold attempts on different days, including one ODE-to-matrix translation and one numerical row-by-column multiplication. If incorrect, explain the mismatch and repeat with changed numbers. Keep tutoring incremental and one problem at a time.

## Conceptual Step 03 — Vector-valued functions and derivative notation (2026-11-18)
**Explicit prerequisite skill: do not assume this is implicit knowledge.**

- A vector-valued function is a column of scalar functions: **x(t) = [f(t), g(t)]ᵀ**.
- Its derivative is taken componentwise: **x′(t) = [f′(t), g′(t)]ᵀ**.
- In **x′ = Px**, each row of P gives the instantaneous rate of change of the corresponding component; it does **not** give the component's current value.
- Worked example: P = [[2,1],[0,-3]], x(t) = [f(t),g(t)]ᵀ implies **f′(t) = 2f(t)+g(t)** and **g′(t) = -3g(t)**.
- Observed gap: correctly computed the right-hand expressions “2f+g; -3g” but initially wrote them as x′ rather than labeling the two component derivatives f′ and g′. After explanation, the user said this made sense and requested it be explicitly saved as a knowledge step.
- Conceptual distinction: the state x(t) is the collection of values; x′(t) is the collection of rates. The rate of f depends on both f and g here (coupling), whereas the rate of g depends only on g.
- **Status: passed independently in session (2026-11-18); cold retention not yet tested.**

### Step 03 retrieval check
Given x(t)=[u(t),v(t)]ᵀ and P=[[1,-4],[3,2]], write both scalar derivative equations with correct left-hand notation, then identify whether u′ depends on v. Require an unaided answer before marking mastery.

## Conceptual Step 04 — Linearity and homogeneity (2026-11-18)
- Independently distinguished linear homogeneous examples (A) from dependent-variable squares and independent forcing terms.
- Correct reasoning: `t²u` and `sin(t)u` are linear in dependent variables despite time-varying coefficients; `u²` or `uv` is nonlinear.
- Explained teacher correction: `v'=u+5` is **linear but nonhomogeneous**, and requires an additive forcing vector `g(t)`.
- **Status: passed in session; ask for cold classification on later date.**

## Conceptual Step 05 — Zero solution and superposition (2026-11-18)
- Independently answered that derivative of an identically zero vector is zero; thus `x'=P(t)x` holds for the zero solution.
- Asked to find derivative of `y(t)=3x(t)`; no answer yet. Superposition **must not** be marked mastered.
- **Status: zero-solution substep passed; constant-scaling/sum proof in progress.**

## Link to final skills tracker
- [Atomic checklist](final-atomic-checkpoints.csv) (168 individually testable operations)
- [Lecture 18 Equations (3)–(5), notation-reading lesson + H21 retrieval drill](lecture18-reading-systems-notation.md)
- [Reconciled scope and original 121-node graph](final-concept-reconciliation.md)

## Conceptual Step 04a — General vs autonomous systems (logged 2026-11-18 15:56 PST; approximate session timestamp)
- **General / potentially time-dependent system:** \(\mathbf{x}'=\mathbf F(t,\mathbf x)\). The rule may depend explicitly on time \(t\) as well as the current state \(\mathbf x\). Example: \(x'=tx+x^2\).
- **Autonomous system:** \(\mathbf{x}'=\mathbf F(\mathbf x)\). The rule does **not** explicitly contain time. Example: \(x'=x^2\). Its solution \(x(t)\) can still change over time.
- **Vector shorthand:** \(\mathbf x=[x_1,\ldots,x_n]^T\); writing \(F(t,x_1,\ldots,x_n)\) lists each component of the state, while \(F(t,\mathbf x)\) abbreviates them.
- **Nuance:** \(F(t,\mathbf x)\) is a notation broad enough to include autonomous rules; the mere appearance of \(t\) in an argument list does not prove that a particular rule explicitly depends on time.
- **Observed learning need:** User asked why the textbook wrote \(t,x_1,\ldots\) instead of just \(x\), then asked whether “general” and “autonomous” needed memorization. Explained that recognizing explicit time dependence matters, but the terminology is not yet a priority.
- **Status:** introduced/explained, **not independently tested**; do not mark passed or mastered. Prioritize conceptual recognition over jargon.

### Step 04a timestamped retrieval drill
1. **2026-11-18 15:56 PST — introduction, not a scored attempt.** Ask: In \(x'=t+x^2\), does the rule explicitly depend on time? Why?
2. **Next cold attempt (timestamp when answered):** Compare \(x'=2x\) with \(x'=tx\). Which is autonomous? What does \(t\) change?
3. **Later cold attempt (timestamp when answered):** Explain in one sentence why \(x'=F(x)\) may still have a changing \(x(t)\).
4. **Notation check (timestamp when answered):** If \(\mathbf x=[x_1,x_2]^T\), rewrite \(F(t,x_1,x_2)\) using vector shorthand.

**Scoring:** Record exact attempt time, response, correctness, hint level, and next review due date. Only count an independent correct response as a pass; require a later cold retest for retention.

## Step 04b — Equation-reading fluency (2026-11-18, ~16:56 PST)
- **New counted atomic checkpoint H21:** Translate `x_i'=a(t)x_1+b(t)x_2` aloud, identifying whose rate is on the left, whose present values are on the right, and the signs of the two contributions.
- Guided answers for `x_1'=3x_1+2x_2` and `x_2'=-x_1-0.125x_2` showed partial understanding but confusion between state variables and “inverse correlation” phrasing. **Status: in progress; not passed.**
- [Read the full saved lesson and drilling instructions](lecture18-reading-systems-notation.md) before the next tutoring session. Prioritize this fluency check before jumping to superposition/eigenvalues.


## Lecture 18.2 — Superposition and dependence (observed 2026-11-18, around 17:57 PST)

**Theorem in plain language:** If two vector functions solve the same homogeneous linear system, any constant-weighted sum of them also solves that system. Superscript labels \(x^{(1)}\), \(x^{(2)}\) name whole solution vectors, unlike subscripts \(x_1,x_2\), which name their components.

**Evidence and limits:** Student independently differentiated \(3e^{2t}\) to get \(6e^{2t}\), recognized the equality \(y'=2y\), and independently reconstructed the scalar proof for \(h=3f+2g\), \(f'=4f\), \(g'=4g\): \(h'=3(4f)+2(4g)=4h\). Ask to write the intermediate factorization \(4(3f+2g)\). This is a **scalar in-session pass**, not a demonstration of vector/matrix superposition or delayed mastery. H16 and H17 remain in progress in the atomic register pending vector transfer and cold testing.

**Student's definition:** A combination of functions inherits a property of its constituent functions. Refine to: a **linear combination** inherits the specific property of **solving the same homogeneous linear equation**, not every property.

**Misconception to drill:** Student predicted superposition would still work for \(f'=4f+1,\ g'=4g+1\) because "you just added a constant." Counterexample \(h=f+g\) gives \(h'=4h+2\), not \(4h+1\). Difference \(f-g\) has derivative \(4(f-g)\): the forcing cancels, so it solves the associated homogeneous equation, *not* the original nonhomogeneous equation. Student explicitly requested more intuition and slower symbol-reading rather than more superficial repetition.

**Dependence check, after introducing fundamental sets:** For \(f=e^t\) and \(g=3e^t\), student independently answered \(g=3f\). **Passed recognition in-session**, but not cold-retained. Explain these two functions are linearly dependent because one is a constant multiple of the other. Next step: contrast \(e^t\) and \(e^{-t}\) without assuming their independence is obvious.

### Next one-at-a-time drills
1. Explain the words "linear combination" and "same homogeneous linear system" without algebra.
2. For \(h=2f-g\), \(f'=3f\), \(g'=3g\), derive \(h'=3h\) without hints, showing the factorization.
3. For \(f'=3f+2,\ g'=3g+2\), find the exact differential equation satisfied by \(h=f+g\), and explain why it is not the original.
4. Move from scalar \(f,g\) to 2-component solution **vectors**, clearly distinguishing solution labels \(x^{(1)}\) from component labels \(x_1\).
5. Recognize linear dependence \(g=3f\); then investigate a pair not related by constant multiplication. Test independence and fundamental sets only after notation is clear.

**Mastery rule:** Credit current in-session scalar proof but retain H16/H17 as in-progress for the actual systems theorem; do not award full Lecture 18.2 mastery until vector proof and delayed independent retrieval.


## Memorization bundle — Lecture 18.2: linear independence by ratio (2026-11-18; session)

**Why this is being drilled:** Distinguish a constant multiple (dependent solutions) from a time-varying ratio (independent functions). This is preparatory for fundamental sets and the Wronskian, not evidence of mastered systems theory.

**Rule to retrieve from memory:** For two functions \(f,g\), where \(f\neq0\) on the interval, ask whether \(g(t)/f(t)\) is **one constant for every \(t\)**. If so, \(g=cf\) and the pair is linearly dependent. If the ratio changes with \(t\), they cannot be constant multiples and are linearly independent. This quick ratio test is for a pair of scalar functions; later, use determinant/Wronskian for systems of vector solutions.

**Worked pair, exactly as taught:**
\[
f(t)=e^t,\qquad g(t)=e^{-t},\qquad
\frac{g(t)}{f(t)}=\frac{e^{-t}}{e^t}=e^{-2t}.
\]
Since \(e^{-2t}\) varies with time, there is no fixed constant \(c\) with \(g=cf\) for all \(t\), so \(f\) and \(g\) are linearly independent.

**Contrast:** If \(f(t)=e^t\), \(g(t)=3e^t\), then \(g/f=3\), constant, so they are linearly dependent.

**Student evidence:** Correctly said the ratio changes, also observed \(\ln f=-\ln g\), which is true for this positive pair but does **not** prove dependence. Correctly substituted \(c_1=2,c_2=-3\) into \(y=c_1e^t+c_2e^{-t}\) to obtain \(y=2e^t-3e^{-t}\). Recognition correct in-session; **no cold retrieval tested**.

### Spaced memorization prompts (ask one at a time, without displaying the answer)
1. For \(f=e^t\) and \(g=e^{-t}\), calculate \(g/f\). Why does its dependence on \(t\) settle the test?
2. For \(f=e^{2t}\) and \(g=7e^{2t}\), are the two functions linearly dependent? Name the constant.
3. For \(f=e^{2t}\) and \(g=e^{-3t}\), determine independence using only the ratio.
4. Explain why \(\ln f=-\ln g\) is **not** evidence that \(g=cf\) for some constant \(c\).
5. If \(y=c_1e^t+c_2e^{-t}\), substitute \(c_1=2,\ c_2=-3\) correctly and describe what the constants do.

**Scheduling:** First future cold review after a delay, then on a later day with new coefficients. Timestamp each actual attempt, record independent/guided correctness, and do not mark cold mastery without successful recall. Keep separate from superposition theorem proof and from fundamental matrix/ Wronskian criteria.


## Lecture 18.2 — Wronskian entry check (2026-11-18, evening PST)

**Prompt shown:** Compute the determinant of the 2×2 matrix with rows \([1,2]\) and \([3,4]\), then interpret nonzero as independence.

**Independent student answer:** “-2 so lin ind.” Correct: \(W=\det\begin{bmatrix}1&2\\3&4\end{bmatrix}=1\cdot4-2\cdot3=-2\neq0\). Thus its two column vectors are linearly independent.

**Assessment distinction:** G08 (calculate a 2×2 determinant) **passed in session**. J10 (Wronskian/determinant test for a time-dependent fundamental set) **in progress**; a constant numerical matrix is an entry-level prerequisite, not full independent computation and interpretation of the Wronskian \(W(t)\) of actual solution vectors throughout an interval. No delayed/cold retention measured.

**Next H/J drill:** Given two explicitly supplied solution vectors \(\mathbf x^{(1)}(t)=[e^t,0]^T\), \(\mathbf x^{(2)}(t)=[0,e^{-t}]^T\), form the matrix with those vectors as *columns*, then compute its determinant as a function of \(t\). After that, interpret nonzero for all \(t\). Ask one step at a time and do not show the solution beforehand.

**Coverage reminder:** Superposition and dependence understood on scalar examples; vector-system proof and Wronskian application still need demonstrations. Avoid treating “we covered Wronskians” as entire-topic mastery.
