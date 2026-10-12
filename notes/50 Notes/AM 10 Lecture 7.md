---
type: lecture
parent: "[[AM 10]]"
domain: math
status: draft
---
A [[Basis]] for a vector space V is a set of vectors in V: B={u,u,...,u,...} such that every vector in the set of V has a unique representation as a linear combination of finitely many rectors from B.
4)

2. $B=\left\{
\begin{bmatrix}1\\2\\0\\1\end{bmatrix},
\begin{bmatrix}1\\1\\2\\0\end{bmatrix}
\right\}$ is a [[basis]]

of $V=\operatorname{col}\!\left(
\begin{bmatrix}
1&1&1\\
2&1&3\\
0&2&-2\\
1&0&2
\end{bmatrix}
\right)$

Because

(i) $V=\operatorname{span}\!\left(
\begin{bmatrix}1\\2\\0\\1\end{bmatrix},
\begin{bmatrix}1\\1\\2\\0\end{bmatrix},
\begin{bmatrix}1\\3\\-2\\2\end{bmatrix}
\right)
=\operatorname{span}\!\left(
\begin{bmatrix}1\\2\\0\\1\end{bmatrix},
\begin{bmatrix}1\\1\\2\\0\end{bmatrix}
\right)$

why?

Because
$$
\begin{bmatrix}1\\3\\-2\\2\end{bmatrix}
=
2\begin{bmatrix}1\\2\\0\\1\end{bmatrix}
-\begin{bmatrix}1\\1\\2\\0\end{bmatrix},
$$
so the 3rd column is already in the span of the first two, hence adding it doesn’t change the span.

---

### super succinct commentary (formal what = what)

- **column space**: if $A=[\mathbf{A}_1\ \cdots\ \mathbf{A}_n]$ then
  $$
  \operatorname{col}(A)=\operatorname{span}(\mathbf{A}_1,\ldots,\mathbf{A}_n).
  $$
- **span**: $\operatorname{span}(S)$ is a *set* (all linear combinations), not the original list $S$.
- **[[basis]]**: $B$ is a [[basis]] for $V$ iff  
  (1) $\operatorname{span}(B)=V$ and (2) $B$ is linearly independent.
- **equivalences here**:
  $$
  V=\operatorname{col}(A)=\operatorname{span}(\mathbf{A}_1,\mathbf{A}_2,\mathbf{A}_3)
  =\operatorname{span}(\mathbf{A}_1,\mathbf{A}_2).
  $$
- **not equivalent**:
  $$
  \operatorname{col}(A)\ne\{\mathbf{A}_1,\mathbf{A}_2,\mathbf{A}_3\}
  \quad\text{(space vs just three vectors)}.
  $$

Because:

$$
2\begin{bmatrix}1\\2\\0\\1\end{bmatrix}
-\begin{bmatrix}1\\1\\2\\0\end{bmatrix}
-\begin{bmatrix}1\\3\\-2\\2\end{bmatrix}
=
\begin{bmatrix}0\\0\\0\\0\end{bmatrix}.
$$

check.

$$
\Longrightarrow\quad
\begin{bmatrix}1\\3\\-2\\2\end{bmatrix}
=
2\begin{bmatrix}1\\2\\0\\1\end{bmatrix}
-\begin{bmatrix}1\\1\\2\\0\end{bmatrix}.
$$

So:

$$
\vec{u}
=
a\begin{bmatrix}1\\2\\0\\1\end{bmatrix}
+b\begin{bmatrix}1\\1\\2\\0\end{bmatrix}
+c\begin{bmatrix}1\\3\\-2\\2\end{bmatrix}
$$

$$
=
a\begin{bmatrix}1\\2\\0\\1\end{bmatrix}
+b\begin{bmatrix}1\\1\\2\\0\end{bmatrix}
+c\left(
2\begin{bmatrix}1\\2\\0\\1\end{bmatrix}
-\begin{bmatrix}1\\1\\2\\0\end{bmatrix}
\right)
$$

$$
=
(a+2c)\begin{bmatrix}1\\2\\0\\1\end{bmatrix}
+(b-c)\begin{bmatrix}1\\1\\2\\0\end{bmatrix}.
$$
(ii) Unique representation?

