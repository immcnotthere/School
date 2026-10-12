---
type: lecture
parent: "[[AM 10]]"
domain: math
status: draft
---
Vector space

aka a real vector space

a vector space over R

nonempty set on which two operations are defined
i. addition
ii. scalar multiplication


Slide 2

Satifysing the axioms
(see axioms)
and satisfieds all of the algebraic properties that we know and love in R^n 

Examples

R^n
2. R ^ R^1
3. **c** {a+bi:a,b set of R, i^2 = -1}
4. V={$\bar0$}

5. 
6. R[x] = {ax^n + ... + ax}

Sum of 2 polynomials = polynomial
Scalar multiple of polynomial

In higher applications we'll apply this to functions

With addition and scalar multiplication defined as usual

Because empty
Addition and scal multplication defined
Properties: 1,2,5,6,7,8
1 is true because it's inherited by R^3
We need to still check 3 and 4
3 Existence of a 0 vector
4 Opposite vectors

Closed means if you add vectors together you still get V

Definition:
If W is a real vector space and V subset of is a real vector space with additoon and scalar multiplication "inherited" from W, then V is 

Example of something that isn't a subspace in R^3

u= $\matrix{[{a\\ b}]}$ : a,b subset of R, a b = 0}

this is not closed under addition so not a subspace

as 1 0 + 0 1 

if its got a zero vector 
b. and you can do linear combination recalling that R^3 inherits most properties of a subspace

aubar + bubar subset V {closed under + and scalar multiplication}
a=b=1 b=0

it needs it's opposite
so if -ubar = -1 ubar subset V

This is not part of the definition but it follows from one of the axioms and you can do it as a brain teaser

Everything else is inherited from v

Slide 12

Is it a subspace

Does it include the 0 vector u and v times 0 = 0
If you add them together you get a linear combination

This construct is super important so it has a name

If you have a vector space any vector space a finite collection of vectors

THe span is the set of all linear combination of those vectors

Theorem 1

If ubar, ubar are vectors in the vetor space V, then u = span (ubar,ubar,ubar) is a subspace of V

The set of solutions of a homogenous solutin

And every set of solutions is a span

Going to transform this pair of Vectors that satisfy this vector equation
Theorem 2

Every span will be a null space

Every matrix has 3 standard subspaces associated with a matrix

Null space

Column space

Row space

Every subspace of R^n can be described as subspaces theyre very mich encoded 

Observation

If A is m by n and xbar subset R^n then Axbar = xAbar + x Abar

so col (A) = {Axbar: xbar subset R^n} implies R^m

or... 

multiplication by A takes xbar subset R^n to ybar Ax

Linearly independent if...

No ubari is a linear comb of 'the others'
{ubar,ubar,ubar...}


This is equivalent to a much simpler condition 



Not I <-> not II

If not I remember, so 
xk = ck 

Easy way to check if true linear indpedence between 3 x vectors

Need to study this equation of the linear combinations = 0 vector

Form the augmented matrix 


Infintiely many solutions 

are not linearly independent

Next up bases and dimension



are not linearly independent

Next up bases and dimen