---
type: lecture
parent: "[[Econ 104]]"
domain: econ
status: draft
---
Assignment
1. Making Tables
	1. Making Tables
		1. Summ Stats
		2. Balance
		3. Regression
	2. Make those tables look good
		1. Pretend to be a presenter of data irl
	3. Do not take stata screenshots
	4. Sections will go over nice looking professional tables
2. Writing
	1. We need to practice writing about this and thinking in our own ways
	2. Basically as soon as you are done writing these tables write about them

--- 
# Lesson 2 cont.

We need to talk about regressions in order to do HW
## Ordinary Least Squares: Example 1

What can we learn from this output?  
![[Pasted image 20260113095932.png]]

We do 3 decimal points like in HS


Econ 104 OLS 14 / 20

---

## Ordinary Least Squares: Example 2

![[Pasted image 20260113100022.png]]

This is making some coarse assumptions A. It omits nonattenders B. That the relationship is a straight line

The intercept is 0 days attended's expected's score
Econ 104 OLS 15 / 20

---

## Ordinary Least Squares: Example 3

This is an example of a levels-levels regression, where both the test score and attendance are continuous measures.

$$  
\text{finalscore}_i=71.838+2.413,\text{attend}_i  
$$

How do we interpret the intercept?  
- The predicted score of a student who attends 0 classes
How do we interpret the coefficient on “attend”?  
- Each class attended increases the predicted score by 2.413 points
- WE DO NOT INFER CAUSALITY UNLESS DEMONSTRATED
Econ 104 OLS 16 / 20

---

## Ordinary Least Squares: Example 4

If our four assumptions are met, then $\hat{\beta}_1$ is an unbiased estimate of $\beta_1$, the effect of attending class on final exam score.

**Assumption 1**: Do you think the true relationship in the population is linear in the parameters and correctly specified?

$$  
\text{final}_i=\beta_0+\beta_1\text{attend}_i+u_i  
$$
- It's hard to guess linearity without demonstrating it
**Assumption 2**: Does our sample of data reflect the population of Econ 113 students?  
- Probably, but not the current one, it's probably well represented
- It's not of students who had already done 104 who had passed.
**Assumption 3**: Is attendance constant in our sample (i.e. do we have variation)? 
- No. There's variation of attendance. Ironically from an econometrician's perspective a more spread data set gives us more explanatory power to answer the core question. TLDR; if basically everyone attends everything the regression is kinda meaningless 
**Assumption 4**: Is the error $u$ correlated with attendance (i.e., do we have omitted variables)?  
- Study, hard workers
- [[Omitted Variable Bias]]
	- You can have things that push up and push down
	- One might be being a math genius
	- The other might be student effort


SO WE WONT CALL IT CAUSAL

Econ 104 OLS 17 / 20

---

## Units of Measurement 1

> Dan Friedman - famous professor that was based out of here

Most important skill is  that students need to know how to read and interpret regression results according to him 

That 2.4 the sum of the true causal effect but also capturing the other biases

How do we interpret the coefficients if we have a binary treatment? For example, suppose we estimate the effect of attending college (0,1) on hourly wages at age 30:

$$  
\text{hourlywage}_i=18.45+11.22,\text{college}_i  
$$

How do we interpret the intercept?  
- The mean hourly wage for people who don't attend college
How do we interpret the coefficient on “college”?  
- The predicted mean hourly wage for college education havers 


Econ 104 OLS 18 / 20

---

## Units of Measurement 2

How do we interpret the coefficients if the outcome variable is in natural logs?

$$  
\ln(\text{hourlywage}_i)=2.94+0.44,\text{college}_i  
$$

How do we interpret the intercept?  
- Don't try and interp without doing it to the e so don't try and interp, all we're interested in in this is the coefficent  points
How do we interpret the coefficient on “college”?  
- by taking the 44% higher 
Econ 104 OLS 19 / 20

---

## Units of Measurement 3

How do we interpret the coefficients if the outcome variable is binary?

$$  
\text{employed}_i=0.81+0.14,\text{college}_i  
$$

How do we interpret the intercept?  
- The probability of being employed without college aka 81% are employed 
How do we interpret the coefficient on “college”?  
- The probability of being employed increases the chance by 14 percentage points NOT 14% bc 14% of 81% is not the same
Econ 104 OLS 20 / 20

