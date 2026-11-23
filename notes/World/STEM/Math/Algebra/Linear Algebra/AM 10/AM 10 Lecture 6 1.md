---
type: lecture
parent: "[[AM 10]]"
domain: math
status: draft
---
A **vector space over** $\mathbb{R}$ (aka, a **real vector space**) is a **nonempty** set $V$ on which two operations are defined:

(i) **Addition** (closure):
$$
\mathbf{u}+\mathbf{v}\in V
\quad\text{for all }\mathbf{u},\mathbf{v}\in V.
$$

(ii) **Scalar multiplication** (closure):
$$
a\mathbf{u}\in V
\quad\text{for all }\mathbf{u}\in V,\ a\in\mathbb{R}.
$$
and satisfies all properties of R^n
1. (**Commutativity of addition**)  
$$
\mathbf{u}+\mathbf{v}=\mathbf{v}+\mathbf{u},
\quad\text{for all }\mathbf{u},\mathbf{v}\in V.
$$

2. (**Associativity of addition**)  
$$
(\mathbf{u}+\mathbf{v})+\mathbf{w}=\mathbf{u}+(\mathbf{v}+\mathbf{w}),
\quad\text{for all }\mathbf{u},\mathbf{v},\mathbf{w}\in V.
$$

3. (**Additive identity**)  
There exists a $\mathbf{0}\in V$ such that
$$
\mathbf{u}+\mathbf{0}=\mathbf{u},
\quad\text{for all }\mathbf{u}\in V.
$$

4. (**Additive inverse**)  
For every $\mathbf{u}\in V$, there exists $-\mathbf{u}\in V$ such that
$$
\mathbf{u}+(-\mathbf{u})=\mathbf{0}.
$$
If that's all we had we'd have a [[Group]], an [[Abelian group]]

So now we want scalar multiplication

5. (**Distributivity over scalar addition**)  
$$
(a+b)\mathbf{u}=a\mathbf{u}+b\mathbf{u},
\quad\text{for all }a,b\in\mathbb{R}\text{ and all }\mathbf{u}\in V.
$$

6. (**Distributivity over vector addition**)  
$$
a(\mathbf{u}+\mathbf{v})=a\mathbf{u}+a\mathbf{v},
\quad\text{for all }a\in\mathbb{R}\text{ and all }\mathbf{u},\mathbf{v}\in V.
$$

7. (**Associativity of scalar multiplication**)  
$$
(ab)\mathbf{u}=a(b\mathbf{u}),
\quad\text{for all }a,b\in\mathbb{R}\text{ and all }\mathbf{u}\in V.
$$

8. (**Scalar identity**)  
$$
1\cdot\mathbf{u}=\mathbf{u},
\quad\text{for all }\mathbf{u}\in V.
$$
We need 8 because it wouldn't follow inherently, and it's satisifed for Rn

This lecture is just looking at examples and learning

We can now most easily go that Given Rn we can say that it satisfies a full vector space

We can go to complex now where a+bi: a,b set R, i^2 = -1


But basically complex are, are, are real + real + complex part so we can think of it rn insofaras as it satisfies being a vector space is that it's just a weird copy of R2

Then there's the trivial space where the set is the zero vector but it's not very interesting

It's useful only to remember that it is it's own vector space (as we'll have to know when we're moving between them and if we happen to move from Rn to V then we'll be misled if we don't recall this)

Now a weird vector space which is all polynomials with real coefficents which is written as $\mathbb{R}[x]$ We can add polynomials we can multiply them the n=0 takes the place of the 0 vector as the null movement element



**Examples**

1.
$$
\mathbb{R}^n=\left\{
\begin{bmatrix}
x_1\\
\vdots\\
x_n
\end{bmatrix}
:\ x_1,\dots,x_n\in\mathbb{R}
\right\}
$$

2.
$$
\mathbb{R}=\mathbb{R}^1
$$
3.
$$
\mathbb{C}=\{\,a+bi:\ a,b\in\mathbb{R},\ i^2=-1\,\}
$$

4.
$$
V=\{\mathbf{0}\}
$$

Upper division math is applying what we learn here about vector spaces and axioms and applying it to functions
5.
$$
\mathbb{R}[x]=\text{ all polynomials with real coefficients.}
$$

