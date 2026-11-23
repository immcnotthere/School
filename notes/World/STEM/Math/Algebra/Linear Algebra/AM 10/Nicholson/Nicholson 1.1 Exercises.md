---
type: concept
parent: "[[Nicholson]]"
domain: math
status: draft
---
# Summary
## Throughline across 1.1 (what all the exercises are really doing)

Every problem in 1.1 is training one unified workflow:

1. **Define what a solution means**  
    A solution is an assignment of variables that makes every equation true when substituted.
    
2. **Choose the right unknowns**  
    Unknowns are the “knobs you can turn” (decision variables, coefficients you are solving for, transformed variables).
    
3. **Translate constraints into a system**  
    Each independent requirement becomes an equation. Missing variables still exist and get coefficient 0.
    
4. **Represent the system in a standard data structure**  
    Use an augmented matrix so the system can be manipulated mechanically.
    
5. **Transform without changing the solution set**  
    Use equivalence-preserving operations (EROs, invertible substitutions) so you can simplify safely.
    
6. **Read off the solution set and interpret it**  
    Unique vs infinite vs none, then convert back to the original units or variables, and check.
    

That is the spine: definition of solution set, encoding, equivalence, computation, interpretation.

---

## Group 1: Solutions as substitution, parameters, and degrees of freedom

**Exercises:** 1.1.1, 1.1.2, 1.1.3, 1.1.4, 1.1.5, 1.1.6

### Shared sol technique

- Treat “solution” as **substitution truth**: plug in and simplify.
    
- When equations are fewer than variables, write **parametric form** by choosing free variables.
    
- When a coefficient can be zero, do **case splits**.
    

### Itemized sig and technique by exercise

- **1.1.1 (verify parametric solutions)**
    
    - **Sol technique:** Substitute the given parametric expressions into each equation and simplify to identities.
        
    - **Sig:** A parametric solution represents infinitely many solutions at once. Verification is not solving, it is checking membership in the solution set.
        
- **1.1.2 (one equation, parametric form in two ways)**
    
    - **Sol technique:** Solve for one variable in terms of the others, then pick a different variable the second time and re-parameterize.
        
    - **Sig:** Parametric form is not unique. Different parameterizations can describe the same geometric object (line or plane).
        
- **1.1.3 (interpret 2x = 5 as 2x + 0y = 5)**
    
    - **Sol technique:** Solve for the constrained variable, declare the missing one free, write parametric form.
        
    - **Sig:** A missing variable does not disappear. Coefficient 0 means “no restriction,” which creates freedom.
        
- **1.1.4 (interpret 4x − 2y = 3 as 4x − 2y + 0z = 3)**
    
    - **Sol technique:** Solve for one variable, treat the remaining variables as parameters.
        
    - **Sig:** Adding variables without adding equations increases degrees of freedom. One equation in three variables is typically a plane.
        
- **1.1.5 (general equation ax = b)**
    
    - **Sol technique:** Split into cases (a \neq 0) (divide) and (a = 0) (check whether (0=b)).
        
    - **Sig:** The form of the equation can force “unique,” “none,” or “infinitely many.” This is the first appearance of consistency logic.
        
- **1.1.6 (one equation can yield 0, 1, or infinitely many solutions)**
    
    - **Sol technique:** Construct examples by forcing a contradiction, a determinate equation, or an identity.
        
    - **Sig:** Counting equations is not enough. What matters is compatibility and how strongly the equation constrains variables.
        

---

## Group 2: Translating between systems and augmented matrices

**Exercises:** 1.1.7, 1.1.8 (and conceptually reinforces 1.1.3 and 1.1.4)

### Shared sol technique

- Fix a variable order.
    
- Each equation becomes one row.
    
- Missing variables get coefficient 0.
    
- The constants column is separated by the bar.
    

### Itemized sig and technique by exercise

- **1.1.7 (system → augmented matrix)**
    
    - **Sol technique:** Write coefficients in the chosen order, append the constant term.
        
    - **Sig:** The augmented matrix is a standardized encoding of the system that makes elimination systematic.
        
- **1.1.8 (augmented matrix → system)**
    
    - **Sol technique:** Read each row as an equation in the fixed variable order.
        
    - **Sig:** Matrices are not new math here, they are bookkeeping that preserves meaning and enables row operations.
        

---

## Group 3: Compute solutions with EROs and RREF

**Exercises:** 1.1.9, 1.1.10, 1.1.11

### Shared sol technique

- Convert to an augmented matrix ([A \mid b]).
    
- Apply **elementary row operations** to reach echelon form or **RREF**.
    
- Classify outcomes by the final form:
    
    - Pivot in every variable column: unique solution.
        
    - Free variables: infinitely many solutions (parametric form).
        
    - A row ([0\ 0\ \dots\ 0 \mid d]) with (d \neq 0): no solution.
        

### Itemized sig and technique by exercise

- **1.1.9 (2 by 2 systems)**
    
    - **Sol technique:** RREF a 2 by 3 augmented matrix, read off (x,y).
        
    - **Sig:** This is the first routine “mechanical solve.” It shows elimination is an algorithm, not an art.
        
