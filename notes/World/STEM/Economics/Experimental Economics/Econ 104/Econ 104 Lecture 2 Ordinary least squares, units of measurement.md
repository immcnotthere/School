---
type: lecture
parent: "[[Econ 104]]"
domain: econ
status: draft
---

# Lecture 2

## Review: Ordinary Least Squares

Econ 104 OLS 1 / 20

---
Cont.
---

## Research design: Randomized Controlled Trials (RCTs)

Randomized controlled trials are presented as the gold standard for causal inference.

In an RCT, researchers recruit a sample and randomly assign individuals to treatment and control groups.

Randomization removes selection into treatment. As a result:
- Treated and control groups are similar in observables
- Treated and control groups are similar in unobservables
- The only systematic difference between groups is treatment status

If properly implemented, RCTs produce causal estimates.

Examples
- imagine a work program for job training you have a control with non accepted 
	- 
- Imagine college
	- Are you going to deny students education?
	- The best one can do is scholarship

However, RCTs are not always feasible. Researchers cannot force countries to open to trade. They are not always ethical, such as forcing people to smoke. They can also be prohibitively expensive, such as paying many people to attend college.


- Imagine college
	- Are you going to deny students education?
	- The best one can do is scholarship but that is prohibitively expensive

Because of these limitations, economists rely heavily on alternatives to RCTs.



---

## Research design: Selection on observables (regression)

Selection on observables is one of the most common research designs in the social sciences.
- Common because it's easy not because it's good
- If it was a research article he was reviewing he'd almost automatically reject it

Researchers compare people who chose the treatment with those who did not and attempt to adjust for differences using regression and control variables.
- It's myopic because it's imagining that people who go to college and don't are twins and then adding in controlled parameters that account for differences
- The truth is that you can't account for everything


This approach is common not because it is strong, but because it is easy to obtain data and run regressions using surveys or administrative datasets.

A typical regression might start with:
$$
earn_i = \beta_0 + \beta_1 BA_i + \varepsilon_i
$$

and then add controls:
$$
earn_i = \beta_0 + \beta_1 BA_i + \beta_2 HSGPA_i + \beta_3 Gender_i + \beta_4 Motivation_i + \varepsilon_i
$$

Omitted variables already would be (in class generated):
- Schooling quality
- Parental Income


The key issue is that it is extremely difficult to identify and measure all relevant differences between treated and untreated individuals. Some important characteristics, such as motivation or ambition, are hard to observe. Even when variables are included, functional form assumptions may be incorrect.
- Hard to identify all the ways in which those who go to college differ from those who don’t. What are some other possible differences? 
- Some dimensions on which you know people differ might be hard to measure (e.g.,motivation). 
- Some of these differences might not affect the outcome linearly (i.e., functional form is misspecified).


---

## Research design: Instrumental Variables (IV)

Instrumental variables exploit random or nearly random variation in the probability of receiving treatment.
	Effect of military service - leverage assignment of draft lottery numbers in Vietnam war 
	Effect of charter schools - compare children who got in via lottery with those who did no

>Examples include:
>- Military service induced by the Vietnam draft lottery
>- Charter school attendance induced by admission lotteries

>Compare the outcomes of the lottery winners and losers
	This is a valid comparison as the two groups were created by a lottery so they should be similar. 

tldr; Lottery winners and losers are comparable because assignment is random.

>We then need to adjust the estimates for the fact that not everyone did what the lottery told them to. 
	Some people with low lottery numbers in the Vietnam draft still did not serve in the military due to medical exemptions or refusing to enlist. 
	Some students admitted to charter schools ultimately decide not to attend.

>However, not everyone complies with the assignment:
>- Some people with low draft numbers did not serve
>- Some students admitted to charter schools did not attend

/tldr not everyone will comply 

E.g. 
Imagine cases T and C
T = admitted 
Some who get admitted won't go, imagine it was up to half
C = Denied admitted/control
Let's suppose none go so perfect compliance



IV methods adjust for this imperfect compliance and estimate causal effects for those whose treatment status was influenced by the instrument.

---

## Research design: Regression Discontinuity (RD)

>Regression discontinuity exploits sharp changes in treatment probability at a cutoff.

>An example is eligibility for Gifted and Talented Education based on an IQ threshold.

>Comparing all students in GATE to non-GATE students is invalid because they differ systematically. However, students just above and just below the cutoff are very similar in ability.

>The counterfactual for students who barely qualified comes from students who barely missed qualification.
- A huge drawback no?

>Causal effects are identified locally around the cutoff.

---

## Research design: Difference-in-Differences (DiD)

tldr; choosing a good control is the art and 

>Difference-in-Differences: compares the before and after outcomes for treatment and control groups

>- Suppose we want to test how a tax increase on cigarettes in California affected the rate of smoking? 
>	- We cannot just compare smoking in California before and after the tax as smoking rates have been going down over time. 
>	- Need to estimate the drop that would have occurred in the absence of the law change and adjust for it.

tldr; For example, to evaluate a cigarette tax increase in California, we cannot simply compare smoking before and after the tax because smoking rates were already declining.

