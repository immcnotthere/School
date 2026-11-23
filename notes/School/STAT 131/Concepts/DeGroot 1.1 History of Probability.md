---
title: 1.1 Randomness
aliases:
  - "1.1"
  - Randomness (1.1)
  - STAT 131 1.1
course: "STAT 131"
module: "1"
section: "1.1"
topics:
  - Randomness
  - Probability
  - Variability
  - Uncertainty
tags:
  - stats131
  - probability
  - foundations
  - randomness
  - statistics
  - Stats
  - history
  - Probability_Theory
  - tags/probability
  - DeGroot
  - Undergrad
type: concept
parent: "[[DeGroot Probability Theory]]"
domain: math
status: draft
---
## 1.1.1 Applications across time
> The use of probability to measure uncertainty and variability dates back hundreds of years. Probability has found application in areas as diverse as medicine, gambling, weather forecasting, and the law.

/tldr; [[Variability]] and [[Uncertainty]] has been measured by probability for ages

## 1.1.2 History of Statistics 

>The concepts of chance and uncertainty are as old as civilization itself. People have always had to cope with uncertainty about the weather, their food supply, and other aspects of their environment, and have striven to reduce this uncertainty and its effects. Even the idea of gambling has a long history. By about the year 3500 b.c., games of chance played with bone objects that could be considered precursors of dice were apparently highly developed in Egypt and elsewhere. Cubical dice with markings virtually identical to those on modern dice have been found in Egyptian tombs dating from 2000 b.c. We know that gambling with dice has been popular ever since that time and played an important part in the early development of probability theory.

tldr; Probability theory grew out of ancient games of [[Chance|chance]] and practical needs to manage uncertainty. It provides a shared mathematical [[Calculus|calculus]] for quantifying [[Randomness]] and [[Variability]], even though interpretations of what probability “means” can differ.

## 1.1.3 Origins of Probability Theory in Gambling
>It is generally believed that the mathematical theory of probability was started by the French mathematicians Blaise Pascal (1623–1662) and Pierre Fermat (1601–1665) when they succeeded in deriving exact probabilities for certain gambling problems involving dice. Some of the problems that they solved had been outstanding for about 300 years. However, numerical probabilities of various dice combinations had been calculated previously by Girolamo Cardano (1501–1576) and Galileo Galilei (1564– 1642)

tldr; Modern [[Probability theory]] is commonly traced to [[Blaise Pascal]] and [[Pierre de Fermat]], who derived exact results for long-standing [[dice]] and [[gambling]] problems, while earlier figures like [[Girolamo Cardano]] and [[Galileo Galilei]] had already computed numerical probabilities for specific dice combinations, showing the field moved from ad hoc calculation to systematic theory.

### 1.2i. Definition: [[Frequency Interpretation]]

The probability of an outcome is the relative frequency with which that outcome would be obtained if the process were repeated a large number of times under similar conditions2.

### 1.2ii. Definition: [[Classical Interpretation]]

Based on the concept of equally likely outcomes. If an experiment has $n$ equally likely outcomes, the probability of each is $1/n$ 3.

### 1.2iii. Definition: [[Subjective Interpretation]]

The probability that a person assigns to a possible outcome represents their own judgment of the likelihood that the outcome will be obtained, based on beliefs and information 4.

---

### 1.3 Experiments and Events

#### **1.3a.** Probability pertains to the possible outcomes of a process.

1.3i. Definition: [[Experiment]]

Any process, real or hypothetical, in which the possible outcomes can be identified ahead of time5.

1.3ii. Definition: [[Event]]

A well-defined set of possible outcomes of the experiment6.

---

### 1.4 Set Theory

**1.4a.** We use set theory to model experiments mathematically. Outcomes are elements, and events are subsets.

1.4i. Definition: [[Sample Space]]

The collection of all possible outcomes of an experiment, denoted by $S$7.

1.4ii. Definition: [[Empty Set]]

