---
type: reference
parent: "[[STATS 131]]"
domain: stats
course: "STATS 131"
status: draft
source: "Notes_08"
tags:
  - decks
---
# STATS 131 Cards - Notes_08 Variance, Covariance, and MGFs

## Variance (Math)
| Front | Back | Notes |
| --- | --- | --- |
| Define the variance $V(X)$ of a random variable $X$. | $V(X) = E[(X-E[X])^2]$, the expected squared deviation of $X$ from its mean | p.1; definition |
| What is the computational (shortcut) formula for $V(X)$ in terms of moments? | $V(X) = E[X^2] - (E[X])^2$ | p.1; formula |
| $X \sim \text{Bernoulli}(p)$: what is $V(X)$? | $V(X) = p(1-p)$ | p.2; formula |
| $X \sim \text{Uniform}(a,b)$: what is $V(X)$? | $V(X) = \dfrac{(b-a)^2}{12}$ | p.2; formula |

## Standard Deviation
| Front | Back | Notes |
| --- | --- | --- |
| Define the standard deviation $\sigma_X$ of $X$. | $\sigma_X = \sqrt{V(X)}$ | p.2; definition |
| How is $\sigma_X^2$ related to $V(X)$? | They are the same quantity: $\sigma_X^2 = V(X)$; standard deviation is just variance's square root, back in the original units of $X$ | p.2; discrimination |

## Properties of Variance
| Front | Back | Notes |
| --- | --- | --- |
| What is the sign restriction on $V(X)$ for any random variable $X$? | $V(X) \ge 0$ always; variance can never be negative | p.3; definition |
| When does $V(X) = 0$? | Iff $P(X=c)=1$ for some constant $c$ (X is degenerate) | p.3; definition |
| For constants $a,b$, what is $V(aX+b)$? | $V(aX+b) = a^2 V(X)$; shifting by $b$ does not change the variance | p.3; formula |

## Variance of a Sum of Independent Random Variables
| Front | Back | Notes |
| --- | --- | --- |
| If $X \perp Y$, what is $V(X+Y)$? | $V(X+Y) = V(X) + V(Y)$ | p.3; formula |
| If $X_1,\dots,X_n$ are independent, what is $V(X_1+\cdots+X_n)$? | $V(X_1+\cdots+X_n) = V(X_1)+\cdots+V(X_n)$ | p.3; formula |

## Variance of the Sample Mean
| Front | Back | Notes |
| --- | --- | --- |
| If $X_1,\dots,X_n$ are iid with variance $\sigma^2$, what is $V(\bar X)$ for $\bar X = \frac{1}{n}\sum_{i=1}^n X_i$? | $V(\bar X) = \dfrac{\sigma^2}{n}$ | p.4; formula |
| What two facts combine to derive $V(\bar X)=\sigma^2/n$ from $\bar X = \frac{1}{n}\sum X_i$? | $V(aX)=a^2V(X)$ with $a=1/n$, then variances add over the independent sum: $V(\bar X)=\frac{1}{n^2}\sum V(X_i)=\frac{1}{n^2}\cdot n\sigma^2=\sigma^2/n$ | p.4; procedure |

## Covariance
| Front | Back | Notes |
| --- | --- | --- |
| Define $\text{Cov}(X,Y)$. | $\text{Cov}(X,Y) = E[(X-E[X])(Y-E[Y])]$ | p.4; definition |
| What is the computational (shortcut) formula for $\text{Cov}(X,Y)$? | $\text{Cov}(X,Y) = E[XY] - E[X]E[Y]$ | p.5; formula |
| What does a positive vs. negative $\text{Cov}(X,Y)$ indicate about $X$ and $Y$? | Positive: above-average $X$ tends to occur with above-average $Y$ (positively correlated); negative: above-average $X$ tends to occur with below-average $Y$ (negatively correlated) | p.4; discrimination |

## Correlation
| Front | Back | Notes |
| --- | --- | --- |
| Define $\text{corr}(X,Y)$ in terms of covariance and variance. | $\text{corr}(X,Y) = \dfrac{\text{Cov}(X,Y)}{\sqrt{V(X)}\sqrt{V(Y)}}$ | p.6; formula |
| Why prefer correlation over covariance when comparing relationships across variables? | Covariance is not unit-free (it changes if you rescale units, e.g. feet vs. inches); correlation is unit-free and always lies in $[-1,1]$ | p.6; discrimination |

