---
type: lecture
parent: "[[Econ 104]]"
domain: econ
status: draft
---
Hypothesis Testing: Means and Differences in Means
Slide 16
We are often very interest in the expected value, or population mean, of some variable Yi (for example, the average health score of people in the U.S.). 
- The population mean can be written as:
		E[Y_i] = mu

---

Slide 17

Var Ybar is telling us how spread out the data is

We get a tighter variation by scaling n 

The more n we have the more precise we get

This doesn't mean we're unbiased

---
Slide 18

SE

You do a square to get standard deviation talks about y

SE talks about the estimate Y bar

What else is gonna help you get a more precise estimate with a bigger sample

When your underlying data is less spread out

Height isn't that hard to estimate with a small sample size

Because heights are so clustered you don't need that much data to get a precise estimate

---

Slide 19
HT is done in the same cookbook way 

But we aren't interested in one mean we're interested in treatment and not treatment

I'm comparing the mean characteristics this is on slide 

If you do randomization correctly

In about 1/20 times at the 5% level you'll find differences between the group but on average you should find no difference between the two groups

You aren't to calculate most of this t-stat formula by hand

So we can do T-tests comparing two variables


---
Slide 20

A good way of testing for balance in an RCT 

Take Treat as a dummy 

Run a regression

Treatment = 0 

That's the lowest age 

Beta 1 is how different the treatment is from the control group

The best coefficient if checking is 0 because we want the groups to be identical

Choppelgaenger 

If B_1 is big then it's awful luck or bad randomization protocol

The great thing is that the syntax of the regression is the same as the operational question

All we'll do is add on additional characteristic variables like female

Slide 20


---
Slide 21

This is more math up front and w/o would make all regressions wrong bc we wouldn't have computed for SE correctly

If we do reg Vote02 treat-real

If we do this it will likely generate the wrong SE because stata assumes [[homoskedacity]] (sigma^2_u)
That is not real life

So we need to know how to assume heteroskedacity

Assume 22 years of education some will be CC English teacher and others will be doctors and lawyers

Homosked assumes that all inputs would be similar 

Real data is a lot more triangular and not linear

The fix for it is quite simple in stata you just write

', robust'

Let's find out what the issue is and how to fix it

So let's find out how we account for hetero

---
26

We start with a simple simple regression

We know it's Cov X,Y over Var o X for Betahat1

We do some math and we end up with x-it's mean times sigma squared 


IF you have homo the expanded equation collapses into the old format of 62/SSST_x

--- 
23

We think it's very unlikely that dispersions are 

Heteroskedacity errors means that Var(u|x)=sigma^2


---
26
Let's take on homo first 

we're assuming all equal errors of var(u|x)=sigma^2

We can cancel stuff out if we treat sigma^2 as a constant

Sigma squared over Sigma sum of squared total of the xs

It's totally unrealistic and we end up with what we had in 113

He's here to tell him it's never true

---
27

If we assume not constant this equation doesn't simplify

This won't simplify and will amplify the numerator

If we do account for hetero and accont for robust and we get points marked off talk to 

---
28

(stata output)

This is now assumongheteroskedacity

Coefficent values had no effect on them

robust has nothing to do with the regression line

It has to do with the standard errors 

Often it is the case that values that are spread away from the mean

Every researcher finds a cool stat sign and doesn't include robust

and all of the sudden the stat sig goes away

We fail now at the 75% level so beyond any reasonable level

THIS IS THE END OF ECONOMETRICS REVIEW

HOW TO USE STATA HOW TO INTERP COEFFECIENTS

SWITCHING OUT OF ECONOMETRICS INTO RESEARCH DESIGNS

---

Lesson 4

---
Slide 1

1 Potential Outcomes Framework
	• Health insurance example
	• Job training example
2 Important Definitions
	• Selection Bias
	• Average Treatment Effect
3 Read Mastering Metrics: Chapter 1

Slide 2

What have we covered so far:
	• Introduction to five research designs
	• Regression review (levels, natural log, binary)
	• Hypothesis testing (t-test, p-value, confidence intervals, robust errors)
Next up:
	• Potential outcomes framework, selection bias
	• Randomized control trials: theory, examples

