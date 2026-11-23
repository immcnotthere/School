---
type: reference
parent: "[[STATS 131]]"
domain: stats
course: "STATS 131"
status: draft
source: "Notes_03"
tags:
  - decks
---
# STATS 131 Cards - Notes_03 Independence and Discrete Random Variables

## Independent Events
| Front | Back | Notes |
| --- | --- | --- |
| What is the definition of two independent events A and B (Definition 3.1)? | $P(A \cap B) = P(A)P(B)$; written $A \perp B$. | p.1; definition |
| What is the alternative (conditional probability) definition of independence, and what condition must hold for it? | Assuming $P(B) \neq 0$: $P(A \mid B) = P(A)$. | p.1; definition |
| If A and B are independent, what is true of their complements? | $A^c$ and $B^c$ are also independent. | p.3; concept |

## Mutually Exclusive vs Independent Events
| Front | Back | Notes |
| --- | --- | --- |
| In Example 3.2, why can two mutually exclusive events with $P(A)>0$, $P(B)>0$ never be independent? | Since $A \cap B = \emptyset$, $P(A \mid B) = \dfrac{P(A \cap B)}{P(B)} = \dfrac{0}{P(B)} = 0 \neq P(A)$. | p.2; procedure |

## Independence Check, Two Dice Rolls
| Front | Back | Notes |
| --- | --- | --- |
| In Example 3.3, how do you test whether $E_1=$ "first roll is 6" and $E_2=$ "second roll is 6" are independent? | Compute $P(E_1)=P(E_2)=1/6$, so $P(E_1)P(E_2)=1/36$; since $P(E_1 \cap E_2)=1/36$ as well, the events are independent. | p.2; procedure |

## Mutual Independence
| Front | Back | Notes |
| --- | --- | --- |
| What does it mean for events $A_1,\dots,A_n$ to be mutually independent (Definition 3.3)? | For every subset $S \subseteq \{1,\dots,n\}$, $P\left(\bigcap_{i \in S} A_i\right) = \prod_{i \in S} P(A_i)$. | p.2; definition |

## Pairwise Independence
| Front | Back | Notes |
| --- | --- | --- |
| What does it mean for events $A_1,\dots,A_n$ to be pairwise independent (Definition 3.4)? | For all $i \neq j$, $P(A_i \cap A_j) = P(A_i)P(A_j)$; every pair of events is independent. | p.2; definition |
| How does pairwise independence differ from mutual independence? | Pairwise only checks two events at a time; mutual independence requires the product rule to hold for every subset, including all events jointly. | p.2; discrimination |

## Pairwise Independent but Not Mutually Independent (Coin Toss)
| Front | Back | Notes |
| --- | --- | --- |
| In Example 3.4, how do you show A, B, C are pairwise but not mutually independent? | Each pair satisfies $P(A_i \cap A_j) = P(A_i)P(A_j) = 1/4$, but $P(A \cap B \cap C) = P(\emptyset) = 0 \neq P(A)P(B)P(C) = 1/8$. | p.3; procedure |

## Conditional Independence
| Front | Back | Notes |
| --- | --- | --- |
| What does it mean for A and B to be conditionally independent given C (Definition 3.5)? | Given $P(C) > 0$: $P(A \cap B \mid C) = P(A \mid C)P(B \mid C)$. | p.3; definition |

## Conditional Independence, Biased Coin
| Front | Back | Notes |
| --- | --- | --- |
| In Example 3.5, what is $P(A \cap B \mid C)$, the probability of two heads given the coin is biased with $P(H \mid C)=2/3$? | $P(A \cap B \mid C) = P(A \mid C)P(B \mid C) = \frac{2}{3}\cdot\frac{2}{3} = \frac{4}{9}$. | p.3; procedure |

