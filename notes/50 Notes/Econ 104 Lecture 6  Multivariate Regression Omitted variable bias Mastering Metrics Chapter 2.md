---
type: lecture
parent: "[[Econ 104]]"
domain: econ
status: draft
---
RCT
1. Question, IRB Approval
2. Recruit a sample
3. Baseline data
4. Randomize into Treatment, Control
5. Balance check
6. Treat them
7. Endline data
8. Analysis/Regressions

Reject the paradigm of doing a shitty job where they rush and you're supposed to rush

People don't have reasonable expectations with others



RCT
Concluding remarks RCT
There's a random sample is representative of a population
- One of these gets you an unbiased average
RCT 
- Gives you a causal effect
No treatment in a sample

Last paragraph @ s5

What is good about these four variables that makes them good variables for a balance table

**What makes Age a good variable to look at for balance**
- It's relevant (they have to be 18)
- Everyone has an age
- We don't variables that vary
- We want to find things that are related to the actual variables
They're baseline variables

You don't want something that is a function of the treatment

Fixed characteristics
- Ethnicity
- Baseline
- Those outcomes occurred before the experiment so you can see the propensity of voting
- You never want to look at something before or after

They give you a sense of balance before the experiment

This is absolutely crucial

Things that are not are not a function of the regression
P =.61

The p value looks essentially identical

The table does exhibit balance 

## Slide 1

Lesson 6  
Selection on Observables  
Econ 104  
Selection on Observables  
1 / 24

## Slide 2

Today’s Lesson  
1  
Reminders  
2  
Concluding Remarks on RCTs  
3  
Selection on Observables  
• Omitted variable bias  
• Private college example  
Econ 104  
Selection on Observables  
2 / 24

## Slide 3

Reminder  
Assignments  
Read Mastering Metrics Chapter 2  
Econ 104  
Selection on Observables  
3 / 24

## Slide 4

Concluding Remarks: RCTs  
Econ 104  
Selection on Observables  
4 / 24

## Slide 5

Concluding Remarks: RCTs  
It is important not to confuse a Random Sample and a Randomized Control Trial  
A random sample is representative of a population. It can be used to get an  
unbiased measure of some population characteristic (e.g., average income).  
A random sample is not a method of estimating the causal effect of a  
treatment D on an outcome Y.  
A randomized control trial (or experiment) is a method of estimating a the  
causal effect of a treatment on an outcome.  
A randomized control trial may be conducted on a sample that is not  
representative of the population. This is fine. It will estimate the causal  
effect of the treatment for that sample (e.g., the effect of blood pressure  
medication on people with high blood pressure).  
Econ 104  
Selection on Observables  
5 / 24

## Slide 6

Concluding Remarks: RCTs  
Interpreting balance in an RCT depends on both the magnitude and statistical  
significance of differences between a treatment and control group. Example 1:

|Variable|Control|Treat|Difference|P-Value|
|---|--:|--:|--:|--:|
|Age|55.738|55.652|-0.085|0.61|
|Female|0.561|0.559|-0.002|0.59|
|Voted in 2000|0.734|0.734|0.000|0.94|
|Voted in 1998|0.572|0.578|0.006|0.18|
We choose these variables because they are baseline variables

They occured before the 

Does the table exhibit balance in terms of the magnitudes of the variables?  
- Yes
Does the table exhibit balance in terms of statistical significance?  
- Yes 



Econ 104  
Selection on Observables  
6 / 24

## Slide 7

Concluding Remarks: RCTs  
Interpreting balance in an RCT depends on both the magnitude and statistical  
significance of differences between a treatment and control group. Example 2:

|Variable|Control|Treat|Difference|P-Value|
|---|--:|--:|--:|--:|
|Age|55.902|55.514|-0.388|0.02|
|Female|0.562|0.555|-0.007|0.11|
|Voted in 2000|0.734|0.729|-0.005|0.16|
|Voted in 1998|0.573|0.571|-0.001|0.77|

Does the table exhibit balance in terms of the magnitudes of the variables?  
- Yes, they look similar. 
Does the table exhibit balance in terms of statistical significance?  
- Do any of the P values concern
- Voted in 1998 is much more stat sig than the others
- The low p value of Age is concern
- 1/4 is concerning

