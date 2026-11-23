---
type: reference
parent: "[[AM20]]"
domain: math
course: "AM 20"
status: draft
source: "AM20 Review2 Vectors"
tags:
  - decks
---
# AM 20 Cards - AM20 Review2 Vectors Vectors, Dot Products, and Norms

## Vectors
| Front | Back | Notes |
| --- | --- | --- |
| What is a vector in $\mathbb{R}^n$? | A column of $n$ real numbers, $\mathbf{x}=[x_1,\ldots,x_n]^T$ | p.1; definition |
| What does the superscript $T$ mean when a vector is written as a row, like $[x_1,\ldots,x_n]^T$? | Transpose: the row has been stood on end to become a column | p.1; definition |

## Vector Addition
| Front | Back | Notes |
| --- | --- | --- |
| How do you add two vectors $\mathbf{x}+\mathbf{y}$? | Add corresponding components: $(x_1+y_1, \ldots, x_n+y_n)$ | p.1; formula |

## Scalar multiplication (linear algebra)
| Front | Back | Notes |
| --- | --- | --- |
| How do you compute $c\mathbf{x}$ for a scalar $c$? | Multiply every component by $c$: $(cx_1,\ldots,cx_n)$ | p.1; formula |

## Dot Product
| Front | Back | Notes |
| --- | --- | --- |
| What is the formula for the dot product $\mathbf{x}\cdot\mathbf{y}$? | $x_1y_1+x_2y_2+\cdots+x_ny_n$, a single number | p.1; formula |
| What symmetry property does the dot product have? | $\mathbf{x}\cdot\mathbf{y}=\mathbf{y}\cdot\mathbf{x}$ | p.1; formula |
| The dot product of two vectors produces what kind of object? | A single real number (scalar), not a vector | p.1; discrimination |

## Euclidean Norm
| Front | Back | Notes |
| --- | --- | --- |
| What is the formula for the Euclidean norm $\lVert \mathbf{x} \rVert$? | $\lVert \mathbf{x} \rVert = \sqrt{\mathbf{x}\cdot\mathbf{x}} = \sqrt{x_1^2+\cdots+x_n^2}$ | p.1; formula |
| In $\mathbb{R}^2$, the Euclidean norm formula restates which classical theorem? | The Pythagorean theorem | p.1; concept |
| How do you turn any nonzero vector $\mathbf{x}$ into a unit vector pointing the same way? | Divide it by its norm: $\mathbf{x}/\lVert \mathbf{x} \rVert$ | p.1; procedure |

## Unit Vector
| Front | Back | Notes |
| --- | --- | --- |
| What defines a unit vector? | A vector with norm equal to $1$ | p.1; definition |

## Orthogonality (Vectors)
| Front | Back | Notes |
| --- | --- | --- |
| When are two vectors exactly perpendicular, that is orthogonal? | When their dot product is zero: $\mathbf{x}\cdot\mathbf{y}=0$ | p.1; formula |
| Where does vector orthogonality come up with eigenvectors? | The eigenvectors of a real symmetric matrix turn out to be orthogonal | p.1; concept |

## Amplitude-Phase Form of a Sinusoid
| Front | Back | Notes |
| --- | --- | --- |
| How do you rewrite $c_1\cos\theta + c_2\sin\theta$ as a single shifted cosine? | $R\cos(\theta-\delta)$ with $R=\sqrt{c_1^2+c_2^2}$ and $\tan\delta = c_2/c_1$ | p.1; formula |
| The amplitude $R$ of a combined sine and cosine oscillation equals the norm of which vector? | $[c_1,c_2]^T$ | p.1; concept |

## Vector Arithmetic Practice
| Front | Back | Notes |
| --- | --- | --- |
| For $\mathbf{x}=[1,-2,3]^T$, $\mathbf{y}=[4,0,-1]^T$, what is $\mathbf{x}\cdot\mathbf{y}$ and $\lVert \mathbf{x} \rVert$? | $\mathbf{x}\cdot\mathbf{y}=4+0-3=1$; $\lVert \mathbf{x} \rVert = \sqrt{1+4+9}=\sqrt{14}$ | p.2; procedure |

## Testing Orthogonality of Vector Pairs
| Front | Back | Notes |
| --- | --- | --- |
| Compute the dot product of $[2,3]^T$ and $[1,1]^T$, and state whether they are orthogonal. | $(2)(1)+(3)(1)=5$, so they are not orthogonal since it is nonzero | p.2; procedure |

## Solving for a Component to Make Vectors Orthogonal
| Front | Back | Notes |
| --- | --- | --- |
| Find $k$ so that $[2,k]^T$ is orthogonal to $[3,-6]^T$. | $6-6k=0 \Rightarrow k=1$ | p.2; procedure |

