# AM 20 — November 18, 2026 learning-session audit

**Written:** 2026-11-18 19:27 PST (America/Los_Angeles).  
**Evidence:** This day's chat transcript; Lecture 18 concepts and the user-pasted **Lecture 18 Problems 1–10 with worked solutions**; [atomic skill tracker](final-atomic-checkpoints.csv); [timed drill notes](row-column-spaced-review.md); [notation lesson](lecture18-reading-systems-notation.md); GitHub commit history for the study log.

> **Timestamp integrity:** In this audit, an exact time attached to an existing GitHub commit is the *time a note was committed*, not necessarily the instant the student answered. Exact per-answer timestamps were generally **not collected**. Some teaching moments have approximate times recorded contemporaneously. For later conversation events, the order is known but not each minute. Do not re-label commit times as quiz-attempt times.

## A. Summary and assessment

The student worked from scalar higher-order ODEs toward first-order vector systems, coefficient matrices, equation reading, linearity/homogeneity, superposition, linear dependence, Wronskians, solution spaces, and the question of what it means for a vector-valued function to *solve* a differential system. Constant-coefficient eigenvalue and phase-plane methods were previewed, then the actual Lecture 18 supplemental set was pasted into chat. Of those ten supplied problem statements, the session stopped at the first rearrangement question of Problem 3; no full independent solution of Problems 3–10 was observed in this chat.

**Current atomic ledger, observed before this audit:** 170 checks total; 10 passed_in_session (5.88%); 5 cold_retest_due; 6 in_progress; 149 unassessed_at_atomic_level. Evidence exists on 21 of 170 (12.35%), but that is not a mastery percentage. A different legacy Brain/FSRS ledger reported approximately 8% readiness on a different scope and cannot be combined with these percentages. No full Lecture 18 mastery or exam score can be inferred.

## B. Directed concept dependency map

~~~mermaid
flowchart TD
  A["Scalar nth-order ODE"] --> B["Choose states x1=y, x2=y', ..."]
  B --> C["First-order component equations"]
  C --> D["Matrix form x'=P(t)x"]
  D --> E["Read state, derivative, coefficients and forcing in words"]
  E --> F["Linear vs nonlinear; homogeneous vs forced"]
  F --> G["Verify x(t) solves every differential equation"]
  G --> H["Homogeneous superposition: c1 f + c2 g"]
  H --> I["Dependent vs independent solutions"]
  I --> J["Wronskian: determinant of solution columns"]
  J --> K["Fundamental set = independent solutions spanning all solutions"]
  K --> L["General solution vs one particular solution"]
  D --> M["Constant coefficient x'=Ax"]
  M --> N["Ansatz x=xi exp(rt)"]
  N --> O["det(A-rI)=0, then (A-rI)xi=0"]
  O --> P["General solution and initial constants"]
  O --> Q["Classify origin in the phase plane"]
  L --> P
~~~

**Structural distinction:** A *solution space* consists of entire solution functions; an initial state is one value of such a function at a chosen time. A field (e.g. R), a vector space over that field, and a field structure on R² identified with C are different types of structure. The student asked about this tangent and then requested return to calculations.

## C. Chronological learning and evidence ledger

Legend: **pass** = independently correct in this session; **partial** = some evidence, not a full checkpoint; **explained** = introduced, no sufficient independent answer; **retest** = delayed check still due. Timestamps with “commit” are exact record times, not exact student-response times.

