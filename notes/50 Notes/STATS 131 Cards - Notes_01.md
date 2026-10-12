---
type: reference
parent: "[[STATS 131]]"
domain: stats
course: "STATS 131"
status: draft
source: "Notes_01"
tags:
  - decks
---
# STATS 131 Cards - Notes_01 Classical Probability Theory

## Experiment
| Front | Back | Notes |
| --- | --- | --- |
| What is an experiment, in the probability sense? | A process where the possible outcomes can be identified ahead of time. | p.1; definition |

## Sample Space
| Front | Back | Notes |
| --- | --- | --- |
| What is the sample space $\Omega$? | The set of all possible outcomes of an experiment. | p.1; definition |
| Sample space for tossing a fair coin twice? | $\{HH, HT, TH, TT\}$ | p.1; formula |

## Event
| Front | Back | Notes |
| --- | --- | --- |
| What is an event, in terms of the sample space? | A subset of the sample space; a set of possible outcomes of the experiment. | p.1; definition |

## Set
| Front | Back | Notes |
| --- | --- | --- |
| What is a set, as used in probability? | A collection of distinct possible outcomes. | p.2; definition |

## Subset
| Front | Back | Notes |
| --- | --- | --- |
| When is $A$ contained in $B$? | When every element of $A$ also belongs to $B$. | p.2; definition |
| Two equivalent notations for A contained in B? | $A \subseteq B$ or $B \supseteq A$ | p.2; formula |

## Empty Set
| Front | Back | Notes |
| --- | --- | --- |
| What is the empty set, and how is it written? | The subset of $\Omega$ with no elements, denoted $\emptyset$. | p.2; definition |

## Complement (Sets)
| Front | Back | Notes |
| --- | --- | --- |
| Definition of the complement $A^C$? | The set of all elements of $\Omega$ that do not belong to $A$. | p.2; definition |
| Simplify $(A^C)^C$. | $A$ | p.2; identity |
| What are $\emptyset^C$ and $\Omega^C$? | $\emptyset^C = \Omega$ and $\Omega^C = \emptyset$ | p.2; identity |

## Union (Sets)
| Front | Back | Notes |
| --- | --- | --- |
| Definition of the union of sets $A_1,\dots,A_n$? | The set of outcomes that belong to at least one of the $n$ sets. | p.3; definition |
| Simplify $A \cup A$, $A \cup A^C$, $A \cup \emptyset$, $A \cup \Omega$. | $A \cup A = A$; $A \cup A^C = \Omega$; $A \cup \emptyset = A$; $A \cup \Omega = \Omega$ | p.3; identity |
| If $A \subseteq B$, what is $A \cup B$? | $B$ | p.3; identity |

## Intersection (Sets)
| Front | Back | Notes |
| --- | --- | --- |
| Definition of the intersection of sets $A_1,\dots,A_n$? | The set of outcomes common to all $n$ sets. | p.3; definition |
| Simplify $A \cap A$, $A \cap A^C$, $A \cap \emptyset$, $A \cap \Omega$. | $A \cap A = A$; $A \cap A^C = \emptyset$; $A \cap \emptyset = \emptyset$; $A \cap \Omega = A$ | p.3; identity |
| If $A \subseteq B$, what is $A \cap B$? | $A$ | p.3; identity |

## Disjoint Sets
| Front | Back | Notes |
| --- | --- | --- |
| When are two sets disjoint? | When their intersection is empty, $A \cap B = \emptyset$ | p.4; definition |

## DeMorgan's Law
| Front | Back | Notes |
| --- | --- | --- |
| De Morgan's law for $(A \cup B)^C$? | $(A \cup B)^C = A^C \cap B^C$ | p.4; identity |
| De Morgan's law for $(A \cap B)^C$? | $(A \cap B)^C = A^C \cup B^C$ | p.4; identity |

## Associativity
| Front | Back | Notes |
| --- | --- | --- |
| Associative property of union, three sets? | $A \cup B \cup C = (A \cup B) \cup C = A \cup (B \cup C)$ | p.4; identity |
| Associative property of intersection, three sets? | $A \cap B \cap C = (A \cap B) \cap C = A \cap (B \cap C)$ | p.4; identity |

## Distributive Properties (Sets)
| Front | Back | Notes |
| --- | --- | --- |
| Distribute $A \cap (B \cup C)$. | $(A \cap B) \cup (A \cap C)$ | p.4; identity |
| Distribute $A \cup (B \cap C)$. | $(A \cup B) \cap (A \cup C)$ | p.4; identity |