# Lesson 3
NEED TO BE ABLE TO AT A GLANCE INTERP THESE THREE BOYS

Determining how to do good hypothesis testing, this is what it's all about in econometrics

1. T-tests
2. P-values
3. Confidence intervals

Assumptions

Under the four assumptions:
$$t= \frac{(\hat\beta _j - \beta_j)}{se(\hat\beta _j)}$$
Why is the mean 0? $\hat\beta_j - \beta_j$ goes to 0 as the sample gets large because $\hat\beta_j$ is unbiased (e.g. because we have a representative sample.)

Why is the variance 1? because we are dividing $\hat\beta_j$ 

## Slide 3 / 28

```text
Assignment 1 - guidance


      Evaluate an RCT: balance tables

      Evaluate an RCT: regressions
      Make formatted tables that are clear and well-labeled (no Stata variable
      names or Stata screenshots)

      Turn in tables and complete code as one PDF




        Econ 104                   Hypothesis Testing                            3 / 28
```

## Slide 4 / 28

```text
  Hypothesis Testing: Regression Coefficients




Econ 104           Hypothesis Testing           4 / 28
```

## Slide 5 / 28

```text
Hypothesis Testing - Regression Coefficients


  OLS assumptions necessary for βb1 to be the best linear unbiased estimator of the
  true population βj :

       Assumption 1: The model in the population is linear in parameters and
       correctly specified y = β0 + β1 x1 + β2 x2 ... + βk xk + ui .

       Assumption 2: We have a random sample of x,y pairs from the population
       of interest.

       Assumption 3: None of the independent variables (Xs) are constant.




Econ 104           Hypothesis Testing           5 / 28
```

## Slide 6 / 28

```text
Hypothesis Testing - Regression Coefficients


  Assumption 4: Zero conditional mean assumption:
                       E(u|x1 , ..., xk ) = 0.

  Under assumptions 1-4, βb1 is an unbiased estimator of the true population β1 .


  But we know βb1 will vary from sample to sample.

  It has a distribution.




Econ 104           Hypothesis Testing           6 / 28
```

## Slide 7 / 28

```text
Hypothesis Testing - Regression Coefficients


 Because ( bβj −βj )/se( bβj ) has a standard normal distribution N(0,1), we can examine statistical significance in several ways: 1 Check our t-statistic against the standard normal distribution. 2 Use the standard normal distribution to compute exact p-values. 3 Construct confidence intervals for the estimate



Econ 104           Hypothesis Testing           7 / 28
```

## Slide 8 / 28




Because $$\frac{(\hatβj −βj )}{se(\hatβj )}$$ has a standard normal distribution N(0,1), we can examine statistical significance in several ways: 1 Check our t-statistic against the standard normal distribution. 2 Use the standard normal distribution to compute exact p-values. 3 Construct confidence intervals for the estimate.




Econ 104                      HypothesisTesting                           8/28

![[Pasted image 20260113103518.png]]
p val needs to be less than .05 it's not stat sig at the 95%

So we're trying to be 95% confident right it includes 0 which is why we're not sure because 0 might have been the coefficent


## Slide 9 / 28

Test if the relationship between attendance and score is statistically significant: finalscore \ i = 

$$71.838+2.413attendi 
\\ (5.665) \\(1.253) $$
Those are the standard errors conventionally but some journals will put p val in the parentheses and it drives economists up a wall bc it confuses 
- The notation changes 
- Not a single person does 1 sided tests


1 Null hypothesis H0 : β1 = 0. Attendance has no effect on final score. 

2 Alternative hypothesis HA : β1 ̸= 0. Attendance has effect on final score. 

IRL nobody talks like this with null and alt they just say it is or it isn't 

3 Choose a significance level (often 5 percent). This means that if the null is true, we will incorrectly say it is false 5 percent of the time just by chance. Find the t-critical = 1.984.
We've decided as economitricians are okay being wrong 5% of the time

4 Compute the t-statistic: $$ t −stat = \frac{\hatβ_1−0}{se(\hatβ_1)} = \frac{2.413−0} {1.253} = 1.93 $$