$$
\mathbb{R}[x]=\left\{
a_nx^n+\cdots+a_1x+a_0
:\ a_0,\ldots,a_n\in\mathbb{R},\ n=0,1,2,3,\ldots
\right\}
$$
6.
$$
V=\left\{
\begin{bmatrix}
a\\
2a\\
b
\end{bmatrix}
:\ a,b\in\mathbb{R}
\right\}
\subseteq \mathbb{R}^3,
\quad\text{with addition and scalar multiplication defined as usual.}
$$
This is a sufficent subspace but why?

How can we know that so easily?

Well we inherit properties 1-2,5,6-8 from R3, we need a 0 and we need the existence of opposites

We also need to show their closed (if we do an operation the result is in the same subspace)

and then we need to check if there's a 0 vector possible and the existence of opposites
So we arrive at this super cool definition:

If $W$ is a real vector space and $V\subseteq W$ is a real vector space with addition and scalar multiplication **inherited** from $W$, then $V$ is a **subspace** of $W$.

Both V and W but because in inherits properties or structure it is a subspace

Let's demonstrate then what isn't a subspace

$$
U=\left\{\begin{bmatrix}a\\ b\end{bmatrix}:a,b\in\mathbb{R},\ ab=0\right\}\subseteq\mathbb{R}^2
$$

Not a subspace (fails closure under addition):
$$
\begin{bmatrix}1\\0\end{bmatrix}\in U,\quad
\begin{bmatrix}0\\1\end{bmatrix}\in U,\quad
\begin{bmatrix}1\\0\end{bmatrix}+\begin{bmatrix}0\\1\end{bmatrix}=\begin{bmatrix}1\\1\end{bmatrix}\notin U
$$
since $1\cdot 1\neq 0$.

Axioms (usual operations from $\mathbb{R}^2$):
1. $\mathbf{u}+\mathbf{v}=\mathbf{v}+\mathbf{u}$: holds in $\mathbb{R}^2$.
2. $(\mathbf{u}+\mathbf{v})+\mathbf{w}=\mathbf{u}+(\mathbf{v}+\mathbf{w})$: holds in $\mathbb{R}^2$.
3. $\mathbf{0}=\begin{bmatrix}0\\0\end{bmatrix}\in U$: yes.
4. $\mathbf{u}\in U\Rightarrow -\mathbf{u}\in U$: yes, $(-a)(-b)=ab=0$.
5. $(\alpha+\beta)\mathbf{u}=\alpha\mathbf{u}+\beta\mathbf{u}$: holds in $\mathbb{R}^2$.
6. $\alpha(\mathbf{u}+\mathbf{v})=\alpha\mathbf{u}+\alpha\mathbf{v}$: equality holds in $\mathbb{R}^2$, but $U$ fails because $\mathbf{u}+\mathbf{v}$ need not be in $U$ (counterexample above).
7. $(\alpha\beta)\mathbf{u}=\alpha(\beta\mathbf{u})$: holds in $\mathbb{R}^2$.
8. $1\mathbf{u}=\mathbf{u}$: holds in $\mathbb{R}^2$.

Scalar closure (does hold):
$$
\mathbf{u}=\begin{bmatrix}a\\b\end{bmatrix}\in U\Rightarrow ab=0,\quad
\alpha\mathbf{u}=\begin{bmatrix}\alpha a\\ \alpha b\end{bmatrix}\Rightarrow (\alpha a)(\alpha b)=\alpha^2ab=0
$$
So the only failure is addition closure, hence not a subspace. Mind you U doesn't just take values of R^2 but takes values of one dimension being 0 and the other being something else, but it adds together

**Useful Fact**

We can easily determine vector space-heit if 

$V\subseteq W$ is a subspace of $W$ if and only if:

A. $\mathbf{0}\in V$

B. $a\mathbf{u}+b\mathbf{v}\in V$ for all $\mathbf{u},\mathbf{v}\in V$ and $a,b\in\mathbb{R}$
So closure under linear combinations kills two birds with one stone

**Theorem 1**