## Properties of Covariance
| Front | Back | Notes |
| --- | --- | --- |
| What is $\text{Cov}(X,X)$? | $\text{Cov}(X,X) = V(X)$ | p.6; definition |
| Contrast: what does $X \perp Y$ imply about $\text{Cov}(X,Y)$, versus what $\text{Cov}(X,Y)=0$ implies about independence? | $X \perp Y \Rightarrow \text{Cov}(X,Y)=0$, but the converse fails: zero covariance does not imply $X,Y$ are independent | p.6; discrimination |
| What is $V(X+Y)$ in general, with no independence assumption? | $V(X+Y) = V(X)+V(Y)+2\,\text{Cov}(X,Y)$ | p.6; formula |

## Conditional Expectation
| Front | Back | Notes |
| --- | --- | --- |
| How is $E[Y \mid X=x]$ computed when $Y\mid X=x$ is discrete vs. continuous? | Discrete: $E[Y\mid X=x] = \sum_y y\, f_{Y\mid X}(y\mid x)$; continuous: $E[Y\mid X=x] = \int y\, f_{Y\mid X}(y\mid x)\, dy$ | p.6; discrimination |
| For a fixed known value $x$, is $E[Y\mid X=x]$ a constant or a random variable, and what about $E[Y\mid X]$ (X left random)? | $E[Y\mid X=x]$ is a constant; $E[Y\mid X]$, as a function of the random $X$, is itself a random variable | p.7; discrimination |

## Law of Iterated Expectation (LIE)
| Front | Back | Notes |
| --- | --- | --- |
| State the Law of Iterated Expectation. | $E[E[Y\mid X]] = E[Y]$ | p.7; formula |
| Why does averaging $E[Y\mid X]$ over $X$'s distribution recover $E[Y]$? | $E[Y\mid X]$ is itself a random variable (a function of $X$); integrating/summing it over the distribution of $X$ reweights every case of $Y$ correctly, giving back the overall average | p.8; definition |

## Conditional Variance
| Front | Back | Notes |
| --- | --- | --- |
| Define $V(Y\mid X=x)$. | $V(Y\mid X=x) = E[(Y-E(Y\mid X=x))^2 \mid X=x]$ | p.8; definition |
| What is the computational (shortcut) formula for $V(Y\mid X=x)$? | $V(Y\mid X=x) = E[Y^2\mid X=x] - (E[Y\mid X=x])^2$ | p.8; formula |

