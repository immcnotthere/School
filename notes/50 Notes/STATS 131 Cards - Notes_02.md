---
type: reference
parent: "[[STATS 131]]"
domain: stats
course: "STATS 131"
status: draft
source: "Notes_02"
tags:
  - decks
---
# STATS 131 Cards - Notes_02 Counting and Conditional Probability

## Multiplication Rule (Counting)
| Front | Back | Notes |
| --- | --- | --- |
| Multiplication rule for counting: total outcomes for a $k$-stage experiment with $n_i$ options at stage $i$? | $\prod_{i=1}^k n_i$ | p.1; formula |
| Flip a coin and roll a die: total outcomes by the multiplication rule? | $2 \times 6 = 12$ | p.1; procedure |
| Rolling two dice: total number of outcomes by the multiplication rule? | $6 \times 6 = 36$ | p.1; procedure |

## Sampling With vs Without Replacement
| Front | Back | Notes |
| --- | --- | --- |
| Sampling with replacement: what happens to an item after it is selected? | It is returned to the pool, so it can be selected again | p.1; definition |
| Yes or no, and why: sampling without replacement: can the same item be selected twice? | No, each item is removed from the pool once selected | p.1; definition |
| Rolling two fair dice: is this sampling with or without replacement (as a model)? | With replacement; equivalent to rolling the same die independently twice | p.1; discrimination |

## Factorial
| Front | Back | Notes |
| --- | --- | --- |
| Definition of $n!$ for a positive integer $n$? | $n! = n \times (n-1) \times \cdots \times 2 \times 1$ | p.2; definition |
| What is $0!$ by definition? | $0! = 1$ | p.2; definition |
| Number of distinct orderings (permutations) of $n$ distinct elements? | $n!$ | p.2; formula |

## Factorial cancellation identity
| Front | Back | Notes |
| --- | --- | --- |
| How does $\dfrac{n!}{(n-k)!}$ simplify without computing full factorials? | $n(n-1)(n-2)\cdots(n-(k-1))$, the product of $k$ descending terms starting at $n$ | p.2; formula |
| Why does $n!/(n-k)!$ cancel down to a short product? | The $(n-k)!$ in the denominator cancels the bottom $(n-k)$ terms of $n!$, leaving only the top $k$ terms | p.2; procedure |

## Permutation count notation
| Front | Back | Notes |
| --- | --- | --- |
| Definition of $P_{n,k}$? | The number of ways to order $k$ elements chosen from $n$ items, without replacement | p.3; definition |
| Formula for $P_{n,k}$? | $P_{n,k} = \dfrac{n!}{(n-k)!}$ | p.3; formula |
| Yes or no, and why: in $P_{n,k}$, does order matter? | Yes, order matters | p.3; definition |
| What does $P_{n,n}$ simplify to? | $n!$ | p.3; formula |

## Choosing Officers and Arranging a Bookshelf (Permutations)
| Front | Back | Notes |
| --- | --- | --- |
| Key move: a club of 25 members picks an ordered president and secretary. Which count and value? | $P_{25,2} = 25!/23! = 25 \times 24 = 600$ | p.3; procedure |

## Birthday Problem
| Front | Back | Notes |
| --- | --- | --- |
| Birthday problem key move: with 100 students, $P(\text{at least 2 share a birthday})$? | $1 - P_{365,100}/365^{100} \approx 1 - 3\times10^{-7} \approx 0.9999997$ | p.4; procedure |

## Combination Number
| Front | Back | Notes |
| --- | --- | --- |
| Definition of a combination of $n$ elements taken $k$ at a time? | A subset of size $k$ chosen from $n$ elements without replacement, order doesn't matter | p.5; definition |
| Formula for $C_{n,k}$ (binomial coefficient $\binom{n}{k}$)? | $C_{n,k} = \dfrac{P_{n,k}}{k!} = \dfrac{n!}{(n-k)!\,k!}$ | p.5; formula |
| Why divide $P_{n,k}$ by $k!$ to get $C_{n,k}$? | Each unordered group of $k$ elements corresponds to $k!$ equivalent ordered permutations, so dividing removes that overcount | p.4; procedure |

