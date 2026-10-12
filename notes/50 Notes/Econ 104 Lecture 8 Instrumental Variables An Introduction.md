---
type: lecture
parent: "[[Econ 104]]"
domain: econ
status: draft
---
Midterm practice 
- There will be questions on coding
- Can pick up old practice content
- Read our writeups
- General notes 
	- When writing paragraphs refrence specific values and coefficents and specific values and comapre p values
	- So what if it has a p-value
	- Busy is not a valid variable
	- If you have randomization and you have balance in your variables is that the unovserbabls are also balanced
	- So few people said that if you can see randomization in the obersrbables and therefore balance observables
	- If it's a binary variable percentage points if it's ln it's %s 
	- You are not meeting the requirement if you can't write page 2 
	- Lost his shit when not causal
	- did all this work to say not causal
	- If it didn't have balance
	- The estimate doesn't have to be 
	- The good writeups weren't rushed


What we're focusing on is not everyone does what they're told

Not everybody gets the treatment who gets assigned the treatment

We're calling RF Ybar_1bar-ybar_c

Pi_1 + Pi_1 Z + e_i

## Slide 14

IV: Reduced Form  
We usually estimate the reduced form via regression. This allows us to include  
covariates easily.  
The reduced form is RF = YT −Y C.  
Remember Zi  
is the assignment to treatment.  
We have seen that you can estimate the difference in means by estimating  
the regression below:  
Yi = π0 +π1Zi +εi  
πc1 is our reduced form estimate of the effect.  
This is also called the Intention To Treat (ITT) estimate. Why is it called the  
intention to treat rather than the treatment effect?  
Econ 104 Instrumental Variables 14 / 23

## Slide 15

Instrument Variables (IV): First Stage  
Econ 104 Instrumental Variables 15 / 23


## Slide 16
Compare the likelihood of the 


IV: First Stage  
**First Stage: The first stage is the effect of being assigned to the treatment group  on the probability of getting the treatment.**  

So if we have a perfect experimetn, our first stage will be one nobody gets treated in C and everyone in T

Z FS D TOT Y

RF between the two



This is called the first stage because it is the first thing the instrument  
affects.  
First Stage = Avgn[Di  
|Zi = 1]−Avgn[Di  
|Zi = 0], where  

%%First stage Avg likelihood average likelihood of getting treatement - average of getting treatment of be assigned to the cotnrol 
%%


• Zi  
is an indicator for whether person i was assigned to get the  
treatment (we call Zi  
the instrument)  

• Di  
is an indicator for whether person i got the treatment  

Whether or not you got treated is the var of int

Fs_i = phi_0+phi_1 z_i + ephsiolon_i

zi assigned if assigned how much more likely FS

we're interested in phi

We can estimate the first stage with the following regression:  
Di = φ0 +φ1Zi +εi  
φc1 is the difference in proportion that got the treatment (tutoring) between  
the group assigned to treatment and the group assigned to control.  


Phi = 0 is the worst case scenario 

Phi = 1 is the best case scenario 

The lower Phi gets the weirder and wackier the group gets


Econ 104 Instrumental Variables 16 / 23

## Slide 17

IV: First Stage  
In the tutoring example we are discussing, 2/3 of the treatment group got the treat￾ment and none of the control group did.  
First Stage = Avgn[Di  
|Zi = 1]−Avgn[Di  
|Zi = 0] = 2  
3 −0 = 2  
3  
What is this an estimate of?  
• It is the difference between the fraction that got the treatment (tutoring)  
in the treatment group (group assigned to get tutoring) and the fraction  
that got the treatment (tutoring) in the control group (group assigned  
not to get tutoring).  


Suppose that 3/4 of the treatment group and 1/4 of the control group got  
tutoring (i.e., some control students got tutoring on their own). What would  
the First Stage estimate be?  

Suppose a quarter got treatment be

It's just .75-.25=.5




Econ 104 Instrumental Variables 17 / 23

## Slide 18

IV: First Stage  
How would the first stage look as regression results?  
In the case where no controls are treated and 2/3 of treatment group are  
treated:  
Dˆ  
i = 0.000+0.667Zi  

So as control 0 and if 2/3 compliance treatmetn

