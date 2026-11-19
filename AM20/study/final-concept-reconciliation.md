# AM 20 — Final concept reconciliation and atomic-skill census
**Audit date:** 2026-11-18. **Sources:** [generated progress](../PROGRESS.md), [legacy concept graph](../progress.csv), [rep ledger](../reps.csv), [homework 4–8 dependency maps](../assignments/INDEX.md), [Lecture 18 working notes](row-column-spaced-review.md), and current study conversation.

## What the numbers mean
- **121 legacy graph nodes:** 95 course-labeled concepts + 26 prerequisites. This is the count generated from the local Brain vault by `sync.py`, not the total number of assessable operations.
- **30/121 legacy nodes studied:** historical exposure from the 2026-11-18 11:50 sync. Not 30 mastered, and not updated for the subsequent chat.
- **8 missing named umbrella concepts** present in the homework 4–8 study orders but absent from `AM20/progress.csv`: Completing the Square; Derivations Of Laplace Transforms; Homogeneous Linear System; Laplace Transform; Method of Undetermined Coefficients; Phase Plane; Polynomial; Variation Of Parameters. At a bare minimum, a named-node inventory including these would contain **129 nodes** (121+8), subject to de-duplication and source validation.
- **168 atomic, independently testable checkpoints** now enumerated in [final-atomic-checkpoints.csv](final-atomic-checkpoints.csv). **This is a separate, finer-grained measurement, NOT 121+168:** many rows are children of legacy nodes. Count their successful cold proofs independently; do not add legacy umbrella nodes into a supposed exam-mastery denominator.
- **Legacy 8% final readiness** comes from FSRS and the older 95-node final scope. It is *not* an independently validated score on the newly inventoried 168 checkpoints and must not be silently recalculated from today's chat.

## Source reconciliation
| Source | What it tracks | Limit |
|---|---|---|
| Brain-generated `progress.csv` / `PROGRESS.md` | 121 prerequisite-and-concept nodes, memory probabilities, historical reps | Under-indexed later lectures, umbrellas instead of micro-operations |
| Earlier standalone `AM20_Study_Tracker.xlsx` | 60 checklist skills, review material and Lectures 1–9 | Different schema, earlier partial coverage; cannot substitute for the final |
| HW4–HW8 generated question-to-concept maps | Named concepts that actual assigned questions require | At least eight names missing from Brain's course slice |
| This audit's atomic checklist | 168 operational checks across fundamentals, first-order, higher-order, Laplace, systems and phase portraits | Preliminary completeness; inferred/provisional subtopics must be checked against actual lecture PDFs and final scope |

## Atomic curriculum by area
| ID | Area | Checks | Source confidence |
|---|---|---:|---|
| A | Algebra and calculus micro-prerequisites | 16 | prerequisite decomposition |
| B | First-order ODE recognition and algorithms | 16 | lectures 1-6 and HW1-HW3 |
| C | Qualitative behavior and mathematical models | 12 | lectures 4-6 and HW1-HW3 |
| D | Second-order homogeneous equations and solution theory | 16 | lectures 7-9 and HW4-HW5 |
| E | Forced equations, higher order, and technique selection | 13 | HW5-HW6 and later-order lecture topics |
| F | Laplace transforms and piecewise inputs | 18 | HW6-HW7; method extensions require lecture verification |
| G | Linear algebra and complex-number prerequisites | 20 | review sheets 1-5 and HW8 prerequisite chain |
| H | Lecture 18: converting and interpreting systems | 21 | lecture 18 and direct chat assessment |
| I | Lecture 19: eigenvalue methods and stability | 18 | lecture 19 topic and HW8; provisional details |
| J | Lecture 20: phase portraits and fundamental matrices | 18 | lecture 20 topic and HW8; provisional details |
| **Total** | **Atomic testable checkpoints** | **168** | |

## Reconciled evidence from Nov 18
| Status | Number | Interpretation |
|---|---:|---|
| unassessed_at_atomic_level | 152 | No atomic evidence reconciled; may have older course-level reps |
| passed_in_session | 9 | Student produced correct independent answer in session; not yet cold retained |
| cold_retest_due | 5 | Correct or improved in session; needs delayed recall |
| in_progress | 2 | Prompt open; no earned pass yet |

**Specifically:** Lecture 18 Step 01 (state-variable conversion) demonstrated; Step 02 (row-column multiplication) practiced but awaits scheduled cold retest; Step 03 (vector derivatives) independently demonstrated; Step 04 (linearity vs homogeneity) passed; Step 05 (zero solution) passed, constant scaling/superposition pending. Do *not* mark umbrella `Superposition Principle` mastered yet.

**2026-11-18 addendum:** A missing explicitly testable prerequisite was identified during notation tutoring: H21, reading a component differential equation in ordinary English without confusing state values and derivatives. It is in progress following two partially accurate guided responses, not passed. This raises the inventory from the original 167 to **168**, with 9 session passes, 5 cold retests due, 2 in progress, and 152 unassessed; the historical 121-node Brain count and 8% legacy FSRS estimate remain unchanged. [Full lesson and drill](lecture18-reading-systems-notation.md).

## Counting discipline
1. **Exposure** = any encounter, explanation, or guided work. **Session pass** = correct independent answer in current session. **Cold retained** = independent retrieval after a delay on a new problem. **Exam ready** = cold retained and able to solve multi-step exam-style problem without cues.
2. A parent and its children may appear in the same knowledge graph, but the **atomic readiness denominator** counts children only. No double credit to `Matrix-Vector Multiplication` just because each row is checked.
3. `unassessed_at_atomic_level` does *not* mean “never studied.” Old reps must be mapped and directly verified.
4. Priority labels indicate learning value, **not measured probability of appearance on the final**. Check actual Lecture 19/20 PDFs and exam study materials before fixing scope; areas marked 'provisional' may be outside scope.
5. `progress.csv` and `PROGRESS.md` are generated by `sync.py` from the laptop's Brain vault; editing them in GitHub would be overwritten. The new `study/` checklist is an additive source of truth pending a laptop-side Brain import.

## Practical next milestone
Complete the scaling and superposition proof in Lecture 18, cold-retake row-column multiplication on November 19, and solve a 2×2 system with eigenvalues/eigenvectors. After each answer, change exactly one or a few appropriate atomic statuses with a timestamp and evidence; don't award mastery by lecture attendance.

## Named gaps in the generator
The Brain vault's upstream concept collection should eventually be updated with the eight missing umbrella nodes plus finer-grained dependency nodes; the sync script's existing prerequisite closure will then incorporate them. Re-run the local `sync.py` for a regenerated `PROGRESS.md` instead of editing generated outputs here.
