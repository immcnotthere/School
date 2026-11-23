---
type: reference
parent: "[[AM20]]"
domain: math
course: "AM 20"
status: draft
source: "AM20 Review3 Matrices"
tags:
  - decks
---
# AM 20 Cards - AM20 Review3 Matrices Matrix Arithmetic

## Matrix
| Front | Back | Notes |
| --- | --- | --- |
| What does it mean for a matrix to have size $m \times n$? | It has $m$ rows and $n$ columns | p.1; definition |
| In the entry $a_{ij}$ of a matrix, which index comes first, row or column? | The row index $i$ comes first, then the column $j$ | p.1; definition |

## Matrix Addition and Scalar Multiplication
| Front | Back | Notes |
| --- | --- | --- |
| How is $(A+B)_{ij}$ computed? | $a_{ij}+b_{ij}$, entry by entry | p.1; formula |
| What size requirement must $A$ and $B$ satisfy in order to add them? | They must be the same size | p.1; concept |
| How is $(cA)_{ij}$ computed? | $c\,a_{ij}$ | p.1; formula |

## Matrix-Vector Multiplication
| Front | Back | Notes |
| --- | --- | --- |
| What is entry $i$ of $A\mathbf{x}$? | $(A\mathbf{x})_i = a_{i1}x_1+a_{i2}x_2+\cdots+a_{in}x_n$, the dot product of row $i$ with $\mathbf{x}$ | p.1; formula |
| What is the column-combination reading of $A\mathbf{x}$? | $A\mathbf{x} = x_1(\text{column }1)+\cdots+x_n(\text{column }n)$ | p.1; formula |

## Matrix Multiplication
| Front | Back | Notes |
| --- | --- | --- |
| What is entry $(i,j)$ of $AB$? | The dot product of row $i$ of $A$ with column $j$ of $B$ | p.1; formula |
| When is the product $AB$ defined? | Only when the number of columns of $A$ equals the number of rows of $B$ | p.1; concept |
| In general, how does $AB$ compare to $BA$? | They are generally not equal: $AB \neq BA$ | p.1; discrimination |

## Identity Matrix
| Front | Back | Notes |
| --- | --- | --- |
| What does the identity matrix $I$ look like, and what does it satisfy? | Ones on the diagonal, zeros elsewhere; $AI=IA=A$ | p.1; definition |
| What does subtracting $rI$ from $A$ do? | Subtracts $r$ from each diagonal entry only, leaving off-diagonal entries unchanged | p.1; formula |
| For a $2\times 2$ matrix $\begin{pmatrix}a&b\\c&d\end{pmatrix}$, what is $\begin{pmatrix}a&b\\c&d\end{pmatrix} - rI$? | $\begin{pmatrix}a-r&b\\c&d-r\end{pmatrix}$ | p.1; formula |

## Transpose
| Front | Back | Notes |
| --- | --- | --- |
| What does the transpose $A^T$ do to a matrix? | Exchanges rows and columns, so $(A^T)_{ij}=a_{ji}$ | p.1; definition |

## Symmetric Matrix
| Front | Back | Notes |
| --- | --- | --- |
| What does it mean for a matrix $A$ to be symmetric? | $A = A^T$; it is unchanged when reflected across the diagonal | p.1; definition |
| To check whether a matrix is symmetric, which entries actually need comparing? | Only the off-diagonal entries: $a_{ij}$ must equal $a_{ji}$ | p.1; procedure |

## Transpose of a Product
| Front | Back | Notes |
| --- | --- | --- |
| How does transposing reverse the order of a product? State the identity. | $(AB)^T = B^T A^T$ | p.1; formula |

## Matrix Arithmetic Practice
| Front | Back | Notes |
| --- | --- | --- |
| For $A=\begin{pmatrix}1&2\\3&-1\end{pmatrix}$, $B=\begin{pmatrix}0&1\\2&3\end{pmatrix}$, what are $AB$ and $BA$? | $AB=\begin{pmatrix}4&7\\-2&0\end{pmatrix}$, $BA=\begin{pmatrix}3&-1\\11&1\end{pmatrix}$; they differ | p.1-2; procedure |

## Matrix Times Vector Two Ways
| Front | Back | Notes |
| --- | --- | --- |
| For $A=\begin{pmatrix}2&-1\\3&0\end{pmatrix}$, $x=[4,1]^T$, what is $Ax$? | $[7,12]^T$, whether computed row by row or as $4[2,3]^T+1[-1,0]^T$ | p.2; procedure |

## Computing A Minus rI at Given Values
| Front | Back | Notes |
| --- | --- | --- |
| For $A=\begin{pmatrix}3&1\\1&3\end{pmatrix}$, what is $A-2I$, and what does its structure indicate? | $\begin{pmatrix}1&1\\1&1\end{pmatrix}$, two identical rows, the sign that $r=2$ is an eigenvalue | p.2; procedure |

