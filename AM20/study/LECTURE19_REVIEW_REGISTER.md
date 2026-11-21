# AM 20 — Lecture 19: eigenvalue cases and phase-plane review register

> **START HERE for any future Lecture 19 session.** Read the unfinished checkpoints below **before** teaching or selecting problems. The learner has worked through Problems 1–8 with varying confidence; Problems 9–10 remain for rigorous treatment. A computational walkthrough, recognition, or assisted solution is **not** evidence of cold mastery.
>
> Audit recorded **2026-11-20** from the learner's spoken post-practice reflection. This class lecture had **not yet been formally covered** when these observations were recorded. The original worksheet is at [Lecture 19 practice problems](../files/lectures/AM20%20Lecture%2019%20-%20practice%20problems.pdf). Problem-specific notes below are based on learner recall, not a line-by-line transcription of the PDF; verify exact matrices and wording on resumption.
>
> **Next review target (Todoist confirmed):** Saturday **2026-11-21, 1:00–2:30 p.m. PST**, School → AM 20, P1 task `6j3x5MF946cF9Gv4`. The all-day HW8 due date is also November 21. Session plan, four confirmed Todoist tasks, and checkbox queue: [LECTURE19_TODO.md](LECTURE19_TODO.md).

## Primary diagnosis

The bottleneck is the map **eigenvalues/eigenvectors → independent real solutions → trajectory shapes and stability**. Algebraic recipes are often recognized; geometric interpretations, special-case cues, and justifying apparently arbitrary substitutions are not yet independently available.

**Do not conflate:** solving an eigenvalue problem, obtaining two independent real solutions, proving they solve x' = Ax, and classifying the origin.

## Learner's original comments — directly quoted and marked

These are **verbatim excerpts of the November 20 spoken reflection**, not corrected mathematical assertions. Each is linked to a numbered review checkpoint below. **The original full message is not reproduced here**; the table makes the learner's own wording visible so future sessions can distinguish what was said from the teaching interpretation.

| Worksheet / theme | Learner's own words (verbatim excerpt) | Marked review checkpoint / evidence |
| --- | --- | --- |
| Phase-plane intuition | “one value usually is quite prominent and speeds towards the origin and the other one is really quite slow.” | **R06, R07 — RETEST:** distinguish modal decay rates; not a universal rule |
| Complex prerequisite | “At the top I have complex conjugate. That's something I need to study.” | **R04 — RETEST** |
| P4 | “R1 suffices as R1 has no new information. That's something that definitely I would not know status quo.” | **R05 — PRIORITY:** why conjugate information is redundant for a real basis |
| P5 / complex procedure | “if I see a complex value that I should immediately use Euler's formula to substitute it in, eliminate the imaginary part of the solution and then have only the real solutions present.” | **R04–R05 — RETEST:** method recognized, understanding of independent solutions incomplete; mathematically refine, don't erase learner wording |
| P5 / significance | “The significance and the reason behind why we need those two values, I would not be able to articulate” | **R05 — PRIORITY:** two real solution functions, not two newly created eigenvalues |
| P5 / classification | “Origin classification, alpha equals minus one. So it's stable asymptotic and spiraled. I have no idea what that says. Wind around and shrink towards it.” | **R07–R08 — PRIORITY:** translate technical labels into trajectory behavior |
| P6 / generalized vector | “Also generalized eigenvector. I presume that's a method that's introduced in lecture 19 or one that we're supposed to remember from AM 10.” | **R09–R10 — PRIORITY:** recognize one-eigenvector defective case |
| P6 / verification | “And so far as the generalized eigenvector, we solve for it and then we should verify it by differentiating.” | **R11 — REDO:** direct product-rule proof of x'=Ax |
| P6 / revisit | “So I definitely recover and review problem 6.” | **R09–R11 — REDO** |
| P7 | “Problem 7, definitely circle back on that. That one did not make a lick of sense to me.” | **R12 — REDO:** no presumed understanding |
| P7 / specific algebra | “the fact that we got the eigenvalue of 3.” | **R12 — REDO:** check exact worksheet; find derivation, not a guessed factor |
| P8 | “number 8 is just a fantastic review for the final” | **R13 — PRIORITY:** parameter-sensitive classification |
| P9–P10 | “For 9 and 10, I won't pretend that 10 makes a ton of sense to me. And I've just left it and 9 I've left as well to really go through rigorously.” | **R15–R16 — NOT ASSESSED:** full independent solutions still due |
| Independence wording | “one independent eigenvector. This language confuses me.” | **R09, R14 — PRIORITY:** independence vs. orthogonality |
| Transpose | “A transpose for shorthand for verticality.” | **R14 — STUDY:** correct interpretation is row/column interchange; perpendicularity from dot product zero |
| Row-sum cue | “The row sum trick or the finding of constant row sum or the finding of eigenvalues by inspection” | **R03 — RETEST:** show precisely when inspection is legitimate |
| Product rule speed | “It would be good to throw in the product rule on top of that. Just was a little slow to it.” | **R02, R11 — RETEST** |
| P8 / complex separation | “bringing around with complex values. I and separating the real and the imaginary part.” | **R04–R05, R13 — RETEST:** carry complex-to-real method into parameter cases |

