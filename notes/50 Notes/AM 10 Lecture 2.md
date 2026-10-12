---
title: "Gaussian Elimination, RREF, and Vectors in R^n"
aliases:
  - "Row Reduction Notes"
  - "Gaussian Elimination & RREF"
  - "Vectors and Matrices (Intro)"
tags:
  - linear-algebra
  - math
  - notes
  - gaussian-elimination
  - rref
  - matrices
  - vectors
  - systems-of-linear-equations
type: lecture
subject: "Linear Algebra"
topics:
  - "Solving linear systems"
  - "Elementary row operations (EROs)"
  - "Row echelon form (REF)"
  - "Reduced row echelon form (RREF)"
  - "Vector notation in R^n"
  - "Augmented matrix [A|B]"
  - "Parametric vector form of solution sets"
key_terms:
  - "pivot"
  - "free variable"
  - "parameter"
  - "coefficient matrix"
  - "constant vector"
  - "augmented matrix"
definitions:
  - "R^n: n-dimensional Euclidean space of real n-tuples"
  - "Matrix: m×n rectangular array (m rows, n columns)"
  - "REF: pivots move right, zero rows at bottom (pivot=1 optional)"
  - "RREF: REF + pivot=1 + pivot columns have zeros above/below pivots"
methods:
  - "Translate system ↔ augmented matrix"
  - "Apply EROs: swap, scale, replacement"
  - "Gaussian elimination to REF, then to RREF"
  - "Describe solution set using parameters and vectors"
worked_example:
  system: 
    - "2x + y - 3z = 4"
    - "x - y + 2z = 1"
    - "x + 2y - 5z = 3"
  rref_result:
    - "x - (1/3)z = 5/3"
    - "y - (7/3)z = 2/3"
    - "0 = 0"
  solution_set:
    parametric: "(x,y,z) = (5/3 + (1/3)t, 2/3 + (7/3)t, t)"
    vector_form: " [5/3, 2/3, 0]^T + t[1/3, 7/3, 1]^T "
observations:
  - "System information is encoded in coefficients; variables are placeholders."
  - "EROs can be performed on augmented matrices without explicit variables."
  - "RREF is unique (path to it is not)."
created: 2026-02-12
updated: 2026-02-12
status: draft
parent: "[[Nicholson]]"
domain: math
---
# Summary of core concepts, vocab, and practicals

## Core concepts
- **Elementary Operations** 
	- Rearranging makes sense
	- Scaling preserves the relationship as it scales the entire equation. It's the same statement of equality.
	- Replacement is less intuitive but is used the most though more useful because it allows the elimination of variables
- Vectors
	- **The [[Solution (math)|Set of Solutions]] of a [[system of linear equations]] is an [[n-tuple|ordered n-tuple]] of [[Real numbers|Reals]]**
		- Fill-in definition
			- The set of '*objects that satisfies a given condition, statement, or structure*' of a *'finite [[collection]] of [[linear equation]]s in the same variables, all of which must be satisfied at the same time'* is an ***ordered list** of $n$ elements:* $(a_1,a_2,\dots,a_n)$ in set of the numbers that live on the continuous [[number line]].
	- Ordered because $(x=2,y=1) \neq (y=2,x=1)$
	- So we can describe these solutions as a [[coordinate]] and a vector
	- There are row vectors and column vectors to describe these solutions
	- Vectors are lists of numbers (used to store variables, data, or directions)
	- A single vector is usually **represented** as either a column ($n\times1$) or a row ($1\times n$) depending on how it will be used.
		- Column vector: numbers down, shape $n\times 1$.
		- Row vector: numbers across, shape $1\times n$.
	- In $A\mathbf{x}=\mathbf{b}$ (with $A$ $m\times n$), $\mathbf{x}$ must be a column so $A\mathbf{x}$ is [[defined]].
	- Same entries can appear in either form, but orientation changes what multiplications are allowed.
	- Letter bar in vector calc applications means vector not average
- Space
	- If all ordered n-tuples of real \#s are collected ... we'd have a set, the set of all reals $\mathbb{R}^n$. This becomes a [[space (mathematics)]], more specifically a vector space (a space in which vectors are defined), with a space being a set with inherent structures given by the field it plays with (see the formal notation below for this space))
		- We can know now that this space can be thought of being composed by either coordinates or row vectors.
			- $\left\{(x_1,x_2,\ldots,x_n)\;:\;x_i\in\mathbb{R},\ \text{for }1\le i\le n\right\}$
			- $\left\{[x_1,x_2,\ldots,x_n]\;:\;x_i\in\mathbb{R},\ \text{for }1\le i\le n\right\}$
			- $\left\{\begin{bmatrix}x_1\\x_2\\\vdots\\x_n\end{bmatrix}:\ x_i\in\mathbb{R},\ \text{for }1\le i\le n\right\}$
			- Despite 
			- n-dimensional [[Euclidean space]]
				- This is significant because it means we can use the graphical algebra we're used to
			- Finally recall that we're expected to be able to know that a vector is just an arrow to the point.
