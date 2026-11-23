---
parent: "[[AM20]]"
title: AM 20 Final Exam Master Study Guide
course: Ordinary Differential Equations for Engineers
school: UCSC
term: Spring 2026
tags:
  - AM20
  - differential-equations
  - final-exam
  - study-guide
aliases:
  - ODE Study Guide
  - AM20 Final
created: 2026-06-09
type: study
domain: math
status: draft
---

# AM 20 — Differential Equations: Final Exam Master Study Guide

## Navigation

| Section | Link |
|---|---|
| Diagnostic Overview | [[#DIAGNOSTIC OVERVIEW]] |
| Model Key + Frequency Table | [[#SECTION 0 — MODEL KEY]] |
| Technique Entries (T1–T22) | [[#SECTION 1 — TECHNIQUE ENTRIES]] |
| Quick Reference | [[#SECTION 2 — QUICK REFERENCE CHECKLISTS]] |
| Midterm Pattern Analysis | [[#SECTION 3 — MIDTERM PATTERN ANALYSIS]] |
| Book Problems by Technique | [[#SECTION 4 — BOOK PROBLEMS BY TECHNIQUE (Practice Problems.md)]] |
| Final Exam Priority Synthesis | [[#SECTION 5 — FINAL EXAM PRIORITY SYNTHESIS]] |
| Post-Midterm 2 Drill Set | [[AM20_Drill_Set_PostMidterm2]] |

**Course:** Ordinary Differential Equations for Engineers (AM 20, UCSC, Spring 2026)
**Sources scraped:** Quizzes 2,3,4,6,7,8,9,10 ✓ | Mid1 Blue/White ✓ | Mid2 Blue/White ✓ | Practice Problems.md ✓
**Last updated:** Phase 3 (+ Book Problems + Diagnostics)


> [!abstract] Guide Statistics
> - **22** technique entries (T1–T22)
> - **~60** verbatim assessment problems (quizzes + midterms)  
> - **183** book problems catalogued
> - **~149** application sub-categories
> - **⚡ Post-Midterm 2 sources:** Q7–Q10, HW5–7 (highest final exam signal)

---

## DIAGNOSTIC OVERVIEW

### Guide Statistics
| Dimension | Count |
|---|---|
| Total technique entries (T1–T22) | **22** |
| Distinct solution techniques | **18** (T1–T16 core; T17–T22 midterm-depth expansions) |
| Total verbatim assessment problems (quizzes + midterms) | **~60** |
| Total book/practice problems catalogued (Section 4) | **183** |
| Taxonomy application sub-categories (Section 4 tags) | **80+** |
| Sections | **5** (Model Key · Technique Entries · Quick Reference · Midterm Analysis · Book Problems · Final Synthesis) |

---

### Technique Diagnostic — All 22 Entries

Each row: technique · exam tier · complexity (1–5) · number of book problems · dominant application family

| # | Technique | Exam Tier | Complexity | Book Probs | Application Family |
|---|---|---|---|---|---|
| T1 | Numerical Methods (Euler, Heun, RK4, ode45) | Tier 1 | 3 | 11 | Approximation / algorithm |
| T2 | Equilibria & Phase Analysis (autonomous ODEs) | Tier 1 | 1 | ~8 | Qualitative / stability |
| T3 | Existence & Uniqueness (1st + 2nd order) | Tier 2 | 1 | 7 | Theoretical / region analysis |
| T4 | Newton's Cooling / Radioactive Decay | Tier 3 | 2 | 18 | Physical modeling / exponential |
| T5 | Mixing Tank — constant volume | Tier 1 | 3 | (→T17/T18) | Applied linear ODE |
| T6 | Separation of Variables | Tier 3 | 2 | 20 | Pure technique / IVP |
| T7 | Bernoulli Equation | Tier 3 | 3 | 1 | Substitution / nonlinear |
| T8 | 2nd-Order Char. Eq. (homogeneous) | Tier 1 | 2 | 30 | Structure / solution form |
| T9 | Undetermined Coefficients (basic) | Tier 1 | 3 | — | Particular solution / RHS type |
| T10 | Variation of Parameters (basic) | Tier 2 | 4 | — | Particular solution / integral |
| T11 | Spring-Mass System (setup + solve) | Tier 1 | 3 | 22 | Physical oscillation model |
| T12 | Laplace Transform (full pipeline) | Tier 2 | 4–5 | 41 | Transform / IVP |
| T13 | Higher-Order ODEs (3rd/4th order) | Tier 2 | 4 | 17 | Structure extension |
| T14 | Eigenvalues of Matrices (2×2, 3×3) | Tier 1 | 2 | — | Linear algebra prerequisite |
| T15 | Systems of ODEs (eigenvalue method) | Tier 1–2 | 4 | 36 | Vector / phase-plane |
| T16 | ODE → Matrix rewrite (companion form) | Tier 3 | 2 | ~4 | Structural conversion |
| T17 | 1st-Order Linear ODE: Integrating Factor | Tier 1 | 2 | 15 | Pure technique / IVP |
| T18 | Mixing Tank — variable volume | Tier 1 | 3 | (in T17 block) | Applied linear ODE |
| T19 | Equilibria: Full Stability (nonlinear) | Tier 1 | 1–2 | ~8 | Qualitative / nonlinear |
| T20 | Undetermined Coefficients: Full IVP | Tier 1 | 3 | 20 | Particular + homogeneous + ICs |
| T21 | Spring-Mass IVP (full physical) | Tier 1 | 3 | 22 | Physical oscillation + initial conditions |
| T22 | Variation of Parameters + Abel's Formula | Tier 2 | 4 | 9 | Wronskian-based particular solution |

---

### Application Taxonomy Diagnostic — 80+ Sub-Categories Across All Techniques

The taxonomy tags in Section 4 (`[description]` after each problem number) represent the emergent classification of every distinct variant encountered in this course. Below is the full map of application families → sub-categories.

#### T1 — Numerical Methods
- Single Euler step, nonlinear RHS
- Multi-step Euler convergence study (compare to exact)
- Improved Euler (Heun), 2nd-order accuracy
- Runge-Kutta 4 (RK4), classical
- Three-method comparison (Euler vs Heun vs RK4)

#### T17 / T18 — 1st-Order Linear ODE + Mixing
- Homogeneous (constant coefficient, $p$ constant)
- Homogeneous (variable coefficient, $p(x)$ rational)
- Nonhomogeneous (constant RHS)
- Nonhomogeneous (rational / polynomial RHS)
- Nonhomogeneous (singular coefficient $p$ has poles)
- Nonhomogeneous (mixed / complex RHS types)
- IVP at $x_0=0$ (standard)
- IVP at $x_0 \ne 0$ (translate interval)
- IVP with answer as definite integral (no closed form)
- Applied: pharmacokinetics (drug elimination)
- Applied: constant-volume mixing tank
- Applied: two-tank cascade (coupled 1st-order system)
- Applied: gas dilution / ventilation (find minimum rate)
- Applied: variable-volume mixing tank
- Theoretical: limiting behavior as $t\to\infty$
- Theoretical: substitution to reduce equation

#### T4 — Newton's Cooling / Exponential Decay & Growth
- Standard cooling (find temp at time $t$)
- Inverse cooling (recover unknown initial temp $T_0$)
- Coupled mutual cooling (two-body Newton system)
- Pure radioactive decay (given half-life → find $A(t)$)
- Production-decay balance (input rate + decay → equilibrium)
- Threshold / minimum capacity (find critical parameter)
- Financial model (continuous compounding, loan balance)
- Terminal velocity (linear drag, $v \to v_\infty$)
- Upward throw with linear drag (direction changes)
- Position from velocity (integrate drag ODE)
- Nonlinear drag (theoretical / qualitative analysis)
- Escape velocity (nonlinear gravity model)

#### T6 — Separation of Variables
- Pure separation, rational integrand
- Pure separation, nonlinear (product form)
- Pure separation, implicit solution only
- IVP with explicit closed-form answer
- IVP with implicit answer
- IVP requiring trig identity to reach explicit form
- IVP with restricted interval of validity
- Logistic population model (finite carrying capacity)
- Epidemic model ($SI$-type, two interacting variables)
- Bifurcation analysis (parameter-dependent equilibria)

#### T3 — Existence & Uniqueness
- Identify region of continuity ($f$ discontinuous along line)
- Identify region ($\partial f/\partial y$ discontinuous at curve)
- Identify region (both $f$ and $\partial f/\partial y$ singular)
- Compare 1st-order nonlinear theorem vs. 2nd-order linear theorem
- Non-unique solution (blow-up / $\partial f/\partial y$ unbounded)
- Explicit solution + determine maximal interval of uniqueness

#### T8 — 2nd-Order Char. Eq. (Homogeneous)
- Solution verification (check given $y_1, y_2$)
- Reduction of order — given $y_1$, find $y_2$ via $y_2 = uy_1$
- Linear combination / fundamental set verification
- Canonical fundamental pair for given char. roots
- General solution, distinct real roots
- General solution, complex roots $\alpha \pm \beta i$
- General solution, repeated real root
- IVP at $x_0=0$ (all three root types)
- IVP at $x_0 \ne 0$ (shift, then apply ICs)
- Shift theorem: $y(x+a)$ substitution
- Abel's formula: compute $W$ from $p(x)$ without solving

#### T9 / T20 — Undetermined Coefficients
- Polynomial RHS degree 1, $\alpha$ not a root
- Polynomial RHS degree 2, $\alpha$ not a root
- Polynomial RHS, $\alpha=0$ is a root (modify by $x$)
- Euler-Cauchy operator with polynomial RHS
- Pure exponential RHS, no resonance ($\alpha$ not root)
- Pure exponential RHS, simple resonance ($\alpha$ is simple root)
- Pure exponential RHS, double resonance ($\alpha$ is repeated root)
- Pure trig RHS ($\cos$ or $\sin$), no resonance
- Pure trig RHS, resonance ($i\beta$ is a root)
- Exp × polynomial, no resonance
- Exp × polynomial, simple resonance
- Exp × polynomial, double resonance
- Three-case modification rule — compare all three
- Exp × trig, no resonance (both $r = \alpha \pm i\beta$ absent)
- Exp × trig, one root present (partial resonance)
- Exp × trig, full resonance
- Exp × trig, complex with shift
- Superposition of two independent RHS terms
- Superposition with resonance in one term only
- Full IVP: find $y_p$, then apply ICs to $y = y_h + y_p$

#### T10 / T22 — Variation of Parameters
- Constant-coeff ODE, RHS transcendental ($g = \sec x$, $\ln x$, etc.) — UC impossible
- Constant-coeff ODE, RHS rational function
- Constant-coeff ODE, RHS $e^{ax}/f(x)$
- Variable-coeff (Euler-Cauchy) with given $y_1, y_2$
- Variable-coeff, find $y_2$ first then apply VoP
- Variable-coeff, non-standard form (divide through first)
- Full IVP: VoP to get $y_p$, then apply ICs

#### T21 — Spring-Mass
- Free underdamped, English units (lb, ft, slug)
- Free overdamped, English units
- Free critically damped, English units
- Free underdamped, SI units (kg, m, N)
- Free critically damped, SI units
- Forced, steady-state only ($y_p$ only, ignore transient)
- Forced, full solution ($y_h + y_p$, then apply ICs)
- General IVP formulas — underdamped form
- General IVP formulas — overdamped form
- General IVP formulas — critically damped form

#### T12 — Laplace Transform
- Forward: definition integral, polynomial $f(t)$
- Forward: definition, exponential / trig
- Forward: induction proof / Gamma function
- Forward: table look-up, simple
- Forward: piecewise $f(t)$ → write as unit step then transform
- Forward: piecewise defined on 3+ pieces
- Inverse: complete-the-square to $s$-shift form
- Inverse: first shift theorem $e^{at}f(t)$
- Inverse: Heaviside partial fractions (distinct poles)
- Inverse: repeated poles ($(s-a)^n$ denominator)
- Inverse: mixed quadratic denominator + PFD
- IVP with exponential RHS
- IVP with trig RHS
- IVP with exp×trig RHS
- Inverse with $e^{-as}$ factor → delayed function
- IVP with unit step (piecewise) forcing, $h$ steps
- IVP with unit step forcing, multi-interval piecewise
- IVP with resonant piecewise forcing
- IVP with ramp-and-plateau piecewise forcing
- IVP with Dirac delta, single impulse
- IVP with Dirac delta, impulse + standard forcing
- IVP with Dirac delta, impulse at $t=0$

#### T13 — Higher-Order ODEs
- Wronskian verification (3 functions, $3\times3$ det)
- Abel's formula, 3rd-order (integrate $p_1$ from standard form)
- Euler-Cauchy 3rd order: substitution $x = e^t$ → const-coeff
- Constant-coeff, triple real root: $e^{rx}(c_1+c_2 x+c_3 x^2)$
- Constant-coeff, mixed real + complex roots
- 4th-order: factor as two quadratics, extract all roots
- Constant-coeff 3rd-order IVP (full solve + ICs)
- Constant-coeff 4th-order IVP

#### T14 / T15 — Eigenvalues & Systems of ODEs
- Physical modeling: two-tank cascade → matrix system
- Physical modeling: double spring-mass → 2nd-order system
- Companion matrix: rewrite scalar ODE as $\mathbf{y}' = A\mathbf{y}$
- Companion matrix: rewrite 3rd-order ODE
- Verify solution of homogeneous system
- Verify particular solution of nonhomogeneous system
- Fundamental matrix theory ($\Phi(t)$, $\Phi^{-1}(t_0)$)
- Fundamental matrix IVP (6 distinct structural variants)
- Real distinct eigenvalues, 2×2 general solution
- Real distinct eigenvalues, 2×2 IVP
- Real distinct eigenvalues, 3×3 general solution
- Complex eigenvalues $\alpha\pm\beta i$, 2×2 general solution
- Complex eigenvalues, 2×2 IVP
- Complex eigenvalues, 3×3 general solution
- Repeated eigenvalue, defective 2×2 (generalized eigenvector)
- Repeated eigenvalue, defective 2×2 IVP
- Repeated eigenvalue, defective 3×3
- Nonhomogeneous: undetermined coefficients (constant $\mathbf{g}$)
- Nonhomogeneous: undetermined coefficients (exponential $\mathbf{g}$)
- Variation of parameters for systems: $\mathbf{y}_p = \Phi\int\Phi^{-1}\mathbf{g}\,dt$
- VoP for systems: 3×3 case
- Theoretical VoP: prove formula from first principles

---

### Master Technique → Application Count

| Technique Block | Distinct Application Sub-Categories |
|---|---|
| T1 Numerical | 5 |
| T17/T18 1st-Order Linear + Mixing | 16 |
| T4 Cooling + Decay/Growth | 12 |
| T6 Separation | 10 |
| T3 Existence & Uniqueness | 6 |
| T8 Char. Eq. (2nd order) | 11 |
| T9/T20 Undetermined Coefficients | 20 |
| T10/T22 Variation of Parameters | 7 |
| T21 Spring-Mass | 10 |
| T12 Laplace Transforms | 22 |
| T13 Higher-Order ODEs | 8 |
| T14/T15 Eigenvalues + Systems | 22 |
| **TOTAL** | **~149** |

---

### Critical Diagnostic Flags

| Flag | Detail |
|---|---|
| **Highest application diversity** | T12 (Laplace) and T14/T15 (Systems) — 22 sub-categories each; most likely source of novel final exam problems |
| **Highest exam frequency** | [[#T21 — SPRING-MASS IVP (Full Physical Setup → Solve)|T21 Spring-Mass]] — 10 total appearances across quizzes + both midterms |
| **Highest complexity ceiling** | Inverse Laplace + PFD (T12) and VoP for [[#T15 — SYSTEMS OF ODEs (Eigenvalue Method)|T15 Systems]] — complexity 5 |
| **Most book problems** | T12 Laplace: 41 problems; T14/T15 Systems: 36 problems |
| **Lowest frequency but must-know** | T3 E&U, T7 Bernoulli, T16 companion matrix — appear rarely but guaranteed short quiz question |
| **Resonance trap** | T9/T20: resonance modification rule ($\times x^s$) most common source of wrong $y_p$ |
| **Unit trap** | T21: English units ($lb \div 32$ for mass) vs SI units ($kg$ direct) — wrong mass kills entire problem |
| **Transform trap** | T12: forgetting $e^{-as}$ delay factor when inverting; wrong PFD sign errors |
| **Eigenvalue trap** | T15: repeated eigenvalue requires generalized eigenvector $(A-\lambda I)\mathbf{w}=\mathbf{v}$, not second eigenvector |
| **Abel's formula trap** | T22/T13: must write ODE in *standard form* (leading coeff = 1) before reading off $p(t)$ |

---

## SECTION 0 — MODEL KEY

### Technique Frequency Table (Full Course: Quizzes + Midterms + HW5–7)
*M1B = Midterm 1 Blue, M1W = Midterm 1 White, M2B = Midterm 2 Blue, M2W = Midterm 2 White*
*Q7–Q10 = post-Midterm 2 quizzes. HW5–7 = post-Midterm 2 homework.*
*⚡ = appeared post-Midterm 2 (highest final exam signal)*

| Technique | Q2–Q6 | M1B | M1W | M2B | M2W | **Q7–Q10** | **HW5–7** | **Total** |
|---|---|---|---|---|---|---|---|---|
| 1st-Order Linear ODE (Integrating Factor) | — | 2 | 2 | — | — | — | — | **4** |
| Euler/Numerical Methods (ode45) | 7 | — | — | — | — | 1 ⚡ | — | **8** |
| Equilibria / Phase Analysis | 4 | 2 | 2 | — | — | — | — | **8** |
| Existence & Uniqueness | 2 | — | — | — | — | — | — | **2** |
| Newton's Cooling / Radioactive Decay | 1 | — | — | — | — | — | — | **1** |
| Mixing Tank (variable volume) | 2 | 3 | 3 | — | — | — | — | **8** |
| Separation of Variables | 1 | — | — | — | — | — | — | **1** |
| Bernoulli Equation | 1 | — | — | — | — | — | — | **1** |
| 2nd-Order Char. Eq. (homogeneous) | 5 | — | — | 1 | 1 | — | — | **7** |
| Undetermined Coefficients | 3 | — | — | 2 | 2 | — | — | **7** |
| Variation of Parameters | 3 | — | — | 1 | 1 | — | — | **5** |
| Abel's Formula (Wronskian) | — | — | — | 1 | 1 | — | — | **2** |
| Spring-Mass System | 6 | — | — | 2 | 2 | 2 ⚡ | — | **12** |
| Laplace Transform (forward) | 2 | — | — | — | — | 1 ⚡ | — | **3** |
| Inverse Laplace Transform | 3 | — | — | — | — | 3 ⚡ | — | **6** |
| Laplace + Unit Step / Heaviside | 2 | — | — | — | — | 4 ⚡ | 3 ⚡ | **9** |
| Laplace + Dirac Delta | — | — | — | — | — | — | 2 ⚡ | **2** |
| Laplace Convolution Theorem | — | — | — | — | — | — | 2 ⚡ | **2** |
| Higher-Order ODE (3rd/4th order) | 2 | — | — | — | — | 2 ⚡ | — | **4** |
| Eigenvalues of Matrix (2×2, 3×3) | 9 | — | — | — | — | 5 ⚡ | 1 ⚡ | **15** |
| Systems of ODEs (eigenvalue method) | 6 | — | — | — | — | 4 ⚡ | 2 ⚡ | **12** |
| Systems of ODEs + particular solution | 1 | — | — | — | — | 2 ⚡ | 3 ⚡ | **6** |
| Complex eigenvalues → trig solution | 2 | — | — | — | — | 2 ⚡ | 2 ⚡ | **6** |
| Repeated eigenvalues (defective) | 1 | — | — | — | — | 1 ⚡ | — | **2** |
| ODE → Matrix rewrite (companion) | 1 | — | — | — | — | 1 ⚡ | — | **2** |
| Nonlinear systems / Lotka-Volterra | — | — | — | — | — | — | 1 ⚡ | **1** |
| Four-tank nonhomogeneous system (ode45) | — | — | — | — | — | — | 1 ⚡ | **1** |

### Priority Tier Ranking (UPDATED: Full Course including post-Midterm 2)
⚡ = elevated by post-Midterm 2 evidence (Q7–Q10, HW5–7) — highest final exam signal

**Tier 1 — Must Master (highest frequency + post-M2 confirmation):**
- Eigenvalues of 2×2 and 3×3 matrices — **15 total** ⚡ (Q8: entire quiz; Q9–Q10: repeated)
- Systems of ODEs via eigenvalue method — **12 total** ⚡ (Q9–Q10 + HW6–7; all three eigenvalue types)
- Spring-Mass system (free/forced/damped) — **12 total** ⚡ (Q7: two problems; on BOTH midterms)
- Laplace + Unit Step / Heaviside / piecewise forcing — **9 total** ⚡ (Q7: 4 problems; HW5: multi-interval + delta)
- Equilibria / Phase Analysis — **8 total** (on BOTH midterms)
- Mixing Tank — **8 total** (on BOTH midterms)
- Undetermined Coefficients — **7 total** (on BOTH midterms)
- 2nd-order linear ODE: characteristic equation — **7 total** (on BOTH midterms)

**Tier 2 — High ROI (post-M2 confirmed, likely on final):**
- Systems + particular solution (UC or VoP) — **6 total** ⚡ (Q9 Q6: constant forcing; HW6–7: UC + IVP)
- Inverse Laplace transform + partial fractions — **6 total** ⚡ (Q7: mixed PFD; Q7 Q5: first-shift)
- Complex eigenvalues → trig solution — **6 total** ⚡ (Q9 Q1, Q5; HW6 #3, HW7 #1b)
- Higher-order ODEs (3rd/4th order, char eq) — **4 total** ⚡ (Q8 Q1–Q2: both 3rd-order)
- 1st-Order Linear ODE (Integrating Factor) — **4 total** (on BOTH midterms)
- Variation of Parameters — **5 total** (on BOTH midterms; includes Abel's formula)
- Laplace Dirac Delta IVP — **2 total** ⚡ (HW5 #2: multi-delta forcing)
- Laplace Convolution Theorem — **2 total** ⚡ (HW5 #3: two distinct factorizations)
- Repeated eigenvalues (defective, generalized eigenvector) — **2 total** ⚡ (Q9 Q2: alg/geom multiplicity)
- ODE → Matrix rewrite (companion form) — **2 total** ⚡ (Q10 Q1)

**Tier 3 — Lower Frequency / Background (still possible):**
- Numerical methods / ode45 — **8 total** (Q10 Q5 = Euler; HW7 Q3b = Lotka-Volterra)
- Existence & Uniqueness — **2 total**
- Abel's Formula / Wronskian — **2 total**
- Nonlinear systems / phase portraits (Lotka-Volterra) — **1 total** ⚡ (HW7 #3: new topic)
- Bernoulli equations — 1
- Newton's Cooling / Radioactive Decay — 1
- Separation of variables — 1

### Complexity Ranking (1 = easiest, 5 = hardest)
| Technique | Complexity |
|---|---|
| Equilibria / phase analysis | 1 |
| Existence & Uniqueness | 1 |
| Newton's Cooling | 2 |
| Separation of Variables | 2 |
| Characteristic equation (2nd order) | 2 |
| Eigenvalues of matrix | 2 |
| Bernoulli equation | 3 |
| Mixing tank | 3 |
| Numerical methods (Euler, ode45) | 3 |
| Undetermined coefficients | 3 |
| Spring-mass system | 3 |
| Systems of ODEs (eigenvalue method) | 4 |
| Variation of parameters | 4 |
| Higher-order ODEs | 4 |
| Laplace transforms | 4 |
| Inverse Laplace + partial fractions | 5 |
| Laplace + unit step / Dirac delta | 5 |

---

## SECTION 1 — TECHNIQUE ENTRIES

---

### T1 — NUMERICAL METHODS (Euler, Improved Euler, ode45)

**Quiz appearances:** Q2 (Q1,Q2), Q3 (Q4,Q5), Q4 (Q4,Q5,Q6), Q10 (Q8) | **Total: 7**
**⚠ Likely on final:** Yes — appeared every quiz, 3 variants tested

#### Variables
| Symbol | Meaning |
|---|---|
| y' = f(t,y) | ODE in explicit form |
| y(t₀) = y₀ | initial condition |
| h | step size |
| yₙ | approximate value at tₙ = t₀ + nh |

#### Core Equations
| Method | Formula |
|---|---|
| Euler | yₙ₊₁ = yₙ + h·f(tₙ, yₙ) |
| Improved Euler (Heun) | k₁ = f(tₙ,yₙ); k₂ = f(tₙ+h, yₙ+hk₁); yₙ₊₁ = yₙ + (h/2)(k₁+k₂) |
| ode45 (MATLAB) | Built-in adaptive RK4/5; just call ode45(@(t,y) f, tspan, y0) |

> [!tip] Decision Tree

```
Given y' = f(t,y), y(t₀) = y₀, find y(T)?
├─ "use ode45" in problem → call ode45, read off value
├─ step-by-step requested → use Euler or Improved Euler
│   └─ how many steps? → n = (T - t₀)/h
└─ answer is a number → round to stated decimal places
```

> [!warning] Common Traps
> ⚠ Euler underestimates for convex functions, overestimates for concave
> ⚠ ode45 answer: must specify correct tspan = [t₀, T]
> ⚠ f(t,y) must be in the form y' = ..., not y'' = ...


> [!example] Verbatim Problems
> **Q2-Q1:** If y is the solution of the IVP y' = −ty + 3t, y(0) = 2, then y(1) ≈ ... [Answer: ≈2.3935]

> **Q2-Q2:** If y is the solution of the IVP y' = (4t²+1)/y, y(0) = 2, then y(1) ≈ ... [Answer: ≈2.9439]

> **Q3-Q4:** If y' = cos²y cos²x, and y(π) = π/4, then y(2π) = ... [Answer: 1.2]

> **Q3-Q5:** Suppose y = f(t) is the solution of the IVP y' + y/(t²+y²+1) = 1, y(0) = 1. Use Matlab's ode45 to find f(2). [Answer: 2.281]

> **Q4-Q4:** If 3y'' + y' − 2y = 0, y(0) = 0 and y'(0) = 2, then, to 3 decimal places, y(2) = ... [Answer: 4.390]

> **Q4-Q5:** If 4y'' − 4y' + y = 0, y(0) = −1 and y'(0) = 2, then y(1) ≈ ... [Answer: 2.473]

> **Q4-Q6:** If 3y'' + y' − 2y = 0, y(0) = 2 and y'(0) = −1, then y(1) ≈ ... [Answer: 1.684]

> **Q10-Q8:** If [4y'' − 4y' + y = 0, y(0)=−1, y'(0)=2], then y(1) ≈ ... [Answer: 2.473]

---

### T2 — EQUILIBRIA AND PHASE ANALYSIS (Autonomous ODEs)

**Quiz appearances:** Q2 (Q6), Q3 (Q1,Q2) | **Total: 4**
**⚠ Likely on final:** Yes — conceptual, no computation required

#### Variables
| Symbol | Meaning |
|---|---|
| y' = f(y) | autonomous ODE |
| y* | equilibrium: f(y*) = 0 |
| stable | nearby solutions → y* as t → ∞ |
| unstable | nearby solutions → away from y* |

#### Core Equations
| Fact | Statement |
|---|---|
| Equilibria | Solve f(y) = 0 |
| Stability | f'(y*) < 0 → stable; f'(y*) > 0 → unstable |
| Between equilibria | sign of f(y) determines direction of motion |

> [!tip] Decision Tree

```
Given y' = f(y), y(0) = y₀
├─ Find equilibria: solve f(y) = 0
├─ Evaluate f'(y*) or check sign of f between equilibria
├─ y₀ between two equilibria?
│   └─ which direction does f push y? → that's where y(t) goes
└─ "is y(t) increasing?" → check sign of f(y₀): positive = increasing
```

> [!warning] Common Traps
> ⚠ "increasing" means f(y₀) > 0, NOT that y₀ is near a stable equilibrium
> ⚠ For y' = 0.7y(1−y)(4−y): equilibria at y=0,1,4; sign chart needed


> [!example] Verbatim Problems
> **Q2-Q6:** If y' = 0.7y(1−y)(4−y), then ... [Answer: y=1 is stable; y=0 and y=4 are unstable]

> **Q3-Q1:** If y = f(t) is a solution of y' = (y²+3y−4)/(t⁶+1), y(0) = 1.72, then f(t) is an increasing function. [Answer: True]

> **Q3-Q2:** If y = f(t) is a solution of y' = (y²−4y+3)/(t⁴+3), y(0) = 0.55, then f(t) is an increasing function. [Answer: True]

---

### T3 — EXISTENCE AND UNIQUENESS

**Quiz appearances:** Q2 (Q5), Q4 (Q1) | **Total: 2**
**⚠ Likely on final:** Yes — conceptual multiple choice

#### Core Theorems
| Theorem | Conditions | Conclusion |
|---|---|---|
| 1st-order E&U | f and ∂f/∂y continuous on rectangle R containing (t₀,y₀) | Unique solution on some interval (t₀−δ, t₀+δ) |
| 1st-order, linear | p(t) and q(t) continuous on (a,b) containing t₀ | Unique solution on ALL of (a,b) |
| 2nd-order, linear | P, Q, R continuous on (a,b), P(t)≠0 | Unique solution on ALL of (a,b) |

> [!tip] Decision Tree

```
Given y' = f(t,y), y(t₀) = y₀:
├─ Is f linear in y? → use linear theorem → solution on entire interval of continuity
├─ Is ∂f/∂y continuous? → unique solution on SOME interval (not necessarily all of R)
├─ Is ∂f/∂y NOT continuous at y₀? → no guarantee of uniqueness
└─ What interval? → largest open interval containing t₀ where P,Q,R continuous and P(t)≠0
```

> [!warning] Common Traps
> ⚠ "unique on (−∞,∞)" requires LINEARITY — nonlinear only guarantees local interval
> ⚠ For y' = x(y²−4)^(2/3): ∂f/∂y not defined at y=±2 → local interval only for y₀≠±2


> [!example] Verbatim Problems
> **Q2-Q5:** y' = x(y²−4)^(2/3), y(0) = y₀ is ... [Answer: unique solution for every y₀≠±2, defined on some interval (−d₀,d₀)]

> **Q4-Q1:** √(t²+2)y'' + cos(πt)y' + 2y = 0, y(0)=1, y'(0)=−2 has unique solution defined on ... [Answer: (−∞,∞)]

---

### T4 — NEWTON'S COOLING / RADIOACTIVE DECAY

**Quiz appearances:** Q2 (Q4) | **Total: 1**
**⚠ Likely on final:** Moderate — classic application, may appear in HW/midterm context

#### Variables
| Symbol | Meaning |
|---|---|
| T(t) | temperature of body at time t |
| Tₐ | ambient (constant) temperature |
| k | cooling constant (k > 0) |
| Q(t) | quantity of radioactive substance |

#### Core Equations
| Model | ODE | Solution |
|---|---|---|
| Newton's Cooling | dT/dt = −k(T − Tₐ) | T(t) = Tₐ + (T₀ − Tₐ)e^(−kt) |
| Radioactive Decay | dQ/dt = −kQ | Q(t) = Q₀e^(−kt) |

> [!tip] Algorithm

```
1. Write ODE: dT/dt = −k(T − Tₐ)
2. Solve: T(t) = Tₐ + Ce^(−kt), C = T₀ − Tₐ
3. Use 2nd data point to find k: T(t₁) = Tₐ + Ce^(−kt₁)
   → k = −(1/t₁)ln[(T(t₁)−Tₐ)/(T₀−Tₐ)]
4. Evaluate T at desired time
```

> [!example] Verbatim Problems
> **Q2-Q4:** A steel ball is heated to 200°C and then immersed in a vat of water kept at a constant temperature of 10°C. After 1 minute, the temperature of the ball is 170°C. What will the temperature of the ball be after 10 minutes? [Answer: ≈44°C]

---

### T5 — MIXING TANK (Linear 1st-Order ODE)

**Quiz appearances:** Q3 (Q6,Q7) | **Total: 2**
**⚠ Likely on final:** Yes — appeared in both midterms (likely), full solve required

#### Variables
| Symbol | Meaning |
|---|---|
| Q(t) | quantity of substance in tank at time t |
| V | volume of tank (constant if in-rate = out-rate) |
| rᵢₙ | flow rate in (gal/hr) |
| rₒᵤₜ | flow rate out (gal/hr) |
| cᵢₙ | concentration of incoming substance |
| C(t) = Q(t)/V | concentration in tank |

#### Core Equations
| Equation | Form |
|---|---|
| ODE for Q | dQ/dt = rᵢₙ·cᵢₙ − rₒᵤₜ·(Q/V) |
| Standard linear form | Q' + (rₒᵤₜ/V)·Q = rᵢₙ·cᵢₙ |
| Integrating factor | μ(t) = e^∫(rₒᵤₜ/V)dt = e^(rₒᵤₜ·t/V) (if V constant) |

> [!tip] Algorithm

```
1. Define Q(t) = total substance in tank
2. Rate in = rᵢₙ × cᵢₙ
3. Rate out = rₒᵤₜ × (Q/V)
4. ODE: Q' = rate_in − rate_out
5. Rewrite in standard linear form: Q' + pQ = g
6. Compute integrating factor μ = e^∫p dt
7. Solve: Q = (1/μ)∫μg dt + C/μ
8. Apply IC to find C
9. Convert Q → concentration if needed: C(t) = Q(t)/V
```

> [!warning] Common Traps
> ⚠ If V is NOT constant (rᵢₙ ≠ rₒᵤₜ): V(t) = V₀ + (rᵢₙ − rₒᵤₜ)t
> ⚠ cᵢₙ may be time-dependent (e.g., C(t) = 3(cos(πt/8)+1)) → harder integral


> [!example] Verbatim Problems
> **Q3-Q6:** Whoville pond contains V₀=2 million gallons. Water flows in at w₀=250 gal/hr, out at same rate. Incoming concentration c₀=0.02 gm/gal. Initial concentration 2 gms/gal. How long to decrease to 0.5 gms/gal? [Answer: ≈1.3 years]

> **Q3-Q7:** A tank contains 200 gallons of pure water. At t=0, saline with C(t)=3(cos(πt/8)+1) oz/gal begins at 5 gal/hr in, 5 gal/hr out. Find concentration at t=24. [Answer: 1.335]

---

### T6 — SEPARATION OF VARIABLES

**Quiz appearances:** Q3 (Q3) | **Total: 1**
**⚠ Likely on final:** Low from quizzes but foundational — will increase with HW/midterm data

#### Core Equation
`M(y) dy = N(x) dx → ∫M(y) dy = ∫N(x) dx + C`

> [!tip] Algorithm

```
1. Write y' = f(x)g(y)
2. Separate: dy/g(y) = f(x)dx
3. Integrate both sides
4. Solve for y (explicit or implicit)
5. Apply IC to find C
```

> [!example] Verbatim Problems
> **Q3-Q3:** The solution to y' = (x²−4)/(2y+3), y(0)=1 is ... [Answer: y = (1/2)(√(4/3·x³−16x+25) − 3)]

---

### T7 — BERNOULLI EQUATION

**Quiz appearances:** Q2 (Q3) | **Total: 1**
**⚠ Likely on final:** Low from quizzes; may appear in HW. Technique: substitution v = y^(1-n)

#### Core Equation
`y' + P(x)y = Q(x)yⁿ`

> [!tip] Algorithm

```
1. Identify n (the power of y on RHS)
2. Substitute v = y^(1-n)
3. Then v' = (1-n)y^(-n) y'
4. Divide original by yⁿ → get v' + (1-n)P(x)v = (1-n)Q(x)
5. Solve the resulting LINEAR ODE for v
6. Back-substitute: y = v^(1/(1-n))
7. Apply IC
```

> [!example] Verbatim Problems
> **Q2-Q3:** If y' + y = 3xy² and y(0) = 1/2, then ... [Answer: y = 1/(3x−3+5eˣ)] *(Comment: Read pp. 63-64 on Bernoulli equations)*

---

### T8 — 2ND-ORDER LINEAR ODE: CHARACTERISTIC EQUATION

**Quiz appearances:** Q4 (Q2,Q3,Q7,Q8), Q6 (Q1) | **Total: 5**
**⚠ Likely on final:** High — core technique, needed for spring-mass and Laplace

#### Variables
| Symbol | Meaning |
|---|---|
| ay'' + by' + cy = 0 | homogeneous 2nd-order constant-coeff ODE |
| r | roots of characteristic equation ar²+br+c=0 |
| r₁, r₂ | distinct real roots |
| α ± βi | complex conjugate roots |
| r (repeated) | double root |

#### Core Equations
| Root type | General solution |
|---|---|
| r₁ ≠ r₂, both real | y = c₁e^(r₁t) + c₂e^(r₂t) |
| r = α ± βi | y = e^(αt)(c₁cos(βt) + c₂sin(βt)) |
| r repeated (r₁ = r₂ = r) | y = (c₁ + c₂t)e^(rt) |

> [!tip] Algorithm

```
1. Write characteristic equation: ar² + br + c = 0
2. Compute discriminant: b²−4ac
   ├─ >0: two distinct real roots r₁,r₂
   ├─ =0: repeated root r = −b/(2a)
   └─ <0: complex roots α±βi, α=−b/(2a), β=√(4ac−b²)/(2a)
3. Write general solution per table above
4. If IVP: apply y(0)=y₀ and y'(0)=y₀' to solve for c₁,c₂
```

#### Behavior as t→∞
```
All roots have Re(r) < 0 → y(t) → 0 (stable)
Any root has Re(r) > 0 → |y(t)| → ∞ (unstable)
```

> [!warning] Common Traps
> ⚠ For y'' + μy' − 3y = 0: char eq r²+μr−3=0; roots always real (b²−4ac = μ²+12 > 0)
> ⚠ For y'' − 2y' + μy = 0: check discriminant 4−4μ; complex when μ>1


> [!example] Verbatim Problems
> **Q4-Q2:** If y is any non-constant solution of y'' + μy' − 3y = 0, then ... [Answer: Neither (A) nor (B) — one root always positive, one negative regardless of μ]

> **Q4-Q3:** If y is a non-constant solution of y'' − 2y' + μy = 0, then ... [Answer: (B) lim|y(t)|=∞, if 1≥μ>0]

> **Q4-Q7:** Every solution of y'' + 4y' − 5y = 0 has the form ... [Answer: y = c₁e^(−5t) + c₂e^t]

> **Q4-Q8:** Every solution of y'' − 2y' − 3y = 0 has the form ... [Answer: y = c₁e^(3t) + c₂e^(−t)]

> **Q6-PNG-Q1:** y'' − 5y' + 6y = 4te^(−2t) general solution ... [Answer: y = c₁e^(2t) + c₂e^(3t) + e^(−2t)(0.2t + 0.09)]

---

### T9 — UNDETERMINED COEFFICIENTS

**Quiz appearances:** Q6 (Q1,Q2), Q8 (Q2) | **Total: 3**
**⚠ Likely on final:** Yes — standard method for nonhomogeneous 2nd/3rd order ODEs

#### Core Structure
`y = yₕ + yₚ`
where yₕ = homogeneous solution (char equation), yₚ = particular solution (guessed form)

#### Guess Table for yₚ
| g(t) (RHS) | Guess for yₚ |
|---|---|
| Pₙ(t) (polynomial degree n) | tˢ(Aₙtⁿ + ... + A₀) |
| e^(at) | tˢAe^(at) |
| e^(at)cos(bt) or e^(at)sin(bt) | tˢe^(at)(Acos(bt)+Bsin(bt)) |
| Pₙ(t)e^(at) | tˢe^(at)(Aₙtⁿ+...+A₀) |

*s = 0 if guess not a root of char eq; s = 1 if simple root; s = 2 if double root*

> [!tip] Algorithm

```
1. Solve homogeneous: ay'' + by' + cy = 0 → find yₕ
2. Identify form of g(t) → write guess for yₚ (including multiplier tˢ if needed)
3. Substitute yₚ into ODE, collect terms, solve for coefficients
4. y = yₕ + yₚ
5. If IVP: apply y(t₀), y'(t₀) to full y (not just yₕ!)
```

> [!example] Verbatim Problems
> **Q6-Q1:** The general solution of y'' + 4y' + 3y = 5te^(2t) is ... [Answer: y = c₁e^(−t) + c₂e^(−3t) + e^(2t)(t/3 − 8/45)]

> **Q6-PNG-Q2:** The solution of y'' + 5y' + 6y = 4t²sint, y(0)=0, y'(0)=1 is ... [Answer: y = (0.6t²−1.32t+0.672)sint + (0.3t²+0.24t−0.804)cost + 1.25e^(−2t) − 0.446e^(−3t)]

> **Q8-Q2:** The general solution of y''' + 2y'' − 5y' − 6y = 6t² is ... [Answer: y = c₁e^(−3t) + c₂e^(−t) + c₃e^(2t) − t² + (5/3)t − 37/18]

---

### T10 — VARIATION OF PARAMETERS

**Quiz appearances:** Q6 (Q2,Q3), Q6-PNG-Q3 | **Total: 3**
**⚠ Likely on final:** Yes — more general than undetermined coefficients; tested conceptually

#### Core Formula
Given y'' + p(t)y' + q(t)y = g(t) with fundamental pair {y₁, y₂}:
```
yₚ = −y₁∫(y₂g/W)dt + y₂∫(y₁g/W)dt
```
where W = y₁y₂' − y₂y₁' (Wronskian)

#### General solution formula (integral form)
```
y = c₁y₁(t) + c₂y₂(t) + y₂(t)∫[y₁(s)g(s)/W(s)]ds − y₁(t)∫[y₂(s)g(s)/W(s)]ds
```

> [!tip] Algorithm

```
1. Find y₁, y₂ from homogeneous solution
2. Compute W(t) = det[[y₁, y₂],[y₁', y₂']]
3. Write yₚ = u₁y₁ + u₂y₂
   where u₁' = −y₂g/W, u₂' = y₁g/W
4. Integrate u₁' and u₂'
5. Assemble y = yₕ + yₚ
```

> [!warning] Common Traps
> ⚠ Must rewrite in STANDARD FORM first: y'' + py' + qy = g (divide by leading coeff)
> ⚠ The integral form with β·y₂(t)∫[y₁(s)/s]g(s)ds uses normalized equation


> [!example] Verbatim Problems
> **Q6-Q3 (conceptual):** Suppose y₁,y₂ form fundamental pair of y'' + 2y'/t − cos(t)y = 0 on (0,∞). General solution of y'' + 2y'/t − cos(t)y = t is given by ... [Answer: β·y₂(t)∫₁ᵗ(y₁(s)/s)ds − β·y₁(t)∫₁ᵗ(y₂(s)/s)ds + c₁y₁(t) + c₂y₂(t), where β depends on y₁,y₂]

> **Q6-PNG-Q3 (conceptual):** y'' + cos(t)y' − sin(t)y = 0 on (−∞,∞); general solution of y'' + cos(t)y' − sin(t)y = t² ... [Answer: β·y₂(t)∫₀ᵗ s²y₁(s)ds − β·y₁(t)∫₀ᵗ s²y₂(s)ds + c₁y₁+c₂y₂]

---

### T11 — SPRING-MASS SYSTEM

**Quiz appearances:** Q6 (Q4,Q5,Q6), Q7 (Q1), Q6-PNG (Q4,Q5,Q6) | **Total: 6**
**⚠ Likely on final:** HIGH — multiple variants, computationally rich

#### Variables
| Symbol | Meaning |
|---|---|
| m | mass (kg) |
| c | damping coefficient |
| k | spring constant |
| F(t) | external forcing |
| y(t) | displacement from equilibrium |
| ω₀ = √(k/m) | natural frequency |
| γ = c/(2m) | damping ratio |
| ωd = √(ω₀²−γ²) | damped frequency |

#### Core ODE
`my'' + cy' + ky = F(t)`

#### Spring constant from static stretch
`k = mg/L` (where L = static stretch, g = 9.8 m/s² or 32 ft/s²)

#### Damping Classification
| Condition | Type | Behavior |
|---|---|---|
| c² − 4mk > 0 | Overdamped | Two real negative roots; no oscillation |
| c² − 4mk = 0 | Critically damped | c = 2√(mk); fastest return, no oscillation |
| c² − 4mk < 0 | Underdamped | Complex roots; oscillates with decay |
| c = 0 | Undamped | Pure oscillation |

#### Steady-State Amplitude (forced, underdamped)
For my'' + cy' + ky = F₀cos(ωt):
```
R = F₀ / √((k−mω²)² + c²ω²)
```

#### Algorithm: Physical Setup → ODE
```
1. Find k: k = mg/(static stretch) [if mass stretches spring]
2. Find c: c = (damping force)/(velocity at that force)
3. Write: my'' + cy' + ky = F(t)
4. Classify: compute c² vs 4mk
5. Solve char equation: mr² + cr + k = 0
6. For steady state amplitude: use R formula above
```

> [!warning] Common Traps
> ⚠ Critical damping: c = 2√(mk), NOT c > 2√(mk)
> ⚠ Underdamped: c < 2√(mk), NOT c < √(mk)
> ⚠ For steady state: does NOT depend on initial conditions


> [!example] Verbatim Problems
> **Q6-Q4:** A free spring-mass system: 100y'' + cy' + 20y = 0. Critically damped if c is ≈ ... [Answer: ≈89.443, i.e., c = 2√(100·20)]

> **Q6-Q5:** Forced spring-mass: 2y'' + 3y'' + 4y = 40cos(t). Amplitude of steady state R ≈ ... [Answer: ≈11.09] *(Note: "2y'' + 3y''" in problem is likely typo for 2y'' + 3y')*

> **Q6-Q6:** Spring-mass 5y'' + cy' + 4y = 0. Under-damped if c < ... [Answer: c < 8.94 = 2√(5·4)]

> **Q6-PNG-Q4:** 400y'' + cy' + 30y = 0. Critically damped if c is ≈ ... [Answer: c ≈ 219.09 = 2√(400·30)]

> **Q6-PNG-Q5:** Forced: 5y'' + 3y'' + 4y = 50cos(πt). R ≈ ... [Answer: ≈2.02]

> **Q6-PNG-Q6:** my'' + 5y' + 4y = 0. Over-damped if m < ... [Answer: m < 1.56]

> **Q7-Q1:** Mass of 6 kg stretches spring 5 cm. External force 8cos(14t) N, damping force 1N at velocity 7 m/s. Amplitude of steady state ... [Answer: ≈2 m]

---

### T12 — LAPLACE TRANSFORM

**Quiz appearances:** Q7 (Q2,Q3,Q4,Q5,Q6,Q7) | **Total: 6**
**⚠ Likely on final:** HIGH — dedicated quiz, multiple problem types

#### Core Transform Table
| f(t) | F(s) = L{f(t)} |
|---|---|
| 1 | 1/s |
| t^n | n!/s^(n+1) |
| e^(at) | 1/(s−a) |
| sin(bt) | b/(s²+b²) |
| cos(bt) | s/(s²+b²) |
| e^(at)sin(bt) | b/((s−a)²+b²) |
| e^(at)cos(bt) | (s−a)/((s−a)²+b²) |
| t·sin(bt) | 2bs/(s²+b²)² |
| t·cos(bt) | (s²−b²)/(s²+b²)² |
| u(t−a) | e^(−as)/s |
| u(t−a)f(t−a) | e^(−as)F(s) |
| δ(t−a) | e^(−as) |

#### Key Properties
| Property | Formula |
|---|---|
| Linearity | L{af+bg} = aF+bG |
| First shift (s-shift) | L{e^(at)f(t)} = F(s−a) |
| Second shift (t-shift) | L{u(t−a)f(t−a)} = e^(−as)F(s) |
| Derivative | L{f'} = sF(s)−f(0) |
| Second derivative | L{f''} = s²F(s)−sf(0)−f'(0) |

#### Algorithm: Solve IVP via Laplace
```
1. Take L of both sides of ODE
2. Substitute L{y''} = s²Y−sy(0)−y'(0), L{y'} = sY−y(0)
3. Solve algebraically for Y(s)
4. Decompose Y(s) using partial fractions
5. Identify each term in transform table
6. Apply inverse Laplace to get y(t)
7. If e^(−as) appears → use second shift: u(t−a)f(t−a)
```

#### Inverse Laplace: Partial Fractions
```
For Y(s) = P(s)/Q(s):
- Linear factor (s−a): A/(s−a)
- Repeated (s−a)²: A/(s−a) + B/(s−a)²
- Irreducible quad (s²+bs+c): (As+B)/(s²+bs+c) → complete the square
```

> [!warning] Common Traps
> ⚠ e^(−as)/F(s) is NOT L^{-1}{e^(−as)}·f(t) — must identify f(t-a), not f(t)
> ⚠ For s-shift: L{e^(at)f(t)} = F(s−a); inverse: given F(s−a) → e^(at)f(t)
> ⚠ Always check: does Y(s) have e^(−as) factor? If yes, second shift applies


> [!example] Verbatim Problems
> **Q7-Q2:** L{3t·cos(4t) − e^(2t)·sin(t)} = ... [Answer: 6s²/(s²+16)² − 3s/(s²+16) − 1/((s−1)²+1)] *(Note: from image rendering, signs approximate)*

> **Q7-Q3:** If F(s) = 2∛s is Laplace transform of f(t), then G(s) = 2∛(s+1) is Laplace transform of g(t) = e^(−t)f(t). [First shift theorem]

> **Q7-Q4:** L^{-1}{(6 + 0.4se^(−3s))/(s²+4)} = ... [Answer: 3sin(2t) + 0.2u(t−3)cos(2(t−3))]

> **Q7-Q5:** L^{-1}{(3s+2)/((s²+4)(s²+3s+2)) + (2s−1)/(s²+3s+2)} = ... [Answer: (2/5)sin2t + (3/10)cos2t − (11/2)e^(−2t) + (12/5)e^(−t)]

> **Q7-Q6:** y'' + 4y' + 5y = 3 − 3u(t−6), y(0)=0, y'(0)=2. Solution is L^{-1} of Y(s) = ... [Answer: Y(s) = 2/(s²+4s+5) − (3−3e^(−6s))/(s(s²+4s+5))]

> **Q7-Q7:** y'' − 4y' + 3y = u(t−2)(t−2)³, y(0)=2, y'(0)=0. Solution is L^{-1} of ... [Answer: Y(s) = 6e^(−2s)/(s⁴(s²−4s+3)) + (2s−8)/(s²−4s+3)]

---

### T13 — HIGHER-ORDER ODES (3rd Order)

**Quiz appearances:** Q8 (Q1,Q2) | **Total: 2**
**⚠ Likely on final:** Moderate — same technique as 2nd order, just more algebra

#### Core Approach
Same as T8 but characteristic polynomial is cubic: ar³ + br² + cr + d = 0
- Factor by inspection or rational root theorem
- Three roots → three basis solutions → y = c₁e^(r₁t) + c₂e^(r₂t) + c₃e^(r₃t)

> [!tip] Algorithm

```
1. Write char equation: ar³ + br² + cr + d = 0
2. Find rational roots: try ±factors(d)/factors(a)
3. Factor: (r−r₁)(quadratic) = 0
4. Solve quadratic for remaining roots
5. Write general solution
6. For nonhomogeneous: find yₚ via undetermined coefficients (same guess table)
```

> [!example] Verbatim Problems
> **Q8-Q1:** y''' − 2y'' − 5y' + 6y = 0. General solution is ... [Answer: y = c₁e^(−2t) + c₂e^t + c₃e^(3t)]

> **Q8-Q2:** y''' + 2y'' − 5y' − 6y = 6t². General solution is ... [Answer: y = c₁e^(−3t) + c₂e^(−t) + c₃e^(2t) − t² + (5/3)t − 37/18]

---

### T14 — EIGENVALUES OF MATRICES

**Quiz appearances:** Q8 (Q3,Q4,Q5,Q6,Q7,Q8), Q9 (Q1,Q2), Q10 (Q1 implied) | **Total: 9**
**⚠ Likely on final:** VERY HIGH — highest frequency technique in Phase 1

#### Core Equation
`det(A − λI) = 0`

#### For 2×2 matrix [[a,b],[c,d]]:
```
λ² − (a+d)λ + (ad−bc) = 0
λ = [(a+d) ± √((a+d)²−4(ad−bc))] / 2
```

#### For 3×3 matrix:
```
det(A−λI) = 0 expands to cubic: −λ³ + tr(A)λ² − (sum of 2×2 minors)λ + det(A) = 0
```

#### Eigenvectors
For each eigenvalue λ: solve (A−λI)v = 0

> [!tip] Algorithm

```
1. Write A − λI
2. Set det(A − λI) = 0
3. For 2×2: use quadratic formula
4. For 3×3: expand by cofactors along row/column with most zeros
5. Find roots of characteristic polynomial
6. For each λ: row reduce (A−λI) to find null space → eigenvector
```

> [!warning] Common Traps
> ⚠ For upper/lower triangular matrices: eigenvalues ARE the diagonal entries
> ⚠ Complex eigenvalues for [[a,b],[−b,a]]: λ = a ± bi
> ⚠ Algebraic multiplicity ≠ geometric multiplicity (defective matrices)


> [!example] Verbatim Problems
> **Q8-Q3:** Eigenvalues of [[1,2],[2,1]] are ... [Answer: λ=−1 and λ=3]

> **Q8-Q4:** Eigenvalues of [[2,3],[−3,2]] are ... [Answer: λ=2−3i and λ=2+3i]

> **Q8-Q5:** Eigenvalues of [[1,3],[3,1]] are ... [Answer: λ=−2 and λ=4]

> **Q8-Q6:** det([[3−u, 2, 1],[−1, 1−u, 2],[1, 1, 2−u]]) = ... [Answer: −u³+6u²−10u+6]

> **Q8-Q7:** Eigenvalues of [[1,7,1],[0,3,5],[0,5,3]] are ... [Answer: λ=−2, λ=1, λ=8]

> **Q8-Q8:** Eigenvalues of [[4,2,1],[0,2,5],[0,5,2]] are ... [Answer: λ=−3, λ=4, λ=7]

> **Q9-Q1:** Matrix A=[[2,−2],[2,2]] has eigenvalues λ=2±2i, complex eigenvectors ... [Answer: [1+i; i] and [1−i; −i]]

> **Q9-Q2:** λ=2 is eigenvalue of [[10,8,−8],[−7,−5,7],[2,2,0]] of algebraic multiplicity ... and geometric multiplicity ... [Answer: alg mult 2, geom mult 1]

---

### T15 — SYSTEMS OF ODEs (Eigenvalue Method)

**Quiz appearances:** Q9 (Q3,Q4,Q5,Q6), Q10 (Q2,Q3) | **Total: 6**
**⚠ Likely on final:** VERY HIGH — most recent material, complex variants tested

#### Core Structure
`x' = Ax` (homogeneous) or `x' = Ax + f(t)` (nonhomogeneous)

#### Solution by Case

**Case 1: Distinct real eigenvalues λ₁, λ₂ with eigenvectors v₁, v₂**
```
x(t) = c₁e^(λ₁t)v₁ + c₂e^(λ₂t)v₂
```

**Case 2: Complex eigenvalues λ = α ± βi with eigenvector p ± qi**
```
x(t) = c₁e^(αt)[p·cos(βt) − q·sin(βt)] + c₂e^(αt)[p·sin(βt) + q·cos(βt)]
```

**Case 3: Repeated eigenvalue λ with only one eigenvector v (defective)**
```
Find generalized eigenvector w: (A−λI)w = v
x(t) = c₁e^(λt)v + c₂e^(λt)(tv + w)
```

**Case 4: Nonhomogeneous x' = Ax + f(t)**
```
x(t) = xₕ(t) + xₚ(t)
xₚ: use undetermined coefficients or variation of parameters for systems
```

> [!tip] Algorithm

```
1. Find eigenvalues: det(A−λI) = 0
2. For each λ: find eigenvector v from (A−λI)v = 0
3. Determine case (real distinct / complex / repeated)
4. Write general solution per case
5. If IVP: apply x(0) = x₀, solve for c₁, c₂
6. If nonhomogeneous: find xₚ (constant particular solution if f is constant)
```

#### Particular solution for constant forcing (x' = Ax + b):
```
Set x' = 0: Axₚ = −b → xₚ = −A^(−1)b
```

> [!warning] Common Traps
> ⚠ Complex eigenvalue: use ONE eigenvector (for λ=α+βi), extract real/imag parts
> ⚠ Repeated eigenvalue: check if 2 linearly independent eigenvectors exist first
> ⚠ For nonhomogeneous: apply IC to FULL solution (xₕ + xₚ), not just xₕ


> [!example] Verbatim Problems
> **Q9-Q3:** x' = [[−2,1],[1,−2]]·x; x(0) = [1;2]. Solution is ... [Answer: x(t) = (1/3)[e^(−t)+2e^(−3t); 3e^(−t)+3e^(−3t)]] *(approximate — answer not shown, use technique)*

> **Q9-Q4:** General solution of x' = [[1,1],[−2,4]]·x + [−1;3] is ... [Answer: c₁[1;−1]e^(2t) + c₂[1;2]e^(3t) + [−1/6; 2/3]]

> **Q9-Q5 (IVP):** y₁'=−y₁+2y₂, y₂'=−2y₁−y₂; y₁(0)=1, y₂(0)=2. Solution ... [Answer: y₁=e^(−t)(cos2t+2sin2t), y₂=e^(−t)(2cos2t−sin2t)] *(complex eigenvalue case)*

> **Q9-Q6:** General solution of x'=4x−y+2, y'=5x−2y+t is ... [Answer: x=2c₁e^(3t)+c₂e^(−t)+t/9−14/9; y=c₁e^(3t)+5c₂e^(−t)+4t/9−41/9]

> **Q10-Q1:** Rewriting nth-order ODE as first-order system — identify matrix A [technique: companion matrix]

> **Q10-Q2 (IVP):** Solve a 2×2 system IVP [details not fully readable from PDF — matrix/answer not rendered]

> **Q10-Q3:** General solution of a 2×2 system [details not fully readable from PDF]

---

### T16 — REWRITING HIGHER-ORDER ODE AS SYSTEM

**Quiz appearances:** Q10 (Q1) | **Total: 1**
**⚠ Likely on final:** Moderate — standard conversion technique

> [!tip] Algorithm

For y^(n) + a_{n-1}y^{(n-1)} + ... + a₁y' + a₀y = f(t):
```
Let x₁ = y, x₂ = y', x₃ = y'', ..., xₙ = y^(n-1)
Then:
x₁' = x₂
x₂' = x₃
...
x_{n-1}' = xₙ
xₙ' = f(t) − a₀x₁ − a₁x₂ − ... − a_{n-1}xₙ

Matrix form: x' = Ax + F where A is the companion matrix
```

#### Companion Matrix (2nd order: y'' + by' + cy = 0)
```
A = [[0, 1], [−c, −b]]
```

---

### T17 — 1ST-ORDER LINEAR ODE: INTEGRATING FACTOR

**Midterm appearances:** M1B (Q1a,Q1b), M1W (Q1a,Q1b) | **Total: 4** (both midterms, worth 6 pts each)
**⚠ Likely on final:** HIGH — both midterms opened with this; appeared in two variants (trig RHS, algebraic RHS)

#### Core Structure
`y' + P(x)y = Q(x)` → integrating factor μ(x) = e^∫P(x)dx

> [!tip] Algorithm

```
1. Get to standard form: y' + P(x)y = Q(x)
   → if given xy' + ny = f: divide through by x first
2. Compute μ = e^∫P(x)dx
3. Multiply both sides: (μy)' = μQ(x)
4. Integrate both sides: μy = ∫μQ(x)dx + C
5. Solve for y: y = (1/μ)[∫μQ(x)dx + C]
6. Apply IC to find C
```

#### Key Integrals (from midterms)
| Integral | Result |
|---|---|
| ∫e^(ax)sin(bx)dx | e^(ax)(a·sin(bx)−b·cos(bx))/(a²+b²) + C |
| ∫e^(ax)cos(bx)dx | e^(ax)(a·cos(bx)+b·sin(bx))/(a²+b²) + C |
| ∫x²√(x³+k)dx | (2/9)(x³+k)^(3/2) + C [sub u=x³+k] |

> [!warning] Common Traps
> ⚠ If ODE is NOT in standard form (e.g., xy'+3y=f), divide by x FIRST before computing μ
> ⚠ μ = e^(3lnx) = x³, NOT 3x — remember e^(a·ln(x)) = x^a
> ⚠ Apply IC to FINAL y expression (after solving for C), not to the integrated form


> [!example] Verbatim Problems
> **M1B-Q1a:** y' − 4y = sin(2x), y(0) = 0. [Answer: y = −(1/5)sin(2x) − (1/10)cos(2x) + (1/10)e^(4x)]

> **M1B-Q1b:** xy' + 3y = √(x³+8), y(1) = 1. [Answer: y = (2(x³+8)^(3/2) − 45)/(9x³)]

> **M1W-Q1a:** y' − 2y = cos(3t), y(0) = 0. [Answer: y = (3/13)sin(3t) − (2/13)cos(3t) + (2/13)e^(2t)]

> **M1W-Q1b:** ty' + 3y = √(t³+3), y(1) = 2. [Answer: y = (2(t³+3)^(3/2) + 2)/(9t³)]

---

### T18 — MIXING TANK: VARIABLE VOLUME

**Midterm appearances:** M1B (Q2a–d, 6 pts), M1W (Q2a–d, 6 pts) | **Total: 8 (counting sub-parts)**
**⚠ Likely on final:** VERY HIGH — full multi-part problem on both midterms

#### Key Difference from Quiz Mixing (T5)
When rᵢₙ ≠ rₒᵤₜ: **V(t) = V₀ + (rᵢₙ − rₒᵤₜ)t** — volume changes over time, so the coefficient of Q is not constant and the integrating factor involves a non-trivial exponential.

> [!tip] Algorithm

```
1. Overflow time: t_overflow = (V_max − V₀)/(rᵢₙ − rₒᵤₜ)
2. ODE: Q' = rᵢₙ·cᵢₙ − rₒᵤₜ·(Q/V(t))
3. Standard form: Q' + [rₒᵤₜ/V(t)]·Q = rᵢₙ·cᵢₙ
4. μ = e^∫(rₒᵤₜ/V(t))dt = (V₀ + (rᵢₙ−rₒᵤₜ)t)^(rₒᵤₜ/(rᵢₙ−rₒᵤₜ))
5. Integrate, apply Q(0) = 0 (pure water)
6. Concentration at overflow: C(t*) = Q(t*)/V_max
```

> [!warning] Common Traps
> ⚠ V(t) = V₀ + (rᵢₙ − rₒᵤₜ)t — must use this, NOT V₀
> ⚠ When dividing to get standard form, the p(t) coefficient is rₒᵤₜ/V(t), which changes form depending on whether you simplify V(t) by factoring
> ⚠ Integrating factor exponent: rₒᵤₜ/(rᵢₙ−rₒᵤₜ), e.g. 4/5 when rₒᵤₜ=4, (rᵢₙ−rₒᵤₜ)=5


> [!example] Verbatim Problems
> **M1B-Q2:** Tank capacity 500 gal, starts with 300 gal pure water. In: 9 gal/min at 8 oz/gal. Out: 4 gal/min.
> - (a) Overflow time: (500−300)/5 = 40 min
> - (b) ODE: Q' + (4/5)/(60+t)·Q = 72, Q(0) = 0
> - (c) Solution: Q = 40(60+t) + C(60+t)^(−4/5), C = −2400·60^(4/5) ≈ −63494
> - (d) Concentration at overflow: Q(40)/500 ≈ 4.81 oz/gal

> **M1W-Q2:** Tank capacity 400 gal, starts with 300 gal pure water. In: 8 gal/min at 7 oz/gal. Out: 4 gal/min.
> - (a) Overflow time: (400−300)/4 = 25 min
> - (b) ODE: Q' + 1/(t+75)·Q = 56, Q(0) = 0
> - (c) Solution: Q = (28t²+4200t)/(t+75) [C=0 in this case]
> - (d) Concentration at overflow: Q(25)/400 = 3.0625 oz/gal

---

### T19 — EQUILIBRIA: FULL STABILITY ANALYSIS (Autonomous, Nonlinear)

**Midterm appearances:** M1B (Q3a,b), M1W (Q3a,b) | **Quiz appearances:** Q2,Q3 | **Total: 8**
**⚠ Likely on final:** HIGH — appeared on every early assessment; midterm requires full written analysis

#### Full Algorithm (midterm level — must show work)
```
1. Set y' = f(y) = 0, factor completely
2. List all equilibria y*
3. For each interval between equilibria: test sign of f(y) with a sample point
4. Classify:
   - f(y) changes − to +: UNSTABLE (moves away on both sides)
   - f(y) changes + to −: STABLE (moves toward on both sides)
   - Consistent sign: semi-stable (moves toward on one side, away on the other)
5. For IVP: determine which equilibrium y₀ moves toward
   → lim_{t→∞} y(t) = nearest stable equilibrium in the direction f(y₀) pushes
```

#### Sign Chart Method
```
y' = y(y−a)(y−b)(y−c)...  (a < b < c < ...)
Equilibria: 0, a, b, c...
Test intervals: (−∞,0), (0,a), (a,b), (b,c), (c,∞)
Each factor contributes a sign change at its zero.
```

> [!example] Verbatim Problems
> **M1B-Q3a:** y' = y³−6y²+5y = y(y−1)(y−5). Equilibria: y=0 (unstable), y=1 (stable), y=5 (unstable).
> **M1B-Q3b:** y' = y³−6y²+5y, y(0)=4. lim_{x→∞} f(x) = 1 (y₀=4 is between unstable y=1 and y=5, moves toward y=1).

> **M1W-Q3a:** y' = y³−7y²+10y = y(y−2)(y−5). Equilibria: y=0 (unstable), y=2 (stable), y=5 (unstable).
> **M1W-Q3b:** y' = y³−7y²+10y, y(0)=3. lim_{x→∞} f(x) = 2.

---

### T20 — UNDETERMINED COEFFICIENTS: FULL IVP (Midterm Level)

**Midterm appearances:** M2B (Q1a,b,c), M2W (Q1a,b,c) | **Total: 6 sub-parts**
**⚠ Likely on final:** VERY HIGH — both midterms: find yₕ → find yₚ → solve IVP. Full 6-pt problem.

#### The Three-Step Midterm Pattern
```
Step 1 (2 pts): Find yₕ — solve homogeneous via characteristic equation
Step 2 (2 pts): Find yₚ — undetermined coefficients guess + solve for coefficients
Step 3 (2 pts): Solve IVP — y = yₕ + yₚ, apply y(0) and y'(0) → 2×2 system for c₁,c₂
```

#### Guess Form: When RHS is te^(at)
```
yₚ = (At + B)e^(at)
y'ₚ = Ae^(at) + a(At+B)e^(at) = (aAt + A + aB)e^(at)
y''ₚ = a²(At+B)e^(at) + 2aAe^(at) = (a²At + a²B + 2aA)e^(at)
Plug in → collect coeff of te^(at) and e^(at) → solve for A, B
```

#### Guess Form: When RHS is xe^(ax)
Same as above. Collect: coeff of x·e^(ax) and e^(ax) separately.

> [!warning] Common Traps
> ⚠ When applying IVP: use y' of the FULL solution (yₕ+yₚ), not just yₕ
> ⚠ yₚ derivative: chain rule applies to both the polynomial AND the exponential
> ⚠ Check: is e^(at) a root of the char equation? If yes, multiply guess by t (or t²)


> [!example] Verbatim Problems
> **M2B-Q1:** y''+5y'+4y = te^(−3t), y(0)=0, y'(0)=0.
> - yₕ = c₁e^(−t) + c₂e^(−4t)
> - yₚ = (−t/2 + 1/4)e^(−3t) [a=−1/2, b=1/4]
> - IVP: c₁=1/12, c₂=−1/3 → y = (−t/2+1/4)e^(−3t) + (1/12)e^(−t) − (1/3)e^(−4t)

> **M2W-Q1:** y''−4y'+3y = 2xe^(−x), y(0)=0, y'(0)=0.
> - yₕ = c₁e^x + c₂e^(3x)
> - yₚ = (x/4 + 3/16)e^(−x)
> - IVP: c₁=−1/4, c₂=1/16 → y = (x/4+3/16)e^(−x) − (1/4)e^x + (1/16)e^(3x)

---

### T21 — SPRING-MASS IVP (Full Physical Setup → Solve)

**Midterm appearances:** M2B (Q2a,b,c), M2W (Q2a,b,c) | **Total: 7 sub-parts**
**⚠ Likely on final:** VERY HIGH — both midterms; full physical-to-math translation required

#### Physical Setup → IVP Translation
```
Given: mass m, static stretch ΔL, damping coeff c, initial displacement d, initial velocity v
1. Find k: mg = kΔL → k = mg/ΔL  [use g = 9.8 m/s²]
2. Write ODE: my'' + cy' + ky = 0  (free damped)
3. Set ICs: 
   - "pulled down" → y(0) = −d  (negative = downward displacement)
   - "downward velocity" → y'(0) = −v  (negative = downward)
   - "pushed up" → y(0) = +d
```

#### Midterm Variants
| Midterm | m | ΔL | c | k | roots | type |
|---|---|---|---|---|---|---|
| M2B | 2 kg | 196 cm | 8 | 10 | −2±i | underdamped |
| M2W | 2 kg | 98 cm | 4 | 20 | −1±3i | underdamped |

#### Critical Damping Formula
`c_crit = 2√(mk)`

| Midterm | m | k | c_crit |
|---|---|---|---|
| M2B | 2 | 10 | √80 = 4√5 ≈ 8.94 |
| M2W | 2 | 20 | √160 = 4√10 ≈ 12.65 |

> [!example] Verbatim Problems
> **M2B-Q2:** m=2kg, ΔL=196cm, c=8 kg·s/m, pulled down 90cm, initial downward v=3 m/s.
> - k = 19.6/1.96 = 10; IVP: 2y''+8y'+10y=0, y(0)=−0.9, y'(0)=−3
> - Roots: r=−2±i; y=e^(−2t)(c₁cost+c₂sint)
> - ICs: c₁=−0.9, c₂=−4.8 → y = −e^(−2t)(0.9cost+4.8sint)
> - c_crit = 4√5 ≈ 8.94

> **M2W-Q2:** m=2kg, ΔL=98cm, c=4 kg/s, pulled down 70cm, initial downward v=2 m/s.
> - k = 19.6/0.98 = 20; IVP: 2y''+4y'+20y=0, y(0)=−0.7, y'(0)=−2
> - Roots: r=−1±3i; y=e^(−t)(c₁cos3t+c₂sin3t)
> - ICs: c₁=−0.7, c₂=−0.9 → y = −e^(−t)(0.7cos3t+0.9sin3t)
> - c_crit = 4√10 ≈ 12.65

---

### T22 — VARIATION OF PARAMETERS + ABEL'S FORMULA (Midterm Level)

**Midterm appearances:** M2B (Q3), M2W (Q3) | **Quiz appearances:** Q6 | **Total: 5**
**⚠ Likely on final:** HIGH — midterm Q3 is 4 pts, requires Abel's formula for Wronskian

#### Abel's Formula
For y'' + p(t)y' + q(t)y = 0, with fundamental pair {y₁, y₂}:
```
W(y₁,y₂)(t) = c₀ · e^(−∫p(t)dt)
```
where c₀ is a nonzero constant.

**Key implication:** W(y₁,y₂) for y''+3/t·y'+4y=0 is:
`W = c₀·e^(−∫3/t dt) = c₀·e^(−3lnt) = c₀·t^(−3)`

Then 1/W = t³/c₀, so the VoP integrals become:
`u₁ = −∫y₂·g·(1/W)dt = −(1/c₀)∫y₂·t³·cos3t dt`
`u₂ = +∫y₁·g·(1/W)dt = +(1/c₀)∫y₁·t³·cos3t dt`

#### Full Algorithm (Midterm Level)
```
1. Identify p(t) from standard form y''+p(t)y'+q(t)y = g(t)
2. Compute W via Abel: W(t) = c₀·e^(−∫p(t)dt)
3. Write VoP formulas:
   u₁ = −∫(y₂·g/W)dt,  u₂ = +∫(y₁·g/W)dt
4. Substitute W = c₀·t^n (whatever Abel gives)
5. General solution: y = c₁y₁ + c₂y₂ + u₁y₁ + u₂y₂
6. Do NOT evaluate the integrals (midterm says so explicitly)
```

> [!example] Verbatim Problems
> **M2B-Q3:** y'' + (3/t)y' + 4y = cos3t. y₁,y₂ fundamental solutions of homogeneous.
> W = c₀t^(−3). Solution: y = c₁y₁+c₂y₂ − (1/c₀)y₁∫y₂t³cos3t dt + (1/c₀)y₂∫y₁t³cos3t dt

> **M2W-Q3:** y'' + (4/t)y' + 5y = sin2t. y₁,y₂ fundamental solutions of homogeneous.
> W = c₀t^(−4). Solution: y = c₁y₁+c₂y₂ − (1/c₀)y₁∫y₂t⁴sin2t dt + (1/c₀)y₂∫y₁t⁴sin2t dt

---

## SECTION 2 — QUICK REFERENCE CHECKLISTS

### Before Any Problem
- [ ] What ORDER is the ODE? (1st, 2nd, higher)
- [ ] Is it LINEAR or NONLINEAR?
- [ ] HOMOGENEOUS or NONHOMOGENEOUS?
- [ ] Is it a SYSTEM (x' = Ax)?
- [ ] Is there an IVP? (need to solve for c₁, c₂)
- [ ] Does it involve LAPLACE? (look for unit step, piecewise, δ)

### Technique Selection Decision Tree
```
ODE given
├─ 1st order
│   ├─ Autonomous (y'=f(y)) → equilibria analysis (T2, T19)
│   ├─ Separable → separation of variables (T6)
│   ├─ Linear (y'+p(t)y=g) → integrating factor (T17)
│   │   └─ Variable volume tank → T18
│   ├─ Bernoulli → substitution v=y^(1-n) (T7)
│   ├─ Physical model → Newton's cooling (T4) or mixing (T5,T18)
│   └─ Can't solve analytically → numerical methods (T1)
├─ 2nd order, constant coeff, homogeneous
│   └─ Characteristic equation (T8); spring-mass (T21)
├─ 2nd order, constant coeff, nonhomogeneous
│   ├─ RHS is polynomial/exp/trig → undetermined coefficients (T9, T20)
│   └─ General g(t) or variable coeff → variation of parameters (T10, T22)
│       └─ Variable coeff: use Abel's formula for W (T22)
├─ Spring-mass physical setup (T21) → T8 or T11
├─ 3rd or higher order → cubic char poly (T13)
├─ Laplace (piecewise forcing, δ, unit step) → (T12)
└─ System x' = Ax
    ├─ Find eigenvalues/eigenvectors (T14)
    └─ Assemble solution per case (T15)
        ├─ Real distinct: c₁e^(λ₁t)v₁ + c₂e^(λ₂t)v₂
        ├─ Complex: e^(αt)[p·cos(βt)−q·sin(βt)] + ...
        └─ Repeated: c₁e^(λt)v + c₂e^(λt)(tv+w)
```

---

## SECTION 3 — MIDTERM PATTERN ANALYSIS

### What Both Midterms Had in Common
Both Mid1 and Mid2 followed **identical structure**:
- **Problem 1 (6 pts):** Two 1st-order linear ODE IVPs — integrating factor, non-trivial RHS (trig or power-of-polynomial)
- **Problem 2 (6 pts):** Full mixing tank (Mid1) or full spring-mass (Mid2) — physical setup → ODE → solve → evaluate at specific time
- **Problem 3 (4–5 pts):** Equilibria analysis (Mid1) or Variation of Parameters + Abel's formula (Mid2)

### Final Exam Prediction
Based on midterm patterns + quiz coverage, the final will likely include:
1. **Systems of ODEs** (eigenvalue method) — most recent material, heavily quizzed, not yet tested on midterm
2. **Laplace transforms** — dedicated quiz week, not on midterms
3. **Spring-mass or mixing** — appeared on every midterm
4. **1st-order linear ODE or equilibria** — appeared on every midterm
5. **Undetermined coefficients or VoP** — appeared on Mid2, high probability of return

---

## SECTION 4 — BOOK PROBLEMS BY TECHNIQUE (Practice Problems.md)

---

### §1.2 — ODE ORDER, SOLUTION VERIFICATION, DIRECT INTEGRATION
*Introductory problems — no technique classification; test order identification and solution verification by substitution.*

> **1.2.1** `[order identification]` Identify the order of four ODEs
> **1.2.4** `[direct integration — 1st/2nd/3rd order]` Solve IVPs by antidifferentiation: $y'=-xe^x$; $y'=x\sin x^2$; $y'=\tan x$; $y''=x^4$; $y''=xe^{2x}$; $y''=-x\sin x$; $y'''=x^2e^x$; $y'''=2+\sin 2x$; $y'''=2x+1$
> **1.2.5** `[solution verification — 1st order, substitute + check IC]` Verify four functions solve their given IVPs
> **1.2.6** `[solution verification — 2nd order, substitute + check two ICs]` Verify four functions solve their given IVPs
> **1.2.7** `[applied — projectile motion, gravity only]` Object launched 320 ft up at 128 ft/s; find max height and time to ground
> **1.2.9** `[solution verification — piecewise function, differentiability at join point]` Verify $y=\begin{cases}e^x-1,&x\ge0\\1-e^{-x},&x<0\end{cases}$ solves $y'=|y|+1$; use definition of derivative at $x=0$
> **1.2.10** `[solution verification — one-parameter family + singular solution]` Verify $y=c^2+cx+2c+1$ and singular solution $y_1=-x(x+4)/4$ both satisfy the same ODE; identify intervals

*Source: `Problems/Practice Problems.md` — full course problem list, Weeks 1–10*
*Cross-referenced to techniques T1–T22. Select problems most relevant to exam techniques listed.*

---

### T17 / T18 — 1ST-ORDER LINEAR ODE + INTEGRATING FACTOR (§1.3, §2.1)
*Constant and variable coefficient; includes mixing tanks*

**General solution — homogeneous ($g=0$), find explicit closed form:**
> **1.3.1** `[homogeneous — constant coefficient, exponential decay]` $y' + ay = 0$
> **1.3.3 / 2.1.3** `[homogeneous — variable coefficient, $p(x)=\ln x / x$]` $xy' + (\ln x)y = 0$
> **1.3.5 / 2.1.5** `[homogeneous — variable coefficient, $p(x)=1/x^2$]` $x^2y' + y = 0$

**General solution — nonhomogeneous ($g\ne0$), find $y_h + y_p$:**
> **1.3.12** `[nonhomogeneous — constant RHS, direction field requested]` $y' + 3y = 1$
> **1.3.13 / 2.1.13** `[nonhomogeneous — rational $p(x)$, rational $g(x)$]` $y' + (1/x - 1)y = -2/x$
> **1.3.17 / 2.1.17** `[nonhomogeneous — singular $p(x)$ at $x=1$, mixed RHS]` $y' + \frac{4}{x-1}y = \frac{1}{(x-1)^5} + \frac{\sin x}{(x-1)^4}$
> **1.3.22 / 2.1.22** `[nonhomogeneous — factored variable coefficient, polynomial RHS]` $(x-2)(x-1)y' - (4x-3)y = (x-2)^3$

**IVP — find unique solution satisfying $y(x_0)=y_0$:**
> **1.3.6 / 2.1.6** `[IVP — homogeneous, rational $p(x)$, IC at $x_0=1$]` $y' + \frac{1+x}{x}y = 0$, $y(1)=1$
> **1.3.9 / 2.1.9** `[IVP — homogeneous, rational $p(x)$, IC at $x_0=0$]` $y' - \frac{2x}{1+x^2}y = 0$, $y(0)=2$
> **1.3.10 / 2.1.10** `[IVP — homogeneous, parametric $k$, power-law solution]` $y' + \frac{k}{x}y = 0$, $y(1)=3$
> **1.3.31 / 2.1.31** `[IVP — nonhomogeneous, Euler-type $p(x)=2/x$, polynomial RHS]` $xy' + 2y = 8x^2$, $y(1)=3$
> **1.3.33 / 2.1.33** `[IVP — nonhomogeneous, Gaussian $\mu$, linear RHS]` $y' + 2xy = x$, $y(0)=3$

**IVP — answer left as definite integral (non-elementary antiderivative):**
> **1.3.38** `[IVP — definite-integral form, $\mu=e^{x^2}$, $g=x^2$]` $y' + 2xy = x^2$, $y(0)=3$
> **1.3.39 / 2.1.39** `[IVP — definite-integral form, $\mu=x$, $g=\sin x/x$]` $y' + \frac{1}{x}y = \frac{\sin x}{x^2}$, $y(1)=2$

**Applied — physical/biological model, derive + solve ODE:**
> **1.3.43 / 2.1.43** `[applied — pharmacokinetics/glucose, constant infusion rate, find equilibrium]` $G' = -\lambda G + r$, $G(0)=G_0$; find $G(t)$ and $\lim_{t\to\infty}G(t)$
> **4.2.9** `[applied — mixing tank, constant volume, constant inflow concentration]` 10 lb salt/60 gal; ½ lb/gal in at 6 gal/min, same rate out; find $Q(t)$
> **4.2.13** `[applied — gas dilution / ventilation, find minimum safe intake rate]` Lab: gas produced $q_1$ ft³/min, intake $q_2$ ft³/min; find min $q_2$
> **4.2.19** `[applied — two-tank cascade, sequential dilution, find both concentrations]` $T_1\to T_2\to$ out; find $c_1(t)$, $c_2(t)$

**Theoretical — general structure, limiting behavior, or substitution:**
> **1.3.45 / 2.1.45** `[theoretical — general formula for $y'+\alpha y=f$; limiting behavior when $\lim f=L$]`
> **1.3.47 / 2.1.47** `[theoretical — nonlinear-to-linear reduction via $z=g(y)$]`

**Pattern:** Standard form $Q' + pQ = g$; compute $\mu = e^{\int p\,dt}$; apply IC.

---

### T4 — NEWTON'S COOLING (§4.2)

**Standard — constant ambient, find $k$ from one intermediate reading, evaluate at target time:**
> **4.2.1** `[standard cooling — two readings given, find temperature at later time]` Thermometer: 70°F room → 12°F freezer; reads 40°F after 30s; find reading after 2 min
> **4.2.4** `[standard cooling — find later temperature AND two specific times]` Thermometer 212°F → 70°F room; reads 125°F after 2 min; (a) temp after 4 min; (b) when reads 72°F; (c) when reads 69°F

**Inverse problem — given two temperature drops, recover unknown initial temperature:**
> **4.2.6** `[inverse problem — two $\Delta T$ measurements, recover $T(0)$]` Object in 20°C room; drops 5°C in 4 min and 7°C in 8 min; find initial temperature

**Coupled system — both object and medium change, derive reduced ODE:**
> **4.2.17** `[coupled cooling — medium not fixed, derive ODE in $T$ alone, find both limits]` $T'=-k(T-T_m)$ with $T_m$ also evolving; eliminate $T_m$; find $T(t)$, $T_m(t)$, and $\lim_{t\to\infty}$

**Pattern:** $T' = -k(T-T_m)$ → $T(t) = T_m + Ce^{-kt}$ → use two data points to find $k$.

---

### T5 — MIXING TANK (Constant Volume)
*See T17/T18 above — same algorithm. All §4.2 mixing problems are listed there.*

---

### T4 alt — RADIOACTIVE DECAY / EXPONENTIAL GROWTH (§4.1)

**Pure decay — find $Q(t)$ or half-life from rate constant:**
> **4.1.1** `[pure decay — half-life given, find $Q(t)$]` Half-life 3200 yr; $Q(0)=20$ g
> **4.1.3** `[pure decay — percentage loss given, find half-life]` Loses 25% in 10 min

**Production + decay equilibrium — find $Q(t)$ and steady state:**
> **4.1.11** `[production-decay balance — linear source, proportional sink, find equilibrium]` Candy: produced 500 lb/wk, consumed at $Q/10$ lb/wk; find $Q(t)$, $\lim Q$
> **4.1.15** `[production-decay balance — constant creation, percentage theft, find equilibrium]` Gold created 1 oz/hr, stolen at 5%/hr; find $W(t)$, $\lim W$

**Threshold / minimum capacity — find critical value from ODE behavior:**
> **4.1.17** `[threshold — find minimum tank capacity so process continues indefinitely]` Water in at 10 gal/min, leaks out at rate = quantity; find min capacity

**Financial model — continuous compounding + payment:**
> **4.1.22** `[financial — mortgage ODE, derive $P'=rP-M$, solve, find payment $M$]`
> **4.1.23** `[financial — accelerated repayment, find payoff time $T(\alpha)$ and total savings]`

**Motion with linear air resistance (§4.3) — $mv'=mg-kv$ or similar:**
> **4.3.1** `[terminal velocity — sliding friction proportional to speed, find $v(t)$ and $v_\infty$]` Firefighter on pole; $k=2.5$ lb·s/ft; find $v(t)$, terminal velocity
> **4.3.5** `[upward throw with drag — find max height]` Stone ½ lb from 5 ft; $k=1/128$; find max height
> **4.3.8** `[position formula derivation — integrate $v(t)$ to get $y(t)$]` Show $y(t)=y_0+\frac{m}{k}(v_0-v-gt)$
> **4.3.14** `[theoretical — general nonlinear drag, existence of terminal speed, two cases]` If $\lim f(s)\le mg$: no terminal speed; if $\lim f(s)>mg$: $s\to s_T$ where $f(s_T)=mg$
> **4.3.17** `[escape velocity — inverse-square gravity, nonlinear ODE, find $v_\text{esc}$]` Space probe 200 mi above Earth

---

### T6 — SEPARATION OF VARIABLES (§2.2)

**Pure separation — polynomial or rational separable form, find general solution:**
> **2.2.1** `[rational separable — $f(x)/g(y)$ form, implicit solution]` $y' = (3x^2+2x+1)/(y-2)$
> **2.2.3** `[rational separable — $y$ side factors, implicit solution]` $xy' + y^2 + y = 0$
> **2.2.6** `[nonlinear separable — irrational $y$-factor, requires trig substitution]` $x^2yy' = (y^2-1)^{3/2}$

**IVP — separate, integrate, apply IC:**
> **2.2.11** `[IVP — rational separable, $y(1)=4$]` $y' = (x^2+3x+2)/(y-2)$, $y(1)=4$
> **2.2.13** `[IVP — implicit $y$-side after separation, trig $x$-side]` $(3y^2+4y)y' + 2x + \cos x = 0$, $y(0)=1$
> **2.2.17** `[IVP — perfect square in $y$, rational $x$-side]` $y'(x^2+2) + 4x(y^2+2y+1)=0$, $y(1)=-1$
> **2.2.19** `[IVP — linear in $x$ and $y$, straightforward]` $y'=2x/(1+2y)$, $y(2)=0$

**Explicit solution via identity:**
> **2.2.25** `[trig substitution — separate, use $\sin(A-B)$ identity to get explicit $y$]` $y'\sqrt{1-x^2}+\sqrt{1-y^2}=0$

**Population / logistic model — separable nonlinear ODE, analyze long-term behavior:**
> **2.2.27** `[logistic — $y'=ay-by^2$, partial fractions, behavior for $y_0\ge0$ vs $y_0<0$]`
> **2.2.28** `[logistic — $P'=aP(1-\alpha P)$, find $P(t)$ explicitly, find $\lim P$]`

**Epidemic model — $I'=rI(S-I)$, separable Bernoulli-like:**
> **2.2.29** `[epidemic — separable logistic, show $\lim I(t)=S$]`
> **2.2.33** `[epidemic with harvest — add $-q$ term, apply bifurcation analysis from 2.2.31]`

**Bifurcation analysis — direction field, qualitative behavior as parameter varies:**
> **2.2.31** `[bifurcation — $y'=ay-by^2-q$; critical value $q_0=a^2/4b$; three qualitative regimes]`

---

### T3 — EXISTENCE AND UNIQUENESS (§2.3)

**Identify region — locate where $f$ and $\partial f/\partial y$ are both continuous:**
> **2.3.1** `[discontinuity from denominator — $\sin x=0$ at $x=n\pi$; $\partial f/\partial y$ continuous everywhere else]` $y'=(x^2+y^2)/\sin x$
> **2.3.3** `[discontinuity from $\tan$ — fails at $xy=\pi/2+n\pi$; curve in the plane]` $y'=\tan xy$
> **2.3.7** `[continuous everywhere — $\ln(1+x^2+y^2)>0$ for all $(x,y)$; unique solution on $(-\infty,\infty)$]` $y'=\ln(1+x^2+y^2)$

**Compare theorems — nonlinear Thm 2.3.1 vs. linear Thm 2.1.2:**
> **2.3.14** `[theoretical comparison — linear ODE satisfies Thm 2.3.1 but Thm 2.1.2 gives larger interval]` Apply both theorems to $y'+p(x)y=q(x)$

**Non-unique solution — $\partial f/\partial y$ fails at equilibrium, multiple solutions exist:**
> **2.3.17** `[non-uniqueness — $\partial f/\partial y=(y-1)^{-2/3}$ blows up at $y=1$; trivial + nontrivial solutions both exist]` $y'=3x(y-1)^{1/3}$; identify where unique, where not
> **2.3.19** `[explicit solution + interval of uniqueness — find largest open interval on which solution is unique]` Same equation, $y(0)=9$; solve explicitly; identify maximal interval

---

### T7 — BERNOULLI EQUATION
*Not directly in Practice Problems — technique introduced via quiz. Algorithm: $v = y^{1-n}$, reduces to linear.*

---

### T1 — NUMERICAL METHODS (§3.1, §3.2, §3.3)

**Euler — single step size, nonlinear ODE:**
> **3.1.1** `[Euler — nonlinear $f(x,y)$, single $h$, compute 3 steps]` $y'=2x^2+3y^2-2$, $y(2)=1$; $h=0.05$
> **3.1.3** `[Euler — mixed nonlinear + linear terms, single $h$]` $y'+3y=x^2-3xy+y^2$, $y(0)=2$; $h=0.05$

**Euler — multiple step sizes, compare accuracy against exact solution:**
> **3.1.7** `[Euler — convergence study, linear ODE with known exact solution]` $y'+\frac{2}{x}y=\frac{3}{x^3}+1$; exact $y=\frac{1}{3x^2}(9\ln x+x^3+2)$; $h=0.1,0.05,0.025$
> **3.1.11** `[Euler — nonlinear implicit ODE, convergence study]` $(3y^2+4y)y'+2x+\cos x=0$; three step sizes
> **3.1.15** `[Euler — Gaussian integrating factor, compare three step sizes on $[0,2]$]` $y'+2xy=x^2$, $y(0)=3$

**Improved Euler (Heun) — two-stage predictor-corrector:**
> **3.2.6** `[Improved Euler — exponential exact solution, measure improvement over Euler]` $y'+3y=7e^{4x}$; exact $y=e^{4x}+e^{-3x}$
> **3.2.7** `[Improved Euler — same ODE as 3.1.7, direct accuracy comparison]`
> **3.2.11** `[Improved Euler — same nonlinear ODE as 3.1.11]`

**Runge-Kutta (RK4) — highest accuracy comparison:**
> **3.3.1** `[RK4 — same nonlinear ODE as 3.1.1, observe error reduction]`
> **3.3.3** `[RK4 — same mixed ODE as 3.1.3]`
> **3.3.7** `[RK4 — same linear ODE as 3.1.7, three-method accuracy comparison]`

---

### T8 — 2ND-ORDER CHARACTERISTIC EQUATION (§5.1, §5.2)

**Solution verification — substitute into ODE, confirm fundamental set:**
> **5.1.1** `[verify distinct real roots — $e^{2x},e^{5x}$; then solve 4 IVP variants]` $y''-7y'+10y=0$
> **5.1.2** `[verify complex roots — $e^x\cos x, e^x\sin x$; solve IVP variants]` $y''-2y'+2y=0$
> **5.1.3** `[verify repeated root — $e^x, xe^x$; solve IVP variants]` $y''-2y'+y=0$
> **5.1.4** `[verify non-constant coefficient — rational solutions $1/(x\pm1)$; solve IVP; verify Abel]` $(x^2-1)y''+4xy'+2y=0$

**Reduction of order — given $y_1$, find $y_2=uy_1$ via $u'$ formula:**
> **5.1.9** `[theoretical — derive $u'=Ke^{-P}/y_1^2$ formula; show result is fundamental]`
> **5.1.11** `[reduction of order — repeated root, $y_1=e^{3x}$, find $y_2=xe^{3x}$]` $y''-6y'+9y=0$
> **5.1.15** `[reduction of order — Euler-Cauchy, $y_1=x^a$, find $y_2$ via reduction]` $x^2y''-(2a-1)xy'+a^2y=0$

**Linear combinations of fundamental sets:**
> **5.1.27** `[theoretical — $\{z_1,z_2\}$ is fundamental iff transformation matrix is nonsingular ($\alpha\delta-\beta\gamma\ne0$)]`
> **5.1.37** `[canonical pair — $y_1(x_0)=1,y_1'(x_0)=0$; $y_2(x_0)=0,y_2'(x_0)=1$; general IVP solution formula]`
> **5.1.41** `[canonical pair — explicit construction for $(x^2-1)y''+4xy'+2y=0$; solve general IVP]`

**General solution — distinct real roots ($b^2-4ac>0$):**
> **5.2.1** `[distinct real — two negative/opposite roots]` $y''+5y'-6y=0$ → $r=1,-6$
> **5.2.3** `[distinct real — both negative roots]` $y''+8y'+7y=0$ → $r=-1,-7$

**General solution — complex roots ($b^2-4ac<0$):**
> **5.2.2** `[complex — $r=2\pm i$, exponential envelope]` $y''-4y'+5y=0$
> **5.2.5** `[complex — $r=-1\pm 3i$, decaying oscillation]` $y''+2y'+10y=0$
> **5.2.11** `[complex — coefficient $\ne1$ on $y''$; divide first]` $4y''+4y'+10y=0$

**General solution — repeated root ($b^2-4ac=0$):**
> **5.2.4** `[repeated — $r=2$ double root, $y=(c_1+c_2x)e^{2x}$]` $y''-4y'+4y=0$

**IVP at $x_0=0$ — find $c_1,c_2$ from standard ICs:**
> **5.2.15** `[IVP at $x_0=0$ — distinct real roots, $6y''+y'-y=0$]` $y(0)=-1$, $y'(0)=3$

**IVP at $x_0\ne0$ — shift argument or solve system:**
> **5.2.22** `[shift theorem — $z(x)=y(x-x_0)$ also solves constant-coeff ODE; restates IVP solution]`
> **5.2.23** `[IVP at $x_0=1$ — distinct real roots, set up $2\times2$ system for $c_1,c_2$]` $y''+3y'+2y=0$, $y(1)=-1$, $y'(1)=4$
> **5.2.25** `[IVP at $x_0=1$ — repeated root $r=7$, $y=(c_1+c_2x)e^{7x}$]` $y''-14y'+49y=0$, $y(1)=2$, $y'(1)=11$

**Abel's formula — Wronskian without knowing $y_1,y_2$ explicitly:**
> **5.1.6** `[Abel — variable coefficient, $W(x)=W(\pi)\cdot e^{-\int_{x_0}^x p\,dt}$, given $W(\pi)=0$]`
> **5.1.8** `[Abel — Bessel's equation, given $W(1)=1$, find $W(x)$]`

---

### T9 / T20 — UNDETERMINED COEFFICIENTS (§5.3, §5.4, §5.5)

**Polynomial RHS — guess $y_p$ = polynomial of same degree:**
> **5.3.1** `[polynomial RHS degree 2 — $\alpha$ not a root, straightforward guess]` $y''+5y'-6y=22+18x-18x^2$; $y_p=A+Bx+Cx^2$
> **5.3.2** `[polynomial RHS degree 1]` $y''-4y'+5y=1+5x$
> **5.3.3** `[polynomial RHS degree 3]` $y''+8y'+7y=-8-x+24x^2+7x^3$
> **5.3.6** `[polynomial RHS degree 1 + full IVP]` $y''+6y'+10y=22+20x$, $y(0)=2$, $y'(0)=-2$

**Euler-Cauchy with polynomial-type RHS — variable coefficient, transform $x=e^t$:**
> **5.3.9** `[Euler-Cauchy — $x^2y''$, power-function RHS $x^{1/2}$]` $x^2y''-7xy'+7y=13x^{1/2}$
> **5.3.13** `[Euler-Cauchy — power-function RHS $x^4$]` $x^2y''-3xy'+13y=2x^4$

**Exponential RHS, $\alpha$ not a root — guess $y_p=Ae^{\alpha x}$:**
> **5.3.17** `[pure exponential RHS — $\alpha=2$, char roots $2\pm i$, no resonance]` $y''-4y'+5y=e^{2x}$
> **5.3.21** `[pure exponential RHS — $\alpha=-3$, char roots $-3\pm i$, no resonance]` $y''+6y'+10y=e^{-3x}$

**Trig RHS, $\omega$ not a root — guess $y_p=A\cos\omega x+B\sin\omega x$:**
> **5.3.24** `[trig RHS — repeated real root $r=4$, $\omega=1$ not a root]` $y''-8y'+16y=23\cos x-7\sin x$
> **5.3.27** `[trig RHS — complex roots $-3\pm2i$, $\omega=1$ not a root]` $y''+6y'+13y=18\cos x+6\sin x$
> **5.5.1** `[trig RHS — distinct real roots, $\omega=1$ not a root]` $y''+3y'+2y=7\cos x-\sin x$

**Trig RHS resonance — $\omega$ is imaginary part of root, multiply guess by $x$:**
> **5.5.19** `[resonance — pure imaginary roots $\pm3i$, $\omega=3$ matches → $y_p=x(A\cos3x+B\sin3x)$]` $y''+9y=-6\cos3x-12\sin3x$

**Exponential × polynomial RHS, $\alpha$ not a root — guess $y_p=e^{\alpha x}\cdot P_n(x)$:**
> **5.4.1 / 5.4.15** `[exp × linear RHS — $\alpha=3$ not a root, $y_p=e^{3x}(A+Bx)$]` $y''-3y'+2y=e^{3x}(1+x)$
> **5.4.5** `[exp × quadratic RHS — $\alpha=-1$ not a root, $y_p=e^{-x}(A+Bx+Cx^2)$]` $y''+4y=e^{-x}(7-4x+5x^2)$
> **5.4.18** `[exp × linear RHS — check if $\alpha=1$ is root before guessing]` $y''+2y'-3y=-16xe^x$

**Exponential × polynomial RHS, $\alpha$ is simple root — multiply guess by $x$:**
> **5.4.7** `[resonance mult 1 — $r=-1$ is simple root → $y_p=xe^{-x}(A+Bx)$]` $y''-4y'-5y=-6xe^{-x}$
> **5.4.21** `[exp × linear RHS + full IVP — $\alpha=2$ not a root]` $y''+3y'-4y=e^{2x}(7+6x)$, $y(0)=2$, $y'(0)=8$

**Exponential × polynomial RHS, $\alpha$ is double root — multiply guess by $x^2$:**
> **5.4.26** `[superposition + resonance mult 2 — $\alpha=4$ double root; polynomial part separate]` $y''-8y'+16y=6xe^{4x}+2+16x+16x^2$

**Modification rule — three-case comparison (no/simple/double resonance):**
> **5.4.31** `[mult 0 — $\alpha=2$ not a root: $y_p=Ae^{2x}$]` $y''-7y'+12y=4e^{2x}$
> **5.4.32** `[mult 1 — $\alpha=4$ simple root: $y_p=Axe^{4x}$]` $y''-7y'+12y=5e^{4x}$
> **5.4.33** `[mult 2 — $\alpha=4$ double root: $y_p=Ax^2e^{4x}$]` $y''-8y'+16y=2e^{4x}$

**Exponential × trig RHS — guess $y_p=e^{\alpha x}(A\cos\beta x+B\sin\beta x)$:**
> **5.5.3** `[exp × trig — $\alpha+\beta i$ not a root]` $y''+2y'+y=e^x(6\cos x+17\sin x)$
> **5.5.5** `[exp × trig with polynomial factor — $e^x\cdot(2+x)\sin x$; guess includes $x$-polynomial]` $y''-y'+y=e^x(2+x)\sin x$
> **5.5.10** `[exp × trig — $\alpha=-1$, $\beta=1$; check against char roots]` $y''+2y'+2y=e^{-x}(8\cos x-6\sin x)$
> **5.5.23** `[exp × trig + full IVP]` $y''-2y'+2y=-e^{-x}(6\cos x+4\sin x)$, $y(0)=1$, $y'(0)=4$
> **5.5.25** `[exp × trig + full IVP]` $y''-6y'+10y=-e^{3x}(6\cos x+4\sin x)$, $y(0)=2$, $y'(0)=7$

**Superposition — RHS is sum of multiple forcing types, solve each separately:**
> **5.5.29** `[three-term superposition — exp×poly + pure exp + trig]` $y''-3y'+2y=xe^x+2e^{2x}+\sin x$
> **5.5.32** `[two-term superposition + full IVP — exp (double root resonance) + trig]` $y''-4y'+4y=6e^{2x}+25\sin x$, $y(0)=5$, $y'(0)=3$

**Rule:** If $\alpha$ is a root of char eq with multiplicity $m$: multiply $y_p$ guess by $x^m$.

---

### T10 / T22 — VARIATION OF PARAMETERS (§5.7)

**Constant coefficient — RHS not amenable to UC (transcendental, rational in $e^x$):**
> **5.7.1** `[constant coeff — $g=\tan3x$, UC impossible; VoP integral involves $\ln|\cos3x|$]` $y''+9y=\tan3x$
> **5.7.3** `[constant coeff — $g=4/(1+e^{-x})$, rational in $e^x$; UC impossible]` $y''-3y'+2y=4/(1+e^{-x})$
> **5.7.5** `[constant coeff — $g=14x^{3/2}e^x$; repeated root $r=1$, $y_1=e^x$, $y_2=xe^x$]` $y''-2y'+y=14x^{3/2}e^x$

**Variable coefficient (Euler-Cauchy) — $y_1,y_2$ given; compute $W$ and integrate:**
> **5.7.7** `[Euler-Cauchy — $y_1=x$, $y_2=1/x$; $W=x\cdot(-1/x^2)-1\cdot(1/x)=-2/x$]` $x^2y''+xy'-y=2x^2+2$
> **5.7.9** `[Euler-Cauchy — exponential $y_1,y_2$ with fractional powers; $W$ computed from given pair]` $4x^2y''+(4x-8x^2)y'+(4x^2-4x-1)y=4x^{1/2}e^x$
> **5.7.24** `[Euler-Cauchy — $y_1=1/x$, $y_2=x^3$; $W=x^3\cdot(-1/x^2)-1/x\cdot3x^2=4x^0$... compute]` $x^2y''-xy'-3y=x^{3/2}$

**Full IVP with VoP — find $y_p$ via VoP, then apply two ICs:**
> **5.7.31** `[variable coeff IVP — $y_1=x-1$, $y_2=x^2-1$; find $y_p$, apply $y(0)=3$, $y'(0)=-6$]` $(x-1)^2y''-2(x-1)y'+2y=(x-1)^2$

**Pattern:** $u_1' = -y_2g/W$, $u_2' = y_1g/W$; compute $W$ via Abel when variable-coeff.

---

### T21 — SPRING-MASS SYSTEMS (§6.1, §6.2)

**Free damped — English units (lb/ft), find displacement and/or amplitude:**
> **6.1.1** `[underdamped — compute $k$, find complex roots, write $y(t)$, find time-varying amplitude $Re^{-ct/2m}$]` 64 lb / 4 ft / $c=8$; 18 in above, 4 ft/s down
> **6.1.3** `[underdamped — small stretch (1.5 in → convert to ft), graph requested]` 8 lb / 1.5 in / $c=8$; 3 in above, 6 ft/s up
> **6.1.6** `[underdamped — large stretch (32 ft → very small $k$), resistance from medium]` 8 lb / 32 ft; 6 in above, 4 ft/s up; 1.5 lb per ft/s
> **6.1.9** `[overdamped — $k$ given directly (not via stretch), check discriminant]` 64 lb / $k=25$ lb/ft; 18 in above, released from rest; 6 lb per ft/s
> **6.1.14** `[critically damped — find $c$ that gives $c^2=4mk$; verify with given $c=12$]` 32 lb / 1 ft / $c=12$; 8 in above, released from rest

**Free damped — SI units (kg/m/N), find displacement:**
> **6.1.15** `[underdamped — SI units, $k=mg/\Delta L$ with $g=9.8$, dashpot in N·s/m]` 1 kg / 49 cm / 4 N·s/m; 10 cm above, 1 m/s down

**Forced oscillation — find steady-state (particular) solution only:**
> **6.2.1** `[forced underdamped — extract steady state $y_p=A\cos\omega t+B\sin\omega t$, ignore transient]` 64 lb / 4 ft / $c=8$; $F(t)=4\cos2t$
> **6.2.9 / 6.2.13** `[forced underdamped — small damping $c=0.5$, find steady state]` 8 lb / 8 in / $c=0.5$; $F(t)=4\cos2t$

**Forced oscillation — find full transient + steady state:**
> **6.2.15** `[overdamped forced — CGS units (gm/cm/dyne); full displacement, no sustained oscillation]` 20 gm / 5 cm / $c=400$ dyne·s/cm; released from 9 cm above

**General IVP formulas — derive solution structure for each damping regime:**
> **6.2.24** `[underdamped formula — $y=e^{-ct/2m}(c_1\cos\omega_1t+c_2\sin\omega_1t)$; solve for $c_1,c_2$ in terms of $y_0,v_0$]`
> **6.2.25** `[overdamped formula — $y=c_1e^{r_1t}+c_2e^{r_2t}$, $r_1,r_2<0$; solve for $c_1,c_2$]`
> **6.2.26** `[critically damped formula — $y=e^{r_1t}(c_1+c_2t)$; solve for $c_1,c_2$]`

**Physical setup steps (English units):** $k = w/\Delta L$ (weight in lb, stretch in ft); $m = w/32$.
**Physical setup steps (SI units):** $k = mg/\Delta L$ (mass in kg, $g=9.8$, stretch in m).

---

### T12 — LAPLACE TRANSFORMS (§8.1–8.5, §8.7)

**Forward transform — compute $F(s)$ from definition (integral):**
> **8.1.1** `[definition integral — five elementary functions: $t$, $te^{-t}$, $\sinh bt$, $e^{2t}-3e^t$, $t^2$]`
> **8.1.8** `[induction proof — $\mathcal{L}(t^n)=n!/s^{n+1}$ from $\mathcal{L}(1)=1/s$ and differentiation w.r.t. $s$]`
> **8.1.12** `[integration theorem proof — $\mathcal{L}(\int_0^t f\,d\tau)=F(s)/s$ via integration by parts]`
> **8.1.16** `[gamma function — $\mathcal{L}(t^\alpha)=\Gamma(\alpha+1)/s^{\alpha+1}$ for non-integer $\alpha>-1$]`

**Forward transform — use table and identities (trig identities, hyperbolic):**
> **8.1.2** `[table-based — products and powers of trig/hyperbolic: $\cosh t\sin t$, $\sin^2t$, $t\sinh2t$, etc.]`

**Forward transform — piecewise function, convert to unit step form first:**
> **8.1.5** `[piecewise → unit step → second shift theorem — four sub-parts with break points]`

**Inverse transform — direct table lookup after completing the square:**
> **8.2.1** `[complete square — quadratic denominators: $s^2-4s+13\to(s-2)^2+9$; nine sub-parts]`

**Inverse transform — first shift theorem $F(s-a)\leftrightarrow e^{at}f(t)$:**
> **8.2.2** `[first shift — $(s-a)^n$ denominators; numerator manipulation to match table; 12 sub-parts]`

**Inverse transform — partial fractions with distinct linear factors (Heaviside cover-up):**
> **8.2.3** `[Heaviside cover-up — all linear factors, cover-up method; six sub-parts]`

**Inverse transform — partial fractions with irreducible quadratic factors:**
> **8.2.7** `[mixed linear × quadratic — complete square on quadratic factor, split numerator; six sub-parts]`

**Laplace IVP — exponential RHS, standard partial fractions:**
> **8.3.1** `[Laplace IVP — exponential $e^t$; $Y(s)$ has linear × quadratic denom]` $y''+3y'+2y=e^t$, $y(0)=1$, $y'(0)=-6$
> **8.3.3** `[Laplace IVP — exponential $e^{3t}$; straightforward partial fractions]` $y''+y'-2y=2e^{3t}$, $y(0)=-1$, $y'(0)=4$
> **8.3.9** `[Laplace IVP — exponential $e^{4t}$; three linear factors in $Y(s)$]` $y''-3y'+2y=e^{4t}$, $y(0)=1$, $y'(0)=-2$

**Laplace IVP — trig RHS:**
> **8.3.17** `[Laplace IVP — sine RHS; $Y(s)$ has quadratic × quadratic denom, no resonance]` $y''+4y=3\sin t$
> **8.3.21** `[Laplace IVP — polynomial + trig RHS; superposition in $s$-domain]` $y''+y=t-3\sin2t$
> **8.3.35** `[Laplace IVP — trig RHS, non-unit leading coefficient; complete square]` $4y''-4y'+5y=4\sin t-4\cos t$

**Laplace IVP — exponential × trig RHS (first shift in forcing):**
> **8.3.27** `[Laplace IVP — $e^t\cos t$ forcing; first shift on $\mathcal{L}(\cos t)$]` $y''-5y'+6y=10e^t\cos t$

**Forward transform — piecewise $f(t)$, find $F(s)$ two ways:**
> **8.4.1** `[two-method comparison — direct integral vs. $f(t)=1+u(t-4)(t-1)$; verify both give same $F(s)$]`
> **8.4.5** `[piecewise → unit step — one break point, linear pieces]`
> **8.4.7** `[piecewise → unit step — polynomial piece starting at $t=2$; write as $u(t-2)g(t-2)$]`
> **8.4.11** `[piecewise → unit step — three pieces, two break points at $t=2,3$]`
> **8.4.15** `[piecewise trig → unit step — $\sin/\cos$ pieces on three intervals, break points at $\pi/2, \pi$]`

**Inverse transform — $e^{-as}$ factor, recover $u(t-a)f(t-a)$ form:**
> **8.4.19** `[second shift inverse — $e^{-2s}/(s-2)\to u(t-2)e^{2(t-2)}$]`
> **8.4.24** `[second shift inverse — complete square + first shift + second shift combined]` $H(s)=e^{-\pi s}(1-2s)/(s^2+4s+5)$

**Laplace IVP with piecewise forcing — convert RHS to unit steps, solve in $s$-domain:**
> **8.5.1** `[two-piece constant forcing, zero ICs — solution is piecewise via unit step]` $y''+y=3$ on $[0,\pi)$, then $0$
> **8.5.5** `[three-piece constant forcing, nonzero ICs — two unit step terms in $F(s)$]` $y''-3y'+2y$, breaks at $t=1,2$
> **8.5.7** `[three-piece constant forcing — nonzero ICs, breaks at $t=1,2$]` $y''-5y'+4y$
> **8.5.15** `[two-piece exponential forcing — $e^t$ starts, then $e^t-1$ after $t=1$]` $y''+2y'+y$, $y(0)=3$, $y'(0)=-1$
> **8.5.17** `[two-piece exponential forcing — $4e^t$ then 0 after $t=1$; zero ICs]` $y''+2y'+y$, $y(0)=0$, $y'(0)=0$

**Laplace IVP with Dirac delta — impulse forcing at isolated time:**
> **8.7.1** `[delta + smooth forcing — $e^{2t}$ continuous part + impulse at $t=1$; $\mathcal{L}(\delta(t-1))=e^{-s}$]` $y''+3y'+2y=6e^{2t}+28\delta(t-1)$
> **8.7.4** `[delta + trig forcing — impulse at $t=\pi/2$; adds $e^{-\pi s/2}$ term to $Y(s)$]` $y''+y=\sin3t+2\delta(t-\pi/2)$
> **8.7.12** `[two delta impulses — opposite signs at $t=\pi$ and $t=2\pi$; zero smooth forcing]` $y''+2y'+2y=\delta(t-\pi)-3\delta(t-2\pi)$

**Key identities:**
```
L{u(t-a)f(t-a)} = e^{-as}F(s)          [second shift]
L{e^{at}f(t)}   = F(s-a)               [first shift]
L{δ(t-a)}       = e^{-as}
L{y''} = s²Y - sy(0) - y'(0)
L{y'}  = sY - y(0)
```

---

### T13 — HIGHER-ORDER ODEs (§9.1, §9.2)

**Wronskian and fundamental sets — verify $n$ solutions are independent:**
> **9.1.6** `[verify two fundamental sets of 3 — compute $W$ for each; verify Abel's theorem for 3rd-order]`
> **9.1.9** `[Wronskian computation + verification — $W\{e^x,xe^x,x^2e^x\}$; verify vs. $y'''-3y''+3y'-y=0$; use Abel; state general solution]`

**Abel's formula for 3rd-order — $W(x)=W(x_0)e^{-\int p\,dx}$ with $p$ from $y'''$ coefficient:**
> **9.1.7** `[Abel — variable coefficient 3rd-order; $W(x)=2e^{-\int_0^x 2t\,dt}=2e^{-x^2}$]` $y'''+2xy''+e^xy'-y=0$, $W(0)=2$

**Euler-Cauchy 3rd order — $x^3y'''$ type, characteristic equation in $m$:**
> **9.1.2** `[Euler-Cauchy 3rd order IVP — substitute $y=x^m$, find $m$, apply 3 ICs]` $x^3y'''-x^2y''-2xy'+6y=0$, $y(-1)=-4$, $y'(-1)=-14$, $y''(-1)=-20$

**Constant coefficient — factor characteristic polynomial, triple/mixed roots:**
> **9.2.1** `[triple root $r=1$ — $y=(c_1+c_2x+c_3x^2)e^x$]` $y'''-3y''+3y'-y=0$
> **9.2.3** `[mixed roots — factor as $(r-1)(r^2+16)=0$; real + complex pair]` $y'''-y''+16y'-16y=0$

**4th-order — factor as product of two quadratics:**
> **9.2.9** `[4th order — $(r^2-4)(r^2+4)=0$; roots $\pm2$ (real) and $\pm2i$ (complex)]` $y^{(4)}-16y=0$
> **9.2.25** `[4th order IVP — factor $4r^4-13r^2+9=(4r^2-9)(r^2-1)$; four ICs]` $4y^{(4)}-13y''+9y=0$

**Constant coefficient IVP — 3rd order with three initial conditions:**
> **9.1.3** `[4th-order IVP — factor char poly, match roots, apply four ICs]` $y^{(4)}+y'''-7y''-y'+6y=0$
> **9.2.15** `[3rd-order IVP — mixed real + complex roots, apply three ICs]` $y'''-2y''+4y'-8y=0$, $y(0)=2$, $y'(0)=-2$, $y''(0)=0$

---

### T14 / T15 — EIGENVALUES AND SYSTEMS OF ODEs (§10.1–10.7)

**Physical modeling — derive system from applied setup:**
> **10.1.1** `[two-tank cascade — salt concentrations $Q_1,Q_2$ couple as 2×2 linear system]`
> **10.1.2** `[double spring-mass — two masses on springs, 2nd-order system → 4×4 first-order system]`

**Rewriting scalar ODE as first-order system (companion matrix):**
> **10.1.5** `[five sub-parts — introduce $y_1=y$, $y_2=y'$, etc.; write $\mathbf{y}'=A\mathbf{y}+\mathbf{f}$]`
> **10.2.6** `[general $n$th-order → $n\times n$ companion matrix; continuity iff scalar ODE is normal]`

**Verify homogeneous solution — check $\mathbf{y}'=A\mathbf{y}$:**
> **10.2.1** `[four 2×2 systems — differentiate each $\mathbf{y}$ and multiply $A\mathbf{y}$; confirm match for any $c_1,c_2$]`
> **10.2.3** `[two IVPs — verify vector solution, then apply IC to find $c_1,c_2$]`
> **10.2.8** `[verify fundamental matrix $Y'=AY$ — three cases including one 3×3]`

**Verify nonhomogeneous solution — check $\mathbf{y}'=A\mathbf{y}+\mathbf{f}$:**
> **10.2.5** `[four nonhomogeneous systems — verify $\mathbf{y}_h+\mathbf{y}_p$ satisfies the full system]`

**Fundamental matrix theory — invertibility and IVP formula:**
> **10.3.6** `[theoretical — prove $Y(t_0)$ invertible; prove IVP solution $\mathbf{y}=Y(t)Y^{-1}(t_0)\mathbf{k}$]`

**Fundamental matrix IVP — verify set, then solve $\mathbf{y}(0)=\mathbf{k}$ via $c_1,c_2$:**
> **10.3.7** `[2×2 real distinct — $\lambda=6,-2$; verify Wronskian nonzero; solve for $c_1,c_2$]` $A=\begin{bmatrix}2&4\\4&2\end{bmatrix}$, $\mathbf{k}=(-3,9)^T$
> **10.3.8** `[2×2 real distinct — $\lambda=-4,3$]` $A=\begin{bmatrix}-2&-2\\-5&1\end{bmatrix}$, $\mathbf{k}=(10,-4)^T$
> **10.3.9** `[2×2 real distinct — $\lambda=2,1$]` $A=\begin{bmatrix}-4&-10\\3&7\end{bmatrix}$, $\mathbf{k}=(-19,11)^T$
> **10.3.10** `[2×2 real distinct — $\lambda=3,1$]` $A=\begin{bmatrix}2&1\\1&2\end{bmatrix}$, $\mathbf{k}=(2,8)^T$
> **10.3.11** `[3×3 real distinct — verify 3 solution vectors; solve IVP via $3\times3$ linear system]` $\mathbf{y}(0)=(2,-7,20)^T$

**Real distinct eigenvalues — find $\lambda$, eigenvectors, write general solution:**
> **10.4.1** `[symmetric matrix — $\lambda=3,-1$; eigenvectors $(1,1)^T$, $(1,-1)^T$]`
> **10.4.3** `[scaled matrix — divide by scalar first; $\lambda=-1,-11/5$]`
> **10.4.7** `[non-symmetric — compute $\det(A-\lambda I)=0$; find eigenvectors]`

**Real distinct eigenvalues IVP — apply IC to determine $c_1,c_2$:**
> **10.4.17** `[IVP — $A=\frac{1}{6}\begin{bmatrix}7&2\\-2&2\end{bmatrix}$, $\mathbf{y}(0)=(0,-3)^T$]`
> **10.4.19** `[IVP — $A=\begin{bmatrix}21&-12\\24&-15\end{bmatrix}$, $\mathbf{y}(0)=(5,3)^T$]`

**Complex eigenvalues — $\lambda=\alpha\pm\beta i$, write real solution via $e^{\alpha t}\cos/\sin\beta t$:**
> **10.5.5** `[2×2 — extract real/imaginary parts of complex eigenvector; form two real solutions]` $A=\begin{bmatrix}4&12\\-3&-8\end{bmatrix}$
> **10.5.7** `[2×2 — complex eigenvalues, construct real basis]` $A=\begin{bmatrix}-13&16\\-9&11\end{bmatrix}$
> **10.5.8** `[3×3 — one real eigenvalue + complex conjugate pair; combine all three solutions]` $A=\begin{bmatrix}0&2&1\\-4&6&1\\0&4&2\end{bmatrix}$

**Complex eigenvalues IVP — apply IC after forming real solution:**
> **10.5.13** `[2×2 complex IVP]` $\mathbf{y}(0)=(6,2)^T$
> **10.5.15** `[2×2 complex IVP]` $\mathbf{y}(0)=(2,3)^T$
> **10.5.17** `[2×2 complex IVP]` $\mathbf{y}(0)=(0,2)^T$

**Repeated eigenvalue — find generalized eigenvector $\mathbf{w}$: $(A-\lambda I)\mathbf{w}=\mathbf{v}$:**
> **10.6.1** `[2×2 defective — repeated $\lambda$, one eigenvector; generalized $\mathbf{w}$ from $(A-\lambda I)\mathbf{w}=\mathbf{v}$]` $A=\begin{bmatrix}-1&2\\-5&5\end{bmatrix}$
> **10.6.4** `[2×2 defective — find repeated $\lambda$, one eigenvector, generalized $\mathbf{w}$]` $A=\begin{bmatrix}5&-6\\3&-1\end{bmatrix}$
> **10.6.7** `[3×3 defective — two linearly independent eigenvectors + one generalized; Jordan structure]` $A=\begin{bmatrix}2&1&-1\\0&1&1\\1&0&1\end{bmatrix}$

**Repeated eigenvalue IVP:**
> **10.6.17** `[2×2 repeated IVP]` $\mathbf{y}(0)=(5,2)^T$
> **10.6.19** `[2×2 repeated IVP]` $\mathbf{y}(0)=(17,7)^T$
> **10.6.21** `[3×3 repeated IVP]` $\mathbf{y}(0)=(4,0,6)^T$

**Nonhomogeneous — constant or exponential forcing, undetermined coefficients for $\mathbf{y}_p$:**
> **10.7.1** `[exponential forcing — guess $\mathbf{y}_p=e^{4t}\mathbf{a}+e^{-3t}\mathbf{b}$; substitute and solve for coefficients]`
> **10.7.3** `[constant forcing — guess $\mathbf{y}_p=\mathbf{c}$; solve $A\mathbf{c}=-\mathbf{b}$ (i.e., $\mathbf{c}=-A^{-1}\mathbf{b}$)]`

**Nonhomogeneous — variation of parameters for systems, $Y$ given:**
> **10.7.11** `[VoP — $Y=t\begin{bmatrix}\cos t&\sin t\\-\sin t&\cos t\end{bmatrix}$; compute $Y^{-1}$, integrate $Y^{-1}\mathbf{f}$]`
> **10.7.13** `[VoP — $Y=\begin{bmatrix}t&1\\1&t\end{bmatrix}$; $Y^{-1}=\frac{1}{t^2-1}\begin{bmatrix}t&-1\\-1&t\end{bmatrix}$]`
> **10.7.14** `[VoP — $Y=\begin{bmatrix}2&e^{-t}\\e^t&2\end{bmatrix}$; compute $\det Y$ and invert]`

**Theoretical — derive general VoP formula for systems:**
> **10.7.23** `[proof — variation of parameters: write $\mathbf{y}=Y\mathbf{u}$, differentiate, solve $Y\mathbf{u}'=\mathbf{f}$, integrate]`

---

### TECHNIQUE COUNT — BOOK PROBLEMS (Phase 3 addition to frequency table)

| Technique | Book Problem Count |
|---|---|
| 1st-Order Linear / Integrating Factor | 10+ |
| Separation of Variables | 7 |
| Existence & Uniqueness | 5 |
| Numerical Methods | 6 |
| Newton's Cooling / Radioactive Decay | 5 |
| Mixing Tank | 5 |
| 2nd-Order Char. Eq. | 8 |
| Undetermined Coefficients | 12+ |
| Variation of Parameters | 7 |
| Abel's Formula / Wronskian | 5 |
| Spring-Mass | 9 |
| Laplace (forward + inverse) | 12+ |
| Laplace + Unit Step / Heaviside | 7 |
| Laplace + Dirac Delta | 3 |
| Higher-Order ODEs | 7 |
| Eigenvalues / Systems of ODEs | 15+ |
| Nonhomogeneous Systems (§10.7) | 5 |

**Updated priority — book problem volume confirms:**
- Eigenvalue/systems: most book problems by far (§10.3–10.7 = 20+ problems)
- Undetermined coefficients + Laplace: tied for 2nd most practice
- Spring-mass: consistent with midterms + 9 dedicated book problems

---

## SECTION 5 — FINAL EXAM PRIORITY SYNTHESIS

### Top 5 Most Likely Final Exam Topics (All Sources Combined)

| Rank | Technique | Evidence |
|---|---|---|
| 1 | **Systems of ODEs** (eigenvalue, complex, repeated) | Highest book volume; Q9,Q10; not yet on midterm → likely on final |
| 2 | **Spring-Mass** (free + forced) | Both midterms; 9 book problems; Q6,Q7 |
| 3 | **Laplace Transform** (inverse, unit step, IVP) | Dedicated quiz week; large book volume; §8.3–8.5 |
| 4 | **Undetermined Coefficients + VoP** | Both midterms; largest §5.x book volume |
| 5 | **1st-Order Linear ODE / Integrating Factor** | Both midterms (Q1); fundamental technique throughout |

### What NOT to Neglect
- **Abel's Formula**: appeared explicitly on both Mid2 problems — will appear on final
- **Laplace + Unit Step**: new material, high quiz coverage, not on midterms
- **Mixing Tank**: both Mid1 problems; classic exam staple
- **Equilibria**: both Mid1 problems; easy points

### Exam Strategy
```
2nd-order homogeneous? → char eq (T8)
   → nonhomogeneous? check RHS form:
       polynomial/exp/trig → undetermined coefficients (T9/T20)
       general g(t) or variable coeff → VoP (T10/T22)
           → variable coeff → Abel for W first

Spring-mass? → physical setup: k=mg/ΔL → ODE → T8 → classify damping
Mixing tank? → dQ/dt = rate_in − rate_out → linear ODE → integrating factor

System x'=Ax?
   → eigenvalues → classify:
       real distinct → c₁e^(λ₁t)v₁ + c₂e^(λ₂t)v₂
       complex α±βi → e^(αt)[A·cos(βt) + B·sin(βt)] form
       repeated λ → c₁e^(λt)v + c₂e^(λt)(tv+w) where Aw=λw−v

Piecewise forcing or δ? → Laplace (T12)
   → write f(t) in unit step form → table → partial fractions → invert
```

---

## SECTION 6 — POST-MIDTERM 2 TARGETED DRILL SET

**Source priority:** Q7–Q10 (verbatim) + HW5–7 (verbatim). These are the highest-signal problems for the final — everything here appeared after Midterm 2 and reflects what the professor chose to test in the final weeks of the course.

**Format:** Work each problem cold. Check technique recognition first, then execute. Estimated times given.

---

### BLOCK A — Laplace Transforms + Unit Step + Dirac Delta
*Q7 was entirely Laplace. HW5 was entirely Laplace. Highest post-M2 signal.*

**A1** `[Spring-Mass → steady state amplitude only; SI units]` *(Q7-Q1, ~4 min)*
> A mass of 6 kg stretches a spring 5 cm. External force $8\cos(14t)$ N; dashpot exerts 1 N when velocity is 7 m/sec. Find the **amplitude of the steady state**.

**A2** `[Forward Laplace — exp×trig superposition; first-shift + derivative formula]` *(Q7-Q2, ~3 min)*
> $\mathcal{L}(3t\cos 4t - e^{2t}\sin t) = \ldots$

**A3** `[First-shift theorem — conceptual; if $F(s)=2\sqrt[3]{s}$, what is $\mathcal{L}(e^{-at}f(t))$?]` *(Q7-Q3, ~2 min)*
> If $F(s) = 2\sqrt[3]{s}$ is the Laplace transform of $f(t)$, identify which $G(s)$ is $\mathcal{L}(e^{-at}f(t))$ for $a>0$.

**A4** `[Inverse Laplace — $e^{-3s}$ delay factor + trig denominator; split into two terms]` *(Q7-Q4, ~5 min)*
> $\mathcal{L}^{-1}\!\left(\dfrac{6 + 0.4se^{-3s}}{s^2+4}\right) = \ldots$

**A5** `[Inverse Laplace — mixed quadratic PFD; $(s^2+4)(s^2+3s+2)$ denominator + rational numerator]` *(Q7-Q5, ~8 min)*
> $\mathcal{L}^{-1}\!\left(\dfrac{3s+2}{(s^2+4)(s^2+3s+2)} + \dfrac{2s-1}{s^2+3s+2}\right) = \ldots$

**A6** `[Laplace IVP — piecewise RHS via unit step; complete square for char roots]` *(Q7-Q6, ~8 min)*
> $y'' + 4y' + 5y = 3 - 3u(t-6)$; $y(0)=0$, $y'(0)=2$. Write $Y(s)$.

**A7** `[Laplace IVP — unit step × polynomial RHS; $u(t-2)(t-2)^3$ forcing]` *(Q7-Q7, ~8 min)*
> $y'' - 4y' + 3y = u(t-2)(t-2)^3$; $y(0)=2$, $y'(0)=0$. Write $Y(s)$.

**A8** `[HW5 — Laplace IVP, 5-piece alternating piecewise RHS; multi-delta $e^{-as}$ sum]` *(HW5 #1, ~15 min)*
> $y'' + 4y' + 13y = f(t)$ where $f(t)=1,\,-1,\,1,\,-1,\,0$ on $[0,1),\,[1,2),\,[2,3),\,[3,4),\,[4,\infty)$; $y(0)=y'(0)=0$.
> Write $f(t)$ in unit step form, find $Y(s)$, invert completely.

**A9** `[HW5 — Laplace IVP, Dirac delta triple impulse; $\mathcal{L}(\delta)=1$, $\mathcal{L}(\delta(t-a))=e^{-as}$]` *(HW5 #2, ~10 min)*
> $y''+4y'+13y = 3\delta(t)+2\delta(t-1)+\delta(t-2)$; $y(0)=y'(0)=0$. Solve completely.

**A10** `[HW5 — Convolution theorem; two distinct factorizations of same $F(s)$]` *(HW5 #3b, ~10 min)*
> $F(s) = \dfrac{s+2}{(s+1)^2(s^2+4s+5)}$. Express $\mathcal{L}^{-1}(F)$ as a convolution integral two different ways by factoring $F$ differently.

---

### BLOCK B — Higher-Order ODEs (3rd order, char eq, UC)
*Q8 Q1–Q2 were both 3rd-order. High signal for final.*

**B1** `[3rd-order homogeneous — factor char poly; three distinct real roots]` *(Q8-Q1, ~3 min)*
> General solution of $y''' - 2y'' - 5y' + 6y = 0$.

**B2** `[3rd-order nonhomogeneous — UC, polynomial RHS; find $y_p$ then general solution]` *(Q8-Q2, ~6 min)*
> General solution of $y''' + 2y'' - 5y' - 6y = 6t^2$.

---

### BLOCK C — Eigenvalues: 2×2 and 3×3
*Q8 was 8 eigenvalue problems. Master speed and accuracy here.*

**C1** `[2×2 real — $(1-\lambda)^2 - 4 = 0$]` *(Q8-Q3, ~1 min)*
> Eigenvalues of $\begin{bmatrix}1&2\\2&1\end{bmatrix}$.

**C2** `[2×2 complex — discriminant negative]` *(Q8-Q4, ~1 min)*
> Eigenvalues of $\begin{bmatrix}2&3\\-3&2\end{bmatrix}$.

**C3** `[2×2 real distinct]` *(Q8-Q5, ~1 min)*
> Eigenvalues of $\begin{bmatrix}1&3\\3&1\end{bmatrix}$.

**C4** `[2×2 — off-diagonal product negative]` *(Q8-Q6, ~1 min)*
> Eigenvalues of matrix with $\lambda^2 - 2\lambda - 8 = 0$.

**C5** `[3×3 upper-triangular — char poly = product of diagonal shifts; cofactor on first column]` *(Q8-Q6, ~2 min)*
> Eigenvalues of $\begin{bmatrix}3-u&2&1\\-1&1-u&2\\1&1&2-u\end{bmatrix}$ — i.e., compute $\det(A-uI) = -u^3+6u^2-10u+6$.

**C6** `[3×3 upper triangular — read off diagonal or expand by first column]` *(Q8-Q7, ~2 min)*
> Eigenvalues of $\begin{bmatrix}1&7&1\\0&3&5\\0&5&3\end{bmatrix}$.

**C7** `[3×3 upper triangular]` *(Q8-Q8, ~2 min)*
> Eigenvalues of $\begin{bmatrix}4&2&1\\0&2&5\\0&5&2\end{bmatrix}$.

---

### BLOCK D — Systems of ODEs: All Eigenvalue Types + Nonhomogeneous
*Q9 and Q10 + HW6–7 cover every sub-type. Work in order.*

**D1** `[2×2 complex eigenvalues — find complex eigenvectors, write real solution]` *(Q9-Q1, ~5 min)*
> $A = \begin{bmatrix}2&-2\\2&2\end{bmatrix}$, $\lambda = 2\pm 2i$. Find the complex eigenvectors.

**D2** `[3×3 — repeated $\lambda=2$; identify algebraic vs geometric multiplicity]` *(Q9-Q2, ~4 min)*
> $\lambda=2$ is an eigenvalue of $\begin{bmatrix}10&8&-8\\-7&-5&7\\2&2&0\end{bmatrix}$. Determine its algebraic and geometric multiplicities.

**D3** `[2×2 real distinct IVP — find $\lambda$, eigenvectors, apply IC]` *(Q9-Q3, ~6 min)*
> $\bar{x}' = \begin{bmatrix}-2&1\\1&-2\end{bmatrix}\bar{x}$; $\bar{x}(0) = \begin{bmatrix}1\\2\end{bmatrix}$.

**D4** `[2×2 nonhomogeneous — constant forcing $\mathbf{g}$; UC: guess $\mathbf{y}_p = \mathbf{c}$, solve $A\mathbf{c} = -\mathbf{g}$]` *(Q9-Q4, ~6 min)*
> $\bar{x}' = \begin{bmatrix}1&1\\-2&4\end{bmatrix}\bar{x} + \begin{bmatrix}-1\\3\end{bmatrix}$.

**D5** `[2×2 complex eigenvalues IVP — apply IC after forming real solution]` *(Q9-Q5, ~8 min)*
> $y_1' = -y_1 + 2y_2$, $y_2' = -2y_1 - y_2$; $y_1(0)=1$, $y_2(0)=2$.

**D6** `[2×2 nonhomogeneous — linear $t$ forcing; UC: guess $\mathbf{y}_p = \mathbf{a}t+\mathbf{b}$, match coefficients]` *(Q9-Q6, ~10 min)*
> $x' = 4x-y+2$, $y' = 5x-2y+t$. Find the general solution.

**D7** `[ODE → companion matrix rewrite]` *(Q10-Q1, ~2 min)*
> Rewrite a given 2nd-order scalar ODE as a first-order system $\mathbf{y}' = A\mathbf{y}$; identify $A$.

**D8** `[HW6 #1–2 — eigenvalues + eigenvectors, then IVP: real distinct + complex cases]` *(HW6, ~15 min)*
> (a) Find eigenvalues and eigenvectors of $A=\begin{bmatrix}3&2\\1&2\end{bmatrix}$ and $B=\begin{bmatrix}2&-1\\1&2\end{bmatrix}$.
> (b) Solve $x'=3x+2y$, $x(0)=1$; $y'=x+2y$, $y(0)=-1$ using $A$.
> (c) Solve $u'=2u-v$, $u(0)=1$; $v'=u+2v$, $v(0)=2$ using $B$.

**D9** `[HW6 #4 — nonhomogeneous system IVP: real distinct + constant forcing + ICs]` *(HW6, ~12 min)*
> $\begin{bmatrix}x'\\y'\end{bmatrix} = \begin{bmatrix}2&1\\6&-3\end{bmatrix}\begin{bmatrix}x\\y\end{bmatrix} + \begin{bmatrix}5\\4\end{bmatrix}$; $x(0)=y(0)=0$.
> (a) General homogeneous solution. (b) Find $\mathbf{y}_p$ by UC. (c) Full IVP.

**D10** `[HW7 #1a — nonhomogeneous system IVP: real distinct + linear $t$ forcing + numeric ICs]` *(HW7, ~15 min)*
> $y_1' = y_1+2y_2+2$, $y_1(0)=0$; $y_2' = 3y_1-4y_2-t$, $y_2(0)=0$.
> Guess $\mathbf{y}_p = \mathbf{a}t+\mathbf{b}$, match coefficients, find $c_1,c_2$ from ICs.

**D11** `[HW7 #1b — complex eigenvalue system IVP; $\lambda=2\pm i$, apply IC to real solution]` *(HW7, ~10 min)*
> $y_1'=2y_1-y_2$, $y_1(0)=0$; $y_2'=y_1+2y_2$, $y_2(0)=1$.

---

### BLOCK E — Synthesis: Multi-step applied problems

**E1** `[HW7 #2 — 4-tank nonhomogeneous system; write ODEs from mixing diagram, find equilibrium concentrations as $t\to\infty$ from particular solution]` *(HW7, ~20 min)*
> Four interconnected tanks (500, 500, 400, 400 gal), each with saline inflow and cross-flow. Write the $4\times4$ system $\mathbf{Q}' = Q\mathbf{Q}+\mathbf{p}$. Use the fact that all eigenvalues of $Q$ are negative to conclude $\mathbf{Q}(t)\to\mathbf{Q}_p = -Q^{-1}\mathbf{p}$ as $t\to\infty$. Find equilibrium salt quantities.

**E2** `[HW7 #3 — Lotka-Volterra nonlinear system; find equilibria, ode45 phase portrait, qualitative behavior]` *(HW7, ~15 min)*
> $\frac{dx}{dt}=0.4x-0.2xy$, $\frac{dy}{dt}=0.1xy-0.3y$. 
> (a) Find both equilibria. (b) Use ode45 for ICs $(5,1),(6,3),(4,1),(2,2)$. (c) Interpret phase portraits relative to equilibrium $(3,2)$.

---

### BLOCK F — "Blasts From The Past" (Q10 review items)
*Q10 included a review section pulling from earlier topics — confirms these aren't dropped.*

**F1** `[Euler/Numerical — Q10-Q5; ode45 answer from earlier IVP, round to 2 decimal places]`
> If $y' = \cos^2 y \cos^2 x$, $y(\pi)=\pi/4$, then $y(2\pi) \approx$ ___. *(Answer: 1.2)*

**F2** `[Fraction / mixing — Q10-Q6; rational Laplace transform answer = 23/5]`
> Conceptual Laplace/system problem. *(Answer: 23/5)*

**F3** `[ode45 IVP — Q10-Q8; $4y''-4y'+y=0$, $y(0)=-1$, $y'(0)=2$, find $y(1)$]`
> *(Answer: 2.473 — same problem appeared in Q4 and Q10, double confirmation)*

---

### DRILL SET PRIORITY ORDER

If time is limited, work in this sequence:

| Priority | Block | Techniques | Time |
|---|---|---|---|
| 1 | D8–D11 | Systems IVP all types (HW6–7) | 50 min |
| 2 | A6–A9 | Laplace piecewise + delta IVPs (Q7, HW5) | 35 min |
| 3 | B1–B2 | 3rd-order char eq + UC (Q8) | 10 min |
| 4 | C1–C7 | Eigenvalue speed drills (Q8) | 15 min |
| 5 | D3–D6 | Systems Q9: all eigenvalue types + nonhom | 30 min |
| 6 | A4–A5 | Inverse Laplace PFD hard cases (Q7) | 15 min |
| 7 | E1–E2 | Applied synthesis (HW7) | 35 min |
| — | F1–F3 | Review anchors (Q10 "Blasts") | 5 min |

**Total: ~3 hours of targeted work covering every post-Midterm 2 technique.**

---
*End of Phase 3 — All sources scraped. Study guide complete.*
