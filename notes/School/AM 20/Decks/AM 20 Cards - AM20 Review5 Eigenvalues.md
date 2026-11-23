---
type: reference
parent: "[[AM20]]"
domain: math
course: "AM 20"
status: draft
source: "AM20 Review5 Eigenvalues"
tags:
  - decks
---
# AM 20 Cards - AM20 Review5 Eigenvalues Eigenvalues and Eigenvectors

## Eigenvalue and Eigenvector Definition
| Front | Back | Notes |
| --- | --- | --- |
| Definition of an eigenvalue $r$ and eigenvector $\xi$ of a square matrix $A$ | A number $r$ is an eigenvalue of square matrix $A$ with eigenvector $\xi \neq 0$ if $A\xi = r\xi$ | p.1; definition |
| What does multiplying an eigenvector $\xi$ by $A$ do geometrically | It stretches $\xi$ by the factor $r$ without turning it, that is, without changing its direction | p.1; definition |

## Characteristic Equation
| Front | Back | Notes |
| --- | --- | --- |
| How do you rewrite $A\xi = r\xi$ as a step toward finding eigenvalues | $(A - rI)\xi = 0$ | p.1; formula |
| Why must $\det(A - rI) = 0$ for an eigenvalue $r$ | A nonzero $\xi$ exists exactly when $A - rI$ is singular, so $\det(A - rI) = 0$; this is the characteristic equation | p.1; formula |
| For an $n$ by $n$ matrix, what degree is the characteristic equation | A polynomial equation of degree $n$ in $r$ | p.1; definition |

## Trace and Determinant Shortcut for Two by Two Matrices
| Front | Back | Notes |
| --- | --- | --- |
| Characteristic equation shortcut for a two by two matrix $A$, using $\text{tr}\,A$ and $\det A$ | $r^2 - (\text{tr}\,A)r + \det A = 0$ | p.1; formula |
| For the two eigenvalues $r_1, r_2$ of a two by two matrix, what do they satisfy | $r_1 + r_2 = \text{tr}\,A$ and $r_1 r_2 = \det A$; a quick check on any answer | p.1; formula |

## Finding Eigenvectors Procedure
| Front | Back | Notes |
| --- | --- | --- |
| Procedure to find the eigenvector for a known eigenvalue $r$ | Substitute $r$ into $(A - rI)\xi = 0$ and solve; the rows will be proportional, confirming $r$ is correct, and collapse to fewer equations than unknowns, so one component may be chosen freely | p.1; procedure |
| Is an eigenvector for a given eigenvalue unique | No, any nonzero multiple of an eigenvector is again an eigenvector for the same eigenvalue; only the direction matters | p.1; definition |

## Three Cases for Eigenvalues and Eigenvectors
| Front | Back | Notes |
| --- | --- | --- |
| Eigenvectors when a matrix has distinct real eigenvalues | Each distinct real eigenvalue gives one independent eigenvector | p.1; discrimination |
| Eigenvalues and eigenvectors of a real matrix when the eigenvalues are complex | Complex eigenvalues come in conjugate pairs $\alpha \pm i\beta$ with conjugate eigenvectors; only one of the pair needs to be computed | p.1; discrimination |
| What can happen with a repeated eigenvalue | It may supply as many independent eigenvectors as its multiplicity, or fewer; when it supplies fewer, a generalized eigenvector is needed | p.1; discrimination |

## Triangular Matrix Eigenvalues
| Front | Back | Notes |
| --- | --- | --- |
| Eigenvalues of a triangular matrix, that is, one with all entries above or all entries below the diagonal equal to zero | The eigenvalues are the diagonal entries | p.1; formula |

## Symmetric Matrix Eigenvalues
| Front | Back | Notes |
| --- | --- | --- |
| Eigenvalue properties of a real symmetric matrix | Real eigenvalues, and it always supplies a full set of independent eigenvectors even when an eigenvalue repeats | p.1; definition |

## Eigenvector Verification for a Two by Two Matrix
| Front | Back | Notes |
| --- | --- | --- |
| Show $[1,2]^T$ is an eigenvector of $A = \begin{bmatrix}1 & 1 \\ 4 & 1\end{bmatrix}$ and find its eigenvalue: key move | Compute $A[1,2]^T = [3,6]^T = 3[1,2]^T$, so $[1,2]^T$ is an eigenvector with eigenvalue $r = 3$ | p.1; problem |