THIS NEEDS TO FEEL SUPER GOOD TO YOU!!
---
Slide 5

Potential Outcomes Framework: How we conceptualize what we are trying to estimate when we do causal inference.

This is standardized notation

1 Want to estimate the effect of some treatment (e.g., going to college) for an individual i.
	• Denote the treatment effect by: τi
what is $\tau$ 1

[[Tau 1|Tau 1 WIP]] = wages with college - wages without college

The difference of going to college on his earnings
There's no way to see bold states of the world to counterfactual this



2 With a binary treatment, the treatment effect is the difference between two
outcomes:
	• Individual i′s outcome (earnings at 25) with treatment (went to college)
	• Individual i′s outcome (earnings at 25) without treatment (no college)

We'd like to compare these two things 

We don't know what their tau one is because we either get the treatement or we don't

We call it the counterfactual that what doesn't receive treatment

3 The challenge is that we only observe one of these outcomes because the
person either got the treatment or they did not.
	• The outcome that didn’t happen could have happened
	(you might not have gone to college)
	• We call the outcome we do not observe the counterfactual

This will be thought with examples rather than theory 

---
Slide 6

What is the impact of giving someone (John) health insurance on his use of health
services?

Why is this interesting?
	• Current policy debate about insurance (ACA, Medicare for all etc.)
	• Understanding what expansion will do to costs requires knowledge of
	how it affects people’s use of health services.
	• Understand impact of having insurance on health outcomes.

Does having care make you use it more, healthier?

What is the treatment?
	• Having insurance (treated) vs not having insurance (untreated)
	• Need to be clear on what the untreated people get
	(i.e., can they still get medical care)

Untreated people doesn't mean you get no care, hospitals cannot deny treatment

However people who don't have insurance might not go for more threatening conditions

But clearly there is a margin for going and not going, but it's not 1 to 1

Ultimately

This is a causal question. We are asking what happens to a person (John) when he does or does not have insurance. What are some measures of
health services usage we could consider?

Slide 6

---
Slide 7

Suppose we want to know the causal effect of having health insurance on how often an individual (John) goes to the doctor.

- This is the difference between two states of the world:
    
    1. How often John goes to the doctor when he does not have insurance.  
        Potential outcome in the untreated state:  
        $Y_{0,\text{John}}$
        
        - $Y$ denotes the number of doctor visits
            
        - Subscript $0$ denotes the untreated state (no insurance)
            
        - Subscript $\text{John}$ indicates this is the outcome for John
            
    2. How often John goes to the doctor when he does have insurance.  
        Potential outcome in the treated state:  
        $Y_{1,\text{John}}$
        
        - Subscript $$1$$ denotes the treated state (insurance)
            
- The causal effect of treatment for John:  
    $$\tau_{\text{John}} = Y_{1,\text{John}} - Y_{0,\text{John}}$$
This is convention for everyone across the board Y_1 is the treated state

Y_0 is the untreated state

Economists don't care about individuals they care about averages

---

Slide 8

Suppose we observe John at age 25 with insurance.

- We conceptualize outcomes as occurring at a point in time. John at 25 to John at 25
    
    - We are interested in the effect of insurance on health care utilization at age 25.
        
    - The treatment effect of getting insurance at age 25 is likely different from the effect at age 65.
	    - Age is significant as a difference on 
        
    - Which treatment effect do you think is larger, and why?

We want to know about how often he utilized his health care

- We can only observe one of the potential outcomes:
    
    - Either  
        $$Y_{1,\text{John}}$$  
        or  
        $$Y_{0,\text{John}}$$
        
    - The potential outcome we do not observe is called the counterfactual.
        
    - Even though it is not observed, it can be conceptualized. There exists some number of doctor visits John would have had at age 25 if he did not have insurance. 

We don't get to see Y_0

So it makes the math hard
        
- We cannot directly estimate the individual treatment effect for John because we only observe one of the two potential outcomes:  
    $$\tau_{\text{John}} = Y_{1,\text{John}} - Y_{0,\text{John}}$$
---
Slide 9

How much does insurance increase John’s doctor’s office visits, if at all?

