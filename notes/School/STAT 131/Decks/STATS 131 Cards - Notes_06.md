---
type: reference
parent: "[[STATS 131]]"
domain: stats
course: "STATS 131"
status: draft
source: "Notes_06"
tags:
  - decks
---
# STATS 131 Cards - Notes_06 Conditional Distributions and Transformations

## Conditional PMF
| Front | Back | Notes |
| --- | --- | --- |
| Definition: conditional pmf $f_{X\mid Y}(x\mid y)$ of $X$ given $Y=y$ for discrete $X,Y$? | $f_{X\mid Y}(x\mid y) = \dfrac{f_{X,Y}(x,y)}{f_Y(y)}$, provided $f_Y(y)>0$ | p.2; definition |
| Why is $f_{X\mid Y}(x\mid y)$, as a function of $x$ with $y$ fixed, always a valid pmf? | $\sum_x f_{X\mid Y}(x\mid y) = \dfrac{1}{f_Y(y)}\sum_x f_{X,Y}(x,y) = \dfrac{f_Y(y)}{f_Y(y)} = 1$ | p.2; theorem (6.1) |
| How do you compute $P(X \in E \mid Y=y)$ from the conditional pmf? | $P(X \in E \mid Y=y) = \sum_{x \in E} f_{X\mid Y}(x\mid y)$ | p.2; formula |
| Conditional pmf $f_{X\mid Y}(x\mid y)$ vs marginal pmf $f_X(x)$: what changes? | $f_X(x)$ sums over the whole sample space; $f_{X\mid Y}(x\mid y)$ restricts to the slice $Y=y$ and renormalizes by dividing the joint pmf by $f_Y(y)$ | p.2; discrimination |

## Conditional PDF
| Front | Back | Notes |
| --- | --- | --- |
| Definition: conditional pdf $f_{X\mid Y}(x\mid y)$ for continuous $X,Y$? | $f_{X\mid Y}(x\mid y) = \dfrac{f_{X,Y}(x,y)}{f_Y(y)}$, provided $f_Y(y)>0$ | p.3; definition (6.2) |
| How do you find $P(X \in E \mid Y=y)$ using the conditional pdf? | $P(X\in E\mid Y=y) = \displaystyle\int_E f_{X\mid Y}(x\mid y)\,dx$ | p.3; formula |
| For fixed $Y=y$, what kind of function of $x$ is $f_{X\mid Y}(x\mid y)$? | A valid pdf: nonnegative and integrates to 1 over $x$ | p.3; fact |

## Multiplication Rule for Densities
| Front | Back | Notes |
| --- | --- | --- |
| State the multiplication rule linking the joint density to conditional and marginal densities. | $f_{(X,Y)}(x,y) = f_{X\mid Y}(x\mid y) f_Y(y) = f_{Y\mid X}(y\mid x) f_X(x)$ | p.4; formula (6.2) |
| How does this density multiplication rule differ from the event Multiplication Rule ($P(A\cap B)=P(A\mid B)P(B)$)? | The event rule gives one number; this version gives an entire joint density as a function of $(x,y)$, built from conditional and marginal densities or pmfs | p.4; discrimination |

## Law of Total Probability (Random Variables)
| Front | Back | Notes |
| --- | --- | --- |
| Law of total probability for $f_X(x)$ when $Y$ is continuous? | $f_X(x) = \displaystyle\int f_{(X,Y)}(x,y)\,dy = \int f_{X\mid Y}(x\mid y) f_Y(y)\,dy$ | p.4; formula (6.3) |
| Law of total probability for $f_X(x)$ when $Y$ is discrete? | $f_X(x) = \displaystyle\sum_y f_{(X,Y)}(x,y) = \sum_y f_{X\mid Y}(x\mid y) f_Y(y)$ | p.4; formula (6.3) |

