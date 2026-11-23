---
type: reference
parent: "[[Bayes Update Algorithm]]"
domain: stats
course: "STAT 132"
status: draft
---


This is the process I've been using on the prior/posterior problems. Anything with (new) I added this week and want to check with you.

The equation everything comes from
f(theta | x) = f(x | theta) f(theta) / f(x)
posterior = likelihood times prior, divided by f(x)
f(x) doesn't have theta in it, so I treat the posterior as proportional to likelihood times prior and fix the scaling at the end.

Step 0 (new). Read what the question wants
0a. Figure out which steps it's actually asking for. If it says "determine the prior pdf" I only do step 2. "Write the likelihood" is just step 4. "Is this a reasonable prior" is just 2a. "Find the posterior" is steps 1 through 6. If it says Bayes estimate or names a loss, I go all the way to step 7.
0b. Write down which loss it names, if it names one, so I don't forget it by step 7.

Step 1. Pick the model for X (one single result)
I ask these in order.
1a. What does one result look like?
  A. yes/no (1 or 0), so Bernoulli, and I'm done with step 1
  B. a whole number count, go to 1b
  C. a number on a continuous scale, go to 1c
  D. none of those (like 3 or more categories), go to 1d
1b. For a count, is there a max?
  yes, it's successes out of n tries, so Binomial
  no, it's events in some window of time or space, so Poisson
1c. For continuous, what range can X be in?
  between 0 and 1, Beta
  between two fixed ends with every value equally likely, Uniform
  positive only: if it's the wait for one event, Exponential. If it's a skewed hump, Gamma.
  any number including negatives: a symmetric bell around a center is Normal. Anything else (heavy tails, two humps) goes to 1d.
1d. If nothing fits I flag it and set it aside.

Step 2. Pick the model for the prior on the parameter
This is only about the unknown parameter. For MLE questions I skip this step since they only use step 4.
2a. Which parameter is unknown and what values can it take? I get this from step 1.
  Bernoulli or Binomial: theta, between 0 and 1
  Poisson: lambda, above 0
  Exponential: beta, above 0
  Normal: mu, any number
2b. How does the problem give me the prior?
  A. as numbers, so I use them as they are
  B. in words, so I translate it
  C. it doesn't, so I pick equal weights or a flat curve and say that I did
  D (new). it names a curve but doesn't give the settings (like "a Beta with mean mu0"), so I keep alpha and beta as letters
2c. Is my prior a list or a curve? The test is whether the problem names possible values for the parameter, each with a weight.
  L. yes, it's a list. I write it as {candidate: weight}.
  C. no, it's a curve. Something like "about 3, and as sure as if I'd seen..." is a curve, because it's a center plus a confidence with no candidates named.
    Ci. Pick the curve. If the problem names one I use that. If not, I filter:
      1. range: it has to live on exactly the range from 2a
      2. shape: a hump at the center I chose, or flat only if I have no idea
      3. dials: it needs a center and a strength
      4. partner: prior times likelihood should give the same kind of curve back
      So 0 to 1 gives Beta, above 0 gives Gamma, any number gives Normal.
    Before Cii, a check I added after messing up HW1 Q1: are the two numbers I was given the curve's settings, or facts about the curve?
      If it says Gamma(a, b) or "parameters a and b", those are alpha and beta and I just plug them in.
      If it says mean m and variance v, those describe the curve. I write them as E[theta] = m and Var(theta) = v and solve backwards for alpha and beta.
        Gamma (with beta as the rate): beta = m / v, then alpha = m times beta
        Beta (new): alpha + beta = m(1 - m)/v - 1, then alpha = m(alpha + beta) and beta = (1 - m)(alpha + beta)
        Normal (new): here the settings really are the mean and variance, N(mu, sigma^2). I think that's why it's easy to mix them up on the other two.
      If I'm given the SD instead of the variance, I square it first (new).
      Then I check by plugging alpha and beta back into the mean and variance formulas.
      On HW1 Q1 I read "mean 5, variance 2" as Gamma(5, 2), but Gamma(5, 2) has mean 2.5, so that was wrong.
    Cii. Fill in the two settings using the total pretend data. The first one is the total pretend events. The second is what they happened over (pretend failures for a Beta, pretend windows or pretend total time for a Gamma).
    Ciii. Check that the curve's mean matches the prior belief the problem stated (the belief, not the data). If the settings are still letters, I keep the mean equation around, like alpha/(alpha + beta) = mu0, because step 7 needs it (new).
    Civ. Write the kernel, which is the curve's formula with my numbers in and the constants dropped (same test as 4c).
      Beta: theta^(alpha - 1) (1 - theta)^(beta - 1)
      Gamma: lambda^(alpha - 1) e^(-beta lambda)

