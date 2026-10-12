---
type: lecture
parent: "[[Nicholson]]"
domain: math
status: draft
---
## Lecture 3

Main learnings

1
- We have Guassian Elim
	- We can show that we get the same solutions row reducing matrix A to Matrix B bc we can undo every step
- Therefore every solution of S_B is also a solution of S_A

2
Any system related by row operations always have the same solutions

3
If we can show A|b and B|c are row equivalent then the systems S_a and S_b are equivalent systems

4
When you reduce an augmented matrix to RREF 3 things can happen

i. No sols in 0=1
ii. x=d_1,x=d_2 unique sols.
iii. no pivot nor contradiction 0=0
5
**RANK**
The # of pivots in RREF
The # of linearly independent rows
If A is an m x n matrix, then you'll always have less or an equal rank than the lowest value of the min of an mxn matrix

formally: $rank(A)≤min(m,n)$

6
HOMOGENOUS
If all constant terms are 0

7
CONSISTENT
has at least one solution
8
HOMOGENOUS SYSTEMS have solutions
bc how can you get Ax=0 and then Ax=1???
9
Trivial solution is when you plug x=0 into Ax=b and get Ax=0 automatically. It's trivial bc it says nothing about a homogenous matrix
10


Homogenous solutions automatically get the trivial solution but sometimes also get infinitely many if the rank < min(m,n)

11
[[Linear combination]]
As mentioned we will spend most of the time focusing on the combination of vectors in R^n and scalars in R (note no n because they must all be of the same order)

12 

If there were vectors u and v that were both solutions of a homogenous system with a coefficent matrix then for

13 
Just like alternate forms of the same matrix are = any solutions of a homogenous matrix are all =0 in Ax=0 such that if n and u are sols they are linear combinations of one another 
14
Fundemental set of solutions
**Definition (basic / fundamental set of solutions).**  
The vectors $u_1,u_2,\ldots,u_k$ form a basic (fundamental) set of solutions of a **homogeneous** linear system (i.e., $Ax=0$) if:

1. **Closure (any combination stays a solution):**  
   For any scalars $c_1,\ldots,c_k\in\mathbb{R}$, the vector  
   $c_1u_1+\cdots+c_ku_k$ is also a solution of $Ax=0$.

2. **Spanning + uniqueness (every solution comes from them, one way only):**  
   For every solution $x$ of $Ax=0$, there exist scalars $c_1,\ldots,c_k\in\mathbb{R}$ such that  
   $x=c_1u_1+\cdots+c_ku_k$,  
   and this representation is **unique** (no other choice of $c_1,\ldots,c_k$ gives the same $x$).


Gaussian elimination, continued  
• Example.  
• Row operations and equivalence.  
• Reading the RREF of an augmented matrix.  
° Rank of a matrix.  
• Linear combinations.  
• Homogeneous systems.  
° Basic sets of solutions.

---

## Example: solve the system

$$  
\begin{aligned}  
w-x+y-2z&=1\  
-w+x+y+z&=-1\  
-w+2x+3y-z&=2\  
w-x+2y+z&=1  
\end{aligned}  
$$

Augmented matrix:

$$  
\left[\begin{array}{rrrr|r}  
1&-1&1&-2&1\  
-1&1&1&1&-1\  
-1&2&3&-1&2\  
1&-1&2&1&1  
\end{array}\right]  
$$

---

## Elimination steps

$$  
\left[\begin{array}{rrrr|r}  
1&-1&1&-2&1\  
0&0&2&-1&0\  
-1&2&3&-1&2\  
1&-1&2&1&1  
\end{array}\right]  
$$

$$  
\left[\begin{array}{rrrr|r}  
1&-1&1&-2&1\  
0&0&2&-1&0\  
0&1&4&-3&3\  
1&-1&2&1&1  
\end{array}\right]  
$$

$$  
\left[\begin{array}{rrrr|r}  
1&-1&1&-2&1\  
0&0&2&-1&0\  
0&1&4&-3&3\  
0&0&1&3&0  
\end{array}\right]  
$$

$$  
\left[\begin{array}{rrrr|r}  
1&-1&1&-2&1\  
0&1&4&-3&3\  
0&0&1&3&0\  
0&0&2&-1&0  
\end{array}\right]  
$$

---

## Finish to RREF and solution

$$  
\left[\begin{array}{rrrr|r}  
1&-1&1&-2&1\  
0&1&4&-3&3\  
0&0&1&3&0\  
0&0&0&-7&0  
\end{array}\right]  
\rightarrow  
\left[\begin{array}{rrrr|r}  
1&-1&1&-2&1\  
0&1&4&-3&3\  
0&0&1&3&0\  
0&0&0&1&0  
\end{array}\right]  
$$