## Random Variable
| Front | Back | Notes |
| --- | --- | --- |
| What is a random variable (Definition 3.6)? | A real-valued function $X:\Omega \to \mathbb{R}$ from the sample space $\Omega$ to the real numbers. | p.4; definition |
| For $\Omega=\{H,T\}$ with X counting heads, what are $X(H)$ and $X(T)$? | $X(H)=1$, $X(T)=0$. | p.4; procedure |
| What is the difference between an event and a random variable? | An event is a subset of the sample space $\Omega$; a random variable is a function mapping outcomes in $\Omega$ to real numbers. | p.4; discrimination |

## Probability distribution
| Front | Back | Notes |
| --- | --- | --- |
| What is the distribution of a random variable X (Definition 3.7)? | The collection of all probabilities $P(X \in E)$ for sets $E \subset \mathbb{R}$ such that $\{X \in E\}$ is an event. | p.4; definition |
| How is $P(X \in A)$ related to the probability measure on the sample space $\Omega$? | $P(X \in A) = P(\{s : X(s) \in A\})$. | p.4; formula |

## Discrete random variables
| Front | Back | Notes |
| --- | --- | --- |
| What does it mean for a random variable X to be discrete (Definition 3.8)? | X can take only a finite number $k$ of different values, or a countably infinite sequence of different values. | p.5; definition |
| Give an example of a discrete random variable from the notes. | Number of heads in coin tosses, or number of hurricanes in a year (each takes only countably many values). | p.5; definition |

## Continuous random variables
| Front | Back | Notes |
| --- | --- | --- |
| What does it mean for a random variable to have a continuous distribution (Definition 3.9)? | It can take every value in an interval, e.g. the height of a person. | p.5; definition |
| How does a discrete random variable differ from a continuous random variable? | Discrete: finitely many or countably infinitely many values; continuous: every value in an interval. | p.5; discrimination |

## PMF, PDF and CDF
| Front | Back | Notes |
| --- | --- | --- |
| For a discrete random variable X, what is the probability function (pf), also called the pmf? | $f(x) = P(X=x)$. | p.5; definition |
| What must be true of $\sum_x f(x)$ for a valid pmf? | $\sum_x f(x) = 1$. | p.5; formula |
| How do you compute $P(E)$ for an event E using the pmf $f(x)$? | $P(E) = \sum_{x \in E} f(x)$. | p.5; formula |

## Discrete Uniform Distribution
| Front | Back | Notes |
| --- | --- | --- |
| What is the pmf of a random variable X uniform on integers $a,\dots,b$ (Definition 3.11)? | $f(x) = \dfrac{1}{b-a+1}$ for $x=a,\dots,b$, and $0$ otherwise. | p.6; formula |
| What condition on X makes it uniformly distributed on the integers $a,\dots,b$? | Every integer from $a$ to $b$ is equally likely to be the value of X. | p.6; definition |

## Bernoulli Distribution
| Front | Back | Notes |
| --- | --- | --- |
| What is the pmf of a Bernoulli($p$) random variable (Definition 3.12)? | $f(x) = p^x(1-p)^{1-x}$ for $x=0,1$. | p.6; formula |
| For a Bernoulli($p$) random variable, what are $f(1)$ and $f(0)$ individually? | $f(1) = p$ and $f(0) = 1-p$. | p.6; procedure |
| What experiment does a Bernoulli($p$) random variable model? | A single trial (e.g. one coin flip) with probability $p$ of success (X=1) and $1-p$ of failure (X=0). | p.6; definition |

## Binomial Distribution
| Front | Back | Notes |
| --- | --- | --- |
| What is the pmf of a Binomial($n,p$) random variable (Definition 3.13)? | $f(x) = \binom{n}{x}p^x(1-p)^{n-x}$ for $x=0,1,\dots,n$. | p.6; formula |
| What experiment does a Binomial($n,p$) random variable model? | The number of heads (successes) in $n$ independent Bernoulli($p$) trials. | p.6; definition |
| What three conditions must hold to recognize a random variable as Binomial? | (1) It is the sum of $n$ independent Bernoulli trials, (2) $n$ is fixed (not random), (3) $p$ is fixed and constant across trials. | p.6; procedure |