## Independence of Random Variables
| Front | Back | Notes |
| --- | --- | --- |
| Density criterion (Thm 6.5) for $X \perp Y$? | $X \perp Y$ iff $f_{X\mid Y}(x\mid y) = f_X(x)$ for all $y$ with $f_Y(y)>0$ | p.5; theorem |

## Transformation of a Discrete Random Variable
| Front | Back | Notes |
| --- | --- | --- |
| Theorem 6.6: if $X$ is discrete with pmf $f_X$ and $Y=r(X)$, what is $f_Y(y)$? | $f_Y(y) = P(r(X)=y) = \displaystyle\sum_{x:\,r(x)=y} f_X(x)$ | p.6; formula |
| Procedure to find the pmf of $Y=r(X)$ for discrete $X$? | For each value $y$ of $Y$, find the set $\{x : r(x)=y\}$ and sum $f_X(x)$ over that set | p.6; procedure |

## Transformation of a Continuous Random Variable (CDF Method)
| Front | Back | Notes |
| --- | --- | --- |
| Theorem 6.7: if $X$ is continuous with cdf $F_X$ and $Y=r(X)$, what is $F_Y(y)$? | $F_Y(y) = P(r(X)\le y) = \displaystyle\int_{x:\,r(x)\le y} f_X(x)\,dx$ | p.6; formula |
| Procedure (CDF method) to get the pdf of $Y=r(X)$? | 1) find the support of $Y$; 2) write $F_Y(y)=P(r(X)\le y)$ and solve the inequality for $x$ in terms of $F_X$; 3) differentiate $F_Y(y)$ with respect to $y$ | p.6-8; procedure |

## Linear Transformation of a Random Variable
| Front | Back | Notes |
| --- | --- | --- |
| Theorem 6.8: if $X$ is continuous with pdf $f_X$ and $Y=aX+b$, $a\neq0$, what is $f_Y(y)$? | $f_Y(y) = \dfrac{1}{\vert a\vert } f_X\!\left(\dfrac{y-b}{a}\right)$ | p.7; formula |
| Why divide by $\vert a\vert $ rather than $a$ in the linear transformation formula? | The Jacobian of $x=(y-b)/a$ has absolute value $1/\vert a\vert $; a density must stay nonnegative, and using $a$ directly could make it negative when $a<0$ | p.7; discrimination |

## Probability Integral Transformation
| Front | Back | Notes |
| --- | --- | --- |
| Theorem 6.9: if $X$ is continuous with cdf $F_X$ and $Y=F_X(X)$, what is the distribution of $Y$? | $Y \sim Unif[0,1]$ | p.8; theorem |
| Inverse-CDF simulation algorithm: how do you generate a random number from a distribution with cdf $F$? | 1) generate $U_i \sim Unif[0,1]$; 2) apply $F^{-1}(U_i)$; the resulting values $\{F^{-1}(U_i)\}$ follow the distribution $F$ | p.8; procedure |

## Auto Insurance Stolen Car
| Front | Back | Notes |
| --- | --- | --- |
| Key move: from $P(X{=}1)=0.024$ and $P(X{=}1, Y{=}3)=0.001$, find $P(Y{=}3 \mid X{=}1)$. | Divide the joint entry by the marginal: $P(Y{=}3\mid X{=}1) = 0.001/0.024 \approx 0.042$ | p.1; problem |

## Conditional PMF from Joint Table (Y given X=2)
| Front | Back | Notes |
| --- | --- | --- |
| Joint table row $x=2$: $(y{=}1,\dots,4)=(0.3,0,0.1,0.2)$, row total $0.6$. Key move to get $f_{Y\mid X}(y\mid 2)$? | Divide each entry by the row total $f_X(2)=0.6$: $f_{Y\mid X}(1\mid2)=\tfrac12$, $f_{Y\mid X}(2\mid2)=0$, $f_{Y\mid X}(3\mid2)=\tfrac16$, $f_{Y\mid X}(4\mid2)=\tfrac13$ | p.2; problem |