- **1.1.10 (3 by 3 systems)**
    
    - **Sol technique:** RREF a 3 by 4 augmented matrix, handle pivots across three variables.
        
    - **Sig:** Same method scales. The purpose of the matrix format is to make scaling up feasible.
        
- **1.1.11 (dependent vs inconsistent pairs)**
    
    - **Sol technique:** Row reduce and watch whether the second equation becomes a multiple of the first (same line) or becomes a contradiction (parallel lines).
        
    - **Sig:** Row reduction does not just give numbers. It diagnoses structure: redundancy versus contradiction.
        

---

## Group 4: Consistency conditions, geometry, and invariants under row operations

**Exercises:** 1.1.12, 1.1.13, 1.1.14

### Shared sol technique

- Use elimination to expose hidden relationships.
    
- Use geometry to interpret solution counts.
    
- Use counterexamples and invariance arguments to prove or disprove claims.
    

### Itemized sig and technique by exercise

- **1.1.12 (symbolic system, condition for inconsistency)**
    
    - **Sol technique:** Row reduce symbolically until you expose a row that becomes (0 = \text{(expression in }a,b,c)). Set that expression to 0 for consistency.
        
    - **Sig:** Some right hand sides are impossible given the left hand relationships. Consistency can impose constraints on parameters.
        
- **1.1.13 (two lines in the plane)**
    
    - **Sol technique:** Interpret each equation as a line. Classify by line positions: intersect once, parallel, coincident.
        
    - **Sig:** The algebraic outcomes match geometry: one solution, none, infinitely many. This is intuition for dependence and inconsistency.
        
- **1.1.14 (true or false statements about systems and EROs)**
    
    - **Sol technique:** Either give a counterexample or prove using equivalence preservation under row operations.
        
    - **Sig:** EROs preserve the solution set. Therefore they preserve consistency and inconsistency, and they justify solving by row reduction.
        

---

## Group 5: Linear algebra hiding inside “nonlinear looking” algebra

**Exercises:** 1.1.15, 1.1.16, 1.1.17

### Shared sol technique

- Choose unknowns so the problem becomes linear in those unknowns.
    
- Translate to a system.
    
- Solve with elimination or RREF.
    
- Interpret back in the original language.
    

### Itemized sig and technique by exercise

- **1.1.15 (quadratic through three points)**
    
    - **Sol technique:** Let coefficients (a,b,c) be unknowns. Each point gives one linear equation in (a,b,c). Solve the 3 by 3 system.
        
    - **Sig:** “Nonlinear curve” does not prevent linear methods. The model is linear in parameters. This is polynomial interpolation and previews regression thinking.
        
- **1.1.16 (change of variables)**
    
    - **Sol technique:** Substitute (x,y) in terms of (x',y'). The chosen substitution is invertible and simplifies the system dramatically. Convert back.
        
    - **Sig:** Solving is about equivalence under invertible transformations, not only row operations. This is the matrix inverse idea in action.
        
- **1.1.17 (partial fractions, equate coefficients)**
    
    - **Sol technique:** Multiply both sides by the common denominator to clear fractions, expand, collect powers of (x), equate coefficients to get a linear system in (a,b,c), then RREF.
        
    - **Sig:** “Equate coefficients” is really “express equality in a basis.” Matching the coefficients forces the same polynomial, which produces a solvable linear system.
        

---

## Group 6: Modeling word problems as (Aq=r) (mixtures and rates)

**Exercises:** 1.1.18, 1.1.19, 1.1.20

### Shared sol technique

- Pick decision variables that represent controllable quantities.
    
- Write one equation per requirement or scenario.
    
- Solve the resulting 2 by 2 system by substitution or RREF.
    
- Check units and verify by plugging back.
    

### Itemized sig and technique by exercise

- **1.1.18 (vitamin supplements)**
    
    - **Sol technique:** Let (x,y) be amounts of each supplement. Write vitamin totals as linear equations, solve.
        
    - **Sig:** Coefficients are “nutrient per unit item.” Rows are constraints, columns are choices. Structural simplification can appear (same D percentage).
        
- **1.1.19 (hourly wages)**
    
    - **Sol technique:** Let (x,y) be hourly rates. Each work schedule is one equation. Solve.
        
    - **Sig:** Scenarios create independent constraints. This is a clean example of modeling the same unknowns under different conditions.
        
- **1.1.20 (fish and meal diet)**
    
    - **Sol technique:** Let (x,y) be grams of fish and meal. Protein and carbs give two constraints, solve and interpret.
        
    - **Sig:** The problem gives ratios per item, and you use them as coefficients in nutrient equations. Variables are the items you control, not the nutrients.
        

---

## One sentence that ties everything together

Chapter 1.1 is teaching you to see every problem as: choose the right unknowns, translate requirements into linear constraints, represent them in a matrix, use equivalence preserving transformations to simplify, then read and interpret the solution set.