If $\mathbf{u}_1,\mathbf{u}_2,\ldots,\mathbf{u}_k$ are vectors in the vector space $V$, then
$$
U=\operatorname{span}(\mathbf{u}_1,\mathbf{u}_2,\ldots,\mathbf{u}_k)
$$
is a subspace of $V$.

If $V$ is a vector space and $\mathbf{v}_1,\mathbf{v}_2,\ldots,\mathbf{v}_k\in V$, then
$$
\operatorname{span}(\mathbf{v}_1,\mathbf{v}_2,\ldots,\mathbf{v}_k)
=
\left\{
a_1\mathbf{v}_1+a_2\mathbf{v}_2+\cdots+a_k\mathbf{v}_k
:\ a_1,a_2,\ldots,a_k\in\mathbb{R}
\right\}.
$$
Equivalently: the set of all linear combinations of $\mathbf{v}_1,\mathbf{v}_2,\ldots,\mathbf{v}_k$.

!We're writing span as a short hand for the set of all linear combinations

$$
V_2=\left\{
\begin{bmatrix}
a\\
b\\
c
\end{bmatrix}
:\ 3a+2b=c,\ a-2c=b
\right\}\subseteq\mathbb{R}^3
$$

$$
3a+2b-c=0,\qquad a-b-2c=0
$$

$$
\begin{bmatrix}
3&2&-1\\
1&-1&-2
\end{bmatrix}
\begin{bmatrix}
a\\
b\\
c
\end{bmatrix}
=
\begin{bmatrix}
0\\
0
\end{bmatrix}
$$

$$
V_2=\left\{
\begin{bmatrix}
a\\
b\\
c
\end{bmatrix}
:
\begin{bmatrix}
3&2&-1\\
1&-1&-2
\end{bmatrix}
\begin{bmatrix}
a\\
b\\
c
\end{bmatrix}
=
\begin{bmatrix}
0\\
0
\end{bmatrix}
\right\}.
$$

A way more useful way of thinking about solving whether or not it's closed under linear combination is just to turn it into..... A MATRIX and if it is matrix-able then it can be =0 bc A0=0 and it's also closed as a linear combo

1. Start with the definition:
$$
V_2=\left\{\begin{bmatrix}a\\b\\c\end{bmatrix}:3a+2b=c,\ a-2c=b\right\}\subseteq\mathbb{R}^3
$$

2. Rewrite each equation with $0$ on the right:
$$
3a+2b-c=0,\qquad a-b-2c=0
$$

3. Package the coefficients into a matrix equation $A\mathbf{x}=\mathbf{0}$:
$$
A=\begin{bmatrix}3&2&-1\\ 1&-1&-2\end{bmatrix},\quad
\mathbf{x}=\begin{bmatrix}a\\b\\c\end{bmatrix},\quad
A\mathbf{x}=\begin{bmatrix}0\\0\end{bmatrix}
$$

4. So equivalently:
$$
V_2=\left\{\mathbf{x}\in\mathbb{R}^3:A\mathbf{x}=\mathbf{0}\right\}
$$

5. Subspace test (barebones):
- $\mathbf{0}\in V_2$ since $A\mathbf{0}=\mathbf{0}$.
- If $\mathbf{u},\mathbf{v}\in V_2$ and $r,s\in\mathbb{R}$, then
$$
A(r\mathbf{u}+s\mathbf{v})=rA\mathbf{u}+sA\mathbf{v}=r\mathbf{0}+s\mathbf{0}=\mathbf{0}
$$
so $r\mathbf{u}+s\mathbf{v}\in V_2$.

Therefore $V_2$ is a subspace of $\mathbb{R}^3$.
1. Start with the definition:
$$
V_2=\left\{\begin{bmatrix}a\\b\\c\end{bmatrix}:3a+2b=c,\ a-2c=b\right\}\subseteq\mathbb{R}^3
$$

2. Rewrite each equation with $0$ on the right:
$$
3a+2b-c=0,\qquad a-b-2c=0
$$

3. Package the coefficients into a matrix equation $A\mathbf{x}=\mathbf{0}$:
$$
A=\begin{bmatrix}3&2&-1\\ 1&-1&-2\end{bmatrix},\quad
\mathbf{x}=\begin{bmatrix}a\\b\\c\end{bmatrix},\quad
A\mathbf{x}=\begin{bmatrix}0\\0\end{bmatrix}
$$

