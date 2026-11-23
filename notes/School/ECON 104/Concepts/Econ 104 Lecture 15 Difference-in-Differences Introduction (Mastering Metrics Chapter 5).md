---
type: lecture
parent: "[[Econ 104]]"
domain: econ
status: draft
---
Treatment is almost exogenous 

A shock that 

Difference-in-Differences: Voting


An alternative way of examining the effect of treatment is to look at the change i nthe voting range 

A randomized control group

Comparing a group of voting behavior and calling the voting diffferences the causal effect is myopic bc those are radically different groups bc time changes a lot

So we'd like to do differences from the control bc they will be our counterfactual to see what they'd be like if they had not undergone the treatment allowing us to account for those other factors that changed over time

If you have multiple pre-periods and multiple post periods, you can do that you just find the averagea

The control group is doing a lot of work

How do you choose a good control group, a lot of the discussion even at a PhD level is choosing a good control

You're going to be look at base certain rules

1. A control group should not be treated
2. The starting group should be similar to start with with the treatment

The fundamental 

Randomization should guarantee this is a causal estimate

Diff and diff can be estimated 

The control group in the before period is alpha, the baseline rate for the control group

Beta it's a coefficient on treatment but what does it represent?

- The difference between the treatment group and the control group is beta, it's account for differences in the before
- We'd like it to be 0

Gamma is how much the control group changed in the before and the after
Pre-post change, the whole group exists just for gamma, the workhorse of the dif and diff model

The control in pre is alpha and alpha + gamma is 



---
course: Econ 104
lesson: 14
title: "Difference-in-Dif:contentReference[oaicite:2]{index=2}n"
slides: 32
---

# Slide 1 — Title
Lesson 14  
Difference-in-Differences: Introduction

# Slide 2 — Today’s Lesson
1. Reminder: Assignment 3  
2. Difference-in-Differences: Voting  
3. Difference-in-Differences: Natural Experiments  
4. Difference-in-Differences: Mississippi Banking (MM Chapter 5)

# Slide 3 — Section
Difference-in-Differences: Voting

# Slide 4 — D-in-D: Voting (treated change)
Context:
- Treatment group got a call.
- Control group did not.
- Randomization lets us compare 2002 voting rates causally.

Alternative approach: compare change vs prior election.

Table:
- Treatment: Voted 1998 = 0.574; Voted 2002 = 0.606

Prompt:
- What is \((Y_{T,2002}-Y_{T,1998})\)?
- What concerns arise if we interpret that change as causal?

# Slide 5 — D-in-D: Voting (control as counterfactual)
Idea: use control group change as the counterfactual time trend.

Table:
- Treatment: 1998 = 0.574; 2002 = 0.606  
- Control: 1998 = 0.572; 2002 = 0.594  

Prompt:
- What is \((Y_{C,2002}-Y_{C,1998})\)?
- How does it help estimate the treatment effect?

# Slide 6 — D-in-D estimator (definition + numbers)
Generic:
$$
(Y_{T,After}-Y_{T,Before})-(Y_{C,After}-Y_{C,Before})
$$

Voting example:
$$
\tau_{DD}=(Y_{T,2002}-Y_{T,1998})-(Y_{C,2002}-Y_{C,1998})
$$
$$
=(0.606-0.574)-(0.594-0.572)
=0.032-0.022
=0.010
$$

Takeaway:
- Single-difference would overstate the effect.
- Control change nets out non-treatment time changes.

# Slide 7 — Parallel trends (core assumption)
Key: having a good control group.

Parallel trends assumption:
- Control group’s change over time captures what would have happened to treated group absent treatment.

Ideal control group:
- Similar to treatment group in the “before” period.
- Similar pre-treatment trend.

Prompt:
- Is an RCT control group likely to satisfy these?

# Slide 8 — Regression form of DiD
$$
Y_{g,t}=\alpha+\beta Treat_g+\gamma Post_t+\delta_{DD}(Treat_g \times Post_t)+u_{g,t}
$$

Prompt:
- What does \(\alpha\) represent?
	- .572
- \(\beta\)?
	- .002 (two tenths of a percentage point)
- \(\gamma\)?
	- .022
	- Change over time
- \(\delta_{DD}\)?
	- .010
	- The additional change that happens to the treatment
	- It's the difference and difference estimator

# Slide 9 — Solve coefficients from the voting table
Given:
- Treatment: 1998 = 0.574; 2002 = 0.606  
- Control: 1998 = 0.572; 2002 = 0.594  

