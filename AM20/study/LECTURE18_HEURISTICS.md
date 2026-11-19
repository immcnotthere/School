# AM 20 — Lecture 18 heuristics, mathematical recipes and persistent confusions

**Compiled 2026-11-19 (PST)** from the November 18 session and instructor-supplied Lecture 18 supplemental problem text. Use alongside [resume guide](LECTURE18_RESUME.md) and [original PDF](../files/lectures/AM20%20Lecture%2018%20-%20practice%20problems.pdf).

## A. Teaching rules established in chat

1. **One meaningful step per question.** Ask for one rearrangement, product, determinant or component derivative, then advance. The student favors completing the actual sheet over extended review and abstract tangents.
2. **Distinguish doing algebra from grasping the mathematical object.** The student calculated Wronskians correctly before comfortably explaining “both vectors solve the same system.”
3. **Treat plain-English interpretation as a separate retrieval skill.** Avoid overly compressed phrases like “two-dimensional homogeneous linear system” without specifying differential equations when the derivative context matters.
4. **Treat the student's language corrections seriously.** A fundamental set is *not merely a better set*; it is a collection of independent solutions that spans the solution space.
5. **Do not overaward mastery.** Reading an instructor solution, guided correction, or answering a scalar version does not independently establish vector transfer, delayed retention, or exam readiness.
6. **Timestamp answers as they arrive** in PST/PDT. Prior GitHub commit times are reliable *save times*, not exact student answer times.

## B. Symbol interpretation crib

