---
type: reference
parent: "[[STATS 131]]"
domain: stats
course: "STATS 131"
status: draft
source: "Notes_05"
tags:
  - decks
---
# STATS 131 Cards - Notes_05 Joint Distributions and Independence

## Joint probability distribution
| Front | Back | Notes |
| --- | --- | --- |
| What is the joint distribution of two random variables X and Y? | The collection of all probabilities $P((X,Y) \in E)$ for every event $E \subset \mathbb{R}^2$ | p.1; definition |
| When is a joint distribution called "discrete" vs "continuous"? | Discrete: both X and Y are discrete random variables. Continuous: both X and Y are continuous random variables. | p.1,2; discrimination |
| Give two real-world examples of a bivariate (joint) distribution. | A person's height and weight; or the number of hires and fires at a company in a given year | p.1; example |

## Joint PMF
| Front | Back | Notes |
| --- | --- | --- |
| What is the formula for the joint pmf $f(x,y)$ of discrete random variables X and Y? | $f(x,y) = P(X=x, Y=y)$ | p.1; formula |
| What two properties must a joint pmf $f(x,y)$ satisfy? | $f(x,y) \ge 0$ for all $(x,y)$, and $\sum_x \sum_y f(x,y) = 1$ | p.1; formula |
| Give two equivalent probability notations for $f(x,y) = P(X=x,Y=y)$. | $P(X=x, Y=y)$ or $P(X=x \cap Y=y)$ | p.1; definition |

## Joint PDF
| Front | Back | Notes |
| --- | --- | --- |
| How do you compute $P(a \le X \le b, c \le Y \le d)$ from the joint pdf $f(x,y)$? | $\displaystyle\int_c^d \int_a^b f(x,y)\,dx\,dy$ | p.2; formula |
| What must the joint pdf $f(x,y)$ satisfy over all of $\mathbb{R}^2$? | $f(x,y) \ge 0$ everywhere, and $\displaystyle\int_{-\infty}^{\infty}\int_{-\infty}^{\infty} f(x,y)\,dx\,dy = 1$ | p.2; formula |
| What is the key difference between a joint pmf and a joint pdf? | The joint pmf gives $P(X=x,Y=y)$ directly for discrete X, Y; the joint pdf $f(x,y)$ is not itself a probability, you get probabilities by integrating it over a region | p.2; discrimination |

## Joint CDF
| Front | Back | Notes |
| --- | --- | --- |
| What is the formula for the joint CDF $F(x,y)$ of X and Y? | $F(x,y) = P(X \le x, Y \le y)$ | p.4; formula |
| For which types of random variables (X, Y) is the joint CDF $F(x,y) = P(X\le x, Y \le y)$ defined? | For any two random variables, discrete or continuous | p.4; definition |

## Joint CDF-PDF Relationship
| Front | Back | Notes |
| --- | --- | --- |
| How do you recover the joint pdf $f(x,y)$ from the joint CDF $F(x,y)$ for continuous X, Y? | $f(x,y) = \dfrac{\partial^2}{\partial x \partial y} F(x,y)$ | p.4; formula |
| In $\dfrac{\partial^2}{\partial x \partial y} F(x,y)$, does the order of differentiation (x then y, or y then x) matter? | No, the mixed partial derivative can be taken in either order and gives the same result | p.4; formula |
| Given $F(x,y) = \frac{1}{16}xy(x+y)$, what is the first step toward finding the joint pdf? | Differentiate with respect to one variable first, e.g. $\partial F/\partial x = \frac{1}{16}(2xy+y^2)$, then differentiate that result with respect to the other variable | p.4; procedure |