## Eigenvalues of a Two by Two Matrix with Distinct Real Roots
| Front | Back | Notes |
| --- | --- | --- |
| Eigenvalues and eigenvectors of $A = \begin{bmatrix}4 & -2 \\ 1 & 1\end{bmatrix}$: key move | $\text{tr}\,A = 5$, $\det A = 6$ give $r^2 - 5r + 6 = (r-2)(r-3) = 0$, so $r = 2, 3$; solving $(A-rI)\xi = 0$ gives $\xi^{(1)} = [1,1]^T$ for $r=2$ and $\xi^{(2)} = [2,1]^T$ for $r=3$ | p.2; problem |

## Eigenvalues of a Two by Two Matrix with Complex Roots
| Front | Back | Notes |
| --- | --- | --- |
| Eigenvalues and eigenvector of $A = \begin{bmatrix}1 & -2 \\ 2 & 1\end{bmatrix}$: key move | $\text{tr}\,A = 2$, $\det A = 5$ give $r^2 - 2r + 5 = 0$ with discriminant $-16$, so $r = 1 \pm 2i$; for $r = 1+2i$, solving gives $\xi = [1,-i]^T$ | p.2-3; problem |

## Repeated Eigenvalue Comparison for Two Matrices
| Front | Back | Notes |
| --- | --- | --- |
| Eigenvectors of $A = \begin{bmatrix}2 & 1 \\ 0 & 2\end{bmatrix}$ versus $B = \begin{bmatrix}5 & 0 \\ 0 & 5\end{bmatrix}$, both with a repeated eigenvalue: key move | Both are triangular; $A$ has repeated eigenvalue $r=2$ but $A-2I$ has rank 1, giving only one independent eigenvector $[1,0]^T$ (defective); $B$ has repeated eigenvalue $r=5$, but $B-5I=0$, so every nonzero vector is an eigenvector, giving two independent eigenvectors $[1,0]^T$ and $[0,1]^T$ | p.3; problem |

## Eigenvalues of a Triangular Three by Three Matrix
| Front | Back | Notes |
| --- | --- | --- |
| Eigenvalues of $A = \begin{bmatrix}2 & 0 & 0 \\ 1 & 3 & 0 \\ 0 & 1 & 4\end{bmatrix}$ and the eigenvector for the smallest eigenvalue: key move | Triangular, so $r = 2, 3, 4$; for $r=2$, solving $(A-2I)\xi = 0$ gives $\xi = [2,-2,1]^T$ | p.4; problem |

## Eigenvalue Check for a Symmetric Matrix
| Front | Back | Notes |
| --- | --- | --- |
| Eigenvalues and eigenvectors of symmetric $A = \begin{bmatrix}3 & 1 \\ 1 & 3\end{bmatrix}$, verifying orthogonality: key move | $\text{tr}\,A = 6$, $\det A = 8$ give $r^2 - 6r + 8 = (r-2)(r-4) = 0$; eigenvectors $\xi^{(1)} = [1,-1]^T$ for $r=2$ and $\xi^{(2)} = [1,1]^T$ for $r=4$; their dot product is $0$, confirming orthogonality | p.4-5; problem |

# Node map

