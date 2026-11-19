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
- [Atomic checklist](final-atomic-checkpoints.csv) (167 individually testable operations)
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