# Solutions as substitution, parameters, and degrees of freedom
## 1.1.1
Skill: Can you plug in values of [[parametric form]] equations as [[Solution (math)]] into linear equations with a [[constant term]] 

## Technique:
Exercise 1.1.1(a) is a **verification** problem, not a solving problem. The expected technique is mechanical substitution and checking, not row reduction or elimination.

Here is the intended method.

---

### Technique for Exercise 1.1.1(a)

You are **given** a proposed parametric solution and a **system of equations**. Your task is to verify that the proposal works **for all values of** the parameter.

#### Step 1. Recognize what is being asked

* You are **not** finding the solution.
* You are checking whether the given expressions for (x,y,z) satisfy the equations.
* The phrase *“for all values of (s) and (t)”* signals a **symbolic check**, not plugging in numbers.

---

#### Step 2. Substitute directly into each equation

Take the **first equation** of the system.

* Replace every occurrence of (x), (y), and (z) with the expressions you are given.
* Do this **carefully**, keeping everything symbolic.

You should end up with an expression involving only the parameter (here, (t)).

---

#### Step 3. Simplify completely

* Combine like terms.
* Collect coefficients of (t).
* Simplify constants.

At the end of simplification, one of two things will happen:

* You get a true numerical statement (like (5 = 5)) independent of (t).
* Or you do not, in which case the proposed solution fails.

---

#### Step 4. Repeat for the second equation

Do the **same substitution and simplification** for the second equation.

You must check **every equation** in the system.

---

#### Step 5. Conclude correctly

* If **each equation simplifies to a true statement with no restriction on the parameter**, then the expressions are solutions **for all values of the parameter**.
* You do **not** need to say anything about uniqueness, rank, or matrices.

---

### What this exercise is testing

Conceptually, this problem checks whether you understand that:

* A **solution** is something that satisfies the equations when substituted.
* A **parametric solution** represents infinitely many solutions at once.
* Verification is done by substitution, not by solving again.

This is the same logic used in Example 1.1.1 in the text.

---

If you want, next we can:

* walk through *one line* of the substitution together without finishing it, or
* compare this verification technique to how later exercises use augmented matrices.
## Problems
Exercise 1.1.1 In each case verify that the following are solutions for all values of (s) and (t).

a.  
$$\begin{aligned}
x = 19t - 35\\
y = 25 - 13t\\ 
z = t  
\end{aligned}
$$
is a solution of  
$$\begin{aligned}  
2x + 3y + z &= 5 \\

5x + 7y - 4z &= 0  
\end{aligned}  $$

b.  
$$
\begin{aligned}  
x_1 &= 2s + 12t + 13 \\  
x_2 &= s \\
x_3 &= -s - 3t - 3 \\  
x_4 &= t  
\end{aligned}  
$$
is a solution of  
$$
\begin{aligned}  
2x_1 + 5x_2 + 9x_3 + 3x_4 &= -1 \\  
x_1 + 2x_2 + 4x_3 &= 1  
\end{aligned}  
$$

c.  
$$
\begin{aligned}  
x - y + z &= 2 \\  
x - z &= 1 \\ 
y + 2x &= 0  
\end{aligned}  
$$

d.  
$$
\begin{aligned}  
x + y &= 1 \\ 
y + z &= 0 \\  
z - x &= 2  
\end{aligned}  
$$

---
## 1.1.2
Exercise 1.1.2 Find all solutions to the following in parametric form in two ways.

Lesson: One linear equation defines a **line** (or plane). Parametric form is not unique. Different choices of free variables lead to different but equivalent descriptions.
## Technique

### Step 1. Understand the task

You are given **one linear equation** (in two or three variables) and asked to:

- find **all solutions**, and
    
- express them in **parametric form**,
    
- **in two different ways**.
    

Key signal:

> “Find all solutions in parametric form in two ways”

This means you must choose **different variables to treat as free**.

---

### Step 2. Identify the degrees of freedom

- Count variables.
    
- Count equations.
    

With:

- one equation,
    
- more than one variable,
    

there will be **infinitely many solutions**.

This tells you:

- at least one variable must be **free** (a parameter).
    

---

### Step 3. Choose a variable to solve for (first way)

- Pick **one variable** and solve the equation for it algebraically.
    
- Express that variable **in terms of the remaining variables**.
    

At this point:

- the remaining variables are not constrained by the equation.
    

---

### Step 4. Introduce parameters

- Rename the remaining variables as parameters (for example (s, t)).
    
- Write each original variable explicitly in terms of those parameters.
    

This produces **one parametric description** of the solution set.

---

### Step 5. Choose a different variable (second way)

Now repeat the process, but:

- Solve the original equation for a **different variable**.
    
- Treat the remaining variable(s) as free.
    
- Introduce **new parameters** (often different letters).
    

This gives a **second parametric form** for the _same_ solution set.

Important:  
The two forms may look very different algebraically, but they describe the **same family of solutions**.

---

### Step 6. What not to do

- Do not use augmented matrices here.
    
