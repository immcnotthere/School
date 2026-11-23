---
type: concept
parent: "[[Econ 104]]"
domain: econ
status: draft
---



ECON 104 Winter 2026 Assignment 1 Background In this assignment, you will examine the effect of an effort to increase voter turnout through encouraging phone calls. Voters were randomly assigned to get (or not) an encouraging phone call. As can be seen by examining the data, not everyone assigned to get a call (treat_real = 1) actually answered and listened to the call (contact = 1). Due to the randomization, the analysis in this assignment should generate a “gold standard” estimate of the effect of getting assigned to receive a phone call on voter turn out. The data is from: Arceneaux, Kevin, Alan Gerber, and Donald Green. “Comparing Experimental and Matching Methods Using a Large-Scale Voter Mobilization Experiment.” Political Analysis, 2006, 14, 37-62. This study was intended to assess the effectiveness of get-out-the-vote efforts. In the experiment, the authors attempted to deliver the following message to those selected for treatment: “Hello, may I speak with (name of person) please? Hi. This is (caller's name) calling from Vote 2002, a nonpartisan effort working to encourage citizens to vote. We just wanted to remind you that elections are being held this Tuesday. The success of our democracy depends on whether we exercise our right to vote or not, so we hope you'll come out and vote this Tuesday. Can I count on you to vote next Tuesday?'” For this assignment, use the dataset posted on Canvas. The dataset includes the following variables (among others): • vote02: Voted in 2002 -- the outcome of interest • treat_real: Assignment to the treatment group • contact: Answered the phone call and responded to the question “Can I count on you to vote next Tuesday?'”, regardless of their answer • newreg - Newly registered voter • busy - Whether the phone line was busy when the call was made • age - Age of the individual in years • female - Gender of the individual • vote00 - Voted in 2000 (prior to treatment) • vote98 - Voted in 98 (prior to treatment) • state - State of residence 1 for Iowa and 0 for Michigan


Assignment 1 - Analysis In this analysis, you will generate three tables: 1) a summary statistics table; 2) a balance table; and 3) a regression table. Details regarding these tables are included below. Important things to remember: 

A) Your tables should be nicely formatted using Stata output commands (as shown in section). This means, for example, no screen shots of Stata output. Use Stata output commands (as shown in section) and use Word or Excel to make your tables. 

No screenshots

You see every economist do this naming the summary statistics table




B) Stata variable names should be replaced with informative names. For example, “vote98” should be something like “Voted in 1998”. 

C) Your tables and code should be submitted in a single PDF file with the three tables appearing first and your complete code at the end. 


1. Summary Statistics Table. Present the mean and standard deviation for each of the variables in your data set. You should group your variables in a logical way (e.g., voting variables should be together, demographic variables together, etc.). Note that it is standard to present 3 decimal places in all tables. Your variables should be given informative names (not Stata variable names). 

2. Balance Table: Provide evidence that the randomization worked by comparing the means of the sample characteristics in the treatment and control groups. Please create a clean table that includes columns with the variable means for the treatment and control groups, the difference between the two groups, and the pvalue of the difference. [Hint: Because you are interested in estimating whether the randomization worked, and not the effect of the treatment, the table should only include fixed characteristics and characteristics measured prior to treatment (and not characteristics that could change in response to the treatment).] 


3. Regression Table: Create a table where each column corresponds to a regression. The first column contains the parameters of a the regression Voted 2002i = β0 + β1 Treatedi + ui In each following column you should add one more covariate (control variable) to the regression. Note that, as in question 2, control variables should be fixed characteristics or those measured prior to treatment. Don’t forget to include the code you wrote to generate your results in the PDF with your results. 



Assignment 1 – Writing The writing component of the assignment is designed to provide you with an opportunity to develop intuition around the tables you created. This intuition is crucial for understanding the five research designs and for performing well on the course exams. Your writing will be graded based on completion and effort and must be your own. AI use will result in a failing grade for the assignment and course. Please follow the directions below to ensure that you receive full credit: 


A. Create a Google Doc (https://docs.google.com) for the assignment. Name it “Assignment 1 – Econ 104”. 


B. Share the Google Doc with me (gbulman@ucsc.edu) with Editor privileges, allowing me to view the version history. Please uncheck “Notify People” so I do not receive an email. 

C. Add the URL for your Google Doc at the top of the Google Doc. This will allow me to click through to your Google Doc when you submit your PDF on Canvas. 


D. When you have completed your writing, submit a PDF of your writing on Canvas. To do this, go to File -> Download -> PDF. Note that your PDF needs to have the link to the Google Doc at the top of the page to receive credit. You should write one full paragraph addressing each of the following topics. Your writing should be in complete, coherent, academic sentences. In total, you should submit a minimum of two single spaced pages for this assignment. 


1. Explain where the data is from (source) and describe the sample using your summary statistics table. You should reference specific values from the table and paint a clear picture of who is in the sample, what fraction of the sample is treated, etc. 
   
2. Discuss the balance table and whether it is consistent with the randomization being correctly implemented. Why or why not? Provide references to specific means of variables, differences between the treatment and control groups, and p-values. 
   

3. Discuss the regression results, highlighting the impact of the treatment on voting rates in 2002. Be sure to use the correct units of measurement and reference whether the effects are statistically significant. Discuss whether the effect seems large in magnitude. 4. Discuss the robustness of your regression results to adding control variables. What effect does adding covariates have on your estimates of the treatment effect? Be specific. What does this tell you about the relationship between the covariates and being assigned to the treatment group? 5. Discuss why you can or cannot interpret the effects as causal in light of the research design (RCT), the balance table, and regression results. Does comparing the voting rates of the treatment and control groups generate an unbiased estimate of the causal effect of getting assigned to get an encouraging call on the probability of voting? Explain.