```json
[
 {
  "name": "Eigenvalue and Eigenvector Definition",
  "type": "concept",
  "existing": false,
  "parent": "Eigenvalues and Eigenvectors",
  "prereqs": [],
  "uses": [],
  "page": 1,
  "summary": "A number $r$ is an eigenvalue of square matrix $A$ with eigenvector $\\xi \\neq 0$ if $A\\xi = r\\xi$; multiplying $\\xi$ by $A$ only stretches it by $r$."
 },
 {
  "name": "Characteristic Equation",
  "type": "concept",
  "existing": true,
  "parent": "Eigenvalues and Eigenvectors",
  "prereqs": [
   "Determinant",
   "Eigenvalue and Eigenvector Definition"
  ],
  "uses": [],
  "page": 1,
  "summary": "Eigenvalues satisfy $\\det(A-rI)=0$, a degree $n$ polynomial equation, since a nonzero eigenvector exists exactly when $A-rI$ is singular."
 },
 {
  "name": "Trace and Determinant Shortcut for Two by Two Matrices",
  "type": "concept",
  "existing": false,
  "parent": "Eigenvalues and Eigenvectors",
  "prereqs": [
   "Characteristic Equation",
   "Determinant"
  ],
  "uses": [],
  "page": 1,
  "summary": "For a two by two matrix, $r^2-(\\text{tr}\\,A)r+\\det A=0$, so the two eigenvalues sum to $\\text{tr}\\,A$ and multiply to $\\det A$."
 },
 {
  "name": "Finding Eigenvectors Procedure",
  "type": "concept",
  "existing": false,
  "parent": "Eigenvalues and Eigenvectors",
  "prereqs": [
   "Characteristic Equation"
  ],
  "uses": [],
  "page": 1,
  "summary": "Substitute each eigenvalue into $(A-rI)\\xi=0$ and solve; the rows are proportional, so one component may be chosen freely, and any nonzero multiple of the result is also valid."
 },
 {
  "name": "Three Cases for Eigenvalues and Eigenvectors",
  "type": "concept",
  "existing": false,
  "parent": "Eigenvalues and Eigenvectors",
  "prereqs": [
   "Characteristic Equation",
   "Finding Eigenvectors Procedure"
  ],
  "uses": [],
  "page": 1,
  "summary": "Distinct real eigenvalues each give one independent eigenvector; complex eigenvalues come in conjugate pairs; a repeated eigenvalue may give fewer independent eigenvectors than its multiplicity, requiring a generalized eigenvector."
 },
 {
  "name": "Triangular Matrix Eigenvalues",
  "type": "concept",
  "existing": false,
  "parent": "Eigenvalues and Eigenvectors",
  "prereqs": [],
  "uses": [],
  "page": 1,
  "summary": "If a matrix is triangular, all entries above or all below the diagonal are zero, so its eigenvalues are simply its diagonal entries."
 },
 {
  "name": "Symmetric Matrix Eigenvalues",
  "type": "concept",
  "existing": false,
  "parent": "Eigenvalues and Eigenvectors",
  "prereqs": [
   "Characteristic Equation"
  ],
  "uses": [],
  "page": 1,
  "summary": "A real symmetric matrix has real eigenvalues and always a full set of independent eigenvectors; eigenvectors for distinct eigenvalues are orthogonal."
 },
 {
  "name": "Eigenvector Verification for a Two by Two Matrix",
  "type": "problem",
  "existing": false,
  "parent": "Eigenvalues and Eigenvectors",
  "prereqs": [
   "Eigenvalue and Eigenvector Definition"
  ],
  "uses": [
   "Eigenvalue and Eigenvector Definition"
  ],
  "page": 1,
  "summary": "Verifies $[1,2]^T$ is an eigenvector of $\\begin{bmatrix}1&1\\\\4&1\\end{bmatrix}$ with eigenvalue $3$ by direct multiplication."
 },
 {
  "name": "Eigenvalues of a Two by Two Matrix with Distinct Real Roots",
  "type": "problem",
  "existing": false,
  "parent": "Eigenvalues and Eigenvectors",
  "prereqs": [
   "Characteristic Equation",
   "Trace and Determinant Shortcut for Two by Two Matrices",
   "Finding Eigenvectors Procedure"
  ],
  "uses": [
   "Characteristic Equation",
   "Trace and Determinant Shortcut for Two by Two Matrices",
   "Finding Eigenvectors Procedure"
  ],
  "page": 2,
  "summary": "Finds eigenvalues $2,3$ and their eigenvectors for $\\begin{bmatrix}4&-2\\\\1&1\\end{bmatrix}$ using the trace and determinant shortcut."
 },
 {
  "name": "Eigenvalues of a Two by Two Matrix with Complex Roots",
  "type": "problem",
  "existing": false,
  "parent": "Eigenvalues and Eigenvectors",
  "prereqs": [
   "Characteristic Equation",
   "Three Cases for Eigenvalues and Eigenvectors"
  ],
  "uses": [
   "Characteristic Equation",
   "Three Cases for Eigenvalues and Eigenvectors"
  ],
  "page": 2,
  "summary": "Finds complex eigenvalues $1\\pm 2i$ and one eigenvector for $\\begin{bmatrix}1&-2\\\\2&1\\end{bmatrix}$."
 },
 {
  "name": "Repeated Eigenvalue Comparison for Two Matrices",
  "type": "problem",
  "existing": false,
  "parent": "Eigenvalues and Eigenvectors",
  "prereqs": [
   "Three Cases for Eigenvalues and Eigenvectors",
   "Triangular Matrix Eigenvalues"
  ],
  "uses": [
   "Three Cases for Eigenvalues and Eigenvectors",
   "Triangular Matrix Eigenvalues"
  ],
  "page": 3,
  "summary": "Compares two triangular matrices with the same repeated eigenvalue, one defective (one eigenvector) and one not (two eigenvectors)."
 },
 {
  "name": "Eigenvalues of a Triangular Three by Three Matrix",
  "type": "problem",
  "existing": false,
  "parent": "Eigenvalues and Eigenvectors",
  "prereqs": [
   "Triangular Matrix Eigenvalues",
   "Finding Eigenvectors Procedure"
  ],
  "uses": [
   "Triangular Matrix Eigenvalues",
   "Finding Eigenvectors Procedure"
  ],
  "page": 4,
  "summary": "Reads off eigenvalues $2,3,4$ from a triangular three by three matrix and finds the eigenvector for the smallest one."
 },
 {
  "name": "Eigenvalue Check for a Symmetric Matrix",
  "type": "problem",
  "existing": false,
  "parent": "Eigenvalues and Eigenvectors",
  "prereqs": [
   "Symmetric Matrix Eigenvalues",
   "Characteristic Equation",
   "Finding Eigenvectors Procedure"
  ],
  "uses": [
   "Symmetric Matrix Eigenvalues",
   "Characteristic Equation",
   "Finding Eigenvectors Procedure"
  ],
  "page": 4,
  "summary": "Finds eigenvalues $2,4$ of a symmetric matrix and verifies their eigenvectors are orthogonal."
 }
]
```