## Binomial Coefficient Identities
| Front | Back | Notes |
| --- | --- | --- |
| $\binom{n}{0}$ and $\binom{n}{n}$ equal what? | $1$ | p.6; formula |
| Symmetry identity for binomial coefficients? | $\binom{n}{k} = \binom{n}{n-k}$ | p.6; formula |
| Pascal's rule: $\binom{n}{k} + \binom{n}{k-1} = ?$ | $\binom{n+1}{k}$ | p.6; formula |
| Vandermonde's identity? | $\binom{m+n}{k} = \sum_{j=0}^k \binom{m}{j}\binom{n}{k-j}$ | p.6; formula |

## Binomial Theorem
| Front | Back | Notes |
| --- | --- | --- |
| Binomial theorem statement? | $(x+y)^n = \sum_{k=0}^n \binom{n}{k} x^k y^{n-k}$ | p.5; formula |
| Sum of all binomial coefficients: $\sum_{k=0}^n \binom{n}{k} = ?$ | $2^n$, from setting $x=y=1$ in the binomial theorem | p.5; procedure |
| Expand $(x+y)^2$ using the binomial theorem? | $y^2 + 2xy + x^2$ | p.5; procedure |

## Full House Poker Probability
| Front | Back | Notes |
| --- | --- | --- |
| Full house key move: probability a 5-card hand from 52 cards is a full house? | $P = \dfrac{13\binom{4}{3}\cdot12\binom{4}{2}}{\binom{52}{5}} \approx 0.00144$ | p.6; procedure |

## Coin Toss Exactly k Heads
| Front | Back | Notes |
| --- | --- | --- |
| Fair coin tossed 10 times, key move for $P(\text{exactly 3 heads})$? | $\dbinom{10}{3}\big/2^{10}$ | p.6; procedure |

## Urn Sampling Without Replacement
| Front | Back | Notes |
| --- | --- | --- |
| Urn with 15 yellow and 30 blue balls, draw 10: key move for $P(\text{exactly 3 yellow})$? | $\dfrac{\binom{15}{3}\binom{30}{7}}{\binom{45}{10}}$ | p.7; procedure |

## Multinomial Coefficient
| Front | Back | Notes |
| --- | --- | --- |
| Number of ways to partition $n$ elements into groups of sizes $n_1,\dots,n_k$ (with $\sum n_i=n$)? | $\dbinom{n}{n_1,\dots,n_k} = \dfrac{n!}{n_1!\,n_2!\cdots n_k!}$ | p.7; formula |
| How is the combination number $C_{n,k}$ a special case of the multinomial coefficient? | It's the 2-group case, with group sizes $k$ and $n-k$ | p.7; discrimination |

## PEPPER Word Arrangements
| Front | Back | Notes |
| --- | --- | --- |
| Distinct arrangements of the letters in PEPPER ($n=6$: P appears 3 times, E 2 times, R once)? | $\dfrac{6!}{3!\,2!\,1!} = 60$ | p.7; procedure |

## Stars and Bars Argument
| Front | Back | Notes |
| --- | --- | --- |
| Stars and bars: ways to give $n$ cookies to $k$ kids so every kid gets at least one? | $\dbinom{n-1}{k-1}$ | p.8; formula |
| Stars and bars: ways to give $n$ cookies to $k$ kids if some kids may get zero? | $\dbinom{n+k-1}{k-1}$ | p.8; formula |
| In the zero-allowed case, why are there $n+k-1$ positions with $k-1$ chosen as bars? | There are $n$ stars and $k-1$ dividers to arrange in a row, so $n+k-1$ total slots hold the $k-1$ bars | p.8; procedure |

