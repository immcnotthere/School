---
title: Measurement Error
course: Econ 104
topic: Classical Measurement Error
tags:
  - econometrics
  - measurement-error
  - attenuation-bias
  - OLS
  - regression
slides: 12
type: concept
parent: "[[Econ 104]]"
domain: econ
status: draft
---
Econ 104 | Measurement Error | 1/12

---

## Measurement Error: Classical

Econ 104 | Measurement Error | 2/12

---

## Measurement Error

We want to estimate the relationship between Y and X:

$$Y_i = B_0 + B_1 X_i + u_i$$

- For the moment, let's ignore the issue of omitted variable bias and focus instead on the effect of measurement error.
- Measurement error is error in the measurement of either *Y* or *X*.
- Unsurprisingly, measurement error can result in biased estimates of $B_1$.
- Suppose we wish to estimate the relationship between how many drinks somebody has in a typical week (*X*) and their health (*Y*).
- Why might *X* (number of drinks in a week) be measured with error?

Econ 104 | Measurement Error | 3/12

---

## Measurement Error

What is the effect of classical measurement error in reporting of the *X* variable?

- Remember this is the case when people give honest reports but sometimes they are too high or low, but on average they are correct.
- We can write the reported $X^*$ as:

$$X^*_i = X_i + \varepsilon_i$$

where *X* is the true value and $\varepsilon_i$ is the reporting error and has a mean of zero and is uncorrelated with *X* and *Y*.

- What happens when we estimate the regression using the mismeasured $X^*$:

$$Y_i = \beta^*_0 + \beta^*_1 X^*_i + u_i$$

Econ 104 | Measurement Error | 4/12

---

## Measurement Error

The true relationship is $Y_i = \beta_0 + \beta_1 X_i + u_i$ but we estimate it with the $X^*$ we observe instead of the true value *X*. Remember, $\hat{\beta}_1 = cov(X,Y)/var(X)$.

$$\hat{\beta}^*_1 = \frac{Cov(X^*, Y)}{Var(X^*)}$$

$$= \frac{Cov(X + \varepsilon,\ Y)}{Var(X + \varepsilon)}$$

$$= \frac{Cov(X, Y) + Cov(\varepsilon, Y)}{Var(X + \varepsilon)}$$

$$= \frac{Cov(X, Y)}{Var(X) + Var(\varepsilon)}$$

- Since variances are positive, our estimate of $\beta_1$ will be biased downwards (towards 0). This is called **attenuation bias**.
- The amount of bias is a function of how much noise there is on our measure of *X* relative to the amount of true signal.

Econ 104 | Measurement Error | 5/12

---

## Measurement Error

Estimate of $Y_i = B_0 + B_1 X_i + u_i$ with no measurement error

*(Scatter plot: Y vs X\*, tight linear relationship, no spread)*

Econ 104 | Measurement Error | 6/12

---

## Measurement Error

Measurement Error in Red $X^* = X + UniformError(-3, 3)$

*(Scatter plot: black dots = true X, red dots = mismeasured X\*; red regression line is flatter than black)*

Econ 104 | Measurement Error | 7/12

---

## Measurement Error

Measurement Error in Red $X^* = X + UniformError(-6, 6)$

*(Scatter plot: larger uniform error; red regression line is even flatter — more attenuation bias)*

Econ 104 | Measurement Error | 8/12

---

## Measurement Error

What is the effect of classical measurement error in reporting of the *Y* variable?

- This is the case when people give honest reports but sometimes they are too high or low, but on average they are correct.
- We can write the reported $Y^*$ as:

$$Y^*_i = Y_i + \varepsilon_i$$

where *Y* is the true value and $\varepsilon_i$ is the reporting error and has a mean of zero and is uncorrelated with *Y* and *X*.

- What happens when we estimate:

$$Y^*_i = \beta^*_0 + \beta^*_1 X_i + u_i$$

Econ 104 | Measurement Error | 9/12

---

## Measurement Error

The true relationship is $Y_i = \beta_0 + \beta_1 X_i + u_i$ but we estimate it with the $Y^*$ we observe instead of the true value *Y*.

$$\hat{\beta}^*_1 = \frac{Cov(X, Y^*)}{Var(X)}$$

$$= \frac{Cov(X,\ Y + \varepsilon)}{Var(X)}$$

$$= \frac{Cov(X, Y) + Cov(X, \varepsilon)}{Var(X)}$$

$$= \frac{Cov(X, Y)}{Var(X)}$$

$$= \hat{\beta}_1$$

- So there is no bias in the estimate when there is measurement error in Y.
	- You'll just get larger standard error
- Can you think of any negative effects of having measurement error in Y?
	- 

Econ 104 | Measurement Error | 10/12

---

## Measurement Error

Estimate of $Y_i = \beta_0 + \beta_1 X_i + u_i$