# Frankenstein problems

**Problem 1.** Find the eigenvalues and eigenvectors of $A = \begin{bmatrix}0 & -1 \\ 1 & 0\end{bmatrix}$, verify the answer with the trace and determinant check, and state which of the three eigenvalue cases applies.

*Concepts tested:* Characteristic Equation, Trace and Determinant Shortcut for Two by Two Matrices, Finding Eigenvectors Procedure, Three Cases for Eigenvalues and Eigenvectors.

*Solution.*

Trace and determinant: $\text{tr}\,A = 0 + 0 = 0$, $\det A = (0)(0) - (-1)(1) = 1$.

Characteristic equation (shortcut): $r^2 - (0)r + 1 = 0$, so $r^2 = -1$ and $r = \pm i$. This is the complex-conjugate-pair case.

Eigenvector for $r = i$: solve $(A - iI)\xi = 0$, that is $\begin{bmatrix}-i & -1 \\ 1 & -i\end{bmatrix}\xi = 0$. The first row gives $-i\xi_1 - \xi_2 = 0 \implies \xi_2 = -i\xi_1$. Setting $\xi_1 = 1$: $\xi = [1, -i]^T$.

Check by direct multiplication: $A[1,-i]^T = [(0)(1)+(-1)(-i),\ (1)(1)+(0)(-i)]^T = [i, 1]^T$, and $i[1,-i]^T = [i, -i^2]^T = [i, 1]^T$. These agree.

Check with the trace/determinant relation: $r_1 + r_2 = i + (-i) = 0 = \text{tr}\,A$, and $r_1 r_2 = (i)(-i) = -i^2 = 1 = \det A$. Both match.

**Problem 2.** A matrix $A$ is triangular with diagonal entries $2, 2, 5$ and is symmetric. Without further computation, state its eigenvalues, whether it is guaranteed to have a full set of independent eigenvectors, and what relation would hold between any two eigenvectors for eigenvalues $2$ and $5$.

*Concepts tested:* Triangular Matrix Eigenvalues, Symmetric Matrix Eigenvalues, Three Cases for Eigenvalues and Eigenvectors.

*Solution.*

Since the matrix is triangular, its eigenvalues are its diagonal entries: $r = 2, 2, 5$, so $r=2$ is a repeated eigenvalue (multiplicity 2) and $r=5$ is a simple eigenvalue.

Since the matrix is also symmetric, it is guaranteed to have real eigenvalues (already seen, since $2$ and $5$ are real) and a full set of independent eigenvectors even though $r=2$ repeats; this rules out the "fewer eigenvectors than multiplicity" outcome from the repeated-eigenvalue case, so two independent eigenvectors exist for $r=2$.

Because $A$ is symmetric, an eigenvector for $r=2$ and an eigenvector for $r=5$ (distinct eigenvalues) must be orthogonal, that is, their dot product is $0$.