>Instead, we compare California’s change to changes in similar states, such as Nevada or Arizona, where the law did not change.

>Examine how smoking changed in Nevada or Arizona (which had no change in the law). This provides an idea of how California might have changed in the absence of the change in taxes.

These control states provide an estimate of the counterfactual trend for California in the absence of the tax.

>That is, estimate the counterfactual trajectory for California using Nevada or Arizona.

The key assumption is that treated and control groups would have followed parallel trends without the policy change.

## Today’s Lesson

1. Ordinary Least Squares
    
2. Stata Example
    
3. Units of Measurement  
    Econ 104 OLS 2 / 20

Need to know 
- levels -> hourly wage
- natural logs -> ln wage **percents**
- binary -> emol(01) **percentage points**

Use the case of california legalizing weed 10 went to 12

News and media and vernacular confuses precents and percentage points
2% percentage point increase 10 to 12 ~ 20% increase 10 to 12
Everyone says percents but percentage points are often more significant and not painted a

---

## Ordinary Least Squares

**Ordinary Least Squares**: A way of estimating the relationship between one variable and another variable (or variables). Fits a line (or hyperplane) that summarizes this relationship by getting as close as possible to the data points.  
Econ 104 OLS 3 / 20

Example: How does final exam performance vary with class attendance?

$$  
\text{finalscore}_i=\beta_0+\beta_1\text{attend}_i+u_i  
$$

I have data on attendance for 5 days throughout the quarter for four students:

|Individual|Attendance|Final Exam Score|
|---|--:|--:|
|Asha|4|92|
|George|2|75|
|Talia|2|88|
|Kim|0|64|

---

## Ordinary Least Squares

We want to estimate the line that fits the data as closely as possible. OLS minimizes the sum of the squared distances from each of the data points to the line.  
(See figure on slide 4: “Relationship Between Exam Score and Classes Attended”.)  
Econ 104 OLS 4 / 20
![[Pasted image 20260108104040.png]]
We take the distance between the regression and the data called residuals we square then add them all up (we used to do absol val in the 80s)

Then we try to find the best intercept and Beta 1 based off of that

Same thing for multivariate


---

## Ordinary Least Squares

OLS chooses the slope and intercept ($\hat{\beta}_0$ and $\hat{\beta}_1$) that minimize the average squared distance from the line to the data points.

Look at the 

The distance from the final exam score for individual $i$ to the line is

$$  
\hat{u}_i=\text{final}_i-(\hat{\beta}_0+\hat{\beta}_1\text{attend}_i).  
$$

So the squared distance is

$$  
\hat{u}_i^{,2}=\left(\text{final}_i-(\hat{\beta}_0+\hat{\beta}_1\text{attend}_i)\right)^2.  
$$

To make the notation general we will use $x$ for attend and $y$ for final.

We are interested in minimizing this over all the data points, so we will minimize the sum of all $\left(y_i-(\hat{\beta}_0+\hat{\beta}_1x_i)\right)^2$.  

Econ 104 OLS 5 / 20


Our goal is to minimize the sum of the squared errors:

$$  
\min \sum_{i=1}^{n}\hat{u}_i^{,2}  
$$

$$  
\min \sum_{i=1}^{n}(y_i-\hat{\beta}_0-\hat{\beta}_1x_i)^2  
$$

First order conditions (set derivatives $=0$):

$$  
\frac{\partial}{\partial \hat{\beta}_0}=-2\sum_{i=1}^{n}(y_i-\hat{\beta}_0-\hat{\beta}_1x_i)=0 \quad (1)  
$$

$$  
\frac{\partial}{\partial \hat{\beta}_1}=-2\sum_{i=1}^{n}x_i(y_i-\hat{\beta}_0-\hat{\beta}_1x_i)=0 \quad (2)  
$$

We have two equations, (1) and (2), and two unknowns: $\hat{\beta}_0$ and $\hat{\beta}_1$.  
Econ 104 OLS 6 / 20

We then solve those as a system of equations
So we have to do the chain rule bc of the square

---

## Ordinary Least Squares

If we divide (1) by $-2$ and then by $n$, we get:

$$  
(1)\Rightarrow \sum_{i=1}^{n}(y_i-\hat{\beta}_0-\hat{\beta}_1x_i)=0  
$$
Don't forget that our line has to balance the above and below such that the uhat should equal 0 bc it's balancing the distances
secondly that the all the xs added up times the uhats added up should = 0


$$  
\Rightarrow \frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{\beta}_0-\hat{\beta}_1x_i)=0  
$$

$$  
\Rightarrow \bar{y}-\hat{\beta}_0-\hat{\beta}_1\bar{x}=0  
$$

$$  
\Rightarrow \hat{\beta}_0=\bar{y}-\hat{\beta}_1\bar{x}  
$$

This is half of the solution.  we plug this in to the second equation
Econ 104 OLS 7 / 20

---

If we divide (2) by $-2$ and then plug in for $\hat{\beta}_0$ using (1), we get:

