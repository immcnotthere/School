---
type: reference
parent: "[[AM20]]"
domain: math
course: "AM 20"
status: draft
source: "AM20 Review4 Linear Systems"
tags:
  - decks
---
# AM 20 Cards - AM20 Review4 Linear Systems Linear Systems and Determinants

## Determinant
| Front | Back | Notes |
| --- | --- | --- |
| What is the formula for the determinant of $\begin{pmatrix}a&b\\c&d\end{pmatrix}$? | $ad-bc$ | p.1; formula |
| What does it mean, in terms of the determinant, for a square matrix to be invertible? | Its determinant is nonzero | p.1; concept |

## Cofactor Expansion of a Determinant
| Front | Back | Notes |
| --- | --- | --- |
| How do you compute a $3\times 3$ determinant by cofactor expansion along the first row, for rows $(a,b,c)$, $(d,e,f)$, $(g,h,k)$? | $a\det\begin{pmatrix}e&f\\h&k\end{pmatrix} - b\det\begin{pmatrix}d&f\\g&k\end{pmatrix} + c\det\begin{pmatrix}d&e\\g&h\end{pmatrix}$ | p.1; formula |
| What is the checkerboard sign pattern used in cofactor expansion of a $3\times 3$ matrix? | $\begin{pmatrix}+&-&+\\-&+&-\\+&-&+\end{pmatrix}$ | p.1; formula |
| When expanding a determinant, which row or column should you choose, and why? | The one with the most zeros, since each zero kills a term | p.1; procedure |

## Determinant of a Triangular Matrix
| Front | Back | Notes |
| --- | --- | --- |
| What is the determinant of a triangular matrix, one with all zeros above or all zeros below the diagonal? | The product of the diagonal entries | p.1; formula |