**Instruction for subsequent tutoring:** Before starting Lecture 19, read the quoted learner comments and the ranked register; address the exact named misunderstandings. Ask for cold derivations rather than recording a walkthrough as independent mastery. Do not overwrite these quotes with a cleaned-up mathematical paraphrase.

## Numbered practice queue — ranked by conceptual complexity

Each item needs an **unaided, explained** response before marking complete. Lower ranks are prerequisites, not automatically mastered.

| Rank / ID | Worksheet problems | Exact retrieval task | Current evidence / status |
| --- | --- | --- | --- |
| **01 · L19-R01** | 1–3, 6 | Explain why an eigenvector can be scaled; choose a free coordinate (e.g. vector (2,1) when first entry = 2× second) and **verify (A-rI)ξ=0**. | Arithmetic intuition shaky; **retest**. |
| **02 · L19-R02** | 6 | Apply the product rule accurately to e^(rt)(tξ+η); differentiate without hints. | Slow to product rule; **retest**. |
| **03 · L19-R03** | 1–3, 7 | Check eigenpairs by Aξ=rξ; apply constant-row-sum inspection only when valid: A(1,1)^T=s(1,1)^T if both row sums equal s. | Cues by inspection not fluent; **retest**. |
| **04 · L19-R04** | 4–5 | Define complex conjugates and use Euler's formula e^((α+iβ)t)=e^(αt)(cos βt+i sin βt). | Recognizes procedure, not yet cold explanation; **retest**. |
| **05 · L19-R05** | 4–5 | For ξ=a+ib, derive the **two independent real solutions** u=e^(αt)(a cosβt−b sinβt), v=e^(αt)(a sinβt+b cosβt). Explain why conjugate eigenpair gives no additional *distinct real* basis solutions beyond these two. | Problem 4 flagged; conceptual meaning missing; **priority**. |
| **06 · L19-R06** | 1–5 | From x=c1 ξ1 e^(r1 t)+c2 ξ2 e^(r2 t), identify invariant eigendirections and how eigenvalue real parts control growth/decay. Distinguish the slow-decaying mode from the fast-decaying one when both r values are negative. | Qualitative fast/slow heuristic acquired but overgeneralized; **retest**. |
| **07 · L19-R07** | 5, 8 | Classify saddle, stable/unstable node, spiral, center and repeated-eigenvalue node using eigenvalues; state stability **in words**, not only a label. | Origin vocabulary not fluent; **priority**. |
| **08 · L19-R08** | 5, 8 | For r=α±iβ, decide: α<0 inward spiral asymptotically stable; α>0 outward spiral unstable; α=0 center (stable but not asymptotically stable, β≠0). Explain α=−1 physically. | Explicitly cannot yet explain 'spiral' or 'asymptotically stable'; **priority**. |
| **09 · L19-R09** | 6 | Recognize defective repeated eigenvalue: algebraic multiplicity two but **only one independent eigenvector**. Distinguish repeated eigenvalue from a second missing eigenvalue. | Terminology confusing; **priority**. |
| **10 · L19-R10** | 6 | Solve (A−rI)η=ξ and build x2=e^(rt)(tξ+η), alongside x1=e^(rt)ξ. Explain why t appears. | Mechanism unintuitive; **priority / redo**. |
| **11 · L19-R11** | 6 | Verify **both** x1'=Ax1 and x2'=Ax2 by differentiation and matrix multiplication; do not appeal to 'integrating the right-hand side'. | Derivative-cancellation justification missing; **priority / redo**. |
| **12 · L19-R12** | 7 | Reconstruct each unexplained coefficient (including the recalled factor **3**) from Aξ=rξ, linear algebra, or an explicit algebraic step; vary ugly coefficients/trig to check real understanding. | Procedure feels like 'fudging' or guessing; **priority / redo**. |
| **13 · L19-R13** | 8 | Classify a parameter-dependent A(α) piecewise: compute trace, determinant, discriminant, critical parameter values, and stable/unstable regimes. | Central professor emphasis; **priority / redo**. |
| **14 · L19-R14** | 8–10 | Use transpose and orthogonality correctly: ξ1^Tξ2=0 tests perpendicularity; **A^T does not itself mean perpendicular**. Spectral theorem orthogonal diagonalization applies to **real symmetric A**, not arbitrary real A. | Terminology/theorem conflated; **study**. |
| **15 · L19-R15** | 9 | Rigorously solve exact worksheet Problem 9 from a blank page; explain independent eigenvectors, exceptional cases, and phase-plane result if requested. | Deliberately left unresolved; **not assessed**. |
| **16 · L19-R16** | 10 | Rigorously solve exact worksheet Problem 10 from a blank page; derive each algebraic/qualitative step and check solution. | Deliberately left unresolved; **not assessed**. |