$$
a\begin{bmatrix}1\\2\\0\\1\end{bmatrix}
+b\begin{bmatrix}1\\1\\2\\0\end{bmatrix}
=
c\begin{bmatrix}1\\2\\0\\1\end{bmatrix}
+d\begin{bmatrix}1\\1\\2\\0\end{bmatrix}
$$

$$
\Longrightarrow\ 
(a-c)\begin{bmatrix}1\\2\\0\\1\end{bmatrix}
+(b-d)\begin{bmatrix}1\\1\\2\\0\end{bmatrix}
=
\begin{bmatrix}0\\0\\0\\0\end{bmatrix}.
$$

If $\left\{\begin{bmatrix}1\\2\\0\\1\end{bmatrix},\begin{bmatrix}1\\1\\2\\0\end{bmatrix}\right\}$ is linearly independent, then the only way this equals $\mathbf{0}$ is
$$
a-c=0,\quad b-d=0
\quad\Longrightarrow\quad
a=c,\ b=d.
$$



So a [[basis]] allows us to analyze the same linear system and preserve it's identity

This lecture is about general properties of vector spaces and their bases 
After facts about bases of Rn and bases of subspaces of Rn

Only to later generalize those facts to all vector spaces that have finite bases



## Observations

1. If $B=\{\mathbf{u}_1,\ldots,\mathbf{u}_k\}$ is a [[basis]] of $V$, then $\mathbf{u}_1,\ldots,\mathbf{u}_k$ are **linearly independent** if the only way to make it homgenous is for their linear combination to be equal to 0 only where the coefficents are =0 aka the trivial solution

Because: a [[basis]] gives **unique representation** (the vectors when combined will not cancel out due to equivalence), so the only way
$$
c_1\mathbf{u}_1+\cdots+c_k\mathbf{u}_k=\mathbf{0}
$$
can happen is if $c_1=\cdots=c_k=0$.

---

2. If $V=\operatorname{span}(\mathbf{u}_1,\ldots,\mathbf{u}_k)$ and $\mathbf{u}_1,\ldots,\mathbf{u}_k$ are **linearly independent**, then
$$
B=\{\mathbf{u}_1,\ldots,\mathbf{u}_k\}
$$
is a [[basis]] of $V$.

Because (uniqueness): if
$$
c_1\mathbf{u}_1+\cdots+c_k\mathbf{u}_k
=
d_1\mathbf{u}_1+\cdots+d_k\mathbf{u}_k,
$$
then
$$
(c_1-d_1)\mathbf{u}_1+\cdots+(c_k-d_k)\mathbf{u}_k=\mathbf{0}
\Longrightarrow
c_i-d_i=0\ \text{for all }i
\Longrightarrow
c_i=d_i.
$$

---

## Definition: $B$-coordinates

If $B=\{\mathbf{u}_1,\ldots,\mathbf{u}_k\}$ is a [[basis]] of $V$, then for any $\mathbf{v}\in V$ there exist **unique** scalars $c_1,\ldots,c_k$ such that
$$
\mathbf{v}=c_1\mathbf{u}_1+\cdots+c_k\mathbf{u}_k.
$$
The scalars $(c_1,\ldots,c_k)$ are the **$B$-coordinates** of $\mathbf{v}$

The b-coordinate is precisely 
$$  
[\mathbf{v}]_B=  
\begin{bmatrix}  
c_1\\  
\vdots\\  
c_k  
\end{bmatrix}.  
$$  
  
Example: $x_1,\ldots,x_n$ are the **standard coordinates** of  
$$  
\begin{bmatrix}  
x_1\\  
\vdots\\  
x_n  
\end{bmatrix}\in\mathbb{R}^n  
$$  
(coordinates with respect to $\{\mathbf{e}_1,\ldots,\mathbf{e}_n\}$).
THIS WILL BE IMPORTANT LATER ON!!!

And because this is for a finite [[basis]] that means that the B-coordinate vector can be written as a column vector of scalars

[[Coordinate vector]]

The great thing about having a [[basis]] is that once you get a [[basis]] you automatically can think of it as Rk vector space V is that once you have the [[basis]] even though we may not know the vector space V which v_b belongs to as a subset of v a subspace of V

Sometimes we'll need to get different bases to answer different questions

IF Finite [[basis]] V a vector space is finite dimensional

Otherise V is infinite dimensional

If V is finite-dimensional, then every [[basis]] of V has the same number of vectors. dimension of V dim V