Our crit value 

5 Because $|t −stat| < t −crit$, we do not reject the null that $β1 = 0$ at the 5 percent level. The relationship between attendance and scores is not statistically significant at the 5 percent level.


## Slide 10 / 28
Hypothesis Testing - Regression Coefficients: t-test

The null is that attendance is unrelated to final score, or $\beta_1=0$. If this is true, then the t-stat should be near zero (in a statistical sense).

![[Pasted image 20260113104811.png]]

Figure text:
    
- If the null is true this is the distribution of the t-statistic.
    
- Let’s draw the rejection regions for a t-stat of 1.93.
    
- In your opinion, is the t-statistic far from zero?

That's why he doesn't like t-tests because its either a yes or a no it just throws away information

![[Pasted image 20260113104811.png]]

## Slide 11 / 28

Hypothesis Testing - Regression Coefficients: t-test

Limitations of standard t test approach presented above:

- You reject or fail to reject without conveying how strong the evidence is (throwing away information).
    
- Two very different results, tstat=-5.9 and tstat=-2.1, but both reject.
    
- Two very similar results, tstat=-2.0 and tstat=-1.9, but only one rejects.
    


HypothesisTesting-RegressionCoefficients: p-values

One way to convey how strong the evidence is by using a p-value.

t- sE. t=1.2

So there's something like a 25% chance of getting a value that large

The p-value is the probability that the t-statistic would be as or more extreme than what we observe if the null hypothesis is true.

In the previous example: t = 1.93

Then the p-value is:
p = 2*Pr(z>1.93)
This is 0.053 or 5.3 percent
It can be computed using a normal distribution table or in statistical software.

		p-value is the chance of getting that t.   


Interpreting p-values:
A small p-value means it is unlikely we would have observed the t-statistic if
the null hypothesis were true.
So a small p-value indicates the null is unlikely to be true.

Can you reject at the 5 percent significance level if p = 0.053?

No, but it is close.

So what do you conclude?

One conclusion:
We find suggestive evidence that college has a positive economic return. But the
evidence is not quite strong enough to conclusively reject the null at the 5
percent significance level.



Econ 104                      HypothesisTesting                             12/28

Econ 104 | Hypothesis Testing | 11/28

## Slide 12 / 28

Hypothesis Testing - Regression Coefficients: p-value

**P-value:** the exact probability associated with a t-statistic.

- The p-value is how unlikely is the $\hat{\beta}_1$ we observe if the null is true.
    
- Compute t-stat and plot it on the std normal distribution $t-stat=1.93$
    

Figure text:

- Standard Normal Distribution
    
- y-axis tick labels: 0, .1, .2, .3, .4
    
- x-axis tick labels: -4, -3, -2, -1, 0, 1, 2, 3, 4
    
- P-value is the sum of all the events less likely than the one we observe.
    
- There is a about a 5.6 percent chance that a difference as large or larger than the one we observe would occur by chance.
    
- Stata reports p-values. Can also estimate from a t-table or standard normal table.
    

Econ 104 | Hypothesis Testing | 12/28




## Slide 13 / 28

Hypothesis Testing - Regression Coefficients: confidence intervals

**Confidence Interval:** a range in which we are confident that the true $\beta_j$ must fall given the estimated coefficient.

- The interval is determined by three factors:
    
    - the estimated coefficient,
        
    - the standard error of the estimate,
        
    - the critical t-value needed for our desired confidence level.
        
- It is given by the following expression:
    

$$β^j−tcrit∗se(β^j),β^j+tcrit∗se(β^j)][\hat{\beta}_j-t_{crit}*se(\hat{\beta}_j),\hat{\beta}_j+t_{crit}*se(\hat{\beta}_j),
β^​j​−tcrit​∗se(β^​j​),β^​j​+tcrit​∗se(β^​j​)$$


- In our example, the 95 percent confidence interval is:  
    $[2.413-1.984_1.253,2.413+1.984_1.253]=[-0.073,4.899]$
    
- What do you notice about this confidence interval?
    

Econ 104 | Hypothesis Testing | 13/28

## Slide 14 / 28

![[Pasted image 20260113110057.png]]

The t stat is super large and the p value is miniscule and stat significance

