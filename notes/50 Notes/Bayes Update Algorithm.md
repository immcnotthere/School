---
type: reference
parent: "[[Posterior Distribution]]"
prereqs:
  - "[[Prior Distribution]]"
  - "[[Likelihood Function]]"
  - "[[Kernel of a Distribution]]"
  - "[[Conjugate Prior]]"
domain: stats
course: "STAT 132"
status: draft
mastery: 0
---
# Bayes Update Algorithm

Jacob's six-step procedure, built and approved over 2026-10-01 to 2026-10-04 (free throws, then the help desk). Each step says what it receives and what it hands to the next one. Exponents are written with ^ so they stay readable.

Flowchart for steps 1 and 2: [[2026-10-04 Flowchart - Steps 1 and 2 model picker]].

## Step 1. Select the model for X (one result)
Ask these of the data, in order.
- **1a. What does one result look like?** (pick one)
  - A. Yes or no (1 or 0) → **Bernoulli**. Done.
  - B. A whole-number count → go to 1b.
  - C. A number on a continuous scale → go to 1c.
  - D. None of these (3+ categories, etc.) → go to 1d.
- **1b. Count: is there a fixed maximum?**
  - Yes, successes out of n tries → **Binomial**
  - No, events in a window → **Poisson**
- **1c. Continuous: what range can X take?**
  - Between 0 and 1 → **Beta**
  - Between two fixed ends, all values equally likely → **Uniform**
  - Positive only → which shape? Waiting time for one event → **Exponential**. Skewed hump → **Gamma**.
  - Any number, negatives included → which shape? Symmetric bell around a center → **Normal**. Anything else (heavy tails, several humps) → 1d.
- **1d. Out-of-scope flag:** if nothing fits, flag it and set it aside.

## Step 2. Determine the model for the prior distribution of the parameter
Only the unknown parameter. Skip this step for MLE questions (they keep only step 4).
- **2a. Which parameter is unknown, and what values can it take?** (lookup from step 1)
  - Bernoulli/Binomial → θ, between 0 and 1. Poisson → λ, above 0. Exponential → β, above 0. Normal → μ, any number.
- **2b. How does the problem give the prior?**
  - A. As numbers → use as is. ([[Prior Given as Numbers]])
  - B. In words → translate. ([[Prior Given in Words]])
  - C. Not given → choose equal weights or a flat curve, and say so. ([[Prior Not Given (Choose Equal Weights)]])