- Arithmetic in the vector space of $\mathbb{R}^n$
	- Addition
		- $\begin{bmatrix}x_1\\\vdots\\x_n\end{bmatrix}+\begin{bmatrix}y_1\\\vdots\\y_n\end{bmatrix}=\begin{bmatrix}x_1+y_1\\\vdots\\x_n+y_n\end{bmatrix}$
	- Multiplication
		- $a\begin{bmatrix}x_1\\\vdots\\x_n\end{bmatrix}=\begin{bmatrix}ax_1\\\vdots\\ax_n\end{bmatrix}$
- Examples of Vector Space Arithmetic/Introduction of the Linear Combination
	- Addition
		- $\begin{bmatrix} 2\\ 1\\ 3\\ 0 \end{bmatrix} + \begin{bmatrix} -1\\ 4\\ 1\\ 5 \end{bmatrix} = \begin{bmatrix} 1\\ 5\\ 4\\ 5 \end{bmatrix}$
	- Multiplication using scalars
		- $2\begin{bmatrix} 1\\ 0\\ 1\\ 0 \end{bmatrix} -3\begin{bmatrix} 0\\ 2\\ 1\\ 4 \end{bmatrix} +4\begin{bmatrix} 2\\ -1\\ 2\\ -3 \end{bmatrix} = \begin{bmatrix} 10\\ -10\\ 7\\ -24 \end{bmatrix}$
> The above is a sum of [[Scalar Multiples]] in the same space 
		This is a [[Linear combination]]
- Set Notation With Systems Of Linear Equations/Vector Column Solutions Preferred
	- Take the set of solutions found at the end of lecture one
		- $S=\left\{\left(\frac13 t+\frac53,\ \frac73 t+\frac23,\ t\right):\ t\in\mathbb{R}\right\}$
			Let's normalize that **we're writing such a solution now as a column vector** because that's more vital to our purposes.
		- $S=\left\{\begin{bmatrix}\frac13 t+\frac53\\[2pt]\frac73 t+\frac23\\[2pt]t\end{bmatrix}:\ t\in\mathbb{R}\right\}\subseteq\mathbb{R}^3$
		- Note that if we were to clear the denominators (multiply by 3) those are equivalent sets
		- We can also do something which is even more advantageous for our purposes
- Factoring out parameters in solution sets (from solved systems of linear equations)
	- $S=\left\{\begin{bmatrix}\frac53\\[2pt]\frac23\\[2pt]0\end{bmatrix}+t\begin{bmatrix}\frac13\\[2pt]\frac73\\[2pt]1\end{bmatrix}:\ t\in\mathbb{R}\right\}$
	- This form is useful because it separates the solution set into:
		- a fixed point (a particular solution) $\begin{bmatrix}\frac53\\[2pt]\frac23\\[2pt]0\end{bmatrix}$
		- plus a direction vector scaled by a parameter $t\begin{bmatrix}\frac13\\[2pt]\frac73\\[2pt]1\end{bmatrix}$
	- Point view (geometric meaning)
		- The set $\{t\mathbf{v}:t\in\mathbb{R}\}$ is a line through the origin in the direction of $\mathbf{v}$.
		- Adding a fixed vector $\mathbf{p}$ shifts that line so it passes through $\mathbf{p}$:
			- $\{\mathbf{p}+t\mathbf{v}:t\in\mathbb{R}\}$ is a line through the point $\mathbf{p}$.
	- Affine (coordinate) form of the same line
		- $x=\frac53+\frac13t$
		- $y=\frac23+\frac73t$
		- $z=t$
	- So $S$ is a line in $\mathbb{R}^3$ passing through $\begin{bmatrix}\frac53\\[2pt]\frac23\\[2pt]0\end{bmatrix}$ in the direction $\begin{bmatrix}\frac13\\[2pt]\frac73\\[2pt]1\end{bmatrix}$
- We don't need the variables to perform elementary row operations
	- All the [[Information (math)]] in a [[system of linear equations|linear system]] is "encoded" in the coefficents of the system
	- The variables are "placeholders" 
		- they're parameters, they don't change and don't take any constant value on
		- so because they 
