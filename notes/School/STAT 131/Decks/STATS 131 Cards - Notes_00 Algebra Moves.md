---
type: reference
parent: "[[STATS 131]]"
domain: math
course: "STATS 131"
status: draft
source: "Notes_00 Algebra Moves"
tags:
  - decks
---
# STATS 131 Cards - Notes_00 Algebra Moves

The moves hidden inside Example 0.1. Each one is ordinary arithmetic; the only new thing is noticing when to use it.

## Letters Stand for Numbers
| Front | Back | Notes |
| --- | --- | --- |
| In $S = 1 + x + x^2 + \cdots + x^n$, what kind of object is $S$ once you pick values for $x$ and $n$? | A single ordinary number (for $x=2, n=3$: $S = 1+2+4+8 = 15$), so every rule for numbers applies to it | move; definition |
| Why can you treat $S$ like an unknown in an equation? | Because $S$ names one number; "$S = \ldots$" is an equation, and you can do algebra on equations | move; procedure |

## Closed Form
| Front | Back | Notes |
| --- | --- | --- |
| What does "evaluate $S$" mean when the answer can't be a plain number? | Rewrite $S$ as one short formula in the given letters with no "$\cdots$" and no $\sum$ | move; definition |
| Is $\dfrac{1-x^{n+1}}{1-x}$ an acceptable answer to "evaluate $1+x+\cdots+x^n$"? Yes or no, and why? | Yes: it is a closed form, a fixed number of operations regardless of how big $n$ is | move; discrimination |

## Same Operation on Both Sides
| Front | Back | Notes |
| --- | --- | --- |
| What are you allowed to do to an equation without changing what's true? | The same operation to both sides: add, subtract, multiply, or divide by a nonzero quantity | move; definition |
| If $S = A$ and $xS = B$, what new equation follows? | $S - xS = A - B$ (subtract one equation from the other) | move; procedure |

## Distributive Law
| Front | Back | Notes |
| --- | --- | --- |
| State the distributive law | $a(b + c + d) = ab + ac + ad$: a factor outside multiplies every term inside | move; formula |
| Run the distributive law backward on $S - xS$ | $S - xS = S(1 - x)$ (factor out $S$) | move; procedure |

## Exponent Rules
| Front | Back | Notes |
| --- | --- | --- |
| Simplify $x \cdot x^k$ | $x^{k+1}$ (add exponents: $x^a x^b = x^{a+b}$) | move; formula |

## Shift by Multiplying
| Front | Back | Notes |
| --- | --- | --- |
| What does multiplying $1 + x + x^2 + \cdots + x^n$ by $x$ do to each term? | Raises every exponent by one: $x + x^2 + \cdots + x^{n+1}$, the same list slid one place to the right | move; procedure |
| Which terms do $S$ and $xS$ share when $S = 1+x+\cdots+x^n$? | $x, x^2, \ldots, x^n$; only $1$ (in $S$) and $x^{n+1}$ (in $xS$) are unmatched | move; procedure |

## Telescoping Cancellation
| Front | Back | Notes |
| --- | --- | --- |
| What happens when you subtract a shifted copy of a sum from the original? | All the overlapping terms cancel; only the first term of one and the last term of the other survive | move; definition |
| Compute $S - xS$ for $S = 1 + x + \cdots + x^n$ | $1 - x^{n+1}$ | move; procedure |

## Constant Ratio Signals Multiply and Subtract
| Front | Back | Notes |
| --- | --- | --- |
| What feature of a sum tells you to try "multiply by $r$ and subtract"? | Each term is the previous term times the same number $r$ (a constant ratio) | move; discrimination |
| In $2 + 6 + 18 + 54 + \cdots$, what is $r$ and what do you multiply $S$ by? | $r = 3$; compute $S - 3S$ | move; procedure |