---
If $V=\operatorname{span}(\mathbf{v}_1,\ldots,\mathbf{v}_k)$ and $\{\mathbf{u}_1,\ldots,\mathbf{u}_\ell\}\subseteq V$ are linearly independent, then $k\ge \ell$.

Justification (clean + short):

Since $V=\operatorname{span}(\mathbf{v}_1,\ldots,\mathbf{v}_k)$, every $\mathbf{u}_j$ can be written as a linear combination of the $\mathbf{v}_i$’s.  
Define a linear map
$$
T:\mathbb{R}^k\to V,\qquad
T(\mathbf{c})=c_1\mathbf{v}_1+\cdots+c_k\mathbf{v}_k.
$$
$T$ is onto (surjective) because its outputs are exactly $\operatorname{span}(\mathbf{v}_1,\ldots,\mathbf{v}_k)=V$.

Pick $\mathbf{c}^{(j)}\in\mathbb{R}^k$ with $T(\mathbf{c}^{(j)})=\mathbf{u}_j$ for each $j=1,\ldots,\ell$.

If there were a nontrivial relation in $\mathbb{R}^k$:
$$
\alpha_1\mathbf{c}^{(1)}+\cdots+\alpha_\ell\mathbf{c}^{(\ell)}=\mathbf{0},
$$
apply $T$:
$$
\alpha_1\mathbf{u}_1+\cdots+\alpha_\ell\mathbf{u}_\ell
=T(\mathbf{0})=\mathbf{0}.
$$
But $\mathbf{u}_1,\ldots,\mathbf{u}_\ell$ are linearly independent, so $\alpha_1=\cdots=\alpha_\ell=0$.

So $\mathbf{c}^{(1)},\ldots,\mathbf{c}^{(\ell)}$ are linearly independent vectors in $\mathbb{R}^k$.  
But $\mathbb{R}^k$ can’t contain more than $k$ linearly independent vectors, so $\ell\le k$.

---

15/

Observation

$\dim(\mathbb{R}^n)=n$ because $\{\mathbf{e}_1,\ldots,\mathbf{e}_n\}$ is a [[basis]].

Fact 2

If $\{\mathbf{v}_1,\ldots,\mathbf{v}_n\}$ are linearly independent in $\mathbb{R}^n$, then $\{\mathbf{v}_1,\ldots,\mathbf{v}_n\}$ is a basis of $\mathbb{R}^n$.

---

16/

Because

linearly independent
$\Longrightarrow\ c_1\mathbf{v}_1+\cdots+c_n\mathbf{v}_n=\mathbf{0}$ has unique solution (only $c_i=0$)

$\Longrightarrow\ [\mathbf{v}_1\ \cdots\ \mathbf{v}_n]\mathbf{c}=\mathbf{0}$ has only the trivial solution

Let $A=[\mathbf{v}_1\ \cdots\ \mathbf{v}_n]\in\mathbb{R}^{n\times n}$.

Only trivial solution
$\Longrightarrow\ A$ has a pivot in every column
$\Longrightarrow\ \operatorname{rref}(A)=I_n$

So
$$
\operatorname{rref}\!\left([A\mid \mathbf{0}]\right)=
\left[\begin{array}{ccc|c}
1&\cdots&0&0\\
\vdots&\ddots&\vdots&\vdots\\
0&\cdots&1&0
\end{array}\right]
$$

and for any $\mathbf{b}\in\mathbb{R}^n$,
$$
\operatorname{rref}\!\left([A\mid \mathbf{b}]\right)=
\left[\begin{array}{ccc|c}
1&\cdots&0&a_1\\
\vdots&\ddots&\vdots&\vdots\\
0&\cdots&1&a_n
\end{array}\right]
$$
(where the $a_i$ are the unique solution coordinates)

---

17/

So for every $\mathbf{b}\in\mathbb{R}^n$,
$$
A\mathbf{x}=\mathbf{b}
\quad\text{has a unique solution.}
$$

That means every $\mathbf{b}$ can be written uniquely as
$$
\mathbf{b}=a_1\mathbf{v}_1+\cdots+a_n\mathbf{v}_n.
$$

INTERPRETATION: in $\mathbb{R}^n$, if you already have $n$ linearly independent vectors, there is “no room left” for them to fail to span, so they automatically span all of $\mathbb{R}^n$ and therefore form a basis.