- Matrix Introduction
	- An [[m x n matrix]] is a rectangular [[array]] of numbers or fraction 
- Matrix notation
	- We don't want to have to write the entire matrix with it's subscript describing it's proportions and so we can write it that way in brackets with the subscript where it's bounded by $1<i<m$, $1<j<m$
		- There are three ways of abbreviating  $A= \begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n}\\ a_{21} & a_{22} & \cdots & a_{2n}\\ \vdots & \vdots & \ddots & \vdots\\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{bmatrix}$
		- $A$
	
		- $A=\bigl[a_{ij}\bigr]_{1\le i\le m,\;1\le j\le n}$
		- $A=(a_{ij})_{1\le i\le m,\;1\le j\le n}$
	- **SO MATRIXES TAKE IN M EQUATIONS IN N VARIABLES** M x N
- Augmented Matrix
	- Augmented matrixes because there's one column of output will have m rows and n+1 columns with the +1 being the vector b of solutions.
	- Formally, an augmented matrix is the m x (n+1) matrix whose i^th row consists of the coefficents of the i^th Eq:
$$
\begin{aligned}
a_{11}x_1+a_{12}x_2+\cdots+a_{1n}x_n &= b_1\\
a_{21}x_1+a_{22}x_2+\cdots+a_{2n}x_n &= b_2\\
\vdots\qquad\qquad\vdots\qquad\ddots\qquad\vdots\;\; & \vdots\\
a_{m1}x_1+a_{m2}x_2+\cdots+a_{mn}x_n &= b_m
\end{aligned}
$$
$$
\sum_{j=1}^{n} a_{ij}x_j=b_i \qquad (i=1,2,\dots,m)
$$
$$
Ax=b,
\quad
A=\bigl[a_{ij}\bigr]_{m\times n},\;
x=\begin{bmatrix}x_1\\ \vdots\\ x_n\end{bmatrix},\;
b=\begin{bmatrix}b_1\\ \vdots\\ b_m\end{bmatrix}
$$
- Coefficent Matrixes
What symbols do you not need?

You don't need + x subscript index and = 

 The coefficient matrix is a matrix with a column for solutions or constants
a_ij = coefficent of x_j in eq. i

Because the column is now seperate bbar is called the constant vector of the system

 If we want to simplify a linear system we perform **elementary operations**

Reduced row echelon form then compels changing it back to a system of linear functions so one can read what it says about each variable

- Parameters
	- t is the possible values of x,y,z or the functions themselves t is arbitrary but x,y,z are the componenets of a function, a rule.

- Guassian Elim
	- Definintely the fastest by hand and the most effective in our uses but some other forms of matrixes like sparse matrixes have better more compulationally efficent ways of solving

leading non-zero coefficent in a row of a matrix is called a pivot

- RREF 
	Defined by being
		In REF
		All pivots =1
		All non-pivot entries in a pivot column = 0 
			All as in above and below
	- there's really no reason not to do RREF when to reach REF it's the same steps. You can find the sols. effectively with both, but why not just solve for all
- Solving a linear system
	- 









- **Linear systems** can be solved by transforming their **augmented matrix** using **elementary row operations (EROs)**.
- The **coefficients encode the whole system**; variables are placeholders, so we can work directly with matrices.
- **Free variables** create families of solutions described with a **parameter**.
- Solution sets are best expressed in **parametric vector form**: particular solution + parameter · direction vector.

## Vocab
- **Vector (in $\mathbb{R}^n$)**: an ordered $n$-tuple of real numbers.
- **$\mathbb{R}^n$**: the set of all real $n$-tuples (Euclidean $n$-space).
- **Matrix**: an $m\times n$ rectangular array ($m$ rows, $n$ columns).
- **Coefficient matrix** $A=[a_{ij}]$: coefficients of variables.
- **Constant vector** $B=\begin{bmatrix} b_1 \\ \vdots \\ b_m \end{bmatrix}$.
- **Augmented matrix** $[A\mid B]$: coefficients with constants appended.
- **Pivot**: leading (leftmost) nonzero entry in a row.
- **REF (row echelon form)**: pivots move right as you go down; zero rows at bottom (pivot $=1$ optional).
- **RREF (reduced row echelon form)**: REF + pivots are $1$ + pivot columns have zeros above and below pivots.
- **Gaussian elimination**: algorithmic use of EROs to reach REF, then RREF.
- **EROs**:
  - Swap: $R_i \leftrightarrow R_j$
  - Scale: $cR_i \to R_i$ with $c\neq 0$
  - Replace: $R_i + cR_j \to R_i$