## Solving for an Unknown That Appears Twice
| Front | Back | Notes |
| --- | --- | --- |
| How do you solve $S - xS = 1 - x^{n+1}$ for $S$? | Factor: $S(1-x) = 1 - x^{n+1}$, then divide both sides by $(1-x)$ | move; procedure |
| General recipe when the unknown shows up in several terms | Move all its terms to one side, factor it out, divide by what's left | move; procedure |

## Division Needs a Nonzero Divisor
| Front | Back | Notes |
| --- | --- | --- |
| After dividing by $(1-x)$, which value of $x$ must you check separately? | $x = 1$, where $1-x = 0$ and the division is illegal | move; discrimination |
| What is $1 + x + \cdots + x^n$ when $x = 1$? | $n + 1$ (it's $n+1$ ones) | move; formula |

## Notes 00 Example 0.1 Finite Geometric Sum
| Front | Back | Notes |
| --- | --- | --- |
| Name the chain of moves that evaluates $1 + x + \cdots + x^n$ | Notice constant ratio $x$; compute $xS$ (shift); subtract ($S - xS$ telescopes to $1 - x^{n+1}$); factor $S(1-x)$; divide by $1-x$; check $x=1$ separately | p.1; procedure |
## Evaluating a Sum SOP
| Front | Back | Notes |
| --- | --- | --- |
| Second step: what makes an abstract sum concrete? | Write out a tiny case (n = 2 or 3) and plug in a number (x = 2) so you can see actual values | SOP 2; procedure |
| Third step: what do you compare in the written-out terms? | How each term relates to the one before it: same ratio (multiply and subtract) or same difference (pair first with last) | SOP 3; procedure |
| Fourth step once you know the pattern | Apply the move that pattern calls for, then check your formula on the tiny numeric case | SOP 4; procedure |

## Adding Zero
| Front | Back | Notes |
| --- | --- | --- |
| What is the "adding zero" move? | Add and subtract the same term (+c - c) so the expression regroups into a form you know, like a perfect square | move; definition |
| Where have you used adding zero before? | Completing the square: $x^2+6x = (x^2+6x+9)-9 = (x+3)^2-9$ | move; procedure |
| Adding zero or multiply and subtract: which one evaluates $1+x+\cdots+x^n$? | Multiply and subtract (constant ratio). Adding zero regroups one expression; it does not collapse a long sum | move; discrimination |

## Difference of Powers Factorization
| Front | Back | Notes |
| --- | --- | --- |
| Factor $1 - x^3$ | $(1-x)(1+x+x^2)$ | move; formula |
| Factor $1 - x^{n+1}$ | $(1-x)(1+x+\cdots+x^n)$, which is the geometric sum formula read backward | move; formula |
| Why can't you FOIL $(1-x^3)(1-x)^{-1}$? | $(1-x)^{-1}$ is not a sum of terms, so there is nothing to distribute; factor the top instead and cancel $(1-x)$ | move; discrimination |

## Why a Closed Form Is Better
| Front | Back | Notes |
| --- | --- | --- |
| Why is $\frac{1-x^{n+1}}{1-x}$ more useful than $1+x+\cdots+x^n$? | It has the same length for every $n$, so you can compute it instantly for huge $n$, take $n \to \infty$, and differentiate it | move; discrimination |
| What does the closed form let you do in Example 0.2 that the dots can't? | Take the limit as $n\to\infty$: $x^{n+1}\to0$ when $\lvert x \rvert<1$, so the infinite sum is $\frac{1}{1-x}$ | move; procedure |

## A Special Case Checks but Does Not Prove
| Front | Back | Notes |
| --- | --- | --- |
| What does plugging in $x=2, n=2$ do for a formula you derived? | Catches algebra slips; it does not prove the formula | move; definition |
| What actually proves $S=\frac{1-x^{n+1}}{1-x}$ for every $n$? | Every step (multiply, subtract, factor, divide) is legal for any $n$, and the cancellation of $x,\dots,x^n$ happens for any $n$ | move; discrimination |

# Node map
```json
[
 {
  "name": "Letters Stand for Numbers",
  "type": "concept",
  "existing": false,
  "parent": "Elementary Algebra",
  "prereqs": [],
  "uses": [],
  "page": "",
  "summary": "Once values are chosen, every letter in an expression (S, x, n) is one ordinary number, so all the rules of arithmetic apply to it. Sums like S are not a special data type."
 },
 {
  "name": "Closed Form",
  "type": "concept",
  "existing": false,
  "parent": "Elementary Algebra",
  "prereqs": [
   "Letters Stand for Numbers"
  ],
  "uses": [],
  "page": "",
  "summary": "An expression with a fixed number of operations and no ellipsis or sigma. \"Evaluate\" a sum with letters in it means find its closed form."
 },
 {
  "name": "Same Operation on Both Sides",
  "type": "concept",
  "existing": false,
  "parent": "Elementary Algebra",
  "prereqs": [
   "Letters Stand for Numbers"
  ],
  "uses": [],
  "page": "",
  "summary": "Doing the same thing to both sides of an equation (add, subtract, multiply, divide by nonzero) keeps it true; subtracting one equation from another is a special case."
 },
 {
  "name": "Distributive Law",
  "type": "concept",
  "existing": false,
  "parent": "Elementary Algebra",
  "prereqs": [
   "Letters Stand for Numbers"
  ],
  "uses": [],
  "page": "",
  "summary": "$a(b+c)=ab+ac$. Forward it multiplies a factor into every term; backward it factors a common term out."
 },
 {
  "name": "Shift by Multiplying",
  "type": "concept",
  "existing": false,
  "parent": "Elementary Algebra",
  "prereqs": [
   "Distributive Law",
   "Exponent Rules"
  ],
  "uses": [],
  "page": "",
  "summary": "Multiplying a sum of powers $1+x+\\dots+x^n$ by $x$ raises each exponent by one, producing the same list shifted one place."
 },
 {
  "name": "Telescoping Cancellation",
  "type": "concept",
  "existing": false,
  "parent": "Elementary Algebra",
  "prereqs": [
   "Shift by Multiplying",
   "Same Operation on Both Sides"
  ],
  "uses": [],
  "page": "",
  "summary": "Subtracting a shifted copy of a sum from the original cancels every overlapping term, leaving only the unmatched ends."
 },
 {
  "name": "Constant Ratio Signals Multiply and Subtract",
  "type": "concept",
  "existing": false,
  "parent": "Elementary Algebra",
  "prereqs": [
   "Telescoping Cancellation"
  ],
  "uses": [],
  "page": "",
  "summary": "The noticing rule: if every term is the previous one times the same $r$, multiply the sum by $r$ and subtract."
 },
 {
  "name": "Solving for an Unknown That Appears Twice",
  "type": "concept",
  "existing": false,
  "parent": "Elementary Algebra",
  "prereqs": [
   "Same Operation on Both Sides",
   "Distributive Law"
  ],
  "uses": [],
  "page": "",
  "summary": "Collect every term containing the unknown on one side, factor it out, then divide by the remaining factor."
 },
 {
  "name": "Division Needs a Nonzero Divisor",
  "type": "concept",
  "existing": false,
  "parent": "Elementary Algebra",
  "prereqs": [
   "Same Operation on Both Sides"
  ],
  "uses": [],
  "page": "",
  "summary": "Dividing by an expression like $(1-x)$ is only valid where it is nonzero; handle that value (here $x=1$) as a separate case."
 },
 {
  "name": "Notes 00 Example 0.1 Finite Geometric Sum",
  "type": "problem",
  "existing": false,
  "parent": "Geometric Series",
  "prereqs": [],
  "uses": [
   "Closed Form",
   "Constant Ratio Signals Multiply and Subtract",
   "Shift by Multiplying",
   "Telescoping Cancellation",
   "Solving for an Unknown That Appears Twice",
   "Division Needs a Nonzero Divisor",
   "Geometric Series"
  ],
  "page": 1,
  "summary": "Evaluate $S=1+x+\\cdots+x^n$: result $\\frac{1-x^{n+1}}{1-x}$ for $x \\ne 1$ and $n+1$ for $x=1$."
 },
 {
  "name": "Exponent Rules",
  "type": "problem",
  "existing": false,
  "parent": "",
  "prereqs": [],
  "uses": [],
  "page": "",
  "summary": ""
 },
 {
  "name": "Evaluating a Sum SOP",
  "type": "concept",
  "existing": false,
  "parent": "Elementary Algebra",
  "prereqs": [
   "closed form"
  ],
  "uses": [],
  "page": "",
  "summary": "1. Name the target: a closed form in the given letters. 2. Write a tiny case with numbers. 3. Compare consecutive terms (ratio or difference). 4. Apply the matching move and check on the tiny case."
 },
 {
  "name": "Adding Zero",
  "type": "concept",
  "existing": false,
  "parent": "Elementary Algebra",
  "prereqs": [
   "Same Operation on Both Sides"
  ],
  "uses": [],
  "page": "",
  "summary": "Add and subtract the same term so an expression regroups into a known form (completing the square). It is not the move for collapsing a geometric sum.",
  "contrasts_with": [
   "Constant Ratio Signals Multiply and Subtract"
  ]
 },
 {
  "name": "Difference of Powers Factorization",
  "type": "concept",
  "existing": false,
  "parent": "Elementary Algebra",
  "prereqs": [
   "Distributive Law"
  ],
  "uses": [],
  "page": "",
  "summary": "$1-x^{n+1}=(1-x)(1+x+\\cdots+x^n)$; in particular $1-x^3=(1-x)(1+x+x^2)$."
 },
 {
  "name": "Why a Closed Form Is Better",
  "type": "concept",
  "existing": false,
  "parent": "Elementary Algebra",
  "prereqs": [
   "closed form"
  ],
  "uses": [],
  "page": "",
  "summary": "A closed form has fixed length, so it can be computed for any n, sent to a limit, or differentiated; an expression with dots cannot."
 },
 {
  "name": "A Special Case Checks but Does Not Prove",
  "type": "concept",
  "existing": false,
  "parent": "Elementary Algebra",
  "prereqs": [],
  "uses": [],
  "page": "",
  "summary": "Plugging in numbers catches mistakes. The proof is that each algebra step is valid for every value of the letters."
 }
]
```

# Frankenstein problems

**Problem 1.** Evaluate $T = 3 + 3\cdot 2 + 3\cdot 2^2 + \cdots + 3\cdot 2^{n}$.

*Solution.* Constant ratio $r=2$. $2T = 3\cdot2 + \cdots + 3\cdot2^{n+1}$. $T - 2T = 3 - 3\cdot2^{n+1}$, so $-T = 3(1-2^{n+1})$ and $T = 3(2^{n+1}-1)$. Check $n=1$: $3+6 = 9 = 3(4-1)$.

*Concepts tested:* Constant Ratio Signals Multiply and Subtract, Shift by Multiplying, Telescoping Cancellation, Solving for an Unknown That Appears Twice.

**Problem 2.** Evaluate $U = 1 - y + y^2 - y^3 + \cdots + y^{2m}$ (signs alternate).

*Solution.* Constant ratio $r = -y$. $U - (-y)U = U(1+y) = 1 - (-y)^{2m+1} = 1 + y^{2m+1}$. So $U = \frac{1+y^{2m+1}}{1+y}$ for $y \ne -1$; if $y=-1$ every term is $1$ and $U = 2m+1$.

*Concepts tested:* Constant Ratio Signals Multiply and Subtract, Telescoping Cancellation, Division Needs a Nonzero Divisor.
