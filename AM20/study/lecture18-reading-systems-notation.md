# AM 20 — Lecture 18: Learn to READ systems notation (Equations 3–5)

**Lesson and first drill:** 2026-11-18, PST.  
**Learning objective:** Given a line of symbolic differential-equation notation, translate it into ordinary English and back without confusing current values with rates of change.  
**Status:** **In progress; needs independent cold retrieval**. This is a prerequisite to calculating with systems, not a completed/mastered skill.  
**Atomic checkpoint:** [H21 in final-atomic-checkpoints.csv](final-atomic-checkpoints.csv). Closely related existing checkpoints: H05, H07, H13, H14, H18, H19.

> Teaching rule: Do not jump to superposition, eigenvalues, or solution algorithms. Work directly from the displayed Lecture 18 page, Equation (3), initial conditions, Equation (4), Definition 1, and Equation (5). Show one small example and ask one question at a time. The student's difficulty is reading the notation, rather than merely understanding what the mathematics is for.

## First, four symbols you must be able to read

| Symbol | Read it as |
|---|---|
| \(t\) | Time |
| \(x_1(t)\) | Value of variable 1 at time \(t\) |
| \(x_1'(t)\) | How quickly variable 1 is changing at that moment |
| \(F_1\) | A rule for calculating that rate of change |

The subscript in \(x_1\) is a **label**, not multiplication by 1.

## 1. Equation (3): Every changing quantity has a rule

Lecture notation:

\[
\begin{cases}
x_1'=F_1(t,x_1,\ldots,x_n),\\
\vdots\\
x_n'=F_n(t,x_1,\ldots,x_n).
\end{cases}
\]

It handles any number of quantities. With two quantities, let \(x_1\) denote position and \(x_2\) velocity. Consider

\[
\begin{cases}
x_1'=x_2,\\
x_2'=-x_1-0.125x_2+5.
\end{cases}
\]

Read **line 1:** The rate of change of position equals velocity.  
Read **line 2:** The rate of change of velocity depends on its current position, velocity, and an additional independent term of 5.

Here \(F_1(t,x_1,x_2)=x_2\) and \(F_2(t,x_1,x_2)=-x_1-0.125x_2+5\). The \(F_i\) names are placeholders for the right-hand-side rules. They need not depend explicitly on \(t\), even though \(t\) appears in the general notation.

## 2. Initial conditions: Where does the system begin?

\[
x_1(t_0)=x_1^0,\qquad x_2(t_0)=x_2^0.
\]

- \(t_0\): starting time.
- \(x_1^0\): starting value of variable 1. Superscript \(0\) is an initial-value **label**, not an exponent.

For example,

\[
x_1(0)=2,\qquad x_2(0)=0
\]

means initial position 2 and velocity 0. Using the rules,

\[
x_1'(0)=0,\qquad x_2'(0)=-2-0+5=3.
\]

The initial *state* is not the same thing as its initial *derivative*.

## 3. Equation (4): A special kind of rule called linear

The lecture writes

\[
F_i(t,x_1,\ldots,x_n)=p_{i1}(t)x_1+\cdots+p_{in}(t)x_n+g_i(t).
\]

Read: Each derivative rule is a sum of state variables multiplied by coefficients, plus an independent term.

Our example, expanded to show every coefficient:

\[
\begin{aligned}
x_1'&=0x_1+1x_2+0,\\
x_2'&=-1x_1-0.125x_2+5.
\end{aligned}
\]

| Equation | Coefficient of \(x_1\) | Coefficient of \(x_2\) | Independent term |
|---|---:|---:|---:|
| 1 | 0 | 1 | 0 |
| 2 | -1 | -0.125 | 5 |

The first index of \(p_{ij}\) tells us the **equation/row**, and the second tells us the **variable/column**. Thus \(p_{21}=-1\). The independent terms are \(g_1=0\), \(g_2=5\).

The same two equations in compact notation are

\[
\boxed{
\mathbf x'=
\underbrace{\begin{bmatrix}0&1\\-1&-0.125\end{bmatrix}}_{P(t)}
\underbrace{\begin{bmatrix}x_1\\x_2\end{bmatrix}}_{\mathbf x}
+
\underbrace{\begin{bmatrix}0\\5\end{bmatrix}}_{\mathbf g(t)}
}.
\]

Nothing has changed mathematically: the matrix holds the coefficients; the state vector holds current values; the forcing vector holds the independent terms. The \(t\) in \(P(t)\) and \(\mathbf g(t)\) allows coefficients and forcing to vary with time, though constants are also permitted.

## 4. Definition 1: What does homogeneous mean?

The textbook's condition is

\[
\mathbf g(t)=\mathbf 0.
\]

Our example has \(\mathbf g(t)=[0,5]^T\), so it is **nonhomogeneous**. If we delete the \(+5\), then \(\mathbf g(t)=[0,0]^T\) and it is **homogeneous**. Every independent term must be zero; a zero coefficient in the matrix does not by itself establish homogeneity.

## 5. Equation (5): Why does the textbook mention continuity?

\[
p_{ij}(t),\,g_i(t)\in C(I).
\]

Read: "The coefficient functions and forcing functions belong to the class of continuous functions on the interval \(I\)."

- \(\in\): belongs to.
- \(C(I)\): continuous functions on interval \(I\).
- \(I\): interval of times under consideration.
- Under the stated continuity condition, prescribing an initial state at a time in \(I\) gives one and only one solution of this **linear** system on \(I\).

The textbook is stating an existence-and-uniqueness guarantee, not asking us to solve the system yet.

## The full page in ordinary English

1. **Equation (3):** Several quantities may each change according to their own rule.
2. **Initial conditions:** Tell us the starting value of every quantity.
3. **Equation (4):** If the rules are linear in the unknown state variables, collect coefficients into a matrix.
4. **Definition 1:** The linear system is homogeneous exactly when every independent forcing term is zero.
5. **Equation (5):** Continuity of the coefficient and forcing functions guarantees existence and uniqueness for a prescribed initial state.

## Explicit prerequisite drill — H21: Read an equation into English

**Prompt A:** Read \(x_1'=3x_1+2x_2\) in words. The correct interpretation must say "*the rate of change of variable 1* equals *three times the current value of variable 1* plus *two times the current value of variable 2*." Do not call both \(x_1\) and \(x_2\) "its position."

**Prompt B:** Read \(x_2'=-x_1-0.125x_2\) in words. Name the derivative on the left and each signed contribution on the right. Avoid "*inverse correlation*" (statistical terminology). Say "negative coefficient" or "negative contribution" at fixed values of the other state.

**Prompt C:** With \(x_1=4\), \(x_2=5\), evaluate the rate \(x_1'\) for prompt A. Answer: \(3(4)+2(5)=22\). Ask the student to show why 22 is a **rate**, not the current value of \(x_1\).

**Prompt D:** Read \(p_{21}(t)\) and locate it in the matrix \(P(t)\). Answer: coefficient of \(x_1\) in equation for \(x_2'\) (row 2, column 1).

**Prompt E:** Explain aloud the difference between \(x_i(t_0)=x_i^0\) and \(x_i'(t_0)\). Then interpret \(\mathbf g(t)=\mathbf 0\) and \(p_{ij}(t)\in C(I)\) in plain English.

### Observed chat responses — 2026-11-18 (PST)

- **Prompt A:** Student correctly recognized the scaling of \(x_1\) by 3 but described the \(2x_2\) term imprecisely as tied to "its position." Teacher corrected the distinction between the two state variables. **Partial, not a pass.**
- **Prompt B:** Student recognized negative contributions and the 0.125 factor but used "*inverse correlation*" and conflated \(x_2\) with position. Teacher corrected vocabulary: negative coefficients, and in this physical example \(x_2\) means velocity. **Partial, not a pass.**
- **As of about 16:56 PST:** The teacher asked for the coefficient of \(x_1\) in \(x_2'=-x_1-0.125x_2\). An independent answer is **not yet recorded**.

### Scheduling and scoring

- **Next session:** Re-test Prompt A or B **without showing the answer first**. Then test D and E one question at a time.
- **Cold-retention follow-up:** Test on a later day with changed coefficients and different state-variable names. Record actual timestamp and accuracy; do not fabricate future attempt times.
- **Session pass:** Independently and accurately read both state variables and their rates, coefficient signs and contributions without teacher repair.
- **Cold mastery:** Two independently correct delayed attempts on different days, plus a successful reading of one unfamiliar equivalent system.
- **Exam readiness:** Translate between general notation, scalar equations, matrix form, initial conditions and continuity condition accurately in a mixed problem.
- **If missed:** Repeat the same idea with simpler notation before proceeding to superposition or eigenvalues.

This lesson preserves the full Equation (3)–(5) explanation for future lessons; H21 is the individually counted **read-an-equation** prerequisite. Other subsections already map to existing atomic checkpoints, rather than being counted twice.