## Practicals (what you do)
1. Translate a system $\leftrightarrow$ augmented matrix $[A\mid B]$.
2. Apply EROs to reach $\operatorname{rref}([A\mid B])$.
3. Translate RREF back to equations.
4. Identify pivots vs free variables.
5. Write solutions:
   - parametric form $(x,y,z)=(\dots)$
   - vector form $\mathbf{x}=\mathbf{x}_p + t\,\mathbf{v}$.

---

# Slides

## Slide 1
**Last time: system**
$$
\begin{cases}
2x+y-3z=4\\
x-y+2z=1\\
x+2y-5z=3
\end{cases}
$$

**After row reduction**
$$
\begin{cases}
x-\frac{1}{3}z=\frac{5}{3}\\
y-\frac{7}{3}z=\frac{2}{3}\\
0=0
\end{cases}
$$

---

## Slide 2
**Elementary operations (on equations or rows)**
1. Rearranging  
2. Scaling  
3. Replacement  

Key idea: we can apply them directly to the **augmented matrix**.

---

## Slide 3
**Notation for vectors**
- Point: $(x_1,x_2,\dots,x_n)$
- Row vector: $[x_1\ x_2\ \dots\ x_n]$
- Column vector:
$$
\begin{bmatrix}
x_1\\
x_2\\
\vdots\\
x_n
\end{bmatrix}
$$
- Shorthand: $\bar{x}$

---

## Slide 4
**Definition of $\mathbb{R}^n$**
$$
\mathbb{R}^n=\{(x_1,\dots,x_n):x_i\in\mathbb{R}\}
$$
$$
\mathbb{R}^n=\left\{
\begin{bmatrix}
x_1\\
\vdots\\
x_n
\end{bmatrix}
:x_i\in\mathbb{R}
\right\}
$$
$\mathbb{R}^n$ is $n$-dimensional Euclidean space.

---


---

---

## Slide 9
**Solution set (parametric form)**
$$
S=\left\{
\left(
\frac{1}{3}t+\frac{5}{3},\ 
\frac{7}{3}t+\frac{2}{3},\ 
t
\right)
:t\in\mathbb{R}
\right\}
$$

As column vectors:
$$
S=\left\{
\begin{bmatrix}
\frac{1}{3}t+\frac{5}{3}\\
\frac{7}{3}t+\frac{2}{3}\\
t
\end{bmatrix}
:t\in\mathbb{R}
\right\}\subseteq\mathbb{R}^3
$$

---

## Slide 10
**Solution set (vector form)**
$$
S=\left\{
\begin{bmatrix}
\frac{5}{3}\\
\frac{2}{3}\\
0
\end{bmatrix}
+t\begin{bmatrix}
\frac{1}{3}\\
\frac{7}{3}\\
1
\end{bmatrix}
:t\in\mathbb{R}
\right\}
$$

Why this is “better”: it separates a **particular solution** and a **direction**.

---

## Slide 11
**Observations**
1. The information in a linear system is encoded in the **coefficients**. Variables are placeholders.
2. We don’t need variables to perform row operations (work on matrices).

---

## Slide 12
**Matrix definition**
An $m\times n$ matrix is a rectangular array.  
$m$ rows, $n$ columns.

---

## Slide 13
**Matrix notation**
$$
A=\begin{bmatrix}
a_{11}&a_{12}&\cdots&a_{1n}\\
a_{21}&a_{22}&\cdots&a_{2n}\\
\vdots&\vdots& &\vdots\\
a_{m1}&a_{m2}&\cdots&a_{mn}
\end{bmatrix}
=[a_{ij}]
$$
$a_{ij}$ is the entry in row $i$, column $j$.

---

## Slide 14
**Augmented matrix**
Given
$$
\begin{aligned}
a_{11}x_1+\cdots+a_{1n}x_n&=b_1\\
\vdots\qquad\qquad\qquad&\vdots\\
a_{m1}x_1+\cdots+a_{mn}x_n&=b_m
\end{aligned}
$$

Augmented matrix:
$$
\left[
\begin{array}{cccc|c}
a_{11}&\cdots&a_{1n}& &b_1\\
\vdots& &\vdots& &\vdots\\
a_{m1}&\cdots&a_{mn}& &b_m
\end{array}
\right]
$$

---

## Slide 15
**Coefficient matrix and constant vector**
- Coefficient matrix: $A=[a_{ij}]$
- Constant vector:
$$
B=\begin{bmatrix}
b_1\\
\vdots\\
b_m
\end{bmatrix}
$$