## Law of Total Variance (Eve's Law)
| Front | Back | Notes |
| --- | --- | --- |
| State the Law of Total Variance (Eve's Law). | $V(Y) = E[V(Y\mid X)] + V[E(Y\mid X)]$ | p.9; formula |
| What do the two terms in Eve's Law represent? | $E[V(Y\mid X)]$: average within-group variance left over once $X$ is known; $V[E(Y\mid X)]$: variance between the group means, due to $X$ alone | p.9; discrimination |

## Moments and Central Moments
| Front | Back | Notes |
| --- | --- | --- |
| Define the $k$th moment of $X$. | $E[X^k]$ for $k=1,2,\dots$ | p.10; definition |
| Define the $k$th central moment of $X$. | $E[(X-E[X])^k]$ for $k=2,3,\dots$ | p.10; definition |
| The mean and the variance are which moments of $X$, respectively? | The mean is the 1st moment, $E[X]$; the variance is the 2nd central moment, $E[(X-E[X])^2]$ | p.10; discrimination |

## Moment Generating Function (MGF)
| Front | Back | Notes |
| --- | --- | --- |
| Define the moment generating function $\psi_X(t)$ of $X$. | $\psi_X(t) = E[e^{tX}]$ for any real $t$ | p.10; definition |
| What is $\psi_X(0)$ for any random variable $X$? | $\psi_X(0) = 1$, always | p.11; definition |
| If $\psi(t)<\infty$ on an open interval around $t=0$, how do you recover $E[X^k]$ from the mgf? | $E[X^k] = \psi^{(k)}(0)$, the $k$th derivative of $\psi(t)$ evaluated at $t=0$ | p.11; formula |
| Why is the mgf useful for identifying a distribution? | If two random variables have the same mgf, they follow the same distribution: the mgf, when it exists, uniquely determines the distribution | p.11; definition |

## MGF of a Linear Transformation
| Front | Back | Notes |
| --- | --- | --- |
| If $Y=aX+b$, how is $\psi_Y(t)$ expressed in terms of $\psi_X(t)$? | $\psi_Y(t) = e^{bt}\,\psi_X(at)$ | p.12; formula |
| Contrast the linear-transform mgf rule with the independent-sum mgf rule. | Linear transform ($Y=aX+b$, one variable): $\psi_Y(t)=e^{bt}\psi_X(at)$, a rescale-and-shift; independent sum ($Y=X_1+\cdots+X_n$): $\psi_Y(t)=\prod_i \psi_{X_i}(t)$, a product across variables | p.12 to p.13; discrimination |

## MGF of a Sum of Independent Random Variables
| Front | Back | Notes |
| --- | --- | --- |
| If $X_1,\dots,X_n$ are independent with mgfs $\psi_{X_i}(t)$, and $Y=X_1+\cdots+X_n$, what is $\psi_Y(t)$? | $\psi_Y(t) = \prod_{i=1}^n \psi_{X_i}(t)$ | p.13; formula |
| What happens to the product formula $\psi_Y(t)=\prod_i \psi_{X_i}(t)$ if $X_1,\dots,X_n$ are not independent? | It no longer holds in general; independence is required for the mgf of a sum to equal the product of the individual mgfs | p.13; discrimination |

## Coin Flip Game Variance
| Front | Back | Notes |
| --- | --- | --- |
| A coin flip pays \$5 for heads, \$0 for tails, giving winnings $X=5Z$ with $Z\sim\text{Bernoulli}(1/2)$. What is the key move to find $V(X)$? | $V(Z)=\tfrac12\left(1-\tfrac12\right)=\tfrac14$, so $V(X)=V(5Z)=5^2V(Z)=25\cdot\tfrac14=\tfrac{25}{4}$ | p.3; procedure |

## Binomial Second Moment via Variance Decomposition
| Front | Back | Notes |
| --- | --- | --- |
| $X\sim\text{Binomial}(n,p)$, written as $X=X_1+\cdots+X_n$ with iid $X_i\sim\text{Bernoulli}(p)$. What is the key move to find $E[X^2]$ without summing the pmf directly? | Compute $V(X)=np(1-p)$ from the independent sum, and also $V(X)=E[X^2]-(np)^2$; setting these equal gives $E[X^2]=np(1-p)+(np)^2$ | p.4; procedure |

## Covariance from a Joint PDF
| Front | Back | Notes |
| --- | --- | --- |
| $f(x,y)=2xy+\tfrac12$ on $[0,1]^2$. What is the key move to show $\text{Cov}(X,Y)=1/144$? | Get marginals to find $E[X]=E[Y]=7/12$, compute $E[XY]=\int_0^1\int_0^1 xy\,f(x,y)\,dx\,dy=50/144$, then $\text{Cov}(X,Y)=E[XY]-E[X]E[Y]=50/144-49/144=1/144$ | p.5; procedure |

## Conditional Expectation from a Joint PMF
| Front | Back | Notes |
| --- | --- | --- |
| $f_X(x)$: $0.1,0.2,0.3,0.2,0.2$ for $x=1,\dots,5$; $Y=\mathbb{1}[X\le 3]$. What is the key move to find $E[X\mid Y=1]$? | Restrict to $x=1,2,3$, divide each $f_X(x)$ by $P(Y=1)=0.6$, then take the weighted average: $E[X\mid Y=1]=1\cdot\tfrac{0.1}{0.6}+2\cdot\tfrac{0.2}{0.6}+3\cdot\tfrac{0.3}{0.6}=\tfrac{7}{3}$ | p.7; procedure |

## Conditional Expectation from a Joint PDF
| Front | Back | Notes |
| --- | --- | --- |
| $f(x,y)=x+y$ on $[0,1]^2$. What is the key move to compute $E[Y\mid X=\tfrac12]$? | Find $f_X(x)=x+\tfrac12$, form $f_{Y\mid X}(y\mid x)=\dfrac{x+y}{x+\tfrac12}$, then integrate: $E[Y\mid X=\tfrac12]=\int_0^1 y\left(y+\tfrac12\right)dy=\tfrac{7}{12}$ | p.7; procedure |

## Clinical Trial Successes via LIE
| Front | Back | Notes |
| --- | --- | --- |
| $X\mid p\sim\text{Binomial}(n,p)$ with $p\sim\text{Uniform}(0,1)$. What is the key move to find $E[X]$? | Apply LIE: $E[X]=E[E[X\mid p]]=E[np]=n\,E[p]=n\cdot\tfrac12$ | p.8; procedure |

## Nested Uniform Expectation via LIE
| Front | Back | Notes |
| --- | --- | --- |
| $X\sim\text{Unif}(0,1)$, $Y\mid X=x\sim\text{Unif}(x,1)$. What is the key move to find $E[Y]$? | $E[Y\mid X]=\tfrac{X+1}{2}$ (midpoint of $[X,1]$), then apply LIE: $E[Y]=E\left[\tfrac{X+1}{2}\right]=\tfrac12+\tfrac12E[X]=\tfrac12+\tfrac14=\tfrac34$ | p.8; procedure |

## Conditional Variance from a Joint PDF
| Front | Back | Notes |
| --- | --- | --- |
| $f(x,y)=x+y$ on $[0,1]^2$. What is the key move to find $V(Y\mid X)$? | Compute $E[Y\mid X]=\dfrac{x/2+1/3}{x+1/2}$ and $E[Y^2\mid X]=\dfrac{x/3+1/4}{x+1/2}$, then subtract: $V(Y\mid X)=E[Y^2\mid X]-(E[Y\mid X])^2$ | p.9; procedure |

## Store Sales via Law of Total Variance
| Front | Back | Notes |
| --- | --- | --- |
| $N$ customers with $E[N]=10, V(N)=10$; $X_i$ iid spending with $E[X_i]=5, V(X_i)=2$; $Y=\sum_{i=1}^N X_i$. What is the key move to find $V(Y)$? | Use $E[Y\mid N]=5N$, $V(Y\mid N)=2N$, then Eve's Law: $E[V(Y\mid N)]=E[2N]=20$ and $V[E(Y\mid N)]=V(5N)=25V(N)=250$, so $V(Y)=20+250=270$ | p.10; procedure |

## MGF of a Linear Transformation of an Exponential
| Front | Back | Notes |
| --- | --- | --- |
| $X\sim\text{Exponential}(1)$, $\psi_X(t)=\tfrac{1}{1-t}$; $Y=3-2X$. What is the key move to find $\psi_Y(t)$? | With $a=-2,b=3$: $\psi_Y(t)=e^{bt}\psi_X(at)=e^{3t}\cdot\dfrac{1}{1-(-2t)}=\dfrac{e^{3t}}{1+2t}$ | p.12; procedure |

## MGF of a Binomial via Independent Sum
| Front | Back | Notes |
| --- | --- | --- |
| $X\sim\text{Binomial}(n,p)$, $X=X_1+\cdots+X_n$ iid $\text{Bernoulli}(p)$ with mgf $1-p+pe^t$. What is the key move to find $\psi_X(t)$? | Multiply the mgfs of the $n$ independent Bernoullis: $\psi_X(t)=\prod_{i=1}^n(1-p+pe^t)=(1-p+pe^t)^n$ | p.13; procedure |
# Node map
```json
[
 {
  "name": "Variance (Math)",
  "type": "concept",
  "existing": true,
  "parent": "Expectation and Variance",
  "prereqs": [],
  "uses": [],
  "page": 1,
  "summary": "The variance of a random variable X is the expected squared deviation of X from its mean, $V(X)=E[(X-E[X])^2]=E[X^2]-(E[X])^2$; it measures spread around the mean."
 },
 {
  "name": "Standard Deviation",
  "type": "concept",
  "existing": false,
  "parent": "Expectation and Variance",
  "prereqs": [
   "Variance (Math)"
  ],
  "uses": [],
  "page": 2,
  "summary": "The standard deviation is the square root of the variance, $\\sigma_X=\\sqrt{V(X)}$, restoring the original units of X."
 },
 {
  "name": "Properties of Variance",
  "type": "concept",
  "existing": false,
  "parent": "Expectation and Variance",
  "prereqs": [
   "Variance (Math)"
  ],
  "uses": [],
  "page": 3,
  "summary": "Variance is always nonnegative, equals zero only for a constant random variable, and scales as $V(aX+b)=a^2V(X)$ under linear transformations."
 },
 {
  "name": "Variance of a Sum of Independent Random Variables",
  "type": "concept",
  "existing": false,
  "parent": "Expectation and Variance",
  "prereqs": [
   "Variance (Math)"
  ],
  "uses": [],
  "page": 3,
  "summary": "For independent random variables, variances add: $V(X+Y)=V(X)+V(Y)$, extending to any finite sum of independent variables."
 },
 {
  "name": "Variance of the Sample Mean",
  "type": "concept",
  "existing": false,
  "parent": "Expectation and Variance",
  "prereqs": [
   "Variance of a Sum of Independent Random Variables",
   "Properties of Variance"
  ],
  "uses": [],
  "page": 4,
  "summary": "For an iid sample of size n with variance $\\sigma^2$, the sample mean has variance $\\sigma^2/n$, shrinking toward 0 as n grows."
 },
 {
  "name": "Covariance",
  "type": "concept",
  "existing": true,
  "parent": "4.6 Covariance and Correlation",
  "prereqs": [
   "Variance (Math)"
  ],
  "uses": [],
  "page": 4,
  "summary": "Covariance measures how two random variables vary together, $\\text{Cov}(X,Y)=E[(X-E[X])(Y-E[Y])]=E[XY]-E[X]E[Y]$; positive means they tend to move together, negative means opposite."
 },
 {
  "name": "Correlation",
  "type": "concept",
  "existing": false,
  "parent": "4.6 Covariance and Correlation",
  "prereqs": [
   "Covariance",
   "Variance (Math)"
  ],
  "uses": [],
  "page": 6,
  "summary": "Correlation rescales covariance to be unit-free, $\\text{corr}(X,Y)=\\text{Cov}(X,Y)/\\sqrt{V(X)V(Y)}$, and always lies between -1 and 1."
 },
 {
  "name": "Properties of Covariance",
  "type": "concept",
  "existing": false,
  "parent": "4.6 Covariance and Correlation",
  "prereqs": [
   "Covariance",
   "Variance (Math)"
  ],
  "uses": [],
  "page": 6,
  "summary": "Covariance satisfies $\\text{Cov}(X,X)=V(X)$, is zero under independence (though the converse need not hold), and $V(X+Y)=V(X)+V(Y)+2\\text{Cov}(X,Y)$ in general."
 },
 {
  "name": "Conditional Expectation",
  "type": "concept",
  "existing": false,
  "parent": "4.7 Conditional Expectation",
  "prereqs": [
   "Conditional Probability"
  ],
  "uses": [],
  "page": 6,
  "summary": "The conditional expectation $E[Y\\mid X=x]$ averages Y over its conditional distribution given X=x, by summation (discrete) or integration (continuous)."
 },
 {
  "name": "Law of Iterated Expectation (LIE)",
  "type": "concept",
  "existing": false,
  "parent": "4.7 Conditional Expectation",
  "prereqs": [
   "Conditional Expectation"
  ],
  "uses": [],
  "page": 7,
  "summary": "The law of iterated expectation states $E[E[Y\\mid X]]=E[Y]$: averaging the conditional expectation over X's distribution recovers the overall expectation."
 },
 {
  "name": "Conditional Variance",
  "type": "concept",
  "existing": false,
  "parent": "4.7 Conditional Expectation",
  "prereqs": [
   "Conditional Expectation",
   "Variance (Math)"
  ],
  "uses": [],
  "page": 8,
  "summary": "The conditional variance $V(Y\\mid X=x)=E[Y^2\\mid X=x]-(E[Y\\mid X=x])^2$ measures the spread of Y within the subpopulation where X=x."
 },
 {
  "name": "Law of Total Variance (Eve's Law)",
  "type": "concept",
  "existing": false,
  "parent": "4.7 Conditional Expectation",
  "prereqs": [
   "Conditional Variance",
   "Law of Iterated Expectation (LIE)"
  ],
  "uses": [],
  "page": 9,
  "summary": "Eve's law decomposes total variance as $V(Y)=E[V(Y\\mid X)]+V[E(Y\\mid X)]$: within-group variance plus variance of the group means."
 },
 {
  "name": "Moments and Central Moments",
  "type": "concept",
  "existing": false,
  "parent": "Moment Generating Functions",
  "prereqs": [
   "Variance (Math)"
  ],
  "uses": [],
  "page": 10,
  "summary": "The kth moment of X is $E[X^k]$; the kth central moment is $E[(X-E[X])^k]$; the mean is the first moment and the variance is the second central moment."
 },
 {
  "name": "Moment Generating Function (MGF)",
  "type": "concept",
  "existing": false,
  "parent": "Moment Generating Functions",
  "prereqs": [
   "Moments and Central Moments"
  ],
  "uses": [],
  "page": 10,
  "summary": "The mgf $\\psi_X(t)=E[e^{tX}]$ encodes all the moments of X via its derivatives at 0, and uniquely determines X's distribution when it exists."
 },
 {
  "name": "MGF of a Linear Transformation",
  "type": "concept",
  "existing": false,
  "parent": "Moment Generating Functions",
  "prereqs": [
   "Moment Generating Function (MGF)"
  ],
  "uses": [],
  "page": 12,
  "summary": "If $Y=aX+b$, the mgf transforms as $\\psi_Y(t)=e^{bt}\\psi_X(at)$, rescaling the argument and applying an exponential shift factor."
 },
 {
  "name": "MGF of a Sum of Independent Random Variables",
  "type": "concept",
  "existing": false,
  "parent": "Moment Generating Functions",
  "prereqs": [
   "Moment Generating Function (MGF)"
  ],
  "uses": [],
  "page": 13,
  "summary": "For independent $X_1,\\dots,X_n$, the mgf of their sum is the product of their individual mgfs, $\\psi_Y(t)=\\prod_i \\psi_{X_i}(t)$."
 },
 {
  "name": "Coin Flip Game Variance",
  "type": "problem",
  "existing": false,
  "parent": "Expectation and Variance",
  "prereqs": [
   "Properties of Variance",
   "Variance (Math)"
  ],
  "uses": [
   "Properties of Variance",
   "Variance (Math)"
  ],
  "page": 3,
  "summary": "Find the variance of coin-flip winnings $X=5Z$ by writing X as a linear transform of a Bernoulli indicator Z and applying $V(aX+b)=a^2V(X)$."
 },
 {
  "name": "Binomial Second Moment via Variance Decomposition",
  "type": "problem",
  "existing": false,
  "parent": "Expectation and Variance",
  "prereqs": [
   "Variance of a Sum of Independent Random Variables",
   "Properties of Variance",
   "Variance (Math)"
  ],
  "uses": [
   "Variance of a Sum of Independent Random Variables",
   "Properties of Variance",
   "Variance (Math)"
  ],
  "page": 4,
  "summary": "Find $E[X^2]$ for $X\\sim\\text{Binomial}(n,p)$ indirectly, by computing V(X) two ways and solving for $E[X^2]$."
 },
 {
  "name": "Covariance from a Joint PDF",
  "type": "problem",
  "existing": false,
  "parent": "4.6 Covariance and Correlation",
  "prereqs": [
   "Covariance"
  ],
  "uses": [
   "Covariance"
  ],
  "page": 5,
  "summary": "Compute $\\text{Cov}(X,Y)=1/144$ for joint density $f(x,y)=2xy+1/2$ on the unit square by integrating for E[X], E[Y], and E[XY]."
 },
 {
  "name": "Conditional Expectation from a Joint PMF",
  "type": "problem",
  "existing": false,
  "parent": "4.7 Conditional Expectation",
  "prereqs": [
   "Conditional Expectation"
  ],
  "uses": [
   "Conditional Expectation"
  ],
  "page": 7,
  "summary": "Compute $E[X\\mid Y=1]$ for a discrete X by restricting the pmf to {1,2,3} and renormalizing by P(Y=1)."
 },
 {
  "name": "Conditional Expectation from a Joint PDF",
  "type": "problem",
  "existing": false,
  "parent": "4.7 Conditional Expectation",
  "prereqs": [
   "Conditional Expectation"
  ],
  "uses": [
   "Conditional Expectation"
  ],
  "page": 7,
  "summary": "Compute $E[Y\\mid X=1/2]$ for joint density $f(x,y)=x+y$ by finding the conditional density and integrating."
 },
 {
  "name": "Clinical Trial Successes via LIE",
  "type": "problem",
  "existing": false,
  "parent": "4.7 Conditional Expectation",
  "prereqs": [
   "Law of Iterated Expectation (LIE)",
   "Conditional Expectation"
  ],
  "uses": [
   "Law of Iterated Expectation (LIE)",
   "Conditional Expectation"
  ],
  "page": 8,
  "summary": "Find $E[X]$ for $X\\mid p\\sim\\text{Binomial}(n,p)$ with $p\\sim\\text{Uniform}(0,1)$ by applying LIE to $E[X\\mid p]=np$."
 },
 {
  "name": "Nested Uniform Expectation via LIE",
  "type": "problem",
  "existing": false,
  "parent": "4.7 Conditional Expectation",
  "prereqs": [
   "Law of Iterated Expectation (LIE)",
   "Conditional Expectation"
  ],
  "uses": [
   "Law of Iterated Expectation (LIE)",
   "Conditional Expectation"
  ],
  "page": 8,
  "summary": "Find $E[Y]$ for $Y\\mid X=x\\sim\\text{Unif}(x,1)$, $X\\sim\\text{Unif}(0,1)$, by computing $E[Y\\mid X]=(X+1)/2$ and applying LIE."
 },
 {
  "name": "Conditional Variance from a Joint PDF",
  "type": "problem",
  "existing": false,
  "parent": "4.7 Conditional Expectation",
  "prereqs": [
   "Conditional Variance",
   "Conditional Expectation"
  ],
  "uses": [
   "Conditional Variance",
   "Conditional Expectation"
  ],
  "page": 9,
  "summary": "Find $V(Y\\mid X)$ for joint density $f(x,y)=x+y$ by computing $E[Y\\mid X]$ and $E[Y^2\\mid X]$ and subtracting the square."
 },
 {
  "name": "Store Sales via Law of Total Variance",
  "type": "problem",
  "existing": false,
  "parent": "4.7 Conditional Expectation",
  "prereqs": [
   "Law of Total Variance (Eve's Law)",
   "Conditional Expectation",
   "Properties of Variance"
  ],
  "uses": [
   "Law of Total Variance (Eve's Law)",
   "Conditional Expectation",
   "Properties of Variance"
  ],
  "page": 10,
  "summary": "Find $V(Y)$ for a random sum $Y=\\sum_{i=1}^N X_i$ by applying Eve's law with $E[Y\\mid N]=5N$ and $V(Y\\mid N)=2N$."
 },
 {
  "name": "MGF of a Linear Transformation of an Exponential",
  "type": "problem",
  "existing": false,
  "parent": "Moment Generating Functions",
  "prereqs": [
   "MGF of a Linear Transformation",
   "Moment Generating Function (MGF)"
  ],
  "uses": [
   "MGF of a Linear Transformation",
   "Moment Generating Function (MGF)"
  ],
  "page": 12,
  "summary": "Find the mgf of $Y=3-2X$ for $X\\sim\\text{Exponential}(1)$ by applying $\\psi_Y(t)=e^{bt}\\psi_X(at)$ with a=-2, b=3."
 },
 {
  "name": "MGF of a Binomial via Independent Sum",
  "type": "problem",
  "existing": false,
  "parent": "Moment Generating Functions",
  "prereqs": [
   "MGF of a Sum of Independent Random Variables",
   "Moment Generating Function (MGF)"
  ],
  "uses": [
   "MGF of a Sum of Independent Random Variables",
   "Moment Generating Function (MGF)"
  ],
  "page": 13,
  "summary": "Find the mgf of $X\\sim\\text{Binomial}(n,p)$ by writing X as a sum of n iid Bernoulli(p) variables and multiplying their mgfs."
 }
]
```

# Frankenstein problems

**Frankenstein Problem 1.** Let $X_1 \sim \text{Bernoulli}(0.3)$ and $X_2 \sim \text{Uniform}(0,4)$ be independent, and let $Y = 2X_1 - 3X_2 + 5$. Find $V(Y)$ and $\text{Cov}(X_1, Y)$.

*Solution.* First, $V(X_1) = 0.3(0.7) = 0.21$ (Bernoulli variance) and $V(X_2) = \frac{(4-0)^2}{12} = \frac{4}{3}$ (Uniform variance). Since $X_1 \perp X_2$, $V(2X_1) = 4V(X_1)$ and $V(-3X_2) = 9V(X_2)$ add: $V(Y) = 4(0.21) + 9\left(\frac{4}{3}\right) = 0.84 + 12 = 12.84$.

For $\text{Cov}(X_1,Y)$, use the computational formula $\text{Cov}(X_1,Y)=E[X_1Y]-E[X_1]E[Y]$. Since $X_1$ is Bernoulli, $X_1^2=X_1$, so $E[X_1^2]=E[X_1]=0.3$. Since $X_1 \perp X_2$, $E[X_1X_2]=E[X_1]E[X_2]=0.3(2)=0.6$ (using $E[X_2]=(0+4)/2=2$). Then
$$E[X_1Y]=E[X_1(2X_1-3X_2+5)]=2E[X_1^2]-3E[X_1X_2]+5E[X_1]=2(0.3)-3(0.6)+5(0.3)=0.6-1.8+1.5=0.3.$$
Also $E[Y]=2(0.3)-3(2)+5=0.6-6+5=-0.4$. So $\text{Cov}(X_1,Y)=0.3-(0.3)(-0.4)=0.3+0.12=0.42$.

Concepts tested: Variance (Math) (Bernoulli and Uniform variance formulas), Properties of Variance (linear transformation $V(aX+b)=a^2V(X)$), Variance of a Sum of Independent Random Variables, Covariance (computational formula), Properties of Covariance (independence gives $E[X_1X_2]=E[X_1]E[X_2]$).

**Frankenstein Problem 2.** The number of daily orders $N$ has $E[N]=8, V(N)=6$. Each order's value $X_i$ is iid with $E[X_i]=25, V(X_i)=100$, independent of $N$ and of each other. Let $Y=\sum_{i=1}^N X_i$ be total daily revenue. Find $V(Y)$ and $\text{Cov}(N,Y)$.

*Solution.* Conditional on $N$, $E[Y\mid N]=25N$ and $V(Y\mid N)=100N$ (sum of $N$ iid terms). By Eve's Law:
$$E[V(Y\mid N)]=E[100N]=100(8)=800, \qquad V[E(Y\mid N)]=V(25N)=625V(N)=625(6)=3750,$$
so $V(Y)=800+3750=4550$.

For $\text{Cov}(N,Y)$, use $\text{Cov}(N,Y)=E[NY]-E[N]E[Y]$. First $E[Y]=E[E[Y\mid N]]=E[25N]=25(8)=200$ (LIE). For $E[NY]$, condition on $N$: $E[NY\mid N]=N\cdot E[Y\mid N]=N(25N)=25N^2$, so by LIE $E[NY]=25E[N^2]$. Since $E[N^2]=V(N)+(E[N])^2=6+64=70$, $E[NY]=25(70)=1750$. Then $\text{Cov}(N,Y)=1750-8(200)=1750-1600=150$. (Check: $\text{Cov}(N,25N)=25V(N)=25(6)=150$, matching.)

Concepts tested: Conditional Expectation, Law of Iterated Expectation (LIE), Conditional Variance, Law of Total Variance (Eve's Law), Covariance (computational formula), Variance (Math) ($E[N^2]=V(N)+(E[N])^2$).