## Marginal Distribution
| Front | Back | Notes |
| --- | --- | --- |
| For discrete X, Y with joint pmf $f(x,y)$, what is the formula for the marginal pmf $f_X(x)$? | $f_X(x) = \displaystyle\sum_y f(x,y)$ | p.5; formula |
| For continuous X, Y with joint pdf $f(x,y)$, what is the formula for the marginal pdf $f_X(x)$? | $f_X(x) = \displaystyle\int_{-\infty}^{\infty} f(x,y)\,dy$ | p.5; formula |
| To get the marginal distribution of X from a joint distribution, do you sum or integrate, and which variable disappears? | Sum over y if discrete, integrate over y if continuous; the y variable is eliminated, leaving a function of x alone | p.5; discrimination |
| What probability law justifies $f_X(x) = \sum_y f(x,y)$? | The law of total probability: $P(X=x) = \sum_y P(X=x \mid Y=y)P(Y=y) = \sum_y P(X=x \cap Y=y)$ | p.5; formula |
| In a joint pmf table with row/column totals, how do you find $P(X=x)$ directly from the table? | Read off the row (or column) total for that value of x; that total is the marginal probability | p.1; procedure |

## Independence of Random Variables
| Front | Back | Notes |
| --- | --- | --- |
| What is the definition of independence ($X \perp Y$) for two random variables, in terms of their joint and marginal distributions? | $f(x,y) = f_X(x)\,f_Y(y)$ for all x, y | p.6; formula |
| For which type(s) of random variables does the factorization condition $f(x,y)=f_X(x)f_Y(y)$ define independence? | Both: it holds for discrete random variables (pmfs) and continuous random variables (pdfs) | p.6; definition |
| What is the standard 3-step check for whether X and Y are independent, given a joint pdf/pmf? | 1) Find the marginal $f_X(x)$; 2) find the marginal $f_Y(y)$; 3) check whether $f_X(x)f_Y(y) = f(x,y)$ for all x, y | p.6; procedure |

## Factorization Theorem for Independence
| Front | Back | Notes |
| --- | --- | --- |
| State the factorization theorem for independence. | If $f_{X,Y}(x,y) = h(x)g(y)$ for all x, y, where h and g are univariate functions, then $X \perp Y$ | p.7; formula |
| Yes or no, and why: using the factorization theorem, do $h(x)$ and $g(y)$ need to already equal the marginal densities $f_X(x)$ and $f_Y(y)$ to conclude independence? | No; any factorization into a function of x alone times a function of y alone is enough, you don't need to compute the actual marginals first | p.7; discrimination |
| Given $f(x,y)=4xy$ on $0 \le x \le 1,\ 0 \le y \le 1$, how does the factorization theorem show $X \perp Y$ quickly? | Write $4xy = (4x)(y) = h(x)g(y)$, a product of a function of x alone and a function of y alone, so by the theorem $X \perp Y$ | p.7; procedure |

## Independence and Variable Support
| Front | Back | Notes |
| --- | --- | --- |
| Why does a support constraint like $x^2 \le y < 1$ rule out independence, even before checking $f(x,y)=f_X(x)f_Y(y)$? | Because the set of possible y-values changes with x, so the joint support isn't a rectangle; the joint density can't equal a product of separate marginals everywhere | p.3,7; discrimination |

## Functions of Independent Random Variables
| Front | Back | Notes |
| --- | --- | --- |
| If $X \perp Y$, what can you say about $g(X)$ and $h(Y)$ for any functions g and h? | $g(X)$ and $h(Y)$ are also independent | p.8; formula |
| Yes or no, and why: if $X \perp Y$, are $X^2$ and $e^Y$ independent? | Yes, since $X^2 = g(X)$ and $e^Y = h(Y)$ are functions of X and Y separately, and independence is preserved under functions | p.8; discrimination |

## Discrete Joint PMF Table (dice example)
| Front | Back | Notes |
| --- | --- | --- |
| Joint pmf table: $P(X=0,Y=1)=1/8,\ P(X=0,Y=2)=1/4,\ P(X=0,Y=3)=1/8$; $P(X=1,Y=1)=1/8,\ P(X=1,Y=2)=0,\ P(X=1,Y=3)=3/8$. Find $P(Y=1)$. | $P(Y=1)=\sum_x P(X=x,Y=1) = 1/8+1/8 = 1/4$ | p.2; procedure |