In the case where 1/4 of controls are treated and 3/4 of treatment group are  
treated:  
Dˆ  
i = 0.250+0.500Zi  


Note that you can test whether the first stage is statistically significant.  
- People who do what they're told are compliers



Econ 104 Instrumental Variables 18 / 23

## Slide 19

Instrument Variables (IV): The IV Estimate  
Econ 104 Instrumental Variables 19 / 23

## Slide 20

IV: The IV Estimate  
Instrumental Variables Estimator gets us an estimate of the treatment on the  treated effect.  
Remember the reduced form got us an estimate of 2/3 τ.  

Where we combine taking the estimate and then we divide by rate of complaince 



• Why is this? Because we have people in the treatment group (1/3)  
who are not treated.  


To get an estimate of the treatment effect τ we need to adjust for the fact  that difference in the fraction treated between the treatment and control  group is 2/3 rather than 1.  

IV = RF/FS

Z ->(FS) D ->(tot(IV)) Y

Path of ausation

To do this we just divide the reduced form estimate by the difference in the  
treatment rates between the treatment and control  
group (First Stage).  
This division puts the reduced form estimate in per-treated person terms.  

This puts it in the per person terms of actually going to tutoring

Econ 104 Instrumental Variables 20 / 23

## Slide 21

# IV: The IV Estimate  
τcIV =  
Reduced Form  
First Stage
$$
Avgn[Yi  
|Zi = 1]−Avgn[Yi  
|Zi = 0]  
Avgn[Di  
|Zi = 1]−Avgn[Di  
|Zi = 0]$$

(2  / 3  )τ  
/
(2 /3)  
= τ



We are putting the reduced form estimate in per-person terms.  
We do this by dividing the Reduced Form estimate by the difference in the  fraction treated between the treatment and control groups.  


If there were perfect compliance (everyone told to get tutoring did and vice  versa), what would the first stage be? What would the reduced form  estimate be?  

Trying to get back to the world of everyone does what they're told

Plenty of cases where we don't get to know the first stage

Take a pill for high blood pressure every two weeks, but people lie

So you end up underestimating the effect

So we try to do heuristics and pop the pill every day



Econ 104 Instrumental Variables 21 / 23

## Slide 22

IV: The IV Estimate


Example: You run an experiment where 100 unemployed people are randomly  assigned to receive IT training and 100 are randomly assigned not to. Only 1/2  of the people assigned to the training actually go. One year after the training, you  measure the average hourly wage for both groups. You find that people who were  assigned to the training earn, on average, 2 dollars more per hour than those not  assigned to the training.  


What is Yi?  
- Hourly wage
What is Zi?  
- Assigned to training
What is Di?  
- Actually got training


Econ 104 Instrumental Variables 22 / 23

## Slide 23

IV: The IV Estimate  
Example: You run an experiment where 100 unemployed people are randomly assigned to receive IT training and 100 are randomly assigned not to. Only 1/2 of the people assigned to the training actually go. One year after the training, you measure the average hourly wage for both groups. You find that people who were assigned to the training earn, on average, 2 dollars more per hour than those not assigned to the training.  
- First stage: What is the first stage estimate?  
	- .5 more likely to 
- First stage: How do we interpret the first stage estimate?  
- Reduced Form: What is the reduced form estimate?  
	- =2
- Reduced Form: Interpret the reduced form estimate?  
	- Being assigned to get the training increases wages by 2 on average
- How much does the training increase the average person’s hourly wage ($\hatτ$)?  
	- 4 dollars

See ToT=RF/FS


Econ 104 Instrumental Variables 23 / 23


Lesson 9

Violations of Chain of Causation

Complier
Defier
Never-Taker
Always-Taker


Motivating eample

# Lesson_9.pdf

## Slide 1

Lesson 9  
Instrumental Variables  
Intuition and Assumptions  
Econ 104 Instrumental Variables 1 / 27

## Slide 2

Today’s Lesson  
1 Reminder: Assignment 2 - Writing  
2 Mastering Metrics - Chapter 3  
3 Instrumental Variables:  
• Chain of Causation  
• Assumptions  
• Local Average Treatment Effect (LATE)  
Econ 104 Instrumental Variables 2 / 27

## Slide 3

Instrumental Variables: Motivating Example  
Econ 104 Instrumental Variables 3 / 27