4. So equivalently:
$$
V_2=\left\{\mathbf{x}\in\mathbb{R}^3:A\mathbf{x}=\mathbf{0}\right\}
$$

5. Subspace test (barebones):
- $\mathbf{0}\in V_2$ since $A\mathbf{0}=\mathbf{0}$.
- If $\mathbf{u},\mathbf{v}\in V_2$ and $r,s\in\mathbb{R}$, then
$$
A(r\mathbf{u}+s\mathbf{v})=rA\mathbf{u}+sA\mathbf{v}=r\mathbf{0}+s\mathbf{0}=\mathbf{0}
$$
so $r\mathbf{u}+s\mathbf{v}\in V_2$.

Therefore $V_2$ is a subspace of $\mathbb{R}^3$.
! [[Null space|Nullspace]]

The **null space** of an $m\times n$ matrix $A$ is the set
$$
\operatorname{null}(A)=\{\mathbf{x}\in\mathbb{R}^n: A\mathbf{x}=\mathbf{0}\}.
$$

Example 8 is a special case of this.

**Theorem 2**

If $A$ is an $m\times n$ matrix, then $\operatorname{null}(A)$ is a subspace of $\mathbb{R}^n$.

**Because:**

(i) $A\mathbf{0}=\mathbf{0}\ \Longrightarrow\ \mathbf{0}\in \operatorname{null}(A)$.

(ii) If $\mathbf{x},\mathbf{y}\in \operatorname{null}(A)$ and $a,b\in\mathbb{R}$, then
$$
A(a\mathbf{x}+b\mathbf{y})=aA\mathbf{x}+bA\mathbf{y}
=a\mathbf{0}+b\mathbf{0}=\mathbf{0}
\ \Longrightarrow\ a\mathbf{x}+b\mathbf{y}\in \operatorname{null}(A).
$$

- ! [[Column Spaces]]
The **column space** of an $m\times n$ matrix $A$ is the span of its columns.  
If
$$
A=\begin{bmatrix}\mathbf{A}_1&\cdots&\mathbf{A}_n\end{bmatrix},
$$
then
$$
\operatorname{col}(A)=\operatorname{span}(\mathbf{A}_1,\ldots,\mathbf{A}_n).
$$
$\operatorname{col}(A)$ is a subspace of $\mathbb{R}^m$.

	We won't play with row spaces but those exist too

- The three core subspaces
Every subspace of Rn can be described as either the null space of a matrix or the column space of a matrix
Confused AF ABOUT THE  BELOW

---
Column spaces also have another cool interpretation  
PREVIEW OF LINEAR TRANSFORMATIONS

IF

$A$ is $m$ by $n$ and $\mathbf{x}$ is in $\mathbb{R}^n$  
THEN  
$A\mathbf{x}$ is a [[Linear combination]] of the columns of $A$ by definition

Because if  
$$  
A=\begin{bmatrix}\mathbf{A}_1&\cdots&\mathbf{A}_n\end{bmatrix}  
\quad\text{and}\quad  
\mathbf{x}=\begin{bmatrix}x_1\\ \vdots \\ x_n\end{bmatrix},  
$$  
then  
$$  
A\mathbf{x}=x_1\mathbf{A}_1+\cdots+x_n\mathbf{A}_n.  
$$

But this exactly is an element of the column space of $A$

And actually it goes both ways:

- Any $A\mathbf{x}$ is a linear combination of the columns $\Rightarrow$ it’s in $\operatorname{col}(A)$
    
- Any linear combination of the columns can be written as $A\mathbf{x}$ (just put the coefficients into $\mathbf{x}$)
    

So instead of saying “all linear combinations of the columns of $A$”, we can say the same thing as:

Which means its the set of all things that look like $A\mathbf{x}$ for any vector in $\mathbb{R}^n$

So those coefficents can be collected and make them entries of a column vector $\mathbf{x}$

That linear combination is same thing as $A\mathbf{x}$

So the column space of $A$ is a subset of $\mathbb{R}^m$