## Normalizing Constant and Region Probability
| Front | Back | Notes |
| --- | --- | --- |
| Given $f(x,y)=cx^2y$ for $x^2 \le y < 1$ (and $-1<x<1$), what value of c makes this a valid joint pdf? | $c = 21/4$, from $\int_{-1}^1 \int_{x^2}^1 cx^2y\,dy\,dx = c\cdot\frac{4}{21}=1$ | p.3; procedure |

## Joint PDF from Joint CDF
| Front | Back | Notes |
| --- | --- | --- |
| Given $F(x,y)=\frac{1}{16}xy(x+y)$ for $x,y \in [0,2]$, find the joint pdf $f(x,y)$. | $f(x,y) = \dfrac{\partial^2}{\partial x \partial y}F(x,y) = \dfrac{1}{16}(2x+2y)$ for $x,y\in[0,2]$ | p.4; procedure |

## Marginal Density from Joint PDF
| Front | Back | Notes |
| --- | --- | --- |
| Given $f(x,y)=x+y$ for $0\le x\le 1,\ 0\le y \le 1$ (0 otherwise), find the marginal density $f_X(x)$. | $f_X(x) = \int_0^1 (x+y)\,dy = x + \tfrac{1}{2}$ for $0 \le x \le 1$ (0 otherwise) | p.6; procedure |

## Independence Check, Sum Form Is Not Factorable
| Front | Back | Notes |
| --- | --- | --- |
| For $f(x,y)=x+y$ on the unit square, with $f_X(x)=x+\frac12$ and $f_Y(y)=y+\frac12$, show why X and Y are not independent. | $f_X(x)f_Y(y) = (x+\tfrac12)(y+\tfrac12) = xy+\tfrac12x+\tfrac12y+\tfrac14 \ne x+y = f(x,y)$, so X and Y are not independent | p.6; procedure |

## Independence Check via Factorization
| Front | Back | Notes |
| --- | --- | --- |
| For $f(x,y)=4xy$ on the unit square, find $f_X(x)$, $f_Y(y)$, and determine independence. | $f_X(x)=2x$, $f_Y(y)=2y$, and $f_X(x)f_Y(y)=4xy=f(x,y)$, so $X \perp Y$ | p.7; procedure |

## Exponential Race Problem
| Front | Back | Notes |
| --- | --- | --- |
| If $X\sim \text{Exp}(\lambda)$, $Y\sim\text{Exp}(\mu)$, and $X \perp Y$, what is $P(X<Y)$? | $P(X<Y)=\int_0^\infty \lambda e^{-\lambda x}\int_x^\infty \mu e^{-\mu y}\,dy\,dx = \int_0^\infty \lambda e^{-(\lambda+\mu) x}\,dx = \dfrac{\lambda}{\lambda+\mu}$ | p.8; procedure |

## Discrete Joint PMF Independence Check
| Front | Back | Notes |
| --- | --- | --- |
| Given $f(x,y)=\frac{x^2+y^2}{31}$ for $x=1,2,3$, $y=0,1$, what are $f_X(x)$ and $f_Y(y)$? | $f_X(x) = \dfrac{2x^2+1}{31}$ for $x=1,2,3$; $f_Y(y) = \dfrac{14+3y^2}{31}$ for $y=0,1$ | p.9; procedure |

# Node map