## Binomial PMF Sums to One
| Front | Back | Notes |
| --- | --- | --- |
| In Example 3.8, what is the key move to show $\sum_x f(x)=1$ for the Binomial pmf? | Recognize the sum as the binomial theorem: $\sum_{x=0}^n \binom{n}{x}p^x(1-p)^{n-x} = (p+(1-p))^n = 1^n = 1$. | p.7; procedure |

## Poisson Distribution
| Front | Back | Notes |
| --- | --- | --- |
| What is the pmf of a Poisson($\lambda$) random variable (Definition 3.14)? | $f(x) = \dfrac{\lambda^x e^{-\lambda}}{x!}$ for $x=0,1,2,\dots$, and $0$ otherwise. | p.7; formula |
| What parameter defines a Poisson distribution, and what constraint must it satisfy? | The mean $\lambda$, which must satisfy $\lambda > 0$. | p.7; definition |

## Poisson PMF Sums to One
| Front | Back | Notes |
| --- | --- | --- |
| In Example 3.9, what is the key move to show $\sum_x f(x)=1$ for the Poisson pmf? | Factor out $e^{-\lambda}$ and recognize the remaining sum as the Taylor series for $e^{\lambda}$: $\sum_{x=0}^\infty \frac{\lambda^x e^{-\lambda}}{x!} = e^{-\lambda}\sum_{x=0}^\infty \frac{\lambda^x}{x!} = e^{-\lambda}e^{\lambda} = 1$. | p.7; procedure |