Now try adding these variables???
Make a table
Called Voted in 2002
1 2 3 . . .

Treat (real) if you were assigned to the treatment group
- When you run that regression you get something near 0.014 + STDV
- That tells me that being Treated increases your chance of voting 0.014 per points
How much does that value change
IF we add age as an additional variable
We get a new coefficent for age  and a stdv and a new coefficent for voting with age and had very little on the estimate

It did not change because Age is not correlated with the treatment

Now we run another control var and the hope is that the coeffient stays pretty stable and 

And that's table 3 

If you add them into the table and they don't change that shows your results are 'robust'

That is what's meant by adding them all up 





Econ 104  
Selection on Observables  
7 / 24

## Slide 8

Concluding Remarks: RCTs  
Interpreting balance in an RCT depends on both the magnitude and statistical  
significance of differences between a treatment and control group. Example 3:

|Variable|Control|Treat|Difference|P-Value|
|---|--:|--:|--:|--:|
|Age|55.902|52.341|3.561|0.00|
|Female|0.562|0.555|-0.007|0.11|
|Voted in 2000|0.734|0.672|0.062|0.00|
|Voted in 1998|0.573|0.561|0.012|0.09|

This would fail the I walk into the control and treat room can I tell what they're sorted on?

Age 55 and 52 looks different etc.

We have terrible p value balances because they're stat significant

There's a huge differnece 

Does the table exhibit balance in terms of the magnitudes of the variables?  
Does the table exhibit balance in terms of statistical significance?  
Econ 104  
Selection on Observables  
8 / 24

## Slide 9

Concluding Remarks: RCTs  
Attrition - in an experiment is the loss of participants before the endline outcome  
is measured.  

%%Think of this as people leaving or dying%%



Problematic if the rate of attrition is different for the treatment and control  
group (undoes balance).  
%% You no longer have the same groups%%
• How to test: examine if attrition rate is similar for the two groups.  
Problematic if the type of people who attrit from treatment group are  
different than those who attrit from the control group (undoes balance).  

%% It's a problem if you lose different types of people between the groups  %%

%%Imagine you lose the best performers to leaving to New York and then the control old folks die. %%

%%In the voting study you'd only be worried if the treatment influenced state departure. It seems unlikely to lose to attrition therefore%%

.
	How to test: examine if those who attrit are similar using baseline  
	characteristics.  
	
Primary solution is to minimize attrition (e.g., follow up surveys). Use  
administrative data that tracks everyone.  
Attrition is not an issue in the voting outreach experiment because voting is  
observed using administrative voting records.  
Econ 104  
Selection on Observables  
9 / 24

## Slide 10

Concluding Remarks: RCTs  
Noncompliance - in an experiment is the failure of people in the treatment and  
control group to do what was assigned by the randomization.  
%%
This one happens all the time.

People don't do what they're told.

e.g. They take blood pressure medication home but they don't take it.

Some of the control folks will go to another doctor and then get treatment




%%

People in the treatment group may not take the treatment (e.g., may not take  
the medicine).  
People in the control group may take the treatment (e.g., may take the  
medicine anyway).  

This does NOT invalidate the experiment. It means that we will need to  
adjust the causal estimates (will address in MM Chapter 3).  

%%

Bizarrely we'll come to find out that's okay and we can account for that



Imagine you have 60% or 10% compliance in either group you can deal with different compliances

But if you deal with the same level of noncompliance, you just adjust your causal estimates

The law of different compliances depends on the size of the experiment

You might lose stat sig from this

As your group gets smaller and smaller you get a more and more bizarre picture

So we might just end up only learning about the folks that do



%%

Do you think noncompliance occurs for the treatment group in the voting  
experiment?  
%%
Not picking up the phone

Do we think noncompliance occurs for the treatment group in the voting
%%

Do you think noncompliance occurs for the control group in the voting  
experiment?  

%%Somebody was not assigned to get the phone call and got it somehow%%

%%


Nobody is seeking out a phone call



%%

Econ 104  
Selection on Observables  
10 / 24

## Slide 11

Selection on Observables: Omitted Variable Bias  
Econ 104  
Selection on Observables  
11 / 24

## Slide 12

Selection on Observables: Omitted Variable Bias  
%%Bullman's favorite thing keeps him employed %%

%%

Omitted variable College in job training program [[Simple Linear Regression Model]] 