Model:
$$
Y_{g,t}=\alpha+\beta Treat_g+\gamma Post_t+\delta_{DD}(Treat_g \times Post_t)+u_{g,t}
$$

Prompt:
- What is ($\alpha$)?
- What is \(\beta\)?
- What is \(\gamma\)?
- What is \(\delta_{DD}\)?
	- 

# Slide 10 — Section
Difference-in-Differences: Natural Experiments

# Slide 11 — D-in-D: Policy experiments (why common)
Difference-in-differences is the most common research design for policy analysis with panel data.
	In its simplest form, difference-in-differences involves identifying two cross-sectional units (states, cities, countries, etc.): 
			One was exposed to a policy change (or some other treatment). 
		A second one which was not. 
	Use data on the two units both before the policy change and after the policy change. 
	To estimate the effect of the policy on a given outcome, simply compare the change in the outcome for the treated unit to the change in the outcome for the control unit. 
	This design can be used in the absence of an RCT.

IF say santa cruz had a random shock 
# Slide 12 — Two-state, two-period setup
Setup:
- Two states \(s=0,1\), one affected by policy.
- Two periods \(t=0\) (pre), \(t=1\) (post).

Estimator:
$$
\tau_{DD}=(Y_{11}-Y_{10})-(Y_{01}-Y_{00})
$$

Key identification problem:
- Find an untreated unit that gives a good counterfactual trajectory for the treated unit.

Extensions:
- Multiple treated/control units.
- Multiple pre/post periods.

# Slide 13 — Santa Cruz rent control: choosing a control city
Prompt: Santa Cruz introduces rent control; estimate effect on house prices.

What to look for in a control city:
- Similar outcome levels pre-policy.
	- Gonna be hard pressed to find a similar price level at the per capita density
- Similar trends pre-policy.
	- If the trajectory of the prices is unmatched
- Not treated by same/similar policy.
	- A university, it sorta drives the economy
		- Santa Barbra, Davis, 
	- Similar employment rates
	- Similar tourism
	- Aging population
		- Tends to be a little bit whiter
	- Similar residential composition
- Similar characteristics pre-policy (which characteristics matter here?).
	- 

# Slide 14 — Section
Difference-in-Differences: Mississippi Banks

# Slide 15 — Mississippi bank run background
In the 1930s, there was a run on banks in Mississippi. ==We will discuss a study that uses a difference-in-differences design to examine whether monetary policy interventions to support banks saved them from closing and improved other economic outcomes. ==
	People deposit money and assume it is available for them to withdraw. 
	In practice, the banks loan the money to others (for interest) and very little money is in the bank. 
	In the 1930s, before the Federal Deposit Insurance Corporation (FDIC), if your bank failed then you were likely to lose your savings. 
	Thus, if you thought your bank might fail, you did not want to be the last one to get your money. 
	In 1930, there was a run on banks in Mississippi, as clients rushed to withdraw their money (and thus caused banks to fail, creating more panic).
The concern is if you think the bank might fail so you gotta get your money bc banks are lenders
This behavior spreads like a disease and the bank collapses
So you try to avoid this panic 

# Slide 16 — Should the Fed support banks?
An important question is how the Federal Reserve should or should not support banks that are at risk of failing (e.g., by providing the banks with loans). 
	This question came up during the last financial crisis. 
		This critical question 
	What are the arguments in favor of propping up banks by extending credit? 
		If you fail to support them you can contribute to the panic. 
		You can save businesses and help individuals that have deposits at the bank. 
	What are the arguments against supporting the banks? 
		The banks might fail anyways and then you have wasted taxpayer money. 
		You create moral hazard (reward risky behavior).


==Watch margin call and the big short==
# Slide 17 — Natural experiment: Mississippi split across Fed districts
To shed light on these questions, Richardson and Troost examined the case of the Mississippi Bank Run of 1930. 
	The failure of one bank in November of 1930 triggered a bank run starting in December of 1930. 
	There are 12 Federal Reserve Banks, each covering a region of the U.S. 
	The Atlanta Fed (6th district) favored lending to troubled banks and increased lending by 40 percent. The 6th district covers part of Mississippi. 
		==The atlanta fed favored lending to bail out banks, and as it turns out the atlanta fed covers part of missipii==
	The St. Louis Fed (8th district) did not favor lending to troubled banks and reduced lending by 10 percent. 
		==The St. Louis fed tightened up lending, and covered up the top part of missippi==
	The 8th district covers part of Mississippi.
	Thus, Mississippi is split into two parts, one that is treated (with more lending to banks) and one that acts as a control. 
	The banks in both parts face the same state regulations but face different responses from their respective Federal Reserves.