**Worksheet coverage notes:** Problems **1–3** felt like Lecture 18 review; **4** revealed complex-conjugate redundancy; **5** combined Euler conversion with origin classification; **6** introduced generalized eigenvector η; **7** introduced unexplained coefficients; **8** is the most exam-relevant parameter/origin-classification problem; **9–10** are pending complete solution.

## Compact decision tree: classify the origin for a 2×2 real constant matrix A

Let τ=tr(A), Δ=det(A), D=τ²−4Δ, so r1,r2=(τ±√D)/2.

1. **Δ<0**: real eigenvalues with opposite signs → **saddle, unstable**.
2. **D>0, Δ>0**: two distinct real eigenvalues with the same sign → **node**; both negative: **asymptotically stable**; both positive: **unstable**.
3. **D<0**: complex pair α±iβ → **spiral** if α≠0; α<0 inward and asymptotically stable, α>0 outward and unstable. If α=0 (τ=0): **center, stable but not asymptotically stable**.
4. **D=0**: repeated real eigenvalue → inspect number of independent eigenvectors; two: proper/star node (scalar matrix case in 2D); one: improper/defective node. Stability from sign of repeated eigenvalue **if nonzero**.
5. **Δ=0**: at least one zero eigenvalue; usual isolated-origin classifications may not apply. Check equilibria and multiplicity instead of forcing node/spiral.
6. When a parameter α varies, search **D=0**, **Δ=0**, and **τ=0** (within complex-pair regime) for changes in geometric behavior.

In a **stable node with unequal negative real eigenvalues**, the mode with eigenvalue *closer to zero* decays more slowly and typically dominates at large positive times (unless its coefficient is zero). This does **not** imply every phase diagram has one fast and one slow trajectory.

### Why the generalized-eigenvector 't' is mandatory, not guessed

If Aξ=rξ and there is only one independent eigenvector, choose η such that
(A−rI)η=ξ, equivalently Aη=rη+ξ. Set

- x1(t)=e^(rt)ξ
- x2(t)=e^(rt)(tξ+η)

Product rule: x2'(t)=e^(rt)[r(tξ+η)+ξ].
Using Aξ=rξ and Aη=rη+ξ:
Ax2(t)=e^(rt)[rtξ+rη+ξ]=x2'(t).

That identity explains why the added **tξ** term compensates for the ξ appearing in Aη. It is **not** because x'(t) should 'equal its integral'; the defining test is x'=Ax. η is not generally unique: adding any multiple of ξ to η gives a different but equivalent basis.

### Spectral-theorem / transpose guardrail

A^T reverses rows and columns. Two vectors v,w are perpendicular if v^T w=0. For a **real symmetric** matrix A=A^T, eigenvectors for distinct eigenvalues can be chosen orthogonal (spectral theorem). Do not infer eigenvector perpendicularity for a general matrix, and do not confuse 'linearly independent' with 'orthogonal'.

## Review method and recording protocol

- Begin with **one cold origin-classification card** and **one cold eigenvector-scaling example**; record hesitation before any explanation.
- Then present the exact Problems 4–10 from the source worksheet; ask for the **next step** rather than revealing full worked answers.
- For each problem, require four outputs: **eigenvalues → eigenvectors/real solution basis → check x'=Ax → classify/sketch**. Parameter problems also need all critical intervals and boundary cases.
- In Problem 6, require a **product-rule derivation** and **direct verification**; in Problem 7, explain the source of the alleged factor 3; in Problems 9–10, start at the statement with no assumed progress.
- Interleave an ugly-sign/eigenvector free-coordinate example and a complex pair so a memorized template cannot substitute for recognition.
- After every attempt, record **independent / hinted / explained-only / not attempted** and one error cue. A 'correct after hint' answer does not meet cold mastery. Use dated attempts and observe no invented timestamps.
- **Never** modify generated AM20/PROGRESS.md, AM20/progress.csv, or AM20/reps.csv manually; they regenerate from Brain/sync.py. This register is the additive persistent entry point pending upstream tracker reconciliation.

## Next step (2026-11-21)

Open [LECTURE19_TODO.md](LECTURE19_TODO.md). Target: cold-check R01–R03, solve P4–P6 rigorously, reconstruct P7, classify P8, and triage P9–P10 without claiming they are complete. The practical success condition is an **explainable diagnostic**, not rushing every problem to completion.