- **2c. Is your prior a list or a curve?** Test: does the problem name possible values of the parameter, each with a weight?
  - **L. Yes → list:** write `{candidate: weight}`.
  - **C. No → curve:** ("about 3, as sure as if..." is a curve: a center plus confidence, no candidates named)
    - **Ci. Select the curve.** If the problem names one, use it. Otherwise filter by: 1. range (lives exactly on 2a's range); 2. shape (a hump at the center you choose; flat only for "no idea"); 3. dials (a center and a strength); 4. partner (prior × likelihood gives the same curve back). Result: 0 to 1 → **Beta**. Above 0 → **Gamma**. Any number → **Normal**.
    - **Prenote to Cii (flag): what are the two numbers the problem gave?** "Gamma(a, b)" or "parameters a and b" are the settings α and β: plug them in. "Mean m and variance v" are facts about the curve, not its settings: solve back for α and β. Gamma (rate β): β = m / v, then α = m × β. Check by putting α and β back into mean = α/β and variance = α/β². (Caught on HW1 Q1, 2026-10-05: "mean 5, variance 2" misread as Gamma(5, 2), which has mean 2.5.)
    - **Cii. Fill its two blanks with the TOTAL pretend data:** first = total pretend events, second = the total they happened over (pretend failures for Beta; pretend windows or pretend total time for Gamma).
    - **Ciii. Check:** the curve's mean equals the stated prior belief (not the data).
    - **Civ. Write its kernel:** the curve's form (Kernels Table 1) with Cii's numbers plugged in, constants dropped (4c test). Beta: θ^(α−1) (1−θ)^(β−1). Gamma: λ^(α−1) e^(−βλ).

## Step 3. Identify the sample data
- Trials
- Possible outcomes per trial (this is what 1b reads)
- What came out
- Chance of a result (from the model's formula)
- **Two tests on the trials:**
  - **3a. Independent?** Does one trial's result change another's? Look for "independently," "random sample," "i.i.d." Yes means 4b multiplies. None found: flag it and ask.
  - **3b. One shared parameter, or a different parameter per trial?** Are all trials drawn from the same hypothetical global population parameter? Different results are expected; a different parameter needs a stated reason (rush hour, fatigue, changed conditions). Shared means one θ covers every trial.

## Step 4. Likelihood
X's model only; the prior does not enter until step 5.
- **List prior:** do 4a and 4b once per candidate, giving one number each.
- **Curve prior:** do 4a and 4b once with θ left as a letter, giving a formula in θ.
- **4a. Build X's dictionary:** `{each value X can take: its chance from the model's formula with θ = this candidate (or the letter)}`. Endless keys (Poisson) mean the formula is the dictionary.
- **4b. Use each observed result as a key,** read the chance, multiply them. The product is the likelihood.
- **4c. Drop the constants?** Test each factor: does it contain θ? If not, it treats every θ the same and step 6 cancels it, so drop it to get the kernel.
  - **Do NOT drop when the question asks for** an actual chance of the data at a specific θ ("find P(X = 3) if λ = 2", "compute the likelihood at θ = 0.8"), or an actual height or probability from the posterior. Get the posterior's own constant from its named curve; never reuse the dropped one.
  - **Safe to drop when** you are only comparing values of θ (the posterior's shape, or the MLE).

## Step 5. Multiply by the prior (the unnormalized posterior)
- **List prior:** number × number, per candidate.
- **Curve prior:** prior kernel (2c-Civ) × likelihood kernel (4c), formula × formula, once. Group like with like and add exponents.

## Step 6. Normalize to get the posterior (make the total equal 1)
- **List prior:** add the step 5 results, then divide each one by the total.
- **Curve prior:** no multiplying. Name the curve: match the step 5 formula to the partner's kernel shape and read off its settings. That is a **new** curve of the same family. Watch the minus-1 trap (λ^19 means α = 20, not 19).

**Flag: what lets us use the curve's settings to normalize and to average.**
1. **Partner property (conjugacy).** Partner prior kernel × likelihood kernel has the same shape as the prior: Gamma × Poisson gives Gamma, Beta × Bernoulli gives Beta (DeGroot Theorem 7.3.1; [[STAT 132 Kernels]] Table 3). Same bases add exponents, so the product never leaves the family.
2. **Naming normalizes.** Every named curve comes with its own constant that makes its area exactly 1 (Gamma: β^α / Γ(α)). Once the shape matches Gamma(α, β), that constant is the right one, so the area is 1 without computing anything. Only the shape had to be right; the constants we dropped never mattered.
3. **Naming also gives the averages.** A named curve has known formulas ([[STAT 132 Distribution Sheets]]): Gamma mean = α / β, Beta mean = α / (α + β). So the posterior mean comes straight from the settings.
4. **When it does NOT work:** a prior that is not the partner (e.g. Uniform on 0 to 10 for λ), or a step 5 formula that matches no named shape. Then the shortcut is gone: add (list) or find the area under the curve directly. On a list prior you always add and divide.

**How to interpret the result.**
- The posterior is your belief about the parameter after the data. The parameter itself is one fixed number; the curve says how believable each value is.
- The settings are **pretend data + real data**: Gamma(α + total count, β + number of windows); Beta(α + successes, β + failures).
- The posterior mean is a **weighted average** of the prior belief and the data's average, weighted by how much each is worth (pretend size vs real size).
- It always lands between the prior belief and the data's average; more data pulls it toward the data.
- Read it out loud: "After [data], I believe [parameter] is about [mean]. My belief is now worth [α + β or β] [trials or windows]."
- It is a conditional statement: if the model, the shared parameter, independence and the prior all hold, then this is the belief. Each "if" is an assumption to check.

## Worked runs
**Free throws (list prior).** Claim 80%, suspicion 50%; prior {0.8: 0.3, 0.5: 0.7}; 4 makes in 5 independent shots.
- 1: yes/no → Bernoulli(θ). 2: θ in 0 to 1; as numbers; list.
- 4: θ = 0.8 → 0.8^4 × 0.2 = 0.082; θ = 0.5 → 0.5^5 = 0.031.
- 5: 0.3 × 0.082 = 0.0246; 0.7 × 0.031 = 0.0217.
- 6: total 0.0463 → posterior {0.8: 0.531, 0.5: 0.469}. Exact likelihoods give 0.529 / 0.471.
- Odds view: prior odds 0.3 / 0.7 = 0.43, × likelihood ratio 2.6 = 1.12 → 53%.

**Help desk (curve prior).** Calls in 4 one-hour windows: 3, 5, 2, 4. Prior "about 3 per hour, as sure as 6 calls in 2 hours."
- 1: whole-number count, no maximum → Poisson(λ).
- 2: λ above 0; in words; no values named → curve → Gamma → Gamma(6, 2), mean 3 → kernel λ^5 e^(−2λ).
- 3: 4 trials; outcomes 0, 1, 2, ...; chance e^(−λ) λ^x / x!; independent; one shared λ.
- 4: four lookups multiplied, 1/34,560 dropped → λ^14 e^(−4λ) (λ^(total count) e^(−(number of windows)λ)).
- 5: λ^5 e^(−2λ) × λ^14 e^(−4λ) = λ^19 e^(−6λ).
- 6: match λ^(α−1) e^(−βλ) → **Gamma(20, 6)**, mean 20 / 6 ≈ 3.33 calls per hour. Pretend 6 calls / 2 hours + real 14 calls / 4 hours = 20 / 6. Weighted: (2 × 3 + 4 × 3.5) / 6 = 3.33.

## Next
Run the same six steps on Binomial, Exponential and Normal problems (one new word problem each).

## Concepts
[[Parameter Space]], [[Data Model vs Prior Model]], [[List Prior vs Curve Prior]], [[Prior as Pretend Data]], [[One Shared Parameter (Identically Distributed)]], [[Zero Prior Weight Is Never Updated]], [[Posterior Odds Equal Prior Odds Times Likelihood Ratio]], [[When Not to Drop Constants]], [[Naming the Curve Normalizes (Kernel Matching)]], [[Posterior Mean as a Weighted Average]], [[Posterior as a Conditional Statement]]

## Cards that depend on this note
If a step here changes, revise these cards (their Notes column says `dep: [[Bayes Update Algorithm]]`). Rebuild this list with a grep for that tag.
- [[STAT 132 Cards - Bayes Rule]] / Bayes' Rule: Free throws: likelihood times prior is 0.0246 for the 80% shooter and 0.0217 for the 50% shooter. What is the posterior for the 80% shooter?
- [[STAT 132 Cards - Bayes Rule]] / Likelihood (Bayes' Rule): Which step of the Bayes update algorithm computes the likelihood?
- [[STAT 132 Cards - Bayes Rule]] / Evidence (Bayes' Rule): Which step of the Bayes update algorithm divides by the evidence $\mathbb{P}(B)$?
- [[STAT 132 Cards - Bayes Rule]] / Evidence (Bayes' Rule): Which step of the Bayes update algorithm multiplies the likelihood by the prior?
- [[STAT 132 Cards - Beta Distribution]] / Beta Distribution: What is the Beta kernel?
- [[STAT 132 Cards - Beta Distribution]] / Beta Distribution: Read $p^8(1-p)^2$ as a Beta.
- [[STAT 132 Cards - Beta Distribution]] / Beta Distribution: How do you read Beta$(\alpha, \beta)$ as pretend data?
- [[STAT 132 Cards - Beta Distribution]] / Beta Distribution: With a Beta prior and x successes in n Bernoulli trials, what is the posterior?
- [[STAT 132 Cards - Beta Distribution]] / Beta Distribution: Flat Beta(1, 1) prior, 4 makes in 5 shots: what is the posterior?
- [[STAT 132 Cards - Binomial Distribution]] / Binomial Distribution: What is the Binomial likelihood kernel in p for x successes out of n?
- [[STAT 132 Cards - Binomial Distribution]] / Binomial Distribution: With a Beta$(\alpha, \beta)$ prior, what is the posterior after x successes in n Binomial tries?
- [[STAT 132 Cards - Exponential Distribution]] / Exponential distribution: What is the Exponential likelihood kernel for waits $x_1, \dots, x_n$?
- [[STAT 132 Cards - Exponential Distribution]] / Exponential distribution: With a Gamma$(\alpha, b)$ prior and Exponential waits $x_1, \dots, x_n$, what is the posterior?
- [[STAT 132 Cards - Gamma Distribution]] / Gamma Distribution: What is the Gamma kernel?
- [[STAT 132 Cards - Gamma Distribution]] / Gamma Distribution: Read the posterior kernel $\lambda^{19} e^{-6\lambda}$ as a Gamma.
- [[STAT 132 Cards - Gamma Distribution]] / Gamma Distribution: How do you read Gamma$(\alpha, \beta)$ as pretend data for a rate?
- [[STAT 132 Cards - Gamma Distribution]] / Gamma Distribution: Which data models take a Gamma as their partner prior?
- [[STAT 132 Cards - Gamma Distribution]] / Gamma Distribution: Gamma vs Beta as a prior: how do you choose?
- [[STAT 132 Cards - Gamma and Beta Functions]] / Gamma and Beta Functions: Where does $\Gamma$ appear in the Gamma distribution?
- [[STAT 132 Cards - Gamma and Beta Functions]] / Gamma and Beta Functions: Why does every distribution need a normalizing constant?
- [[STAT 132 Cards - Lecture_01 Prep]] / Function as a Dictionary: How can a function act like a dictionary?
- [[STAT 132 Cards - Lecture_01]] / Parametric vs Nonparametric: Besides the distribution's family, what other assumptions can an inference make about the data?
- [[STAT 132 Cards - Lecture_01]] / Statistic (inference): How can a function of the data behave like a dictionary lookup?
- [[STAT 132 Cards - Lecture_01]] / Point Estimate vs Interval Estimate: In the Bayes update algorithm, where does a point estimate come from?
- [[STAT 132 Cards - Lecture_01]] / Point Estimate vs Interval Estimate: In the Bayes update algorithm, where does an interval estimate come from?
- [[STAT 132 Cards - Lecture_01]] / Parameter Space: Why does knowing the parameter space matter?
- [[STAT 132 Cards - Normal Distribution]] / Normal distribution: What is the Normal likelihood kernel in $\mu$ (with $\sigma^2$ known)?
- [[STAT 132 Cards - Normal Distribution]] / Normal distribution: Which prior is the partner of Normal data with known variance?
- [[STAT 132 Cards - Poisson Distribution]] / Poisson Distribution: What is the Poisson likelihood kernel in $\lambda$ for counts $x_1, \dots, x_n$?
- [[STAT 132 Cards - Poisson Distribution]] / Poisson Distribution: With a Gamma$(\alpha, \beta)$ prior and Poisson counts $x_1, \dots, x_n$, what is the posterior?
- [[STAT 132 Cards - Poisson Distribution]] / Poisson Distribution: Help desk: prior Gamma(6, 2), calls 3, 5, 2, 4 in four hours. What is the posterior?
- [[STAT 132 Cards - Uniform Distribution]] / Uniform Distribution (Continuous): Why is a Uniform(0, 10) prior risky for a rate?
