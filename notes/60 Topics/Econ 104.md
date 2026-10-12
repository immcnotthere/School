---
type: topic
parent: "[[Experimental Economics]]"
domain: econ
---
# Week 1
## L1 Overview
This course is about **causal inference**: estimating how a treatment or intervention changes an outcome.

Prediction can be accurate without being causal.

For any individual, we observe either:
- outcome with treatment
- outcome without treatment

but never both.

This missing counterfactual is the core challenge of causal inference.

A rough ordering from most credible to least credible:

1. Randomized experiments  
2. Regression discontinuity designs  
3. Difference-in-differences  
4. Instrumental variables  
5. Selection on observables (regression)

Credibility declines as identification relies more heavily on assumptions that cannot be directly tested.
## L2 OLS
Ordinary Least Squares: A way of estimating the relationship between one variable and another variable (or variables). Fits a line (or hyperplane) that summarizes this relationship by getting as close as possible to the data points. OLS minimizes the sum of the squared distances from each of the data points to the line.

The distance from the final exam score for individual i to the line is $\hat{u_i} = y_i −(\hatβ_0 + \hatβ_1x_i )$
We square to normalize to absolute difference without mathematical complexity which absol. val. calcs create $\hat{u_i}^2 = (y_i −(\hatβ_0 + \hatβ_1x_i ))^2$ We want to minimize the the sum of the squared errors the errors being $\hat{u_i}^2$

We set=0 to do a partial derivative and we get from the minimized square of summed differences and our slope for the regression is simplified as cov(x,y)/var(x) and the the intercept is the average y-the slope the average x

**Assumption 1**: The model in the population is linear in parameters
$$  
y=\beta_0+\beta_1x_1+\beta_2x_2+\cdots+\beta_kx_k+u_i  
$$
where the Betas are parameters and $u_i$ is an unobservable random error term, AND the model is correctly specified.
- Least squares model is linear so it will only be the right model if the actual relationship in the population is linear.

**Assumption 2**: We have a random sample of $x,y$ pairs from the population of interest.
- If we want to correctly estimate the relationship in the population, we need a random sample that is representative of the population.

**Assumption 3**: In the sample, none of the independent variables (Xs) are constant (or have an exact linear relationship with each other).
	If you want to estimate x over y, x needs to vary duh-doy bc you can't divide by 0 variance


**Assumption 4**: Zero conditional mean $E[u\mid x_1,x_2,\ldots,x_k]=0$.
**THE REASON ILL HAVE A JOB IS THIS DOES NOT HOLD, OMMITTED VARIABLE BIAS IS REAL AND CONSTANT**
# Week 2

## L3 HT & Robust
Context: [[Standard Error]],[[t-critical]],[[t-statistic]],[[Standardization (math)]], [[Hat notation in econometrics|Hat (Econometrics)]], [[Estimators]], [[Mean]], [[Variance (Math)]], [[Sample Mean]], [[Estimators and Estimates]], sample, [[Sample variance]], [[Standard Error|Standard Error of the Mean]], [[t-statistic|t-stat]], [[t-critical|t*]], [[p-value]], [[confidence interval]], [[Hypothesis Testing|Hypothesis test]], [[Population Mean]], [[Population Variance]], 
### **Tests on Regression Coefficients**
If we can get the difference between the estimate and the real population's coefficient (We don't know this hence the experiment, so we use 0 as a way of engaging the null hypothesis where the true effect is 0 so $\beta_1$ is =0) we can determine how large that difference is in generalizable terms when we standardize it, by dividing it by the spread of sample statistics across repeated samples (not the spread of the individual data points that would be standard deviation). This is the t-test and the t-stat provides the foundation for the rest of the statistical tests that are informative by putting the quality of the coefficient estimate into standardized normal terms using the logic of the CLT which states that as n grows it will come to approximate the shape of a standard normal distribution.

1. T-tests
2. P-values
3. Confidence intervals

NEED TO BE ABLE TO AT A GLANCE INTERP THESE THREE BOYS

- T-Tests
	- How unusual is my estimated coefficient, relative to the normal sampling noise I expect under OLS?
	- Calculated using 
		- $\hat\beta_j$ is your estimate from the sample  
		- $\beta_j$ is the actual population coefficient  
			- We intuitively subtract our estimate from our true coefficient to determine how we well we've estimated the relationship. However we need to standardize this proportion of accuracy to the Standard Normal Distribution for it to be interpretable. 
		- $se(\hat\beta_j)$ is the typical amount your estimate would vary from sample to sample
	- In practice, you usually **do not know** $\beta_j$, so you cannot directly compute this exact expression.
	- Instead, you usually test something like: $t = \frac{\hat\beta_j-0}{se(\hat\beta_j)}$ asking, “How many standard errors away is my estimate from 0?" We use 0 because it is the true relationship $\beta_j$ in the null hypothesis where there is no effect.
	- SO
		- $t$ equals the fraction $\frac{\hat\beta_j - 0}{se(\hat\beta_j)}$: take $\hat\beta_j$, subtract $0$, and divide by $se(\hat\beta_j)$.
		- That is the usual t-test for whether $x_j$​ has any effect.
		- This $t$ is normally distributed "$\sim Normal(0,1)$" after being standardized by the $se$ of the pop estimate.
	- Interpreting ([[t-critical]] you have to search this up)
		- **If $|t| > t_{critical}$**: Your estimate is so many standard errors away from zero that it's unlikely to have happened by chance. You **reject the null**
		- **If $|t| < t_{critical}$**: Your estimate is "near zero" in a statistical sense. You **fail to reject the null**.
Because the standardized estimate $\frac{\hat{\beta}_j - \beta_j}{se(\hat{\beta}_j)}$ follows a standard normal distribution $N(0, 1)$, we can evaluate statistical significance using three equivalent methods

- P-value
	- 1. Calculate the t-statistic
	- 2. Determine the Probability Area
		- The p-value represents the probability of seeing a result as extreme as yours if the null hypothesis were true. For a standard two-tailed test ($H_A: \beta_1 \ne 0$), you calculate the area in both tails of the distribution: $p\text{-value} = 2 \times P(Z > |t|)$
	- 3. Find the Value 
		1. By Hand: Look up your $|t|$ in a Standard Normal (Z) Table. Find the area to the right of your value and multiply by 
		2. In Stata: Read the value directly from the regression output table under the P>|t| column.
	- 4. Use the standard normal distribution to compute the exact probability of observing a result at least as extreme as yours, assuming the null is true.
		- **Definition**: The p-value is the sum of all events less likely than the one observed.
		- **Decision Rule**: Reject $H_0$ if $p < \alpha$ (usually $0.05$)
- Confidence Intervals (CI)
	- A range around the estimate where we are confident the true population parameter $\beta_j$ falls
		- **Formula**: 
			- $[\hat{\beta}_j - ME, \hat{\beta}_j + ME]: ME=t_{crit} \times se(\hat{\beta}_j)$.
				- Expanded Form: $[\hat{\beta}_j - t_{crit} \times se(\hat{\beta}_j), \hat{\beta}_j + t_{crit} \times se(\hat{\beta}_j)]$
				- In plain English, the confidence interval is built by taking the **estimate** $\hat{\beta}_j$ and then subtracting and adding the **margin of error** (which is just the critical value multiplied by the standard error).
		- **Decision Rule**: Reject $H_0$ if the interval **does not** include $0$.
Determining how to do good hypothesis testing, is what it's all about in econometrics

### **Means and Differences in Means**

A **statistical [[Hypothesis Testing|hypothesis test]]** is a method of statistical inference used to decide whether the data provide sufficient evidence to reject a particular hypothesis. In order to arrive at this conclusion the inputs of a HT, variance and expectation, are required of respondent variable $Y_i$.

Being interested in the **[[Population Mean]]** ($\mu_Y = E[Y_i]$) and **[[Population Variance]]** ($\sigma_Y^2 = E[(Y_i - \mu_Y)^2]$), which represents the "true" center and spread of a variable in an entire group. Because we rarely observe the whole population, we calculate the **[[Sample Mean]]** ($\bar{Y} = \frac{1}{n} \sum Y_i$) and **[[Sample Variance]]** ($\hat{\sigma}_Y^2 = \frac{1}{n-1} \sum (Y_i - \bar{Y})^2$) to estimate these truths. To determine the precision of our estimate, we calculate the **[[Standard Error of the Mean]]** ($se(\bar{Y}) = \frac{\hat{\sigma}_Y}{\sqrt{n}}$), which measures how much the sample mean would vary across different samples. Finally, we assemble these into a **[[t-statistic]]** ($t = \frac{\bar{Y} - c}{se(\bar{Y})}$) to test whether our observed mean is significantly different from a hypothesized constant $c$.
### 
**Robust Standard Errors**
We want to know how precise our estimate $\hat{\beta}_1$​ is. That means finding $\text{Var}(\hat{\beta}_1)$.

We start with the OLS formula $\hat{\beta}_1 = \frac{\sum (x_i - \bar{x})(Y_i - \bar{Y})}{\sum (x_i - \bar{x})^2}$ and simplify the numerator by distributing: $\sum (x_i - \bar{x})(Y_i - \bar{Y}) = \sum (x_i - \bar{x})Y_i - \sum (x_i - \bar{x})\bar{Y}$. The second term disappears entirely because $\bar{Y}$ is a constant with respect to the summation, so it factors out to give $\bar{Y} \sum (x_i - \bar{x})$. This inner sum is the sum of all deviations from the mean($\bar{x}_n$); by definition, the positive and negative distances perfectly cancel ...

($\sum x_i = x_1 + x_2 + \dots + x_n$, $\sum \bar{x} = \bar{x} + \bar{x} + \dots + \bar{x}$ since $\bar{x} = \frac{1}{n}\sum x_i$ by definition, multiplying both sides by $n$ gives $n\bar{x} = \sum x_i$.)

, so $\sum (x_i - \bar{x}_n) = 0$, and therefore $\bar{Y} \times 0 = 0$. We are left with $\hat{\beta}_1 = \frac{\sum (x_i - \bar{x})Y_i}{\sum (x_j - \bar{x})^2}$, which we can rewrite by pulling the $Y_i$ outside the fraction:

$$\hat{\beta}_1 = \sum \left[ \frac{x_i - \bar{x}}{\sum (x_j - \bar{x})^2} \right] Y_i = \sum w_i Y_i$$

This representation is powerful for three reasons. First, the weights $w_i = \frac{x_i - \bar{x}}{\sum (x_j - \bar{x})^2}$ are pure constants — they depend only on $x$, not on $Y$, so they carry no randomness. Second, it proves that $\hat{\beta}_1$ is simply a linear combination of the data points $Y_i$. Third, and most usefully for deriving standard errors, it lets us apply the rule $\text{Var}(\sum w_i Y_i) = \sum w_i^2 \text{Var}(Y_i)$ directly.

---

Step 2: Apply the variance of a weighted sum

For any weighted sum of **independent** random variables:

$$\text{Var}!\left(\sum w_i Y_i\right) = \sum w_i^2 ,\text{Var}(Y_i)$$

Since $\text{Var}(Y_i) = \sigma_i^2$ (each observation can have its own variance — this is the _heteroskedastic_ case), we get:

$$\text{Var}(\hat{\beta}_1) = \sum w_i^2 ,\sigma_i^2$$

Step 3: Substitute $w_i$ back in

Plugging $w_i = \frac{x_i - \bar{x}}{\sum(x_j - \bar{x})^2}$ into $\sum w_i^2 \sigma_i^2$:

$$\text{Var}(\hat{\beta}_1) = \sum \left(\frac{x_i - \bar{x}}{\sum(x_j - \bar{x})^2}\right)^2 \sigma_i^2$$

The denominator is a constant across the sum, so it factors out as its square:

$$= \frac{\sum (x_i - \bar{x})^2 ,\sigma_i^2}{\left(\sum (x_i - \bar{x})^2\right)^2}$$

And that's exactly the formula in your notes.

**The intuition**

The formula is essentially a **signal-to-noise ratio** in the denominator vs. numerator:

- **Denominator** $\left(\sum(x_i - \bar{x})^2\right)^2$ — the more spread out your $x$ values are, the more "leverage" you have to precisely estimate the slope. More variation in $x$ → smaller variance of $\hat\beta_1$.
- **Numerator** $\sum(x_i - \bar{x})^2\sigma_i^2$ — observations with high noise ($\sigma_i^2$) contribute more uncertainty, but only proportionally to how far they are from $\bar{x}$ (since outlier $x$ values pull the slope harder).

This is also why it's called a **robust** standard error — by not assuming all $\sigma_i^2$ are equal (homoskedasticity), it remains valid even when variance differs across observations.
To understand where the variance of our slope estimate comes from, we first have to view the OLS estimator, $\hat{\beta}_1$, not just as a static number, but as a **weighted sum of our outcomes**. By rearranging the standard OLS formula, we can define $\hat{\beta}_1$ as $\sum w_i Y_i$. Here, the weights $w_i$ are determined entirely by the "leverage" of each $x$ value—specifically, how far an individual $x_i$ sits from the mean relative to the total variation in $x$. Because these weights are constants (determined by our fixed $x$ values), they act as the scaling factors for the randomness inherent in our $Y$ observations.

When we transition to calculating the variance, we rely on the property that the variance of a weighted sum of independent variables is the sum of the squared weights multiplied by the individual variances. In a **heteroskedastic world**, we cannot assume every observation has the same "noise" level; instead, each $Y_i$ has its own variance, $\sigma_i^2$. By substituting our specific weights back into this general rule, we arrive at a ratio: the numerator is the sum of squared deviations of $x$ weighted by their specific error variances, while the denominator is the square of the total variation in $x$.

$$\text{Var}(\hat{\beta}_1) = \frac{\sum (x_i - \bar{x})^2 \sigma_i^2}{\left(\sum (x_i - \bar{x})^2\right)^2}$$

This "sandwich" structure tells a clear story of **signal versus noise**. The denominator represents our signal—the more spread out our $x$ values are, the more stability we have in "pinning down" the slope, which reduces our overall uncertainty. The numerator, meanwhile, captures the impact of noise—it shows that observations with high variance ($\sigma_i^2$) create the most trouble when they also happen to be at the extremes of our $x$ distribution. By acknowledging that $\sigma_i^2$ can differ across the sample, this robust approach ensures our standard errors remain reliable even when the "scatter" around our regression line isn't perfectly uniform.



Standard Errors
	To conduct significance testing in a simple regression model $Y_i = \beta_0 + \beta_1X_i + u_i$, we must compute the standard error of the slope coefficient $\hat{\beta}_1$, which is derived from the [[Variance (Math)]] formula $Var(\hat{\beta}_1) = \frac{\sum_{i=1}^{n}(x_i - \hat{\mu}_x)^2\sigma_i^2}{(\sum_{i=1}^{n}(x_i - \hat{\mu}_x)^2)^2}$. 
		
The simplification of this formula depends on whether the errors are **[[homoscedastic]]**, meaning the variance $Var(u_i|x_i) = \sigma_u^2$ is constant across all levels of $X$, or **[[heteroscedastic]]**, where the variance $Var(u_i|x_i) = \sigma_i^2$ changes depending on the value of $X$.

