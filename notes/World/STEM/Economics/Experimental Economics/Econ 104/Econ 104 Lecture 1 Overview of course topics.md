---
title: Causal Inference and Research Designs
aliases: [Lesson 1, Econ 104 Lesson 1, Research Designs Overview]
tags: [econometrics, causal-inference, econ104]
type: lecture
parent: "[[Econ 104]]"
domain: econ
status: draft
---
To do
Read chapter 1 as you have the book
Univariate and multivariate regressions 
Units of Measurement levels log and binary
hypo testing
stata code and do-files
## Table of Contents
- [What this course is about](#what-this-course-is-about)
- [Three uses of statistics](#three-uses-of-statistics)
- [Why causal inference matters](#why-causal-inference-matters)
- [The fundamental problem of causal inference](#the-fundamental-problem-of-causal-inference)
- [Motivating examples](#motivating-examples)
  - [Job training](#job-training)
  - [College attendance](#college-attendance)
- [Five research designs](#five-research-designs)
- [Ranking research designs by credibility](#ranking-research-designs-by-credibility)
- [Design-by-design intuition](#design-by-design-intuition)

---

## What this course is about
This course is about **causal inference**: estimating how a treatment or intervention changes an outcome.

The emphasis is not on:
- describing data
- or predicting outcomes

but on answering questions of the form:
> What is the effect of X on Y?

---

## Three uses of statistics
Statistics is used for three distinct purposes:

**Description**
- Summarizing characteristics of a population or sample
- Examples: average income, inequality trends
This is not where economics is going
We can't describe much it's not the direction taking

**Prediction**
- Forecasting outcomes given inputs
- Examples: GPA prediction, house price prediction
Highly sought after


**Causal inference**
- Estimating the effect of a treatment
- Examples: earnings with vs without college, outcomes with vs without tutoring
Economists specialize in this of treatment and outcome
It's much harder in many ways

Key distinction:
Prediction can be accurate without being causal.

---

## Why causal inference matters
Causal inference is essential for:

- Understanding the world  
  Example: how parental income affects college attendance

- Policy design  
  Example: whether cash transfers improve outcomes during downturns

- Business decisions  
  Example: whether team training raises productivity

- Medicine  
  Example: whether a drug is effective

---

## The fundamental problem of causal inference
Every causal question compares two states of the world:
- what actually happened
- what would have happened otherwise

The second state is the **counterfactual**, and it is never observed.

For any individual, we observe either:
- outcome with treatment
- outcome without treatment

but never both.

This missing counterfactual is the core challenge of causal inference.

---

## Motivating examples

### Job training
Question:
How much more (or less) does someone earn *because* they enrolled in job training?

What we observe:
- earnings after training

What we do not observe:
- what earnings would have been without training

Naive comparisons fail because:
- people self-select into training
- earnings change over time
- trained and untrained people differ systematically

---

### College attendance
Question:
How much more will a person earn if they attend college versus if they do not?

Bad counterfactuals:
- earnings before college
- earnings of a high school classmate who did not attend

Problem:
People who attend college differ in motivation, ability, background, and expectations.

---

## Five research designs
The course covers five research designs, each offering a different way to approximate the counterfactual:

There's 5 categories of research design
- BEST **[[Randomized experiment]] (RCT)** - gold standard for causal inference
- - WORST **[[Selection on observables]] (multivariate regression)** - using regression adjustment (multivariate regression)
	- The worst bc of omitted variable bias
    - Requires “no unobserved confounding”.
        
    - Easy to run, hard to trust.
        
    - Baseline or descriptive unless assumptions are very convincing.

    - Cleanest identification.
    - They don't get to choose what group they're in that's where the causal comes from
    - Fewest assumptions.
    - Benchmark against which everything else is judged.
Quasi-experimental methods - developed by economists
- **[[Regression discontinuity design]] (RDD)**
    
    - Near-random assignment at a cutoff.
        
    - Very strong internal validity locally.
        
    - Narrow scope, but highly credible.
- **[[Difference-in-differences]] (DiD)**
    
    - Strong when parallel trends is believable.
        
    - Widely used for policy evaluation.
        
    - Weaker than RDD because trends are an assumption, not enforced.
    - The treatment is a policy or a schock
- **[[Instrumental variables]] (IV)**
	- Got really popular about 20 years ago
    - Powerful when a truly exogenous instrument exists.
    - Often fragile due to exclusion and weak instruments.
    - Estimates a local effect (LATE), not a global one.
    - There are correlates between socio economic status and wealth
    - Randomized lotteries allow us to measure the prohibitively measured
    


Each design relies on different assumptions and offers different levels of credibility.

---

## Ranking research designs by credibility
A rough ordering from most credible to least credible:

1. Randomized experiments  
2. Regression discontinuity designs  
3. Difference-in-differences  
4. Instrumental variables  
5. Selection on observables (regression)

Credibility declines as identification relies more heavily on assumptions that cannot be directly tested.

---

## Design-by-design intuition

### Randomized Controlled Trials
Random assignment ensures treated and control groups are similar in both observed and unobserved characteristics.

If properly implemented, the only systematic difference between groups is treatment status.

Limitations:
- infeasible in many settings
- ethical constraints
- high cost

---

### Selection on observables (regression)
Compare treated and untreated individuals while controlling for observed differences using regression.

This approach assumes:
- all relevant confounders are observed and included

Main weakness:
- unobserved differences remain
- functional form assumptions matter

Common because it is easy, not because it is strong.

---

### Instrumental Variables
Use an external variable that shifts the probability of treatment but does not directly affect the outcome.

Examples:
- draft lotteries
- school admission lotteries

Key issues:
- not everyone complies with the instrument
- estimates apply to a local group (compliers)
- exclusion restrictions are hard to justify

---

### Regression Discontinuity Design
Exploit sharp cutoffs in treatment assignment.

Idea:
- units just above and just below the cutoff are very similar
- differences in outcomes near the cutoff can be interpreted causally

Credible locally, but applies only near the threshold.

---

### Difference-in-Differences
Compare changes over time between treated and control groups.

Key assumption:
- treated and control groups would have followed parallel trends absent treatment

Commonly used for policy evaluation.

Threats include:
- violated parallel trends
- differential shocks
- anticipation effects

---

## Mental checklist going forward
For any causal claim:
- What is the treatment?
- What is the outcome?
- What is the counterfactual?
- Which assumptions identify the effect?
- How could those assumptions fail?


WHAT TO LEARN:
Learn how each of these five research designs works
Learn the strengths and weaknesses of these five research designs
Learn how to implement these research designs
Improve your programming skills
Improve your writing skills
Learn how to think critically about causal claims

## Causal inference challenges: Example 1 – Job training

The first motivating example is a county-level job training program aimed at unemployed individuals.

This question is interesting because long-term unemployment is often caused by structural shifts in the economy that leave workers without in-demand skills. Job training programs attempt to provide both soft skills (punctuality, workplace behavior) and hard skills (Excel, IT, trade skills, driving) to improve employment prospects.

The treatment is participation in the job training program.
These treatments were primarily soft skills and hard skills 


Possible outcomes of interest include earnings, employment status, job stability, or hours worked.
CAUSAL
---
The causal question is:  
How much more or less does Sarah earn *because* she enrolled in the training program?

This question contrasts two states of the world:
- Sarah enrolls in training
- Sarah does not enroll in training

The core problem is that we only observe Sarah’s earnings after training. We can not observe the hypothetical of what she would have earned without training. That missing outcome is the counterfactual.

Two natural but flawed counterfactuals are:
- Sarah’s earnings before training
- The earnings of an unemployed person who did not take the training

Both fail because earnings change over time naturally and because people who choose training differ systematically from those who do not.

---

## Causal inference challenges: Example 2 – College attendance

The second example asks whether going to college has a positive economic return.

We like to think it's a benefit and that most who go are meant to go and therefore suited to do it.

This is interesting for private reasons (tuition costs and foregone earnings) and public reasons (government subsidies for higher education).

The treatment is college attendance, which includes both soft skills (working in groups, discipline) and hard skills (accounting, writing, coding).
CAUSAL
---
The causal question is:  
How much will you earn at age 25 if you go to college versus if you do not?

We have to look at the shape of the data to know how to study this. We expect college earners to start off lower and then outscale

Again, this contrasts two states of the world for the same person.

The problem is that we only observe one outcome. We do not observe what the same individual would have earned without college.

Common but invalid approaches include:
- Using earnings before college
- Comparing to a high school classmate who did not attend college
---
**Aside**:
Suppose we wanted to know the average height of a UCSC student

And we stood outside the gym and surveyed at 8 PM

Probably too tall

But he says let's do a bunch of other colleges to fix it

It's a design issue not a size problem

---
These approaches fail because college-goers differ in motivation, ability, background, and expectations in ways that affect earnings.

---