## Conditional Probability
| Front | Back | Notes |
| --- | --- | --- |
| Definition of $P(A\mid B)$ when $P(B)>0$? | $P(A\mid B) = \dfrac{P(A \cap B)}{P(B)}$ | p.9; definition |
| How do we interpret $P(A\mid B)$ versus $P(A)$? | $P(A)$ is the prior probability of $A$; $P(A\mid B)$ is the posterior probability of $A$ after learning $B$ occurred | p.9; discrimination |
| Why does conditioning on "the first calf is a bull" give a different answer than "at least one calf is a bull"? | "At least one" includes both mixed-order outcomes (bull-heifer and heifer-bull), which dilutes the two-bull outcome more than fixing one specific calf | p.10; discrimination |

## Multiplication Rule (General)
| Front | Back | Notes |
| --- | --- | --- |
| General multiplication rule for two events? | $P(A \cap B) = P(A\mid B)P(B)$ | p.10; formula |
| Chain rule for the intersection of events $A_1,\dots,A_n$? | $P(\cap_{i=1}^n A_i) = P(A_1)P(A_2\mid A_1)P(A_3\mid A_1\cap A_2)\cdots P(A_n\mid \cap_{i=1}^{n-1}A_i)$ | p.10; formula |

## Bayes' Rule
| Front | Back | Notes |
| --- | --- | --- |
| Bayes' rule formula for $P(A\mid B)$? | $P(A\mid B) = \dfrac{P(B\mid A)P(A)}{P(B)}$ | p.11; formula |
| How to expand the denominator $P(B)$ in Bayes' rule using $A$ and $A^c$? | $P(B) = P(B\mid A)P(A) + P(B\mid A^c)P(A^c)$ | p.11; formula |

## Law of Total Probability
| Front | Back | Notes |
| --- | --- | --- |
| Law of total probability: if $\{B_j\}$ partition $\Omega$, then $P(A) = ?$ | $\sum_{j=1}^k P(B_j)P(A\mid B_j)$ | p.11; formula |
| Conditional version of the law of total probability, given event $C$? | $P(A\mid C) = \sum_{j=1}^k P(B_j\mid C)P(A\mid B_j \cap C)$ | p.11; formula |

## Conditional Probability Special Cases
| Front | Back | Notes |
| --- | --- | --- |
| If $A \subset B$ with $P(B)>0$, what is $P(A\mid B)$? | $P(A)/P(B)$ | p.12; formula |
| If $A$ and $B$ are disjoint with $P(B)>0$, what is $P(A\mid B)$? | $0$ | p.12; formula |
| If $P(A)>0$, what is $P(A\mid A)$? | $1$ | p.12; formula |

## Conditional Probability from a Venn Diagram
| Front | Back | Notes |
| --- | --- | --- |
| Venn diagram key move: given $P(A\cap B)=2/16$ and $P(B)=5/16$, find $P(A\mid B)$? | $(2/16)/(5/16) = 2/5$ | p.9; procedure |

## Two Offspring, At Least One Bull
| Front | Back | Notes |
| --- | --- | --- |
| Cindy has 2 calves and at least one is a bull. Key move for $P(\text{both bulls}\mid \text{at least one bull})$? | $\dfrac{P(\text{both bulls})}{P(\text{at least one bull})} = \dfrac{1/4}{3/4} = 1/3$ | p.9; procedure |

## Two Offspring, First Born Is a Bull
| Front | Back | Notes |
| --- | --- | --- |
| Cindy has 2 calves and the first born is a bull. Key move for $P(\text{both bulls}\mid \text{first is a bull})$? | $\dfrac{P(\text{both bulls and first is a bull})}{P(\text{first is a bull})} = \dfrac{1/4}{2/4} = 1/2$ | p.10; procedure |