## Finding a Unit Vector
| Front | Back | Notes |
| --- | --- | --- |
| Find a unit vector pointing in the same direction as $[3,-4]^T$. | The norm is $5$, so the unit vector is $[3/5,-4/5]^T$ | p.2; procedure |

## Converting a Sum of Sine and Cosine to Amplitude-Phase Form
| Front | Back | Notes |
| --- | --- | --- |
| Write $3\cos 2t + 4\sin 2t$ in the form $R\cos(2t-\delta)$. | $R=\sqrt{3^2+4^2}=5$, $\delta=\arctan(4/3)\approx 0.9273$ rad, giving $5\cos(2t-\delta)$ | p.3; procedure |

## Solving for Constants in a Vector Valued General Solution
| Front | Back | Notes |
| --- | --- | --- |
| Given $\mathbf{x}(t)=c_1[1,3]^Te^{2t}+c_2[1,1]^Te^{4t}$ with $\mathbf{x}(0)=[5,7]^T$, find $c_1$ and $c_2$. | Solve $c_1+c_2=5$ and $3c_1+c_2=7$, giving $c_1=1$, $c_2=4$ | p.3; procedure |
# Node map
```json
[
 {
  "name": "Vectors",
  "type": "concept",
  "existing": true,
  "parent": "Vectors, Dot Products, and Norms",
  "prereqs": [],
  "uses": [],
  "page": 1,
  "summary": "A vector in $\\mathbb{R}^n$ is a column of $n$ real numbers, written $\\mathbf{x}=[x_1,\\ldots,x_n]^T$ using the transpose to save space."
 },
 {
  "name": "Vector Addition",
  "type": "concept",
  "existing": true,
  "parent": "Vectors, Dot Products, and Norms",
  "prereqs": [
   "Vectors"
  ],
  "uses": [],
  "page": 1,
  "summary": "Vectors add componentwise: $\\mathbf{x}+\\mathbf{y}$ has entries $x_i+y_i$."
 },
 {
  "name": "Scalar multiplication (linear algebra)",
  "type": "concept",
  "existing": true,
  "parent": "Vectors, Dot Products, and Norms",
  "prereqs": [
   "Vectors"
  ],
  "uses": [],
  "page": 1,
  "summary": "A scalar $c$ multiplies a vector componentwise: $c\\mathbf{x}$ has entries $cx_i$."
 },
 {
  "name": "Dot Product",
  "type": "concept",
  "existing": true,
  "parent": "Vectors, Dot Products, and Norms",
  "prereqs": [
   "Vectors"
  ],
  "uses": [],
  "page": 1,
  "summary": "The dot product $\\mathbf{x}\\cdot\\mathbf{y}=x_1y_1+\\cdots+x_ny_n$ is a single number, symmetric and linear in each slot."
 },
 {
  "name": "Euclidean Norm",
  "type": "concept",
  "existing": false,
  "parent": "Vectors, Dot Products, and Norms",
  "prereqs": [
   "Dot Product"
  ],
  "uses": [],
  "page": 1,
  "summary": "The length of a vector is $\\lVert \\mathbf{x} \\rVert=\\sqrt{\\mathbf{x}\\cdot\\mathbf{x}}$; dividing a nonzero vector by its norm gives a unit vector in the same direction."
 },
 {
  "name": "Unit Vector",
  "type": "concept",
  "existing": true,
  "parent": "Vectors, Dot Products, and Norms",
  "prereqs": [
   "Euclidean Norm"
  ],
  "uses": [],
  "page": 1,
  "summary": "A unit vector is a vector whose norm equals $1$."
 },
 {
  "name": "Orthogonality (Vectors)",
  "type": "concept",
  "existing": false,
  "parent": "Vectors, Dot Products, and Norms",
  "prereqs": [
   "Dot Product"
  ],
  "uses": [],
  "page": 1,
  "summary": "Two vectors are perpendicular, that is orthogonal, exactly when their dot product is zero; eigenvectors of a real symmetric matrix are orthogonal."
 },
 {
  "name": "Amplitude-Phase Form of a Sinusoid",
  "type": "concept",
  "existing": false,
  "parent": "Vectors, Dot Products, and Norms",
  "prereqs": [
   "Euclidean Norm",
   "Trigonometric functions",
   "Arctan"
  ],
  "uses": [],
  "page": 1,
  "summary": "A sum $c_1\\cos\\theta+c_2\\sin\\theta$ equals a single shifted cosine $R\\cos(\\theta-\\delta)$, where $R$ is the norm of $[c_1,c_2]^T$ and $\\tan\\delta=c_2/c_1$."
 },
 {
  "name": "Vector Arithmetic Practice",
  "type": "problem",
  "existing": false,
  "parent": "Vectors, Dot Products, and Norms",
  "prereqs": [],
  "uses": [
   "Vector Addition",
   "Scalar multiplication (linear algebra)",
   "Dot Product",
   "Euclidean Norm"
  ],
  "page": 2,
  "summary": "Computes $\\mathbf{x}+\\mathbf{y}$, $3\\mathbf{x}$, $\\mathbf{x}\\cdot\\mathbf{y}$, and $\\lVert \\mathbf{x} \\rVert$ for given vectors."
 },
 {
  "name": "Testing Orthogonality of Vector Pairs",
  "type": "problem",
  "existing": false,
  "parent": "Vectors, Dot Products, and Norms",
  "prereqs": [],
  "uses": [
   "Orthogonality (Vectors)",
   "Dot Product"
  ],
  "page": 2,
  "summary": "Checks three vector pairs for orthogonality by computing their dot products."
 },
 {
  "name": "Solving for a Component to Make Vectors Orthogonal",
  "type": "problem",
  "existing": false,
  "parent": "Vectors, Dot Products, and Norms",
  "prereqs": [],
  "uses": [
   "Orthogonality (Vectors)",
   "Dot Product"
  ],
  "page": 2,
  "summary": "Finds the unknown component $k$ that makes $[2,k]^T$ orthogonal to $[3,-6]^T$."
 },
 {
  "name": "Finding a Unit Vector",
  "type": "problem",
  "existing": false,
  "parent": "Vectors, Dot Products, and Norms",
  "prereqs": [],
  "uses": [
   "Euclidean Norm",
   "Unit Vector"
  ],
  "page": 2,
  "summary": "Normalizes $[3,-4]^T$ into a unit vector by dividing by its norm."
 },
 {
  "name": "Converting a Sum of Sine and Cosine to Amplitude-Phase Form",
  "type": "problem",
  "existing": false,
  "parent": "Vectors, Dot Products, and Norms",
  "prereqs": [],
  "uses": [
   "Amplitude-Phase Form of a Sinusoid"
  ],
  "page": 3,
  "summary": "Rewrites $3\\cos 2t+4\\sin 2t$ as $R\\cos(2t-\\delta)$ by computing amplitude and phase."
 },
 {
  "name": "Solving for Constants in a Vector Valued General Solution",
  "type": "problem",
  "existing": false,
  "parent": "Vectors, Dot Products, and Norms",
  "prereqs": [],
  "uses": [
   "Vector Addition",
   "Scalar multiplication (linear algebra)",
   "System of equations"
  ],
  "page": 3,
  "summary": "Uses an initial condition to turn a vector-valued general solution into a linear system for the constants $c_1,c_2$."
 }
]
```

