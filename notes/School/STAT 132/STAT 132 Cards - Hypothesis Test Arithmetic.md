---
type: reference
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "Hypothesis Test Arithmetic"
tags:
  - decks
---
# STAT 132 Cards - Hypothesis Test Arithmetic (the steps and the numbers)

## Hypothesis Testing
| Front | Back | Notes |
| --- | --- | --- |
| What are the four arithmetic steps of a hypothesis test? | **State H0 and H1; compute the test statistic; compare it with a cutoff (or get the p-value); reject H0 or not.** | DeGroot 9.1; assembly |
| What are the two possible decisions in a hypothesis test? | **Reject H0, or do not reject H0.** *Side note, not tested: "not reject" is not the same as proving H0 true.* | DeGroot 9.1.1; definition |

## Test Statistic and Rejection Region
| Front | Back | Notes |
| --- | --- | --- |
| What is a test statistic? | **A statistic T computed from the data whose value decides the test.** | DeGroot 9.1.5; definition |
| What is a rejection region? | **The set R of values of T that lead you to reject H0**, e.g. $T \ge c$. | DeGroot 9.1.5; definition |
| What is the cutoff c in "reject H0 if $T \ge c$" called? | **The critical value.** | DeGroot 9.1; definition |

## Z Test for Normal Mean (Known Variance)
| Front | Back | Notes |
| --- | --- | --- |
| Write the Z test statistic for $H_0: \mu = \mu_0$ with $\sigma$ known. | $Z = \dfrac{\bar X - \mu_0}{\sigma / \sqrt{n}}$. *Read aloud: "X bar minus mu naught, over sigma over root n."* | DeGroot 9.1.10; formula |
| What does the Z statistic measure? | **How many standard errors $\bar X$ sits from the claimed mean $\mu_0$.** | DeGroot 9.1; motivation |
| What distribution does Z have if H0 is true? | **Standard normal, $N(0, 1)$.** | DeGroot 9.1; definition |
| Two-sided Z test at level 0.05: when do you reject H0? | **When $\vert Z\vert  \ge 1.96$.** | DeGroot 9.1.10; formula |
| One-sided Z test at level 0.05 with $H_1: \mu > \mu_0$: when do you reject? | **When $Z \ge 1.645$.** | formula |
| Why does a two-sided test at level 0.05 use 1.96 rather than 1.645? | **The 0.05 is split into two tails of 0.025 each**, and 1.96 cuts off 0.025 on each side. | motivation |
| Fruit: $\mu_0 = 100$ g, $\sigma = 10$, n = 25, $\bar x = 104$. What is Z? | $Z = \dfrac{104 - 100}{10/5} = 2$. | worked example |
| Fruit test, Z = 2, two-sided at level 0.05: what is the decision? | **Reject H0**, since $\vert 2\vert  \ge 1.96$. | worked example |
| Fruit test, Z = 2: what is the two-sided p-value? | **About 0.046**: $2(1 - \Phi(2)) = 2(0.0228)$. | worked example |

## p-value
| Front | Back | Notes |
| --- | --- | --- |
| What is a p-value? | **The smallest significance level at which you would reject H0 with the observed data.** | DeGroot 9.1.9; definition |
| In words, what chance does a p-value measure? | **If H0 were true, the chance of a test statistic at least as extreme as the one observed.** | definition |
| How do you decide with a p-value and a level $\alpha_0$? | **Reject H0 when the p-value is at most $\alpha_0$.** | DeGroot 9.1; formula |
| DeGroot's example observed Z = 2.78, with p-value 0.0054. What is the decision at level 0.01? | **Reject H0, since $0.0054 < 0.01$.** | DeGroot 9.1.11; worked example |

## Type I and Type II Error
| Front | Back | Notes |
| --- | --- | --- |
| What is a Type I error? | **Rejecting H0 when H0 is true** (a false alarm). | DeGroot 9.1.7; definition |
| What is a Type II error? | **Not rejecting H0 when H0 is false** (a miss). | DeGroot 9.1.7; definition |
| Which error does the level $\alpha_0$ control? | **Type I:** the chance of it is at most $\alpha_0$. | DeGroot 9.1.8; definition |

