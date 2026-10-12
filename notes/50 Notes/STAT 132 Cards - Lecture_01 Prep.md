---
type: reference
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "Lecture_01 Prep"
tags:
  - decks
---
# STAT 132 Cards - Lecture_01 Prep pre-lecture vocabulary

## Population
| Front | Back | Notes |
| --- | --- | --- |
| In statistics, what is a population? %%dk:t:5vt0yv%% | **The whole group you want conclusions about**, e.g. every Californian. | prep; definition |

## Sample in statistics
| Front | Back | Notes |
| --- | --- | --- |
| In statistics, what is a sample? %%dk:t:k327ti%% | **The part of the population you actually observe**, e.g. 1,000 surveyed Californians. | prep; definition |
| Sample vs data: what is the difference? %%dk:t:6df6h0%% | **The sample is who or what you observed; the data are the values you recorded on them.** | prep; discrimination |

## Probability distribution
| Front | Back | Notes |
| --- | --- | --- |
| In one line, what is a probability distribution? %%dk:t:qx5juu%% | **A rule giving the chance of each value (or range of values) of a random variable.** | prep; definition |

## Parameters
| Front | Back | Notes |
| --- | --- | --- |
| Outside statistics, what is a parameter? %%dk:t:jyzp6p%% | **A setting that is fixed for one situation but can change between situations**, like a dial. | prep; definition |

## Sample Notation
| Front | Back | Notes |
| --- | --- | --- |
| In $X_1, \dots, X_n$, what does the subscript on $X_i$ do? %%dk:t:cp5fcu%% | **Labels the position: $X_1$ is the first observation, $X_2$ the second.** | prep; notation |
| In a sample $X_1, \dots, X_n$, what does n count? %%dk:t:fqpi9u%% | **How many observations are in the sample.** | prep; notation |
| Capital $X_i$ vs lowercase $x_i$ in a sample: what is the difference? %%dk:t:r5f8nr%% | **$X_i$ is the slot before you look (random); $x_i$ is the number it actually took.** | prep; discrimination |

## Function as a Dictionary
| Front | Back | Notes |
| --- | --- | --- |
| How can a function act like a dictionary? %%dk:t:k7tm2g%% | **Each input (key) has exactly one output (value)**, e.g. Bernoulli: {1: $\theta$, 0: $1 - \theta$}. | prep; motivation; dep: [[Bayes Update Algorithm]] |

## Decision Theory
| Front | Back | Notes |
| --- | --- | --- |
| What is decision theory? | **The study of choosing actions under uncertainty by weighing their possible outcomes.** *Side note, not tested: Abraham Wald built statistical decision theory in the 1940s.* | prep; definition |

# Node map
```json
[
 {
  "name": "Population",
  "uses": [],
  "type": "concept",
  "existing": true,
  "parent": "Statistical Inference",
  "prereqs": [],
  "page": "",
  "summary": "The whole group you want conclusions about."
 },
 {
  "name": "Sample in statistics",
  "uses": [],
  "type": "concept",
  "existing": true,
  "parent": "Statistical Inference",
  "prereqs": [
   "Population"
  ],
  "page": "",
  "summary": "The part of the population you actually observe."
 },
 {
  "name": "Probability distribution",
  "uses": [],
  "type": "concept",
  "existing": true,
  "parent": "Random variable",
  "prereqs": [
   "Random variable"
  ],
  "page": "",
  "summary": "A rule giving the chance of each value, or each range of values, of a random variable."
 },
 {
  "name": "Parameters",
  "uses": [],
  "type": "concept",
  "existing": true,
  "parent": "Statistical Model",
  "prereqs": [],
  "page": "",
  "summary": "A fixed number in a model that sets its exact shape."
 },
 {
  "name": "Sample Notation",
  "uses": [],
  "type": "concept",
  "existing": false,
  "parent": "Statistical Inference",
  "prereqs": [
   "Sum and Product Notation"
  ],
  "page": "",
  "summary": "$X_1, \\dots, X_n$: one random variable per observation; the subscript labels position, n counts observations."
 },
 {
  "name": "Function as a Dictionary",
  "uses": [],
  "type": "concept",
  "existing": false,
  "parent": "Function",
  "prereqs": [
   "Function"
  ],
  "page": "",
  "summary": "A function pairs each input (key) with exactly one output (value), like a dictionary."
 },
 {
  "name": "Decision Theory",
  "uses": [],
  "type": "concept",
  "existing": false,
  "parent": "Statistical Inference",
  "prereqs": [],
  "page": "",
  "summary": "The study of choosing actions under uncertainty by weighing their possible outcomes."
 }
]
```

# Frankenstein problems

None yet.