```json
[
 {
  "name": "Joint probability distribution",
  "type": "concept",
  "existing": true,
  "parent": "Joint Distributions",
  "prereqs": [],
  "uses": [],
  "page": 1,
  "summary": "The joint distribution of two random variables X and Y is the collection of all probabilities $P((X,Y)\\in E)$; it is discrete if both variables are discrete and continuous if both are continuous."
 },
 {
  "name": "Joint PMF",
  "type": "concept",
  "existing": false,
  "parent": "Joint Distributions",
  "prereqs": [
   "Joint probability distribution"
  ],
  "uses": [],
  "page": 1,
  "summary": "The joint pmf of two discrete random variables is $f(x,y)=P(X=x,Y=y)$, satisfying $f(x,y)\\ge 0$ and $\\sum_x\\sum_y f(x,y)=1$."
 },
 {
  "name": "Joint PDF",
  "type": "concept",
  "existing": false,
  "parent": "Joint Distributions",
  "prereqs": [
   "Joint probability distribution"
  ],
  "uses": [],
  "page": 2,
  "summary": "The joint pdf of two continuous random variables is a non-negative function $f(x,y)$ such that $P(a\\le X\\le b, c\\le Y\\le d)=\\int_c^d\\int_a^b f(x,y)\\,dx\\,dy$ and total integral is 1."
 },
 {
  "name": "Joint CDF",
  "type": "concept",
  "existing": false,
  "parent": "Joint Distributions",
  "prereqs": [
   "Joint probability distribution"
  ],
  "uses": [],
  "page": 4,
  "summary": "The joint CDF of X and Y is $F(x,y)=P(X\\le x, Y\\le y)$."
 },
 {
  "name": "Joint CDF-PDF Relationship",
  "type": "concept",
  "existing": false,
  "parent": "Joint Distributions",
  "prereqs": [
   "Joint PDF",
   "Joint CDF"
  ],
  "uses": [],
  "page": 4,
  "summary": "For continuous X and Y, the joint pdf is the mixed second partial derivative of the joint CDF: $\\frac{\\partial^2}{\\partial x\\partial y}F(x,y)=f(x,y)$."
 },
 {
  "name": "Marginal Distribution",
  "type": "concept",
  "existing": false,
  "parent": "Marginal Distributions",
  "prereqs": [
   "Joint PMF",
   "Joint PDF"
  ],
  "uses": [],
  "page": 5,
  "summary": "The marginal distribution of X is obtained by summing (discrete) or integrating (continuous) the joint pmf/pdf over all values of the other variable Y."
 },
 {
  "name": "Independence of Random Variables",
  "type": "concept",
  "existing": false,
  "parent": "Independence of Random Variables",
  "prereqs": [
   "Joint PMF",
   "Joint PDF",
   "Marginal Distribution"
  ],
  "uses": [],
  "page": 6,
  "summary": "X and Y are independent ($X\\perp Y$) if and only if their joint pmf/pdf factors as $f(x,y)=f_X(x)f_Y(y)$."
 },
 {
  "name": "Factorization Theorem for Independence",
  "type": "concept",
  "existing": false,
  "parent": "Independence of Random Variables",
  "prereqs": [
   "Independence of Random Variables"
  ],
  "uses": [],
  "page": 7,
  "summary": "If the joint pdf/pmf factors as $f(x,y)=h(x)g(y)$ for any univariate functions h and g, then $X\\perp Y$, without needing to compute the actual marginals."
 },
 {
  "name": "Independence and Variable Support",
  "type": "concept",
  "existing": false,
  "parent": "Independence of Random Variables",
  "prereqs": [
   "Independence of Random Variables"
  ],
  "uses": [],
  "page": 7,
  "summary": "If the support of one variable depends on the value of the other, the variables cannot be independent, regardless of the formula for f(x,y)."
 },
 {
  "name": "Functions of Independent Random Variables",
  "type": "concept",
  "existing": false,
  "parent": "Independence of Random Variables",
  "prereqs": [
   "Independence of Random Variables"
  ],
  "uses": [],
  "page": 8,
  "summary": "If X and Y are independent, then g(X) and h(Y) are independent for any functions g and h."
 },
 {
  "name": "Discrete Joint PMF Table (dice example)",
  "type": "problem",
  "existing": false,
  "parent": "Joint Distributions",
  "prereqs": [],
  "uses": [
   "Joint PMF",
   "Marginal Distribution"
  ],
  "page": 2,
  "summary": "Given a 2x3 joint pmf table for X and Y, compute a joint probability and a marginal probability by summing table entries."
 },
 {
  "name": "Normalizing Constant and Region Probability",
  "type": "problem",
  "existing": false,
  "parent": "Joint Distributions",
  "prereqs": [],
  "uses": [
   "Joint PDF"
  ],
  "page": 3,
  "summary": "Given $f(x,y)=cx^2y$ on $x^2\\le y<1$, find the normalizing constant c and the probabilities $P(X>Y)$ and $P(X=Y)$."
 },
 {
  "name": "Joint PDF from Joint CDF",
  "type": "problem",
  "existing": false,
  "parent": "Joint Distributions",
  "prereqs": [],
  "uses": [
   "Joint CDF",
   "Joint CDF-PDF Relationship"
  ],
  "page": 4,
  "summary": "Given the joint CDF $F(x,y)=\\frac{1}{16}xy(x+y)$, find the joint pdf by taking the mixed partial derivative."
 },
 {
  "name": "Marginal Density from Joint PDF",
  "type": "problem",
  "existing": false,
  "parent": "Marginal Distributions",
  "prereqs": [],
  "uses": [
   "Joint PDF",
   "Marginal Distribution"
  ],
  "page": 6,
  "summary": "Given $f(x,y)=x+y$ on the unit square, find the marginal density of X by integrating out y."
 },
 {
  "name": "Independence Check, Sum Form Is Not Factorable",
  "type": "problem",
  "existing": false,
  "parent": "Independence of Random Variables",
  "prereqs": [],
  "uses": [
   "Marginal Distribution",
   "Independence of Random Variables"
  ],
  "page": 6,
  "summary": "Show that $f(x,y)=x+y$ on the unit square does not factor into the product of its marginals, so X and Y are not independent."
 },
 {
  "name": "Independence Check via Factorization",
  "type": "problem",
  "existing": false,
  "parent": "Independence of Random Variables",
  "prereqs": [],
  "uses": [
   "Independence of Random Variables",
   "Factorization Theorem for Independence"
  ],
  "page": 7,
  "summary": "Show that $f(x,y)=4xy$ on the unit square factors as a product of a function of x and a function of y, so X and Y are independent."
 },
 {
  "name": "Exponential Race Problem",
  "type": "problem",
  "existing": false,
  "parent": "Independence of Random Variables",
  "prereqs": [],
  "uses": [
   "Independence of Random Variables"
  ],
  "page": 8,
  "summary": "For independent $X\\sim\\text{Exp}(\\lambda)$ and $Y\\sim\\text{Exp}(\\mu)$, find $P(X<Y)$ by integrating the joint density over the region $x<y$."
 },
 {
  "name": "Discrete Joint PMF Independence Check",
  "type": "problem",
  "existing": false,
  "parent": "Independence of Random Variables",
  "prereqs": [],
  "uses": [
   "Joint PMF",
   "Marginal Distribution",
   "Independence of Random Variables"
  ],
  "page": 9,
  "summary": "Given $f(x,y)=(x^2+y^2)/31$ for $x=1,2,3$, $y=0,1$, find the marginals and show X and Y are not independent."
 }
]
```