$$  
(2)\Rightarrow \sum_{i=1}^{n}x_i(y_i-\hat{\beta}_0-\hat{\beta}_1x_i)=0  
$$

$$  
\Rightarrow \sum_{i=1}^{n}x_i\Bigl(y_i-(\bar{y}-\hat{\beta}_1\bar{x})-\hat{\beta}_1x_i\Bigr)=0  
$$

$$  
\Rightarrow \sum_{i=1}^{n}x_i\Bigl((y_i-\bar{y})+\hat{\beta}_1(\bar{x}-x_i)\Bigr)=0  
$$

$$  
\Rightarrow \sum_{i=1}^{n}x_i(y_i-\bar{y})+\hat{\beta}_1\sum_{i=1}^{n}x_i(\bar{x}-x_i)=0  
$$

$$  
\Rightarrow \hat{\beta}_1=\frac{\sum_{i=1}^{n}x_i(y_i-\bar{y})}{\sum_{i=1}^{n}x_i(x_i-\bar{x})}  
=\frac{\operatorname{Cov}(X,Y)}{\operatorname{Var}(X)}  
$$

This is what we wanted: $\hat{\beta}_1$ in terms of the data.  

Write Cov XY / Var Y on your arm spake the teacher

* TOUCH UP ON THE MATH TO WORK WITH OLS*

Econ 104 OLS 8 / 20

---


$$  
y_i=\beta_0+\beta_1x_i+u_i  
$$

We did this by minimizing the distance from the lines to the data points

$$  
\sum_{i=1}^{n}\left(y_i-(\hat{\beta}_0+\hat{\beta}_1x_i)\right)^2  
$$

to get

$$  
\hat{\beta}_1=\frac{\operatorname{Cov}(x,y)}{\operatorname{Var}(x)}  
$$
The difference between the two points divided by how spread they are

$$  
\hat{\beta}_0=\bar{y}-\hat{\beta}_1\bar{x}  
$$

When we have more than one $x$ variable we have a very similar formula using matrices.  
Econ 104 OLS 9 / 20

---

## Ordinary Least Squares: Assumptions

Under several assumptions, OLS produces the best, linear, unbiased estimates of the $\beta$ coefficients for the population.

**Assumption 1**: The model in the population is linear in parameters

$$  
y=\beta_0+\beta_1x_1+\beta_2x_2+\cdots+\beta_kx_k+u_i  
$$

where the Betas are parameters and $u_i$ is an unobservable random error term, AND the model is correctly specified.

- Least squares model is linear so it will only be the right model if the actual relationship in the population is linear.
    

**Assumption 2**: We have a random sample of $x,y$ pairs from the population of interest.

- If we want to correctly estimate the relationship in the population, we need a random sample that is representative of the population.  
    Econ 104 OLS 10 / 20
    

---

**Assumption 3**: In the sample, none of the independent variables (Xs) are constant (or have an exact linear relationship with each other).

If you want to estimate x over y, x needs to vary duh-doy bc you can't divide by 0 variance

- Remember $\hat{\beta}_1=\frac{\operatorname{Cov}(x,y)}{\operatorname{Var}(x)}$. If $x$ is constant, then $\operatorname{Var}(x)$ is zero.
    
- Can’t estimate how $y$ varies with $x$ if $x$ does not vary.
    

**Assumption 4**: Zero conditional mean $E[u\mid x_1,x_2,\ldots,x_k]=0$.
THE REASON ILL HAVE A JOB IS THIS DOES NOT HOLD, OMMITTED VARIABLE BIAS IS REAL AND CONSTANT
---
- The assumption is that the average (expected value) of $u$ does not vary with the level of $x$.
    
- $u$ captures all the other factors that determine $y$ other than $x$. If any of them vary with $x$ they will bias the estimate of the effect of $x$ on $y$.
    
- If this is violated we have omitted variables bias (endogeneity).  
    Econ 104 OLS 11 / 20
    

---

## Sampling Bias: Selection, Response, and Recall

In order to estimate the population coefficients, we need a sample that is representative. Suppose we want to estimate the relationship between attending class and final exam score in Econ 113. Suppose I ask everyone in class to tell me their final exam score and how many classes they attended.

1. Do you think the selected sample is representative of the population of Econ 113 students?
	1. No because you had to pass
	2. You had to show up to class
	3. You had to choose 104 not 197
    
2. Do you think that those who respond will be representative of the sample?
	1. Not here, not responding
	2. Maybe people don't want to respond bc it's shameful to have done poorly
	These biases have names
	[[Selection bias]], [[Non-response bias]]
    
3. Do you think that people will accurately recall their attendance and grades?  
    Econ 104 OLS 12 / 20
    

---

## Ordinary Least Squares: Example

(See slide 13 image: Stata do-file style example titled “Ordinary Least Squares: Example”.)  
Econ 104 OLS 13 / 20

There are abbreviations for everything common
e.g. summ
`drop if 'condition' ==0`

Nobody runs code in that testing way you make do files so you can just rerun it you
So when correcting you can just tweak this preloaded 



---