Shorthand:
$$
\left[\begin{array}{c|c}A&B\end{array}\right]=[A\mid B]
$$

---

## Slide 16
**Translate system to augmented matrix**
$$
\begin{cases}
2x+y-3z=4\\
x-y+2z=1\\
x+2y-5z=3
\end{cases}
\Longleftrightarrow
\left[
\begin{array}{ccc|c}
2&1&-3&4\\
1&-1&2&1\\
1&2&-5&3
\end{array}
\right]
$$

---

## Slide 17
**Row reduction (EROs)**

$R_1\leftrightarrow R_2$
$$
\left[
\begin{array}{ccc|c}
1&-1&2&1\\
2&1&-3&4\\
1&2&-5&3
\end{array}
\right]
$$

$R_2-2R_1\to R_2$
$$
\left[
\begin{array}{ccc|c}
1&-1&2&1\\
0&3&-7&2\\
1&2&-5&3
\end{array}
\right]
$$

---

## Slide 18

$R_3-R_1\to R_3$
$$
\left[
\begin{array}{ccc|c}
1&-1&2&1\\
0&3&-7&2\\
0&3&-7&2
\end{array}
\right]
$$

$R_3-R_2\to R_3$
$$
\left[
\begin{array}{ccc|c}
1&-1&2&1\\
0&3&-7&2\\
0&0&0&0
\end{array}
\right]
$$

---

## Slide 19

$\frac{1}{3}R_2\to R_2$
$$
\left[
\begin{array}{ccc|c}
1&-1&2&1\\
0&1&-\frac{7}{3}&\frac{2}{3}\\
0&0&0&0
\end{array}
\right]
$$

$R_1+R_2\to R_1$
$$
\left[
\begin{array}{ccc|c}
1&0&-\frac{1}{3}&\frac{5}{3}\\
0&1&-\frac{7}{3}&\frac{2}{3}\\
0&0&0&0
\end{array}
\right]
$$

---

## Slide 20
**Translate back (free variable)**
$$
\begin{cases}
x-\frac{1}{3}z=\frac{5}{3}\\
y-\frac{7}{3}z=\frac{2}{3}\\
0=0
\end{cases}
$$

Let $z=t$:
$$
\begin{cases}
x=\frac{5}{3}+\frac{1}{3}t\\
y=\frac{2}{3}+\frac{7}{3}t\\
z=t
\end{cases}
\qquad (t\in\mathbb{R})
$$

---

## Slide 21
**Pivot**  
The leading (leftmost) nonzero entry in a row is a **pivot**.

---

## Slide 22
**Row echelon form (REF)**  
A matrix is in REF if:
1. Each pivot is to the right of the pivot above it.
2. Any all-zero rows are at the bottom.
3. (Optional) pivots equal $1$.

---

## Slide 23
**Reduced row echelon form (RREF)**  
A matrix is in RREF if:
1. It is in REF.
2. All pivots equal $1$.
3. In each pivot column, all non-pivot entries are $0$ above and below.

---

## Slide 24
**How to solve a linear system**
1. Form $[A\mid B]$.
2. Compute $\operatorname{rref}([A\mid B])$.
3. Translate back to equations.
4. Describe the solution set.

---

## Slide 25
**Gaussian elimination**  
Use EROs to reach REF, then clear above pivots to reach RREF.

---

## Slide 26
**EROs (row operations)**
- Swap: $R_i\leftrightarrow R_j$
- Scale: $cR_i\to R_i$, $c\neq 0$
- Replace: $R_i+cR_j\to R_i$

---

## Slide 27
**Algorithm (step pattern)**  
Step 1:
- Make $a_{11}\neq 0$ (swap if needed)
- Scale row 1 so pivot becomes $1$
- Zero out entries below the pivot

Repeat on the lower-right submatrix.

---

## Slide 28
**REF template**
$$
\begin{bmatrix}
1&*&\cdots&*&\cdots&*\\
0&1&\cdots&*&\cdots&*\\
\vdots&\vdots&\ddots&\vdots& &\vdots\\
0&0&\cdots&1&\cdots&*\\
0&0&\cdots&0&\cdots&0\\
\vdots&\vdots& &\vdots& &\vdots\\
0&0&\cdots&0&\cdots&0
\end{bmatrix}
\qquad (*=\text{any number})
$$

Then clear above pivots to reach RREF.

---

## Slide 29
**Comments**
1. The RREF of a matrix is **unique**.
2. How you get there is **not**.
3. Practical.