So you start with vectors in $\mathbb{R}^n$ and end up with vectors in $\mathbb{R}^m$

Example: if $A$ is $3\times 2$, then it takes vectors in $\mathbb{R}^2$ and outputs vectors in $\mathbb{R}^3$  
(if $A$ is $2\times 3$, then it takes vectors in $\mathbb{R}^3$ and outputs vectors in $\mathbb{R}^2$)

This is what's meant by a linear transformation

So  
$$  
\operatorname{col}(A)={A\mathbf{x}:\mathbf{x}\in\mathbb{R}^n}\subseteq\mathbb{R}^m.  
$$

Multiplication by $A$ takes $\mathbf{x}\in\mathbb{R}^n$ to $\mathbf{y}=A\mathbf{x}\in\mathbb{R}^m$.

Also,  
$$  
\operatorname{col}(A)=\operatorname{Im}(A)  
$$  
(the “[[Image (linear algebra)]]” of $A$).

>It matters because it reframes the column space as **everything the matrix (as a linear transformation) can output**, so you can immediately tell what vectors are reachable/solvable as ($A\mathbf{x}=\mathbf{y}$) and what directions get “missed.”

---

So the

The vectors $\mathbf{u}_1,\ldots,\mathbf{u}_k\in U$ are **linearly independent** if

(i) No $\mathbf{u}_i$ is a linear combination of the others:
$$
\mathbf{u}_i\notin \operatorname{span}\big(\mathbf{u}_1,\ldots,\mathbf{u}_{i-1},\mathbf{u}_{i+1},\ldots,\mathbf{u}_k\big)
\quad\text{for each }i.
$$
We want this complex condition but as it turns out it's equivalent to something much simpler

If $\mathbf{u}_1,\ldots,\mathbf{u}_k$ are linearly independent, then
$$
c_1\mathbf{u}_1+\cdots+c_k\mathbf{u}_k=\mathbf{0}
\quad\Longrightarrow\quad
c_1=\cdots=c_k=0,
$$
and vice versa.

Because: $\text{not I}\ \Longleftrightarrow\ \text{not II}$.

--- 
Example (showing the “only trivial solution” test):

Let
$$
\mathbf{u}_1=\begin{bmatrix}1\\0\end{bmatrix},\quad
\mathbf{u}_2=\begin{bmatrix}0\\1\end{bmatrix}\in\mathbb{R}^2.
$$

Check condition (ii): solve
$$
c_1\mathbf{u}_1+c_2\mathbf{u}_2=\mathbf{0}.
$$

Write it out:
$$
c_1\begin{bmatrix}1\\0\end{bmatrix}+c_2\begin{bmatrix}0\\1\end{bmatrix}
=
\begin{bmatrix}c_1\\c_2\end{bmatrix}
=
\begin{bmatrix}0\\0\end{bmatrix}.
$$

So
$$
\begin{aligned}
c_1&=0\\
c_2&=0
\end{aligned}
$$
is the only solution, which means $\mathbf{u}_1,\mathbf{u}_2$ are linearly independent.

And condition (i) matches: $\mathbf{u}_1\notin\operatorname{span}(\mathbf{u}_2)$ and $\mathbf{u}_2\notin\operatorname{span}(\mathbf{u}_1)$.

---

Is there a non-trivial solution to linear independence is the question, although condition II is much easier to confirm

You don't have to go very far echelon form will do 

Let
$$
\mathbf{x}_1=\begin{bmatrix}1\\2\\3\end{bmatrix},\quad
\mathbf{x}_2=\begin{bmatrix}2\\1\\-1\end{bmatrix},\quad
\mathbf{x}_3=\begin{bmatrix}0\\3\\7\end{bmatrix}.
$$

Check linear independence by solving
$$
c_1\mathbf{x}_1+c_2\mathbf{x}_2+c_3\mathbf{x}_3=\mathbf{0}.
$$

As a matrix equation:
$$
\begin{bmatrix}
1&2&0\\
2&1&3\\
3&-1&7
\end{bmatrix}
\begin{bmatrix}
c_1\\
c_2\\
c_3
\end{bmatrix}
=
\begin{bmatrix}
0\\
0\\
0
\end{bmatrix}.
$$
So dependent