Under the assumption of homoscedasticity, the variance formula simplifies to $Var(\hat{\beta}_1) = \frac{\sigma_u^2}{\sum_{i=1}^{n}(x_i - \hat{\mu}_x)^2}$, which is the default calculation used by Stata. However, because the precision of an estimate is often a function of the size of the independent variables, this assumption is unlikely to hold in many real-world contexts. In these cases, the variance does not simplify, and researchers should use the Stata command `reg y x, robust` to obtain **robust standard errors** that accurately account for heteroscedasticity.


1. T-tests
2. P-values
3. Confidence intervals

Under the four asssumptions:
$$t= \frac{(\hat\beta _j - \beta_j)}{se(\hat\beta _j)}$$

//Take the estimated coefficient, subtract the true coefficient, and divide by the standard error of the estimate.
//In plain English, this tells you **how far your estimate is from the true value, measured in standard-error units**.

In practice, you usually **do not know βj\beta_jβj​**, so you cannot directly compute this exact expression.

Instead, you usually test something like:

$t = \frac{\hat\beta_j - 0}{se(\hat\beta_j)}$

which asks:

> “How many standard errors away is my estimate from 0?”

That is the usual t-test for whether xjx_jxj​ has any effect.
So the t-stat is basically a **standardized estimation error**.

Why is the mean 0? $\hat\beta_j - \beta_j$ goes to 0 as the sample gets large because $\hat\beta_j$ is unbiased (e.g. because we have a representative sample.)

Why is the variance 1? because we are dividing $\hat\beta_j$ 

Why is the t-stat normally distributed? bβj is a sum of a bunch of independent Xs and Y. Sums of a large number of independent variables will be normally distributed (Central Limit Theorem)



##  L4 Potential Outcomes Framework

**Tags:** #econ104 #causal-inference #RCT **Related:** [[L1 Overview]] · [[Selection Bias]] · [[Average Treatment Effect]] · [[Randomized Control Trials]]

---

The potential outcomes framework is how we formalize what causal inference is trying to estimate.

For any individual $i$, the treatment effect $\tau_i$ is the difference between two states of the world:

- $Y_{1,i}$ — outcome in the treated state
- $Y_{0,i}$ — outcome in the untreated state

$$\tau_i = Y_{1,i} - Y_{0,i}$$

We only ever observe one. The one we don't observe is the **counterfactual**.

---

### The Bias Problem

When treatment is chosen rather than assigned, the people who select into treatment are systematically different from those who don't. Using an untreated person as a counterfactual for a treated person conflates two things:

$$\hat{\tau}_i = Y_{1,i} - Y_{0,\text{comparison}} = \tau + \underbrace{(Y_{0,i} - Y_{0,\text{comparison}})}_{\text{Selection Bias}}$$

The bias term is nonzero whenever the treated and untreated groups would have had different outcomes even in the absence of treatment.

---

### Selection Bias

Selection bias arises when people choose treatment based on expected benefit. This means:

- Those who opt in likely have higher potential outcomes in _both_ states
- $Y_{0,\text{treated}} \neq Y_{0,\text{untreated}}$ — the untreated baseline differs across groups
- Naive comparisons overstate the treatment effect

---

### Average Treatment Effect (ATE)

Since $\tau_i$ is unobservable at the individual level, we target the population average:

$$\tau_{ATE} = \frac{1}{N}\sum_{i=1}^{N} \tau_i = \frac{1}{N}\sum_{i=1}^{N}(Y_{1,i} - Y_{0,i})$$

This is estimated by comparing group means:

$$\hat{\tau}_{ATE} = \bar{Y}_{\text{treat}} - \bar{Y}_{\text{notreat}} = \frac{1}{n_T}\sum_{i \in \text{treat}} Y_i - \frac{1}{n_C}\sum_{i \in \text{notreat}} Y_i$$

This estimate is unbiased o
Only if group membership is independent of potential outcomes — i.e., no selection bias.

---

### The Fix

Randomization eliminates selection bias by ensuring treatment assignment is independent of potential outcomes. If the two groups are created by a lottery:

$$Y_{0,\text{treated}} = Y_{0,\text{control}}$$

and the comparison $\bar{Y}_{\text{treat}} - \bar{Y}_{\text{notreat}}$ recovers the true ATE.

# Week 3

## L5 Randomized Controlled Trials

**Tags:** #econ104 #RCT #causal-inference **Related:** [[L4 Potential Outcomes Framework]] · [[L3 Hypothesis Testing]] · [[Selection Bias]] · [[Average Treatment Effect]]

---

The goal of causal inference is to estimate $\tau = E[Y_i \mid D_i = 1] - E[Y_i \mid D_i = 0]$, the difference in expected outcomes between treated and untreated states. The problem is that when people choose their treatment status, this comparison is contaminated by selection bias.

---

### Key Definitions

**Expectation** $E[Y_i]$ is the true population average. Estimated from a sample by $\text{Avg}_n[Y_i] = \frac{1}{n}\sum y_i$.

**Conditional expectation** $E[Y_i \mid X_i = X]$ is the average of $Y$ at a given value of $X$. OLS estimates this relationship.

**Treatment effect** is the difference between two conditional expectations:

$$\tau = E[Y_i \mid D_i = 1] - E[Y_i \mid D_i = 0]$$

where $D_i = 1$ means treated and $D_i = 0$ means not treated.

**Unbiased estimator**: $\hat{\tau}$ is unbiased if $E[\hat{\tau}] = \tau$. Repeating the experiment many times, the average estimate would equal the true value.

---

### Why Non-Random Assignment Fails

When $Y_{1i} = Y_{0i} + \tau$ (constant treatment effect), the naïve comparison gives:

$$\hat{\tau}_{ATE} = \text{Avg}[Y_{1i} \mid D_i = 1] - \text{Avg}[Y_{0i} \mid D_i = 0] = \tau + \underbrace{(\text{Avg}[Y_{0i} \mid D_i = 1] - \text{Avg}[Y_{0i} \mid D_i = 0])}_{\text{Selection Bias}}$$

The bias term is nonzero when the treated and untreated groups have different baseline outcomes. People selecting into treatment are typically different in ways that also affect the outcome — even absent treatment. These designs are common because they are easy, not because they are good.

---

### How Randomization Fixes This

Random assignment makes $D_i$ independent of $Y_{0i}$. The two groups are similar in both observables (age, gender) and unobservables (motivation, health). Therefore:

$$E\text{Avg}[Y_{0i} \mid D_i = 1] = E\text{Avg}[Y_{0i} \mid D_i = 0]$$

The bias term cancels and the estimate is unbiased:

$$E[\hat{\tau}_{ATE}] = \tau + 0 = \tau$$

The control group becomes a valid counterfactual. Any difference in outcomes between groups is attributable to the treatment.

---

### Implementation

**Estimating the treatment effect** via regression:

$$Y_i = \beta_0 + \tau D_i + u_i$$

$\beta_0$ is the mean outcome for the control group. $\tau$ is the treatment effect. $u_i$ captures all other determinants of $Y_i$.

**Checking balance** — verifying the randomization worked — via regression:

$$X_i = \beta_0 + \beta_1 D_i + u_i$$

where $X_i$ is a pre-treatment characteristic (age, income, etc.). $\beta_0$ is the control group mean. $\beta_1$ is the difference between groups. A statistically insignificant $\beta_1$ supports successful randomization. A significant $\beta_1$ indicates the randomization failed.

---

### RAND Health Insurance Experiment

The canonical RCT in health economics. Participants were randomly assigned to insurance plans ranging from catastrophic-only to fully free. The balance tables showed no statistically significant differences in demographics or baseline health across groups — evidence the randomization succeeded. The treatment effects showed that more generous insurance increased health care use and spending, but had little measurable effect on most health outcomes.

## L6 Selection on Observables

Tags: #econ104 #selection-bias #omitted-variable-bias #observational-data Related: [[L5 Randomized Controlled Trials]] · [[L3 Hypothesis Testing]] · [[Causal Inference]] · [[Selection Bias]] · [[Observational Data]]

When an [[RCT]] is not feasible, researchers turn to [[Observational Data|observational data]]. The challenge is that [[Treatment Assignment|treatment assignment]] is no longer random — people _select_ into treatment, introducing [[Selection Bias|selection bias]]. [[Selection on Observables]] is the strategy of controlling for [[Confounding Variable|confounding factors]] that are measurable, though it has important limitations.

---

### Concluding Remarks on RCTs

#### Random Sample vs. RCT

These two concepts are frequently confused but are fundamentally different:

A **[[Random Sample]]** is representative of a population. It produces unbiased estimates of [[Population parameter|population characteristics]] (e.g., average income) but is **not** a method for estimating the [[Causal Effect|causal effect]] of a treatment.

A **[[RCT|randomized control trial]]** is a method for estimating [[Causal Effect|causal effects]]. It may be conducted on a non-representative sample — this is fine. It estimates the [[Treatment Effect|treatment effect]] _for that sample_ (e.g., the effect of blood pressure medication on people with high blood pressure).

#### Interpreting Balance Tables

[[Balance Table|Balance]] must be assessed on **both** magnitude and [[Statistical Significance|statistical significance]]. Three illustrative examples from the voting outreach experiment:

|Example|Magnitude|Statistical Significance|Verdict|
|---|---|---|---|
|1|Small differences|All p-values > 0.10|✅ Balanced|
|2|Small differences|Age p = 0.02|⚠️ Marginal — age is borderline significant|
|3|Large age difference (3.56 yrs)|Age & Voted 2000 p = 0.00|❌ Not balanced|

#### Attrition

**[[Attrition]]** is the loss of participants before the endline outcome is measured.

[[Attrition]] is problematic when:

- The _rate_ of attrition differs between treatment and control (undoes [[Balance Table|balance]]) — test by comparing attrition rates across groups
- The _type_ of people who leave differs between groups (undoes [[Balance Table|balance]]) — test by comparing [[Baseline Characteristics|baseline characteristics]] of those who attrit

The primary solution is to minimize [[Attrition|attrition]] via follow-up surveys or [[Administrative Data|administrative data]] that tracks everyone. Attrition was not an issue in the voting experiment because voting is observed in [[Administrative Data|administrative records]].

#### Noncompliance

**[[Noncompliance]]** is the failure of participants to do what the [[Randomization|randomization]] assigned:

- Treatment group members may not take the treatment
- Control group members may obtain the treatment anyway

This does **not** invalidate the experiment — it requires adjusting the [[Causal Effect|causal estimates]] (addressed in MM Chapter 3). In the voting experiment, treatment-group [[Noncompliance|noncompliance]] occurs when recipients ignore the mailer; control-group [[Noncompliance|noncompliance]] is unlikely since the control group receives no outreach by design.

---

### Selection on Observables: Omitted Variable Bias

#### Definition