# Node map
```json
[
 {
  "name": "Independent Events",
  "type": "concept",
  "existing": false,
  "parent": "Independence",
  "prereqs": [
   "Conditional Probability"
  ],
  "uses": [],
  "page": 1,
  "summary": "Two events A and B are independent if $P(A \\cap B) = P(A)P(B)$; equivalently, if $P(B) \\neq 0$, $P(A \\mid B) = P(A)$."
 },
 {
  "name": "Mutually Exclusive vs Independent Events",
  "type": "problem",
  "existing": false,
  "parent": "Independence",
  "prereqs": [],
  "uses": [
   "Independent Events"
  ],
  "page": 2,
  "summary": "Two disjoint events with positive probability can never be independent, since their intersection probability is 0."
 },
 {
  "name": "Independence Check, Two Dice Rolls",
  "type": "problem",
  "existing": false,
  "parent": "Independence",
  "prereqs": [],
  "uses": [
   "Independent Events"
  ],
  "page": 2,
  "summary": "Tests whether pairs of events from two die rolls satisfy $P(E_1 \\cap E_2) = P(E_1)P(E_2)$."
 },
 {
  "name": "Mutual Independence",
  "type": "concept",
  "existing": false,
  "parent": "Independence",
  "prereqs": [
   "Independent Events"
  ],
  "uses": [],
  "page": 2,
  "summary": "Events $A_1,\\dots,A_n$ are mutually independent if the product rule holds for every subset of indices, not just pairs."
 },
 {
  "name": "Pairwise Independence",
  "type": "concept",
  "existing": false,
  "parent": "Independence",
  "prereqs": [
   "Independent Events",
   "Mutual Independence"
  ],
  "uses": [],
  "page": 2,
  "summary": "Events $A_1,\\dots,A_n$ are pairwise independent if every pair satisfies $P(A_i \\cap A_j) = P(A_i)P(A_j)$; weaker than mutual independence."
 },
 {
  "name": "Pairwise Independent but Not Mutually Independent (Coin Toss)",
  "type": "problem",
  "existing": false,
  "parent": "Independence",
  "prereqs": [],
  "uses": [
   "Independent Events",
   "Mutual Independence",
   "Pairwise Independence"
  ],
  "page": 3,
  "summary": "A classic coin-toss example where three events are pairwise independent but their triple intersection breaks the mutual independence product rule."
 },
 {
  "name": "Conditional Independence",
  "type": "concept",
  "existing": false,
  "parent": "Independence",
  "prereqs": [
   "Conditional Probability",
   "Independent Events"
  ],
  "uses": [],
  "page": 3,
  "summary": "A and B are conditionally independent given C (with $P(C)>0$) if $P(A \\cap B \\mid C) = P(A \\mid C)P(B \\mid C)$."
 },
 {
  "name": "Conditional Independence, Biased Coin",
  "type": "problem",
  "existing": false,
  "parent": "Independence",
  "prereqs": [],
  "uses": [
   "Conditional Independence",
   "Independent Events"
  ],
  "page": 3,
  "summary": "Uses conditional independence to compute the probability of two heads given a coin is known to be biased."
 },
 {
  "name": "Random Variable",
  "type": "concept",
  "existing": false,
  "parent": "Random variable",
  "prereqs": [],
  "uses": [],
  "page": 4,
  "summary": "A random variable is a real-valued function $X:\\Omega \\to \\mathbb{R}$ mapping outcomes in the sample space to real numbers."
 },
 {
  "name": "Probability distribution",
  "type": "concept",
  "existing": true,
  "parent": "Random variable",
  "prereqs": [
   "Random Variable"
  ],
  "uses": [],
  "page": 4,
  "summary": "The distribution of X is the collection of probabilities $P(X \\in E)$ for all sets E such that $\\{X \\in E\\}$ is an event."
 },
 {
  "name": "Discrete random variables",
  "type": "concept",
  "existing": false,
  "parent": "Random variable",
  "prereqs": [
   "Random Variable"
  ],
  "uses": [],
  "page": 5,
  "summary": "A random variable is discrete if it takes only finitely many, or countably infinitely many, distinct values."
 },
 {
  "name": "Continuous random variables",
  "type": "concept",
  "existing": false,
  "parent": "Random variable",
  "prereqs": [
   "Random Variable"
  ],
  "uses": [],
  "page": 5,
  "summary": "A random variable is continuous if it can take every value in an interval."
 },
 {
  "name": "PMF, PDF and CDF",
  "type": "concept",
  "existing": true,
  "parent": "Random variable",
  "prereqs": [
   "Discrete random variables"
  ],
  "uses": [],
  "page": 5,
  "summary": "For a discrete random variable X, the probability mass function is $f(x)=P(X=x)$, with $\\sum_x f(x)=1$ and $P(E)=\\sum_{x\\in E} f(x)$."
 },
 {
  "name": "Discrete Uniform Distribution",
  "type": "concept",
  "existing": false,
  "parent": "Common Distributions",
  "prereqs": [
   "PMF, PDF and CDF"
  ],
  "uses": [],
  "page": 6,
  "summary": "X is uniform on integers $a,\\dots,b$ if every value is equally likely, with pmf $f(x) = 1/(b-a+1)$."
 },
 {
  "name": "Bernoulli Distribution",
  "type": "concept",
  "existing": false,
  "parent": "Common Distributions",
  "prereqs": [
   "PMF, PDF and CDF"
  ],
  "uses": [],
  "page": 6,
  "summary": "Models a single trial with success probability $p$; pmf $f(x) = p^x(1-p)^{1-x}$ for $x=0,1$."
 },
 {
  "name": "Binomial Distribution",
  "type": "concept",
  "existing": false,
  "parent": "Common Distributions",
  "prereqs": [
   "Bernoulli Distribution",
   "Independent Events"
  ],
  "uses": [],
  "page": 6,
  "summary": "Counts successes in $n$ independent Bernoulli($p$) trials; pmf $f(x) = \\binom{n}{x}p^x(1-p)^{n-x}$."
 },
 {
  "name": "Binomial PMF Sums to One",
  "type": "problem",
  "existing": false,
  "parent": "Common Distributions",
  "prereqs": [],
  "uses": [
   "Binomial Distribution"
  ],
  "page": 7,
  "summary": "Shows $\\sum_x f(x)=1$ for the Binomial pmf using the binomial theorem."
 },
 {
  "name": "Poisson Distribution",
  "type": "concept",
  "existing": false,
  "parent": "Common Distributions",
  "prereqs": [
   "PMF, PDF and CDF"
  ],
  "uses": [],
  "page": 7,
  "summary": "Models counts with mean $\\lambda>0$; pmf $f(x) = \\lambda^x e^{-\\lambda}/x!$ for $x=0,1,2,\\dots$."
 },
 {
  "name": "Poisson PMF Sums to One",
  "type": "problem",
  "existing": false,
  "parent": "Common Distributions",
  "prereqs": [],
  "uses": [
   "Poisson Distribution",
   "Taylor Series"
  ],
  "page": 7,
  "summary": "Shows $\\sum_x f(x)=1$ for the Poisson pmf using the Taylor series for $e^{\\lambda}$."
 }
]
```