## Checking Whether Matrices Are Symmetric
| Front | Back | Notes |
| --- | --- | --- |
| Of $A=\begin{pmatrix}1&2\\2&5\end{pmatrix}$, $B=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$, $C=\begin{pmatrix}0&1&1\\1&0&1\\1&1&0\end{pmatrix}$, which are symmetric? | $A$ and $C$ are symmetric; $B$ is not since $b_{12}=1 \neq -1=b_{21}$, in fact $B^T=-B$ | p.2-3; procedure |

## Verifying the Transpose of a Product
| Front | Back | Notes |
| --- | --- | --- |
| For $A=\begin{pmatrix}1&2\\3&-1\end{pmatrix}$, $B=\begin{pmatrix}0&1\\2&3\end{pmatrix}$, does $(AB)^T$ match $B^TA^T$ or $A^TB^T$? | $(AB)^T=B^TA^T=\begin{pmatrix}4&-2\\7&0\end{pmatrix}$; multiplying in the original order, $A^TB^T$, gives a different result | p.3; procedure |

## linear dependence
| Front | Back | Notes |
| --- | --- | --- |
| What does $A\mathbf{x}=\mathbf{0}$ with $\mathbf{x}\neq\mathbf{0}$ tell you about the columns of $A$? | They are linearly dependent | p.1; concept |

# Node map
```json
[
 {
  "name": "Matrix",
  "type": "concept",
  "existing": false,
  "parent": "Matrix Arithmetic",
  "prereqs": [],
  "uses": [],
  "page": 1,
  "summary": "An $m \\times n$ matrix has $m$ rows and $n$ columns; entry $a_{ij}$ is in row $i$, column $j$, row index always first."
 },
 {
  "name": "Matrix Addition and Scalar Multiplication",
  "type": "concept",
  "existing": false,
  "parent": "Matrix Arithmetic",
  "prereqs": [
   "Matrix"
  ],
  "uses": [],
  "page": 1,
  "summary": "Matrix addition and scalar multiplication act entry by entry; addition requires both matrices to be the same size."
 },
 {
  "name": "Matrix-Vector Multiplication",
  "type": "concept",
  "existing": false,
  "parent": "Matrix Arithmetic",
  "prereqs": [
   "Matrix",
   "Dot Product"
  ],
  "uses": [],
  "page": 1,
  "summary": "$A\\mathbf{x}$ can be read entry by entry as dot products of rows with $\\mathbf{x}$, or as a linear combination of the columns of $A$ weighted by the entries of $\\mathbf{x}$."
 },
 {
  "name": "Matrix Multiplication",
  "type": "concept",
  "existing": false,
  "parent": "Matrix Arithmetic",
  "prereqs": [
   "Matrix",
   "Dot Product"
  ],
  "uses": [],
  "page": 1,
  "summary": "Entry $(i,j)$ of $AB$ is the dot product of row $i$ of $A$ with column $j$ of $B$; the product is defined only when columns of $A$ match rows of $B$, and in general $AB \\neq BA$."
 },
 {
  "name": "Identity Matrix",
  "type": "concept",
  "existing": false,
  "parent": "Matrix Arithmetic",
  "prereqs": [
   "Matrix"
  ],
  "uses": [],
  "page": 1,
  "summary": "The identity matrix $I$ has ones on the diagonal and zeros elsewhere with $AI=IA=A$; $A-rI$ subtracts $r$ from each diagonal entry only."
 },
 {
  "name": "Transpose",
  "type": "concept",
  "existing": true,
  "parent": "Matrix Arithmetic",
  "prereqs": [
   "Matrix"
  ],
  "uses": [],
  "page": 1,
  "summary": "The transpose $A^T$ exchanges rows and columns, so $(A^T)_{ij}=a_{ji}$."
 },
 {
  "name": "Symmetric Matrix",
  "type": "concept",
  "existing": false,
  "parent": "Matrix Arithmetic",
  "prereqs": [
   "Transpose"
  ],
  "uses": [],
  "page": 1,
  "summary": "A matrix is symmetric if $A=A^T$, meaning it is unchanged when reflected across the diagonal; only off-diagonal entries need checking."
 },
 {
  "name": "Transpose of a Product",
  "type": "concept",
  "existing": false,
  "parent": "Matrix Arithmetic",
  "prereqs": [
   "Transpose",
   "Matrix Multiplication"
  ],
  "uses": [],
  "page": 1,
  "summary": "Transposing a product reverses the order of the factors: $(AB)^T = B^T A^T$."
 },
 {
  "name": "Matrix Arithmetic Practice",
  "type": "problem",
  "existing": false,
  "parent": "Matrix Arithmetic",
  "prereqs": [],
  "uses": [
   "Matrix Addition and Scalar Multiplication",
   "Matrix Multiplication"
  ],
  "page": 1,
  "summary": "Computes $A+B$, $2A$, $AB$, and $BA$ for two $2\\times2$ matrices, showing $AB \\neq BA$."
 },
 {
  "name": "Matrix Times Vector Two Ways",
  "type": "problem",
  "existing": false,
  "parent": "Matrix Arithmetic",
  "prereqs": [],
  "uses": [
   "Matrix-Vector Multiplication"
  ],
  "page": 2,
  "summary": "Computes $Ax$ both row by row and as a combination of the columns of $A$."
 },
 {
  "name": "Computing A Minus rI at Given Values",
  "type": "problem",
  "existing": false,
  "parent": "Matrix Arithmetic",
  "prereqs": [],
  "uses": [
   "Identity Matrix"
  ],
  "page": 2,
  "summary": "Evaluates $A-rI$ at $r=2$ and $r=4$, noting the resulting proportional rows signal eigenvalues."
 },
 {
  "name": "Checking Whether Matrices Are Symmetric",
  "type": "problem",
  "existing": false,
  "parent": "Matrix Arithmetic",
  "prereqs": [],
  "uses": [
   "Symmetric Matrix"
  ],
  "page": 2,
  "summary": "Tests three matrices for symmetry by comparing off-diagonal entries."
 },
 {
  "name": "Verifying the Transpose of a Product",
  "type": "problem",
  "existing": false,
  "parent": "Matrix Arithmetic",
  "prereqs": [],
  "uses": [
   "Transpose",
   "Transpose of a Product",
   "Matrix Multiplication"
  ],
  "page": 3,
  "summary": "Confirms $(AB)^T=B^TA^T$ directly for the matrices of the arithmetic practice problem."
 },
 {
  "name": "linear dependence",
  "type": "concept",
  "existing": true,
  "parent": "",
  "prereqs": [],
  "summary": ""
 }
]
```

