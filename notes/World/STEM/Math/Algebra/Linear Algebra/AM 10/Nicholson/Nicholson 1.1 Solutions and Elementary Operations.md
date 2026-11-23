---
type: concept
parent: "[[Nicholson]]"
domain: math
status: draft
---
# Reading and Notes
## 1.1.1
### 1.1.1.a The Significance of Linear Algebra
> Practical problems in many fields of study--such as biology, business, chemistry, computer science, economics, electronics, engineering, physics and the social sciences--can often be reduced to solving a system of linear equations. Linear algebra arose from attempts to find systematic methods for solving these systems, so it is natural to begin this book by studying linear equations.

tldr; STEM can be reduced to solving a [[Systems (math)|system]] of [[linear equation|linear equations]]. 

Linear algebra arose from attempts to find [[Systems (math)|systemic]] methods for solving these [[Systems (math)]], so 

### 1.1.1.d.1 New Definition Of A Linear Equation

>If $a$, $b$, and $c$ are real numbers, the graph of an equation of the form

**NOTE: THIS IS NOT Y=MX+B (THE AFFINE FUNCTION) OF GEOMETRIC LINEARITY FROM HIGHSCHOOL.**

$$  
ax + by = c  
$$

>is a straight line (if $a$ and $b$ are not both zero), so such an equation is called a [[linear equation#2.1 School algebra (one or two variables)|linear equation]] *in the variables $x$ and $y$*. However, it is often convenient to write the variables as $x_1, x_2, \ldots, x_n$, particularly when more than two variables are involved. An equation of the form
$$  
a_1x_1 + a_2x_2 + \cdots + a_nx_n = b  
$$

>is called a _[[linear equation#2.2 Many variables and linear algebra|linear equation]]_ in the $n$ variables $x_1, x_2, \ldots, x_n$. Here $a_1, a_2, \ldots, a_n$ denote real numbers (called the **[[coefficients]]** of $x_1, x_2, \ldots, x_n$, respectively) and $b$ is also a number (called the **[[constant term]]** of the equation). 
### 1.1.1.d.2 System of Linear Equation
>A finite collection of linear equations in the variables $x_1, x_2, \ldots, x_n$ is called a **[[Systems (math)|system]] of [[linear equation#linear equation vs system of linear equations|linear equation]]s** in these variables. Hence,

$$  
2x_1 - 3x_2 + 5x_3 = 7  
$$

>is a linear equation; the coefficients of $x_1$, $x_2$, and $x_3$ are $2$, $-3$, and $5$, and the constant term is $7$. **Note that each variable in a linear equation occurs to the first power only.**
## 1.1.2
1.1.2
>Given a linear equation $a_1x_1 + a_2x_2 + \cdots + a_nx_n = b$, a sequence $s_1, s_2, \ldots, s_n$ of $n$ numbers is called a **[[Solution to a system of equations|solution]]** to the equation if

$$  
a_1s_1 + a_2s_2 + \cdots + a_ns_n = b  
$$

>that is, if the equation is satisfied when the substitutions $x_1 = s_1$, $x_2 = s_2$, $\ldots$, $x_n = s_n$ are made. A sequence of numbers is called a **solution** to a **system** of equations if it is a solution to every equation in the system.
## 1.1.3
1.1.3.ex
>For example, $x = -2$, $y = 5$, $z = 0$ and $x = 0$, $y = 4$, $z = -1$ are both solutions to the system

$$  
\begin{cases}  
x + y + z = 3 \\  
2x + y + 3z = 1  
\end{cases}  
$$
1.1.3.i
>A system may have no solution at all, or it may have a unique solution, or it may have an infinite family of solutions. For instance, the system $x + y = 2$, $x + y = 3$ has no solution because the sum of two numbers cannot be $2$ and $3$ simultaneously. A system that has no solution is called **[[inconsistent system|inconsistent]]**; a system with at least one solution is called **[[consistent system|consistent]]**. The system in the following example has infinitely many solutions.

tldr; **[[Systems of Linear Equations]] can have $\infty$, none, a or multiple solution/s**

If sol. consistent, in no sol. inconsistent
## 1.1.4
### 1.1.4.ex (ex 1.1.1)

>Show that, for arbitrary values of (s) and (t),  
>$$ 
\begin{aligned}  
x_1 &= t - s + 1 \\  
x_2 &= t + s + 2 \\  
x_3 &= s \\  
x_4 &= t  
\end{aligned}  
$$  
>is a solution to the system  
>$$
\begin{aligned}  
x_1 - 2x_2 + 3x_3 + x_4 &= -3 \\  
2x_1 - x_2 + 3x_3 - x_4 &= 0 .  
\end{aligned}  
$$

>Solution. Simply substitute these values of ($x_1, x_2, x_3$,) and ($x_4$) in each equation.  
>$$ 
\begin{aligned}  
x_1 - 2x_2 + 3x_3 + x_4  
&= (t - s + 1) - 2(t + s + 2) + 3s + t = -3, \\  
2x_1 - x_2 + 3x_3 - x_4  
&= 2(t - s + 1) - (t + s + 2) + 3s - t = 0.  
\end{aligned}  
$$  
>Because both equations are satisfied, it is a solution for all choices of (s) and (t).
## 1.1.5
>The quantities (s) and (t) in Example 1.1.1 are called **[[parameters]]**, and the set of solutions, described in this way, is said to be given in **[[parametric form]]** and is called the **[[general solution]]** to the system. It turns out that the solutions to every system of equations (if there are solutions) can be given in parametric form (that is, the variables ($x_1, x_2, \ldots$) are given in terms of new independent variables (s, t,) etc.). The following example shows how this happens in the simplest systems where only one equation is present.

---

### 1.1.5.ex (ex.1.1.2)

Describe all solutions to (3x - y + 2z = 6) in [[parametric form]].

Solution. Solving the equation for (y) in terms of (x) and (z), we get  $y = 3x + 2z - 6$  
If (s) and (t) are arbitrary then, setting (x = s, z = t), we get solutions  
$$\begin{aligned}  
x &= s, \\  
y &= 3s + 2t - 6 \quad & s \text{ and } t \text{ arbitrary}, \\  
z &= t.  
\end{aligned}  $$


Of course we could have solved for (x):  
$x = \tfrac{1}{3}(y - 2z + 6)$  
Then, if we take (y = p, z = q), the solutions are represented as follows:   
$$\begin{aligned}  
x &= \tfrac{1}{3}(p - 2q + 6), \\  
y &= p \quad & p \text{ and } q \text{ arbitrary}, \\  
z &= q.  
\end{aligned}$$

The same family of solutions can “look” quite different!
## 1.1.6
When only two variables are involved, the solutions to systems of linear equations can be described geometrically because the graph of a linear equation  
$ax + by = c$ 
is a straight line if (a) and (b) are not both zero. Moreover, a point (P(s,t)) with coordinates (s) and (t) lies on the line if and only if (as + bt = c), that is, when (x = s, y = t) is a solution to the equation. Hence the solutions to a system of linear equations correspond to the points (P(s,t)) that lie on all of the lines in question.
## 1.1.7
In particular, if the system consists of just one equation, there must be infinitely many solutions because there are infinitely many points on a line. If the system has two equations, there are three possibilities for the corresponding straight lines:

1. The lines intersect at a single point. Then the system has a unique solution corresponding to that point.
    
2. The lines are parallel (and distinct) and so do not intersect. Then the system has no solution.
    
3. The lines are identical. Then the system has infinitely many solutions, one for each point on the (common) line.
    
## 1.1.8
These three situations are illustrated in Figure 1.1.1. In each case the graphs of two specific lines are plotted and the corresponding equations are indicated. In the last case, the equations are (3x - y = 4) and (-6x + 2y = -8), which have identical graphs.
## 1.1.9
With three variables, the graph of an equation  
$ax + by + cz = d$ 
can be shown to be a plane (see Section 4.2) and so again provides a “picture’’ of the set of solutions. However, this graphical method has its limitations: When more than three variables are involved, no physical image of the graphs (called hyperplanes) is possible. It is necessary to turn to a more “algebraic’’ method of solution.
## 1.1.10
Before describing the method, we introduce a concept that simplifies the computations involved. Consider the following system  
$$
\begin{aligned}  
3x_1 + 2x_2 - x_3 + x_4 &= -1 \\  
2x_1 \phantom{{}+ 2x_2} - x_3 + 2x_4 &= 0 \\  
3x_1 + x_2 + 2x_3 + 5x_4 &= 2  
\end{aligned} $$ 
of three equations in four variables. The array of numbers  
$$
\begin{bmatrix}  
3 & 2 & -1 & 1 & -1 \\  
2 & 0 & -1 & 2 & 0 \\  
3 & 1 & 2 & 5 & 2  
\end{bmatrix} $$
occurring in the system is called the _augmented matrix_ of the system. Each row of the matrix consists of the coefficients of the variables (in order) from the corresponding equation, together with the constant term.

_A rectangular array of numbers is called a matrix. Matrices will be discussed in more detail in Chapter 2._

For clarity, the constants are separated by a vertical line. The augmented matrix is just a different way of describing the system of equations. The array of coefficients of the variables

$$ 
\begin{bmatrix}  
3 & 2 & -1 & 1 \\  
2 & 0 & -1 & 2 \\  
3 & 1 & 2 & 5  
\end{bmatrix} $$

is called the **coefficient matrix** of the system and

$$
\begin{bmatrix}  
-1 \\[2pt]  
0 \\[2pt]  
2  
\end{bmatrix}  
$$

is called the **constant matrix** of the system.

---

## 1.1.11 Elementary Operations

The algebraic method for solving systems of linear equations is described as follows. Two such systems are said to be **equivalent** if they have the same set of solutions. A system is solved by writing a series of systems, one after the other, each equivalent to the previous system. Each of these systems has the same set of solutions as the original one; the aim is to end up with a system that is easy to solve. Each system in the series is obtained from the preceding system by a simple manipulation chosen so that it does not change the set of solutions.
## 1.1.12
As an illustration, we solve the system (x + 2y = -2,; 2x + y = 7) in this manner. At each stage, the corresponding augmented matrix is displayed. The original system is


$$\begin{aligned}  
x + 2y &= -2 \\  
2x + y &= 7  
\end{aligned}  
\qquad  
\left[  
\begin{array}{cc|c}  
1 & 2 & -2 \\  
2 & 1 & 7  
\end{array}  
\right]  $$

First, subtract twice the first equation from the second. The resulting system is

$$
\begin{aligned}  
x + 2y &= -2 \\  
-3y &= 11  
\end{aligned}  
\qquad  
\left[  
\begin{array}{cc|c}  
1 & 2 & -2 \\  
0 & -3 & 11  
\end{array}  
\right]  
$$

which is equivalent to the original (see Theorem 1.1.1). At this stage we obtain  
$y = -\frac{11}{3}$
by multiplying the second equation by (-\tfrac{1}{3}). The result is the equivalent system

$$\begin{aligned}  
x + 2y &= -2 \\  
y &= -\dfrac{11}{3}  
\end{aligned}  
\qquad  
\left[  
\begin{array}{cc|c}  
1 & 2 & -2 \\ 
0 & 1 & -\dfrac{11}{3}  
\end{array}  
\right]  $$

Finally, we subtract twice the second equation from the first to get another equivalent system.


$$\begin{aligned}  
x &= \dfrac{16}{3} \\  
y &= -\dfrac{11}{3}  
\end{aligned}  
\qquad  
\left[  
\begin{array}{cc|c}  
1 & 0 & \dfrac{16}{3} \\  
0 & 1 & -\dfrac{11}{3}  
\end{array}  
\right]$$

Now this system is easy to solve! And because it is equivalent to the original system, it provides the solution to that system.
## 1.1.13
Observe that, at each stage, a certain operation is performed on the system (and thus on the augmented matrix) to produce an equivalent system.

### 1.1.14.d (Definition 1.1 Elementary Operations)

The following operations, called elementary operations, can routinely be performed on systems of linear equations to produce equivalent systems.

I. Interchange two equations.

II. Multiply one equation by a nonzero number.

III. Add a multiple of one equation to a different equation.

---

### 1.1.14.t (Theorem 1.1.1)

Suppose that a sequence of elementary operations is performed on a system of linear equations. Then the resulting system has the same set of solutions as the original, so the two systems are equivalent.

The proof is given at the end of this section.
## 1.1.14
Elementary operations performed on a system of equations produce corresponding manipulations of the rows of the augmented matrix. Thus, multiplying a row of a matrix by a number (k) means multiplying every entry of the row by (k). Adding one row to another row means adding each entry of that row to the corresponding entry of the other row. Subtracting two rows is done similarly. Note that we regard two rows as equal when corresponding entries are the same.
## 1.1.15
In hand calculations (and in computer programs) we manipulate the rows of the augmented matrix rather than the equations. For this reason we restate these elementary operations for matrices.

---

### 1.1.16.d (Definition 1.2 Elementary Row Operations)

The following are called elementary row operations on a matrix.

I. Interchange two rows.

II. Multiply one row by a nonzero number.

III. Add a multiple of one row to a different row.
## 1.1.16
In the illustration above, a series of such operations led to a matrix of the form

$$ 
\begin{bmatrix}  
1 & 0 & * \\  
0 & 1 & *  
\end{bmatrix}  
$$

where the asterisks represent arbitrary numbers. In the case of three equations in three variables, the goal is to produce a matrix of the form

$$
\begin{bmatrix}  
1 & 0 & 0 & * \\  
0 & 1 & 0 & * \\  
0 & 0 & 1 & *  
\end{bmatrix}  $$

This does not always happen, as we will see in the next section. Here is an example in which it does happen.

### 1.1.17.ex Example 1.1.3

Find all solutions to the following system of equations.

[  
\begin{aligned}  
3x + 4y + z &= 1 \  
2x + 3y &= 0 \  
4x + 3y - z &= -2  
\end{aligned}  
]

Solution. The augmented matrix of the original system is

[  
\left[  
\begin{array}{rrr|r}  
3 & 4 & 1 & 1 \  
2 & 3 & 0 & 0 \  
4 & 3 & -1 & -2  
\end{array}  
\right].  
]

To create a 1 in the upper left corner we could multiply row 1 through by ( \tfrac13 ). However, the 1 can be obtained without introducing fractions by subtracting row 2 from row 1. The result is

[  
\left[  
\begin{array}{rrr|r}  
1 & 1 & 1 & 1 \  
2 & 3 & 0 & 0 \  
4 & 3 & -1 & -2  
\end{array}  
\right].  
]

The upper left 1 is now used to “clean up’’ the first column, that is create zeros in the other positions in that column. First subtract 2 times row 1 from row 2 to obtain

[  
\left[  
\begin{array}{rrr|r}  
1 & 1 & 1 & 1 \  
0 & 1 & -2 & -2 \  
4 & 3 & -1 & -2  
\end{array}  
\right].  
]

Next subtract 4 times row 1 from row 3. The result is

[  
\left[  
\begin{array}{rrr|r}  
1 & 1 & 1 & 1 \  
0 & 1 & -2 & -2 \  
0 & -1 & -5 & -6  
\end{array}  
\right].  
]

This completes the work on column 1. We now use the 1 in the second position of the second row to clean up the second column by subtracting row 2 from row 1 and then adding row 2 to row 3. For convenience, both row operations are done in one step. The result is

[  
\left[  
\begin{array}{rrr|r}  
1 & 0 & 3 & 3 \  
0 & 1 & -2 & -2 \  
0 & 0 & -7 & -8  
\end{array}  
\right].  
]

Note that the last two manipulations did not affect the first column (the second row has a zero there), so our previous effort there has not been undermined. Finally we clean up the third column. Begin by multiplying row 3 by (-\tfrac17) to obtain

[  
\left[  
\begin{array}{rrr|r}  
1 & 0 & 3 & 3 \  
0 & 1 & -2 & -2 \  
0 & 0 & 1 & \tfrac87  
\end{array}  
\right].  
]

Now subtract 3 times row 3 from row 1, and then add 2 times row 3 to row 2 to get

[  
\left[  
\begin{array}{rrr|r}  
1 & 0 & 0 & -\tfrac37 \  
0 & 1 & 0 & \tfrac27 \  
0 & 0 & 1 & \tfrac87  
\end{array}  
\right].  
]

The corresponding equations are (x = -\tfrac37), (y = \tfrac27), and (z = \tfrac87), which give the (unique) solution.
## 1.1.17
Every elementary row operation can be reversed by another elementary row operation of the same type (called its inverse). To see how, we look at types I, II, and III separately:

Type I Interchanging two rows is reversed by interchanging them again.

Type II Multiplying a row by a nonzero number (k) is reversed by multiplying by (1/k).

Type III Adding (k) times row (p) to a different row (q) is reversed by adding (-k) times row (p) to row (q) (in the new matrix). Note that (p \ne q) is essential here.
## 1.1.18
To illustrate the Type III situation, suppose there are four rows in the original matrix, denoted (R_1, R_2, R_3,) and (R_4), and that (k) times (R_2) is added to (R_3). Then the reverse operation adds (-k) times (R_2) to (R_3). The following diagram illustrates the effect of doing the operation first and then the reverse:

$$
\left[  
\begin{array}{c}  
R_1 \\  
R_2 \\  
R_3 \\  
R_4  
\end{array}  
\right]  
\longrightarrow  
\left[  
\begin{array}{c}  
R_1 \\  
R_2 \\  
R_3 + kR_2 \\  
R_4  
\end{array}  
\right]  
\longrightarrow  
\left[  
\begin{array}{c}  
R_1 \\  
R_2 \\  
(R_3 + kR_2) - kR_2 \\  
R_4  
\end{array}  
\right]
=
\left[  
\begin{array}{c}  
R_1 \\  
R_2 \\  
R_3 \\  
R_4  
\end{array}  
\right].  
]
$$
The existence of inverses for elementary row operations and hence for elementary operations on a system of equations, gives:
### 1.1.19.p (Proof of Theorem 1.1.1)
Suppose that a system of linear equations is transformed into a new system by a sequence of elementary operations. Then every solution of the original system is automatically a solution of the new system because adding equations, or multiplying an equation by a nonzero number, always results in a valid equation. In the same way, each solution of the new system must be a solution to the original system because the original system can be obtained from the new one by another series of elementary operations (the inverses of the originals). It follows that the original and new systems have the same solutions. This proves Theorem 1.1.1.1

# What To Know
## Vocab
Linear Equation
Linear Equation in n variables
System of Linear Equations
Constant Term
Coefficients
Solution to a system of linear equations
Consistent system
Inconsistent System
Parameters
Parametric Form
General Solution To A System
Augmented Matrix Of A System
Coefficient Matrix
Constant Matrix
Equivalency In Systems
Elementary Operations
Elementary Row Operations
Reversible
Reversible EROs
Inverse
Inverse of EROs
## Actionables
1. How many powers a linear equation occurs to
2. A linear equation is always in x variables
3. A system of linear equations may have a unique solution,
4. infinite solutions, or no sol
5. When only two variables are involved, the solutions to systems of linear equations can be described geometrically because the graph of a linear equation ax + by = c is a straight line if a and b are not both zero.
6. Three possibilities of systems with two equations