- Do not try to “find” a single solution.
    
- Do not plug in numbers.
    

This exercise is about understanding:

- freedom vs constraint, and
    
- how parametric descriptions depend on which variables you choose to eliminate.
    

---

### What this exercise is testing

Conceptually, Exercise 1.1.2 checks that you understand:

- One linear equation defines a **line** (or plane).
    
- Parametric form is not unique.
    
- Different choices of free variables lead to different but equivalent descriptions.
    

This directly reinforces the discussion after Example 1.1.2 in the text.

---
## Problems 
a. (3x + y = 2)

b. (2x + 3y = 1)

c. (3x - y + 2z = 5)

d. (x - 2y + 5z = 1)

---
## 1.1.3/1.1.14/1.1.5
- A missing variable still exists.
    
- A coefficient of 0 means “no restriction,” not “the variable disappears.”
    
- A single equation in two variables describes a **vertical line** in the plane.
    
- Parametric form makes that freedom explicit.
## Technique for Exercise 
Meaning:
- A missing variable still exists.
- A coefficient of 0 means “no restriction,” not “the variable disappears.”
- A single equation in two variables describes a **vertical line** in the plane.
- Parametric form makes that freedom explicit.
## Technique
### Step 1. Reinterpret the equation correctly

You are explicitly told to regard  
[  
2x = 5  
]  
as  
[  
2x + 0y = 5.  
]

This is crucial. It tells you:

- There are **two variables**: (x) and (y).
    
- Only **one equation** constrains them.
    

---

### Step 2. Count freedom

- Number of variables: 2
    
- Number of equations: 1
    

Therefore:

- There is **one degree of freedom**.
    
- One variable must be a **parameter**.
    

---

### Step 3. Solve for the constrained variable

- Identify which variable is actually constrained by the equation.
    
- Solve the equation **for that variable only**.
    

This gives a **fixed value** for one variable.

---

### Step 4. Declare the other variable free

- The variable that does not appear (or appears with coefficient 0) is **unconstrained**.
    
- Assign it a parameter, usually (t).
    

This step is essential:  
the equation places **no restriction** on that variable.

---

### Step 5. Write parametric form

- Write **both variables** explicitly:
    
    - the constrained one as a constant,
        
    - the unconstrained one as the parameter.
        

That is the full parametric description of all solutions.

---

### What this exercise is testing

This problem checks whether you understand that:

- A missing variable still exists.
    
- A coefficient of 0 means “no restriction,” not “the variable disappears.”
    
- A single equation in two variables describes a **vertical line** in the plane.
    
- Parametric form makes that freedom explicit.
    

---

### Common mistake to avoid

Do **not** say “there is only one solution for (x), so that’s the solution.”

That ignores the second variable.

The correct mindset is:

> One equation fixes one variable and leaves the other free.

---

If you want, next we can:

- connect this directly to the geometry (vertical line), or
    
- compare it to Exercise 1.1.4 where a third variable is added.

---
## Problems
Exercise 1.1.3 Regarding (2x = 5) as the equation (2x + 0y = 5) in two variables, find all solutions in parametric form.
Here is a **fully worked solution**, written exactly in the style the book expects.

Exercise 1.1.4 Regarding (4x - 2y = 3) as the equation (4x - 2y + 0z = 3) in three variables, find all solutions in parametric form.

Exercise 1.1.5 Find all solutions to the general system (ax = b) of one equation in one variable (a) when (a = 0) and (b) when (a \ne 0).
### Solution

We rewrite the equation as  
[  
2x + 0y = 5.  
]

This is one linear equation in the two variables (x) and (y).

Solve the equation for (x):  
[  
2x = 5 \quad \Rightarrow \quad x = \tfrac{5}{2}.  
]

The equation places **no restriction** on (y), since its coefficient is zero. Therefore (y) may take any real value. Let  
[  
y = t,  
]  
where (t) is an arbitrary real number (a parameter).

Hence all solutions are given in parametric form by  
[  
\begin{aligned}  
x &= \tfrac{5}{2}, \  
y &= t, \qquad t \text{ arbitrary}.  
\end{aligned}  
]






---
## 1.1.6
Exercise 1.1.6 Show that a system consisting of exactly one linear equation can have no solution, one solution, or infinitely many solutions. Give examples.
## Sol

Consider a system with **exactly one linear equation**. The outcome depends on how many variables appear and how the equation constrains them.

### Case 1. No solution (inconsistent)

This happens when the equation reduces to a false statement.

Example:  
[  
0x = 5.  
]

Here the left-hand side is always zero, but the right-hand side is not. There is **no value of (x)** that satisfies the equation, so the system has **no solution**.

---

### Case 2. Exactly one solution

This happens when there is **one variable** and its coefficient is nonzero.

Example:  
[  
2x = 5.  
]

Dividing by (2),  
[  
x = \tfrac{5}{2}.  
]

There is **exactly one solution**.

---

### Case 3. Infinitely many solutions

This happens when the equation does **not fully determine all variables**.