## Rare Disease Bayes Rule
| Front | Back | Notes |
| --- | --- | --- |
| Rare disease: $P(D=1)=0.01$, $P(T=1\mid D=1)=P(T=0\mid D=0)=0.95$. Key move for $P(D=1\mid T=1)$? | $\dfrac{0.95\times0.01}{0.95\times0.01+0.05\times0.99} = \dfrac{0.0095}{0.059}\approx0.161$ | p.12; procedure |
# Node map
```json
[
 {
  "name": "Multiplication Rule (Counting)",
  "type": "concept",
  "existing": false,
  "parent": "Counting Methods",
  "prereqs": [],
  "uses": [],
  "page": 1,
  "summary": "For a multi-stage experiment where stage $i$ has $n_i$ options, the total number of outcomes is $\\prod_i n_i$."
 },
 {
  "name": "Sampling With vs Without Replacement",
  "type": "concept",
  "existing": false,
  "parent": "Counting Methods",
  "prereqs": [],
  "uses": [],
  "page": 1,
  "summary": "With replacement, a selected item is returned to the pool before the next draw; without replacement, it is removed and cannot be chosen again."
 },
 {
  "name": "Factorial",
  "type": "concept",
  "existing": false,
  "parent": "Counting Methods",
  "prereqs": [],
  "uses": [],
  "page": 2,
  "summary": "$n! = n(n-1)\\cdots2\\cdot1$ with $0!=1$; it counts the number of distinct orderings of $n$ elements."
 },
 {
  "name": "Factorial cancellation identity",
  "type": "concept",
  "existing": true,
  "parent": "Permutations, Falling Factorials, and No-Repeat Probabilities",
  "prereqs": [
   "Factorial"
  ],
  "uses": [],
  "page": 2,
  "summary": "$n!/(n-k)!$ collapses to the product $n(n-1)\\cdots(n-k+1)$ of $k$ descending terms, since the denominator cancels the rest of $n!$."
 },
 {
  "name": "Permutation count notation",
  "type": "concept",
  "existing": true,
  "parent": "Permutations, Falling Factorials, and No-Repeat Probabilities",
  "prereqs": [
   "Factorial",
   "Factorial cancellation identity"
  ],
  "uses": [],
  "page": 3,
  "summary": "$P_{n,k}=n!/(n-k)!$ is the number of ordered selections of $k$ items from $n$ without replacement; order matters and $P_{n,n}=n!$."
 },
 {
  "name": "Combination Number",
  "type": "concept",
  "existing": false,
  "parent": "Combinations",
  "prereqs": [
   "Permutation count notation",
   "Factorial"
  ],
  "uses": [],
  "page": 5,
  "summary": "$C_{n,k}=\\binom{n}{k}=n!/((n-k)!k!)$ counts unordered subsets of size $k$ from $n$ elements, obtained by dividing $P_{n,k}$ by the $k!$ orderings of each subset."
 },
 {
  "name": "Binomial Coefficient Identities",
  "type": "concept",
  "existing": false,
  "parent": "Combinations",
  "prereqs": [
   "Combination Number"
  ],
  "uses": [],
  "page": 6,
  "summary": "Key binomial coefficient facts: $\\binom{n}{0}=\\binom{n}{n}=1$, symmetry $\\binom{n}{k}=\\binom{n}{n-k}$, Pascal's rule $\\binom{n}{k}+\\binom{n}{k-1}=\\binom{n+1}{k}$, and Vandermonde's identity $\\binom{m+n}{k}=\\sum_j\\binom{m}{j}\\binom{n}{k-j}$."
 },
 {
  "name": "Binomial Theorem",
  "type": "concept",
  "existing": false,
  "parent": "Combinations",
  "prereqs": [
   "Combination Number"
  ],
  "uses": [],
  "page": 5,
  "summary": "$(x+y)^n=\\sum_{k=0}^n \\binom{n}{k}x^k y^{n-k}$; setting $x=y=1$ gives $\\sum_k\\binom{n}{k}=2^n$."
 },
 {
  "name": "Multinomial Coefficient",
  "type": "concept",
  "existing": false,
  "parent": "Partitions",
  "prereqs": [
   "Combination Number",
   "Factorial"
  ],
  "uses": [],
  "page": 7,
  "summary": "The number of ways to partition $n$ elements into groups of sizes $n_1,\\dots,n_k$ is $n!/(n_1!\\cdots n_k!)$; the combination number is the 2-group special case."
 },
 {
  "name": "Stars and Bars Argument",
  "type": "concept",
  "existing": false,
  "parent": "Stars and Bars",
  "prereqs": [
   "Combination Number"
  ],
  "uses": [],
  "page": 8,
  "summary": "Ways to distribute $n$ identical items into $k$ distinguishable bins: $\\binom{n-1}{k-1}$ if every bin must get at least one, or $\\binom{n+k-1}{k-1}$ if bins may be empty."
 },
 {
  "name": "Conditional Probability",
  "type": "concept",
  "existing": true,
  "parent": "Conditional Probability",
  "prereqs": [],
  "uses": [],
  "page": 9,
  "summary": "$P(A\\mid B)=P(A\\cap B)/P(B)$ for $P(B)>0$; it updates the prior $P(A)$ into a posterior given that $B$ occurred."
 },
 {
  "name": "Multiplication Rule (General)",
  "type": "concept",
  "existing": true,
  "parent": "Conditional Probability",
  "prereqs": [
   "Conditional Probability"
  ],
  "uses": [],
  "page": 10,
  "summary": "$P(A\\cap B)=P(A\\mid B)P(B)$, generalizing to a chain rule $P(\\cap_i A_i)=P(A_1)P(A_2\\mid A_1)P(A_3\\mid A_1\\cap A_2)\\cdots$ for any number of events."
 },
 {
  "name": "Bayes' Rule",
  "type": "concept",
  "existing": true,
  "parent": "Conditional Probability",
  "prereqs": [
   "Conditional Probability",
   "Multiplication Rule (General)"
  ],
  "uses": [],
  "page": 11,
  "summary": "$P(A\\mid B)=P(B\\mid A)P(A)/P(B)$, where $P(B)=P(B\\mid A)P(A)+P(B\\mid A^c)P(A^c)$."
 },
 {
  "name": "Law of Total Probability",
  "type": "concept",
  "existing": false,
  "parent": "Conditional Probability",
  "prereqs": [
   "Conditional Probability",
   "Multiplication Rule (General)"
  ],
  "uses": [],
  "page": 11,
  "summary": "If $\\{B_j\\}$ partitions $\\Omega$, then $P(A)=\\sum_j P(B_j)P(A\\mid B_j)$, with a conditional version $P(A\\mid C)=\\sum_j P(B_j\\mid C)P(A\\mid B_j\\cap C)$."
 },
 {
  "name": "Conditional Probability Special Cases",
  "type": "concept",
  "existing": false,
  "parent": "Conditional Probability",
  "prereqs": [
   "Conditional Probability"
  ],
  "uses": [],
  "page": 12,
  "summary": "If $A\\subset B$, $P(A\\mid B)=P(A)/P(B)$; if $A,B$ disjoint, $P(A\\mid B)=0$; and $P(A\\mid A)=1$."
 },
 {
  "name": "Choosing Officers and Arranging a Bookshelf (Permutations)",
  "type": "problem",
  "existing": false,
  "parent": "Permutations, Falling Factorials, and No-Repeat Probabilities",
  "prereqs": [],
  "uses": [
   "Permutation count notation"
  ],
  "page": 3,
  "summary": "Counting ordered selections: choosing a president and secretary from 25 members ($P_{25,2}=600$), and arranging 10 books on a shelf ($P_{10,10}=10!$)."
 },
 {
  "name": "Birthday Problem",
  "type": "problem",
  "existing": false,
  "parent": "Permutations, Falling Factorials, and No-Repeat Probabilities",
  "prereqs": [
   "Complement Rule and De Morgan"
  ],
  "uses": [
   "Permutation count notation",
   "Multiplication Rule (Counting)"
  ],
  "page": 4,
  "summary": "With 100 students, $P(\\text{at least 2 share a birthday}) = 1-P_{365,100}/365^{100}\\approx0.9999997$, computed via the complement and the permutation count."
 },
 {
  "name": "Full House Poker Probability",
  "type": "problem",
  "existing": false,
  "parent": "Combinations",
  "prereqs": [],
  "uses": [
   "Combination Number",
   "Multiplication Rule (Counting)"
  ],
  "page": 6,
  "summary": "Probability a 5-card hand is a full house: $13\\binom{4}{3}\\cdot12\\binom{4}{2}$ favorable hands over $\\binom{52}{5}$ total, $\\approx0.00144$."
 },
 {
  "name": "Coin Toss Exactly k Heads",
  "type": "problem",
  "existing": false,
  "parent": "Combinations",
  "prereqs": [],
  "uses": [
   "Combination Number"
  ],
  "page": 6,
  "summary": "For 10 fair coin tosses, $P(\\text{exactly 3 heads})=\\binom{10}{3}/2^{10}$; the at-most-3-heads probability sums this term with the 0,1,2-heads terms."
 },
 {
  "name": "Urn Sampling Without Replacement",
  "type": "problem",
  "existing": false,
  "parent": "Combinations",
  "prereqs": [],
  "uses": [
   "Combination Number"
  ],
  "page": 7,
  "summary": "Drawing 10 balls from an urn of 15 yellow and 30 blue, $P(\\text{exactly 3 yellow})=\\binom{15}{3}\\binom{30}{7}/\\binom{45}{10}$."
 },
 {
  "name": "PEPPER Word Arrangements",
  "type": "problem",
  "existing": false,
  "parent": "Partitions",
  "prereqs": [],
  "uses": [
   "Multinomial Coefficient"
  ],
  "page": 7,
  "summary": "Distinct rearrangements of PEPPER's 6 letters (P:3, E:2, R:1) is $6!/(3!2!1!)=60$."
 },
 {
  "name": "Conditional Probability from a Venn Diagram",
  "type": "problem",
  "existing": false,
  "parent": "Conditional Probability",
  "prereqs": [],
  "uses": [
   "Conditional Probability"
  ],
  "page": 9,
  "summary": "Reading region probabilities off a Venn diagram ($P(A\\cap B)=2/16$, $P(B)=5/16$) to compute $P(A\\mid B)=2/5$."
 },
 {
  "name": "Two Offspring, At Least One Bull",
  "type": "problem",
  "existing": false,
  "parent": "Conditional Probability",
  "prereqs": [],
  "uses": [
   "Conditional Probability"
  ],
  "page": 9,
  "summary": "Given at least one of Cindy's 2 calves is a bull, $P(\\text{both bulls}) = (1/4)/(3/4) = 1/3$."
 },
 {
  "name": "Two Offspring, First Born Is a Bull",
  "type": "problem",
  "existing": false,
  "parent": "Conditional Probability",
  "prereqs": [],
  "uses": [
   "Conditional Probability"
  ],
  "page": 10,
  "summary": "Given the first-born of Cindy's 2 calves is a bull, $P(\\text{both bulls}) = (1/4)/(2/4) = 1/2$, contrasting with the 'at least one' version."
 },
 {
  "name": "Rare Disease Bayes Rule",
  "type": "problem",
  "existing": false,
  "parent": "Conditional Probability",
  "prereqs": [],
  "uses": [
   "Bayes' Rule",
   "Law of Total Probability",
   "Multiplication Rule (General)"
  ],
  "page": 12,
  "summary": "With disease rate 1% and test accuracy 95%, a positive test gives $P(D=1\\mid T=1)\\approx0.161$, illustrating why Bayes' rule matters for rare diseases."
 }
]
```

