---
type: concept
parent: "[[Econ 104]]"
domain: econ
status: draft
---
# Introduction

Economists reputation for dismality is a bad rap
the excitement comes from learning cause and effect in human affairs

Our questions in this textbook are the questions of the day 
- Will loose monetary policy speak economic growth or fan the fires of inflation
- Iowa farmers and the Federal Reserve chair want to know
- Will mandatory health insurance make Americans healthier
Economists use of data to answer cause-and-effect questions constitutes the field of applied econometrics

US college graduation rates are on the downtick 
Politicians and policy analysts blame on tuition hikes and large student loans use to finance their studies

Increased student borrowing derails some who would stay on track

The fact that the students most likely drop out of school often shoulder large student loans would seem to substantiate this hypothesis

How should we interpret the negative correlation between debt burden and college graduation rates?

Because lower income families are less likely to complete a degree than higher income we should be skeptical for multiple reasons

therefore by virtue of the correlation between family background and college debt the contrast in graduation rates between those with and without student loans not an other things equal comparison or ceteris paribus

Ceteris paribus is maybe in Latin to keep kids from realizing that all things being equal is hard to engineer and maybe impossible.

Our first line of attack on the causality problem is a randomized experiment, often called a randomized trial. 

Random assignment isn't the same as holding everything else fixed, but it has the same effect. Random manipulation makes *other things equal* hold on average across the groups that did and did not experience manipulation. 



For starters, motivated by the contemporary American debate over health care, the first chapter describes two social experiments that reveal whether, as many policymakers believe, health insurance indeed helps those who have it stay healthy. Chapters 2–5 put our other tools to work, crafting answers to important questions ranging from the benefits of attending private colleges and selective high schools to the costs of teen drinking and the effects of central bank injections of liquidity.

**The path to causal understanding is rough and shadowed as it snakes around the boulders of selection bias. And yet, masters of ’metrics walk this path with confidence as well as humility, successfully linking cause and effect**

Our final chapter puts the Furious Five to the test by returning to the education arena. On average, college graduates earn about twice as much as high school graduates, an earnings gap that only seems to be growing. Chapter 6 asks whether this gap is evidence of a large causal return to schooling or merely a reflection of the many other advantages those with more education might have (such as more educated parents). Can the relationship between schooling and earnings ever be evaluated on a ceteris paribus [[basis]], or must the boulders of selection bias forever block our way? The challenge of quantifying the causal link between schooling and earnings provides a gripping test match for ’metrics tools and the masters who wield them.

Chapter 1

/r Our path begins with [[Experimental Random Assignment]] 
as a framework for causal questions 
&
a benchmark by which the results from other methods are judged

/tldr Experimental random assigment will be the guiding principle for asking and analyzing questions

/r what follows are two illustrations of 

>1.1 In Sickness and in Health (Insurance)

/r America has significantly poor outcomes compared to what it invests into itself

/r There is spotty coverage in America, Hospitals will not turn all away nonetheless, but there is no requirement for long term care. It stands to reason then that mandated health insurance with long term care might yield dividends in health outcomes therefore creating the push for subsidized universal health insurance on the belief that it would be worth it.

/r Our ceteris paribus question in this context is the health of someone with insurance compared to the same person with no health insurance. We can't live in both worlds for the person at the same condition

/r Anecdotes from written works about how "acts demolish their alternatives, that is the paradox." - Light Years, James Salter

/r We'll see how we answer this question using some actual examples of how we do it. With the index being *outcome*: a measure we're interested in studying. /v The causal relation of interest here is determined by a variable that indicates coverage by private health insurance. We call this variable the *treatment* those w/ insurance as the *treatment group* those w/o *comparison* or *control group*. A good control group reveals teh fate of the treated in a counterfactual world where they are not treated.

/r The first row compares the average health index of insured and unisured Americans. The differences between men and women lie are large when it's considered that stdv of the health index is 1 These gaps may be the health dividend trying to be proven.  

/r Take the case of a Kazakhstani and a Chilean who arrive at MIT to take this study

/r each has their reason to take and or reject the health care offered. Because the kazakhstani's choice to take the healthcare doesn't make him any healthier than had he not in the face of cold new england winters he creates a false apperance that taking insurance doesn't improve health outcomes 

$$
\begin{aligned}
Y_{\text{Khuzdar}} - Y_{\text{Maria}}
&= Y_{1,\text{Khuzdar}} - Y_{0,\text{Maria}} \\
&= \underbrace{\left\{ Y_{1,\text{Khuzdar}} - Y_{0,\text{Khuzdar}} \right\}}_{1}
\;+\;
\underbrace{\left\{ Y_{0,\text{Khuzdar}} - Y_{0,\text{Maria}} \right\}}_{-2}.
\end{aligned}
$$
