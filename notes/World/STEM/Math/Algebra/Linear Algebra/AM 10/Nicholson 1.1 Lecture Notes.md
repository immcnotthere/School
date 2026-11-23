---
aliases:
  - AM 10 Lecture 1
tags:
  - lectures
  - LinearAlgebra
type: lecture
parent: "[[AM 10]]"
domain: math
status: draft
---

# Lecture

## Slide 1: Lecture map

> Lecture 1  
> • Introduction.  
> ° To the course.  
> ° To linear algebra — Some applications.  
> • Linear equations, and linear systems.  
> ° Lines, planes and hyperplanes.  
> • Example.  
> ° Gaussian elimination, first pass.

- Goal: connect [[applications]] → [[linear equation|Linear equation 1]] → [[geometry]] → [[Gaussian elimination]].
    

## Slide 2: What [[Linear Algebra]] is

> Linear Algebra:  
> The theory of solving systems of [[linear equation|Linear equation 1]] (and applications)  
> Also: The study of linear maps between vector spaces.

- Two lenses: [[solving systems]] and [[Linear Maps]] (structure behind the solving).
Uniquness comes from this restrction of finding the polynomial of [[Degree]] k<_ n-1

In HW we'll find what happens when an example of infinite solutions
## Slide 3: Application 1, [[Interpolation]]

> Interpolation: Given data $(x_1,y_1),(x_2,y_2),\ldots,(x_n,y_n)$ with $x_i\ne x_j$ for $i\ne j$, find the unique polynomial  
> $p(x)=c_0+c_1x+\cdots+c_kx^k$ of degree $k\le n-1$ satisfying $p(x_i)=y_i$ for $1\le i\le n$.

- Turns “hit these points exactly” into a [[Linear system]] for the coefficients $c_0,\ldots,c_k$.


## Slide 4: Interpolation example (exact fit)

> Points: $(1,1),(2,7),(4,-1),(5,-3),(6,4)$ and an explicit polynomial $p(x)$ shown.

- Takeaway: the “unique polynomial” claim becomes “unique solution” of a coefficient system.
    
Example of a polynomial of degree 4
But it looks like a graph of a cubit
So how can it possibly be a graph of a polynomial of degree 4
But the rest of the graph is missing 
**By looking at the equation we can intuit what the function behavior is**
^ I CANT DO THIS



## Slide 5: Application 2, [[Fitting]] (least squares idea)

> “Fitting”: Given data $(x_1,y_1),\ldots,(x_n,y_n)$, find the polynomial $\hat y(x)=c_0+c_1x+\cdots+c_kx^k$ of degree $k$ that minimizes the sum of squares $\sum_{i=1}^n (y_i-\hat y(x_i))^2$.

- Contrast with [[Interpolation]]: here you generally do **not** hit all points; you minimize total squared error.
    
Specifying K 

We're trying to minimize the sum of squares of the vertical distance of the difference between the graph and the point

Fitting a curve to theta, this will reappear at the end of the course


## Slide 6: Fitting example (degree $k=2$)

> Same points; degree $k=2$ fit $\hat y=\frac{151}{22}-\frac{185}{56}x+\frac{249}{616}x^2$ (as shown).

- A low-degree model captures trend, not exact point matching.
    
If a we're desiring to do that with a quadratic it will approximate the points and that's found by solving a certain linear system of equations

**Most of the problems boil down to solving a system of linear equations**

## Slide 7: Application 3, [[Economic mobility]] (transition percentages)

> Three classes: upper, middle, lower; transition arrows with percentages; “1st generation: 10% U, 50% m, 40% L; nth generation: ?”

- This is a “system” viewpoint: repeated transitions can be modeled with matrices later.

These examples are arbitrary but emblematic

This example is moreso the case of the study of linear maps between vector spaces

This is also a markov chain or a dynamical system

## Slide 8: More places it shows up

> Ordinary Differential Eq.s (AM 20), Partial Differential Eq.s (AM 112), Machine learning (CSE 40), Cryptography (CSE 108), etc.

- Expect [[Linear system|linear systems]] everywhere as a reusable tool.
    

## Slide 9: Definition, [[linear equation]]

> A linear equation in $n$ variables: $a_1x_1+a_2x_2+\cdots+a_nx_n=b$.  
> $a_1,\ldots,a_n,b$: coefficients. $x_1,\ldots,x_n$: variables.  
> Example: $x_1+2x_2+4x_3+8x_4+16x_5=7$.

- Pattern: variables only appear to the first power, no products like $x_1x_2$.
    
Starting with definitions

Coefficents of the equations x through xn are variables

Students struggle with the [[indicies]]

BE ABLE TO STATE INDICIES AND DEF.
## Slide 10: Definition, [[Solution (math)]] of one linear equation

> A solution of a linear equation is an $n$-tuple $(u_1,\ldots,u_n)$ of numbers that satisfy the equation.  
> Example: $(7,0,0,0,0)$ solves $x_1+2x_2+4x_3+8x_4+16x_5=7$.

- A solution is a point in $\mathbb R^n$.

This is a solution not necessarily the only solution

This isn't new but the structure is

## Slide 11: Definition, [[system of linear equations]]

> A system of $m$ linear equations in $n$ variables (coefficients $a_{ij}$, constants $b_i$).  
> $a_{ij}$ = coefficient of $x_j$ in equation $i$. $b_i$ = constant in equation $i$.

- Think “many constraints at once” on the same variable vector.
    
This is most of the class

Coefficients change vars don't
## Slide 12: Definition, [[Solution (math)]] of a linear system