$$  
\left[\begin{array}{rrrr|r}  
1&-1&1&0&1\  
0&1&4&0&3\  
0&0&1&0&0\  
0&0&0&1&0  
\end{array}\right]  
\rightarrow  
\left[\begin{array}{rrrr|r}  
1&0&0&0&4\  
0&1&0&0&3\  
0&0&1&0&0\  
0&0&0&1&0  
\end{array}\right]  
$$

$$  
w=4,\quad x=3,\quad y=0,\quad z=0  
$$

---

## Claim 1

System $S_A \rightarrow [A\mid b] \rightarrow [B\mid c] \rightarrow S_B$

then $S_A$ and $S_B$ have the same solutions.

---

## Because

1. Every solution of $S_A$ is a solution of $S_B$
    
2. EROs are reversible by EROs
    
3. Every solution of $S_B$ is a solution of $S_A$
    

---

## Observation 1

If System A $\xrightarrow{\text{ERO}}$ System B, then every solution of $S_A$ is also a solution of $S_B$.

Because:

If ERO…

(i) … is a swap $\rightarrow$ Same equations.

---

## (ii) scaling

(ii) … is a scaling: $\alpha R_i \to R_i$

$\rightarrow$ Equations are the same except $R_i$:

$S_A:\ a_{i1}x_1+\cdots+a_{in}x_n=b_i$

$S_B:\ \alpha a_{i1}x_1+\cdots+\alpha a_{in}x_n=\alpha b_i$

$$  
=\alpha(a_{i1}x_1+\cdots+a_{in}x_n)=\alpha b_i  
$$

If $(u_1,\ldots,u_n)$ satisfies $S_A$ then it also satisfies $S_B$.

---

## (iii) replacement

(iii) … is a replacement: $R_i+\alpha R_j\to R_i$

$\rightarrow$ Equations are the same except $R_i$:

$S_A:\ a_{i1}x_1+\cdots+a_{in}x_n=b_i$

$$  
S_B:\ (a_{i1}+\alpha a_{j1})x_1+\cdots+(a_{in}+\alpha a_{jn})x_n=b_i+\alpha b_j  
$$

$$  
(a_{i1}x_1+\cdots+a_{in}x_n)+\alpha(a_{j1}x_1+\cdots+a_{jn}x_n)=b_i+\alpha b_j  
$$

If $(u_1,\ldots,u_n)$ satisfies $S_A$, then  
$a_{i1}u_1+\cdots+a_{in}u_n=b_i$, and  
$\alpha(a_{j1}u_1+\cdots+a_{jn}u_n)=\alpha b_j$,  
$\rightarrow (u_1,\ldots,u_n)$ satisfies $S_B$.

---

## Observation 2

EROs are reversible by EROs

To reverse…

(i) $R_i \leftrightarrow R_j$, do it again.  
(ii) $\alpha R_i \to R_i$, do $\alpha^{-1}R_i \to R_i$ $(\alpha\neq 0)$.  
(iii) $R_i+\alpha R_j\to R_i$, do $R_i-\alpha R_j\to R_i$.

---

## Definition

Matrices $A$ and $B$ are row equivalent if

$$  
A \xrightarrow{\text{ERO}_1} A_1 \xrightarrow{\text{ERO}_2} A_2 \xrightarrow{\text{ERO}_3} \cdots \xrightarrow{\text{ERO}_m} B  
$$

Conclusion:

Augmented matrices $[A\mid b]$ and $[B\mid c]$ row equivalent $\Rightarrow$ Systems $S_A, S_B$ are equivalent, same solutions.

---

## Reading $\mathrm{rref}([A\mid b])$

$$  
\begin{aligned}  
a_{11}x_1+a_{12}x_2+\cdots+a_{1n}x_n&=b_1\\
a_{21}x_1+a_{22}x_2+\cdots+a_{2n}x_n&=b_2\\  
&\vdots\\  
a_{m1}x_1+a_{m2}x_2+\cdots+a_{mn}x_n&=b_m  
\end{aligned}  
$$

$$  
\left[\begin{array}{cccc|c}  
a_{11}&a_{12}&\cdots&a_{1n}&b_1\\  
a_{21}&a_{22}&\cdots&a_{2n}&b_2\\  
\vdots&\vdots&\ddots&\vdots&\vdots\\  
a_{m1}&a_{m2}&\cdots&a_{mn}&b_m  
\end{array}\right]=[A\mid b]  
$$

---

## Three possibilities

### (i) Pivot in the last column

row $j:\ [0\ 0\ \cdots\ 0\ 1]$

(new) equation $j$:

$$  
0\cdot x_1+0\cdot x_2+\cdots+0\cdot x_n=1 \Rightarrow 0=1  
$$

$\rightarrow$ No solutions

---

### (ii) Unique solution case