# Frankenstein problems

**Problem A.** Let $A=\begin{pmatrix}4&1\\1&4\end{pmatrix}$ and $B=\begin{pmatrix}0&2\\-2&0\end{pmatrix}$. (a) Determine whether $A$ and $B$ are symmetric. (b) Compute $AB$. (c) Verify that $(AB)^T = B^T A^T$.

*Concepts tested: Symmetric Matrix, Matrix Multiplication, Transpose, Transpose of a Product.*

Solution. (a) For $A$: $a_{12}=1=a_{21}$, so $A$ is symmetric. For $B$: $b_{12}=2 \neq -2 = b_{21}$, so $B$ is not symmetric (indeed $B^T=-B$). (b) $AB = \begin{pmatrix}4(0)+1(-2) & 4(2)+1(0)\\1(0)+4(-2) & 1(2)+4(0)\end{pmatrix} = \begin{pmatrix}-2&8\\-8&2\end{pmatrix}$. (c) $(AB)^T = \begin{pmatrix}-2&-8\\8&2\end{pmatrix}$. Since $A$ is symmetric, $A^T=A$, and $B^T=\begin{pmatrix}0&-2\\2&0\end{pmatrix}$, so $B^TA^T = \begin{pmatrix}0(4)+(-2)(1) & 0(1)+(-2)(4)\\2(4)+0(1) & 2(1)+0(4)\end{pmatrix} = \begin{pmatrix}-2&-8\\8&2\end{pmatrix}$, which matches $(AB)^T$.

**Problem B.** Let $A=\begin{pmatrix}2&1\\0&3\end{pmatrix}$ and $x=[1,-2]^T$. Compute $(A-2I)x$ two ways: (i) form $A-2I$ first and multiply, and (ii) compute $Ax - 2x$. Confirm the two ways agree.

*Concepts tested: Identity Matrix, Matrix-Vector Multiplication, Matrix Addition and Scalar Multiplication.*

Solution. (i) $A - 2I = \begin{pmatrix}0&1\\0&1\end{pmatrix}$, so $(A-2I)x = \begin{pmatrix}0(1)+1(-2)\\0(1)+1(-2)\end{pmatrix} = [-2,-2]^T$. (ii) $Ax = \begin{pmatrix}2(1)+1(-2)\\0(1)+3(-2)\end{pmatrix} = [0,-6]^T$, and $2x = [2,-4]^T$, so $Ax - 2x = [0-2,\, -6-(-4)]^T = [-2,-2]^T$. Both methods give $[-2,-2]^T$.