ALL BASES OF A FINITE DIMENSIONAL VECTOR SPACE HAVE THE EXACT SAME SIZE AND THATS WHAT WE CALL THE DIMENSION OF THE VECTOR SPACE

So if we know a set of n vectors are linearly independent in Rn  then those vectors form a [[basis]] of Rn

And if that's true then we can use the identity of linear independence to add on cv + --- + cv = 0

Which because 0 means arbitrary we can also say that therefore rref we can also reduce it to vector b

## Observation

$$  
\dim(\mathbb{R}^n)=n  
\quad\text{because}\quad  
{e_1,\dots,e_n}\ \text{is a basis of } \mathbb{R}^n.  
$$  
(A [[basis]] has as many vectors as the dimension.) ([MIT OpenCourseWare](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/resources/lecture-9-independence-[[basis]]-and-dimension/?utm_source=chatgpt.com "Lecture 9: Independence, basis, and dimension | Linear ..."))

---

## Fact 2

> If ${v_1,\dots,v_n}$ are **linearly independent** in $\mathbb{R}^n$, then ${v_1,\dots,v_n}$ is a **basis** of $\mathbb{R}^n$. ([MIT OpenCourseWare](https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/0bbc30e3f1d7933ea07a2d2e9ab050d9_MIT18_06SCF11_Ses1.9sum.pdf?utm_source=chatgpt.com "Lecture 9: Independence, basis, and dimension"))

---

## Culmination: why linear independence forces “basis” in $\mathbb{R}^n$

Let  
$$  
A=\big[,v_1\ \cdots\ v_n,\big]\in\mathbb{R}^{n\times n}.  
$$

### 1) Independence $\Longleftrightarrow$ unique solution to the homogeneous system

$$  
{v_1,\dots,v_n}\ \text{is linearly independent}  
\iff  
c_1v_1+\cdots+c_nv_n=\mathbf 0\ \text{has only }c=\mathbf 0.  
$$  
Equivalently,  
$$  
Ac=\mathbf 0 \ \text{has the unique solution }c=\mathbf 0.  
$$  
So the augmented matrix reduces to  
$$  
\operatorname{rref}!\big([A\mid \mathbf 0]\big)=\big[I\mid \mathbf 0\big].  
$$  
### 2) Then every right-hand side is solvable (so the columns span $\mathbb{R}^n$)

Since $\operatorname{rref}(A)=I$, for **any** $b\in\mathbb{R}^n$ the system $Ax=b$ has a (in fact unique) solution, i.e.  
$$  
\forall, b\in\mathbb{R}^n,\ \exists,x\in\mathbb{R}^n \text{ such that } Ax=b.  
$$  
That statement is exactly: the columns $v_1,\dots,v_n$ **span** $\mathbb{R}^n$.
### 3) Conclusion

They are

- linearly independent, and
    
- spanning $\mathbb{R}^n$,
    

so ${v_1,\dots,v_n}$ is a **basis** of $\mathbb{R}^n$. 

"Find coord. vector of x with respect to the basis" is then asking

Find the unique linear combination of the basis to find the vector x

This is called a [[vector equation]]

Here’s the **scraped + Obsidian-ready** version (Markdown + LaTeX).

---

## 18) Example

Let

$$  
u_1=\begin{bmatrix}1\2\1\0\end{bmatrix},\quad  
u_2=\begin{bmatrix}1\1\0\3\end{bmatrix},\quad  
u_3=\begin{bmatrix}0\2\1\1\end{bmatrix},\quad  
u_4=\begin{bmatrix}1\0\1\2\end{bmatrix}.  
$$

Form the matrix with these as **columns**:

# $$  
A=\big[u_1\ u_2\ u_3\ u_4\big]

\begin{bmatrix}  
1&1&0&1\  
2&1&2&0\  
1&0&1&1\  
0&3&1&2  
\end{bmatrix}.  
$$

Row-reduction (shown in the notes) gives an echelon form with a pivot in **every column**, e.g.

$$  
\sim  
\begin{bmatrix}  
1&1&0&1\  
0&-1&2&-2\  
0&0&-1&2\  
0&0&0&10  
\end{bmatrix}.  
$$

So the columns are linearly independent (\Rightarrow) ({u_1,u_2,u_3,u_4}) **forms a basis** of (\mathbb{R}^4).

---

## 19) Coordinates of (x) in the basis (B)

Find the coordinate vector of