So Mississippi is covered by two different policies on the same polity 
# Slide 18 — Map (Federal Reserve districts)
Visual: geographic boundaries of Federal Reserve districts; shows where MS lies across districts.

# Slide 19 — What variation is leveraged?
Treatment variation:
- Southern MS (Atlanta / 6th): +40% lending → treatment group.
- Northern MS (St. Louis / 8th): −10% lending → control group.

First outcome: how many banks failed.

# Slide 20 — First look at outcome
Observation: decline in number of banks.
Prompt: is this evidence the intervention failed?

# Slide 21 — Single-difference in treated region (6th)
Define \(Y_{d,t}\) = number of banks open in district \(d\) at time \(t\).

Single difference for district 6:
$$
\tau_D=Y_{6,1931}-Y_{6,1930}=121-135=-14
$$

So 14 banks closed in the region with easier access to credit.

Key point:
- Decline alone isn’t proof of failure.
- Need counterfactual: closures absent access to credit.

# Slide 22 — Single-difference in control region (8th)
Counterfactual candidate: MS region under the 8th district (no aggressive intervention).

Single difference for district 8:
$$
Y_{8,1931}-Y_{8,1930}=132-165=-33
$$

# Slide 23 — Labeled comparison (6th vs 8th)
6th District: increased lending from Federal Reserve  
8th District: slightly reduced lending

# Slide 24 — DiD estimate (banks saved)
Define:
$$
\tau_{DD}=\text{Change in Treated}-\text{Change in Untreated}
$$

Compute:
$$
\tau_{DD}=(Y_{6,1931}-Y_{6,1930})-(Y_{8,1931}-Y_{8,1930})
$$
$$
=(121-135)-(132-165)=-14-(-33)=19
$$

Interpretation:
- Untreated change (33 closures) is best estimate of what would have happened without intervention.

# Slide 25 — Treatment effect picture
Statement:
- Treatment effect is the difference between the treated group’s change relative to the control group’s change.
(Graphic illustrates treated path, counterfactual, and the treatment-effect gap.)

# Slide 26 — Parallel trends again (why same-state comparison)
Parallel trends is key:
- Untreated unit must share the same trajectory as treated would have absent treatment.

Why compare within same state:
- Same laws and culture → more plausible similar economic/social forces.

Implication:
- Similar year-to-year changes absent treatment; remaining difference attributed to treatment.

Prompt:
- How assess whether the units move together absent treatment?

# Slide 27 — Regression setup (two periods)
Table:
- 1930: 6th = 135; 8th = 165  
- 1931: 6th = 121; 8th = 132  

Regression:
$$
Y_{d,t}=\alpha+\beta Treat_d+\gamma Post_t+\delta_{DD}(Treat_d \times Post_t)+u_{d,t}
$$

# Slide 28 — Add years (1929–1934)
Data available:

Year | 6th | 8th  
1929 | 141 | 168  
1930 | 135 | 165  
1931 | 121 | 132  
1932 | 115 | 120  
1933 | 102 | 112  
1934 | 102 | 110  

Benefits:
- evaluate parallel trends
- estimate regression with multiple pre and post periods

# Slide 29 — Trend check (visual)
Point:
- Untreated area is a good counterfactual only if it moves with treated unit absent treatment (parallel trends).

# Slide 30 — Multi-period regression result
Using all 6 years (1929–1934): 2 pre-treatment, 4 post-treatment years.

Result:
$$
Y_{d,t}=167-29Treat_d-49Post_t+20.5(Treat_d \times Post_t)
$$

Notes:
- 20.5 is similar to 19 from the simple pre/post comparison.
- Multiple periods allow standard errors (multiple change observations).
- Multiple periods help test persistence (did policy delay closures?).

# Slide 31 — Persistence question (visual)
Prompt:
- Do effects appear persistent?
(Graphic includes a DiD counterfactual path.)

# Slide 32 — Beyond banks: wholesale firms
Motivation:
- Want broader economic outcomes, not only bank survival.

Prompt:
- How did increased lending by the Atlanta Fed affect wholesale firms?

Table: “Wholesale firm failures and sales in 1929 and 1933”

Panel A: Number of wholesale firms  
- Sixth (Atlanta): 783 → 641, change = −142  
- Eighth (St. Louis): 930 → 607, change = −323  
- DiD (Sixth–Eighth difference in changes): 181  

Panel B: Net wholesale sales (\$ million)  
- Sixth (Atlanta): 141 → 60, change = −81  
- Eighth (St. Louis): 245 → 83, change = −162  
- DiD (Sixth–Eighth difference in changes): 81