# Frankenstein problems

**Problem A.** Let $\mathbf{a}=[4,-3]^T$. (a) Find the unit vector in the direction of $\mathbf{a}$. (b) Find $k$ so that $[k,2]^T$ is orthogonal to $\mathbf{a}$. (c) Verify that $\mathbf{a}\cdot\mathbf{a} = \lVert \mathbf{a} \rVert^2$.

*Concepts tested: Euclidean Norm, Unit Vector, Orthogonality (Vectors), Dot Product.*

Solution. (a) $\lVert \mathbf{a} \rVert = \sqrt{4^2+(-3)^2} = \sqrt{16+9} = 5$, so the unit vector is $[4/5,-3/5]^T$. (b) Orthogonality requires $[k,2]^T \cdot [4,-3]^T = 0$, so $4k - 6 = 0$, giving $k = 3/2$. (c) $\mathbf{a}\cdot\mathbf{a} = 16+9 = 25$, and $\lVert \mathbf{a} \rVert^2 = 5^2 = 25$. They match, confirming the norm-dot product relationship.

**Problem B.** An oscillator's position is $x(t) = 5\cos 3t + 12\sin 3t$. (a) Write $x(t)$ in amplitude-phase form $R\cos(3t-\delta)$. (b) Confirm that $R$ equals the norm of the vector $\mathbf{v}=[5,12]^T$. (c) Letting $\mathbf{y}(t)=[\cos 3t,\sin 3t]^T$, confirm that $x(t) = \mathbf{v}\cdot\mathbf{y}(t)$.

*Concepts tested: Amplitude-Phase Form of a Sinusoid, Euclidean Norm, Dot Product.*

Solution. (a) $R = \sqrt{5^2+12^2} = \sqrt{25+144} = \sqrt{169} = 13$, and $\delta = \arctan(12/5) \approx 1.176$ rad, so $x(t) = 13\cos(3t-\delta)$. (b) $\lVert \mathbf{v} \rVert = \sqrt{5^2+12^2} = 13 = R$, confirming the amplitude is the norm of $[c_1,c_2]^T$. (c) By the dot product formula, $\mathbf{v}\cdot\mathbf{y}(t) = 5\cos 3t + 12\sin 3t = x(t)$, exactly the definition being applied.