| When (PST, Nov 18) | Topic / student request | Actual evidence / observation | Status or linked skill |
|---|---|---|---|
| By 15:07:51 **commit** | Higher-order ODE to state variables; matrix row × column | Correct conceptual conversion of y, y', ... but initially misassigned rows [1,0,0] rather than shift rows [0,1,0] and [0,0,1] | H01/H02 pass; G04/G05 and H03/H04/H06 retest |
| By 15:36:16 **commit** | Distinguish vector states from component derivatives | Initially wrote correct scalar expressions without derivative labels; corrected in the session; componentwise differentiation established | H08/H09 pass; notation still needs retest |
| By 15:53:24 **commit** | Linear vs nonlinear, homogeneous vs forcing, zero solution | Correct classification involving squares of dependent variables, time-dependent coefficients, nonzero additive forcing, and zero solution | H11/H12/H13/H15 pass |
| About 15:56; by 16:00:49 **commit** | Why F(t,x) includes t; autonomous vs general notation | Understood distinction between explicit time dependence and time-varying solution, but no independent cold test | explained, unscored |
| About 16:56; by 17:00:13 **commit** | Read x1'=3x1+2x2 and x2'=-x1-0.125x2 in English | Student partially described scaling, but confused which state each x_i denotes; called a negative coefficient “inverse correlation” | H21 in_progress |
| Around 17:57; by 18:01:44 **commit** | Scalar superposition proof | Independently differentiated 3exp(2t), and derived h'=4h for h=3f+2g given f'=4f, g'=4g | H16/H17 partial; vector transfer untested |
| Same stretch | Nonhomogeneous challenge | Initially predicted f+g still satisfied x'=4x+1; learned sum has +2, difference cancels forcing and satisfies associated homogeneous equation | conceptual gap flagged |
| By 18:01:44 **commit** | Dependent scalar functions | Correctly identified g=3f for f=exp(t), g=3exp(t) | recognition pass; no cold test |
| By 18:04:27 **commit** | Independence by ratio and memorization request | For exp(t) and exp(-t), said ratio changes; observed ln f=-ln g, which is true here but does not imply dependence; substituted constants into 2exp(t)-3exp(-t) correctly | ratio worked; memorization prompts saved |
| By 18:07:27 **commit** | Initial Wronskian/determinant check | Independently computed det([[1,2],[3,4]])=-2 and associated nonzero determinant with independent columns | G08 pass, J10 partial |
| Between 18:07 and 18:38 (sequence only) | Functional Wronskians | Computed det diag(exp(t),exp(-t))=1; after initially saying this meant dependence, correctly responded that W=5 implies independence. Later calculated W=-5exp(t) for columns [exp(2t),exp(-t)] and [3exp(2t),-2exp(-t)] | J10 in_progress; correct arithmetic and corrected interpretation |
| Same interval | Fundamental sets, spanning | Explained g=5f makes two functions redundant; objected to vague word “better” and correctly identified span and linear independence as defining requirements | conceptual understanding partial |
| By 18:38:08 **commit** | What is solution space? | Student recognized a space as a set with operations but conflated the space of *solution functions* with the real values they attain | H22 in_progress |
| Same later interval | Algebraic side question | Asked whether R² over R can be a field and what i² means; explained R² as ordered pairs, real scalars, and complex multiplication; correctly rejected i as a real scalar | explained, not part of tested Lecture 18 skills |
| By 18:56:13 **commit** | Precise phrase “two-dimensional homogeneous linear system,” and “solve same system” | Correctly objected that “differential” was implicit, not stated; requested definition and quiz; learned each candidate vector function separately must satisfy both differential equations | H23 in_progress |
| After 18:56, before audit at 19:27 | Particular vs general solution | Correctly answered that [exp(t),0] is a solution, not the general solution; guided general form [c1 exp(t), c2 exp(-t)] | independent distinction on this example; full substitution check still untested |
| After 18:56, before audit at 19:27 | Asked to accelerate to supplementary exercises | Previewed eigensolution x=xi exp(rt), characteristic equation and phase-plane classification, without independently solving any eigenvalue problems | introduced only |
| After 18:56, before audit at 19:27 | Provided exact Lecture 18 supplementary worksheet (Problems 1–10 and solutions) | The sheet was made available in the chat; Problem 3's first algebra rearrangement x2=x1'-2x1 was posed but not answered | problem-solving checkpoint not yet passed |

## D. The exact conceptual corrections that matter most

1. **Matrix row construction:** a coefficient row encodes what a *derivative* depends on; [0,1,0] selects x2. Must cold-retest.
2. **State vs rate:** x_i is a current value; x_i' is a rate. Negative coefficients are not “inverse correlations.”
3. **Equation category:** time-dependent coefficients can still be linear; additive forcing can make a linear system nonhomogeneous.
4. **Superposition has a domain of validity:** homogeneous linear equations preserve arbitrary constant-coefficient combinations of solutions. The +1 forcing counterexample proves this boundary.
5. **Independence vs shared rules:** two functions may both solve one equation while still being dependent; being a solution is independent of testing whether the solutions are redundant.
6. **Wronskian:** put *whole solution vectors* in columns; a nonzero determinant establishes independence in the setting studied, but cannot alone establish that the candidate vectors solve the ODE system.
7. **Solution space:** its objects are whole time-dependent solution functions, not merely real output values or points reached by a trajectory.
8. **Two meanings of “solve”:** a particular solution satisfies all differential equations; a general solution describes every such solution.
9. **Terminology precision:** call it a “two-dimensional homogeneous linear system of differential equations.” Without “differential,” a system of algebraic equations is also possible.
10. **Vector space over R:** “over R” means real scalars. R² can also be made into a field isomorphic to C under the complex multiplication rule. This was understood as an aside and is not a Lecture 18 pass.

## E. Exact supplemental-problem inventory (from user-pasted source)