# Frankenstein problems

**Frankenstein Problem 1.** Let X and Y have joint pdf $f(x,y) = 6xy^2$ for $0 \le x \le 1,\ 0 \le y \le 1$ (0 otherwise).

a) Verify $f$ is a valid joint pdf, then find the marginal densities $f_X(x)$ and $f_Y(y)$.
b) Determine whether $X \perp Y$.
c) Find the joint CDF $F(x,y)$ and verify $\frac{\partial^2}{\partial x \partial y}F(x,y) = f(x,y)$.
d) Compute $P(X > Y)$.

*Solution.*

a) $\int_0^1\int_0^1 6xy^2\,dy\,dx = \int_0^1 6x\left[\frac{y^3}{3}\right]_0^1 dx = \int_0^1 2x\,dx = 1$, so $f$ is valid.
$f_X(x) = \int_0^1 6xy^2\,dy = 6x\cdot\frac{1}{3} = 2x$ for $0\le x\le 1$ (check: $\int_0^1 2x\,dx=1$).
$f_Y(y) = \int_0^1 6xy^2\,dx = 6y^2\cdot\frac{1}{2} = 3y^2$ for $0\le y\le 1$ (check: $\int_0^1 3y^2\,dy=1$).

b) $f_X(x)f_Y(y) = 2x\cdot 3y^2 = 6xy^2 = f(x,y)$, so by the factorization theorem $X \perp Y$.