*(Scatter plot: Y and Y\* vs X; regression line fits both tightly — slope unchanged)*



Econ 104 | Measurement Error | 11/12

---

## Measurement Error

Measurement Error in Red $Y^* = Y + UniformError(-3, 3)$

*(Scatter plot: red dots = mismeasured Y\*; red regression line nearly identical slope to black — no attenuation)*

Econ 104 | Measurement Error | 12/12

It makes our residuals far bigger but we get an unbiased estimate

Try to get less biased data

So get multiple measures of the same 

independent repeatable data

Cleaning up data is the first way of reducing measurement error

ex. they went to go see twins

They asked both people their stats but without differentiating along lines of twins

And then they divided the ident. twins into pairs

In then they got a lower estimated coefficient on education 

Imagine if they had identitcal education levels then the return on earnings would be 0 

Their solution for measurement error was to report the education of the twin's education

**SO THE FIX FOR MEASUREMENT ERROR IS DUAL SAMPLING**

First stage: Karen's Education on Sharon 

And we think this estimate is biased on measurement error

We Reduced Form it

First stage: Sharon's ed  Karen report of sharon's educ 
Reduced Form: Regress Sharon's earnings on karen's report of sharon's education

But in IV = two wrongs make a right = 



This creates downwards bias

So instrumenting usign twin-reporting educatin reduce attenutation bias to measurement error

---
LABOR LAW

Researchers are interested in researching the return of schooling on earnings

Back in the day education wasn't compulsory

Many states adopted voluntary educational floors

Required school permission to leave

North adopted first

South later

---

Acemoglu and Angrist (2000)

They used diff-and-diff to estimate the effects

this would have multiple states and years as we saw for the MDLA

First stage effect: impact on years of schooling and wages

Reduced Form: 


---
What they found

7 not much
8 not much
9 a lot of effect and made them stay far later in school

They ran it all together on the second stage and they got the effect of each year of education increases 12.4% in wages

This applies to those who would've dropped out of school in year 8 or 9

We're not learning about college and hs graduates

IS there any sense that this is local?

These are southern states and this is a time period in the early 1900s

---

It turns out these results are bullshit

But the trends in education are totally drastically different

Is Maine a good estimate for the south NO!

---

So we're gonna try and control for intra trends in the north and southern groups and then using that to account for it and year by year controls


---

If we look at each adopter per age group

WE DONT HAVE A FIRST STAGE

THERE WAS NO IMPACT OF THESE POLICIES THE SOUTHERN STATES WERE ALREADY ON AN UPWARDS TREND

---

Compulsory Schooling Laws Estimates

These are fairly recent

Some states let drop out at 16,17,18

---

Josh Angrist and Kruger

One of the most famous applied microecon papers

In many states, children enter school the year they turn 5

A child who turns 5 on Jan 1 

Is young enough but they must wait a year

Dec 31 gets to go 

That would be a good rgression discontuinity study we should be thinking

---

This means that these kids are in a different position when they drop out

the kid is gonna be one grade less 

One kid is going to get fundamentally more education than the other kid

---

Exploiting the randomness

2 children born in adjacent months

one child gets an extra year of schooling due to being eligbible to start at a younger age

The kids born in the first quarter will get less
children in the later 2 will get more

---

We see year of birth and it's divided into quarters

And what we see consistently that every year the people born in the fourth quarter got education and got far more years of education 

Those born in the beginning of the year got less eucation

What is the relationship between birth quarter and schooling

It turns out a lot of these aren't right because times of birth are correlated with socioeconomics

---

The relationship between birth quarter and earnings, so the finding is that those born in the end of the year earn more and they get more educated

To get our IV estimate and we divide thecoeffcent from the fs and the rf to get 7.4 return per year

---

Who does this apply to?

If you're someone who would've dropped out in 16 in the 30s

We're not learning about the always takers (college goers) and neither the never takers (gonna leave no matter the legality)

Difficult to argue that additional schooling is the only way in which being the youngest child in a cohort affects future earnings, which is necessary for the IV interpretation

---


Measurement error could be on the final anyting covered in class

obv the bias will be towards hw and towards the main takeaways

There are students who are methodical

If someone

The style will be similar but more than 6 questions

Asking about a table how do we interp.

Here's some data how do we code...

---

There will be some questions straight from the book

---

Don't care as much about the outputting

It's about how do understand the regression 

Like dif and dif RCT

---

He'd go through all the end of class exercises and read the lecture notes

Go back through the book and make sure you understand each of the examples and know them

Understand the thrust of what makes a good dif and dif and not a bad one

It's about intuition

Doe we understand why manupulation is bad for a discon.

what would make good and bad estimates


---
Undoubtedly some of the first parts will come up

It'll be almost impossible to write a first half without refrencing a second half

How many questions: 9 or 10

---
Chapters 1-5 not the mathematical appendices

---