| Problem | Professor's prompt / mathematical operation | Session status |
|---|---|---|
| 1 | Convert y''+3y'+2y=0 to two first-order equations and matrix form | Similar conversions previously practiced; exact sheet problem not independently retested |
| 2 | Convert y'''-2y''+y'-5y=0 to three-variable matrix system | Similar third-order conversion practiced; exact sheet problem not independently retested |
| 3 | Reduce x1'=2x1+x2, x2'=3x1+4x2 to scalar x1''-6x1'+5x1=0 | Started; tutor posed isolate x2; student answer not yet given |
| 4 | For A=[[3,-2],[2,-2]], eigenvalues 2,-1, eigenvectors, general solution, saddle | Not attempted independently |
| 5 | For A=[[1,1],[4,-2]], eigenvalues 2,-3, eigenvectors, general solution, saddle | Not attempted independently |
| 6 | Verify both eigen-solutions from Problem 5, find W(t)=-5 exp(-t), conclude fundamental set | Not attempted independently |
| 7 | Classify four origins: stable node, center, saddle, stable spiral | Not attempted independently |
| 8 | Solve IVP A=[[1,1],[4,1]], x(0)=[2,3]; eigenvalues 3,-1 and c1=7/4, c2=1/4 | Not attempted independently |
| 9 | Convert u''+5u'+6u=0, solve by eigenvalues -2,-3, compare first component | Not attempted independently |
| 10 | General solution of 3×3 matrix with eigenvalues 1,2,3 and three independent eigenvectors | Not attempted independently |

**Suggested rapid order:** complete Problem 3 with the first algebra step; do 4 and 5 as eigenvalue/eigenvector templates; use 6 as the verification/Wronskian diagnostic; speed through the four classifications in 7; then 8 initial conditions; 9 consistency check; 10 3×3. Revisit 1–2 cold only if matrix-row mistakes recur.

## F. Prioritized retrieval queue

| Priority | Skill ID | Task | Pass criterion |
|---|---|---|---|
| 1 | G04/G05, H03/H04/H06 | Matrix row×column and reverse translation | Independent changed-numbers exercise; repeat on Nov 19 |
| 2 | H23 | Verify an entire proposed vector function solves *each* equation | Differentiate, multiply, compare both components for all t; no hints |
| 3 | H21 | Read two component-rate equations in ordinary language | Correct subjects, derivative, signs, no “correlation” substitution |
| 4 | J10 | Wronskian from two function-valued vectors | Construct columns unaided, calculate W(t), correctly interpret nonzero |
| 5 | H16/H17 | Transfer scalar superposition proof to vectors | Show (c1 x^(1)+c2 x^(2))'=P(t)(c1 x^(1)+c2 x^(2)) |
| 6 | H22 | Articulate solution-space vs state-space distinction | Explain functions are elements; scalars come from R; show span with example |

The local study notes already require two delayed independent attempts on different days for the most fragile matrix retrieval targets. Do not treat guided completion or a new formula introduced by the tutor as earned mastery.

## G. Request inventory

Today's explicit user directions included: (a) explaining Lecture 18 notation from the ground up; (b) slowing down the superposition proof and letting the student formulate its meaning; (c) capturing the student's own mathematical definition and misunderstandings; (d) saving corrected concepts, ratio tests, and Wronskians to a memorization bundle; (e) tracking exact atomic skills and progress percentages in GitHub; (f) giving timestamps on attempts and next tests; (g) distinguishing precise terms like “differential system” and “solves”; (h) reducing philosophical/algebraic tangents and returning to problems quickly; and (i) beginning the exact Lecture 18 supplemental sheet.

**Teaching contract going forward:** One question at a time when drilling. Explain the meaning of notation before asking for manipulations only when necessary. Use the source's actual problem statements rather than newly invented substitutes. Record a timestamp **when the answer arrives**, method (independent/guided), exact evidence, and next cold-review date. Never call a section mastered because it was covered.

## H. Accuracy and maintenance notes

- These records are **reconstructed from the chat**. The answers exist in sequence but precise per-message timestamps were unavailable. Commit history provides exact *save times*, not all learning times.
- At audit, counts are 10 passed, 5 cold retests, 6 in progress, 149 unassessed = 170 total. Earlier README/reconciliation references to 168 are historic and now outdated. Keep the ledger's current count authoritative.
- The autogenerated AM20/PROGRESS.md and AM20/progress.csv are managed by sync.py from the user's Brain vault; do **not** manually edit them.
- Lecture 18 practice PDF exists at AM20/files/lectures/AM20 Lecture 18 - practice problems.pdf. The user pasted the full text and solutions into today's chat, so these are the source for the inventory above.