It's correlated with the outcome and the manipulated variable

It's if it's not correlated with both not just one to create bias

%%
Omitted Variable Bias: Occurs when an important causal factor is omitted from a  
regression, resulting in the effect of the other factor being over or underestimated.  
It is what happens when you have selection bias in a regression.  

An omitted variable creates bias if:  


1  it is correlated with the outcome variable  

2  it is correlated with an explanatory variable  

Why are important variables omitted:  

1  they are not available in the data  


2  the researcher does not think of them  


Econ 104  
Selection on Observables  
12 / 24

## Slide 13

Selection on Observables: Omitted Variable Bias 

Example: Suppose you wish to estimate the effect of going to college on hourly  
wages at age 30.  

The regression you are able to estimate is:  
$$wage_i=14.00+10.00college_i$$  
The regression you would like to estimate is:  
$$wage_i=12.20+7.00college_i+6.00motivated_i$$

The regressor changes because we're now including it

By not including motivated we were biased by 3 dollars

Why did this bias occur




What is the magnitude of the omitted variable bias on the coefficient for  
college in the first regression? 

Why did this bias occur?  

Econ 104  
Selection on Observables  
13 / 24

## Slide 14

Selection on Observables: Omitted Variable Bias  
Omitted Variable Bias theory:  
True equation:  
$$Y=\beta_0+\beta_1X_1+\beta_2X_2+u$$  
The equation we estimate:  
The underscores are incorrect. Use hats for estimated coefficients:

Y=β^0+β^1X1+uY=\hat{\beta}_0+\hat{\beta}_1 X_1+uY=β^​0​+β^​1​X1​+u

If you want the population (true) model instead:

Y=β0+β1X1+uY=\beta_0+\beta_1 X_1+uY=β0​+β1​X1​+u

He runs Y just on X1

he thinks it will nto be realtted to the real Beta 1


And suppose we estimate the relationship between $X_2$ and $X_1$:  
$$X_2=\delta_0+\delta_1X_1+\eta$$  
Pretend we know the relationship perfectly between X1 and X2 and we get the coefficent delta 1



Econ 104  
Selection on Observables  
14 / 24

## Slide 15

Selection on Observables: Omitted Variable Bias  
Let us start with the equation we would like to estimate.  
$$Y=\beta_0+\beta_1X_1+\beta_2X_2+\varepsilon$$  
$$Y=\beta_0+\beta_1X_1+[\beta_2X_2+\varepsilon]$$  
$$Y=\beta_0+\beta_1X_1+[\beta_2(\delta_0+\delta_1X_1+\eta)+\varepsilon]$$

So we're plugging in this equation for the omitted variable it's relationship with the included variable


$$Y=\beta_0+\beta_1X_1+\beta_2\delta_0+\beta_2\delta_1X_1+\beta_2\eta+\varepsilon$$  
If you parse this out you end up with 

$$Y=(\beta_0+\beta_2\delta_0)+(\beta_1+\beta_2\delta_1)X_1+(\beta_2\eta+\varepsilon)$$  
So, instead of estimating $\beta_1$, we estimate: $\beta_1^{*}=\beta_1+\beta_2\delta_1$  

This bias term is beta 1 + beta 2\*delta 1 

WE NEED TO KNOW

We can not run the regression on anything and get the real answer


This bias term 
Econ 104  
Selection on Observables  
15 / 24

## Slide 16

Selection on Observables: Omitted Variable Bias  
Instead of estimating $\beta_1$, we estimate: $\beta_1^{*}=\beta_1+\beta_2\delta_1$

$$Bias=\beta_2\delta_1$$

||$\mathrm{Corr}(x_1,x_2)>0$|$\mathrm{Corr}(x_1,x_2)<0$|
|---|---|---|
|$\beta_2>0$|Positive bias|Negative bias|
|$\beta_2<0$|Negative bias|Positive bias|


Stole this from woolridge

Downward bias

Econ 104  
Selection on Observables  
16 / 24

## Slide 17

Selection on Observables: Omitted Variable Bias  
The regression you are able to estimate is:  
$$wage_i=14.00+10.00college_i$$  
The regression you would like to estimate is:  
$$wage_i=12.20+7.00college_i+6.00motivated_i$$  6 here is beta 2 
The relationship between the omitted variable and the X variable we have:  
$$motivated_i=0.30+0.50college_i$$  .5 is delta 1

