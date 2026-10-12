---
type: lecture
parent: "[[Econ 104]]"
domain: econ
status: draft
---
Experimental versus Non-Experimental Evidence

1. Can we get an estimate of the causal effect of getting a call encouraging you to vote on your probability of voting with an experiment? (Assignment 1)
2. Can we get an estimate of the causal effect of getting a call encouraging you to vote on your probability of voting with a non-experiment (multivariate regression with controls)? (Assignment 2)
\[These are explorations of whether or not experimental and non-experimental research designs can be used to generate credible causal estimates. We are com-
paring and contrasting experimental estimates and non-experimental regression
adjustment estimates. The context has to do with voting, but our goal is to learn
about empirical designs, not voting.]

Slide 15 Contact is our outcome variable

Baseline is 51% voted

WE know because the previous slide w/ RCT we got basically 0 from treatment

W/O Random 

The experiment can we drive this estimate down to 0 by adding control variables

Add age and it becomes super predictive of voting

This drops the effect of contact from 5 to 4 in %P

When we add the estimate didn't change

We added 4 control variables and the effect of contact plummmets

So we can add control dummy vars and drive the unrandom assigned into something closer to the real true causal effect

Sometimes control variables are grouped into one sum variable instead of doing them one at a time

All we have to do for assignment two is demonstrate the story of the data

So when you hear a data ask 

Public health researchers are the worst they find a correlation instead of controling other variables

Instrumental variables

Econometrics review
	• Regressions
	• Hypothesis testing
Causal inference
	• Potential outcomes framework
	• Selection bias
Randomized controlled trial
	• Gold standard
	• Balance
	• Regression analysis
Regression adjustment (selection on observables)
	• Omitted variable bias
	• Regression analysis
Comparing experimental (RCT) and non-experimental (regression adjustment) designs.

We find that when we did not have groups that were created by random assignment we were not able to overcome the omitted variables problem using regression.

Adjusting for the observable differences using regression gets us closer to an unbiased estimate, but does not get us all the way there.

This does not mean that experiments are the only way to get causal
estimates.
	• We are going to spend the rest of the course studying techniques that,
	in the proper setting, let us recover causal estimates.
	• These include instrumental variables, regression discontinuity, and
	difference in differences.
	• Today we are going to study instrumental variables

Instrumental Variables - Motivating Example: Some students struggline in Econ 113 as they have forgotten some of their basic statistics. We want to determine if an intensive five-hour tutoring session in basic statiistics in the first week of Econ 113 is helpful

- What outcome are we interested in for these students?
	- How they did
- What are the two potential outcomes?
	- Always gonna define our potential outcomes with y_0 ~ w/o tutoring or y_1 outcome w/ tutoring
- How would we ideally estimate the causal effect of tutoring?
	- DO AN RCT
- If we let people choose to get tutoring or not, will the two groups have similar expected outcomes?
	- Selection Bias they won't look the same

Assume half of the people went and half of the people didn't

Not trying to compare the whole treatment group 

trying to compare the effect of tutoring and let's assume half of the folks in the treatment group 

If half of the treatment shows up and there's a difference of 2 

So the effect of half the group means the treatment must've received 4

IRL there's a difference with compliers so that's a bias WE (the class) don't know how to account for

How do we implement our study 

How do we implement our study?
Apply for approval from the Institutional Review Board (IRB). Why do we
have to get approval from the human subjects committee?
On the first day of Econ 113 we ask for volunteers to participate in a tutoring
experiment. 180 students volunteer to participate.
We assign (at random) 90 students to get the 5 hours of tutoring and 90 to
not get the tutoring (does not need to be an even split).
The randomization will result in the two groups having (on average) the
same potential outcomes: Y0 and Y1 same for treat and control.
Hopefully generate unbiased estimate of assigning people to treatment

How do we implement our study?

- Apply for approval from the Institutional Review Board (IRB), also called the Human Subjects Committee.
    

Why do we have to get approval from the human subjects committee?

- Because the study involves human participants. The IRB reviews the plan to ensure:
    
    - risks to participants are minimized,
        
    - informed consent is obtained,
        
    - participation is voluntary and can be ended at any time,
        
    - privacy and confidentiality are protected,
        
    - benefits justify any risks,
        
    - participants are treated fairly (no undue coercion or unfair selection).
        

Study implementation plan

1. Recruitment
    
    - On the first day of Econ 113, ask for volunteers to participate in a tutoring experiment.
        
    - 180 students volunteer.
        
2. Random assignment
    
    - Randomly assign students to groups:
        
        - Treatment group: 90 students receive 5 hours of tutoring.
            
        - Control group: 90 students do not receive tutoring.
            
    - The split does not have to be exactly even, but random assignment is required.
        
3. What randomization accomplishes
    
    - Randomization makes the treatment and control groups comparable on average.
        
    - In expectation, both groups have the same distribution of potential outcomes:
        
        - average (Y_0) is the same in treatment and control,
            
        - average (Y_1) is the same in treatment and control.
            