## Slide 4

IV: Motivating Example  
You are asked to evaluate the effect of a new, fast-acting blood pressure medica￾tion. You start with a sample of 200 people with high blood pressure and assign  
half of them at random to take the pill. Of the 100 assigned to take the pill, 30  
refuse and 70 take it. None of the people in the control group have access to the  
pill. At the end of a week, you check the blood pressure of the group assigned to  
get the pill and it is 142 on average and the blood pressure of the group assigned  
to control is 148 on average.  
1 What are Yi, Zi, and Di in this experiment?  
Y blood presure
Z assigned to pil
D taking the pill

FS: Dt-Dc
.7 70 percentage points

Reduced form Y_i - Y_c = -6
	Here that's 142-148
			Assigned to the pill - Assigned to Control
		IV: RF/FS = -6 / .7 
		= -8.6

2 What is the first stage estimate? Estimate and interpret  
3 What is the reduced form estimate? Estimate and interpret.  
4 What is the IV effect of the drug on blood pressure? Estimate and interpret.  
Econ 104 Instrumental Variables 4 / 27

## Slide 5

IV: Motivating Example  
1 What are Yi  
, Zi  
, and Di  
in this experiment?  
• Yi

- Blood pressure for individual i after the experiment.  
    • Di
    
- Indicates whether individual i was treated (took the pill).  
    • Zi
    
- Indicates individual i was assigned to treatment.  
    2 What is the first stage estimate? Estimate and interpret.  
    First Stage = Avgn[Di  
    |Zi = 1]−Avgn[Di  
    |Zi = 0]  
    =  
    70  
    100 −  
    0  
    100  
    = 0.70  
    • This how much the assignment to treatment group affected whether or  
    not people actually got the treatment (took the pill).  
    • Indicates how much more likely are people in the treatment group to  
    have taken the pill than people in the control group.  
    Econ 104 Instrumental Variables 5 / 27
    

## Slide 6

IV: Motivating Example  
3 What is the reduced form estimate? Estimate and interpret.  
RF = mean Y assigned to treatment− mean Y assigned to control  
= Avgn[Yi  
|Zi = 1]−Avgn[Yi  
|Zi = 0]  
= 142−148  
= −6.0  
• This is the intention to treat (ITT) estimate, or the effect of being  
assigned to get the pill on blood pressure.  
Econ 104 Instrumental Variables 6 / 27

## Slide 7

# IV: Motivating Example  
4 What is the IV effect of the drug on blood pressure? Estimate and interpret.  
τcIV =  
Reduced Form  
First Stage

# Avgn[Yi  
|Zi = 1]−Avgn[Yi  
|Zi = 0]  
Avgn[Di  
|Zi = 1]−Avgn[Di  
|Zi = 0]

−6.0  
0.7  
= −8.6  
• The pill reduces blood pressure by 8.6 points. It is the effect of taking  
the pill on blood pressure for the kind of person that complies with the  
experiment by taking the pill as directed.  

Group called never takers

What if there's partial treatment

There is such a thing and they can calculate based off amount but others 

Econ 104 Instrumental Variables 7 / 27

## Slide 8

Instrumental Variables: Chain of Causation  
Econ 104 Instrumental Variables 8 / 27

## Slide 9

IV: Chain of Causation  
Let us work through what is going on intuitively.  
	We take the sample of patients and split them into two groups at random.  
	Half are assigned to take the pill and half are not. 
		If being assigned to treatment only affects blood pressure through the pill then the difference in blood pressure between the two groups is:  
Difference between groups in blood pressure =  
(Difference between groups in proportion taking pill)

- (Effect of pill on blood pressure)  
    Econ 104 Instrumental Variables 9 / 27
    

## Slide 10

IV: Chain of Causation  
What is the chain of causation?  
Assigning people to the treatment group → Results in more of the people in  
the treatment group taking the pill.  
• This is the first stage.  
• First Stage = Avgn[Di  
|Zi = 1]−Avgn[Di  
|Zi = 0]  
• The effect of Z on D.  
For the people who took the pill → The pill reduces their blood pressure.  
• This is the treatment effect.  
• The effect of D on Y.  
Remember the Reduced Form is the effect of Z on Y  
• Reduced Form = Avgn[Yi  
|Zi = 1]−Avgn[Yi  
|Zi = 0]  
• The effect of Z on Y.  
Econ 104 Instrumental Variables 10 / 27
%%
Reduced form is the direct effect and go straight to the ffect of ebing assigned ot the condition to the result

