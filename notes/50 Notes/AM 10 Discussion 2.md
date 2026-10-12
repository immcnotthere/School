---
type: concept
parent: "[[AM 10]]"
domain: math
status: draft
---
Vectors and bases 

Suppose three column vectors.

The question is can you hit everything in R^3 with those vectors 

The motivation of the question

vs are anything that acts like vectors 

Show v_1,v_2,v_3 form a [[basis]] of R^3 express $[1\\ 2\\ 3]$ a [[basis]] is a minimal [[Spanning Set]] (See [[Span]] [[Set]])

Suppose \[1 0 1] \[1 1 1] \[1 0 1] \[0 0 1] We can kill several of them to span all of R^3

It is sufficent to show v1,v2,v3 are linearly independent

If you solve the linear equation=0
The only thing you should have is x=y=z=0 this is the definition of linear independence

TLDR; the vector is a necessary and sufficient equation

They'll hit the dimensionality of R vectors for something that looks like R2 

You find [[Span]] through [[RREF]] 

But we need to show v1,v2,v3 form a [[basis]] of R^3 express \[1;2;3] as coordinates of v1,v2,v3

Another way to ask this is how do I take combinations to get this 4th column (an augmented column)

TA did the form a [[basis]] question first to seperate the two pedagogically 

Did that to seperate the concepts

The sols 

Span is different then [[basis]]

The null space is matrix times a sum vector = 0

Suppose Cx=0 x solves 0 

imagine C lambda x  so we're scaling x 

so then we're multiplying every element of my matrix by my lambda meaning I can pop the lambda out

So alt. it's lambda Cx

And lambda * 0  = 0

So the null space will be one of two possibilities

So it's either 0 for x or there's an infinite number of sols. 

There's another properties of null spaces which makes them so important

What if there are two solutions like C (x+y)

So we can show this through dot products but a significant thing and it holds by matrix multiplication 

So C(x+y) = 0

Cx + Cy

We solve for Cx = 0 

So every member we pop is a set of members 

1 1 1 is not the 

How do we find the [[column space]] of the matrix?

Column space is the vector your coordinates can hit

The vectors that survive after you do after an RREF

What you'll find after doing RREF you get pivots

You'll find that pivots retain their pivot quality

Each pivot that survived is a member of the column space

If you set up the matrix and RREF you'll get almost always full marks

For C on the review using the pivot explanation 

The column space is the first three columns as they are those with pivots and in RREF

So you take the first three column vectors

So it means column 1 

Because it's 5x4

Quick easy way to memorize your multiplication

You have an (axb) you multiply it by (cxd) you get (axd)

So no matter what b or c are you up losing data 

The column space is straight forward

So the nullspace are the things you toss into your matrix

The things you toss into your matrix are size 5

You need assume it square in order to 