# Frankenstein problems

**Problem 1.** STAT 132 has 30 students available for a study-group committee: 12 freshmen, 10 sophomores, 8 juniors. A committee of 4 students is selected uniformly at random, without replacement.

(a) How many different committees of 4 are possible?
(b) What is the probability the committee has exactly 2 freshmen and 2 sophomores (no juniors)?
(c) Given that the committee has no juniors at all, what is the probability it has exactly 2 freshmen and 2 sophomores?

*Concepts tested:* Combination Number, Multiplication Rule (Counting), Conditional Probability.

*Solution.*

(a) Order doesn't matter for a committee, so use the combination number with $n=30$, $k=4$:
$$C_{30,4} = \binom{30}{4} = \frac{30\cdot29\cdot28\cdot27}{4!} = \frac{657720}{24} = 27405.$$

(b) Choosing 2 freshmen from 12 and 2 sophomores from 10 are two independent stages of a selection, so by the multiplication rule for counting the number of favorable committees is
$$\binom{12}{2}\binom{10}{2} = 66\times45 = 2970.$$
So
$$P(\text{2 fresh, 2 soph}) = \frac{2970}{27405} = \frac{22}{203} \approx 0.1084.$$

(c) "No juniors" means all 4 members come from the 22 non-juniors (12 freshmen + 10 sophomores):
$$\binom{22}{4} = \frac{22\cdot21\cdot20\cdot19}{24} = \frac{175560}{24} = 7315.$$
By the definition of conditional probability, restrict to this smaller sample space:
$$P(\text{2 fresh, 2 soph}\mid \text{no juniors}) = \frac{\binom{12}{2}\binom{10}{2}}{\binom{22}{4}} = \frac{2970}{7315} = \frac{54}{133} \approx 0.4060.$$