## Joint Density Conditionals (Exponential Joint Density)
| Front | Back | Notes |
| --- | --- | --- |
| Given $f(x,y)=e^{-x}$ for $0\le y \le x <\infty$, key move to find $f_{X\mid Y}(x\mid y)$? | Integrate out $x$ for the marginal, $f_Y(y)=\int_y^\infty e^{-x}dx = e^{-y}$, then divide: $f_{X\mid Y}(x\mid y) = e^{-x}/e^{-y} = e^{-(x-y)}$ for $y\le x<\infty$ | p.3; problem |

## Compound Uniform (Y given X, Both Uniform)
| Front | Back | Notes |
| --- | --- | --- |
| $X\sim Unif[0,1]$, $Y\mid X{=}x \sim Unif[x,1]$. Key move to get the joint pdf? | Multiply: $f(x,y) = f_{Y\mid X}(y\mid x)f_X(x) = \dfrac{1}{1-x}\cdot 1 = \dfrac{1}{1-x}$ for $0<x<y<1$ | p.4; problem |

## Semicircle Conditional Density
| Front | Back | Notes |
| --- | --- | --- |
| $(X,Y)$ uniform (density $c$) on $\{x^2+y^2\le1, x\ge0\}$. Key move to get $f_{X\mid Y}(x\mid y)$? | Integrate out $x$ for the marginal, $f_Y(y)=\int_0^{\sqrt{1-y^2}} c\,dx = c\sqrt{1-y^2}$, then divide: $f_{X\mid Y}(x\mid y) = 1/\sqrt{1-y^2}$ for $0\le x\le\sqrt{1-y^2}$ | p.4; problem |

## Bayes Update for a Discrete Conditional Family
| Front | Back | Notes |
| --- | --- | --- |
| Given $f_{Y\mid X}(y\mid x) = \dfrac{x^2+y^2}{2x^2+1}$, $f_Y(y)=\dfrac{14+3y^2}{31}$, $f_X(x)=\dfrac{2x^2+1}{31}$. Key move to get $f_{X\mid Y}(x\mid y)$ by Bayes? | $f_{X\mid Y}(x\mid y) = \dfrac{f_{Y\mid X}(y\mid x)f_X(x)}{f_Y(y)} = \dfrac{x^2+y^2}{2x^2+1}\cdot\dfrac{2x^2+1}{31}\cdot\dfrac{31}{14+3y^2} = \dfrac{x^2+y^2}{14+3y^2}$, for $x=1,2,3$; the $(2x^2{+}1)$ and $31$ factors cancel | p.5; problem |

## Distance from the Middle (Discrete Transformation)
| Front | Back | Notes |
| --- | --- | --- |
| $X\sim Unif\{1,\dots,9\}$, $Y=\lvert X-5\rvert$. Key move to get the pmf of $Y$? | Group $x$-values by $\lvert x-5\rvert$ and sum: $P(Y{=}0)=P(X{=}5)=1/9$; $P(Y{=}k)=2/9$ for $k=1,2,3,4$ (probabilities sum to 1) | p.6; problem |

## Average Waiting Time (Reciprocal of an Exponential)
| Front | Back | Notes |
| --- | --- | --- |
| $Z\sim Exp(\lambda)$, $Y=1/Z$. Key move to find $F_Y$ (then $f_Y$)? | Invert the event: $P(Y\le y)=P(Z\ge 1/y)=1-F_Z(1/y)=e^{-\lambda/y}$ for $y>0$; differentiate to get $f_Y(y)=\dfrac{\lambda e^{-\lambda/y}}{y^2}$ | p.7; problem |

## Square of a Uniform Random Variable
| Front | Back | Notes |
| --- | --- | --- |
| $X\sim Unif[-1,1]$, $Y=X^2$. Key move to find $F_Y(y)$? | Split into both tails: $F_Y(y)=P(-\sqrt y \le X \le \sqrt y) = F_X(\sqrt y) - F_X(-\sqrt y) = \sqrt y$ for $0\le y\le1$, giving $f_Y(y) = \tfrac12 y^{-1/2}$ | p.7; problem |