4. Estimation goal
    
    - We want an unbiased estimate of the causal effect of being assigned to tutoring (the intention-to-treat effect).
        

Unbiasedness (filled in)

Let (Y^T) be the observed outcome mean for those assigned to treatment, and (Y^C) for those assigned to control. The difference-in-means estimator is:

$$  
\hat{\tau} = \bar{Y}^{T} - \bar{Y}^{C}  
$$

Under random assignment,

$$
\mathbb{E}[\hat{\tau}] = \mathbb{E}[\bar{Y}^{T} - \bar{Y}^{C}] = \mathbb{E}[Y_1 - Y_0]  
$$

So the expected difference in average outcomes between treatment and control equals the average treatment effect.

[[External Validity|External Validity WIP]]
-> who did I start with
[[Internal validity]]
-> Good RCT

If we're doing this experiment and we ask for volunteers for tutoring

We can't learn about folks who never signed up for tutoring 

It may not be externally valid


Often compliance rates drop so low you can't even continue the study
What could go wrong with the experiment?

- Noncompliance: some students assigned to tutoring do not attend.
- Crossovers: students assigned to control obtain tutoring elsewhere.
- Attrition: some students drop out or are missing outcome data.
- Spillovers: treated students share help or materials with control students.
- Behavioral responses: assignment affects effort or motivation.
- Measurement problems: grades may be noisy or inconsistently measured.
- Implementation issues: tutoring quality or hours vary across students.

Why might some people assigned to treatment not go to tutoring?

- Scheduling conflicts with work or other classes.
- Low motivation or low perceived benefit.
- Forgetting or poor follow-through.
- Discomfort or stigma.
- Logistical barriers such as time or location.

Suppose 30 of the 90 people assigned to treatment do not go.

We estimate the treatment effect as:
τ̂ = Ȳ^T − Ȳ^C

Will τ̂ overestimate or underestimate the effect of tutoring?

- It will underestimate the effect of actually going to tutoring (assuming tutoring improves grades).

What could go wrong with the experiment?

- Noncompliance: some students assigned to tutoring do not attend.
- Crossovers: students assigned to control obtain tutoring elsewhere.
- Attrition: some students drop out or are missing outcome data.
- Spillovers: treated students share help or materials with control students.
- Behavioral responses: assignment affects effort or motivation.
- Measurement problems: grades may be noisy or inconsistently measured.
- Implementation issues: tutoring quality or hours vary across students.

Why might some people assigned to treatment not go to tutoring?

- Scheduling conflicts with work or other classes.
- Low motivation or low perceived benefit.
- Forgetting or poor follow-through.
- Discomfort or stigma.
- Logistical barriers such as time or location.

Suppose 30 of the 90 people assigned to treatment do not go.

We estimate the treatment effect as:
$$
\hat{\tau} = \bar Y^T - \bar Y^C
$$

Will $$\hat{\tau}$$ overestimate or underestimate the effect of tutoring?

- It will underestimate the effect of actually going to tutoring (assuming tutoring improves grades).

Why?

- $$\bar Y^T$$ is the mean outcome of a group that is $$\tfrac{2}{3}$$ treated and $$\tfrac{1}{3}$$ untreated.
- Because tutoring helps, the untreated students in the treatment-assigned group pull $$\bar Y^T$$ downward.
- $$\bar Y^C$$ is the mean outcome of a group that is entirely untreated.
- As a result, $$\bar Y^T - \bar Y^C$$ is smaller than the true effect of tutoring attendance.


IN IRL Economics you use this terminiology not textbook slop

Intuition of Instrumental Variables: Binary Treatment

People do not always comply with the treatment.
As a result, the simple difference in outcomes identifies the Intention To Treat (ITT),
not the causal effect of actually receiving treatment.

We analyze instrumental variables in three stages:

1. Reduced form  
   - Compare outcomes for those assigned to treatment and control,
     ignoring whether they actually complied.
   - This estimates the ITT:
     $$
     ITT = E[Y \mid Z=1] - E[Y \mid Z=0]
     $$
     where $Z$ is assignment to treatment.

2. First stage  
   - Estimate how assignment affects actual treatment take-up.
   - This measures compliance:
     $$
     FS = E[D \mid Z=1] - E[D \mid Z=0]
     $$
     where $D$ is whether the individual actually received treatment.

3. IV estimate  
   - Scale the reduced form by the first stage:
     $$
     IV = \frac{ITT}{FS}
     $$

Interpretation:

- The IV estimator recovers the Treatment on the Treated (TOT) effect,
  also called the Local Average Treatment Effect (LATE).
- This is the causal effect of treatment for compliers,
  the people whose treatment status is changed by the assignment.

Instrumental Variables can help us estimate how much actually going to tutoring
raises a student’s grade.

The idea is to convert the difference in average grades between those assigned
to treatment and those assigned to control into a per-person treatment effect.

This is done by dividing the difference in outcomes by the difference in the
treatment rates between the two assignment groups.