Example with one variable:  
[  
0x = 0.  
]

This equation is true for **every** value of (x), so there are **infinitely many solutions**.

Example with two variables:  
[  
x + y = 3.  
]

This is one equation in two variables, so one variable can be chosen freely and the other adjusts accordingly. The solution set is infinite.

---

## Sig

- This exercise shows that the **number of equations alone does not determine the number of solutions**. What matters is how strongly the equation constrains the variables.
    
- A single linear equation can:
    
    - impose **no constraint** at all (leading to infinitely many solutions),
        
    - impose a **contradiction** (leading to no solutions),
        
    - or impose **one exact constraint** (leading to a unique solution).
        
- It previews the general principle used throughout [[Linear Algebra]]:  
    the number of solutions depends on the relationship between the number of equations, the number of variables, and whether the equations are compatible.
    
- This result motivates later ideas such as [[consistent system]], [[inconsistent system]], and the use of [[augmented matrix|augmented matrices]] to classify solution sets.

---
# Translating between systems and augmented matrices
## 1.1.7/1.1.8
## Sig

- An augmented matrix records, row by row, the coefficients of each variable (in a fixed order) followed by the constant term, separated by a vertical bar.
    
- If a variable is missing from an equation, its coefficient is (0) in the augmented matrix.
    
- Writing a system as an augmented matrix is the setup for solving via elementary row operations and Gaussian elimination.
## Problems
Exercise 1.1.7 Write the augmented matrix for each of the following systems of linear equations.

a.  
$$ 
\begin{aligned}  
x - 3y &= 5 \\ 
2x + y &= 1  
\end{aligned}  
$$

b.  
$$ 
\begin{aligned}  
x + 2y &= 0 \\  
y &= 1  
\end{aligned}  
$$
Exercise 1.1.8 Write a system of linear equations that has each of the following augmented matrices.

a.  
$$
\left[  
\begin{array}{rrr|r}  
1 & -1 & 6 & 0 \\  
0 & 1 & 0 & 3 \\  
2 & -1 & 0 & 1  
\end{array}  
\right]  
$$

b.  
$$
\left[  
\begin{array}{rrr|r}  
2 & -1 & 0 & -1 \\
-3 & 2 & 1 & 0 \\
0 & 1 & 1 & 3  
\end{array}  
\right]  
$$


## Sol

### (a)

System:  
[  
\begin{aligned}  
x - 3y &= 5 \  
2x + y &= 1  
\end{aligned}  
]

Augmented matrix:  
[  
\left[  
\begin{array}{rr|r}  
1 & -3 & 5 \  
2 & 1 & 1  
\end{array}  
\right]  
]

---

### (b)

System:  
[  
\begin{aligned}  
x + 2y &= 0 \  
y &= 1  
\end{aligned}  
]

Write the second equation as (0x + 1y = 1). Then the augmented matrix is:  
[  
\left[  
\begin{array}{rr|r}  
1 & 2 & 0 \  
0 & 1 & 1  
\end{array}  
\right]  
]

---


# Compute solutions with EROs and RREF
## 1.1.9
Exercise 1.1.9 Find the solution of each of the following systems of linear equations using augmented matrices.

a.  
$$
\begin{aligned}  
x - 3y &= 1 \\  
2x - 7y &= 3  
\end{aligned} 
$$

b.  
$$
\begin{aligned}  
x + 2y &= 1 \\  
3x + 4y &= -1  
\end{aligned}  
$$

c.  
$$
\begin{aligned}  
2x + 3y &= -1 \\
3x + 4y &= 2  
\end{aligned}  
$$

d.  
$$
\begin{aligned}  
3x + 4y &= 1 \\
4x + 5y &= -3  
\end{aligned}  
$$

---
## 1.1.10
Exercise 1.1.10 Find the solution of each of the following systems of linear equations using augmented matrices.

a.  
$$
\begin{aligned}  
x + y + 2z &= -1 \\
2x + y + 3z &= 0 \\
-2y + z &= 2  
\end{aligned}  
$$

b.  
$$
\begin{aligned}  
2x + y + z &= -1 \\  
x + 2y + z &= 0 \\  
3x - 2z &= 5  
\end{aligned}  
$$

---
## 1.1.11
Exercise 1.1.11 Find all solutions (if any) of the following systems of linear equations.

a.  
$$
\begin{aligned}  
3x - 2y &= 5 \\
-12x + 8y &= -20  
\end{aligned}  
$$

b.  
$$
\begin{aligned}  
3x - 2y &= 5 \\  
-12x + 8y &= 16  
\end{aligned}  
$$

---
# Consistency conditions, geometry, and invariants under row operations
## *1.1.12*
Exercise 1.1.12 Show that the system  
$$
\begin{cases}  
x + 2y - z = a \\  
2x + y + 3z = b \\
x - 4y + 9z = c  
\end{cases}  
$$
is inconsistent unless ($c = 2b - 3a$).
## Technique A: Eliminate to expose a necessary condition