When we did ass 1 that was a reduced form

2nd assignment is looking at compliars vs non

and it's estimating the treatment on tht e treatment

Both a bad design and estimatign the effect of the assginemnt

Had two different ba dthings abuot it




%%
## Slide 11

IV: Chain of Causation  
So, there are two ways to represent the path from Z to Y:  
Z  
First Stage  
−−−−−−−→ D  
Treatment Effect  
−−−−−−−−−−→ Y  
and  
Z  
Reduced Form  
−−−−−−−−−→ Y  
We can combine them to get:  
Z  
First Stage  
−−−−−−−→ D  
Treatment Effect  
−−−−−−−−−−→ Y = Z  
Reduced Form  
−−−−−−−−−→ Y  
which we can rewrite as  
First Stage ·Treatment Effect = Reduced Form  
which we can then solve to get the treatment effect  
Treatment Effect = Reduced Form  
First Stage  
Econ 104 Instrumental Variables 11 / 27
%%
Assigned to treatment how much more likely to vote

Both Z to Y

If we want the treamtne on the grtreated  effect we subtract by the first stage tog et the effeect

Rewritten First stage multi treatment effect = reduced form


There's no decision bias 

Suppose treatment group and we have a treatment group 

Just assume nobody got treated 

Some got the call and some did not

Telling us is all we have to do the average outcomes between and divide by 

Because we're assuming perfect randomization we're assuming balance

So the kind of people who go to treatment and the kinds that 

When we o this analysis we're only learning about the compliers and can not learn about the never takers

So we're not getting bias but only applies to what those that do what theyre told

Pretend in the control group That there was an equal level of noncompliers bc balanced bc randomization

So we learn nothing about the never takers


%%
## Slide 12

Instrumental Variables: Assumptions  
Econ 104 Instrumental Variables 12 / 27

## Slide 13

IV: Assumptions  
Let us consider what is necessary to estimate the treatment effect using instru￾mental variables.  
Treatment Effect = Reduced Form  
First Stage  
Intuitively, we need an instrument Z that is randomly assigned or is as good as  
randomly assigned.  
To get consistent estimates of the Treatment Effect, we need consistent  
estimates of its two components.  
If the instrument Z is randomly assigned or as good as randomly assigned,  
then the regression Di = φ0 +φ1Zi +εi will get us a consistent first stage  
estimate and Yi = π0 +π1Zi +εi will get us a consistent reduced form  
estimate.  
We can then take the ratio of them to get a consistent estimate of the  
Treatment Effect.  
Econ 104 Instrumental Variables 13 / 27

## Slide 14

IV: Assumptions  
Let us consider the formal assumptions necessary to have a valid instrument:  
Assumption 1 - Inclusion Restriction: The instrument Z affects the treatment  
variable D of interest.  
This is just saying that the first stage is not zero.  
We need this because you can’t divide by zero:  
Treatment Effect = Reduced Form  
First Stage  
If the treatment and control groups have the same fraction treated then there  
is no difference between the two groups so there is nothing to compare.  
This can be tested empirically: Does Z have a significant effect on D in the  
regression: Di = φ0 +φ1Zi +ui  
Econ 104 Instrumental Variables 14 / 27

## Slide 15

IV: Assumptions  
Assumption 2 - Exclusion Restriction: The instrument affects the outcome only  
through the variable of interest.  
This assumption is that Z being 0 or 1 only affects the treatment D.  
Z does not affect anything else that affects the outcome Y.  
In other words, Z is not correlated with any omitted variables in the error  
term: Y = π0 +π1Di +u.  
This assumption is unlikely to be met in many social science settings.  
Z D Y  
NOT  
Z D  
D2  
Y  
Econ 104 Instrumental Variables 15 / 27

## Slide 16