- Suppose John has chosen to have insurance at age 25. He goes to the doctor 5 times that year:  
    $$  
    Y_{1,\text{John}} = 5  
    $$

- We do not observe John at age 25 without insurance, but the potential outcome does exist:  
    $$  
    Y_{0,\text{John}}  
    $$
    
- Pretend we can magically observe the counterfactual. When John has no insurance, he goes to the doctor 3 times:  
    $$  
    Y_{0,\text{John}} = 3  
    $$
    
- We can now write the expression for and calculate the treatment effect of insurance:  
    $$  
    \tau_{\text{John}} = Y_{1,\text{John}} - Y_{0,\text{John}} = 5 - 3 = 2  
    $$
---
Slide 10

Insurance increased John’s visits to the doctor by 2:  
$$  
\tau_{\text{John}} = 2  
$$  
In practice, we would not observe both potential outcomes.

- Therefore, we need to estimate  
    $$  
    \tau_{\text{John}}  
    $$  
    without access to the true counterfactual.
    
- We observe John’s doctor’s office visits when he has insurance:  
    $$  
    Y_{1,\text{John}}  
    $$
    
- We do not observe  
    $$  
    Y_{0,\text{John}},  
    $$  
    so we need to estimate it.

Here's the idea, he has a friend


    
- Suppose we use John’s 25-year-old friend Chuck, who has decided not to pay for insurance, as the counterfactual for John.
    
    - Why might Chuck have decided not to pay for insurance?
Reasons for this not being a good counterfactual
	        Maybe because he didn't think he was going to use it
	        They might also might have different health
	        He might not believe he needs medical care

    - Do we observe Chuck in the treated state  
        $$  
        Y_{1,\text{Chuck}}  
        $$  
        or in the untreated state  
        $$  
        Y_{0,\text{Chuck}} , ?  
        $$
    We see him at Y_0
Slide 10
---
Slide 11

### Potential Outcomes Framework: Health Insurance

* Chuck goes to the doctor only 1 time:
  $$
  Y_{0,\text{Chuck}} = 1
  $$
  because he is healthy, and without insurance doctor’s office visits are expensive.

* Let’s estimate the treatment effect for John $$\left(\tau_{\text{John}}\right)$$ using Chuck as the counterfactual:
  $$
  \widehat{\tau}*{\text{John}} = Y*{1,\text{John}} - \widehat{Y}*{0,\text{John}}
  $$
  $$
  = Y*{1,\text{John}} - Y_{0,\text{Chuck}}
  $$
  $$
  = Y_{\text{John}} - Y_{\text{Chuck}}
  $$
  $$
  = 5 - 1
  $$
  $$
  = 4
  $$


* Is this a good estimate of the treatment effect of insurance for John? How do we know?

We agree this is a bad idea but let's pretended and just try it

---


### Potential Outcomes Framework: Health Insurance

Slide 12
Our estimate was biased upward:  
$$  
\widehat{\tau}_{\text{John}} = 4  
$$  
relative to the true value  (that we pretended into existence)
$$  
\tau_{\text{John}} = 2 .  
$$

- What went wrong?
    
    - What do we know about John?
        
        - He decided to pay for insurance.
            
    - What do we know about Chuck?
        
        - He decided not to get insurance.
            
- Why should this worry us?
    
    - Individuals are, to some extent, optimizing agents and have made an important choice.
        
    - It is possible that Chuck is healthier than John and anticipates less need to go to the doctor.
        
    - If this is the case, their potential outcomes are different:  
        $$  
        Y_{1,\text{John}} \neq Y_{1,\text{Chuck}}  
        $$  
        $$  
        Y_{0,\text{John}} \neq Y_{0,\text{Chuck}} .  
        $$
// They're fundementally different so they shouldnt ave the same outcomes

Here's why it's flawd

---

Slide 13

We want  
$$  
\tau_{\text{John}} = Y_{1,\text{John}} - Y_{0,\text{John}} .  
$$