## Scaled Exponential (Dividing by 5)
| Front | Back | Notes |
| --- | --- | --- |
| $X\sim Exp(1)$, $Y=X/5$. Key move using the linear transformation theorem? | Apply $f_Y(y)=\dfrac{1}{\vert a\vert }f_X\!\left(\dfrac{y-b}{a}\right)$ with $a=1/5, b=0$: $f_Y(y) = 5e^{-5y}$, i.e. $Y\sim Exp(5)$ | p.8; problem |

## CDF of the CDF (Y = F(X))
| Front | Back | Notes |
| --- | --- | --- |
| $X\sim Exp(1)$, $Y=F_X(X)$. Key move to confirm $Y\sim Unif[0,1]$ directly? | Invert: $F_Y(y)=P(F_X(X)\le y) = P(X\le F_X^{-1}(y)) = F_X(F_X^{-1}(y)) = y$ for $0\le y\le1$, so $f_Y(y)=1$: uniform | p.8; problem |

## Bayes' Theorem for Distributions
| Front | Back | Notes |
| --- | --- | --- |
| Bayes theorem for two random variables: express $f_{X\mid Y}(x\mid y)$ in terms of $f_{Y\mid X}$. | $f_{X\mid Y}(x\mid y) = \dfrac{f_{Y\mid X}(y\mid x) f_X(x)}{f_Y(y)}$, provided $f_Y(y)>0$ | p.5; formula (6.4) |
| In the random-variable Bayes formula, which piece is the prior and which is the likelihood? | $f_X(x)$ is the prior; $f_{Y\mid X}(y\mid x)$ is the likelihood of $Y=y$ given $X=x$; $f_Y(y)$ normalizes | p.5; discrimination |