Formally:
$$
IV = \frac{\bar Y^T - \bar Y^C}{E[D \mid Z=1] - E[D \mid Z=0]}
$$

where:
- $Z$ is assignment to tutoring,
- $D$ is actual tutoring attendance.

Question:
What do we divide $\bar Y^T - \bar Y^C$ by if everyone assigned to treatment
gets tutoring and everyone assigned to control does not?

Answer:

- In this case,
$$
E[D \mid Z=1] = 1 \quad \text{and} \quad E[D \mid Z=0] = 0
$$

- So the denominator is:
$$
E[D \mid Z=1] - E[D \mid Z=0] = 1
$$

Therefore:
$$
IV = \bar Y^T - \bar Y^C
$$

Intuition:

- With full compliance, assignment perfectly determines treatment.
- There is no dilution from noncompliance.
- The IV estimate equals the simple difference in means,
  which directly identifies the treatment effect.

Reduced Form

The reduced form is the difference in outcomes Y between the group assigned
to treatment and the group assigned to not get the treatment.

We use the variable $Z_i$ to denote whether individual $i$ was assigned to the
treatment or control group.

- $Z_i = 1$ if individual $i$ was assigned to the treatment group
- $Z_i = 0$ if individual $i$ was assigned to the control group

This is different from $D_i$, which indicates whether individual $i$ actually
received the treatment.

- $D_i = 1$ if individual $i$ got the treatment
- $D_i = 0$ if individual $i$ did not get the treatment



To keep it simple, suppose all students have the same response to treatment
(a constant treatment effect) $\tau$, so:

$$
Y_{1i} = Y_{0i} + \tau
$$

That is, the treated potential outcome $Y_{1i}$ equals the untreated potential
outcome $Y_{0i}$ plus the treatment effect $\tau$.
We assume that everyone has the same tau even though that's not realistic



We're comparing the outcome of the treatment for the control group

IF 2/3 got the treatment 

The treated group has compliers and 2/3 of the people got the treatment and 2/3 got the treatment

Assuming that all the people didn't get treatment 

For the treated folks it's the treated outcome + tau

2/3 tau

All this was to say it was half the effect

If only 2/3 of the treatment group actually received the treatment (tutoring),
the Reduced Form estimate is:

$$
\text{Reduced Form}
= \text{Avg}_n[ Y_i \mid Z_i = 1 ] - \text{Avg}_n[ Y_i \mid Z_i = 0 ]
$$

We can decompose the treated group into those who complied and those who did not:

$$
= \tfrac{2}{3}\,\text{Avg}_n[ Y_{1i} \mid D_i = 1, Z_i = 1 ]
+ \tfrac{1}{3}\,\text{Avg}_n[ Y_{0i} \mid D_i = 0, Z_i = 1 ]
- \text{Avg}_n[ Y_{0i} \mid D_i = 0, Z_i = 0 ]
$$

Using the constant treatment effect assumption $Y_{1i} = Y_{0i} + \tau$:

$$
= \tfrac{2}{3}\,\text{Avg}_n[ Y_{0i} + \tau \mid D_i = 1, Z_i = 1 ]
+ \tfrac{1}{3}\,\text{Avg}_n[ Y_{0i} \mid D_i = 0, Z_i = 1 ]
- \text{Avg}_n[ Y_{0i} \mid D_i = 0, Z_i = 0 ]
$$

Separate out $\tau$:

$$
= \tfrac{2}{3}\tau
+ \tfrac{2}{3}\,\text{Avg}_n[ Y_{0i} \mid D_i = 1, Z_i = 1 ]
+ \tfrac{1}{3}\,\text{Avg}_n[ Y_{0i} \mid D_i = 0, Z_i = 1 ]
- \text{Avg}_n[ Y_{0i} \mid D_i = 0, Z_i = 0 ]
$$

Recognize the weighted average:

$$
= \tfrac{2}{3}\tau
+ \text{Avg}_n[ Y_{0i} \mid Z_i = 1 ]
- \text{Avg}_n[ Y_{0i} \mid Z_i = 0 ]
$$

By random assignment, the untreated potential outcomes are the same on average:

$$
\text{Avg}_n[ Y_{0i} \mid Z_i = 1 ] \approx \text{Avg}_n[ Y_{0i} \mid Z_i = 0 ]
$$

Therefore:

$$
\text{Reduced Form} \approx \tfrac{2}{3}\tau
$$

If you can solve the math but not the story it's poiintless

Last slide for today

Reduced Form slide 14

We usually estimate the reduced form via regression. This allows us to include
covariates easily.
- The reduced form is RF = Y T − Y C .
- Remember Zi is the assignment to treatment.
- We have seen that you can estimate the difference in means by estimating the regression below:
$Yi = π0 + π1Zi + εi$
$\hat{π1}$ is our reduced form estimate of the effect.
This is also called the Intention To Treat (ITT) estimate. Why is it called the intention to treat rather than the treatment effect?

Pi_0 is the control group and the difference of the tutoring group is 86 and 84

IT's the IOT because not everyone shows up