The subset of $S$ that contains no elements, denoted by $\emptyset$. In terms of events, it is an event that cannot occur8.

**1.4b.** Relationships between events are described using set operations.

- **Containment:** $A \subset B$ means if A occurs, so does B9.
    
- **Complement:** $A^c$ is the event that A does _not_ occur10.
    
- **Union:** $A \cup B$ is the event that either A or B or both occur11.
    
- **Intersection:** $A \cap B$ is the event that both A and B occur12.
    

1.4iii. Definition: [[Disjoint]]

Two events A and B are disjoint (or mutually exclusive) if they have no outcomes in common, meaning they cannot both occur.

$$A \cap B = \emptyset$$

13

Theorem 1.4.9: [[DeMorgan's Law|De Morgan's Laws]]

For every two sets A and B:

$$(A \cup B)^c = A^c \cap B^c$$

$$(A \cap B)^c = A^c \cup B^c$$

14

Theorem 1.4.11: [[Partitioning a Set]]

For every two sets A and B, A can be partitioned into disjoint sets:

$$A = (A \cap B) \cup (A \cap B^c)$$

15

---

### 1.5 The Definition of Probability

**1.5a.** A probability measure is defined by three axioms that ensure the numbers assigned to events behave consistently.

Axiom 1: [[Nonnegativity]]

For every event A, $Pr(A) \ge 0$16.

Axiom 2: [[Normalization]]

If an event is certain to occur (the sample space S), its probability is 1.

$$Pr(S) = 1$$

17

Axiom 3: [[Countable Additivity]]

For every infinite sequence of disjoint events $A_1, A_2, \dots$:

$$Pr\left(\bigcup_{i=1}^{\infty}A_{i}\right)=\sum_{i=1}^{\infty}Pr(A_{i})$$

18

Theorem 1.5.3: [[Complement Rule]]

$$Pr(A^c) = 1 - Pr(A)$$

19

Theorem 1.5.7: [[Addition Rule]]

For any two events A and B (not necessarily disjoint):

$$Pr(A \cup B) = Pr(A) + Pr(B) - Pr(A \cap B)$$

20

Theorem 1.5.8: [[Bonferroni Inequality]]

$$Pr\left(\bigcup_{i=1}^{n}A_{i}\right) \le \sum_{i=1}^{n}Pr(A_{i})$$

21

---

### 1.6 Finite Sample Spaces

**1.6a.** The simplest experiments involve finitely many outcomes.

1.6i. Definition: [[Simple Sample Space]]

A sample space $S$ containing $n$ outcomes where each outcome has probability $1/n$. The probability of an event A is simply the number of outcomes in A divided by $n$ 22.

---

### 1.7 Counting Methods

**1.7a.** To calculate probabilities in simple sample spaces, we need efficient ways to count outcomes without listing them all.

Theorem 1.7.1: [[Multiplication Rule]]

If an experiment has two parts, with $m$ outcomes for the first part and $n$ outcomes for the second (regardless of the first outcome), the total outcomes are $mn$23.

Theorem 1.7.2: General Multiplication Rule

If an experiment has $k$ parts with $n_i$ outcomes for the $i$-th part, the total number of outcomes is:

$$n_1 \times n_2 \times \dots \times n_k$$

24

Definition 1.7.1: [[Permutations]]

An ordered arrangement of $k$ items selected from $n$ distinct items without replacement.

Equation (1.7.2)

$$P_{n,k} = \frac{n!}{(n-k)!}$$

25

