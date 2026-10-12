---
type: lecture
parent: "[[AM 10]]"
domain: math
status: draft
---
- More types of matrices Square matricies
		- Square if m=n
	- Upper triangular if a_ij=0 
		- When i>j (row#>col #)
		- %% What does that mean %%
	- Lower triangular if a_ij
	- Diagonal if it's square and a_ij = 0 when i=/=j
	- Scalar matrix if it's diagonal and a_11=a_22=a_nn
	- Symmetric if it's square and a_ij=a_ij for all i,j
- Transposes
	- The [[Transpose]] of a matrix
	- is where a matrix goes from c_ij = a_ji
		- e.g. So (A^T)^T = A
		- A^T = A means A is a symmetric matrix
- Matrix multiplication, Part 1
		- Up until the first midterm it'll just be matricies times column vectors
		- After the first midterm we'll extend that to matrix multiplication where we can multiply two matricies together
		- This turns out to be extraordinarily useful
	- Only defined under
		- Matrix x column vector
			- - A matrix time a column 
			- We need to write Matrix x column vector because the product is only "[[defined (math)]]" for matrix on the left, column on the right
		- when the m x n matrix has n many columns as the column vector has n rows
			- So those entries on the column vector are actually rows
			- come time to do matricies by matricies it'll be rows  on rows not rows on entries
	- If those are satisfied then...
		- Matrix times a column vector is A . cbar such that A

Definition (matrix–vector product as a linear combination of columns)

Let $A\in\mathbb{R}^{m\times n}$ with columns $A_1,\dots,A_n$, and let $c\in\mathbb{R}^{n\times 1}$ with entries $c_1,\dots,c_n$.

$$
A\,c
=
\begin{bmatrix}
A_1 & A_2 & \cdots & A_n
\end{bmatrix}
\begin{bmatrix}
c_1\\
c_2\\
\vdots\\
c_n
\end{bmatrix}
=
c_1A_1+c_2A_2+\cdots+c_nA_n.
$$
The product, interestingly, is another vector because a matrix multiplied on a vector is rows x columns and if the columns match with the amount of rows in the vector then you'll get a vector in R^m as m is the amount of rows in the matrix that you multply against are A_1, A_2,A_3 as an element of the set R^m

Example (compute $A\,c$ as a column combination)

$$
\begin{bmatrix}
1&2&1&0\\
2&3&0&4\\
-3&0&1&-2
\end{bmatrix}
\begin{bmatrix}
2\\
3\\
7\\
4
\end{bmatrix}
=
2\begin{bmatrix}
1\\
2\\
-3
\end{bmatrix}
+
3\begin{bmatrix}
2\\
3\\
0
\end{bmatrix}
+
7\begin{bmatrix}
1\\
0\\
1
\end{bmatrix}
+
4\begin{bmatrix}
0\\
4\\
-2
\end{bmatrix}
$$

$$
=
\begin{bmatrix}
2\\
4\\
-6
\end{bmatrix}
+
\begin{bmatrix}
6\\
9\\
0
\end{bmatrix}
+
\begin{bmatrix}
7\\
0\\
7
\end{bmatrix}
+
\begin{bmatrix}
0\\
16\\
-8
\end{bmatrix}
$$

$$
=
\begin{bmatrix}
2+6+7+0\\
4+9+0+16\\
-6+0+7-8
\end{bmatrix}
=
\begin{bmatrix}
15\\
29\\
-7
\end{bmatrix}
$$

- Inner Product
	- Remember $A\times \bar{c}$ is only defines if Columns of A = # of rows of $\bar{c}$ 
		- Special case: A has one row 
		- A = $[a_1,a_2,...a_n]$ 
			- Because all vectors are just matrices where one of their dimensions is 1
			- It's technically an [[Inner Product]] but we'll call this a row-column product for now
		- What you end up getting is a scalar

- An Easier Way of Doing it in your head
$$
\begin{bmatrix}
1&2&1&0\\
2&3&0&4\\
-3&0&1&-2
\end{bmatrix}
\begin{bmatrix}
2\\
3\\
7\\
4
\end{bmatrix}
=
\begin{bmatrix}
2+6+7+0\\
4+9+0+16\\
-6+0+7-8
\end{bmatrix}
=
\begin{bmatrix}
15\\
29\\
-7
\end{bmatrix}
$$

$$
\begin{bmatrix}
1&3&4&1&0\\
2&4&0&0&3\\
1&2&5&1&-2\\
0&-1&2&3&0
\end{bmatrix}
\begin{bmatrix}
1\\
2\\
3\\
4\\
6
\end{bmatrix}
=
\begin{bmatrix}
1+6+12+4+0\\
2+8+0+0+18\\
1+4+15+4-12\\
0-2+6+12+0
\end{bmatrix}
=
\begin{bmatrix}
23\\
28\\
12\\
16
\end{bmatrix}
$$
You can just run every value in a row against the column

So now we have a system of equations described as a coefficient matrix of mxn that given a column vector of constants that exist as a subset of R^n columns and the solution is a subset of R^m 

- It's now time to discuss for what properties of multiplication does Matrix time a vector multiplication work 
	Distribution
		A(x+y)=Ax+Ay and A(ux)=uAx
	Commutativity
		A(uxbar)=uAxbar
- What properties do not apply 
	- "some of" =/= all of
		- Axbar = 0bar -> {A=0 (matrix); xbar = 0bar
	- \[1 1; 2 2] \times \[1; -1] = \[0; 0]
So we're going to back and figure why ab=0 -> a=0 or b=0

INVERTIBILITY AND NEUTRAL ELEMENT PREEMPTIVE DEMONSTRATION


It's not inherent in the real numbers that you get this property in the simple case by if a=0 then done but a=/=0 a we need to use a property of a to demonstrate that b must be 0

That property is [[invertibility]] a^-1 \times (ab) = a^-1 /times 0

We're relying on associativity to let this work. 

We can't divide by 0 so in mathematical zugzwang you write a=/=0 = 0 which can't be true
So a must not be =0 so it must b=0

But now we come to another question??

why does 0 \times a = 0

It means intuitively that you have 0 copies of something, but formally, multiplication is defined not as multiplication itself but as addition, but the problem is you can't add 1/3 times  

a is defined as what in the reals, not by a specific property but by it being the neutral element
























Slide 1
Beginning of how we use matricies more completely 

A generic matrix has m rows and n columns

If the two are the same it's a [[Square Matrix]]

Upper triangular matrix if all the non zero entries are above the diagonal where i = j

all the entries below that are 0
Slide 2

Lower triangular is analogous but in the other direction

It can be thought alternately that 

Another way of dividing this is when the information has a smaller row # than column # then it is lower triangular and when it the row # is greater than the column # it is upper triangular

Diagonal matrix if it's square and aij = 0 when i =/= j
(if every non 0 value is on the diagonal)

Slide 3

If all those entries are the same then it's a scalar matrix





Slide 9
Don't take shortcuts breaking down a matrix into a linear equation 

Slide 10
The product of matrix times vector is only defined if # of columns of A = # of rows of $\bar C$ 
It just means it's not defined if it's not a square

Special case: A has one row 

Scalar product of a row vector

## Slide 1

Lecture 5  
Matrix and Vector Arithmetic, I  
• Some matrix terminology.  
• Definition of a matrix transpose, and some properties.  
• Matrix multiplication and some properties.  
• Arithmetic properties of matrix-vector multiplication.  
↑

---

## Slide 2

More matrix terminology.

The $m\times n$ matrix  
$$  
A=\begin{bmatrix}  
a_{11}&a_{12}&\cdots&a_{1n}\  
a_{21}&a_{22}&\cdots&a_{2n}\  
\vdots&\vdots&\ddots&\vdots\  
a_{m1}&a_{m2}&\cdots&a_{mn}  
\end{bmatrix}  
$$

$A$ is

1. Square, if $m=n$.
    
2. Upper triangular if $a_{ij}=0$ when $i>j$ (row # > col. #)
    

---

## Slide 3

3. lower triangular if $a_{ij}=0$ when $i<j$ (row # < col.#)
    

Examples:  
$$  
\begin{bmatrix}  
1&2&3&1&0\  
0&2&4&1&2\  
0&0&3&3&0\  
0&0&0&4&2  
\end{bmatrix}  
\ \text{upper}  
\qquad  
\begin{bmatrix}  
1&0&0&0\  
4&2&0&0\  
0&3&1&0\  
3&0&2&4  
\end{bmatrix}  
\ \text{lower}  
$$

4. Diagonal if it’s square and $a_{ij}=0$ when $i\ne j$
    

---

## Slide 4

5. a scalar matrix if it’s diagonal and $a_{11}=a_{22}=\cdots=a_{nn}$
    

Examples:  
$$  
\begin{bmatrix}  
1&0&0&0\  
0&2&0&0\  
0&0&1&0\  
0&0&0&4  
\end{bmatrix}  
\ \text{diagonal}  
\qquad  
\begin{bmatrix}  
2&0&0&0\  
0&2&0&0\  
0&0&2&0\  
0&0&0&2  
\end{bmatrix}  
\ \text{scalar}  
$$

6. Symmetric if it’s square and $a_{ij}=a_{ji}$ for all $i,j$
    

---

## Slide 5

Example  
$$  
\begin{bmatrix}  
1&4&0&3\  
4&2&3&0\  
0&3&1&2\  
3&0&2&4  
\end{bmatrix}  
\ \text{symmetric}  
$$

Note: Diagonal $\Rightarrow$ symmetric; ref $\Rightarrow$ upper triangular.

---

## Slide 6

The transpose of  
$$  
A=\begin{bmatrix}  
a_{11}&a_{12}&\cdots&a_{1n}\  
a_{21}&a_{22}&\cdots&a_{2n}\  
\vdots&\vdots&\ddots&\vdots\  
a_{m1}&a_{m2}&\cdots&a_{mn}  
\end{bmatrix}  
$$  
is  
$$  
A^T=\begin{bmatrix}  
c_{11}&c_{12}&\cdots&c_{1m}\  
c_{21}&c_{22}&\cdots&c_{2m}\  
\vdots&\vdots&\ddots&\vdots\  
c_{n1}&c_{n2}&\cdots&c_{nm}  
\end{bmatrix}  
$$  
with $c_{ij}=a_{ji}$.

---

## Slide 7

# Example:  
$$  
\begin{bmatrix}  
1&2&0&1&3&4\  
1&1&3&0&4&2\  
0&1&2&4&3&1\  
2&0&1&3&1&4  
\end{bmatrix}^T

\begin{bmatrix}  
1&1&0&2\  
2&1&1&0\  
0&3&2&1\  
1&0&4&3\  
3&4&3&1\  
4&2&1&4  
\end{bmatrix}  
$$

(i) $(A^T)^T=A$  
(ii) $A^T=A\Leftrightarrow A$ symmetric

---

## Slide 8

Matrix multiplication, I

1. matrix x column
    

If $A=[\bar{A}_1,\bar{A}_2,\ldots,\bar{A}_n]$ is an $m\times n$ matrix (n col.s)

and $\bar{c}=\begin{bmatrix}c_1\c_2\ \vdots\ c_n\end{bmatrix}\in\mathbb{R}^n$ (n rows)

Then

---

## Slide 9

# $$  
A\bar{c}

# \underbrace{\begin{bmatrix}\bar{A}_1&\bar{A}_2&\cdots&\bar{A}_n\end{bmatrix}}_{m\times n}  
\underbrace{\begin{bmatrix}c_1\c_2\ \vdots\ c_n\end{bmatrix}}_{n\times 1}

c_1\bar{A}_1+c_2\bar{A}_2+\cdots+c_n\bar{A}_n  
$$

Definition $\Rightarrow$  
$$  
=\begin{bmatrix}w_1\ \vdots\ w_m\end{bmatrix}\in\mathbb{R}^m  
$$

$\bar{A}_1,\bar{A}_2,\ldots,\bar{A}_n\in\mathbb{R}^m$

---

## Slide 10

# Example  
$$  
\begin{bmatrix}  
1&2&1&0\  
2&3&0&4\  
-3&0&1&-2  
\end{bmatrix}  
\begin{bmatrix}  
2\  
3\  
7\  
4  
\end{bmatrix}

# 2\begin{bmatrix}1\2\-3\end{bmatrix}  
+3\begin{bmatrix}2\3\0\end{bmatrix}  
+7\begin{bmatrix}1\0\1\end{bmatrix}  
+4\begin{bmatrix}0\4\-2\end{bmatrix}  
$$  
$$

# \begin{bmatrix}  
2+6+7+0\  
4+9+0+16\  
-6+0+7-8  
\end{bmatrix}

\begin{bmatrix}  
15\  
29\  
-7  
\end{bmatrix}  
$$

---

## Slide 11

Important

$A\cdot\bar{c}$ is only defined if

# columns of $A$ = # of rows of $\bar{c}$

# Special Case: $A$ has one row  
$$  
A=\begin{bmatrix}a_1&a_2&\cdots&a_n\end{bmatrix}  
$$  
$$  
\begin{bmatrix}a_1&a_2&\cdots&a_n\end{bmatrix}  
\begin{bmatrix}c_1\c_2\ \vdots\ c_n\end{bmatrix}

\begin{bmatrix}a_1c_1+\cdots+a_nc_n\end{bmatrix}  
\quad \text{(row-column product)}  
$$

Scalar  
$$  
=a_1c_1+\cdots+a_nc_n  
$$

---

## Slide 12

Another perspective:

write  
$$  
A=  
\begin{bmatrix}  
\bar{R}_1\  
\vdots\  
\bar{R}_m  
\end{bmatrix},  
\quad  
\bar{R}_i=\text{row }i\text{ of }A  
$$  
(has $n$ columns.)

$\Rightarrow\ \bar{R}_i\cdot\bar{c}$ is defined.

# Claim:  
$$  
A\cdot\bar{c}

\begin{bmatrix}  
\bar{R}_1\cdot\bar{c}\  
\vdots\  
\bar{R}_m\cdot\bar{c}  
\end{bmatrix}  
$$

---

## Slide 13

# … Because  
$$  
A=  
\begin{bmatrix}  
\bar{R}_1\  
\vdots\  
\bar{R}_m  
\end{bmatrix}

\begin{bmatrix}  
\bar{A}_1&\bar{A}_2&\cdots&\bar{A}_n  
\end{bmatrix}  
$$

# $i$th entry in  
$$  
A\bar{c}=c_1\cdot\bar{A}_1+c_2\cdot\bar{A}_2+\cdots+c_n\cdot\bar{A}_n  
$$  
is  
$$  
=c_1\cdot a_{i1}+c_2\cdot a_{i2}+\cdots+c_n\cdot a_{in}  
$$  
$$

\begin{bmatrix}  
a_{i1}&a_{i2}&\cdots&a_{in}  
\end{bmatrix}  
\begin{bmatrix}  
c_1\  
\vdots\  
c_n  
\end{bmatrix}  
=\bar{R}_i\cdot\bar{c}  
$$
## Slide 1

Lecture 5  
Matrix and Vector Arithmetic, I  
• Some matrix terminology.  
• Definition of a matrix transpose, and some properties.  
• Matrix multiplication and some properties.  
• Arithmetic properties of matrix-vector multiplication.  
↑

---

## Slide 2

More matrix terminology.

The $m\times n$ matrix  
$$  
A=\begin{bmatrix}  
a_{11}&a_{12}&\cdots&a_{1n}\  
a_{21}&a_{22}&\cdots&a_{2n}\  
\vdots&\vdots&\ddots&\vdots\  
a_{m1}&a_{m2}&\cdots&a_{mn}  
\end{bmatrix}  
$$

$A$ is

1. Square, if $m=n$.
    
2. Upper triangular if $a_{ij}=0$ when $i>j$ (row # > col. #)
    

---

## Slide 3

3. lower triangular if $a_{ij}=0$ when $i<j$ (row # < col.#)
    

Examples:  
$$  
\begin{bmatrix}  
1&2&3&1&0\  
0&2&4&1&2\  
0&0&3&3&0\  
0&0&0&4&2  
\end{bmatrix}  
\ \text{upper}  
\qquad  
\begin{bmatrix}  
1&0&0&0\  
4&2&0&0\  
0&3&1&0\  
3&0&2&4  
\end{bmatrix}  
\ \text{lower}  
$$

4. Diagonal if it’s square and $a_{ij}=0$ when $i\ne j$
    

---

## Slide 4

5. a scalar matrix if it’s diagonal and $a_{11}=a_{22}=\cdots=a_{nn}$
    

Examples:  
$$  
\begin{bmatrix}  
1&0&0&0\  
0&2&0&0\  
0&0&1&0\  
0&0&0&4  
\end{bmatrix}  
\ \text{diagonal}  
\qquad  
\begin{bmatrix}  
2&0&0&0\  
0&2&0&0\  
0&0&2&0\  
0&0&0&2  
\end{bmatrix}  
\ \text{scalar}  
$$

6. Symmetric if it’s square and $a_{ij}=a_{ji}$ for all $i,j$
    

---

## Slide 5

Example  
$$  
\begin{bmatrix}  
1&4&0&3\  
4&2&3&0\  
0&3&1&2\  
3&0&2&4  
\end{bmatrix}  
\ \text{symmetric}  
$$

Note: Diagonal $\Rightarrow$ symmetric; ref $\Rightarrow$ upper triangular.

---

## Slide 6

The transpose of  
$$  
A=\begin{bmatrix}  
a_{11}&a_{12}&\cdots&a_{1n}\  
a_{21}&a_{22}&\cdots&a_{2n}\  
\vdots&\vdots&\ddots&\vdots\  
a_{m1}&a_{m2}&\cdots&a_{mn}  
\end{bmatrix}  
$$  
is  
$$  
A^T=\begin{bmatrix}  
c_{11}&c_{12}&\cdots&c_{1m}\  
c_{21}&c_{22}&\cdots&c_{2m}\  
\vdots&\vdots&\ddots&\vdots\  
c_{n1}&c_{n2}&\cdots&c_{nm}  
\end{bmatrix}  
$$  
with $c_{ij}=a_{ji}$.

---

## Slide 7

# Example:  
$$  
\begin{bmatrix}  
1&2&0&1&3&4\  
1&1&3&0&4&2\  
0&1&2&4&3&1\  
2&0&1&3&1&4  
\end{bmatrix}^T

\begin{bmatrix}  
1&1&0&2\  
2&1&1&0\  
0&3&2&1\  
1&0&4&3\  
3&4&3&1\  
4&2&1&4  
\end{bmatrix}  
$$

(i) $(A^T)^T=A$  
(ii) $A^T=A\Leftrightarrow A$ symmetric

---

## Slide 8

Matrix multiplication, I

1. matrix x column
    

If $A=[\bar{A}_1,\bar{A}_2,\ldots,\bar{A}_n]$ is an $m\times n$ matrix (n col.s)

and $\bar{c}=\begin{bmatrix}c_1\c_2\ \vdots\ c_n\end{bmatrix}\in\mathbb{R}^n$ (n rows)

Then

---

## Slide 9

# $$  
A\bar{c}

# \underbrace{\begin{bmatrix}\bar{A}_1&\bar{A}_2&\cdots&\bar{A}_n\end{bmatrix}}_{m\times n}  
\underbrace{\begin{bmatrix}c_1\c_2\ \vdots\ c_n\end{bmatrix}}_{n\times 1}

c_1\bar{A}_1+c_2\bar{A}_2+\cdots+c_n\bar{A}_n  
$$

Definition $\Rightarrow$  
$$  
=\begin{bmatrix}w_1\ \vdots\ w_m\end{bmatrix}\in\mathbb{R}^m  
$$

$\bar{A}_1,\bar{A}_2,\ldots,\bar{A}_n\in\mathbb{R}^m$

---

## Slide 10

# Example  
$$  
\begin{bmatrix}  
1&2&1&0\  
2&3&0&4\  
-3&0&1&-2  
\end{bmatrix}  
\begin{bmatrix}  
2\  
3\  
7\  
4  
\end{bmatrix}

# 2\begin{bmatrix}1\2\-3\end{bmatrix}  
+3\begin{bmatrix}2\3\0\end{bmatrix}  
+7\begin{bmatrix}1\0\1\end{bmatrix}  
+4\begin{bmatrix}0\4\-2\end{bmatrix}  
$$  
$$

# \begin{bmatrix}  
2+6+7+0\  
4+9+0+16\  
-6+0+7-8  
\end{bmatrix}

\begin{bmatrix}  
15\  
29\  
-7  
\end{bmatrix}  
$$

---

## Slide 11

Important

$A\cdot\bar{c}$ is only defined if

# columns of $A$ = # of rows of $\bar{c}$

# Special Case: $A$ has one row  
$$  
A=\begin{bmatrix}a_1&a_2&\cdots&a_n\end{bmatrix}  
$$  
$$  
\begin{bmatrix}a_1&a_2&\cdots&a_n\end{bmatrix}  
\begin{bmatrix}c_1\c_2\ \vdots\ c_n\end{bmatrix}

\begin{bmatrix}a_1c_1+\cdots+a_nc_n\end{bmatrix}  
\quad \text{(row-column product)}  
$$

Scalar  
$$  
=a_1c_1+\cdots+a_nc_n  
$$

Vectors are equal if all their entries are the same

The ith entry in a linear combination of $A\bar c=c$

This needs to be verified

---

## Slide 12

Another perspective:

write  
$$  
A=  
\begin{bmatrix}  
\bar{R}_1\  
\vdots\  
\bar{R}_m  
\end{bmatrix},  
\quad  
\bar{R}_i=\text{row }i\text{ of }A  
$$  
(has $n$ columns.)

$\Rightarrow\ \bar{R}_i\cdot\bar{c}$ is defined.

# Claim:  
$$  
A\cdot\bar{c}

\begin{bmatrix}  
\bar{R}_1\cdot\bar{c}\  
\vdots\  
\bar{R}_m\cdot\bar{c}  
\end{bmatrix}  
$$

---

## Slide 13

# … Because  
$$  
A=  
\begin{bmatrix}  
\bar{R}_1\  
\vdots\  
\bar{R}_m  
\end{bmatrix}

\begin{bmatrix}  
\bar{A}_1&\bar{A}_2&\cdots&\bar{A}_n  
\end{bmatrix}  
$$

# $i$th entry in  
$$  
A\bar{c}=c_1\cdot\bar{A}_1+c_2\cdot\bar{A}_2+\cdots+c_n\cdot\bar{A}_n  
$$  
is  
$$  
=c_1\cdot a_{i1}+c_2\cdot a_{i2}+\cdots+c_n\cdot a_{in}  
$$  
$$

\begin{bmatrix}  
a_{i1}&a_{i2}&\cdots&a_{in}  
\end{bmatrix}  
\begin{bmatrix}  
c_1\  
\vdots\  
c_n  
\end{bmatrix}  
=\bar{R}_i\cdot\bar{c}  
$$
## Slide 14

16/  
Examples
Here is the corrected, properly formatted LaTeX, with the computation completed and no syntax errors.

# $$  
\begin{bmatrix}  
1&2&1&0\  
2&3&0&4\  
-3&0&1&-2  
\end{bmatrix}  
\begin{bmatrix}  
2\  
3\  
7\  
4  
\end{bmatrix}

2\begin{bmatrix}1\2\-3\end{bmatrix}  
+3\begin{bmatrix}2\3\0\end{bmatrix}  
+7\begin{bmatrix}1\0\1\end{bmatrix}  
+4\begin{bmatrix}0\4\-2\end{bmatrix}  
$$


$$
\begin{bmatrix}  
2+6+7+0\\  
4+9+0+16\\  
-6+0+7-8  
\end{bmatrix}

\begin{bmatrix}  
15\  
29\  
-7  
\end{bmatrix}  
$$

If you want this rewritten **strictly in the slide’s two-column placeholder style**, say so and I will mirror it exactly.

# $$  
\begin{bmatrix}  
1&3&4&1&0\  
2&4&0&0&3\  
1&2&5&1&-2\  
0&-1&2&3&0  
\end{bmatrix}  
\begin{bmatrix}  
1\  
2\  
3\  
4\  
6  
\end{bmatrix}

# \begin{bmatrix}  
;\  
;\  
;\  
;  
\end{bmatrix}

\begin{bmatrix}  
;\  
;\  
;\  
;  
\end{bmatrix}  
$$

---

## Slide 15

17/ Linear system  
$$  
\begin{aligned}  
a_{11}x_1+\cdots+a_{1n}x_n&=b_1\  
a_{21}x_1+\cdots+a_{2n}x_n&=b_2\  
\vdots\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ &\vdots\  
a_{m1}x_1+\cdots+a_{mn}x_n&=b_m  
\end{aligned}  
$$

$\cdots$ to vector equation

$$  
x_1\bar{A}_1+\cdots+x_n\bar{A}_n=\bar{b}  
$$

to $\cdots$

How can he rewrite that linear combination 

As a matrix product where those are the columns of the matrix 

What do we call that matrix

How is that matrix related to the original system

It's the [[coefficient matrix]] just made up of other columns

---

## Slide 16

18/ $\cdots$ matrix equation


$$  
\begin{bmatrix}\bar{A}_1&\bar{A}_2&\cdots&\bar{A}_n\end{bmatrix}  
\begin{bmatrix}  
x_1\\  
\vdots\\  
x_n  
\end{bmatrix}

\begin{bmatrix}  
b_1\  
\vdots\  
b_n  
\end{bmatrix}  
$$

$$  
A\bar{x}=\bar{b}  
$$

$m\times n$  
$\bar{x}\in\mathbb{R}^n$  
$\bar{b}\in\mathbb{R}^m$

coefficient matrix  
constant vector

$\Leftrightarrow\ [A\mid b]$

(same as in augmented matrix)

The first thing you do is take the two pieces of inromation

aRead of the x1s and xns thought of as vectors in Rn this is just a useful way of thinking about them 

Many present inthe fashion of a 



---

## Slide 17

19/ Matrix-vector multiplication has (some of) the usual properties:

(i) Distributes over addition  
$$  
A\cdot(\bar{x}+\bar{y})=A\bar{x}+A\bar{y}  
$$




(ii) Commutes with scalar mult.  
$$  
A(u\bar{x})=uA\bar{x}  
$$

How can we tell?


---

## Slide 18

# 20/  
$$  
A\cdot(\bar{x}+\bar{y})
=
\begin{bmatrix}\bar{A}_1&\bar{A}_2&\cdots&\bar{A}_n\end{bmatrix}  
\left(  
\begin{bmatrix}  
x_1\\  
\vdots\\  
x_n  
\end{bmatrix}  
+  
\begin{bmatrix}  
y_1\\  
\vdots\\
y_n  
\end{bmatrix}  
\right)  
$$

# (i)  
$$

\begin{bmatrix}\bar{A}_1&\bar{A}_2&\cdots&\bar{A}_n\end{bmatrix}  
\begin{bmatrix}  
x_1+y_1\  
\vdots\  
x_n+y_n  
\end{bmatrix}  
$$

$$  
=(x_1+y_1)\bar{A}_1+\cdots+(x_n+y_n)\bar{A}_n  
$$

$$  
=(x_1\bar{A}_1+\cdots+x_n\bar{A}_n)+(y_1\bar{A}_1+\cdots+y_n\bar{A}_n)  
$$

$$  
=A\bar{x}+A\bar{y}\ \ \checkmark  
$$

---

## Slide 19

# 21/  
(ii)  
$$  
A(u\bar{x})

\begin{bmatrix}\bar{A}_1&\bar{A}_2&\cdots&\bar{A}_n\end{bmatrix}  
\cdot  
\begin{bmatrix}  
ux_1\  
\vdots\  
ux_n  
\end{bmatrix}  
$$

$$  
=ux_1\bar{A}_1+\cdots+ux_n\bar{A}_n  
$$

$$  
=u(x_1\bar{A}_1+\cdots+x_n\bar{A}_n)  
$$

$$  
=u\cdot A\bar{x}\ \ \checkmark  
$$


Some of our assumptions fail

---

## Slide 20

22/ “some of” $\ne$ “all of”

$$  
A\bar{x}=\bar{0}\ \not\Rightarrow\  
\left{  
\begin{aligned}  
&A=0\ \text{(matrix)}\  
&\text{or}\  
&\bar{x}=\bar{0}  
\end{aligned}  
\right.  
$$

Example

# $$  
\begin{bmatrix}  
1&1\  
2&2  
\end{bmatrix}  
\cdot  
\begin{bmatrix}  
1\  
-1  
\end{bmatrix}

\begin{bmatrix}  
0\  
0  
\end{bmatrix}  
$$


---

## Slide 21

 Question

Why is it true that  
for numbers $a,b$  
$ab=0$ ..........> $a=0$ or $b=0$ ?

If a=0 then we're done. If a is not 0, now we come to a basic property of the real numbers

Every non 0 number has a reciprocal

so if a is not 0 it's invertible

So we can take a here and multiply both sides by a inverse

So a^-1 (ab)= a^-1 0

basically if a is not 0 we divide ab by a and get b which is = 0

What we've never noticed is that multiplication is associative



---

## Slide 22

24/ Question

Why is it true that  

$0\cdot a=0$ 

We first think of multiplication as shorthand of addition

But that loses its meaning once we leave the integers

We think of this as the ultimate eraser

The defining property of 0 among all real numbers

0 is the unit element for addition, it's the neutral unit

we can use that bc 0 * a = (0+0) a

now we use multiplication distributing over addition

to get 0\*a + 0\*a

-0\*a
-\0\*a
0=0\*a

for all real #'s $a$ ?