## Inverse of a 2x2 Matrix
| Front | Back | Notes |
| --- | --- | --- |
| What is the formula for the inverse of $\begin{pmatrix}a&b\\c&d\end{pmatrix}$ when $ad-bc\neq 0$? | $\dfrac{1}{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$ | p.1; formula |

## Elimination Method for Linear Systems
| Front | Back | Notes |
| --- | --- | --- |
| What is the elimination method for solving a linear system? | Add multiples of one equation to another until only one unknown is left | p.1; procedure |

## Solving a Linear System via Matrix Inverse
| Front | Back | Notes |
| --- | --- | --- |
| For a $2\times 2$ system $Ax=b$, how does the inverse give the solution directly? | $x = A^{-1}b$ | p.1; formula |

## Singular Matrix Equivalences
| Front | Back | Notes |
| --- | --- | --- |
| Name the four equivalent conditions for a square matrix $A$ to be singular. | $\det A=0$; $A^{-1}$ does not exist; $Ax=0$ has a nonzero solution; the columns of $A$ are linearly dependent | p.1; theorem |
| Which singular-matrix equivalence does the eigenvalue problem rely on? | That $(A-rI)\xi=0$ has a nonzero solution $\xi$ exactly when $\det(A-rI)=0$ | p.1; concept |

## Determinant and Invertibility Practice
| Front | Back | Notes |
| --- | --- | --- |
| For $A=\begin{pmatrix}3&1\\1&3\end{pmatrix}$ and $B=\begin{pmatrix}1&2\\2&4\end{pmatrix}$, compute each determinant and state invertibility. | $\det A = 8 \neq 0$, invertible; $\det B = 0$, not invertible since column 2 is twice column 1 | p.1; procedure |

## Cofactor Expansion Practice
| Front | Back | Notes |
| --- | --- | --- |
| Compute $\det\begin{pmatrix}1&2&0\\0&3&0\\2&-4&2\end{pmatrix}$. | Expand along the third column, one nonzero entry: $+2\det\begin{pmatrix}1&2\\0&3\end{pmatrix} = 2(3)=6$ | p.2; procedure |

## Solving a 2 by 2 System by Substitution
| Front | Back | Notes |
| --- | --- | --- |
| Solve $2x+3y=7$, $x-y=1$. | From the second equation $x=y+1$; substituting gives $y=1$, then $x=2$ | p.2; procedure |

## Solving a System Using the Matrix Inverse
| Front | Back | Notes |
| --- | --- | --- |
| For $A=\begin{pmatrix}1&1\\3&1\end{pmatrix}$, find $A^{-1}$ and use it to solve $Ax=[5,7]^T$. | $\det A=-2$, so $A^{-1}=\dfrac{1}{2}\begin{pmatrix}-1&1\\3&-1\end{pmatrix}$, giving $x=[1,4]^T$ | p.2-3; procedure |

## Finding a Value That Makes a Matrix Singular
| Front | Back | Notes |
| --- | --- | --- |
| For $A=\begin{pmatrix}2&k\\3&6\end{pmatrix}$, find $k$ making $A$ singular, and a nonzero solution of $Ax=0$. | $12-3k=0 \Rightarrow k=4$; then $2x_1+4x_2=0$, so $x=[-2,1]^T$ works | p.3; procedure |

## Solving a 3 by 3 Linear System by Elimination
| Front | Back | Notes |
| --- | --- | --- |
| Solve $c_1+c_2+c_3=1$, $c_1-c_2+c_3=3$, $c_1+2c_2-c_3=0$. | Subtracting equations 1 and 2 gives $c_2=-1$; solving the rest gives $c_1=2$, $c_3=0$ | p.3-4; procedure |

# Node map
```json
[
 {
  "name": "Determinant",
  "type": "concept",
  "existing": true,
  "parent": "Linear Systems and Determinants",
  "prereqs": [],
  "uses": [],
  "page": 1,
  "summary": "For a $2\\times2$ matrix, $\\det\\begin{pmatrix}a&b\\\\c&d\\end{pmatrix}=ad-bc$; a matrix is invertible exactly when its determinant is nonzero."
 },
 {
  "name": "Cofactor Expansion of a Determinant",
  "type": "concept",
  "existing": false,
  "parent": "Linear Systems and Determinants",
  "prereqs": [
   "Determinant"
  ],
  "uses": [],
  "page": 1,
  "summary": "A $3\\times3$ determinant expands along any row or column using minors and a checkerboard sign pattern; choose the row or column with the most zeros."
 },
 {
  "name": "Determinant of a Triangular Matrix",
  "type": "concept",
  "existing": false,
  "parent": "Linear Systems and Determinants",
  "prereqs": [
   "Determinant"
  ],
  "uses": [],
  "page": 1,
  "summary": "If a matrix is triangular, its determinant is simply the product of the diagonal entries."
 },
 {
  "name": "Inverse of a 2x2 Matrix",
  "type": "concept",
  "existing": false,
  "parent": "Linear Systems and Determinants",
  "prereqs": [
   "Determinant"
  ],
  "uses": [],
  "page": 1,
  "summary": "When $ad-bc\\neq0$, the inverse of $\\begin{pmatrix}a&b\\\\c&d\\end{pmatrix}$ swaps the diagonal entries, negates the off-diagonal entries, and divides by the determinant."
 },
 {
  "name": "Elimination Method for Linear Systems",
  "type": "concept",
  "existing": false,
  "parent": "Linear Systems and Determinants",
  "prereqs": [
   "System of equations"
  ],
  "uses": [],
  "page": 1,
  "summary": "Elimination solves a linear system by adding multiples of one equation to another until only one unknown remains."
 },
 {
  "name": "Solving a Linear System via Matrix Inverse",
  "type": "concept",
  "existing": false,
  "parent": "Linear Systems and Determinants",
  "prereqs": [
   "Inverse of a 2x2 Matrix"
  ],
  "uses": [],
  "page": 1,
  "summary": "For a $2\\times2$ system $Ax=b$, the inverse gives the solution directly as $x=A^{-1}b$."
 },
 {
  "name": "Singular Matrix Equivalences",
  "type": "concept",
  "existing": false,
  "parent": "Linear Systems and Determinants",
  "prereqs": [
   "Determinant",
   "Invertibility"
  ],
  "uses": [],
  "page": 1,
  "summary": "For a square matrix, zero determinant, nonexistent inverse, a nonzero solution to $Ax=0$, and linearly dependent columns are all equivalent; this is the basis of the eigenvalue equation $\\det(A-rI)=0$."
 },
 {
  "name": "Determinant and Invertibility Practice",
  "type": "problem",
  "existing": false,
  "parent": "Linear Systems and Determinants",
  "prereqs": [],
  "uses": [
   "Determinant",
   "Singular Matrix Equivalences"
  ],
  "page": 1,
  "summary": "Computes two $2\\times2$ determinants and determines invertibility from each."
 },
 {
  "name": "Cofactor Expansion Practice",
  "type": "problem",
  "existing": false,
  "parent": "Linear Systems and Determinants",
  "prereqs": [],
  "uses": [
   "Cofactor Expansion of a Determinant"
  ],
  "page": 2,
  "summary": "Computes a $3\\times3$ determinant by expanding along the column with the most zeros."
 },
 {
  "name": "Solving a 2 by 2 System by Substitution",
  "type": "problem",
  "existing": false,
  "parent": "Linear Systems and Determinants",
  "prereqs": [],
  "uses": [
   "Elimination Method for Linear Systems"
  ],
  "page": 2,
  "summary": "Solves a two-equation linear system by solving one equation for a variable and substituting."
 },
 {
  "name": "Solving a System Using the Matrix Inverse",
  "type": "problem",
  "existing": false,
  "parent": "Linear Systems and Determinants",
  "prereqs": [],
  "uses": [
   "Inverse of a 2x2 Matrix",
   "Solving a Linear System via Matrix Inverse"
  ],
  "page": 2,
  "summary": "Finds the inverse of a $2\\times2$ matrix and uses it to solve $Ax=b$ directly."
 },
 {
  "name": "Finding a Value That Makes a Matrix Singular",
  "type": "problem",
  "existing": false,
  "parent": "Linear Systems and Determinants",
  "prereqs": [],
  "uses": [
   "Determinant",
   "Singular Matrix Equivalences"
  ],
  "page": 3,
  "summary": "Solves for the parameter $k$ that makes a matrix singular, then finds a nonzero solution of $Ax=0$."
 },
 {
  "name": "Solving a 3 by 3 Linear System by Elimination",
  "type": "problem",
  "existing": false,
  "parent": "Linear Systems and Determinants",
  "prereqs": [],
  "uses": [
   "Elimination Method for Linear Systems"
  ],
  "page": 3,
  "summary": "Solves a three-equation, three-unknown system by combining equations to eliminate variables two at a time."
 }
]
```

# Frankenstein problems

**Problem A.** Let $A = \begin{pmatrix}2 & k \\ 4 & 8\end{pmatrix}$. (a) Find the value of $k$ that makes $A$ singular, and give a nonzero solution of $Ax=0$ for that $k$. (b) For $k=1$ instead, find $A^{-1}$ and use it to solve $Ax = [3, 10]^T$.

*Concepts tested: Determinant, Singular Matrix Equivalences, Inverse of a 2x2 Matrix, Solving a Linear System via Matrix Inverse.*

Solution. (a) $\det A = (2)(8) - k(4) = 16 - 4k = 0 \Rightarrow k=4$. With $k=4$, $A=\begin{pmatrix}2&4\\4&8\end{pmatrix}$, and $Ax=0$ becomes $2x_1+4x_2=0$, so $x_1=-2x_2$; taking $x_2=1$ gives $x=[-2,1]^T$, a nonzero solution, confirming the matrix is singular. (b) With $k=1$, $A=\begin{pmatrix}2&1\\4&8\end{pmatrix}$, $\det A = 16-4=12$, so $A^{-1}=\dfrac{1}{12}\begin{pmatrix}8&-1\\-4&2\end{pmatrix}$. Then $x = \dfrac{1}{12}\begin{pmatrix}8&-1\\-4&2\end{pmatrix}\begin{pmatrix}3\\10\end{pmatrix} = \dfrac{1}{12}\begin{pmatrix}24-10\\-12+20\end{pmatrix} = \dfrac{1}{12}\begin{pmatrix}14\\8\end{pmatrix} = \begin{pmatrix}7/6\\2/3\end{pmatrix}$. Check: $2(7/6)+1(2/3)=7/3+2/3=3$ and $4(7/6)+8(2/3)=14/3+16/3=10$, both correct.

**Problem B.** Let $M = \begin{pmatrix}2&0&0\\5&3&0\\1&4&6\end{pmatrix}$. (a) Compute $\det M$ using the triangular matrix rule. (b) Verify the same value using cofactor expansion along the first row. (c) State whether $Mx=0$ has a nonzero solution.

*Concepts tested: Determinant of a Triangular Matrix, Cofactor Expansion of a Determinant, Singular Matrix Equivalences.*

Solution. (a) $M$ is lower triangular (all entries above the diagonal are zero), so $\det M$ is the product of the diagonal entries: $2 \cdot 3 \cdot 6 = 36$. (b) Expanding along the first row, $(2,0,0)$: $\det M = 2\det\begin{pmatrix}3&0\\4&6\end{pmatrix} - 0 + 0 = 2(3\cdot6 - 0\cdot4) = 2(18) = 36$, matching part (a). (c) Since $\det M = 36 \neq 0$, $M$ is not singular, so $Mx=0$ has only the trivial solution $x=0$, no nonzero solution exists.