Theorem 1.7.5: [[Stirling's Formula]]

For approximating $n!$ when $n$ is large:

$$n! \approx (2\pi)^{1/2} n^{n+1/2} e^{-n}$$

26

---

### 1.8 Combinatorial Methods

**1.8a.** When the order of selection does not matter, we count subsets rather than arrangements.

Definition 1.8.1: [[Combinations]]

A subset of size $k$ chosen from a set of $n$ elements is called a combination. The number of distinct combinations is denoted $C_{n,k}$ or $\binom{n}{k}$ 27.

Equation (1.8.1)

$$C_{n,k} = \binom{n}{k} = \frac{n!}{k!(n-k)!}$$

28

Theorem 1.8.2: [[Binomial Theorem]]

For all numbers $x$ and $y$ and positive integer $n$:

$$(x+y)^{n}=\sum_{k=0}^{n}\binom{n}{k}x^{k}y^{n-k}$$

29

**1.8b.** When sampling with replacement where order does not matter (unordered sampling with replacement), the number of distinguishable sets of size $k$ from $n$ elements is $\binom{n+k-1}{k}$30.

---

### 1.9 Multinomial Coefficients

**1.9a.** This generalizes binomial coefficients to splitting a set into more than two groups.

1.9i. Definition: [[Multinomial Counting]]

The number of ways to divide $n$ distinct elements into $k$ different groups where the $j$-th group has size $n_j$ (and $\sum n_j = n$) is:

$$\frac{n!}{n_1! n_2! \dots n_k!}$$

31

---

### 1.10 The Probability of a Union of Events

**1.10a.** For the union of three or more events, the formula extends the Addition Rule by including and excluding intersections to avoid double counting.

Theorem 1.10.1: Union of Three Events

$$Pr(A \cup B \cup C) = Pr(A) + Pr(B) + Pr(C) - [Pr(A \cap B) + Pr(A \cap C) + Pr(B \cap C)] + Pr(A \cap B \cap C)$$

32

Theorem 1.10.2: [[Inclusion-Exclusion Principle]]

For $n$ events, the probability of their union is the sum of single probabilities, minus the sum of pairs, plus the sum of triples, etc.

$$Pr\left(\bigcup_{i=1}^{n}A_{i}\right)=\sum Pr(A_{i})-\sum Pr(A_{i}\cap A_{j})+\dots+(-1)^{n+1}Pr(A_{1}\cap\dots\cap A_{n})$$

33

Example: [[The Matching Problem]]

If $n$ letters are placed randomly into $n$ envelopes, the probability that at least one letter is in the correct envelope approaches $1 - 1/e \approx 0.632$ as $n$ becomes large 34

### 1.5 The Definition of Probability

**1.5a.** To calculate probabilities mathematically, we assign a number $Pr(A)$ to every event $A$ in the sample space. These numbers must satisfy three specific axioms to ensure they behave consistently with our intuitive understanding of probability 1.

Axiom 1: [[Nonnegativity]]

For every event $A$, $Pr(A) \ge 0$2.

Axiom 2: [[Normalization]]

If an event is certain to occur (the sample space $S$), its probability is 1.

$$Pr(S) = 1$$

3

Axiom 3: [[Countable Additivity]]

For every infinite sequence of disjoint events $A_1, A_2, \dots$, the probability of their union is the sum of their individual probabilities.

$$Pr\left(\bigcup_{i=1}^{\infty}A_{i}\right)=\sum_{i=1}^{\infty}Pr(A_{i})$$

4

1.5i. Definition: [[Probability Measure]]

A probability measure on a sample space $S$ is a specification of numbers $Pr(A)$ for all events $A$ that satisfy Axioms 1, 2, and 35.

Theorem 1.5.1: Probability of the Empty Set

$$Pr(\emptyset)=0$$

6

Theorem 1.5.2: Finite Additivity

For every finite sequence of $n$ disjoint events $A_1, \dots, A_n$:

$$Pr\left(\bigcup_{i=1}^{n}A_{i}\right)=\sum_{i=1}^{n}Pr(A_{i})$$

7

**1.5b.** From these basic axioms, we can derive several fundamental properties of probability, such as how to calculate the probability of a complement or the union of non-disjoint events.

Theorem 1.5.3: [[Complement Rule]]

$$Pr(A^{c})=1-Pr(A)$$

8

Theorem 1.5.4: [[Containment]]

If $A \subset B$, then $Pr(A) \le Pr(B)$9.

Theorem 1.5.7: [[Addition Rule]]

For every two events $A$ and $B$:

$$Pr(A\cup B)=Pr(A)+Pr(B)-Pr(A\cap B)$$

10

Theorem 1.5.8: [[Bonferroni Inequality]]

$$Pr\left(\bigcup_{i=1}^{n}A_{i}\right)\le\sum_{i=1}^{n}Pr(A_{i})$$

11

---

### 1.6 Finite Sample Spaces

**1.6a.** The simplest experiments are those with a finite number of outcomes. If every outcome is equally likely, the calculation of probabilities simplifies to counting outcomes.

1.6i. Definition: [[Simple Sample Space]]

A sample space $S$ containing $n$ outcomes $s_1, \dots, s_n$ is called a simple sample space if the probability assigned to each outcome is $1/n$ 12.

1.6x. Equation

If an event $A$ contains exactly $m$ outcomes in a simple sample space of size $n$:

$$Pr(A) = \frac{m}{n}$$

13

---

### 1.7 Counting Methods

**1.7a.** To compute probabilities in simple sample spaces, we need efficient methods to count the number of outcomes without listing them all.

Theorem 1.7.1: [[Multiplication Rule (Two Parts)]]

If an experiment has two parts, where the first part has $m$ outcomes and the second part has $n$ outcomes (regardless of the first outcome), the total number of outcomes is $mn$14.Shutterstock

Theorem 1.7.2: [[General Multiplication Rule]]

If an experiment has $k$ parts, and the $i$-th part has $n_i$ possible outcomes regardless of the previous outcomes, the total number of outcomes is:

$$n_{1} \times n_{2} \times \dots \times n_{k}$$

15

**1.7b.** A specific application of the multiplication rule is counting permutations, which are ordered arrangements of items.

Definition 1.7.1: [[Permutations]]

A permutation of $n$ elements taken $k$ at a time is an ordered arrangement of $k$ distinct elements selected from a set of $n$ 16.

1.7x. Equation

$$P_{n,k} = n(n-1)\dots(n-k+1) = \frac{n!}{(n-k)!}$$

17171717

Theorem 1.7.5: [[Stirling's Formula]]

For large $n$, computing $n!$ is difficult. Stirling's formula provides an approximation:

$$n! \approx (2\pi)^{1/2}n^{n+1/2}e^{-n}$$

18

---

### 1.8 Combinatorial Methods

**1.8a.** Many probability problems involve counting subsets where the order of selection does not matter.

Definition 1.8.1: [[Combinations]]

A subset of size $k$ chosen from a set of $n$ elements is called a combination. The order of elements in a combination is irrelevant19.

Theorem 1.8.1: [[Number of Combinations]]

The number of distinct subsets of size $k$ that can be chosen from a set of size $n$ is:

$$C_{n,k} = \binom{n}{k} = \frac{P_{n,k}}{k!} = \frac{n!}{k!(n-k)!}$$

20

Theorem 1.8.2: [[Binomial Theorem]]

For all numbers $x$ and $y$ and positive integer $n$:

$$(x+y)^{n}=\sum_{k=0}^{n}\binom{n}{k}x^{k}y^{n-k}$$

21

1.8b. Binomial coefficients have a symmetry property useful for calculations:

$$\binom{n}{k}=\binom{n}{n-k}$$

22

---

### 1.9 Multinomial Coefficients

**1.9a.** We can generalize the concept of combinations to partitioning a set into more than two groups.

1.9i. Definition: [[Multinomial Counting]]

The number of different ways to divide $n$ distinct elements into $k$ different groups where the $j$-th group contains exactly $n_j$ elements (and $\sum n_j = n$) is:

$$\frac{n!}{n_{1}! n_{2}! \dots n_{k}!}$$