# Node map
```json
[
 {
  "name": "Conditional PMF",
  "type": "concept",
  "existing": false,
  "parent": "Conditional Distributions",
  "prereqs": [
   "Conditional Probability",
   "PMF, PDF and CDF"
  ],
  "uses": [],
  "page": 2,
  "summary": "For discrete $X,Y$, $f_{X\\mid Y}(x\\mid y)=f_{X,Y}(x,y)/f_Y(y)$ when $f_Y(y)>0$; it is itself a valid pmf in $x$ for each fixed $y$."
 },
 {
  "name": "Conditional PDF",
  "type": "concept",
  "existing": false,
  "parent": "Conditional Distributions",
  "prereqs": [
   "Conditional PMF",
   "Probability density function"
  ],
  "uses": [],
  "page": 3,
  "summary": "For continuous $X,Y$, $f_{X\\mid Y}(x\\mid y)=f_{X,Y}(x,y)/f_Y(y)$ when $f_Y(y)>0$; probabilities of $X$ given $Y=y$ are obtained by integrating this conditional density."
 },
 {
  "name": "Multiplication Rule for Densities",
  "type": "concept",
  "existing": false,
  "parent": "Conditional Distributions",
  "prereqs": [
   "Conditional PMF",
   "Conditional PDF",
   "Joint probability distribution"
  ],
  "uses": [],
  "page": 4,
  "summary": "The joint density factors as $f_{(X,Y)}(x,y)=f_{X\\mid Y}(x\\mid y)f_Y(y)=f_{Y\\mid X}(y\\mid x)f_X(x)$."
 },
 {
  "name": "Law of Total Probability (Random Variables)",
  "type": "concept",
  "existing": false,
  "parent": "Conditional Distributions",
  "prereqs": [
   "Multiplication Rule for Densities"
  ],
  "uses": [],
  "page": 4,
  "summary": "The marginal density/pmf of $X$ is obtained by integrating (continuous $Y$) or summing (discrete $Y$) the joint density/pmf over $y$."
 },
 {
  "name": "Bayes' Rule",
  "type": "concept",
  "existing": true,
  "parent": "Conditional Distributions",
  "prereqs": [
   "Multiplication Rule for Densities",
   "Law of Total Probability (Random Variables)"
  ],
  "uses": [],
  "page": 5,
  "summary": "For random variables, $f_{X\\mid Y}(x\\mid y)=f_{Y\\mid X}(y\\mid x)f_X(x)/f_Y(y)$: the conditional density of $X$ given $Y$ inverted from the conditional density of $Y$ given $X$."
 },
 {
  "name": "Independence of Random Variables",
  "type": "concept",
  "existing": false,
  "parent": "Conditional Distributions",
  "prereqs": [
   "Conditional PMF",
   "Conditional PDF"
  ],
  "uses": [],
  "page": 5,
  "summary": "$X$ and $Y$ are independent iff $f_{X\\mid Y}(x\\mid y)=f_X(x)$, equivalently iff the joint density factors as $f_X(x)f_Y(y)$."
 },
 {
  "name": "Transformation of a Discrete Random Variable",
  "type": "concept",
  "existing": false,
  "parent": "Transformations of Random Variables",
  "prereqs": [
   "PMF, PDF and CDF"
  ],
  "uses": [],
  "page": 6,
  "summary": "For discrete $X$ and $Y=r(X)$, $f_Y(y)=\\sum_{x:r(x)=y} f_X(x)$: sum the pmf over all $x$ mapping to that $y$."
 },
 {
  "name": "Transformation of a Continuous Random Variable (CDF Method)",
  "type": "concept",
  "existing": false,
  "parent": "Transformations of Random Variables",
  "prereqs": [
   "PMF, PDF and CDF"
  ],
  "uses": [],
  "page": 6,
  "summary": "For continuous $X$ and $Y=r(X)$, find $F_Y(y)=P(r(X)\\le y)$ by rewriting the event in terms of $X$, then differentiate to get $f_Y$."
 },
 {
  "name": "Linear Transformation of a Random Variable",
  "type": "concept",
  "existing": false,
  "parent": "Transformations of Random Variables",
  "prereqs": [
   "Transformation of a Continuous Random Variable (CDF Method)"
  ],
  "uses": [],
  "page": 7,
  "summary": "For $Y=aX+b$, $a\\neq0$, $f_Y(y)=\\frac{1}{|a|}f_X((y-b)/a)$: a shortcut instance of the CDF method."
 },
 {
  "name": "Probability Integral Transformation",
  "type": "concept",
  "existing": false,
  "parent": "Transformations of Random Variables",
  "prereqs": [
   "Transformation of a Continuous Random Variable (CDF Method)"
  ],
  "uses": [],
  "page": 8,
  "summary": "If $X$ is continuous with cdf $F_X$, then $Y=F_X(X)\\sim Unif[0,1]$; inverting gives the inverse-CDF method for simulating any distribution from uniforms."
 },
 {
  "name": "Auto Insurance Stolen Car",
  "type": "problem",
  "existing": false,
  "parent": "Conditional Distributions",
  "prereqs": [
   "Conditional Probability"
  ],
  "uses": [
   "Conditional PMF"
  ],
  "page": 1,
  "summary": "From a joint table of brand and theft status, compute $P(\\text{Brand }3\\mid \\text{stolen})$ by dividing the joint cell by the marginal."
 },
 {
  "name": "Conditional PMF from Joint Table (Y given X=2)",
  "type": "problem",
  "existing": false,
  "parent": "Conditional Distributions",
  "prereqs": [],
  "uses": [
   "Conditional PMF"
  ],
  "page": 2,
  "summary": "Divide the $x=2$ row of a joint pmf table by its row total to get $f_{Y\\mid X}(y\\mid 2)$."
 },
 {
  "name": "Joint Density Conditionals (Exponential Joint Density)",
  "type": "problem",
  "existing": false,
  "parent": "Conditional Distributions",
  "prereqs": [],
  "uses": [
   "Conditional PDF"
  ],
  "page": 3,
  "summary": "From $f(x,y)=e^{-x}$ on $0\\le y\\le x$, find both conditional densities by first computing the relevant marginal."
 },
 {
  "name": "Compound Uniform (Y given X, Both Uniform)",
  "type": "problem",
  "existing": false,
  "parent": "Conditional Distributions",
  "prereqs": [],
  "uses": [
   "Multiplication Rule for Densities",
   "Law of Total Probability (Random Variables)"
  ],
  "page": 4,
  "summary": "Build the joint pdf via the multiplication rule, then integrate out $x$ to get the marginal of $Y$."
 },
 {
  "name": "Semicircle Conditional Density",
  "type": "problem",
  "existing": false,
  "parent": "Conditional Distributions",
  "prereqs": [],
  "uses": [
   "Conditional PDF"
  ],
  "page": 4,
  "summary": "For a uniform density on a semicircle, integrate out $x$ to get $f_Y(y)$, then divide to get $f_{X\\mid Y}(x\\mid y)$."
 },
 {
  "name": "Bayes Update for a Discrete Conditional Family",
  "type": "problem",
  "existing": false,
  "parent": "Conditional Distributions",
  "prereqs": [],
  "uses": [
   "Bayes' Rule"
  ],
  "page": 5,
  "summary": "Apply Bayes' rule to a conditional pmf and two marginal pmfs, with algebraic cancellation, to get a simplified conditional pmf."
 },
 {
  "name": "Distance from the Middle (Discrete Transformation)",
  "type": "problem",
  "existing": false,
  "parent": "Transformations of Random Variables",
  "prereqs": [],
  "uses": [
   "Transformation of a Discrete Random Variable"
  ],
  "page": 6,
  "summary": "For $X$ uniform on $\\{1,\\dots,9\\}$ and $Y=|X-5|$, group outcomes by their $Y$-value to get the pmf of $Y$."
 },
 {
  "name": "Average Waiting Time (Reciprocal of an Exponential)",
  "type": "problem",
  "existing": false,
  "parent": "Transformations of Random Variables",
  "prereqs": [],
  "uses": [
   "Transformation of a Continuous Random Variable (CDF Method)"
  ],
  "page": 7,
  "summary": "For $Z\\sim Exp(\\lambda)$ and $Y=1/Z$, use the CDF method to find $F_Y$ and $f_Y$."
 },
 {
  "name": "Square of a Uniform Random Variable",
  "type": "problem",
  "existing": false,
  "parent": "Transformations of Random Variables",
  "prereqs": [],
  "uses": [
   "Transformation of a Continuous Random Variable (CDF Method)"
  ],
  "page": 7,
  "summary": "For $X\\sim Unif[-1,1]$ and $Y=X^2$, use the CDF method with both tails to find $f_Y$."
 },
 {
  "name": "Scaled Exponential (Dividing by 5)",
  "type": "problem",
  "existing": false,
  "parent": "Transformations of Random Variables",
  "prereqs": [],
  "uses": [
   "Linear Transformation of a Random Variable"
  ],
  "page": 8,
  "summary": "For $X\\sim Exp(1)$ and $Y=X/5$, apply the linear transformation formula directly to get $Y\\sim Exp(5)$."
 },
 {
  "name": "CDF of the CDF (Y = F(X))",
  "type": "problem",
  "existing": false,
  "parent": "Transformations of Random Variables",
  "prereqs": [],
  "uses": [
   "Probability Integral Transformation"
  ],
  "page": 8,
  "summary": "For $X\\sim Exp(1)$ and $Y=F_X(X)$, directly verify $Y\\sim Unif[0,1]$ by inverting the cdf."
 },
 {
  "name": "Bayes' Theorem for Distributions",
  "type": "concept",
  "existing": true,
  "parent": "",
  "prereqs": [],
  "summary": ""
 }
]
```