**[[Variable Bias#OVB (Omitted Variable Bias)|Omitted Variable Bias]]** occurs when an important causal factor is left out of a [[Regression|regression]], causing the estimated [[Regression#Coefficients|coefficient]] on the included variable to be over- or underestimated. It is the regression manifestation of [[Selection Bias|selection bias]].

A variable must satisfy **both** conditions to create [[Variable Bias#OVB (Omitted Variable Bias)|bias]]:

1. It is correlated with the **[[Outcome Variable|outcome variable]]**
2. It is correlated with an **[[Explanatory Variable|explanatory variable]]**

Variables are omitted for two main reasons: they are unavailable in the data, or the researcher does not think to include them.

#### The Bias Formula

Suppose the true model is:

$$Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + u$$

But we can only estimate:

$$Y = \beta_0^* + \beta_1^* X_1 + u$$

And the [[Auxiliary Regression|auxiliary regression]] between the omitted variable and the included one is:

$$X_2 = \delta_0 + \delta_1 X_1 + \eta$$

Substituting into the true equation shows that instead of estimating $\beta_1$, we estimate:

$$\boxed{\beta_1^* = \beta_1 + \beta_2 \delta_1}$$

$$\text{Bias} = \beta_2 \delta_1$$

The direction of [[Variable Bias#OVB (Omitted Variable Bias)|bias]] follows from the signs of $\beta_2$ (effect of omitted variable on $Y$) and $\delta_1$ ([[Correlation|correlation]] between omitted and included variable):

||$\text{Corr}(X_1, X_2) > 0$|$\text{Corr}(X_1, X_2) < 0$|
|---|---|---|
|$\beta_2 > 0$|Positive bias|Negative bias|
|$\beta_2 < 0$|Negative bias|Positive bias|

#### Worked Example: College and Wages

Estimable [[Regression|regression]]: $$\widehat{wage_i} = 14.00 + 10.00 \cdot college_i$$

True regression (with motivation): $$\widehat{wage_i} = 12.20 + 7.00 \cdot college_i + 6.00 \cdot motivated_i$$

[[Auxiliary Regression|Auxiliary regression]] (omitted on included): $$\widehat{motivated_i} = 0.30 + 0.50 \cdot college_i$$

Applying the [[Variable Bias#OVB (Omitted Variable Bias)|bias formula]]: $$\beta_1^* = 7.00 + 6.00 \times 0.50 = 7.00 + 3.00 = 10.00 \checkmark$$

The [[Variable Bias#OVB (Omitted Variable Bias)|omitted variable bias]] is **+3.00**. Motivated people are more likely to attend college ($\delta_1 > 0$) _and_ earn higher wages ($\beta_2 > 0$), so the college [[Regression#Coefficients|coefficient]] is inflated upward.

#### Practice: Tutoring and GPA

$$\widehat{GPA_i} = 2.90 + 0.20 \cdot tutoring_i$$

- **[[Confounding Variable|Work ethic]]**: positively affects GPA ($\beta_2 > 0$) and positively correlated with seeking tutoring ($\delta_1 > 0$) → **positive [[Variable Bias#OVB (Omitted Variable Bias)|bias]]**, tutoring coefficient overstated
- **[[Confounding Variable|Ability]]**: positively affects GPA ($\beta_2 > 0$) but may be _negatively_ correlated with tutoring if high-ability students need it less ($\delta_1 < 0$) → **negative [[Variable Bias#OVB (Omitted Variable Bias)|bias]]**, tutoring coefficient understated
- Adding these variables to the [[Regression|regression]] will **reduce** [[Variable Bias#OVB (Omitted Variable Bias)|bias]]
- Adding them will **not eliminate** [[Variable Bias#OVB (Omitted Variable Bias)|bias]] unless they are perfectly measured and all omitted variables are included

---

### Selection on Observables: Private College Example

#### Setup

From Dale and Krueger (2002), _"Estimating the Payoff to Attending a More Selective College: An Application of [[Selection on Observables]] and [[Selection on Unobservables|Unobservables]]"_:

$$\ln(earn_i) = \beta_0 + \beta_1 \cdot private_i + u_i$$

Likely [[Confounding Variable|omitted variables]]: student ability ([[Standardized Testing|SAT scores]]), family background ([[Socioeconomic Status|parental income]]), motivation, ambition. All are positively correlated with both private college attendance and future earnings → expected **upward [[Variable Bias#OVB (Omitted Variable Bias)|bias]]** on $\beta_1$.

#### Strategy

The paper adds [[Control Variable|controls]] sequentially to observe how $\beta_1$ changes:

- Observable student characteristics: [[Standardized Testing|SAT scores]], [[Socioeconomic Status|parental income]], gender, race, HS class rank
- **Key innovation**: control for the _selectivity of the application set_ — the average [[Standardized Testing|SAT score]] of all colleges the student applied to. This acts as a [[Proxy Variable|proxy]] for otherwise unobservable traits like motivation, unobserved ability, and parental influence.

#### Results: Effect of Controls on the Private School Coefficient

|Specification|Controls|Private Coefficient|
|---|---|---|
|(1)|None|.212|
|(2)|+ Own SAT|.152|
|(3)|+ SAT, income, gender, race, HS rank|.139|
|(4)|+ Application set SAT (no other controls)|.034|
|(5)|+ Application set SAT + own SAT|.031|
|(6)|+ All controls|.037|

- Baseline estimated effect: **+21.2%** earnings premium for private college
- Adding student [[Standardized Testing|SAT score]] eliminated ~6 percentage points of [[Variable Bias#OVB (Omitted Variable Bias)|bias]] (.212 → .152)
- Adding other student traits eliminated another ~1.3 pp (.152 → .139)
- Adding application set controls eliminated the largest share — ~10.5 pp (.139 → .037)

The final estimate of ~3–4% is small and [[Statistical Significance|statistically insignificant]], suggesting most of the raw premium was due to [[Selection Bias|selection]], not the college itself.

---

### Big Takeaways

> [[Selection on Observables]] can reduce but generally cannot eliminate [[Variable Bias#OVB (Omitted Variable Bias)|bias]] from [[Selection on Unobservables|unobservables]].

- Adding relevant [[Control Variable|controls]] **reduces** [[Variable Bias#OVB (Omitted Variable Bias)|omitted variable bias]]
- Cannot **eliminate** [[Variable Bias#OVB (Omitted Variable Bias)|bias]] unless _all_ omitted variables are included
- Cannot eliminate [[Variable Bias#OVB (Omitted Variable Bias)|bias]] unless all omitted variables are **well-measured**
- When [[Selection on Unobservables|unobservable confounders]] remain, other [[Identification Strategy|identification strategies]] ([[RCT]], [[Instrumental Variables|IV]], [[Regression Discontinuity|RDD]], [[Difference-in-Differences|DiD]]) are needed to recover unbiased [[Causal Effect|causal effects]]
# Week 4
## L7 Experimental vs Non-Experimental Evidence

Tags: #econ104 #RCT #causal-inference #observational-data #voting-experiment Related: [[L6 Selection on Observables]] · [[L5 Randomized Controlled Trials]] · [[Causal Inference]] · [[Internal Validity]] · [[Selection Bias]]

This lesson uses a [[Get Out the Vote|voting encouragement experiment]] as a concrete case study to compare what [[RCT|experimental]] and [[Observational Data|non-experimental]] designs can and cannot tell us about [[Causal Effect|causal effects]]. The core question: does it matter whether people are _randomly assigned_ to treatment versus _choosing_ to receive it?

---

### The Voting Experiment: Setup

#### Research Question

What is the [[Causal Effect|causal effect]] of receiving a phone call encouraging you to vote on the probability of voting?

- **[[Treatment Assignment|Treatment]]**: being randomly assigned to receive a call (`treat_real = 1`)
- **[[Outcome Variable|Outcome]]**: whether the individual voted in 2002 (`vote02`)
- Note: estimates are scaled ×100 to be expressed as percentage points

#### Key Variable Distinction

This dataset contains two critically different treatment variables — understanding the difference is the whole lesson:

|Variable|What it measures|Assignment mechanism|
|---|---|---|
|`treat_real`|Randomly _assigned_ to get a call|[[Randomization\|Random]]|
|`contact`|Actually _received and answered_ the call|[[Self-Selection\|Self-selected]]|

#### Dataset Variables

`vote02` (outcome), `treat_real` (random assignment), `contact` (answered call), `newreg` (newly registered), `busy` (line was busy), `age`, `female`, `vote00` (voted 2000, pre-treatment), `vote98` (voted 1998, pre-treatment), `state`, `comp_ia` (competitive Iowa district)

---

### Part 1: The Experiment (Random Assignment)

#### Potential Outcomes Framework

The two [[Potential Outcomes|potential outcomes]] of interest:

- $Y_{1,i}$: whether individual $i$ votes _if_ assigned to get the call (`treat_real = 1`)
- $Y_{0,i}$: whether individual $i$ votes _if not_ assigned to get the call (`treat_real = 0`)

The [[Average Treatment Effect|treatment effect]] of interest: $$\tau = E[\tau_i] = E[Y_{1,i} - Y_{0,i}]$$

Because people did **not** choose their assignment, [[Randomization|random assignment]] means the two groups have similar [[Potential Outcomes|potential outcomes]] — making the estimate of $\tau$ likely [[Unbiased Estimator|unbiased]].

#### Why Can't We Compare Potential Outcomes Directly?

The [[Fundamental Problem of Causal Inference|fundamental problem of causal inference]]: we never observe both $Y_{1,i}$ and $Y_{0,i}$ for the same person. [[Randomization|Randomization]] solves this by making the control group a valid [[Counterfactual|counterfactual]].

#### How Can Randomization Fail?

- Actually implementing the [[Randomization|randomization]] incorrectly (e.g., Vietnam War [[Draft Lottery|draft lottery]])
- [[Attrition|Attrition]] — sometimes easier to track the treated group, which unbalances the groups post-randomization

#### Balance Table: Random Assignment

|Variable|Control|Treatment|Difference|P-Value|
|---|---|---|---|---|
|Age|52.16|51.98|-0.18|0.2270|
|Female|55.23|54.64|-0.59|0.1479|
|Voted 2000|56.37|56.72|0.35|0.3906|
|Voted 1998|23.14|22.68|-0.47|0.1767|
|New Voter|11.68|11.64|-0.04|0.8718|
|N|1,153,072|14,972|||

All differences are small in magnitude and [[Statistical Significance|statistically insignificant]] (all p > 0.10). The most informative variable for assessing [[Balance Table|balance]] is **Voted 2000**, since past voting is the best [[Proxy Variable|proxy]] for the [[Potential Outcomes|baseline potential outcome]] (propensity to vote absent treatment). The [[Balance Table|balance table]] supports the validity of the [[Randomization|randomization]].

#### Regression Results: Effect of Assignment on Voting (%)

||(1)|(2)|(3)|(4)|(5)|(6)|
|---|---|---|---|---|---|---|
|Assigned to Treatment|-0.262|-0.156|-0.172|-0.340|-0.245|-0.241|
|SE|(0.411)|(0.401)|(0.401)|(0.366)|(0.359)|(0.359)|
|Controls|None|Age|+Female|+Vote00|+Vote98|+NewReg|
|Constant|51.00|20.27|21.29|5.747|8.078|6.703|
|N|1,168,044|1,168,044|1,167,495|1,167,495|1,167,495|1,167,495|

**Interpreting the constant (51.0)**: this is the average voting rate for the [[Control Group|control group]] — 51% of the control group voted in 2002.

**Effect of treatment**: approximately −0.2 to −0.3 percentage points across all specifications — essentially zero.

**Magnitude**: very small.

**[[Statistical Significance|Statistical significance]]**: the [[Standard Error|standard errors]] (~0.4) are larger than the coefficient (~0.26), so the effect is **not [[Statistical Significance|statistically significant]]**.

**Key insight for [[Internal Validity|internal validity]]**: the treatment coefficient is _stable_ as [[Control Variable|controls]] are added (ranging only from −0.156 to −0.340). This is exactly what we expect under successful [[Randomization|randomization]] — covariates are uncorrelated with treatment assignment, so adding them doesn't change the estimate much. It only improves [[Precision|precision]] by reducing residual variance.

---

### Part 2: Without Random Assignment (Self-Selection)

#### The Non-Experimental Comparison

Now instead of using `treat_real` (random assignment), we use `contact` — whether the person actually _answered the phone and heard the message_. This is **not random**. People who pick up the phone and engage with a get-out-the-vote call are making a choice.

> What type of person answers a call and listens to a voting encouragement message? → Likely already civic-minded, older, more habitual voters.

This is [[Self-Selection|self-selection]] into treatment, which introduces [[Selection Bias|selection bias]].

#### Balance Table: Self-Selected Contact vs. Random Assignment — Side by Side

**Randomly assigned (valid [[Counterfactual|counterfactual]])**:

|Variable|Control|Treatment|Difference|P-Value|
|---|---|---|---|---|
|Age|52.16|51.98|-0.18|0.2270|
|Voted 2000|56.37|56.72|0.35|0.3906|
|Voted 1998|23.14|22.68|-0.47|0.1767|
|New Voter|11.68|11.64|-0.04|0.8718|

**Chose to answer the call (invalid [[Counterfactual|counterfactual]])**:

|Variable|Didn't Get Call|Got Call|Difference|P-Value|
|---|---|---|---|---|
|Age|52.14|54.42|**2.28**|**0.0000**|
|Voted 2000|56.35|60.96|**4.61**|**0.0000**|
|Voted 1998|23.13|25.60|**2.47**|**0.0000**|
|New Voter|11.68|10.38|-1.30|**0.0027**|

The non-experimental groups are badly [[Balance Table|imbalanced]]. People who answered the call are older, more likely to have voted in 2000 and 1998, and less likely to be new voters. This strongly suggests their [[Potential Outcomes|baseline potential outcomes]] are higher — they were _already_ more likely to vote regardless of the call. This is [[Selection Bias|selection bias]] in action.

#### Regression Results: Effect of Answering the Call on Voting (%)

||(1)|(2)|(3)|(4)|(5)|(6)|
|---|---|---|---|---|---|---|
|contact|**5.509**|**4.167**|**4.164**|**2.605**|**2.495**|**2.486**|
|SE|(0.668)|(0.652)|(0.652)|(0.597)|(0.585)|(0.585)|
|Controls|None|Age|+Female|+Vote00|+Vote98|+NewReg|
|Constant|50.97|20.25|21.28|5.736|8.068|6.693|
|N|1,168,044|1,168,044|1,167,495|1,167,495|1,167,495|1,167,495|

**Effect of contact**: +5.5 percentage points baseline, falling to +2.5 after full controls. All estimates are [[Statistical Significance|statistically significant]].

**Adding which variable changes the coefficient most?** Adding `Voted 2000` (column 3→4) drives the contact coefficient from 4.164 to 2.605 — the largest single drop. This is because: (1) prior voting has a large effect on 2002 voting ($\beta_2$ is large: 41.82), and (2) people who answered the call were more likely to have voted in 2000 ($\delta_1 > 0$, as shown in the [[Balance Table|balance table]]). By the [[Variable Bias#OVB (Omitted Variable Bias)|OVB formula]], $\text{Bias} = \beta_2 \delta_1$ is large and positive — inflating the contact coefficient upward.

---

### The Core Comparison

||Experimental (`treat_real`)|Non-Experimental (`contact`)|
|---|---|---|
|Assignment|[[Randomization\|Random]]|[[Self-Selection\|Self-selected]]|
|[[Balance Table\|Balance]]|✅ All variables balanced|❌ Age, prior voting, new voter all imbalanced|
|Baseline coefficient|−0.26 pp|+5.51 pp|
|After full controls|−0.24 pp|+2.49 pp|
|[[Statistical Significance\|Stat. significant?]]|No|Yes|
|[[Causal Inference\|Causal interpretation]]|✅ Valid|❌ Biased upward|
|Coefficient stability w/ controls|Stable (as expected)|Falls substantially (reveals [[Variable Bias#OVB (Omitted Variable Bias)\|OVB]])|

**The non-experimental estimate overstates the effect of the call** because people who answered were already predisposed to vote. [[Selection on Observables|Adding controls]] reduces but does not eliminate the bias. The experimental estimate (near zero, insignificant) is likely the more credible causal estimate.

---

### Big Takeaways

> The same data, two treatment variables, two completely different answers — one credible, one not.

- [[RCT|Randomization]] produces [[Balance Table|balanced groups]] and a valid [[Counterfactual|counterfactual]], making [[Causal Effect|causal inference]] credible
- [[Self-Selection|Self-selection]] into treatment produces [[Selection Bias|selection bias]] — the "treated" group was different to begin with
- In an [[RCT]], adding [[Control Variable|controls]] barely changes the treatment estimate (stability = sign of good [[Randomization|randomization]])
- In a non-experiment, adding controls substantially shrinks the estimate — revealing the [[Variable Bias#OVB (Omitted Variable Bias)|omitted variable bias]] that was present
- [[Selection on Observables|Controlling for observables]] reduces but **cannot eliminate** bias from [[Selection on Unobservables|unobservables]] (e.g., civic motivation, which is unobserved but correlated with both answering the call and voting)
## L8 Instrumental Variables: An Introduction

Tags: #econ104 #instrumental-variables #causal-inference #noncompliance Related: [[L7 Experimental vs Non-Experimental Evidence]] · [[L6 Selection on Observables]] · [[Causal Inference]] · [[RCT]] · [[Identification Strategy]]

[[Selection on Observables|Regression adjustment]] cannot eliminate [[Variable Bias#OVB (Omitted Variable Bias)|bias]] from unobservables. [[RCT|Experiments]] are the gold standard but are not always feasible. [[Instrumental Variables|Instrumental variables (IV)]] is the first of three quasi-experimental [[Identification Strategy|identification strategies]] — alongside [[Regression Discontinuity|RDD]] and [[Difference-in-Differences|DiD]] — that can recover [[Causal Effect|causal estimates]] from [[Observational Data|observational data]] in the right setting. IV is particularly useful when we have an [[RCT]] with [[Noncompliance|noncompliance]].

---

### Motivation: The Noncompliance Problem

#### Setup

We want to estimate the causal effect of an intensive 5-hour tutoring session on student performance in Econ 113. The ideal approach is an [[RCT]]:

- Apply for [[IRB|Institutional Review Board (IRB)]] approval (required for human subjects research)
- Recruit 180 volunteers; randomly assign 90 to tutoring, 90 to control
- [[Randomization|Random assignment]] gives both groups the same [[Potential Outcomes|potential outcomes]] on average
- Unbiased [[Average Treatment Effect|ATE]] estimate: $E[\hat{\tau}] = E[\bar{Y}_T - \bar{Y}_C] = \tau$

#### What Goes Wrong: Noncompliance

Suppose 30 students (1/3) assigned to tutoring don't show up. Now:

- $\bar{Y}_T$ is the average grade of a group that is 2/3 treated and 1/3 untreated
- $\bar{Y}_C$ is the average grade of a fully untreated group
- $\bar{Y}_T - \bar{Y}_C \approx \frac{2}{3}\tau$ — **the naive difference-in-means _underestimates_ the true effect**

This is because the [[Noncompliance|noncompliers]] in the treatment group pull $\bar{Y}_T$ down toward the control mean.

#### Key Variable Distinction

[[Instrumental Variables|IV]] requires distinguishing two different variables:

|Variable|Symbol|Meaning|
|---|---|---|
|[[Treatment Assignment\|Assignment to treatment]]|$Z_i$|Was person $i$ _assigned_ to get the treatment? (the [[Instrumental Variables\|instrument]])|
|[[Treatment Receipt\|Actual treatment]]|$D_i$|Did person $i$ _actually_ receive the treatment?|

- $Z_i = 1$ assigned to treatment; $Z_i = 0$ assigned to control
- $D_i = 1$ got the treatment; $D_i = 0$ did not get the treatment

When there is perfect [[Noncompliance|compliance]], $Z_i = D_i$ for everyone. With noncompliance, they diverge.

---

### The Three-Stage IV Framework

[[Instrumental Variables|IV]] recovers the [[Treatment on the Treated|Treatment on the Treated (TOT)]] effect by working through three stages:

1. **[[Instrumental Variables#Reduced Form|Reduced form]]**: compare outcomes by _assignment_ (ignoring compliance) → [[Intention to Treat|ITT]]
2. **[[Instrumental Variables#First Stage|First stage]]**: estimate how much _assignment_ changes actual _receipt_ of treatment → compliance rate
3. **[[Instrumental Variables|IV estimate]]**: divide reduced form by first stage → [[Treatment on the Treated|TOT]]

---

### Stage 1: Reduced Form

#### Definition

The **[[Instrumental Variables#Reduced Form|reduced form]]** is the raw difference in outcomes between the group _assigned_ to treatment and the group _assigned_ to control:

$$RF = \bar{Y}_T - \bar{Y}_C = Avg_n[Y_i | Z_i = 1] - Avg_n[Y_i | Z_i = 0]$$

This is also called the **[[Intention to Treat|Intention to Treat (ITT)]]** estimate — it measures the effect of the _intention_ to treat, not the effect of the treatment itself. It is called ITT because some people assigned to treatment never actually received it.

#### Estimated via Regression

$$Y_i = \pi_0 + \pi_1 Z_i + \varepsilon_i$$

$\hat{\pi}_1$ is the [[Instrumental Variables#Reduced Form|reduced form]] / [[Intention to Treat|ITT]] estimate. [[Regression|Regression]] is preferred in practice because it allows [[Control Variable|covariates]] to be added easily.

#### Why the Reduced Form Underestimates $\tau$

Assuming [[Constant Treatment Effect|constant treatment effect]] $\tau$ (so $Y_{1i} = Y_{0i} + \tau$) and 2/3 compliance:

$$Avg_n[Y_i|Z_i=1] - Avg_n[Y_i|Z_i=0] \approx \frac{2}{3}\tau$$

The [[Randomization|random assignment]] means the baseline potential outcomes cancel (as the sample grows large), leaving only $\frac{2}{3}\tau$. If _no one_ assigned to treatment showed up, the reduced form would be 0 — because assignment would have had zero effect on outcomes.

---

### Stage 2: First Stage

#### Definition

The **[[Instrumental Variables#First Stage|first stage]]** is the effect of _assignment_ ($Z_i$) on _actual receipt_ of treatment ($D_i$):

$$\text{First Stage} = Avg_n[D_i|Z_i=1] - Avg_n[D_i|Z_i=0]$$

This measures how much being assigned to treatment increases the probability of actually receiving it — i.e., the [[Compliance Rate|compliance rate]] induced by the [[Instrumental Variables|instrument]].

#### Estimated via Regression

$$D_i = \phi_0 + \phi_1 Z_i + \varepsilon_i$$

$\hat{\phi}_1$ is the [[Instrumental Variables#First Stage|first stage]] estimate. It should be [[Statistical Significance|statistically significant]] — a weak first stage is a serious problem (called a [[Weak Instrument|weak instrument]]).

#### Numerical Examples

No control-group contamination, 2/3 treatment compliance: $$\hat{D}_i = 0.000 + 0.667 Z_i \quad \Rightarrow \quad \text{First Stage} = \frac{2}{3}$$

1/4 of controls also get treatment, 3/4 of treatment group comply: $$\hat{D}_i = 0.250 + 0.500 Z_i \quad \Rightarrow \quad \text{First Stage} = \frac{3}{4} - \frac{1}{4} = \frac{1}{2}$$

---

### Stage 3: The IV Estimate

#### The Formula

The **[[Instrumental Variables|IV estimator]]** recovers the [[Treatment on the Treated|TOT]] by scaling the [[Instrumental Variables#Reduced Form|reduced form]] by the [[Instrumental Variables#First Stage|first stage]]:

$$\boxed{\hat{\tau}_{IV} = \frac{\text{Reduced Form}}{\text{First Stage}} = \frac{Avg_n[Y_i|Z_i=1] - Avg_n[Y_i|Z_i=0]}{Avg_n[D_i|Z_i=1] - Avg_n[D_i|Z_i=0]}}$$

Applied to the tutoring example:

$$\hat{\tau}_{IV} = \frac{\frac{2}{3}\tau}{\frac{2}{3}} = \tau$$

Dividing by the [[Instrumental Variables#First Stage|first stage]] puts the [[Instrumental Variables#Reduced Form|reduced form]] estimate in _per-treated-person_ terms, recovering the true [[Treatment on the Treated|TOT]] effect.

#### Perfect Compliance as a Special Case

If everyone assigned to treatment receives it and no one in control does, then:

- First Stage = 1
- $\hat{\tau}_{IV} = \frac{RF}{1} = RF = \bar{Y}_T - \bar{Y}_C$

The IV estimate collapses to the simple [[Difference in Means|difference in means]] — which is just the standard [[RCT]] estimator. IV is the generalization that handles imperfect compliance.

---

### Worked Example: IT Training

100 unemployed workers randomly assigned to IT training, 100 to control. Only 1/2 of those assigned to training actually attend. One year later, the assigned-to-training group earns $2/hour more on average.

|Component|Value|Interpretation|
|---|---|---|
|$Y_i$|Hourly wage one year later|[[Outcome Variable\|Outcome]]|
|$Z_i$|Randomly assigned to training|[[Instrumental Variables\|Instrument]] / assignment|
|$D_i$|Actually attended training|[[Treatment Receipt\|Treatment receipt]]|
|[[Instrumental Variables#Reduced Form\|Reduced Form]]|$2/hour|Effect of _assignment_ on wages ([[Intention to Treat\|ITT]])|
|[[Instrumental Variables#First Stage\|First Stage]]|$1/2 - 0 = 1/2$|Assignment raises training take-up by 50 pp|
|$\hat{\tau}_{IV}$|$2 \div \frac{1}{2} = $4/\text{hour}$|[[Treatment on the Treated\|TOT]]: effect on those who actually trained|

The $2 [[Intention to Treat|ITT]] understates the true effect because half the assigned group never trained. Scaling up by $1/\frac{1}{2} = 2$ gives ${4} dollars /hour$ — the [[Treatment on the Treated|TOT]] for those who complied.

---

### Big Takeaways

> [[Instrumental Variables|IV]] turns an [[Intention to Treat|ITT]] estimate into a [[Treatment on the Treated|TOT]] estimate by accounting for imperfect [[Compliance Rate|compliance]].

- The [[Instrumental Variables|instrument]] $Z_i$ is the [[Treatment Assignment|random assignment]] — it shifts $D_i$ but is unrelated to [[Potential Outcomes|potential outcomes]] (by [[Randomization|randomization]])
- [[Instrumental Variables#Reduced Form|Reduced form]] = effect of instrument on outcome ([[Intention to Treat|ITT]])
- [[Instrumental Variables#First Stage|First stage]] = effect of instrument on treatment receipt ([[Compliance Rate|compliance]])
- $\hat{\tau}_{IV} = RF / \text{FS}$ = [[Treatment on the Treated|TOT]], in per-treated-person terms
- When compliance is perfect, IV = simple [[Difference in Means|difference in means]]
- A [[Weak Instrument|weak first stage]] (instrument barely affects treatment receipt) inflates the IV estimate and its [[Standard Error|standard errors]] — always check first stage [[Statistical Significance|significance]]
# Week 5
## L9 Instrumental Variables: Intuition and Assumptions

Tags: #econ104 #instrumental-variables #causal-inference #LATE Related: [[L8 Instrumental Variables]] · [[Instrumental Variables]] · [[Causal Inference]] · [[Average Treatment Effect]] · [[Potential Outcomes]]

This lesson deepens the L8 mechanics by working through the [[Chain of Causation|causal chain]] underlying [[Instrumental Variables|IV]], formalizing its two key assumptions, and introducing the [[Local Average Treatment Effect|LATE]] — the specific population whose treatment effect IV actually recovers.

---

### Worked Example: Blood Pressure Medication

200 high-blood-pressure patients; 100 randomly assigned to take a pill, 100 to control. Of those assigned the pill, 70 take it and 30 refuse. No control patients have access. After one week: assigned-to-pill group averages BP = 142; control group averages BP = 148.

|Component|Calculation|Value|Interpretation|
|---|---|---|---|
|$Y_i$|Blood pressure after experiment|—|[[Outcome Variable\|Outcome]]|
|$Z_i$|Random assignment to pill|—|[[Instrumental Variables\|Instrument]]|
|$D_i$|Actually took the pill|—|[[Treatment Receipt\|Treatment receipt]]|
|[[Instrumental Variables#First Stage\|First Stage]]|$70/100 - 0/100$|**0.70**|Assignment raises pill-taking by 70 pp|
|[[Instrumental Variables#Reduced Form\|Reduced Form]] / [[Intention to Treat\|ITT]]|$142 - 148$|**−6.0**|Assignment lowers BP by 6 points|
|$\hat{\tau}_{IV}$|$-6.0 / 0.70$|**−8.6**|Pill lowers BP by 8.6 points for [[Compliers\|compliers]]|

The [[Intention to Treat|ITT]] (−6) understates the pill's effect because 30% of the assigned-to-pill group never took it. Scaling up recovers the [[Treatment on the Treated|TOT]] / [[Local Average Treatment Effect|LATE]] of −8.6.

---

### Chain of Causation

The key intuition: if the [[Instrumental Variables|instrument]] $Z$ affects the [[Outcome Variable|outcome]] $Y$ **only through** the [[Treatment Receipt|treatment]] $D$, then there are two ways to express the path from $Z$ to $Y$:

$$Z \xrightarrow{\text{First Stage}} D \xrightarrow{\text{Treatment Effect}} Y$$

$$Z \xrightarrow{\text{Reduced Form}} Y$$

Equating them:

$$\text{First Stage} \times \text{Treatment Effect} = \text{Reduced Form}$$

$$\boxed{\text{Treatment Effect} = \frac{\text{Reduced Form}}{\text{First Stage}}}$$

This is the [[Instrumental Variables|IV estimator]]. The logic depends entirely on the [[Exclusion Restriction|exclusion restriction]] — the assumption that $Z$ reaches $Y$ _only_ through the single path via $D$.

---

### IV Assumptions

For [[Instrumental Variables|IV]] to produce a consistent [[Causal Effect|causal estimate]], two formal assumptions must hold.

#### Assumption 1: Inclusion Restriction (First Stage ≠ 0)

> The instrument $Z$ must have a meaningful effect on the treatment $D$.

Formally: $\hat{\phi}_1 \neq 0$ in the regression $D_i = \phi_0 + \phi_1 Z_i + \varepsilon_i$.

This is required because the [[Instrumental Variables|IV estimator]] divides by the [[Instrumental Variables#First Stage|first stage]] — dividing by zero is undefined. If $Z$ doesn't affect $D$ at all, there is no difference between treatment and control groups in treatment rates, so there is nothing to compare.

**Testable**: Run the [[Instrumental Variables#First Stage|first stage regression]] and check [[Statistical Significance|statistical significance]] of $\hat{\phi}_1$. In the blood pressure example: First Stage = 0.70, clearly non-zero.

A related problem is the [[Weak Instrument|weak instrument]] — where the first stage is statistically significant but small. A weak first stage inflates the [[Instrumental Variables|IV]] estimate and its [[Standard Error|standard errors]], making estimates unreliable.

#### Assumption 2: Exclusion Restriction

> The instrument $Z$ affects the outcome $Y$ **only through** $D$ — not through any other channel.

Formally: $Z$ is uncorrelated with the [[Error Term|error term]] $u$ in the structural equation $Y = \pi_0 + \pi_1 D_i + u$.

**Valid path**: $Z \rightarrow D \rightarrow Y$

**Violation**: $Z \rightarrow D \rightarrow Y$ AND $Z \rightarrow D_2 \rightarrow Y$ (instrument opens a second channel to $Y$)

**Example of a violation**: If being _told_ to take the blood pressure pill also causes patients to start exercising and eating better, then the [[Instrumental Variables#Reduced Form|reduced form]] picks up all three effects:

$$\frac{RF}{FS} = \tau + \frac{FS_2 \cdot \tau_{EB} + FS_3 \cdot \tau_{EX}}{FS} = \tau + \text{bias}$$

The [[Exclusion Restriction|exclusion restriction]] cannot be tested directly from the data — it must be argued on [[Internal Validity|theoretical/design grounds]]. It is one of the most important and most debated assumptions in applied econometrics.

---

### Local Average Treatment Effect (LATE)

#### Why IV ≠ ATE

The [[Average Treatment Effect|ATE]] is the average treatment effect across the _entire population_. Recovering the ATE requires a representative sample, random assignment, and **full compliance**. [[Instrumental Variables|IV]] doesn't give us this — it gives us something more limited.

Even with a perfectly representative sample, the people who _comply_ with their assignment may be systematically different from those who don't. [[Instrumental Variables|IV]] identifies the treatment effect only for the people whose behavior was actually _changed_ by the instrument.

#### The Four Compliance Types

With binary $Z$ and binary $D$, every person falls into one of four types:

|Type|If assigned ($Z=1$)|If not assigned ($Z=0$)|Proportion|
|---|---|---|---|
|**[[Compliers\|Complier]]**|Takes treatment ($D=1$)|Doesn't take ($D=0$)|$P_C$|
|**[[Never Takers\|Never Taker]]**|Doesn't take ($D=0$)|Doesn't take ($D=0$)|$P_{NT}$|
|**[[Always Takers\|Always Taker]]**|Takes treatment ($D=1$)|Takes treatment ($D=1$)|$P_{AT}$|
|**[[Defiers\|Defier]]**|Doesn't take ($D=0$)|Takes treatment ($D=1$)|$P_D$|

**Defiers** are assumed not to exist ([[Monotonicity Assumption|monotonicity assumption]]). This is not merely assuming non-compliance — defiers would have to _actively do the opposite_ of what the instrument directs, which is an extreme and implausible behavior.

**Which groups are affected by assignment?** Only [[Compliers|Compliers]] and [[Defiers|Defiers]] change their behavior based on $Z$. [[Always Takers|Always takers]] and [[Never Takers|never takers]] behave the same regardless of assignment.

#### Why We Can't Estimate ATE for Always/Never Takers

- **[[Always Takers|Always takers]]**: take the treatment in _both_ groups — we never observe their untreated outcome $Y_{0i}$, so we cannot form the counterfactual
- **[[Never Takers|Never takers]]**: never take the treatment in _either_ group — we never observe their treated outcome $Y_{1i}$

Without variation in $D$ induced by $Z$ for these groups, the instrument provides no information about their [[Causal Effect|treatment effects]].

#### The LATE Derivation

Working through the math (with no [[Defiers|defiers]], $P_D = 0$):

$$E[RF] = E[Y_i|Z_i=1] - E[Y_i|Z_i=0]$$

Always takers contribute $E[Y_{1i}|AT]$ to both sides — they cancel. Never takers contribute $E[Y_{0i}|NT]$ to both sides — they cancel. Only [[Compliers|compliers]] contribute differently:

$$E[RF] = P_C \cdot E[Y_{1i} - Y_{0i} | C] = P_C \cdot E[\tau_i | C]$$

The [[Instrumental Variables#First Stage|first stage]] equals $P_C$ (the proportion of compliers, since no defiers). Therefore:

$$\tau_{IV} = \frac{RF}{FS} = \frac{P_C \cdot E[\tau_i|C]}{P_C} = E[\tau_i|C]$$

$$\boxed{\tau_{IV} = LATE = E[\tau_i | \text{Complier}]}$$

#### Blood Pressure Application

- **[[Always Takers|Always takers]]**: None — the control group has no access to the pill, so no one in the control group can take it; any always-taker assigned to control couldn't comply
- **[[Never Takers|Never takers]]**: The 30 patients assigned to treatment who refused the pill — people who won't take the medication regardless
- Can we estimate the treatment effect for never takers? **No** — we never observe them in a treated state
- Are never takers likely to have a larger or smaller effect than compliers? Likely **smaller** — people who refuse medication may be doing so because they believe it won't work for them, or because they are already managing blood pressure through other means

---

### Big Takeaways

> [[Instrumental Variables|IV]] doesn't give us the ATE for everyone — it gives us the LATE for the _compliers_. This is both a limitation and a precision.

- The [[Exclusion Restriction|exclusion restriction]] is the critical, untestable assumption: $Z$ must affect $Y$ only through $D$. Violations cause bias that looks just like a valid IV estimate
- The [[Instrumental Variables#First Stage|inclusion restriction]] is testable: run the [[Instrumental Variables#First Stage|first stage]] and check significance — always report it
- [[Compliers|Compliers]] are the "marginal" group whose behavior the instrument actually shifts; they may not be representative of the broader population
- $LATE \neq ATE$ when [[Treatment Effect Heterogeneity|treatment effects are heterogeneous]] across compliance types
- [[Monotonicity Assumption|Monotonicity]] (no [[Defiers|defiers]]) is the third implicit assumption needed for the LATE interpretation to hold
## L10 Instrumental Variables: Two-Stage Least Squares

Tags: #econ104 #instrumental-variables #2SLS #causal-inference #LATE Related: [[L9 Instrumental Variables]] · [[Instrumental Variables]] · [[Two-Stage Least Squares]] · [[Local Average Treatment Effect]] · [[Regression Adjustment]]

This lesson builds on L9 by introducing [[Two-Stage Least Squares|2SLS]] as a general method for estimating [[Instrumental Variables|IV]], extending it to multiple instruments and controls, and connecting IV back to the voting experiment to align it with the regression adjustment benchmark.

---

### IV: Overview

Recap of [[Instrumental Variables|IV]] as scaling:

|Component|Description|
|---|---|
|[[Instrumental Variables#First Stage\|First Stage]]|Effect of instrument $Z$ on treatment $D$|
|[[Instrumental Variables#Reduced Form\|Reduced Form]]|Effect of instrument $Z$ on outcome $Y$|
|$\hat{\tau}_{IV}$|$RF / FS$ — scales up to estimate the treatment effect|

**Important considerations:**

- The [[Instrumental Variables#Reduced Form|reduced form]] estimates the [[Intention to Treat|ITT]]
- The scaled IV estimates the [[Local Average Treatment Effect|LATE]]
- [[Local Average Treatment Effect|LATE]] is the average treatment effect for [[Compliers|compliers]] — not the true [[Average Treatment Effect|ATE]]
- Requires the [[Exclusion Restriction|exclusion restriction]]: $Z$ only affects $Y$ through $D$

---

### ITT, ATE, and LATE in the Voting Experiment

|Estimand|Description|
|---|---|
|[[Intention to Treat\|ITT]]|Effect of being _assigned_ to receive a voting call|
|[[Average Treatment Effect\|ATE]]|Effect of actually getting a call, averaged over the full population|
|[[Local Average Treatment Effect\|LATE]]|Effect of actually getting a call, for [[Compliers\|compliers]] only|

**A fundamental comparison issue:**

- The [[Randomized Controlled Trial|RCT]] estimates the [[Intention to Treat|ITT]] — it compares assigned-to-treatment vs. control
- [[Regression Adjustment|Regression adjustment]] (conditioning on observables) compares those who _actually_ got a call vs. those who did not → biased [[Local Average Treatment Effect|LATE]]
- These two estimates are not directly comparable — they measure different things

**What we need:** The [[Instrumental Variables|IV]] estimate from the experiment. This gives the [[Local Average Treatment Effect|LATE]] — the effect of actually getting a call for [[Compliers|compliers]]. Now the IV estimate and the regression adjustment estimate are both trying to measure the same quantity and can be directly compared.

---

### Two-Stage Least Squares (2SLS)

[[Two-Stage Least Squares|2SLS]] is another implementation of [[Instrumental Variables|IV]]. Instead of scaling $RF/FS$ directly, it:

1. Estimates the [[Instrumental Variables#First Stage|first stage]] to get a predicted likelihood of treatment $\hat{D}_i$
2. Uses $\hat{D}_i$ as the explanatory variable in a second-stage regression on $Y$

#### Basic 2SLS (No Controls, One Instrument)

**First stage:**

$$D_i = \phi_0 + \phi_1 Z_{1i} + u_i$$

**Predicted treatment:**

$$\hat{D}_i = \hat{\phi}_0 + \hat{\phi}_1 Z_{1i}$$

**Second stage:**

$$Y_i = \lambda_0 + \lambda_{2SLS} \hat{D}_i + \varepsilon_i$$

The coefficient $\lambda_{2SLS}$ is the [[Two-Stage Least Squares|2SLS]] instrumental variables estimate ([[Local Average Treatment Effect|LATE]]).

---

#### Adding Control Variables

**First stage with controls:**

$$D_i = \phi_0 + \phi_1 Z_{1i} + \gamma_1 X_i + u_i$$

**Predicted treatment:**

$$\hat{D}_i = \hat{\phi}_0 + \hat{\phi}_1 Z_{1i} + \hat{\gamma}_1 X_i$$

**Second stage with controls:**

$$Y_i = \lambda_0 + \lambda_{2SLS} \hat{D}_i + \gamma_2 X_i + \varepsilon_i$$

The second stage exploits only the variation in $D$ generated by the instrument — "good variation" — while controlling for confounders $X$.

---

#### 2SLS = IV (with One Instrument)

With a single instrument $Z$, 2SLS and IV are algebraically identical:

$$\hat{\lambda}_{IV} = \frac{\hat{\pi}_1}{\hat{\phi}_1} = \frac{Cov(Y,Z)/Var(Z)}{Cov(D,Z)/Var(Z)} = \frac{Cov(Y,Z)}{Cov(D,Z)}$$

$$\hat{\lambda}_{2SLS} = \frac{Cov(Y, \hat{D}_i)}{Var(\hat{D}_i)} = \frac{\hat{\phi}_1 Cov(Y,Z)}{\hat{\phi}_1^2 Var(Z)} = \frac{\hat{\pi}_1}{\hat{\phi}_1} = \hat{\lambda}_{IV}$$

> This equivalence holds for the voting experiment.

---

#### Multiple Instruments

When there are multiple instruments (e.g., multiple treatment arms), the ratio approach $RF/FS$ does not work. [[Two-Stage Least Squares|2SLS]] generalizes naturally:

**Example:** To induce students to attend tutoring, two separate instruments are used — offering tutoring, and _paying_ students to attend.

**First stage with two instruments:**

$$D_i = \phi_0 + \phi_1 Z_{1i} + \phi_2 Z_{2i} + u_i$$

**Predicted treatment:**

$$\hat{D}_i = \hat{\phi}_0 + \hat{\phi}_1 Z_{1i} + \hat{\phi}_2 Z_{2i}$$

**Second stage:**

$$Y_i = \lambda_0 + \lambda_{2SLS} \hat{D}_i + \varepsilon_i$$

The second stage now exploits variation in $D$ generated by _both_ instruments simultaneously.

---

### Weak First Stage and Bias Inflation

A [[Weak Instrument|weak first stage]] (small $FS$) inflates bias in the [[Instrumental Variables|IV]] estimate. If the [[Instrumental Variables#Reduced Form|reduced form]] contains any bias (e.g., from differential attrition):

$$\hat{\tau}_{IV} = \frac{\widehat{RF}}{\widehat{FS}} = \frac{RF + \text{bias}}{FS} = \frac{RF}{FS} + \frac{\text{bias}}{FS}$$

A small $FS$ in the denominator magnifies even small amounts of reduced-form bias — this is why always reporting and checking the [[Instrumental Variables#First Stage|first stage]] is critical.

---

### 2SLS in Stata

```stata
* Basic 2SLS (Y = outcome, D = treatment, Z = instrument)
ivregress 2sls Y (D = Z)

* With control variables X
ivregress 2sls Y X (D = Z)
```

Stata directly outputs the second-stage IV estimate — no manual scaling required.

**For the voting RCT:**

|Variable|Role|
|---|---|
|$Y$|Voting outcome|
|$D$|Actually received a call|
|$Z$|Random assignment to receive a call|

---

### 2SLS Example 1: KIPP Charter Schools

**Research question:** Effect of charter school attendance on test scores. Admission is determined by lottery.

|Variable|Description|
|---|---|
|Treatment $D$|Years attending charter school|
|Instrument $Z$|Winning lottery to attend the school|
|Outcome $Y$|Test scores (standard deviations)|

**Results (Table 2: Lottery Results):**

||First Stage (1)|Reduced Form (2)|2SLS (3)|
|---|---|---|---|
|_Panel A: Math_||||
|Basic|1.222*** (0.063)|0.431*** (0.116)|0.353*** (0.095)|
|Demographics & baseline|1.228*** (0.066)|0.425*** (0.066)|0.346*** (0.052)|
|_Panel B: ELA_||||
|Basic|1.223*** (0.063)|0.183 (0.117)|0.150 (0.094)|
|Demographics & baseline|1.234*** (0.066)|0.149** (0.073)|0.120** (0.058)|

_Notes: Robust standard errors clustered at the student level. N=856 with baseline scores._

**Interpreting the relationship:**

- **First stage** (~1.22): Winning the lottery increases years of charter attendance by ~1.2 years
- **Reduced form** (0.431 for math): Winning the lottery raises math scores by 0.43 SD
- **2SLS** (0.353 for math): Each additional year at a KIPP school raises math scores by ~0.35 SD
- Verify: $0.431 / 1.222 \approx 0.353$ ✓ — confirms $2SLS = RF / FS$

---

### 2SLS Example 2: Family Size and Children's Education

**Research question:** Does having more children (quantity) reduce each child's educational attainment (quality)? The quantity–quality tradeoff.

|Variable|Description|
|---|---|
|Treatment $D$|Number of children|
|Instruments $Z$|Having twins; gender of first two children (same-sex)|
|Outcomes $Y$|Years of schooling, high school graduation, college attendance|

**Results (OLS vs. 2SLS):**

|Dependent Variable|OLS (1)|Twins (2)|Same-sex (3)|Twins + Same-sex (4)|
|---|---|---|---|---|
|Years of schooling|−0.145 (0.005)|0.174 (0.166)|0.318 (0.210)|0.237 (0.128)|
|High school graduate|−0.029 (0.001)|0.030 (0.028)|0.001 (0.033)|0.017 (0.021)|
|Some college (age ≥ 24)|−0.023 (0.001)|0.017 (0.052)|0.078 (0.054)|0.048 (0.037)|
|College graduate (age ≥ 24)|−0.015 (0.001)|−0.021 (0.045)|0.125 (0.053)|0.052 (0.032)|

**Why do OLS and 2SLS differ so much?**

- **OLS** shows a negative relationship: larger families → lower educational attainment. But this is driven by [[Selection Bias|selection bias]] — families who choose to have more children differ systematically (lower income, lower education) from those who don't
- **2SLS** uses only _exogenous_ variation in family size (twin births, same-sex sibling composition) — variation that is effectively random
- Once selection bias is removed, the quantity–quality tradeoff largely disappears or even reverses — suggesting OLS was confounded by background characteristics correlated with both family size and child outcomes

---

### Big Takeaways

> [[Two-Stage Least Squares|2SLS]] is the standard implementation of [[Instrumental Variables|IV]]. It generalizes naturally to multiple instruments and controls, and equals $RF/FS$ with one instrument.

- The [[Instrumental Variables#First Stage|first stage]] must be strong — always report it and check significance
- [[Weak Instrument|Weak instruments]] amplify any bias present in the [[Instrumental Variables#Reduced Form|reduced form]]
- 2SLS and simple IV scaling are identical with a single instrument — Stata's `ivregress 2sls` handles this automatically
- The voting experiment IV estimate ([[Local Average Treatment Effect|LATE]]) is now directly comparable to the regression adjustment estimate — both target the effect of _actually_ receiving a call
- OLS vs. 2SLS differences (as in the family size example) reveal the magnitude and direction of [[Selection Bias|selection bias]] in observational estimates
# Week 6
## L11 Regression Discontinuity: An Introduction

Tags: #econ104 #regression-discontinuity #causal-inference #LATE #health-insurance #drinking-crime Related: [[L10 Instrumental Variables]] · [[Regression Discontinuity]] · [[Running Variable]] · [[Cutoff]] · [[Local Average Treatment Effect]] · [[Intention to Treat]] · [[Instrumental Variables]]

This lesson introduces [[Regression Discontinuity|RD]] as a strategy for causal identification when treatment is determined by a sharp cutoff in a continuous variable. Two empirical examples are developed: the effect of health insurance on medical debt (Medicare at age 65) and the effect of alcohol on violent crime (minimum legal drinking age at 21).

---

### The Fundamental Challenge

Without [[Randomized Controlled Trial|randomization]], getting causal estimates is challenging because:

- The individual treatment effect is the difference between [[Potential Outcomes|potential outcomes]] in the treated and untreated state
- People who _choose_ to get treatment are typically different from those who do not — in both their untreated baseline outcomes and in how much they benefit from treatment
- These differences stem from [[Omitted Variable Bias|unobserved factors]] that cause [[Selection Bias|selection bias]] in regression analysis

> To get causal estimates we need a source of variation in the probability of treatment that is **not due to individual choice**.

---

### Regression Discontinuity: Core Idea

**[[Regression Discontinuity|Regression Discontinuity (RD)]]** designs leverage variation from sharp cutoffs that determine who gets a treatment.

- If treatment assignment is based on a cutoff in a [[Running Variable|continuous running variable]] $X$, this induces a **discontinuity** in the probability of treatment at the threshold $c$
- We compare people just above and just below the cutoff — they are likely very similar in observable _and_ unobservable characteristics, but differ in treatment probability
- By examining outcomes on either side of the cutoff, we can identify the causal effect of treatment

---

### RD vs. RCT: Comparison

|Dimension|RCT|RD|
|---|---|---|
|**Randomization**|Random assignment creates exogenous variation|The cutoff creates "as-good-as-random" variation near the threshold|
|**Compliance**|Non-compliance possible → use IV/LATE|Non-compliance possible → can use fuzzy RD / IV approach|
|**Balance**|Balance holds across the full sample|Balance holds only _locally_ near the cutoff — not globally|
|**Population affected**|Entire sample|Only people near the cutoff (a local estimate)|

---

### RD Example 1: Health Insurance and Medical Debt

**Research question:** Does having health insurance protect people from the financial impact of illness?

**Why OLS/regression adjustment fails:** People who choose to get insurance are systematically different from those who don't — likely wealthier, healthier, and better at managing finances. Any comparison without a causal design will be biased (probably downward, since insured people tend to be better off).

**Why an RCT is hard:** Ethically and practically difficult to randomly withhold insurance from people.

#### The RD Design: Medicare at Age 65

- At age 65, individuals become eligible for [[Medicare]]
- This creates a **sharp discontinuity** in the probability of insurance coverage that is not driven by individual choice
- Comparing people just over and just under 65 gives a valid causal comparison — they should be similar on all dimensions except insurance status

**Data:** California hospital data linked to financial records.

|Variable|Role|
|---|---|
|Running variable $X$|Age at hospitalization|
|Cutoff $c$|Age 65|
|Instrument $Z$|Turning 65 (above cutoff)|
|Treatment $D$|Having insurance|
|Outcome $Y$|Collection balances (medical debt)|

#### First Stage: Effect of Turning 65 on Insurance

- RD estimate = **−0.057** (SE = 0.0023)
- Turning 65 reduces the probability of being uninsured at hospitalization by **5.7 percentage points**
- The first stage is large and clearly significant — a strong instrument

_Interpretation:_ People just over 65 are 5.7 pp less likely to be uninsured at an ER admission than those just under 65. This is the [[Instrumental Variables#First Stage|first stage]].

#### Reduced Form: Effect of Turning 65 on Collection Balances

- RD estimate = **−$451** (SE = 99)
- Turning 65 reduces outstanding collection balances by $451

_Interpretation:_ People just over 65 carry $451 less in medical debt collections than those just under 65. Unless there are other sharp changes at 65, this is driven by the insurance change. This is the [[Instrumental Variables#Reduced Form|reduced form]].

#### IV Estimate: Effect of Insurance on Collection Balances

$$\hat{\tau}_{unins} = \frac{\widehat{RF}}{\widehat{FS}} = \frac{-$451}{-0.057} = $7{,}912$$

Having insurance **reduces** collection balances by approximately **$7,912** for compliers.

**Who are the compliers?** People near age 65 who gained insurance specifically because of Medicare eligibility — those who were uninsured just before 65 and became insured just after. This is a [[Local Average Treatment Effect|LATE]], not an [[Average Treatment Effect|ATE]].

---

### RD Example 2: Drinking and Violent Crime

**Research question:** Does drinking cause violent crime?

**Why OLS fails:** People who choose to drink are likely different from those who don't (age, social environment, risk tolerance). Comparison would be biased upward.

**Why an RCT is hard:** Ethically impossible to randomly assign alcohol consumption and monitor criminal activity.

#### The RD Design: Minimum Legal Drinking Age at 21

- At age 21, individuals are legally permitted to drink
- This creates a **sharp change** in the probability of drinking that is not due to individual choice
- Comparing people just over and just under 21 isolates the causal effect of drinking on crime

**Data:** California Health Interview Survey (drinking) + California Department of Justice (arrest data).

|Variable|Role|
|---|---|
|Running variable $X$|Age|
|Cutoff $c$|Age 21|
|Instrument $Z$|Turning 21 (above cutoff)|
|Treatment $D$|Drinking|
|Outcome $Y$|Violent crime arrest rate (per 10,000)|

#### First Stage: Effect of Turning 21 on Drinking

- RD estimate (Beta) = **0.198** (SE = 0.039)
- Turning 21 increases the proportion who drank in the last month by **19.8 percentage points**
- Strong, statistically significant first stage

_Interpretation:_ People just over 21 are ~20 pp more likely to have drunk in the past month than those just under 21 — driven by legal access, not individual choice.

#### Reduced Form: Effect of Turning 21 on Violent Crime Arrests

- RD estimate (Beta) = **12.5** (SE = 1.17)
- Turning 21 increases violent crime arrest rates by **12.5 per 10,000**

_Interpretation:_ Unless there are other sharp changes at 21, this increase in arrests is caused by the change in drinking behavior.

#### IV Estimate: Effect of Drinking on Arrest Rate

$$\hat{\tau}_{ins} = \frac{\widehat{RF}}{\widehat{FS}} = \frac{12.5}{0.198} = 63.1$$

Drinking causes a **63.1 per 10,000** increase in violent crime arrests — approximately a **0.63 percentage point** increase in the probability of arrest for a violent crime.

**Who are the compliers?** People near age 21 who started drinking specifically because they turned 21 — those who were not drinking just before 21 and started after. This [[Local Average Treatment Effect|LATE]] may not generalize to all drinkers.

**Concerns about other causal channels:** Turning 21 may bring other behavioral changes (e.g., more time in bars, different social environments) that independently affect crime — a potential [[Exclusion Restriction|exclusion restriction]] violation.

---

### Big Takeaways

> [[Regression Discontinuity|RD]] exploits sharp cutoffs in a running variable to mimic randomization near the threshold. Like [[Instrumental Variables|IV]], the RD estimate is a [[Local Average Treatment Effect|LATE]] for compliers near the cutoff — not an [[Average Treatment Effect|ATE]] for the full population.

- RD is valid when people near the cutoff are comparable on all dimensions except treatment status
- The [[Instrumental Variables#First Stage|first stage]] (effect of crossing the cutoff on treatment) must be strong
- The [[Exclusion Restriction|exclusion restriction]] requires that crossing the cutoff affects the outcome _only_ through the treatment — other sharp changes at the cutoff would invalidate the design
- The population of inference is narrow: compliers near the threshold
- RD produces graphs that visually reveal both the first stage and reduced form — always plot the data
## L12 Regression Discontinuity: Regression Specifications

Tags: #econ104 #regression-discontinuity #specification #balance #running-variable #polynomial Related: [[L11 Regression Discontinuity]] · [[Regression Discontinuity]] · [[Running Variable]] · [[Bandwidth]] · [[Continuity Assumption]] · [[Balance Test]] · [[Density Test]]

This lesson develops the formal regression machinery for [[Regression Discontinuity|RD]], covering bandwidth choice, polynomial order selection, and how to validate the design through balance graphs, balance tables, and density tests.

---

### Setting Up the RD Regression

The goal of an RD regression is to formally estimate the size of the discontinuity at the cutoff and test for [[Statistical Significance|statistical significance]]. The parametric approach requires two key choices:

1. **[[Bandwidth|Bandwidth]]**: the range of $X$ values on either side of the cutoff $c$ to include in the analysis
2. **Polynomial order**: the functional form used to model the relationship between $X$ and $Y$ on each side

---

### Choosing the Bandwidth

- Pick a window centered at the cutoff $c$ and extend it far enough to see the relationship clearly
- The bandwidth should **not** include other discontinuities (e.g., in the drinking example, age 18 is another legal threshold — the bandwidth should stay within ~2 years of 21 to avoid including it)
- Narrower bandwidth → more comparable groups, but less data and more noise
- Wider bandwidth → more data, but groups may differ more and functional form assumptions matter more

**Example:** For the minimum legal drinking age study, restricting to ages 19–23 (within 2 years of 21) keeps the sample close to the cutoff while avoiding the age-18 discontinuity.

---

### The Linear RD Regression

The simplest specification fits a **separate line** on each side of the cutoff:

$$Drink_i = \beta_0 + \beta_1 Z_i + \beta_2 Age_i + \beta_3 Age_i * Z_i + u_i$$

Where:

- $Z_i = 1$ if $X_i \geq c$ (at or above the cutoff), 0 otherwise
- $Age_i$ is **centered at $c$** (i.e., age 21 = 0) to make $\beta_1$ directly interpretable
- The interaction term $Age_i * Z_i$ allows a **different slope** on each side of the cutoff

#### Why Centering Matters

With $Age_i$ centered at $c$, plugging in $Age_i \approx 0$ (just at the cutoff) simplifies the regression to show exactly what the discontinuity captures:

**Just under the threshold** ($Z_i = 0$, $Age_i \approx 0$):

$$\widehat{Drink}_{just\ under} = \hat{\beta}_0 + \hat{\beta}_1 \cdot 0 + \hat{\beta}_2 \cdot (\approx 0) + \hat{\beta}_3 \cdot (\approx 0) \cdot 0 \approx \hat{\beta}_0$$

**Just over the threshold** ($Z_i = 1$, $Age_i \approx 0$):

$$\widehat{Drink}_{just\ over} = \hat{\beta}_0 + \hat{\beta}_1 \cdot 1 + \hat{\beta}_2 \cdot (\approx 0) + \hat{\beta}_3 \cdot (\approx 0) \cdot 1 \approx \hat{\beta}_0 + \hat{\beta}_1$$

**Change at threshold:**

$$\widehat{Drink}_{just\ over} - \widehat{Drink}_{just\ under} = \hat{\beta}_1$$

> $\hat{\beta}_1$ is the [[Regression Discontinuity|RD estimate]] — the discontinuous jump at the cutoff.

#### The Two Separate Lines

For people **under** 21 ($Z_i = 0$): $$Drink_i = \beta_0 + \beta_2 Age_i + u_i$$

For people **21 or older** ($Z_i = 1$): $$Drink_i = (\beta_0 + \beta_1) + (\beta_2 + \beta_3) Age_i + u_i$$

Each side gets its own intercept and slope.

---

### Higher-Order Polynomial Specifications

When the relationship between $X$ and $Y$ is nonlinear, a linear fit may misattribute curvature as a discontinuity (or mask a real one). We can add polynomial terms, each interacted with $Z_i$ to allow different shapes on each side.

#### Quadratic specification:

$$Drink_i = \beta_0 + \beta_1 Z_i + \beta_2 Age_i + \beta_3 Age_i^2 + \beta_4 Age_i * Z_i + \beta_5 Age_i^2 * Z_i + u_i$$

#### Cubic specification:

$$Drink_i = \beta_0 + \beta_1 Z_i + \beta_2 Age_i + \beta_3 Age_i^2 + \beta_4 Age_i^3 + \beta_5 Age_i * Z_i + \beta_6 Age_i^2 * Z_i + \beta_7 Age_i^3 * Z_i + u_i$$

In all cases, $\hat{\beta}_1$ remains the coefficient of interest — the estimated jump at the cutoff.

#### Regression Results: Drinking Example

||Linear|Quadratic|Cubic|
|---|---|---|---|
|Over 21 ($\hat{\beta}_1$)|**6.66** (1.16)|**9.36** (1.75)|**9.94** (2.36)|
|Age|8.32 (0.51)|−2.89 (2.02)|−4.83 (5.08)|
|Age²|—|−3.82 (0.66)|−5.46 (3.98)|
|Age³|—|—|−0.37 (0.88)|
|Age×Z|−7.60 (0.68)|9.06 (2.72)|10.60 (6.82)|
|Age²×Z|—|2.00 (0.88)|3.98 (5.29)|
|Age³×Z|—|—|0.30 (1.16)|
|Constant|58.99 (0.86)|53.55 (1.29)|53.07 (1.73)|
|N|27,756|27,756|27,756|
|R²|0.05|0.05|0.05|

_Note: Age centered at 21; Z = 1 if age ≥ 21._

The quadratic and cubic fits both suggest a jump of ~9–10 pp, while the linear model estimates ~6.7 pp — the linear model likely understates the jump because it cannot account for the leveling-off in drinking rates above 21. The quadratic appears to capture the data shape well in this case.

---

### Balance Graphs

#### Why Balance Matters

The key identifying assumption in RD is the **[[Continuity Assumption|continuity assumption]]**: that potential outcomes vary smoothly through the cutoff in the absence of treatment. If this holds, groups just above and below are comparable.

Balance can fail if:

- **Manipulation of the running variable**: If the treatment is desirable, people may strategically sort above (or below) the cutoff — creating imbalance in who appears on each side
- **Differential attrition/non-response**: Survey non-response rates might change at the cutoff (e.g., people just over 21 might be less willing to admit drinking on a survey, causing differential response rates)
- **Misspecified polynomial**: Groups may appear falsely different at the cutoff if the polynomial order is too low or too high

#### What to Check

Check **predetermined covariates** — characteristics that are fixed before treatment and cannot be affected by it (e.g., gender, race). Do **not** check variables that could themselves be affected by treatment (e.g., employment rates might be affected by drinking).

**How to check:**

1. Plot the covariate on the vertical axis against $X$ — look for a visible jump at $c$
2. Formally estimate RD regressions with the covariate as the outcome and test the coefficient on $Z_i$

**Example — Minimum Legal Drinking Age:**

- ✅ **Gender composition** (fraction male): flat and continuous through age 21 — no discontinuity. Good.
- ✅ **Racial composition** (fraction White, fraction Hispanic): continuous through age 21. Good.
- ⚠️ **Educational attainment** (fraction with HS diploma): shows a strong trend through the ages, but no sharp jump at 21. Acceptable — the trend is smooth, not discontinuous.
- ❌ **Employment rates**: shows a continuous upward trend — but employment could itself be affected by drinking, so this variable _should not_ be included in a balance table.

---

### Balance Tables

Formally test balance by running the RD regression separately for each predetermined covariate as the outcome variable. Use the **same bandwidth and polynomial order** as the main first-stage and reduced-form regressions.

**Example regression (for gender balance):**

$$male_i = \phi_0 + \phi_1 Z_i + \phi_2 Age_i + \phi_3 Age_i^2 + \phi_4 Age_i * Z_i + \phi_5 Age_i^2 * Z_i + u_i$$

**Balance table results (drinking/crime example):**

||HS Diploma|Married|Working LW|In School|Male|
|---|---|---|---|---|---|
|$Z$|7.64 (1.40)|−2.85 (1.24)|1.94 (1.72)|−0.33 (1.35)|1.88 (1.78)|
|Age|−20.39 (1.71)|6.70 (1.23)|1.07 (2.01)|−2.60 (1.72)|−4.04 (2.04)|
|Age×Z|22.83 (2.23)|−2.97 (1.91)|4.30 (2.68)|−1.42 (2.13)|5.40 (2.78)|
|Age²|−11.34 (0.58)|0.86 (0.37)|−2.10 (0.66)|1.67 (0.59)|−0.76 (0.67)|
|Age²×Z|10.31 (0.74)|−0.28 (0.62)|1.34 (0.87)|−1.58 (0.70)|0.30 (0.91)|
|Constant|74.80 (1.04)|15.73 (0.87)|62.45 (1.26)|17.59 (1.02)|42.16 (1.28)|
|N|27,756|27,756|27,756|27,756|27,756|
|R²|0.06|0.04|0.03|0.05|0.00|

_Note: Age centered at 21; Z = 1 if age ≥ 21._

None of the $Z$ coefficients on the predetermined covariates are statistically significant at conventional levels — supporting the validity of the RD design.

---

### Density Test

Another validity check is to look for **manipulation of the running variable** by testing whether the _number of observations_ changes discontinuously at the cutoff.

- If people can manipulate their position relative to the cutoff (e.g., to gain or avoid treatment), we would expect to see an unusual **bunching** of observations just above or below the threshold
- A smooth density through the cutoff is reassuring — it suggests people cannot precisely control which side they are on

**In the drinking example:** The count of people surveyed increases smoothly with age — no jump at 21. This supports the assumption that people near 21 cannot manipulate their birthdate relative to the cutoff.

> Age is a running variable people cannot manipulate — you cannot choose when you turn 21. This makes the [[Density Test|density test]] easy to pass for age-based RD designs.

---

### Adding Covariates

Including predetermined covariates in the RD regression (alongside the running variable and threshold indicator) can improve precision without affecting the estimate's validity — similar to adding controls in an RCT.

**Effect of adding covariates to the drinking first-stage regression:**

|Controls included|$\hat{\beta}_1$ (Over 21)|SE|
|---|---|---|
|None|9.25|(2.15)|
|+ HS Diploma|8.77|(2.13)|
|+ Work LW|8.53|(2.12)|
|+ In School|8.44|(2.12)|
|+ Male|8.15|(2.09)|

The point estimate is stable across specifications (declining modestly from 9.25 to 8.15), and the standard error shrinks slightly as controls absorb residual variance. Stability of the estimate across covariate specifications is a robustness check — large changes would be concerning.

---

### Big Takeaways

> The [[Regression Discontinuity|RD]] estimate $\hat{\beta}_1$ is the discontinuous jump at the cutoff. It always represents the effect of crossing the threshold — the same logic as the [[Instrumental Variables#Reduced Form|reduced form]] divided by the [[Instrumental Variables#First Stage|first stage]].

- Center the [[Running Variable|running variable]] at $c$ so that $\hat{\beta}_1$ directly reads off the jump
- Always try multiple polynomial orders and compare — the linear model can be misspecified
- The bandwidth should be narrow enough to ensure comparability, but wide enough to see the relationship
- Validate with **balance graphs** and **balance tables** using predetermined covariates only
- The **[[Density Test|density test]]** (checking for bunching at the cutoff) detects potential manipulation of the running variable
- Adding covariates increases precision and serves as a robustness check — the estimate should be stable
# Week 7
## L13 Regression Discontinuity: Sharp, Fuzzy, and Graphing

Tags: #econ104 #regression-discontinuity #sharp-RD #fuzzy-RD #graphing #bin-width #bandwidth #running-variable Related: [[L12 Regression Discontinuity Specifications]] · [[Regression Discontinuity]] · [[Running Variable]] · [[Bandwidth]] · [[Continuity Assumption]] · [[Instrumental Variables]] · [[LATE]]

This lesson covers the distinction between sharp and fuzzy RD designs, the formal estimators for each, and the practical choices involved in graphing an RD relationship (bin width and bandwidth).

---

### Sharp Regression Discontinuity (SRD)

In the **Sharp RD** design, treatment $D_i$ is a **deterministic function** of the running variable: $D_i = \mathbf{1}(X_i \geq c)$.

- Everyone below the cutoff is untreated; everyone at or above is treated (or vice versa).
- The causal effect is estimated as the **difference in mean outcomes** on either side of the cutoff:

$$\tau_{SRD} = \lim_{x \downarrow c} E[Y_i | X_i = x] - \lim_{x \uparrow c} E[Y_i | X_i = x]$$

- This identifies the **average causal effect at the cutoff**:

$$\tau_{SRD} = E[Y_{1i} - Y_{0i} | X_i = c]$$

#### Continuity Assumption

To justify this comparison, we must assume that the **potential outcomes** $E[Y_{0i}|X_i = x]$ and $E[Y_{1i}|X_i = x]$ are **continuous in $x$** — no sharp changes in potential outcomes at the threshold.

- Since we never observe $Y_{0i}$ for units exactly at $c$, we extrapolate using units just below $c$.
- The continuity assumption guarantees the bias from this extrapolation becomes negligible as we approach $c$.

---

### Fuzzy Regression Discontinuity (FRD)

In the **Fuzzy RD** design, $D_i$ is **not** a deterministic function of $X_i$. Instead, crossing the cutoff causes a **discontinuous jump in the probability of treatment**, but not a 100 percentage point jump:

$$0 < \lim_{x \downarrow c} P(D_i = 1 | X_i = x) - \lim_{x \uparrow c} P(D_i = 1 | X_i = x) < 1$$

- This is more common in practice due to non-compliance.
- **Examples:**
    - Medicare eligibility at 65: many already had insurance → only a ~6 p.p. jump. Fuzzy design.
    - Boston Latin School attendance: nearly all above the cutoff attended → ~90 p.p. jump. Close to sharp.

#### The FRD Estimator

$$\tau_{FRD} = \frac{\lim_{x \downarrow c} E[Y_i|X_i=x] - \lim_{x \uparrow c} E[Y_i|X_i=x]}{\lim_{x \downarrow c} E[D_i|X_i=x] - \lim_{x \uparrow c} E[D_i|X_i=x]}$$

- The **numerator** is the reduced form: the jump in $Y$ at the cutoff.
- The **denominator** is the first stage: the jump in $D$ at the cutoff.
- This is the same structure as the [[Instrumental Variables|IV estimator]] (Wald ratio).

#### Compliers, Never-Takers, Always-Takers

As in IV/RCT settings:

- **Complier**: does not take treatment when cutoff is just above $X_i$; does take treatment when cutoff is just below $X_i$.
- **Never-taker**: never takes treatment regardless of which side of the cutoff they are on.
- **Always-taker**: always takes treatment regardless of which side of the cutoff they are on.
- **Defiers**: assumed not to exist (monotonicity assumption).

Always-takers and never-takers contribute nothing to the FRD numerator or denominator. The FRD estimate is the **LATE for compliers at the cutoff**:

$$\tau_{FRD} = E[Y_{1i} - Y_{0i} | \text{unit } i \text{ is a complier and } X_i = c]$$

---

### RD Graphing: Bin Width

Figures are central to RD designs — they provide a **raw, visual representation** of the discontinuity in treatment $D$ or outcome $Y$ at the cutoff.

#### How RD Figures Are Constructed

Group observations into evenly-spaced bins of the running variable $X$. For bin $k$ spanning $(b_k, b_{k+1}]$:

$$N_k = \sum_{i=1}^{N} \mathbf{1}(b_k < X_i \leq b_{k+1})$$

$$\bar{D}_k = \frac{1}{N_k} \sum_{i=1}^{N} D_i \cdot \mathbf{1}(b_k < X_i \leq b_{k+1})$$

$$\bar{Y}_k = \frac{1}{N_k} \sum_{i=1}^{N} Y_i \cdot \mathbf{1}(b_k < X_i \leq b_{k+1})$$

Plot $\bar{D}_k$ or $\bar{Y}_k$ against the bin midpoints. **No bin should span the cutoff $c$.**

#### Choosing the Bin Width

The bin width trades off **variance** against **bias**:

|Bin width|Problem|
|---|---|
|Too narrow|Very noisy (high variance); hard to see the relationship|
|Too wide|Contains data far from the cutoff; may introduce bias or obscure the jump|

**Goal**: find a bin width that clearly reveals the underlying relationship between $X$ and $D$ (or $Y$) without being either too noisy or too smoothed.

**Example — Drinking Age (running variable = age in days):**

- **1 day**: too narrow — extremely noisy, no pattern visible.
- **3 days**: still too narrow — noisy scatter.
- **200 days**: too wide — only a handful of bins, relationship masked.
- **20 days**: reasonable — trend and jump starting to appear.
- **45 days**: also reasonable — clean trend with clear jump at 21.

---

### RD Graphing: Bandwidth

The **bandwidth** is the overall range of the running variable $X$ shown in the figure (not to be confused with the bin width). It should be:

- **Centered at the cutoff** $c$.
- **Wide enough** to see the overall relationship.
- **Narrow enough** to highlight the jump at the cutoff.

#### Bandwidth Examples (bin width fixed at 30 days)

|Range of $X$|Assessment|
|---|---|
|Ages 18–30|Too wide — jump at 21 hard to see; data from far away the cutoff|
|Ages 20.9–21.1|Too narrow — only ~4 bins, no context|
|Ages 18–24|Reasonable — good context, jump visible|
|Ages 19–23|Good — tighter focus, jump clearly visible|

- Also consider **zooming in on the vertical axis** to better display the magnitude of the jump.
- The final figure with ages 19–23 and vertical axis restricted to $[0.4, 0.8]$ clearly reveals the sharp increase in drinking at age 21.

---

### Putting It Together

A well-constructed RD figure:

1. **Pick a bin width** by visually examining the bias–variance tradeoff.
2. **Pick the bandwidth** (range of $X$) to accurately capture the relationship around $c$.
3. **Zoom in on the vertical axis** to better reveal the jump at $c$.
4. **Construct the same figure for both the first stage** (treatment $D$ on $Y$-axis) and the **reduced form** (outcome $Y$ on $Y$-axis).

---

### Big Takeaways

> In a **Sharp RD**, the threshold perfectly predicts treatment; the RD estimate directly identifies the average treatment effect at the cutoff. In a **Fuzzy RD**, the threshold is an instrument — the estimator is reduced form divided by first stage, identifying the LATE for compliers at the cutoff.

- Sharp RD: $D_i = \mathbf{1}(X_i \geq c)$; treatment is deterministic.
- Fuzzy RD: threshold shifts treatment probability but not by 100 pp — analogous to IV.
- Both rely on the **continuity assumption**: no discontinuous changes in potential outcomes at $c$.
- RD figures require careful choices of **bin width** (bias–variance tradeoff) and **bandwidth** (range of $X$ to display).
- A good RD paper makes its case visually with a few well-constructed figures.
## L14 Difference-in-Differences: Introduction

Tags: #econ104 #difference-in-differences #parallel-trends #natural-experiment #panel-data #causal-inference Related: [[L13 Regression Discontinuity]] · [[RCT]] · [[Parallel Trends Assumption]] · [[Panel Data]] · [[Counterfactual]]

This lesson introduces the Difference-in-Differences (DiD) design — its logic, regression formulation, and application to natural experiments, illustrated through the Mississippi banking crisis of 1930.

---

### Motivation: From Single Difference to DiD

In the voting RCT, treatment and control groups were compared **cross-sectionally** in the post period. An alternative is to look at the **change over time** for the treatment group:

$$\tau_D = Y_{T,2002} - Y_{T,1998} = 0.606 - 0.574 = 0.032$$

**Problem**: This change may reflect **time trends** (e.g., higher overall turnout in 2002) rather than the treatment effect itself.

**Solution**: Use the **control group's change over time** as a counterfactual for what would have happened to the treatment group in the absence of treatment.

---

### The DiD Estimator

The **Difference-in-Differences** estimator subtracts the control group's change from the treatment group's change:

$$\tau_{DD} = (Y_{T,After} - Y_{T,Before}) - (Y_{C,After} - Y_{C,Before})$$

**Voting example:**

$$\tau_{DD} = (0.606 - 0.574) - (0.594 - 0.572) = 0.032 - 0.022 = 0.010$$

The single difference (0.032) **overstated** the effect. The control group's change (0.022) captures background trends in voting unrelated to treatment.

---

### The Parallel Trends Assumption

The DiD design rests on the **parallel trends assumption**: the change in the control group over time is the same as the change that would have occurred in the treatment group **in the absence of treatment**.

A good control group should:

- Be **similar to the treatment group** in the pre-period (levels).
- Have a **similar trend** in the outcome prior to treatment.
- **Not be treated** by the same or similar policy.

> This assumption is **not directly testable** for the post period (we can't observe the counterfactual), but we can check whether pre-treatment trends were parallel.

---

### DiD as a Regression

DiD can be estimated using the following regression:

$$Y_{g,t} = \alpha + \beta , Treat_g + \gamma , Post_t + \delta_{DD} , Treat_g \times Post_t + u_{g,t}$$

|Coefficient|Interpretation|
|---|---|
|$\alpha$|Mean outcome for the **control group in the pre-period**|
|$\beta$|**Pre-period difference** between treatment and control groups|
|$\gamma$|**Time trend** common to both groups (change for control group)|
|$\delta_{DD}$|The **DiD estimate** — the causal effect of treatment|

**Voting example coefficients:**

- $\alpha = 0.572$ (control, before)
- $\beta = 0.574 - 0.572 = 0.002$ (pre-period gap)
- $\gamma = 0.594 - 0.572 = 0.022$ (control group time trend)
- $\delta_{DD} = 0.010$ (treatment effect)

This framework extends naturally to **multiple treated/control units** and **multiple pre/post periods**.

---

### DiD for Policy Analysis: Natural Experiments

DiD is the **most common research design for policy analysis with panel data**. It does not require an RCT — it exploits variation from naturally occurring policy changes.

**Setup:**

- Two cross-sectional units (states, cities, countries): one treated, one not.
- Data on both units before and after the policy change.
- Estimate:

$$\tau_{DD} = (Y_{11} - Y_{10}) - (Y_{01} - Y_{00})$$

where $Y_{st}$: outcome in state $s$ ($s=1$ treated, $s=0$ control) at time $t$ ($t=1$ post, $t=0$ pre).

**What makes a good control unit?**

- Similar outcome values in the pre-period.
- Similar pre-period trend in the outcome.
- Not treated by the same or similar policy.
- Similar relevant characteristics (e.g., for a rent control study: similar housing markets, population density, income levels).

---

### Application: Mississippi Banking Crisis (1930)

#### Background

In the 1930s, before the FDIC, bank runs were self-fulfilling panics: fear of failure → withdrawals → actual failure. In late 1930, the failure of one Mississippi bank triggered a cascade.

Two Federal Reserve districts covered Mississippi, and they responded **very differently**:

|District|Fed|Policy|Region|
|---|---|---|---|
|6th (Atlanta)|Accommodative|Increased lending by **+40%**|Southern Mississippi → **Treatment**|
|8th (St. Louis)|Restrictive|Reduced lending by **−10%**|Northern Mississippi → **Control**|

Both regions face the same state regulations, shared culture, and similar economic conditions — making this a strong natural experiment.

#### First Stage: Single Difference

Did the Atlanta Fed's lending save banks? Looking only at the 6th district:

$$\tau_D = Y_{6,1931} - Y_{6,1930} = 121 - 135 = -14$$

14 banks still closed. But this doesn't tell us what would have happened **without** the intervention.

#### Introducing the Counterfactual

In the 8th district (no aggressive lending):

$$Y_{8,1931} - Y_{8,1930} = 132 - 165 = -33$$

33 banks closed without support. This is our counterfactual for how many would have closed in the 6th district absent the policy.

#### The DiD Estimate

$$\tau_{DD} = (Y_{6,1931} - Y_{6,1930}) - (Y_{8,1931} - Y_{8,1930}) = (-14) - (-33) = 19$$

The Atlanta Fed's intervention **saved approximately 19 banks** from failing.

#### Regression Formulation

$$Y_{d,t} = \alpha + \beta , Treat_d + \gamma , Post_t + \delta_{DD} , Treat_d \times Post_t + u_{d,t}$$

Using data from 1929–1934 (6 years, 2 pre / 4 post):

$$Y_{d,t} = 167 - 29 , Treat_d - 49 , Post_t + 20.5 , Treat_d \times Post_t$$

The multi-year estimate (20.5) closely matches the two-period estimate (19). Additional periods allow:

- Estimation of **standard errors** (more variation to estimate uncertainty).
- Assessment of **effect persistence** (did the policy just delay closures?).
- Evaluation of the **parallel trends assumption** using pre-treatment data.

#### Pre-Trends and the Parallel Trends Assumption

The two districts had **parallel trends in bank counts** in 1929–1930 (before the crisis hit), supporting the assumption that the 8th district is a valid counterfactual for the 6th.

> The gap between the 6th district's actual path and its **DiD counterfactual** (constructed by applying the 8th district's trend to the 6th district) represents the treatment effect. The graph shows the effects were **persistent** — the 6th district consistently outperformed its counterfactual through 1934.

#### Spillover Effects: Wholesale Firms

The Fed intervention also improved broader economic outcomes:

||1929|1933|Difference|
|---|---|---|---|
|**Number of wholesale firms**||||
|6th District (Atlanta)|783|641|−142|
|8th District (St. Louis)|930|607|−323|
|**DiD**|||**+181**|
|**Net wholesale sales ($M)**||||
|6th District|141|60|−81|
|8th District|245|83|−162|
|**DiD**|||**+81**|

Keeping banks open preserved approximately 181 more wholesale firms and ~$81M more in net sales in the accommodative district.

---

### Big Takeaways

> DiD estimates the treatment effect by comparing **the change for a treated group** to **the change for a control group**. The control group's change proxies the counterfactual trend the treated group would have followed without treatment.

- The DiD estimator: $(Y_{T,After} - Y_{T,Before}) - (Y_{C,After} - Y_{C,Before})$
- Implemented as a regression with a **treatment × post interaction** — the coefficient $\delta_{DD}$ is the causal estimate.
- The identifying assumption is **parallel trends** — untestable in the post period, but assessable with pre-treatment data.
- DiD is most credible when the control unit is **similar** to the treated unit (same state, similar characteristics) and has **parallel pre-treatment trends**.
- Multiple time periods improve precision, enable parallel trends checks, and reveal effect persistence.
# Week 8
## L15 Difference-in-Differences: Design Options

Tags: #econ104 #difference-in-differences #scaling #multiple-treatments #parallel-trends #triple-differences #natural-experiment #panel-data #causal-inference  
Related: [[L14 Difference-in-Differences Introduction]] · [[Parallel Trends Assumption]] · [[Panel Data]] · [[Counterfactual]] · [[MLDA]] · [[John Snow Cholera Study]]

This lesson extends the DiD framework to cover scaled outcomes, multiple treatment units, differential trends, and the triple differences (DDD) estimator, illustrated through the London cholera epidemic and the minimum legal drinking age (MLDA) literature.

---

### Part 1: Scaled Outcomes

#### Motivation: The London Cholera Case

In the 1840s–1850s, London's drinking water was supplied by private companies drawing from the Thames, which was also contaminated by sewers. John Snow mapped cholera incidence and identified the waterborne source. In 1852, the **Lambeth Water Company** moved its intake ~20 miles upstream on the Thames — a natural experiment in water quality.

Two epidemics bracketed this change: one in 1849 (pre-treatment) and one in 1854 (post-treatment).

#### Single Difference

For the Lambeth-served area:

$$\tau_D = Y_{L,1854} - Y_{L,1849} = 37 - 162 = -125$$

**Problem**: The 1854 epidemic may have been less severe overall, so the 125-life reduction could partly reflect a milder epidemic rather than the pipe relocation.

#### The DiD Estimator — Raw Counts

Using Southwark & Vauxhall (S&V) as the control (did not move intake):

|Water Company|Deaths 1849|Deaths 1854|Districts|
|---|---|---|---|
|Southwark & Vauxhall|2261|2485|12|
|Lambeth|162|37|4|

$$\tau_{DD} = (37 - 162) - (2485 - 2261) = -125 - 224 = -349$$

**Problem**: The two companies serve very different numbers of districts. S&V's death count rose by 224 — this large increase in the control group partly reflects that the 1854 epidemic was _more_ severe in S&V areas, not just a common time trend. Comparing raw counts across groups of very different sizes is misleading.

#### Scaled DiD — Converting to Proportions

To make the two groups comparable, convert the change to a **proportional** (percentage) change relative to the baseline:

$$\tau_{DD} = \left(\frac{Y_{L,1854} - Y_{L,1849}}{Y_{L,1849}}\right) - \left(\frac{Y_{S,1854} - Y_{S,1849}}{Y_{S,1849}}\right)$$

$$= \left(\frac{37 - 162}{162}\right) - \left(\frac{2485 - 2261}{2261}\right) = (-0.77) - (0.099) = -0.87$$

**Interpretation**: The counterfactual (S&V's +9.9% increase) reveals the 1854 epidemic was actually _more_ severe than 1849. After accounting for this, the Lambeth intervention produced an **87% reduction** in mortality — a 77% drop in Lambeth areas, against a 10% increase that would have been expected without the intervention.

> **Key takeaway on scaling**: When treatment and control groups differ substantially in size or baseline levels, comparing raw changes can be misleading. Scaling outcomes to rates or proportions (deaths per capita, percentage changes) allows apples-to-apples comparisons.

#### Additional Evidence: The Overlap Districts

Areas served by _both_ companies fell from 3,905 deaths (1849) to 2,547 deaths (1854) — a large reduction consistent with the DiD finding, since the Lambeth pipe improvement would have benefited residents who switched to Lambeth water.

---

### Part 2: Multiple Treatment Units

#### Motivation: MLDA and Death Rates

After Prohibition, all states set their minimum legal drinking ages (MLDAs) at 21. Following the **26th Amendment** (1971, lowering the voting age to 18), many states lowered their drinking ages as well — but at different times and to different ages. In 1984, Congress threatened to withhold highway funds from states with MLDAs below 21; by 1988, all states had returned to 21.

This staggered variation creates many natural experiments.

#### Single State, Single Control

In 1975, Alabama lowered its MLDA to 19. A single-difference estimate:

$$\tau_D = Y_{AL,1976} - Y_{AL,1974}$$

**Problems**: Other factors may have changed in Alabama over 1974–1976 (road conditions, car safety technology, economic conditions) that are unrelated to the drinking age change.

**Solution**: Use Arkansas (which never lowered its MLDA from 21) as a control:

$$\tau_{DD} = (Y_{AL,1976} - Y_{AL,1974}) - (Y_{AR,1976} - Y_{AR,1974})$$

A good control unit should be chosen based on population similarity, physical proximity, and similar pre-period outcomes.

#### Extending to All States: Panel DiD

Rather than limiting the analysis to Alabama vs. Arkansas, we can exploit _all_ state-level MLDA changes over time. The regression specification becomes:

$$Y_{s,t} = \alpha + \sum_{s=AK}^{WY} \beta_s , State_s + \sum_{t=1971}^{1983} \gamma_t , Year_t + \delta_{DD} , Legal_{s,t} + u_{s,t}$$

|Term|Interpretation|
|---|---|
|$\beta_s , State_s$|State fixed effects — captures permanent differences across states (analogous to $Treat$)|
|$\gamma_t , Year_t$|Year fixed effects — captures national time trends (analogous to $Post$)|
|$Legal_{s,t}$|Fraction of 18–20 year olds who can legally drink in state $s$, year $t$ (analogous to $Treat \times Post$)|
|$\delta_{DD}$|The DiD estimate — causal effect of legal drinking on the outcome|

#### Results: MLDA Effects on Death Rates

|Dependent Variable|(1) No State Trends|
|---|---|
|All deaths|10.80 (4.59)|
|Motor vehicle accidents|7.59 (2.50)|
|Suicide|0.59 (0.59)|
|All internal causes|1.33 (1.59)|

The largest and most precisely estimated effect is on **motor vehicle accidents** — consistent with the mechanism that legal drinking increases drunk driving among young adults. Effects on suicide and internal causes are small and statistically insignificant.

---

### Part 3: Differential Trends and Bias

#### What Causes DiD to Be Biased?

The DiD estimator differences out changes that affect _both_ groups equally. However:

- **Factors affecting both states equally** (e.g., national improvements in automobile safety, national economic conditions): These are captured by year fixed effects and do **not** cause bias.
- **Factors affecting only the treated state** (e.g., Alabama improving road quality independently of the MLDA change): These are _not_ captured and **do cause bias**, because they violate the parallel trends assumption.

#### Diagnosing the Problem Visually

Three scenarios illustrate this:

1. **Parallel pre-trends with a post-treatment jump** → DiD gives an unbiased causal estimate.
2. **Non-parallel pre-trends, no real effect** → DiD produces a spurious positive estimate because the treated group was already on a steeper trend.
3. **Non-parallel pre-trends, real effect** → A true causal jump is still visible but DiD will be biased unless trends are accounted for.

#### Controlling for State-Specific Trends

To address pre-existing differential trends, add a **state-specific linear time trend** $\theta_s \cdot t$ to the regression:

$$Y_{s,t} = \alpha + \sum_{s=AK}^{WY} \beta_s , State_s + \sum_{t=1971}^{1983} \gamma_t , Year_t + \sum_{s=AK}^{WY} \theta_s , State_s \times t + \delta_{DD} , Legal_{s,t} + u_{s,t}$$

If the DiD effect shrinks substantially after adding state trends, it suggests the original estimate was contaminated by pre-existing trends. If the estimate is **robust**, confidence in causality increases.

#### Robustness Check: MLDA with State Trends

|Dependent Variable|(1) No Trends|(2) With State Trends|
|---|---|---|
|All deaths|10.80 (4.59)|8.47 (5.10)|
|Motor vehicle accidents|7.59 (2.50)|6.64 (2.66)|
|Suicide|0.59 (0.59)|0.47 (0.79)|
|All internal causes|1.33 (1.59)|0.08 (1.93)|

The motor vehicle accidents estimate is fairly **stable** after adding state trends (7.59 → 6.64), suggesting the MLDA effect on driving deaths is not primarily driven by pre-existing trends. The internal causes estimate collapses to near zero, suggesting that earlier coefficient reflected differential trends rather than a true MLDA effect.

---

### Part 4: Triple Differences (DDD)

#### Motivation

Even with a control state, the DiD estimate can be biased if **state-specific factors** change at the same time as the MLDA law. For example:

- A state speed limit change in Alabama at the same time as the MLDA reduction.
- Increased law enforcement investment unique to Alabama.
- Weather events or other state-specific shocks.

These factors would affect death rates in Alabama but not in Arkansas, biasing the DiD estimate.

#### The Solution: A Third Dimension of Comparison

The **triple differences (DDD)** estimator adds another layer of comparison: a group _within_ each state that is exposed to any state-specific changes but is **not** directly affected by the treatment (the MLDA change).

For the MLDA example, people aged **21–22** in both states serve as this "placebo" group — they are subject to the same roads, weather, and state policies, but the MLDA law does not change their legal drinking status.

#### The DDD Estimator

$$\tau_{DDD} = \underbrace{[(Y_{AL,18-20,1976} - Y_{AL,18-20,1974}) - (Y_{AR,18-20,1976} - Y_{AR,18-20,1974})]}_{\text{DiD for affected age group (18–20)}}$$

$$- \underbrace{[(Y_{AL,21-22,1976} - Y_{AL,21-22,1974}) - (Y_{AR,21-22,1976} - Y_{AR,21-22,1974})]}_{\text{DiD for unaffected age group (21–22)}}$$

|Layer|What it controls for|
|---|---|
|First difference (within state, over time)|State-level time trends and national shocks|
|Second difference (across states)|Cross-state differences in baseline levels|
|Third difference (across age groups)|State-specific changes that affect all ages equally|

#### What DDD Controls For (vs. DiD)

|Factor|DiD controls?|DDD controls?|
|---|---|---|
|National seat belt law|✅ Yes|✅ Yes|
|National economic conditions|✅ Yes|✅ Yes|
|State speed limit change (Alabama)|❌ No|✅ Yes|
|State road investment (Alabama)|❌ No|✅ Yes|
|Arkansas rainy season (all ages)|❌ No|✅ Yes|
|Alabama policy targeting 18–20 _specifically_|❌ No|❌ No|

> **Residual bias**: A change that is state-specific _and_ age-group-specific will still bias the DDD estimate — e.g., if the governor of Alabama simultaneously cracked down specifically on teenage drivers (not older ones) at the same time as the MLDA change.

#### Worked Example

||Death Rate 1974|Death Rate 1976|
|---|---|---|
|**Ages 18–20**|||
|Alabama|10.8|9.2|
|Arkansas|12.3|12.1|
|**Ages 21–22**|||
|Alabama|8.4|7.4|
|Arkansas|8.9|8.6|

**DiD for ages 18–20** (the treated group):

$$\tau_{DD,18-20} = (9.2 - 10.8) - (12.1 - 12.3) = (-1.6) - (-0.2) = -1.4$$

**DiD for ages 21–22** (the placebo/control group):

$$\tau_{DD,21-22} = (7.4 - 8.4) - (8.6 - 8.9) = (-1.0) - (-0.3) = -0.7$$

**Triple Differences estimate**:

$$\tau_{DDD} = \tau_{DD,18-20} - \tau_{DD,21-22} = (-1.4) - (-0.7) = -0.7$$

The DDD estimate is smaller in magnitude than the DiD estimate, suggesting that some of the apparent MLDA effect in the DiD was attributable to factors in Alabama that reduced death rates for _all_ ages, not just the newly-drinking cohort.

#### DDD Regression Framework

The DDD can be implemented in a single regression by including all main effects and two-way interactions, with the three-way interaction as the key coefficient:

$$Y_{sta} = \beta_0 + \beta_1 Treat_s + \beta_2 Post_t + \beta_3 Age18to20_a$$ $$+ \beta_4 Treat_s \times Post_t + \beta_5 Treat_s \times Age18to20_a$$ $$+ \beta_6 Post_t \times Age18to20_a + \beta_7 Treat_s \times Post_t \times Age18to20_a + \varepsilon_{sta}$$

|Coefficient|Interpretation|
|---|---|
|$\beta_1$|Pre-period, old-age difference between Alabama and Arkansas|
|$\beta_2$|Time trend for old ages in the control state (Arkansas)|
|$\beta_3$|Age-group difference (18–20 vs. 21–22) in the control state, pre-period|
|$\beta_4$|DiD for the 21–22 group (state-level time trend, unaffected by MLDA)|
|$\beta_5$|Pre-period age gap between states|
|$\beta_6$|Time trend specific to the 18–20 age group in Arkansas|
|$\beta_7$|**The DDD estimate** — applies to those who are in the treated state, in the post period, and in the affected age group (18–20)|

The coefficient $\beta_7$ captures the change in the _gap between age groups_ caused by the MLDA change in the treated state — isolating the effect of legal drinking access from any state-level trends that would affect all drivers equally.

---

### Big Takeaways

> DiD can be extended in several important directions to improve credibility and handle more complex data structures.

- **Scaling**: When groups differ in size or baseline levels, use proportional or per-capita outcomes rather than raw counts to make treatment and control groups comparable.
- **Multiple treatments**: With staggered treatment timing across many units, use state and year fixed effects as the analogs of $Treat$ and $Post$. The key treatment variable becomes the continuous share of the affected group that is treated.
- **Differential trends**: If treated and control units had different pre-treatment trends, simple DiD will be biased. Adding unit-specific time trends can partially address this; stability of estimates before and after adding trends is a robustness check.
- **Triple differences (DDD)**: Adding a third dimension of comparison (a group unaffected by treatment within each unit) controls for unit-specific factors that would otherwise bias DiD. The DDD estimate is the DiD for the treated group minus the DiD for the "placebo" group. In regression, the DDD coefficient is the three-way interaction term.
- The DDD does not eliminate all sources of bias — factors that are simultaneously unit-specific _and_ group-specific will still confound the estimate.
----
# BREAK
## L16
# Week 9
## L17
## L18
# Week 10
## L19
## L20

## Under this topic

```dataview
TABLE WITHOUT ID file.link AS note, type, status
WHERE parent = this.file.link
SORT type ASC, file.name ASC
```