## Partition (Sets)
| Front | Back | Notes |
| --- | --- | --- |
| When does $\{E_i\}_{i=1}^n$ partition $A$? | When $A = \bigcup_{i=1}^n E_i$ and $E_i \cap E_j = \emptyset$ for all $i \neq j$ | p.4; definition |
| Partition identity splitting $A$ using $B$? | $A = (A \cap B) \cup (A \cap B^C)$ | p.5; identity |
| Rewrite $A \cup B$ as a union of disjoint pieces. | $A \cup B = A \cup (B \cap A^C)$ | p.5; identity |

## Interpretations of Probability
| Front | Back | Notes |
| --- | --- | --- |
| Two ways to interpret probability? | Long run relative frequency, or subjective belief | p.6; distinction |

## Axioms of Probability
| Front | Back | Notes |
| --- | --- | --- |
| Axiom 1 of probability (positivity)? | For every event $A$, $\mathbb{P}(A) \geq 0$ | p.6; axiom |
| Axiom 2 of probability (unity)? | $\mathbb{P}(\Omega) = 1$ | p.6; axiom |
| Axiom 3 of probability (countable additivity)? | For disjoint $A_1, A_2, \dots$: $\mathbb{P}(\bigcup_{i=1}^\infty A_i) = \sum_{i=1}^\infty \mathbb{P}(A_i)$ | p.6; axiom |
| What is a probability measure, formally? | A specification of numbers $\mathbb{P}(A)$ for all events $A$ satisfying Axioms 1 to 3 | p.6; definition |

## Properties of Probability Measures
| Front | Back | Notes |
| --- | --- | --- |
| Value of $\mathbb{P}(\emptyset)$? | $0$ | p.7; identity |
| Finite additivity formula for disjoint $A_1,\dots,A_n$? | $\mathbb{P}(\bigcup_{i=1}^n A_i) = \sum_{i=1}^n \mathbb{P}(A_i)$ | p.7; identity |
| Monotonicity: if $A \subseteq B$, compare $\mathbb{P}(A)$ and $\mathbb{P}(B)$. | $\mathbb{P}(A) \leq \mathbb{P}(B)$ | p.8; theorem |
| Range of $\mathbb{P}(A)$ for any event $A$? | $\mathbb{P}(A) \in [0,1]$ | p.8; theorem |

## Complement Rule and De Morgan
| Front | Back | Notes |
| --- | --- | --- |
| Complement rule for probability? | $\mathbb{P}(A^C) = 1 - \mathbb{P}(A)$ | p.8; formula |
| Why does $\mathbb{P}(A^C) = 1 - \mathbb{P}(A)$ hold? | $A$ and $A^C$ are disjoint with $A \cup A^C = \Omega$, so their probabilities sum to 1 | p.8; procedure |

## Addition Rule
| Front | Back | Notes |
| --- | --- | --- |
| General addition rule for $\mathbb{P}(A \cup B)$? | $\mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A \cap B)$ | p.8; formula |
| Decomposition identity for $\mathbb{P}(A \cap B^C)$? | $\mathbb{P}(A) - \mathbb{P}(A \cap B)$ | p.8; identity |

## Union Bound
| Front | Back | Notes |
| --- | --- | --- |
| Union bound for $A_1,\dots,A_n$? | $\mathbb{P}(\bigcup_{i=1}^n A_i) \leq \sum_{i=1}^n \mathbb{P}(A_i)$ | p.9; formula |
| When is the union bound most useful? | For a quick upper bound on the probability that at least one of several events occurs, without knowing their intersections | p.9; distinction |

## Bonferroni Inequality
| Front | Back | Notes |
| --- | --- | --- |
| Bonferroni inequality for $A_1,\dots,A_n$? | $\mathbb{P}(\bigcap_{i=1}^n A_i) \geq 1 - \sum_{i=1}^n \mathbb{P}(A_i^C)$ | p.9; formula |
| Does the Bonferroni inequality give an upper or lower bound, on what? | A lower bound on the probability that all the events occur simultaneously | p.9; distinction |

## Simple Finite Space
| Front | Back | Notes |
| --- | --- | --- |
| Equally likely outcomes: if $\Omega = \{\omega_i\}_{i=1}^N$, what is $\mathbb{P}(\omega_i)$? | $\dfrac{1}{N}$ for each $i = 1,\dots,N$ | p.10; definition |