> A solution of a [[Linear system]] is an [[n-tuple]] that simultaneously satisfies all equations.  
> Example: a specific 5-tuple is stated as the [[unique solution]] of the interpolation-related system.

- “Unique solution” is a property of the whole system, not of each equation separately.
- This constant imposes a condition on the equation
    

## Slide 13: Interpolation becomes a system (setup)

> From Example 1, the conditions $(1,1),(2,7),(4,-1),(5,-3),(6,4)$ produce equations in $a_0,\ldots,a_4$ (expanded powers shown).

- Method: write $p(x)=a_0+a_1x+a_2x^2+a_3x^3+a_4x^4$, plug in each $x_i$, get 5 equations.
    
Bearing that these variables are arbitrary the equation can be reduced to 
the coefficents = constant
These coefficents are constants

Most square matricies will have a sol.
## Slide 14: Geometry in $\mathbb R^2$ (a line)

> The set of all solutions of $ax+by=c$ (with $b\ne 0$) form the line $y=-\frac{a}{b}x+\frac{c}{b}$ in the plane $\mathbb R^2={(x,y):x,y\in\mathbb R}$.

- One linear equation in 2 variables cuts space down by 1 dimension (plane → line).
    
Euclidean Geometry and Linear Algebra play very nicely with each other

Geometric intuition helps with learning linear alg

RECALL ax+by=c  

## Slide 15: Geometry in $\mathbb R^3$ (a plane)

> The set of all solutions of $ax+by+cz=d$ form a plane in $\mathbb R^3={(x,y,z):x,y,z\in\mathbb R}$.  
> Example: solutions of $2x-3y-z=4$.

- One equation in 3 variables gives a 2D surface (a plane).
    
## Slide 16: Geometry in $\mathbb R^n$ (a [[Hyperplane]])

> The set of solutions of $c_1x_1+c_2x_2+\cdots+c_nx_n=b$ forms a hyperplane in $\mathbb R^n$.  
> “No picture if $n\ge 4$”; dimension $=n-1$.

- Same “dimension drops by 1” rule.
    
This plane in 2d is a point
In 3d it's a 2d in a 3d
If you have nD it becomes a hyperplane and the solution should be an n-1 dimension 
## Slide 17: Two lines can miss (no solution)

> For the system ${ax+by=c,;dx+ey=f}$ the solution set is empty if the lines are parallel.

- Empty solution set happens when constraints contradict.
    
It's parallel ~ they never touch
the same slope different intercepts
The sol. set is empty
## Slide 18: Two lines can meet once, or overlap (unique vs infinite) INTERSECTION CASE

> Unique solution if the lines intersect.  
> Infinitely many solutions if the lines coincide.

- Three outcomes to track early: 0, 1, or infinitely many solutions.
    

If they intersect there will always be a unique sol.

If the two coincide inf.

ALL HAVE 1 none or inf.
There's no such thing as 3 or n sols.
## Slide 19: Next goal: “find” solutions and “describe” the whole set

> Example system:  
> $2x+y-3z=4$  
> $x-y+2z=1$  
> $x+2y-5z=3$

- “Describe the set” means parameterize when there are free variables.
    

You don't "find" solutions, the words matter, you ~~solve~~ you describe the solutions. The first step is to describe what the solution ought to be especially when there are inf. so you need to be able to desc. what it will look like or what it could be, hence desc.

For this system what we'll do is [[transform]] the system into a simpler system that has the same set of sols.


## Slide 20: Core idea of [[Gaussian elimination]]

> Transform the system into a simpler system that has the same set of solutions.  
> (i) Rearrange  
> (ii) Eliminate variables using elementary operations

- Allowed moves are the ones that preserve the solution set.

## Slide 21: Elimination step 1 and 2

> 1. Swap equations 1 and 2
>     
> 2. Replace Eq. 2 by Eq. 2 − 2×Eq. 1
>     

- Purpose: get a clean pivot equation first, then eliminate the leading variable from the next equation.
    

## Slide 22: Elimination step 3 and 4

> 3. Replace Eq. 3 by Eq. 3 − Eq. 1
>     
> 4. Replace Eq. 3 by Eq. 3 − Eq. 2, yielding $0=0$
>     

- Seeing $0=0$ means one equation was redundant, so you should expect a free variable.
    

## Slide 23: Elimination step 5 and 6 (cleaning up)

> 5. Scale Eq. 2 (by $\frac13$)
>     
> 6. Replace Eq. 1 by Eq. 1 + Eq. 2
>     

- Goal: isolate variables so you can read off relationships directly.
    

## Slide 24: “Simple” system and free variable

> Now: $z$ is free (no restrictions). Solve for $x$ and $y$ in terms of $z$.

- Free variable appears when you have fewer independent equations than variables.
    

## Slide 25: Final solution set (parameterization)

> Set $z=t$ (a parameter).  
$$
S=\left\{\left(\frac13t+\frac53,\frac73t+\frac23,t\right):t\in\mathbb R\right\}
$$
.

- This is the “describe the set” output: an infinite family of solutions indexed by one parameter.
    
Finding a line described by three plane's intersection

Next lecture is getting into the details of this
# Learning Objectives

## Vocab

- [[Linear Algebra]]
    
- [[linear equation|Linear equation 1]]
    
- [[Solution (math)]] (equation vs system)
    
- [[system of linear equations]]
    
- line, plane, [[Hyperplane]]
    
- [[Free variable]] (implicit in $0=0$ and parameterization)
    

## Techniques

- [[Interpolation]] setup as a linear system
    
- [[Least squares]] fitting objective idea
    
- [[Gaussian elimination]] via [[elementary row operations]] (swap, scale, replace)
    
- [[Solution set parameterization]] with a parameter $t$