- If we estimate $$\tau_{\text{John}}$$ by comparing John’s visit count with Chuck’s:  
    $$  
    \widehat{\tau}_{\text{John}} = Y_{\text{John}} - Y_{\text{Chuck}}  
    $$  
    $$  
    = Y_{1,\text{John}} - Y_{0,\text{Chuck}}  
    $$  
    $$  
    = Y_{1,\text{John}} - \left( Y_{0,\text{John}} - Y_{0,\text{John}} \right) - Y_{0,\text{Chuck}}  
    $$

He wants to put a 0 in the middle so he can group terms because you're allowed to just insert math
    $$  
    = \left( Y_{1,\text{John}} - Y_{0,\text{John}} \right) + \left( Y_{0,\text{John}} - Y_{0,\text{Chuck}} \right)  
    $$  



    
    $$  
    = \tau + \left( Y_{0,\text{John}} - Y_{0,\text{Chuck}} \right)  
    $$  
You get tau and whatever the difference is between the two different same treatements of the world 

    $$  
    = \tau + \text{Bias} .  
    $$
    
- Because  
    $$  
    Y_{0,\text{John}} \neq Y_{0,\text{Chuck}}  
    $$  
    meaning that without insurance John is more likely to go to the doctor than Chuck, our estimate is biased.
    
- [[Selection Bias]]: John selected into treatment and is different from Chuck, who did not select into treatment.

Slide 13

--- 

### Potential Outcomes Framework: Job Training
Slide 15

Suppose we want to know the effect of a job training program on Sarah’s weekly earnings.

- This is the difference between two states of the world:
    
    - What Sarah would earn without the training:  
        $$  
        Y_{0,\text{Sarah}}  
        $$  
        (potential outcome in the untreated state)
        
        - $$Y$$ denotes earnings at age 42
            
        - Subscript $$0$$ denotes the untreated state
            
        - Subscript $$\text{Sarah}$$ indicates this is the outcome for Sarah
            
    - What Sarah would earn at age 42 with the training:  
        $$  
        Y_{1,\text{Sarah}}  
        $$  
        (potential outcome in the treated state)
        
        - Subscript $$1$$ denotes the treated state
            
- The causal effect of treatment for Sarah is:  
    $$  
    \tau_{\text{Sarah}} = Y_{1,\text{Sarah}} - Y_{0,\text{Sarah}}  
    $$
    
---
Slide 16
#### Individual Treatment Effect

We want the causal effect of job training on Sarah’s weekly earnings:  
$$  
\tau_{\text{Sarah}} = Y_{1,\text{Sarah}} - Y_{0,\text{Sarah}}  
$$


#### Observed and Counterfactual Outcomes

- We observe Sarah with job training at age 42:  
    $$  
    Y_{1,\text{Sarah}} = 750  
    $$
    
- Pretend we can observe the counterfactual outcome without training:  
    $$  
    Y_{0,\text{Sarah}} = 520  
    $$
    
- The true treatment effect is:  
    $$  
    \tau_{\text{Sarah}} = 750 - 520 = 230  
    $$
    
---
Slide 17
### Potential Outcomes Framework: Job Training

We observe Sarah at age 42 having chosen to participate in the training program.

- We conceptualize outcomes as occurring at a point in time.
    
    - We are interested in the effect of training on a 42-year-old individual.
        
- Because the outcome is measured at a point in time, we only observe one of the potential outcomes:  
    $$  
    Y_{1,\text{Sarah}} \quad \text{or} \quad Y_{0,\text{Sarah}}  
    $$
    
- The potential outcome we do not observe, Sarah without the training at age 42, is referred to as the **counterfactual**.
    
- We cannot directly estimate the treatment effect for Sarah because we only observe one of the two potential outcomes:  
    $$  
    \tau_{\text{Sarah}} = Y_{1,\text{Sarah}} - Y_{0,\text{Sarah}}  
    $$
---
Slide 18

In practice, we do not observe both potential outcomes.
So we know that the training increased Sarah’s weekly earnings by (τSarah = 230).
In practice, we wouldn’t observe both potential outcomes.
Lets try to estimate τSarah.
Suppose Sarah’s neighbor Jen, who is 42, has a history of unemployment
like Jen.

WE can get creative in all the differences that might emerge
• In what ways might Jen differ from Sarah?
---