## Classical Probability Formula
| Front | Back | Notes |
| --- | --- | --- |
| Classical probability formula for $E \subseteq \Omega$ with equally likely outcomes? | $\mathbb{P}(E) = \dfrac{\lvert E \rvert}{\lvert \Omega \rvert}$ | p.10; formula |
| With equally likely outcomes, probability calculation reduces to what? | Counting: the number of outcomes in $E$ over the number in $\Omega$ | p.10; procedure |

## Verifying a Probability Measure (Die Roll)
| Front | Back | Notes |
| --- | --- | --- |
| Roll one die, $\mathbb{P}(A) = \lvert A \rvert / \lvert \Omega \rvert$. Key step to confirm this is a valid probability measure? | Check the three axioms: $\mathbb{P}(A) \geq 0$ always; $\mathbb{P}(\Omega) = 6/6 = 1$; and for disjoint $A_i$, $\sum \mathbb{P}(A_i) = \mathbb{P}(\cup A_i)$ by counting | p.6; procedure |

## Diagnosing Diseases (Bacterial or Viral)
| Front | Back | Notes |
| --- | --- | --- |
| $\mathbb{P}(B)=0.7$, $\mathbb{P}(V)=0.4$, patient definitely has $B$ or $V$ or both. Find $\mathbb{P}(B \cap V)$. | $\mathbb{P}(B \cap V) = \mathbb{P}(B) + \mathbb{P}(V) - \mathbb{P}(B \cup V) = 0.7 + 0.4 - 1 = 0.1$ | p.9; procedure |

## Late to Class (Union Bound)
| Front | Back | Notes |
| --- | --- | --- |
| 4 classes, $\mathbb{P}(\text{late to class } i) = 0.05$ each. Upper bound for $\mathbb{P}(\text{late to at least one})$? | By the union bound: $4 \times 0.05 = 0.2$ | p.9; procedure |

## Passing All Exams (Bonferroni)
| Front | Back | Notes |
| --- | --- | --- |
| 3 exams, $\mathbb{P}(\text{pass exam } i) = 0.9$ each. Lower bound for $\mathbb{P}(\text{pass all 3})$? | By Bonferroni: $1 - 3(0.1) = 0.7$ | p.9; procedure |

## Three Coins, Exactly Two Heads
| Front | Back | Notes |
| --- | --- | --- |
| Toss 3 fair coins. $\mathbb{P}(\text{exactly two heads})$? | $E = \{HHT, HTH, THH\}$, so $\mathbb{P}(E) = 3/8$ | p.10; procedure |

