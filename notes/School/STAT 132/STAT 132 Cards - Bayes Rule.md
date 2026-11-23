---
type: reference
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "Bayes Rule"
tags:
  - decks
---
# STAT 132 Cards - Bayes Rule and its parts

## Bayes' Rule
| Front | Back | Notes |
| --- | --- | --- |
| In words, what does Bayes' rule do? | **It flips a conditional:** it gets $\mathbb{P}(A \mid B)$ from $\mathbb{P}(B \mid A)$, using $\mathbb{P}(A)$ and $\mathbb{P}(B)$. | Lecture_01 p.2; definition |
| You see $\dfrac{\mathbb{P}(B \mid A)\,\mathbb{P}(A)}{\mathbb{P}(B)}$. Which conditional probability is this? | **$\mathbb{P}(A \mid B)$, by Bayes' rule.** | Lecture_01 p.2; recognition |
| In words, how do the four parts of Bayes' rule assemble? | **Posterior = likelihood times prior, divided by the evidence.** | Lecture_01 p.2; assembly |
| Why does $\mathbb{P}(B) = \mathbb{P}(B \mid A)\mathbb{P}(A) + \mathbb{P}(B \mid A^c)\mathbb{P}(A^c)$? | **B can happen with A or without A**; add the two routes (law of total probability). | Lecture_01 p.2; motivation |
| Free throws: likelihood times prior is 0.0246 for the 80% shooter and 0.0217 for the 50% shooter. What is the posterior for the 80% shooter? | $0.0246 / (0.0246 + 0.0217) = 0.0246 / 0.0463 \approx 0.53$. | worked example; dep: [[Bayes Update Algorithm]] |

## Posterior Probability
| Front | Back | Notes |
| --- | --- | --- |
| In Bayes' rule, what is $\mathbb{P}(A \mid B)$ called? | **The posterior:** belief in A after seeing B. | Lecture_01 p.2; definition |
| Which piece of Bayes' rule is the posterior? | **$\mathbb{P}(A \mid B)$**, the left-hand side. | Lecture_01 p.2; recognition |

## Prior Probability
| Front | Back | Notes |
| --- | --- | --- |
| In Bayes' rule, what is $\mathbb{P}(A)$ called? | **The prior:** belief in A before seeing B. | Lecture_01 p.2; definition |
| Which piece of Bayes' rule is the prior? | **$\mathbb{P}(A)$**, on the top right. | Lecture_01 p.2; recognition |

## Likelihood (Bayes' Rule)
| Front | Back | Notes |
| --- | --- | --- |
| In Bayes' rule, what is $\mathbb{P}(B \mid A)$ called? | **The likelihood:** how likely the evidence B is if A is true. | Lecture_01 p.2; definition |
| Which piece of Bayes' rule is the likelihood? | **$\mathbb{P}(B \mid A)$**, on the top left. | Lecture_01 p.2; recognition |
| Which step of the Bayes update algorithm computes the likelihood? | **Step 4**: look up each data value in X's dictionary and multiply. | assembly; dep: [[Bayes Update Algorithm]] |

## Evidence (Bayes' Rule)
| Front | Back | Notes |
| --- | --- | --- |
| In Bayes' rule, what is $\mathbb{P}(B)$ called? | **The evidence** (also the marginal probability of B): the total chance of B over every case. | Lecture_01 p.2; definition |
| Which piece of Bayes' rule is the evidence? | **$\mathbb{P}(B)$**, the denominator. | Lecture_01 p.2; recognition |
| Which step of the Bayes update algorithm divides by the evidence $\mathbb{P}(B)$? | **Step 6, normalize**: in the free throws, the total 0.0463. | assembly; dep: [[Bayes Update Algorithm]] |
| Which step of the Bayes update algorithm multiplies the likelihood by the prior? | **Step 5**: it gives the top of Bayes' rule, before dividing by the evidence. | assembly; dep: [[Bayes Update Algorithm]] |

# Node map
```json
[
 {
  "name": "Bayes' Rule",
  "uses": [],
  "type": "concept",
  "existing": true,
  "parent": "Conditional Probability",
  "prereqs": [
   "Conditional Probability",
   "Law of Total Probability"
  ],
  "page": 2,
  "summary": "$\\mathbb{P}(A\\mid B) = \\mathbb{P}(B\\mid A)\\mathbb{P}(A)/\\mathbb{P}(B)$: posterior = likelihood times prior over evidence."
 },
 {
  "name": "Posterior Probability",
  "uses": [],
  "type": "concept",
  "existing": false,
  "parent": "Bayes' Rule",
  "prereqs": [
   "Bayes' Rule"
  ],
  "page": 2,
  "summary": "$\\mathbb{P}(A\\mid B)$ in Bayes' rule: belief in A after seeing B."
 },
 {
  "name": "Prior Probability",
  "uses": [],
  "type": "concept",
  "existing": false,
  "parent": "Bayes' Rule",
  "prereqs": [
   "Bayes' Rule"
  ],
  "page": 2,
  "summary": "$\\mathbb{P}(A)$ in Bayes' rule: belief in A before seeing B."
 },
 {
  "name": "Likelihood (Bayes' Rule)",
  "uses": [],
  "type": "concept",
  "existing": false,
  "parent": "Bayes' Rule",
  "prereqs": [
   "Bayes' Rule",
   "Likelihood Function"
  ],
  "page": 2,
  "summary": "$\\mathbb{P}(B\\mid A)$ in Bayes' rule: how likely the evidence B is if A is true."
 },
 {
  "name": "Evidence (Bayes' Rule)",
  "uses": [],
  "type": "concept",
  "existing": false,
  "parent": "Bayes' Rule",
  "prereqs": [
   "Bayes' Rule",
   "Law of Total Probability"
  ],
  "page": 2,
  "summary": "$\\mathbb{P}(B)$ in Bayes' rule: the total chance of the evidence over every case; the normalizer."
 }
]
```

# Frankenstein problems

None yet.