IV: Assumptions  
Back to our example: You are asked to evaluate the effect of a new, fast-acting  
blood pressure medication. You start with a sample of 200 people with high blood  
pressure and assign half of them at random to take the pill. Of the 100 assigned  
to take the pill, 30 refuse and 70 take it. None of the people in the control group  
have access to the pill. At the end of a week, you check the blood pressure of the  
group assigned to get the pill and it is 142 on average and the blood pressure of the  
group assigned to control is 148 on average.  
Intuitively, is the instrument Z “as good as random” in this context?  
We need to assess if this is true based on how Z was created.  
In this case the instrument is actually randomly assigned so we get a  
consistent estimate of the first stage and the reduced form.  
Econ 104 Instrumental Variables 16 / 27

## Slide 17

# IV: Assumptions  
Assumption 1 - Inclusion Restriction: The instrument Z affects the treatment  
variable D of interest.  
This one we can assess by looking at the data. Does Z affect D. In this  
case it did, the people assigned to treatment Zi = 1 are much more likely to  
get the treatment Di = 1.  
First Stage = Avgn[Di  
|Zi = 1]−Avgn[Di  
|Zi = 0]

70  
100 −  
0  
100  
= 0.70  
So, we are not dividing by zero (the instrument affects the treatment).  
We could also estimate the regression of D on Z and test for a statistically  
significant relationship.  
Econ 104 Instrumental Variables 17 / 27

## Slide 18

IV: Assumptions  
Assumption 2 - Exclusion Restriction: The instrument affects the outcome only  
through the variable of interest.  
How can this go wrong?.  
If assigning people to treatment (telling them to take the pill) also resulted in  
some of them doing other things to lower their blood pressure, such as  
exercising.  
Then there are two differences between the people assigned to get the  
treatment and those not assigned to treatment.  
So, the treatment group has a decrease in blood pressure due to the pill and  
a decrease due to exercising.  
This would lead us to overestimate the effectiveness of the pill if we  
implement the IV approach.  
Another way of viewing this is you can’t divide by the first stage if there are  
two of them.  
Econ 104 Instrumental Variables 18 / 27

## Slide 19

IV: Assumptions  
Assumption 2 - Exclusion Restriction: The instrument affects the outcome only  
through the variable of interest.  
Z -Told take the Pill Take the Pill  
Eat Better  
Exercise  
Blood Pressure  
FS  
FS 2  
FS 3  
τ  
τEB  
τEX  
One channel: Treat Effect \ = RF  
FS = FS·τ  
FSc = τ  
Several: Treat Effect \ = RF  
FS =  
FS·τ+FS2·τEB+FS3·τEX  
FSc = τ +  
FS2·τEB+FS3·τEX  
FSc = τ +bias  
Econ 104 Instrumental Variables 19 / 27

## Slide 20

Instrumental Variables: Local Average Treatment Effect  
Econ 104 Instrumental Variables 20 / 27

## Slide 21

IV: LATE  
Average Treatment Effect (ATE): The average treatment effect across everyone  
in some population of interest. This can be found if you have a sample that is rep￾resentative of the population of interest, you randomly assign people to treatment,  
and everyone complies with their treatment assignment.  
Instrumental Variables gets us something slightly different, even if our  
sample is correctly drawn from the population of interest.  
• The people that comply with their assignment might be different than  
the rest of the population.  
• IV estimates the average treatment effect for the people that complied  
with the assignment.  
• This is called the Local Average Treatment Effect (LATE) and it  
might be quite different than the ATE.  
How might the people in the treatment group that took the pill as assigned  
be different from those who did not?  
Econ 104 Instrumental Variables 21 / 27

## Slide 22

IV: LATE  
With binary assignment to treatment (Z) and binary treatment (D) we can split  
people into 4 groups:  
Compliers: They do what the experimenter (or instrument Z) tells them.  
• If told to take the pill Zi = 1 they take it: Di = 1  
• If told not to take the pill Zi = 0 they don’t take it: Di = 0  
Never takers: They never take the treatment  
• If told to take the pill Zi = 1 they don’t take it: Di = 0  
• If told not to take the pill Zi = 0 they don’t take it: Di = 0  
Always takers: They always take the treatment regardless of Z.  
• If told to take the pill Zi = 1 they take it: Di = 1  
• If told not to take the pill Zi = 0 they take it: Di = 1  
Defiers: Do the opposite of what they are told.  
• If told to take the pill Zi = 1 they don’t take it: Di = 0  
• If told not to take the pill Zi = 0 they take it: Di = 1  
Econ 104 Instrumental Variables 22 / 27