## Two Dice, Sum 11 vs Sum 12
| Front | Back | Notes |
| --- | --- | --- |
| Roll two fair dice. Which is more likely, sum $=11$ or sum $=12$? | Sum $=11$: $\mathbb{P} = 2/36$ from $(5,6),(6,5)$; sum $=12$: $\mathbb{P} = 1/36$ from $(6,6)$; so sum $=11$ is more likely | p.10; procedure |
# Node map
```json
[
 {
  "name": "Experiment",
  "type": "concept",
  "existing": false,
  "parent": "Sample Spaces and Events",
  "prereqs": [],
  "uses": [],
  "page": 1,
  "summary": "An experiment is any process where the possible outcomes can be identified ahead of time."
 },
 {
  "name": "Sample Space",
  "type": "concept",
  "existing": false,
  "parent": "Sample Spaces and Events",
  "prereqs": [
   "Experiment"
  ],
  "uses": [],
  "page": 1,
  "summary": "The sample space $\\Omega$ is the set of all possible outcomes of an experiment."
 },
 {
  "name": "Event",
  "type": "concept",
  "existing": false,
  "parent": "Sample Spaces and Events",
  "prereqs": [
   "Sample Space"
  ],
  "uses": [],
  "page": 1,
  "summary": "An event is a subset of the sample space: a set of possible outcomes."
 },
 {
  "name": "Set",
  "type": "concept",
  "existing": true,
  "parent": "Basic Set Theory",
  "prereqs": [],
  "uses": [],
  "page": 2,
  "summary": "A set is a collection of different possible outcomes."
 },
 {
  "name": "Subset",
  "type": "concept",
  "existing": true,
  "parent": "Basic Set Theory",
  "prereqs": [
   "Set"
  ],
  "uses": [],
  "page": 2,
  "summary": "A is a subset of B ($A \\subseteq B$) if every element of A also belongs to B."
 },
 {
  "name": "Empty Set",
  "type": "concept",
  "existing": false,
  "parent": "Basic Set Theory",
  "prereqs": [
   "Set"
  ],
  "uses": [],
  "page": 2,
  "summary": "The empty set $\\emptyset$ is the subset of $\\Omega$ containing no elements."
 },
 {
  "name": "Complement (Sets)",
  "type": "concept",
  "existing": false,
  "parent": "Basic Set Theory",
  "prereqs": [
   "Set"
  ],
  "uses": [],
  "page": 2,
  "summary": "The complement $A^C$ contains all elements of $\\Omega$ not in $A$; $(A^C)^C=A$, $\\emptyset^C=\\Omega$, $\\Omega^C=\\emptyset$."
 },
 {
  "name": "Union (Sets)",
  "type": "concept",
  "existing": false,
  "parent": "Basic Set Theory",
  "prereqs": [
   "Set"
  ],
  "uses": [],
  "page": 3,
  "summary": "The union of sets is the set of outcomes belonging to at least one of them, with standard identities like $A \\cup \\Omega = \\Omega$."
 },
 {
  "name": "Intersection (Sets)",
  "type": "concept",
  "existing": false,
  "parent": "Basic Set Theory",
  "prereqs": [
   "Set"
  ],
  "uses": [],
  "page": 3,
  "summary": "The intersection of sets is the set of outcomes common to all of them, with standard identities like $A \\cap A^C = \\emptyset$."
 },
 {
  "name": "Disjoint Sets",
  "type": "concept",
  "existing": false,
  "parent": "Basic Set Theory",
  "prereqs": [
   "Intersection (Sets)",
   "Empty Set"
  ],
  "uses": [],
  "page": 4,
  "summary": "Two sets are disjoint if their intersection is empty."
 },
 {
  "name": "DeMorgan's Law",
  "type": "concept",
  "existing": true,
  "parent": "Basic Set Theory",
  "prereqs": [
   "Union (Sets)",
   "Intersection (Sets)",
   "Complement (Sets)"
  ],
  "uses": [],
  "page": 4,
  "summary": "$(A \\cup B)^C = A^C \\cap B^C$ and $(A \\cap B)^C = A^C \\cup B^C$."
 },
 {
  "name": "Associativity",
  "type": "concept",
  "existing": true,
  "parent": "Basic Set Theory",
  "prereqs": [
   "Union (Sets)",
   "Intersection (Sets)"
  ],
  "uses": [],
  "page": 4,
  "summary": "Union and intersection of sets are associative: grouping of $A \\cup B \\cup C$ or $A \\cap B \\cap C$ does not matter."
 },
 {
  "name": "Distributive Properties (Sets)",
  "type": "concept",
  "existing": false,
  "parent": "Basic Set Theory",
  "prereqs": [
   "Union (Sets)",
   "Intersection (Sets)"
  ],
  "uses": [],
  "page": 4,
  "summary": "Intersection distributes over union and union distributes over intersection, analogous to arithmetic distribution."
 },
 {
  "name": "Partition (Sets)",
  "type": "concept",
  "existing": false,
  "parent": "Basic Set Theory",
  "prereqs": [
   "Disjoint Sets",
   "Union (Sets)"
  ],
  "uses": [],
  "page": 4,
  "summary": "A collection of sets partitions A if their union is A and they are pairwise disjoint; yields identities like $A=(A\\cap B)\\cup(A\\cap B^C)$."
 },
 {
  "name": "Interpretations of Probability",
  "type": "concept",
  "existing": false,
  "parent": "Probability Theory",
  "prereqs": [],
  "uses": [],
  "page": 6,
  "summary": "Probability can be interpreted as long-run relative frequency or as subjective belief; both use the same calculational framework."
 },
 {
  "name": "Axioms of Probability",
  "type": "concept",
  "existing": false,
  "parent": "Probability Theory",
  "prereqs": [
   "Event",
   "Sample Space"
  ],
  "uses": [],
  "page": 6,
  "summary": "A probability measure assigns numbers $\\mathbb{P}(A)$ to events satisfying positivity, unity, and countable additivity."
 },
 {
  "name": "Properties of Probability Measures",
  "type": "concept",
  "existing": false,
  "parent": "Probability Theory",
  "prereqs": [
   "Axioms of Probability"
  ],
  "uses": [],
  "page": 7,
  "summary": "From the axioms: $\\mathbb{P}(\\emptyset)=0$, finite additivity holds, probability is monotone under subset, and always lies in $[0,1]$."
 },
 {
  "name": "Complement Rule and De Morgan",
  "type": "concept",
  "existing": true,
  "parent": "Probability Theory",
  "prereqs": [
   "Axioms of Probability",
   "Complement (Sets)"
  ],
  "uses": [],
  "page": 8,
  "summary": "$\\mathbb{P}(A^C) = 1 - \\mathbb{P}(A)$, since $A$ and $A^C$ partition $\\Omega$."
 },
 {
  "name": "Addition Rule",
  "type": "concept",
  "existing": true,
  "parent": "Probability Theory",
  "prereqs": [
   "Axioms of Probability",
   "Union (Sets)",
   "Intersection (Sets)"
  ],
  "uses": [],
  "page": 8,
  "summary": "$\\mathbb{P}(A \\cup B) = \\mathbb{P}(A) + \\mathbb{P}(B) - \\mathbb{P}(A \\cap B)$, with the related identity $\\mathbb{P}(A \\cap B^C) = \\mathbb{P}(A) - \\mathbb{P}(A \\cap B)$."
 },
 {
  "name": "Union Bound",
  "type": "concept",
  "existing": false,
  "parent": "Probability Theory",
  "prereqs": [
   "Axioms of Probability",
   "Addition Rule"
  ],
  "uses": [],
  "page": 9,
  "summary": "$\\mathbb{P}(\\bigcup_{i=1}^n A_i) \\leq \\sum_{i=1}^n \\mathbb{P}(A_i)$, an upper bound not requiring knowledge of intersections."
 },
 {
  "name": "Bonferroni Inequality",
  "type": "concept",
  "existing": false,
  "parent": "Probability Theory",
  "prereqs": [
   "Complement Rule and De Morgan",
   "Axioms of Probability"
  ],
  "uses": [],
  "page": 9,
  "summary": "$\\mathbb{P}(\\bigcap_{i=1}^n A_i) \\geq 1 - \\sum_{i=1}^n \\mathbb{P}(A_i^C)$, a lower bound on all events occurring together."
 },
 {
  "name": "Simple Finite Space",
  "type": "concept",
  "existing": true,
  "parent": "Probability on Finite Sample Spaces",
  "prereqs": [
   "Sample Space",
   "Axioms of Probability"
  ],
  "uses": [],
  "page": 10,
  "summary": "A finite sample space $\\Omega=\\{\\omega_i\\}_{i=1}^N$ where every outcome has equal probability $1/N$."
 },
 {
  "name": "Classical Probability Formula",
  "type": "concept",
  "existing": false,
  "parent": "Probability on Finite Sample Spaces",
  "prereqs": [
   "Simple Finite Space"
  ],
  "uses": [],
  "page": 10,
  "summary": "With equally likely outcomes, $\\mathbb{P}(E) = |E|/|\\Omega|$, reducing probability to counting."
 },
 {
  "name": "Verifying a Probability Measure (Die Roll)",
  "type": "problem",
  "existing": false,
  "parent": "Probability Theory",
  "prereqs": [
   "Axioms of Probability"
  ],
  "uses": [
   "Axioms of Probability",
   "Properties of Probability Measures"
  ],
  "page": 6,
  "summary": "Checks that $\\mathbb{P}(A)=|A|/|\\Omega|$ on a die roll satisfies all three probability axioms."
 },
 {
  "name": "Diagnosing Diseases (Bacterial or Viral)",
  "type": "problem",
  "existing": false,
  "parent": "Probability Theory",
  "prereqs": [
   "Addition Rule"
  ],
  "uses": [
   "Addition Rule"
  ],
  "page": 9,
  "summary": "Uses the addition rule with $\\mathbb{P}(B\\cup V)=1$ to solve for $\\mathbb{P}(B\\cap V)=0.1$."
 },
 {
  "name": "Late to Class (Union Bound)",
  "type": "problem",
  "existing": false,
  "parent": "Probability Theory",
  "prereqs": [
   "Union Bound"
  ],
  "uses": [
   "Union Bound"
  ],
  "page": 9,
  "summary": "Applies the union bound over 4 classes at 0.05 each to bound the chance of being late at least once by 0.2."
 },
 {
  "name": "Passing All Exams (Bonferroni)",
  "type": "problem",
  "existing": false,
  "parent": "Probability Theory",
  "prereqs": [
   "Bonferroni Inequality"
  ],
  "uses": [
   "Bonferroni Inequality"
  ],
  "page": 9,
  "summary": "Applies Bonferroni over 3 exams at 0.9 pass probability each to lower-bound passing all three at 0.7."
 },
 {
  "name": "Three Coins, Exactly Two Heads",
  "type": "problem",
  "existing": false,
  "parent": "Probability on Finite Sample Spaces",
  "prereqs": [
   "Classical Probability Formula"
  ],
  "uses": [
   "Classical Probability Formula",
   "Simple Finite Space"
  ],
  "page": 10,
  "summary": "Counts the 3 outcomes with exactly two heads out of 8 equally likely triples, giving probability 3/8."
 },
 {
  "name": "Two Dice, Sum 11 vs Sum 12",
  "type": "problem",
  "existing": false,
  "parent": "Probability on Finite Sample Spaces",
  "prereqs": [
   "Classical Probability Formula"
  ],
  "uses": [
   "Classical Probability Formula",
   "Simple Finite Space"
  ],
  "page": 10,
  "summary": "Compares $\\mathbb{P}(\\text{sum}=11)=2/36$ to $\\mathbb{P}(\\text{sum}=12)=1/36$ using equally likely dice outcomes."
 }
]
```