Step 3. Lay out the data
How many trials
What outcomes each trial can have (this is what 1b looks at)
What actually came out
The chance of each result, from the model's formula
Then two checks on the trials:
3a. Are they independent? Does one result change another? I look for "independently", "random sample", or "iid". If yes, 4b multiplies. If I can't find anything saying so, I flag it and ask.
3b. Do they share one parameter, or does each trial get its own? Different results are normal. A different parameter would need a reason in the problem, like rush hour or fatigue. If shared, one theta covers every trial.

Step 4. The likelihood
This only uses X's model. The prior doesn't come in until step 5. The data goes in here, not into the prior.
For a list prior I do 4a and 4b once per candidate and get one number each.
For a curve prior I do 4a and 4b once with theta left as a letter and get a formula in theta.
4a. Build X's dictionary: every value X can take, paired with its chance from the model's formula (with theta set to the candidate, or left as the letter). If there are endless values, like Poisson, the formula itself is the dictionary.
4b. Look up each observed result in the dictionary, read off its chance, and multiply them all together. That product is the likelihood.
4c. Can I drop the constants? For each factor I ask whether it has theta in it. If it doesn't, it's the same for every theta and step 6 would cancel it anyway, so I drop it and keep the kernel.
  I don't drop them if the question wants an actual probability of the data at a specific theta (like "find P(X = 3) if lambda = 2" or "compute the likelihood at theta = 0.8"), or an actual height or probability from the posterior. In that case I get the posterior's constant from its named curve and never reuse the one I dropped.
  It's safe to drop them when I'm only comparing values of theta, like for the posterior's shape or the MLE.

Step 5. Multiply by the prior
List prior: multiply number by number for each candidate.
Curve prior: prior kernel (from Civ) times likelihood kernel (from 4c), once. Group the same bases and add the exponents.

Step 6. Normalize so it adds up to 1
List prior: add up the step 5 results and divide each one by the total.
Curve prior: I don't multiply anything here. I name the curve. I match the step 5 formula to the partner's kernel and read off the new settings. It's a new curve from the same family. Watch the minus 1: lambda^19 means alpha = 20, not 19.
Why naming the curve works:
  1. Partner property (conjugacy). A partner prior kernel times the likelihood kernel has the same shape as the prior. Gamma times Poisson gives Gamma, Beta times Bernoulli gives Beta (DeGroot Theorem 7.3.1). The bases match so the exponents just add, and the product stays in the family.
  2. Naming normalizes. Every named curve comes with its own constant that makes the area 1 (for Gamma that's beta^alpha / Gamma(alpha)). Once the shape matches, that constant is the right one, so the area is 1 without computing anything. Only the shape had to be right. The constants I dropped never mattered.
  3. Naming also gives me the averages. Gamma mean = alpha / beta, Beta mean = alpha / (alpha + beta), so the posterior mean comes straight from the settings.
  4. When it doesn't work: if the prior isn't the partner (like a Uniform on 0 to 10 for lambda), or the step 5 formula doesn't match any named shape. Then there's no shortcut and I have to add things up (list) or find the area under the curve directly. With a list prior I always add and divide.
How I read the result:
  The posterior is my belief about the parameter after seeing the data. The parameter itself is one fixed number. The curve says how believable each value is.
  The settings are pretend data plus real data. Gamma(alpha + total count, beta + number of windows). Beta(alpha + successes, beta + failures).
  The posterior mean is a weighted average of the prior belief and the data average, weighted by how much each is worth (pretend size vs real size). It always lands between the two, and more data pulls it toward the data.
  Out loud: "After [data], I believe [parameter] is about [mean], and my belief is now worth [alpha + beta, or beta] trials or windows."
  It's an if-then. If the model, the shared parameter, independence and the prior all hold, then this is the belief. Each of those ifs is something to check.

Step 7 (new). Turn the posterior into one number, if the question asks for one
The posterior is the belief. The loss is what turns it into one answer. The loss doesn't change the posterior at all.
From Lecture 4: the Bayes estimate is the value a that makes the expected posterior loss E[L(theta, a) | x] as small as possible.
7a. Which loss is it? Squared error (theta - a)^2 gives the posterior mean. Absolute error |theta - a| gives the posterior median.
7b. Read that off the named curve. Gamma(alpha, beta) has mean alpha/beta. Beta(alpha, beta) has mean alpha/(alpha + beta).
7c. If the question wants a certain form, like gamma_n Xbar_n + (1 - gamma_n) mu0, rearrange to get it.
7d. If it asks what happens as n goes to infinity, take the limit.

What I want to ask
1. Is reading the question first to see which steps it wants (step 0) a good way to approach the homework?
2. For step 6, is it fine to show that the kernel matches, or do you want to see the integral for f(x)?
3. If a question asks for a Bayes estimate and doesn't say which loss, should I assume squared error?