## Slide 23

IV: LATE  
We can write the groups out as a matrix:  
Assigned to Treatment (Zi = 1) Assigned to no Treat (Zi = 0) Proportion  
Always Taker Take Treatment (Di = 1) Take Treatment (Di = 1) PAT  
Never Taker Don’t Take Treatment (Di = 0) Don’t Take Treatment (Di = 0) PNT  
Complier Take Treatment (Di = 1) Don’t Take Treatment (Di = 0) PC  
Defier Don’t Take Treatment (Di = 0) Take Treatment (Di = 1) PD  
One of the assumptions necessary for instrumental variables is that there  
are no defiers.  
This is a reasonable assumption as defiers are engaging in very perverse  
behavior.  
• It is not that defiers are ignoring the directions.  
• They are listening to what people want them to do and then doing the  
opposite.  
Which two groups are affected by their assignment?  
Econ 104 Instrumental Variables 23 / 27

## Slide 24

IV: LATE  
When comparing treatment and control group outcomes, we are comparing the  
following:  
Assigned to treat (Zi = 1) Assigned to no Treat (Zi = 0) Proportion  
Always Taker E[Y1i  
|Zi = 1,AT] E[Y1i  
|Zi = 0,AT] PAT  
Never Taker E[Y0i  
|Zi = 1,NT] E[Y0i  
|Zi = 0,NT] PNT  
Complier E[Y1i  
|Zi = 1,C] E[Y0i  
|Zi = 0,C] PC  
Defiers E[Y0i  
|Zi = 1,D] E[Y1i  
|Zi = 0,D] PD  
We observe the treated outcome for always takers in both the treatment and  
control group.  
We observe the untreated outcome for never takers in both the treatment  
and control group.  
Why can’t we credibly estimate the effect of the treatment on Always Takers  
or Never Takers?  
Econ 104 Instrumental Variables 24 / 27

## Slide 25

IV: LATE  
RF =(Average outcome for Treatment Group)−(Average Outcome for Control Group)  
E[RF] =E[Yi  
|Zi = 1]−E[Yi  
|Zi = 0]  
=(PATE[Yi  
|Zi = 1,AT] + PNTE[Yi  
|Zi = 1,NT] + PCE[Yi  
|Zi = 1,C] + PDE[Yi  
|Zi = 1,D])  
−(PATE[Yi  
|Zi = 0,AT] + PNTE[Yi  
|Zi = 0,NT] + PCE[Yi  
|Zi = 0,C] + PDE[Yi  
|Zi = 0,D])  
=(PATE[Y1i  
|AT] + PNTE[Y0i  
|NT] + PCE[Y1i  
|C] + PDE[Y0i  
|D])  
−(PATE[Y1i  
|AT] + PNTE[Y0i  
|NT] + PCE[Y0i  
|C] + PDE[Y1i  
|D])  
=PCE[Y1i  
|C] + PDE[Y0i  
|D]−PCE[Y0i  
|C]−PDE[Y1i  
|D]  
=PCE[Y1i  
|C]−PCE[Y0i  
|C]  
=PC(E[Y1i  
|C]−E[Y0i  
|C])  
=PCE[Y1i −Y0i  
|C]  
=PCE[τi  
|C]  
The reduced form is the fraction of the population that are compliers times  
the average treatment effect for compliers.  
Econ 104 Instrumental Variables 25 / 27

## Slide 26

# IV: LATE  
What is the Instrumental Variables Estimating?  
τIV =  
Reduced Form  
FirstStage

PCE[τi  
|C]  
PC  
= E[τi  
|C]  
The instrumental variables estimator is getting us the average treatment  
effect for the type of person that complies with the assignment.  
This is called the Local Average Treatment Effect to distinguish it from the  
Average Treatment Effect.  
Econ 104 Instrumental Variables 26 / 27

## Slide 27

IV: LATE  
Consider the experiment on blood pressure medication:  
Are there any Always Takers?  
Who are the Never Takers?  
Can we estimate the treatment effect for the Never Takers? Why not?  
Do you think the Never Takers will have a larger or smaller treatment effect  
than the Compliers? Why?  
Econ 104 Instrumental Variables 27 / 27