# Frankenstein problems

**Problem 1.** Among a group of students, let $A$ be the event a random student takes Stats and $B$ be the event they take Econ. Suppose $\mathbb{P}(A) = 0.6$, $\mathbb{P}(B) = 0.5$, and $\mathbb{P}(A \cup B) = 0.8$.
(a) Find $\mathbb{P}(A \cap B)$.
(b) Find $\mathbb{P}(A^C \cap B^C)$, the probability a student takes neither.
(c) Confirm part (b) using De Morgan's law.

*Solution.*
(a) By the addition rule, $\mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B) - \mathbb{P}(A \cap B)$, so
$0.8 = 0.6 + 0.5 - \mathbb{P}(A \cap B) \Rightarrow \mathbb{P}(A \cap B) = 1.1 - 0.8 = 0.3$.
(b) By De Morgan's law, $A^C \cap B^C = (A \cup B)^C$. By the complement rule,
$\mathbb{P}((A \cup B)^C) = 1 - \mathbb{P}(A \cup B) = 1 - 0.8 = 0.2$.
So $\mathbb{P}(A^C \cap B^C) = 0.2$.
(c) The equality $A^C \cap B^C = (A \cup B)^C$ used in (b) is exactly De Morgan's law, and the complement rule (which itself rests on the unity and additivity axioms, since $A\cup B$ and $(A\cup B)^C$ partition $\Omega$) gives the numeric value.