You multiply 6 by .5 and you get 3 the bias that we uncovered by including motivateed
Let’s examine how the bias formula works in practice:  
$$\beta_1^{_}=\beta_1+\beta_2\delta_1=7.00+6.00_0.5=7.00+3.00=10.00$$  

We randomize 

HE will include an exam question from Ch1 and 2 of mastering metrics



Econ 104  
Selection on Observables  
17 / 24

## Slide 18

Selection on Observables: Omitted Variable Bias  
Suppose you want to estimate the effect of attending tutoring on GPA:  
$$GPA_i=2.90+0.20tutoring_i$$  


How will omitting “work ethic” bias the coefficent?  
- Positive times a positive 

- So we're upwards biasing it because people who go to tutoring tend to be hard working
How will omitting “ability” bias the coefficient?  
- Negatively correlated
- Someone who knows a lot of math already and going to tutoring
- Delta 1 is less than 0
- Math ability and GPA
Will adding these variables to the regression reduce bias?  
- 
Will adding these variables to the regression eliminate bias?  
- 



Econ 104  
Selection on Observables  
18 / 24

## Slide 19

Selection on Observables: Example  
Econ 104  
Selection on Observables  
19 / 24

## Slide 20

Selection on Observables: Example  
Mastering Metrics:  
What is the effect of attending a private university rather than a public  
university on future earnings?  
$$\ln(earn_i)=\beta_0+\beta_1private_i+u_i$$  
What are some omitted variables that could cause bias in $\beta_1$?  
Do you expect $\beta_1$ to be biased upward or downward?  
Econ 104  
Selection on Observables  
20 / 24

## Slide 21

Selection on Observables: Example  
Famous paper: Dale and Krueger (2002): “Estimating the Payoff to Attending a  
More Selective College: An Application of Selection on Observables and Unob-  
servables”  
First add observables: students’ SAT scores, parent income, gender, race,  
HS class rank.  
Can add these sequentially (one at a time) in order to see effect on  
coefficient on Private College.  
Idea: Control for selectivity of application set: average SAT score at colleges  
applied to.  
Idea: This may control for some otherwise unobservable characteristics of  
the student (e.g., how motivated they are, unobserved ability, parental  
influence, etc.).  
Econ 104  
Selection on Observables  
21 / 24

## Slide 22

Selection on Observables: Example

Private school effects: Average SAT score controls

||No selection controls|||Selection controls|||
|---|--:|--:|--:|--:|--:|--:|
||(1)|(2)|(3)|(4)|(5)|(6)|
|Private school|.212|.152|.139|.034|.031|.037|
||(.060)|(.057)|(.043)|(.062)|(.062)|(.039)|
|Own SAT score + 100||.051|.024||.036|.009|
|||(.008)|(.006)||(.006)|(.006)|
|Log parental income|||.181|||.159|
||||(.026)|||(.025)|
|Female|||-.398|||-.396|
||||(.012)|||(.014)|
|Black|||-.003|||-.037|
||||(.031)|||(.035)|
|Hispanic|||.027|||.001|
||||(.052)|||(.054)|
|Asian|||.189|||.155|
||||(.035)|||(.037)|
|High school top 10%|||.067|||.064|
||||(.020)|||(.020)|
|Average SAT score of schools applied to ÷ 100||||.110|-.082|.077|
|||||(.024)|(.022)|(.012)|

Econ 104  
Selection on Observables  
22 / 24

## Slide 23

Selection on Observables: Example  
Consider how adding controls affected the coefficient on ”Private”:  
What is the baseline estimated effect of attending a private college?  
How much bias was eliminated by adding student SAT score?  
How much bias was eliminated by adding other student traits?  
How much bias was eliminated by adding application set controls?  
Econ 104  
Selection on Observables  
23 / 24

## Slide 24

Selection on Observables: Example  
Big takeaways about selection on observables designs and omitted variable bias:  
Can reduce bias by adding relevant controls  
Cannot eliminate bias unless include all omitted variables  
Cannot eliminate bias unless have good measure of all omitted variables  
Need other approaches (like RCT) to estimate unbiased causal effects  
Econ 104  
Selection on Observables  
24 / 24