#### Using Jen as a Counterfactual

- Suppose Sarah’s neighbor Jen, age 42, did not participate in job training.
    
- Jen earns:  
    $$  
    Y_{0,\text{Jen}} = 100  
    $$
    
- Estimate the treatment effect using Jen as the counterfactual:  
    $$  
    \widehat{\tau}_{\text{Sarah}} = Y_{1,\text{Sarah}} - Y_{0,\text{Jen}}  
    $$  
    $$  
    = Y_{\text{Sarah}} - Y_{\text{Jen}}  
    $$  
    $$  
    = 750 - 100  
    $$  
    $$  
    = 650  
    $$
    
We know that we're grossly overstating the effect

---

#### Bias in the Estimate

- The estimated effect is:  
    $$  
    \widehat{\tau}_{\text{Sarah}} = 650  
    $$
    
- The true effect is:  
    $$  
    \tau_{\text{Sarah}} = 230  
    $$
    
- The estimate is biased upward.
    

---

#### Why Is the Estimate Biased?

- What do we know about Sarah?
    
    - She is motivated and chose to participate in job training.
        
- What do we know about Jen?
    
    - She did not participate in job training.
        
- Motivation likely affects earnings even without training.
    
- Therefore, potential outcomes differ:  
    $$  
    Y_{1,\text{Sarah}} \neq Y_{1,\text{Jen}}  
    $$  
    $$  
    Y_{0,\text{Sarah}} \neq Y_{0,\text{Jen}}  
    $$
    

---

#### Decomposing the Bias

If we estimate by comparing Sarah’s earnings to Jen’s:  
$$  
\widehat{\tau}_{\text{Sarah}} = Y_{\text{Sarah}} - Y_{\text{Jen}}  
$$  
$$  
= Y_{1,\text{Sarah}} - Y_{0,\text{Jen}}  
$$  
$$  
= (Y_{1,\text{Sarah}} - Y_{0,\text{Sarah}}) + (Y_{0,\text{Sarah}} - Y_{0,\text{Jen}})  
$$  
$$  
= \tau + \text{Bias}  
$$

Because  
$$  
Y_{0,\text{Sarah}} \neq Y_{0,\text{Jen}},  
$$  
the estimate is biased.

---

#### Selection Bias (Definition)

**Selection Bias**: The bias that results from people selecting into treatment. This results in the people that get the treatment being systematically different from those that do not in ways that affect the outcome. 
- People are making decisions about whether to get treatment or not based on whether or not they think it is beneficial for them.
- People that opt into the treatment are likely to have different potential outcomes than people that did not decide to get the treatment.
- It is not just that they are likely to benefit more, but their outcomes in the absence of treatment are likely to be different also.

Average Treatment Effect: The average treatment effect is the average of the individual treatment effects in a population.

$$  
\tau_{ATE}=\frac{1}{N}\sum_{i=1}^{N}\tau_i  
$$

$$  
=\frac{1}{N}\sum_{i=1}^{N}\left(Y_{1,i}-Y_{0,i}\right)\qquad (5)  
$$

$$  
=\frac{1}{N}\sum_{i=1}^{N}Y_{1,i}-\frac{1}{N}\sum_{i=1}^{N}Y_{0,i}  
$$
The whole lesson is that Y_0 is uncalculable 

RCT is the way around that, we get to see both versions of reality

where $$\tau_i=Y_{1,i}-Y_{0,i}$$ and $i$ denotes individual $i$
Slide 24

Average Treatment Effect: The average treatment effect is the average of the individual treatment effects in a population.

$$  
\tau_{ATE}=\frac{1}{N}\sum_{i=1}^{N}\tau_i  
$$

$$  
=\frac{1}{N}\sum_{i=1}^{N}\left(Y_{1,i}-Y_{0,i}\right)\qquad (5)  
$$

$$  
=\frac{1}{N}\sum_{i=1}^{N}Y_{1,i}-\frac{1}{N}\sum_{i=1}^{N}Y_{0,i}  
$$

where $$\tau_i=Y_{1,i}-Y_{0,i}$$ and $$i$$ denotes individual $$i$$