$$  
x=\begin{bmatrix}1\2\3\4\end{bmatrix}  
$$

with respect to the basis

$$  
B=\left{  
\begin{bmatrix}1\2\1\0\end{bmatrix},  
\begin{bmatrix}1\1\0\3\end{bmatrix},  
\begin{bmatrix}0\2\1\1\end{bmatrix},  
\begin{bmatrix}1\0\1\2\end{bmatrix}  
\right}.  
$$

Solve (Ac=x) (augment and row-reduce):

# $$  
\left[;A\mid x;\right]

\left[  
\begin{array}{cccc|c}  
1&1&0&1&1\  
2&1&2&0&2\  
1&0&1&1&3\  
0&3&1&2&4  
\end{array}  
\right]  
\sim  
\left[  
\begin{array}{cccc|c}  
1&0&0&0&-0.1\  
0&1&0&0&-0.4\  
0&0&1&0&1.6\  
0&0&0&1&1.3  
\end{array}  
\right].  
$$

Therefore,

# $$  
[x]_B

\begin{bmatrix}  
-0.1\  
-0.4\  
1.6\  
1.3  
\end{bmatrix}.  
$$

---

_(Obsidian’s standard math delimiters are inline `$...$` and display `$$...$$`.)_ ([forum.obsidian.md](https://forum.obsidian.md/t/allow-for-custom-math-delimiter/105128?utm_source=chatgpt.com "Allow for custom math delimiter - Feature requests - Obsidian Forum"))

## 18) Example

Let

$$  
u_1=\begin{bmatrix}1\2\1\0\end{bmatrix},\quad  
u_2=\begin{bmatrix}1\1\0\3\end{bmatrix},\quad  
u_3=\begin{bmatrix}0\2\1\1\end{bmatrix},\quad  
u_4=\begin{bmatrix}1\0\1\2\end{bmatrix}.  
$$

Form the matrix with these vectors as **columns**:

# $$  
A=\big[u_1\ u_2\ u_3\ u_4\big]

\begin{bmatrix}  
1&1&0&1\  
2&1&2&0\  
1&0&1&1\  
0&3&1&2  
\end{bmatrix}.  
$$

Row-reducing (one possible echelon form shown in the notes):

$$  
A \sim  
\begin{bmatrix}  
1&1&0&1\  
0&-1&2&-2\  
0&0&-1&2\  
0&0&0&10  
\end{bmatrix}.  
$$

There is a pivot in **every column** (\Rightarrow) the columns are linearly independent (\Rightarrow) since there are (4) independent vectors in (\mathbb{R}^4), they form a **basis** of (\mathbb{R}^4). ([Math Textbooks](https://textbooks.math.gatech.edu/ila/invertible-matrix-thm.html?utm_source=chatgpt.com "The Invertible Matrix Theorem"))

---

## 19) Coordinate vector with respect to the basis

Find the coordinate vector of

$$  
x=\begin{bmatrix}1\2\3\4\end{bmatrix}  
$$

with respect to the basis

$$  
\mathcal B={u_1,u_2,u_3,u_4}.  
$$

Solve (Ac=x) (augment and row-reduce):

# $$  
\left[;A\mid x;\right]

\left[  
\begin{array}{cccc|c}  
1&1&0&1&1\  
2&1&2&0&2\  
1&0&1&1&3\  
0&3&1&2&4  
\end{array}  
\right]  
\sim  
\left[  
\begin{array}{cccc|c}  
1&0&0&0&-0.4\  
0&1&0&0&-0.4\  
0&0&1&0&1.6\  
0&0&0&1&1.8  
\end{array}  
\right].  
$$

So the coordinate vector is

# $$  
[x]_{\mathcal B}

# \begin{bmatrix}  
-0.4\  
-0.4\  
1.6\  
1.8  
\end{bmatrix}

\begin{bmatrix}  
-\frac25\  
-\frac25\  
\frac85\  
\frac95  
\end{bmatrix}.  
$$

(General fact: finding ([v]_{\mathcal B}) is exactly solving the linear system whose columns are the basis vectors.) ([Oklahoma State University Mathematics](https://math.okstate.edu/people/binegar/3013/3013-l15.pdf?utm_source=chatgpt.com "Coordinatization and Change of Basis"))

Every nontrivial susbapce has a basis with 1<k<n vectors

Linear independence 