Start with the system  
$$
\begin{cases}  
x+2y-z=a\\  
2x+y+3z=b\\  
x-4y+9z=c  
\end{cases}  
$$

Goal: combine equations to eliminate (x) and (y) so you get an equation involving only (z) on the left. If two different eliminations produce different required values for the same expression, consistency forces a relation among (a,b,c).

Steps (conceptually):

1. Use the first two equations to eliminate (x) (form ($E_2-2E_1$).  
    This gives a new equation involving only (y) and (z) with right side involving (a,b).
    
2. Use the first and third equations to eliminate (x) (form ($E_3-E_1$).  
    This gives another equation involving only (y) and (z) with right side involving (a,c).
    
3. Now eliminate (y) between those two new equations (take an appropriate linear combination).  
    The left side becomes (0) (or a multiple of (z) that cancels), so you end with something like  
    $$
    0 = \text{(some combination of }a,b,c\text{)}.  
    $$
    
4. Consistency requires the right side to be (0). That gives the needed condition on (a,b,c). When you simplify, it should come out as  
    $$ 
    c=2b-3a.  
    $$
    

This is exactly the “hidden constraint” idea: the third equation must be a linear combination of the first two in order to avoid contradiction.

---

## Technique B: Do a quick row-reduction with symbols

Write the augmented matrix:  
$$
\left[  
\begin{array}{ccc|c}  
1&2&-1&a\\  
2&1&3&b\\  
1&-4&9&c  
\end{array}  
\right].  
$$

Then perform row operations (no need to fully solve for (x,y,z):

1. Eliminate (x) from rows 2 and 3 using row 1:
    
    - ($R_2 \leftarrow R_2-2R_1$)
        
    - ($R_3 \leftarrow R_3-R_1$)
        
2. Next eliminate (y) in row 3 using row 2 (scale row 2 if needed to match coefficients).
    
3. You will eventually reach a last row of the form  
    $$  
    0\ \ 0\ \ 0\mid \text{(expression in }a,b,c\text{)}.  
    $$
    
4. The system is inconsistent unless that right-hand expression equals (0). Setting it to (0) simplifies to  
    $$
    c=2b-3a.  
    $$
    

This method directly ties to the “inconsistent row” criterion ($0=d\neq 0$).

---

## What to say in your writeup

- “Row-reduce/eliminate to see what conditions are required for the last equation not to contradict the others.”
    
- “The system becomes inconsistent exactly when the reduction produces a row (0= \text{nonzero expression}).”
    
- “Setting that expression to zero yields ($c=2b-3a$).”
    

If you paste your elimination steps or your intermediate augmented matrices, I can point out the cleanest combination that makes the condition pop out quickly.
## 1.1.13
Exercise 1.1.13 
By examining the possible positions of lines in the plane, show that two equations in two variables can have zero, one, or infinitely many solutions.

---

## Sol

A linear equation in two variables has the form  
[  
ax+by=c  
]  
with ((a,b)\neq(0,0)). Its graph in the (xy)-plane is a line. A system of two such equations is two lines:

[  
\begin{cases}  
a_1x+b_1y=c_1\  
a_2x+b_2y=c_2  
\end{cases}  
]

A solution ((x,y)) is a point that lies on **both** lines, so the solution set is the **intersection** of the two lines. In the plane, two lines can be positioned in only three ways:

### 1) Intersecting lines → one solution

If the lines have different slopes, they cross at exactly one point. That unique intersection point is the unique solution.

Example:  
[  
\begin{cases}  
x+y=2\  
x-y=0  
\end{cases}  
]  
These lines intersect once, so there is exactly one solution.

### 2) Parallel distinct lines → no solution

If the lines have the same slope but different intercepts, they never meet. Then there is no point satisfying both equations, so the system has no solution (inconsistent).

Example:  
[  
\begin{cases}  
x+y=2\  
x+y=3  
\end{cases}  
]  
Same left side, different constants, so the lines are parallel and distinct. No solution.

### 3) Coincident lines → infinitely many solutions

If the two equations describe the same line, then every point on that line satisfies both equations, so there are infinitely many solutions.

Example:  
[  
\begin{cases}  
x+y=2\  
2x+2y=4  
\end{cases}  
]  
The second equation is a multiple of the first, so they are the same line. Infinitely many solutions.

These three cases exhaust all possibilities for two lines in the plane, so two linear equations in two variables can have zero, one, or infinitely many solutions.

---

## Sig

- A system of two linear equations in two variables is a question about the intersection of two lines.
    
- The number of solutions equals the number of intersection points: none (parallel), one (intersect once), infinitely many (same line).
    
- Algebraically this matches coefficient comparisons:
    
    - proportional coefficients but mismatched constants → no solution,
        
    - proportional coefficients and proportional constants → infinitely many solutions,
        
    - nonproportional coefficients → unique solution.
---
## 1.1.14
Exercise 1.1.14 In each case either show that the statement is true, or give an example showing it is false.
## Sol

### (a) “If a linear system has (n) variables and (m) equations, then the augmented matrix has (n) rows.”

False.

The augmented matrix has one row per equation, so it has (m) rows, not (n).

Counterexample: take (n=2) variables and (m=3) equations, e.g.  
[  
\begin{cases}  
x+y=1\  
x-y=0\  
2x+y=3  
\end{cases}  
]  
The augmented matrix is  
[  
\left[\begin{array}{cc|c}  
1&1&1\  
1&-1&0\  
2&1&3  
\end{array}\right]  
]  
which has (3) rows, not (2).

---

### (b) “A consistent linear system must have infinitely many solutions.”

False.

A consistent system can have exactly one solution.

Counterexample:  
[  
\begin{cases}  
x=1\  
y=2  
\end{cases}  
]  
This is consistent and has the unique solution ((1,2)).

---

### (c) “If a row operation is done to a consistent linear system, the resulting system must be consistent.”

True.

Elementary row operations produce an equivalent system (same solution set). If the original system is consistent (has at least one solution), an equivalent system has that same solution, so it is also consistent.

---

### (d) “If a series of row operations on a linear system results in an inconsistent system, the original system is inconsistent.”

True.

Row operations preserve equivalence. If after row operations you get an inconsistent system, that final system has no solutions. Because it is equivalent to the original, the original also has no solutions, so it is inconsistent.

---

## Sig

- Rows correspond to equations, so the augmented matrix has (m) rows (not (n)).
    
- “Consistent” means at least one solution, which can be unique or infinite.
    
- Row operations preserve the solution set, so they preserve consistency or inconsistency.

---
# Linear algebra hiding inside “nonlinear looking” algebra
## *1.1.15*
Exercise 1.1.15 Find a quadratic (a + bx + cx^{2}) such that the graph of (y = a + bx + cx^{2}) contains each of the points ((-1, 6)), ((2, 0)), and ((3, 2)).

## Why we are doing this

The point of the exercise is not “quadratics” by itself. It is showing a general method:

> Convert a verbal or geometric requirement into a [[Linear system]] in unknown parameters, then solve it with the same tools you use for any system.

Here the unknowns are the **coefficients** $a,b,c$. Even though the model is quadratic in $x$, it is **linear in the parameters** $(a,b,c)$, which is why the chapter’s linear-system machinery applies.

This is also a first example of [[polynomial interpolation]]: with enough data points, you can determine a polynomial that fits them exactly.

---

## Solution notes

### Step 1: Translate “passes through a point” into an equation

If the graph of $y=a+bx+cx^2$ passes through $(x_0,y_0)$, that means:

$$  
y_0 = a + b x_0 + c x_0^2.  
$$

So each point gives one linear equation in $a,b,c$.

### Step 2: Build the linear system from the three points

Using $(-1,6)$, $(2,0)$, $(3,2)$:

- From $(-1,6)$:  
    $$  
    a - b + c = 6  
    $$
    
- From $(2,0)$:  
    $$  
    a + 2b + 4c = 0  
    $$
    
- From $(3,2)$:  
    $$  
    a + 3b + 9c = 2  
    $$
    

This is a 3 equation, 3 unknown system.

### Step 3: Solve by elimination

Subtract (2) from (3):  
$$  
b + 5c = 2  
$$

Subtract (1) from (2):  
$$  
3b + 3c = -6 \Rightarrow b + c = -2  
$$

Solve:

- $b+c=-2$
    
- $b+5c=2$
    

Subtract:  
$$  
4c = 4 \Rightarrow c=1  
$$  
Then:  
$$  
b=-3  
$$

Plug into $a+2b+4c=0$:  
$$  
a + 2(-3) + 4(1)=0 \Rightarrow a=2  
$$

### Final quadratic

$$  
y = x^2 - 3x + 2.  
$$

---

## Significance

### 1) Linear algebra in disguise

The “quadratic fitting” becomes a linear algebra task because $(a,b,c)$ enter linearly. This is the same structural idea behind [[linear regression]]: nonlinear-looking curves in $x$ can still be linear in coefficients.

### 2) Why three points determine a unique quadratic

A quadratic has three free parameters $(a,b,c)$. Each point gives one independent condition (typically). With three distinct $x$-values, you usually get a unique solution because the coefficient matrix is invertible.

 Matrix form:  
$$  
\begin{bmatrix}  
1 & -1 & 1\\  
1 & 2 & 4\\  
1 & 3 & 9  
\end{bmatrix}  
\begin{bmatrix}  
a\\ b\\ c  
\end{bmatrix}
=
\begin{bmatrix}  
6\\ 0\\ 2  
\end{bmatrix}.  
$$

That left matrix is a [[Vandermonde matrix]] built from the $x$-values.

### 3) Interpolation vs fitting

This is **interpolation**: you have exactly enough flexibility to hit every point perfectly. In data work, when you have more points than parameters, you move to approximate fit (least squares), but the core idea “build equations from conditions” stays the same.

### 4) Connection to EROs

Solving is done by elimination, which is implemented by [[Elementary row operations]]. EROs matter here because they preserve the [[solution set]] of the system, so the transformed system is equivalent to the original constraints.
---
## 1.1.16
Exercise 1.1.16 Solve the system  
$$
\begin{cases}  
3x + 2y = 5 \\  
7x + 5y = 1  
\end{cases}  
$$
by changing variables  
$$
\begin{cases}  
x = 5x' - 2y' \\  
y = -7x' + 3y'  
\end{cases}  
$$  
and solving the resulting equations for (x') and (y').

---
## 1.1.17
Exercise 1.1.17 Find (a, b,) and (c) such that  
$$ 
\frac{x^{2} - x + 3}{(x^{2} + 2)(2x - 1)} = \frac{ax + b}{x^{2} + 2} + \frac{c}{2x - 1}.  
$$

\[Hint: Multiply through by ((x^{2} + 2)(2x - 1)) and equate coefficients of powers of (x).]

---
# Modeling word problems as $Aq=r$ (mixtures and rates)
## 1.1.18/19/20
Exercise 1.1.18 A zookeeper wants to give an animal 42 mg of vitamin A and 65 mg of vitamin D per day. He has two supplements: the first contains 10% vitamin A and 25% vitamin D; the second contains 20% vitamin A and 25% vitamin D. How much of each supplement should he give the animal each day?

---
Exercise 1.1.19 Workmen John and Joe earn a total of $24.60 when John works 2 hours and Joe works 3 hours. If John works 3 hours and Joe works 2 hours, they get $23.90. Find their hourly rates.
 - - - 
Exercise 1.1.20 A biologist wants to create a diet from fish and meal containing 183 grams of protein and 93 grams of carbohydrate per day. If fish contains 70% protein and 10% carbohydrate, and meal contains 30% protein and 60% carbohydrate, how much of each food is required each day?

---
## Problem

A zookeeper wants **42 mg** of vitamin A and **65 mg** of vitamin D per day.  
Supplement 1: 10% A, 25% D.  
Supplement 2: 20% A, 25% D.  
How much of each supplement per day?

---

## Why we are doing this

This is a standard “mixture” setup: unknown amounts times known percentages must hit target totals. The key move is to translate the word problem into a [[Linear system]], then solve it with elimination or [[RREF]].

---

## Solution (sol)

Let

- (x) = amount of supplement 1 (in mg)
    
- (y) = amount of supplement 2 (in mg)
    

Vitamin A requirement:  
[  
0.10x + 0.20y = 42  
]

Vitamin D requirement:  
[  
0.25x + 0.25y = 65  
]

From the D equation:  
[  
0.25(x+y)=65 \Rightarrow x+y=260  
]

Substitute (y=260-x) into the A equation:  
[  
0.10x + 0.20(260-x)=42  
]  
[  
0.10x + 52 - 0.20x = 42  
]  
[  
-0.10x = -10 \Rightarrow x=100  
]  
[  
y=260-100=160  
]

**Answer:** (x=100) mg of supplement 1 and (y=160) mg of supplement 2.

Quick check:

- A: (0.10(100)+0.20(160)=10+32=42)
    
- D: (0.25(100)+0.25(160)=25+40=65)
    

---

## Matrix form (same solution)

 Write (A\mathbf{u}=\mathbf{b}) with (\mathbf{u}=\begin{bmatrix}x\y\end{bmatrix}):  
[  
\begin{bmatrix}  
0.10 & 0.20\  
0.25 & 0.25  
\end{bmatrix}  
\begin{bmatrix}x\y\end{bmatrix}

\begin{bmatrix}42\65\end{bmatrix}.  
]

 To avoid decimals, multiply the first row by 10 and the second by 4 (equivalent scaling of equations):  
[  
\begin{bmatrix}  
1 & 2\  
1 & 1  
\end{bmatrix}  
\begin{bmatrix}x\y\end{bmatrix}

\begin{bmatrix}420\260\end{bmatrix}.  
]

Augmented matrix and RREF:  
[  
\left[\begin{array}{cc|c}  
1&2&420\  
1&1&260  
\end{array}\right]  
\to  
\left[\begin{array}{cc|c}  
1&2&420\  
0&-1&-160  
\end{array}\right]  
\to  
\left[\begin{array}{cc|c}  
1&0&100\  
0&1&160  
\end{array}\right].  
]

So (x=100,\ y=160).

---

## Significance (sig)

- **Linear system from composition constraints:** percentages become coefficients; required totals become the right-hand side. This is the main modeling pattern.
    
- **Notable structure:** both supplements have **25% vitamin D**, so the D equation collapses to “total supplement amount” (x+y). The A equation then decides how that total must be split.
    
- **General lesson:** mixture, rate, and budget problems often reduce to (A\mathbf{u}=\mathbf{b}), solved by [[Elementary row operations]] or substitution.
    

---

## Related links

- [[Linear system]]
    
- [[Augmented matrix]]
    
- [[RREF]]
    
- [[Elementary row operations]]
    
- [[Mixture problem]]

---