## Level and Size of a Test
| Front | Back | Notes |
| --- | --- | --- |
| What does it mean for a test to have level $\alpha_0$? | **Its chance of rejecting H0 is at most $\alpha_0$ whenever H0 is true.** | DeGroot 9.1.8; definition |
| What is the size of a test? | **The largest chance of rejecting H0 over all parameter values in H0.** *Side note, not tested: For $H_0: \theta = \theta_0$ it is just that one chance.* | DeGroot 9.1.8; definition |
| What level is used most often in practice? | **0.05** (sometimes 0.01 or 0.10). | recognition |

## Power Function
| Front | Back | Notes |
| --- | --- | --- |
| What does the power function $\pi(\theta \mid \delta)$ give? | **The chance that test $\delta$ rejects H0 when the true parameter is $\theta$.** | DeGroot 9.1.6; definition |
| What should the power function look like for a good test? | **Low (at most $\alpha_0$) for $\theta$ in H0, and high for $\theta$ in H1.** | DeGroot 9.1; motivation |
| For $\theta$ in H1, how do power and the Type II error chance relate? | **Type II chance = 1 minus power.** | DeGroot 9.1.7; formula |

## One-Sided and Two-Sided Hypotheses
| Front | Back | Notes |
| --- | --- | --- |
| When do you use a one-sided alternative instead of a two-sided one? | **When only one direction matters**, e.g. a drug that may only raise recovery. | DeGroot 9.1; discrimination |
| In a one-sided test, which side usually keeps the boundary value? | **H0 keeps the equals sign**, e.g. $H_0: \mu \ge 140$ vs $H_1: \mu < 140$. | DeGroot 9.1; definition |
# Node map
```json
[
 {
  "name": "Hypothesis Testing",
  "uses": [],
  "type": "concept",
  "existing": true,
  "parent": "Statistical Inference",
  "prereqs": [],
  "page": 3,
  "summary": "Deciding whether data argue against a claim about a parameter: a test statistic, a rejection region, and a chosen level."
 },
 {
  "name": "Test Statistic and Rejection Region",
  "uses": [],
  "type": "concept",
  "existing": true,
  "parent": "Hypothesis Testing",
  "prereqs": [],
  "page": 3,
  "summary": "A test rejects H0 when a statistic T lands in a rejection region R."
 },
 {
  "name": "Z Test for Normal Mean (Known Variance)",
  "uses": [],
  "type": "concept",
  "existing": true,
  "parent": "Hypothesis Testing",
  "prereqs": [],
  "page": 3,
  "summary": "Test $H_0: \\mu = \\mu_0$ with $Z = \\sqrt n(\\bar X - \\mu_0)/\\sigma$; two-sided, reject when $|Z| \\ge \\Phi^{-1}(1-\\alpha_0/2)$."
 },
 {
  "name": "p-value",
  "uses": [],
  "type": "concept",
  "existing": true,
  "parent": "Hypothesis Testing",
  "prereqs": [],
  "page": 3,
  "summary": "The smallest level at which the observed data would reject H0."
 },
 {
  "name": "Type I and Type II Error",
  "uses": [],
  "type": "concept",
  "existing": true,
  "parent": "Hypothesis Testing",
  "prereqs": [],
  "page": 3,
  "summary": "Type I: reject a true H0. Type II: fail to reject a false H0."
 },
 {
  "name": "Level and Size of a Test",
  "uses": [],
  "type": "concept",
  "existing": true,
  "parent": "Hypothesis Testing",
  "prereqs": [],
  "page": 3,
  "summary": "Level $\\alpha_0$: Type I error chance at most $\\alpha_0$ for every $\\theta$ in H0; size = the largest such chance."
 },
 {
  "name": "Power Function",
  "uses": [],
  "type": "concept",
  "existing": true,
  "parent": "Hypothesis Testing",
  "prereqs": [],
  "page": 3,
  "summary": "$\\pi(\\theta \\mid \\delta)$: the chance the test rejects H0 when the parameter is $\\theta$."
 },
 {
  "name": "One-Sided and Two-Sided Hypotheses",
  "uses": [],
  "type": "concept",
  "existing": true,
  "parent": "Hypothesis Testing",
  "prereqs": [],
  "page": 3,
  "summary": "Two-sided $H_1: \\mu \\ne \\mu_0$; one-sided $H_1: \\mu > \\mu_0$ or $\\mu < \\mu_0$."
 }
]
```

# Frankenstein problems

None yet.