$$  
\mathrm{rref}([A\mid b])=  
\left[\begin{array}{cccc|c}  
1&0&\cdots&0&d_1\\  
0&1&\cdots&0&d_2\\  
\vdots&\vdots&\ddots&\vdots&\vdots\\  
0&0&\cdots&1&d_n\\  
0&0&\cdots&0&0\\  
\vdots&\vdots&&\vdots&\vdots  
\end{array}\right]  
$$

transformed system:

$$  
\begin{aligned}  
x_1&=d_1\\  
x_2&=d_2\\  
&\vdots\\  
x_n&=d_n  
\end{aligned}  
$$

unique solution

---

### (iii) Infinitely many solutions case

No pivot in col. $k$ ($\le n=$ # of cols in coeff. matrix $=$ # variables)

$\rightarrow x_k$ is free

$\rightarrow$ Infinitely many solutions.

---

## Rank

1. The [[Rank|Rank of a matrix]] of a matrix is the number of pivots in its reduced row echelon form  
    = # of pivots in original matrix.
    

$A$ is $m\times n$

$$  
\mathrm{rank}(A)\le \min(m,n)  
$$

---

## Homogeneous systems

2. A linear system is homogeneous if all the constant terms are 0:


$$  
\begin{aligned}  
a_{11}x_1+a_{12}x_2+\cdots+a_{1n}x_n&=0\\  
a_{21}x_1+a_{22}x_2+\cdots+a_{2n}x_n&=0\\  
&\vdots\\  
a_{m1}x_1+a_{m2}x_2+\cdots+a_{mn}x_n&=0  
\end{aligned}  
$$
There will always be one solution

---

## Observations

Observations

1. Every homogeneous system is consistent, has solutions
    

Because:

(i) $\mathrm{rref}([A\mid 0])=[\mathrm{rref}(A)\mid 0]$ zero vector … no pivot

or:

(ii) $x_1=x_2=\cdots=x_n=0$ is a solution

---

## “Trivia” about rank and solutions

$A=$ coeff. matrix of a homog. system of $m$ equations in $n$ variables, $A$ is $m\times n$

If… “trivia”

(i) $\mathrm{rank}(A)=n$ solution “unique solution $u=0$”  
(ii) $\mathrm{rank}(A)=k<n$  
$n-k$ free variables  
infinitely many sol(s).

---

## Linear combination

$x_1,x_2,\ldots,x_n$: vectors in $\mathbb{R}^m$  
$a_1,a_2,\ldots,a_n$: scalars in $\mathbb{R}$

$$  
a_1x_1+a_2x_2+\cdots+a_nx_n  
$$

is a [[Linear combination]] of $x_1,x_2,\ldots,x_n$

---

## Observation

If $u$ and $v$ are both solutions of the [[homogeneous]] system with coeff. matrix $A=[a_{ij}]$, then every linear combination of $u$ and $v$ is also a solution.

Because, for any $s,t\in\mathbb{R}$:

$$  
\begin{aligned}  
a_{i1}(su_1+tv_1)+\cdots+a_{in}(su_n+tv_n)  
&=s(a_{i1}u_1+\cdots+a_{in}u_n)+t(a_{i1}v_1+\cdots+a_{in}v_n)\  
&=s\cdot 0+t\cdot 0\  
&=0  
\end{aligned}  
$$

So $su+tv$ is also a solution.

---

## Example: describe the set of solutions

$$  
\begin{aligned}  
a+2b+c-d&=0\  
b+3c+2d&=0\  
2a+3b-c-4d&=0\  
a+4b+7c+3d&=0  
\end{aligned}  
$$

Set of solutions:

$$  
\begin{aligned}  
a&=5u+5v\  
b&=-3u-2v\  
c&=u\  
d&=v  
\end{aligned}  
$$

with parameters $u\in\mathbb{R}$, $v\in\mathbb{R}$.

Vector form:

$$  
\left[\begin{array}{c}  
a\\  
b\\  
c\\  
d  
\end{array}\right]

u\left[\begin{array}{c}  
5\\  
-3\\  
1\\  
0\\  
\end{array}\right]  
+  
v\left[\begin{array}{c}  
5\\  
-2\\
0\\  
1  
\end{array}\right]  
$$

---

## Definition: basic (fundamental) set of solutions

$u_1,u_2,\ldots,u_p$ is a [[basic]], aka fundamental set of solutions of the homogeneous linear system

$$  
\begin{aligned}  
a_{11}x_1+\cdots+a_{1n}x_n&=0\  
&\vdots\  
a_{m1}x_1+\cdots+a_{mn}x_n&=0  
\end{aligned}  
$$

if…

(i) $u_1,u_2,\ldots,u_p$ are solutions of the system  
(ii) every solution of the system has a unique representation as a linear combination of $u_1,u_2,\ldots,u_p$