# Frankenstein problems

**Frankenstein Problem 1.** Let $X \sim Unif[0,1]$ and, given $X=x$, let $Y \mid X{=}x \sim Unif[0,x]$.

(a) Find the joint pdf $f(x,y)$.
(b) Find the marginal pdf $f_Y(y)$.
(c) Find the conditional pdf $f_{X\mid Y}(x\mid y)$.
(d) Are $X$ and $Y$ independent?

Concepts tested: Multiplication Rule for Densities, Law of Total Probability (Random Variables), Bayes' Rule, Independence of Random Variables.

*Solution.*

(a) $f_X(x)=1$ for $0<x<1$, and $f_{Y\mid X}(y\mid x) = 1/x$ for $0<y<x$. By the multiplication rule,
$$f(x,y) = f_{Y\mid X}(y\mid x)f_X(x) = \frac{1}{x}\cdot 1 = \frac{1}{x}, \quad 0<y<x<1.$$

(b) By the law of total probability, integrating out $x$ from $y$ to $1$ (since $x>y$):
$$f_Y(y) = \int_y^1 \frac{1}{x}\,dx = [\ln x]_y^1 = -\ln y, \quad 0<y<1.$$
Check: $\int_0^1 (-\ln y)\,dy = [y - y\ln y]_0^1 = 1 - 0 = 1$, a valid pdf.