Concepts tested: Addition Rule, Complement Rule and De Morgan, DeMorgan's Law, Axioms of Probability.

**Problem 2.** Roll a fair six-sided die twice, giving 36 equally likely outcomes (a Simple Finite Space). Let $A$ = the first roll is 1, $B$ = the second roll is 1, and $C$ = the sum of the two rolls is 2.
(a) Using the classical probability formula, find $\mathbb{P}(A)$, $\mathbb{P}(B)$, and $\mathbb{P}(A \cap B)$.
(b) Use the addition rule to find the exact value of $\mathbb{P}(A \cup B)$.
(c) Use the union bound to find an upper bound on $\mathbb{P}(A \cup B)$ and compare it to (b).
(d) Note $C \subseteq A$. Use monotonicity to bound $\mathbb{P}(C)$ above, then compute $\mathbb{P}(C)$ exactly and confirm the bound holds.

*Solution.*
(a) $|\Omega| = 36$. $A = \{(1,1),\dots,(1,6)\}$, so $\mathbb{P}(A) = 6/36 = 1/6$. $B = \{(1,1),\dots,(6,1)\}$, so $\mathbb{P}(B) = 6/36 = 1/6$. $A \cap B = \{(1,1)\}$, so $\mathbb{P}(A \cap B) = 1/36$.
(b) By the addition rule, $\mathbb{P}(A \cup B) = 6/36 + 6/36 - 1/36 = 11/36$.
(c) By the union bound, $\mathbb{P}(A \cup B) \leq \mathbb{P}(A) + \mathbb{P}(B) = 6/36 + 6/36 = 12/36 = 1/3$. Since $11/36 < 12/36$, the exact answer respects the bound, which is not tight because $A$ and $B$ overlap.
(d) $C = \{(1,1)\} = A \cap B \subseteq A$, so by monotonicity $\mathbb{P}(C) \leq \mathbb{P}(A) = 6/36 = 1/6$. Exactly, $\mathbb{P}(C) = 1/36$, and indeed $1/36 \leq 1/6$, confirming the bound.

Concepts tested: Simple Finite Space, Classical Probability Formula, Addition Rule, Union Bound, Properties of Probability Measures, Subset.