c) $F(x,y) = \int_0^x\int_0^y 6uv^2\,dv\,du = \int_0^x 6u\left[\frac{v^3}{3}\right]_0^y du = \int_0^x 2uy^3\,du = 2y^3\left[\frac{u^2}{2}\right]_0^x = x^2y^3$ for $0\le x,y\le 1$.
Check: $\frac{\partial F}{\partial x} = 2xy^3$, then $\frac{\partial}{\partial y}(2xy^3) = 6xy^2 = f(x,y)$. Matches.

d) $P(X>Y) = \int_0^1\int_0^x 6xy^2\,dy\,dx = \int_0^1 6x\left[\frac{y^3}{3}\right]_0^x dx = \int_0^1 2x^4\,dx = \frac{2}{5}$.

Concepts tested: Joint PDF, Marginal Distribution, Independence of Random Variables (Factorization Theorem for Independence), Joint CDF, Joint CDF-PDF Relationship.

**Frankenstein Problem 2.** Let X and Y have joint pmf $f(x,y) = \dfrac{x+y}{21}$ for $x=1,2,3$ and $y=1,2$ (0 otherwise).

a) Verify $f$ is a valid joint pmf.
b) Find $f_X(x)$ and $f_Y(y)$.
c) Determine whether $X \perp Y$.
d) Find $F(2,1) = P(X\le 2, Y\le 1)$.

*Solution.*

a) Values: $f(1,1)=\frac{2}{21}, f(1,2)=\frac{3}{21}, f(2,1)=\frac{3}{21}, f(2,2)=\frac{4}{21}, f(3,1)=\frac{4}{21}, f(3,2)=\frac{5}{21}$. Sum $=\frac{2+3+3+4+4+5}{21}=\frac{21}{21}=1$, so $f$ is valid.

b) $f_X(1)=\frac{2+3}{21}=\frac{5}{21}$, $f_X(2)=\frac{3+4}{21}=\frac{7}{21}$, $f_X(3)=\frac{4+5}{21}=\frac{9}{21}$ (sum $=\frac{21}{21}=1$, checks).
$f_Y(1)=\frac{2+3+4}{21}=\frac{9}{21}$, $f_Y(2)=\frac{3+4+5}{21}=\frac{12}{21}$ (sum $=\frac{21}{21}=1$, checks).

c) $f_X(1)f_Y(1) = \frac{5}{21}\cdot\frac{9}{21} = \frac{45}{441}$, while $f(1,1) = \frac{2}{21} = \frac{42}{441}$. Since $\frac{45}{441}\ne\frac{42}{441}$, $X$ and $Y$ are not independent.

d) $F(2,1) = f(1,1)+f(2,1) = \frac{2}{21}+\frac{3}{21} = \frac{5}{21}$.

Concepts tested: Joint PMF, Marginal Distribution, Independence of Random Variables, Joint CDF.