# Frankenstein problems

**Problem 1.** A factory machine produces defective items independently with probability $p=0.2$ per item. Five items are inspected; let X be the number of defective items among the five.

(a) Explain why $X \sim \text{Binomial}(5, 0.2)$, citing the recognition conditions.
(b) Compute $P(X=2)$.
(c) Let $A = \{\text{first item is defective}\}$ and $B = \{X=5\}$ (all five defective). Are A and B independent?

*Solution.*

(a) Each item's defect status is a Bernoulli(0.2) trial; the trials are independent, $n=5$ is fixed, and $p=0.2$ is constant across items. All three recognition conditions hold, so $X \sim \text{Binomial}(5,0.2)$.

(b) $P(X=2) = \binom{5}{2}(0.2)^2(0.8)^3 = 10 \times 0.04 \times 0.512 = 0.2048$.

(c) $P(A) = 0.2$. $P(B) = (0.2)^5 = 0.00032$. Since $B$ (all five defective) implies $A$ (first is defective), $A \cap B = B$, so $P(A \cap B) = 0.00032$. But $P(A)P(B) = 0.2 \times 0.00032 = 0.000064$. Since $0.00032 \neq 0.000064$, A and B are not independent.

*Concepts tested:* Bernoulli Distribution, Binomial Distribution, Independent Events.

---

**Problem 2.** A fair six-sided die (uniform on integers 1 to 6) is rolled twice, independently, giving $X_1$ and $X_2$. Let $A = \{X_1 = 6\}$, $B = \{X_2 = 6\}$, and $C = \{X_1+X_2 = 7\}$.

(a) Use the discrete uniform pmf to find $P(X_1=6)$.
(b) Verify $A$ and $B$ are independent using Definition 3.1.
(c) Find $P(C)$ by summing the joint pmf over the outcomes in C, then determine whether A and C are independent.

*Solution.*

(a) By the discrete uniform pmf, $f(x) = 1/(b-a+1) = 1/(6-1+1) = 1/6$, so $P(X_1=6) = 1/6$.

(b) $P(A)=P(B)=1/6$, so $P(A)P(B) = 1/36$. Since the rolls are independent, $P(A \cap B) = 1/36$ as well, matching $P(A)P(B)$, confirming $A \perp B$.

(c) The outcomes with $X_1+X_2=7$ are $(1,6),(2,5),(3,4),(4,3),(5,2),(6,1)$, each with joint probability $1/36$ (independent uniform rolls), so $P(C) = 6 \times \frac{1}{36} = \frac{1}{6}$. Now $A \cap C$ requires $X_1=6$ and $X_1+X_2=7$, i.e. $X_2=1$: only the outcome $(6,1)$, so $P(A \cap C) = 1/36$. Since $P(A)P(C) = \frac{1}{6}\cdot\frac{1}{6} = \frac{1}{36} = P(A \cap C)$, A and C are also independent.

*Concepts tested:* Discrete Uniform Distribution, Independent Events, PMF, PDF and CDF.