(Arithmetic double-checked: $30\cdot29\cdot28\cdot27=657720$; $657720/24=27405$. $66\times45=2970$. $22\cdot21\cdot20\cdot19=175560$; $175560/24=7315$. $2970/7315$ reduces by 5 to $594/1463$, then by 11 to $54/133$.)

---

**Problem 2.** Three urns are used in a game. Urn 1 has 3 red and 2 blue balls; Urn 2 has 4 red and 4 blue balls; Urn 3 has 1 red and 5 blue balls. An urn is chosen at random (each with probability $1/3$), then 2 balls are drawn from that urn without replacement.

(a) What is the probability that both balls drawn are red?
(b) Given that both balls drawn are red, what is the probability that Urn 1 was chosen?

*Concepts tested:* Combination Number, Law of Total Probability, Bayes' Rule.

*Solution.*

First find $P(\text{2 red}\mid \text{urn } i)$ using the combination number for each urn (order doesn't matter when drawing 2 balls):
$$P(\text{2 red}\mid U_1) = \frac{\binom{3}{2}}{\binom{5}{2}} = \frac{3}{10}, \qquad P(\text{2 red}\mid U_2) = \frac{\binom{4}{2}}{\binom{8}{2}} = \frac{6}{28} = \frac{3}{14}, \qquad P(\text{2 red}\mid U_3) = \frac{\binom{1}{2}}{\binom{6}{2}} = \frac{0}{15} = 0$$
(Urn 3 has only 1 red ball, so drawing 2 reds from it is impossible.)

(a) By the law of total probability, with $P(U_i)=1/3$ for each urn:
$$P(\text{2 red}) = \frac{1}{3}\left(\frac{3}{10}\right) + \frac{1}{3}\left(\frac{3}{14}\right) + \frac{1}{3}(0) = \frac{1}{3}\left(\frac{21}{70}+\frac{15}{70}\right) = \frac{1}{3}\cdot\frac{36}{70} = \frac{36}{210} = \frac{6}{35} \approx 0.1714.$$

(b) By Bayes' rule:
$$P(U_1 \mid \text{2 red}) = \frac{P(\text{2 red}\mid U_1)P(U_1)}{P(\text{2 red})} = \frac{(3/10)(1/3)}{6/35} = \frac{1/10}{6/35} = \frac{1}{10}\cdot\frac{35}{6} = \frac{35}{60} = \frac{7}{12} \approx 0.5833.$$

(Arithmetic double-checked: $3/10=21/70$, $3/14=15/70$, sum $=36/70=18/35$, times $1/3=6/35$. Then $(1/10)/(6/35) = 35/60 = 7/12$.)