| Symbol | Spoken meaning |
|---|---|
| \(x_1(t)\), \(x_2(t)\) | Current values of state variables 1 and 2 |
| \(x_1'\), \(x_2'\) | Their respective **rates of change**, not their current values |
| \(\mathbf x(t)\) | Entire time-dependent state **vector function** |
| \(\mathbf x'=[x_1',x_2']^T\) | Differentiate **componentwise** |
| \(\mathbf x'=P(t)\mathbf x\) | Homogeneous linear **differential** system: the state determines its rates |
| \(\mathbf x'=P(t)\mathbf x+\mathbf g(t)\) | Linear *nonhomogeneous* system if \(\mathbf g\ne0\) |
| \(p_{ij}(t)\) | Matrix row i, column j; coefficient of \(x_j\) in equation for \(x_i'\) |
| \(\mathbf x^{(1)}\), \(\mathbf x^{(2)}\) | Different **whole candidate solution functions**, labelled by superscript in parentheses |
| \(x_i\) | Component i of one solution function |
| \(F(t,\mathbf x)\) | Rule may depend explicitly on time and state; autonomous case has no explicit time dependence |
| \(\mathbf x(t_0)=\mathbf x^0\) | Starting values at t0, **not** initial derivatives |

**Observed confusion H21:** In \(x_2'=-x_1-0.125x_2\), say “the **rate of change of variable 2** has negative contributions from the values of variables 1 and 2.” Do not say “inverse correlation” or assume both states are physical positions.

## C. Conversion and matrix recipes (supp. 1–3, 9)

For a second-order homogeneous constant-coefficient equation \(y''+ay'+by=0\):
\[
x_1=y,\quad x_2=y',\qquad
\begin{bmatrix}x_1'\\x_2'\end{bmatrix}=
\underbrace{\begin{bmatrix}0&1\\-b&-a\end{bmatrix}}_A
\begin{bmatrix}x_1\\x_2\end{bmatrix}.
\]

Third order \(y'''+a_2y''+a_1y'+a_0y=0\):
\[
A=\begin{bmatrix}0&1&0\\0&0&1\\-a_0&-a_1&-a_2\end{bmatrix}.
\]

**Matrix-row heuristic:** Matrix rows encode derivatives. Row \([0,1,0]\) times \([x_1,x_2,x_3]^T\) equals \(x_2\), not \(x_1\). Wrong shift rows were actually observed and corrected; cold retest still due.

**Reverse conversion (Problem 3):** If \(x_1'=a x_1+b x_2,\ x_2'=c x_1+d x_2\) with \(b\ne0\), isolate \(x_2=(x_1'-ax_1)/b\), differentiate, substitute \(x_2\) and \(x_2'\) into the second equation, collect a second-order ODE in \(x_1\). Compare characteristic polynomial with \(\det(A-rI)\) as a check. **On resume, the student has not yet answered the very first isolation step.**

## D. What “solves the same system” really means (H23)

A **single** vector-valued function solves a system if, when its components are plugged into the state equations and their derivatives computed, **every equation holds for all t on the interval**.

For \(x_1'=x_1,\ x_2'=-x_2\), \([e^t,0]^T\) is a solution *by itself* because \(x_1'=e^t=x_1,\ x_2'=0=-x_2\). So is \([0,e^{-t}]^T\). Each one separately solves the same pair of ODEs.

**Verification algorithm:** Compute \(\mathbf x'(t)\); compute \(A\mathbf x(t)\); compare both components. **Nonzero Wronskian cannot substitute for this verification.**

A **particular solution** is one valid function. A **general solution** gives *all* possible solutions, typically \(\sum_i c_i\mathbf x^{(i)}(t)\) for a fundamental set.

## E. Superposition and homogeneous forcing boundary (H16–H17)

For \(f'=Pf,\ g'=Pg\), constant weights \(a,b\) produce
\[
(af+bg)'=aPf+bPg=P(af+bg).
\]
The functions inherit the **specific property of satisfying the same homogeneous linear differential equation**, not every property of the constituent functions.

**Student's independent scalar proof:** \(f'=4f,\ g'=4g,\ h=3f+2g\) implies \(h'=3(4f)+2(4g)=4h\). This is **not yet an independent vector-level proof**.

**Necessary counterexample:** If \(f'=4f+1\) and \(g'=4g+1\), then \(h=f+g\) gives \(h'=4h+2\), not \(4h+1\). Conversely \(f-g\) solves the **associated homogeneous equation** because the added +1 terms cancel. This boundary was not yet intuitive for the student; retain for cold retest.

## F. Independence, fundamental sets, solution spaces and the Wronskian

**Scalar ratio test:** For nonzero \(f\) on an interval, if \(g/f\) is a constant, scalar functions \(f,g\) are dependent; if the ratio varies, independent. Example: \(e^{-t}/e^t=e^{-2t}\) varies ⇒ independent; \(3e^t/e^t=3\) constant ⇒ dependent. The observation \(\ln(e^t)=-\ln(e^{-t})\) is true but does not establish linear dependence.

**Solution space H22:** Its objects are **whole solution functions** \(\mathbf x:I\to\mathbb R^n\), not the particular numbers they output. Vector addition and real scalar multiplication operate on functions pointwise. A fundamental set is **independent solution functions spanning the entire space of solutions**. The phrase “better building blocks” was judged too imprecise.

**Wronskian for a 2D differential system** (two known solutions placed as columns):
\[
W(t)=\det\begin{bmatrix}a(t)&c(t)\\b(t)&d(t)\end{bmatrix}
=a(t)d(t)-b(t)c(t).
\]
If \(W(t)\ne0\), the pair is independent. For two actual solutions of the *same* 2D homogeneous linear system with continuous coefficients, a nonzero Wronskian anywhere on the interval yields a fundamental set.

**Observed correct calculations:** \(\det\begin{bmatrix}1&2\\3&4\end{bmatrix}=-2\), \(\det \operatorname{diag}(e^t,e^{-t})=1\), and
\[
\det\begin{bmatrix}e^{2t}&3e^{2t}\\e^{-t}&-2e^{-t}\end{bmatrix}=-5e^t.
\]
The student momentarily said a nonzero Wronskian means dependence, then correctly answered a new nonzero example means **independence**. Interpret cold, without prompting.

## G. Solve constant-coefficient systems using eigenvalues (supp. 4–5, 8–10)

For \(\mathbf x'=A\mathbf x\), try \(\mathbf x=\boldsymbol\xi e^{rt}\). Substitution gives \(A\boldsymbol\xi=r\boldsymbol\xi\). Procedure:

1. Form \(A-rI\).
2. Calculate \(\det(A-rI)=0\), solve for \(r\).
3. For each eigenvalue, find a **nonzero** eigenvector \(\boldsymbol\xi\) from \((A-rI)\boldsymbol\xi=0\).
4. Combine independent eigenmodes: \(\mathbf x(t)=\sum c_i\boldsymbol\xi^{(i)}e^{r_it}\).
5. For IVPs, set \(t=t_0\) and solve the resulting linear equations for the constants.

**2×2 determinant:** \(\det\begin{bmatrix}a-r&b\\c&d-r\end{bmatrix}=(a-r)(d-r)-bc\). Guard against double-negative errors. Distinct eigenvalues imply independent eigenvectors. For triangular matrices, eigenvalues are diagonal entries.

## H. Phase-plane classification from the worksheet (supp. 7)

| Eigenvalue pattern | Equilibrium at origin |
|---|---|
| Both real negative | Asymptotically stable node |
| Both real positive | Unstable node |
| Opposite real signs | Saddle |
| Pair \(r=\pm i\beta\), \(\beta\ne0\) | Center; stable but **not** asymptotically stable |
| Complex pair with negative real part | Asymptotically stable spiral |
| Complex pair with positive real part | Unstable spiral |

The phase-plane axes are \(x_1,x_2\), **not** \(t,x_1\).

## I. Six retention targets (do not force these before each calculation)

| Skill IDs | Verify independently later |
|---|---|
| G04/G05, H03/H04/H06 | Multiply rows by state column and construct correct shift rows |
| H21 | Read a derivative equation in plain English, naming the subject and signs |
| H23 | Verify all equations for a candidate vector function |
| H16/H17 | Derive superposition for vector functions and explain homogeneous restriction |
| J10 | Construct, simplify and correctly interpret functional Wronskian |
| H22 | Describe solution space's elements and operations, and identify span |

## J. Scoring and timestamps

Log **answer receipt time** in America/Los_Angeles, not the GitHub save time. Include problem number, exact student response, independence/hint level, correctness, specific checkpoint, next cold-review due date. Distinguish **exposure → guided → independent session pass → cold retained → exam ready**.

At the Nov 18 audit: **170 atomic checks**, 10 passed in-session, 5 cold retests due, 6 in progress, 149 unassessed. Do **not** compare the 5.9% atomic in-session tally to the older ~8% Brain/FSRS estimate as though they measured the same thing.

Reference: [Nov 18 audit](session-2026-11-18-lecture18-audit.md), [timestamped record](attempt-log-2026-11-18.csv), [current tracker](final-atomic-checkpoints.csv), [memorization prompts](row-column-spaced-review.md).

## K. November 19 — Problem 4 eigenvector error (cold retest required)

While solving A = [[3,-2],[2,-2]], the student correctly found eigenvalues r=2 and r=-1 but repeatedly reversed the component relationship when translating (A-rI)xi=0 into a column vector. For r=-1, A+I=[[4,-2],[2,-1]], so 4xi_1-2xi_2=0 gives xi_2=2xi_1. Choosing xi_1=1 yields (1,2)^T; (2,1)^T fails direct substitution. Also confused r=-1 with r=+1 when forming A-rI, initially obtaining [[2,-2],[2,-3]]. For r=2, xi_1=2xi_2 gives (2,1)^T, not (1,2)^T. Student specifically identified this as a likely exam point loss and requested later review. **Do not mark mastered.** Cold quiz: (1) form A-rI for a negative eigenvalue, (2) independently rearrange a new homogeneous row equation, (3) write ordered vector components, (4) verify (A-rI)xi=0. Avoid intervening hints.

**Progress:** Problem 3 deferred; Problem 4 characteristic polynomial and eigenvectors completed with guidance; now beginning general-solution substitution x(t)=c_1 xi^(1)e^(2t)+c_2 xi^(2)e^(-t), not yet independently completed. Exact answer timestamps unavailable; recorded on 2026-11-19 (America/Los_Angeles).