(c) By Bayes' rule,
$$f_{X\mid Y}(x\mid y) = \frac{f(x,y)}{f_Y(y)} = \frac{1/x}{-\ln y} = \frac{-1}{x\ln y}, \quad y<x<1$$
(this is positive since $\ln y<0$ for $0<y<1$). Check: $\int_y^1 \frac{-1}{x\ln y}\,dx = \frac{-1}{\ln y}[\ln x]_y^1 = \frac{-1}{\ln y}(0-\ln y) = 1$, valid.

(d) $f_X(x)=1$ is constant, but $f_{X\mid Y}(x\mid y) = -1/(x\ln y)$ depends on $y$. Since $f_{X\mid Y}(x\mid y)\neq f_X(x)$, by the independence criterion $X$ and $Y$ are **not** independent.

---

**Frankenstein Problem 2.** Let $X \sim Exp(1)$, so $f_X(x)=e^{-x}$ and $F_X(x)=1-e^{-x}$ for $x>0$.

(a) Let $Y = 2X+1$. Use the linear transformation theorem to find $f_Y(y)$ and its support.
(b) Verify part (a) directly with the CDF method: find $F_Y(y)$, then differentiate.
(c) Let $W = F_X(X)$. State the distribution of $W$ using the probability integral transformation, then confirm it by finding $F_W(w)$ directly.

Concepts tested: Linear Transformation of a Random Variable, Transformation of a Continuous Random Variable (CDF Method), Probability Integral Transformation.

*Solution.*

(a) With $a=2, b=1$: $f_Y(y) = \dfrac{1}{|2|}f_X\!\left(\dfrac{y-1}{2}\right) = \dfrac{1}{2}e^{-(y-1)/2}$ for $y>1$.

(b) $F_Y(y) = P(2X+1\le y) = P\!\left(X \le \dfrac{y-1}{2}\right) = F_X\!\left(\dfrac{y-1}{2}\right) = 1-e^{-(y-1)/2}$ for $y>1$. Differentiating: $f_Y(y) = \dfrac{d}{dy}\left[1-e^{-(y-1)/2}\right] = \dfrac{1}{2}e^{-(y-1)/2}$, matching (a).

(c) By the probability integral transformation, $W=F_X(X) \sim Unif[0,1]$ immediately. Direct check: for $0<w<1$,
$$F_W(w) = P(1-e^{-X}\le w) = P(e^{-X}\ge 1-w) = P(X \le -\ln(1-w)) = F_X(-\ln(1-w)) = 1-e^{\ln(1-w)} = 1-(1-w) = w.$$
So $f_W(w)=1$ on $(0,1)$: confirmed uniform.
