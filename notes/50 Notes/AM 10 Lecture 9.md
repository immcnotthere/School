---
type: lecture
parent: "[[AM 10]]"
domain: math
status: draft
---
For an nxn matrix A, the following statements are equivalent:

1. A is invertible
2. Axbar=0bar -> xbar = 0bar
3. rref(A)=In (<-> rank(A)=n)
4. Axbar=bbar has a solution for all bbar set of R^n
5. AN=In for some nxn matrix u

uxbar = 0 

A u is also 0

If AU = In and uxbar=0bar
So using the associative property

If u satisifes condition 2 then it satisfies 3 and then 4 and 5 and so on

So therefore there is a u v = in for some matrix V

V = AU) V = A(UV)=A

All we need to do is find a right inverse and it can become a complete inverse left and right

Either if the RREF isnt going to be 

There's lots of matricies that are square and not invertible

Statisitically speaking if you put random numbers into square matricies

The dimension of the set of matricies that are not invertible is less than R^n^2 You'd have to work to get something invertible something off the plane of Rn


A prelude to determinants

Identify another way of identifying when 2x2 matricies are invertible based off of no gaussain elim

If the first column is  \[a; c] = \[0 0] not invert

If both a and c can not equal c it's not invertible

If if a dn equal 0

do weird algebra to get 1 

If you get a row of 0s not invertible (See slide 7)

Slide 8 is correct (we're supposed to valdiate)

We're evneutally going to generalize the formula of an nxn matrix

This is the formula

![[Pasted image 20260128110413.png]]

This is the formula at it's least generalizable

In the end yuou get some leg work which results in the statemetn that 

a=0, c=/=0 and (ad-bc=/=0 which is equivalently b=/=0)

You can pull out the scalar and put - signs in front of b and c 

This value which makes it invertible is the determinant??

We can't have line of 0s in column or horizontal

This condition is universal

SOO

For A=\[abcd] the determinant of A is det(A)=ad-bc=|A|

The geometric interp of an absol of a real is a distance from 0

Of a 2x2 is a plane 3x3 a volume of 4x4 a hyperplane

More fun facts of invertibles

a. A^-1 is unique if it exists

AB = I = AC
	A^-1(AB)=A^-1(AC) -> B=C
Same process that we use to intuit Ax=b

b. The inverse of the inverse is the original matrix

c. A inverible <-> A^Transpose is inverible

A^T -1 = A-1 ^T

==Check that==

d. If A, B are nxn, then AB is inveritible if and only if both A and B are invertible

Becasuse

A^-1, B^-1 --> (AB)^-1

If you multiply AB by the produt of the inverse in reverse order you get cancelation by cancelation

A^-1 = BC

What is B inverse = CA


bases and invertible matricies 

If B={ubar_1, ..., ubar_x } is a basis of R^k then u = \[ubar, ... ubar_x]


because of 3 or 4

The definition of a basis is

Their span is everything

and theyre linearlly dependent

IF every in Rk is a linear combination has a unique combination of 

We want to find a general formula for the b1 coordinates

We want to augment the matrix

We can find the inverse of this basis and just multpily abc by this inverse

e.g. another basis

Now you give a second basis and there's teh second matrix

elementary matricies

An nxn matrix is an identity and the result is the identity matrix

Swapped rows 1 and 3

You can use elementary matricies to do 

Suppose 


a_i k

M

The three cases ot check out

When RB_i 

GO TO OFFICE HOURS THATS WHAT YOU NEED TO DO BRUH

