---
type: reference
domain: stats
course: "STAT 132"
status: draft
---
# Todo: shooter example audit and likelihood follow-ups (2026-10-01)

Source: the evening chat working the free-throw example (prior 0.3 on θ = 0.8, 0.7 on θ = 0.5; 4 makes in 5 independent shots). Parked here because it is too deep for Todoist. Practice problems come first; work this list after.

## Where the example stopped

- [x] Step 5: 0.3 × 0.082 = 0.0246 and 0.7 × 0.031 = 0.0217 (done 2026-10-03)
- [x] Step 6: add the two, divide each by the total (posterior 0.531 / 0.469, done 2026-10-03). Read the result out loud as a posterior ("after 4 of 5, I believe the friend's claim __%").

## The procedure as it stands (candidate for a permanent note)

1. Identify the model (X ~ Bernoulli(θ)).
2. Identify the θ candidates and the prior on each.
3. Identify the sample data:
   - number of trials
   - possible outcomes per trial (this line is the model clue: 2 outcomes = Bernoulli, counts 0, 1, 2, ... = Poisson, any positive number = Exponential)
   - what came out (each result, or the total)
   - chance of a result (from the model)
   - 3a. Independent? Look for "independently", "random sample", "i.i.d." Yes means 4b multiplies. None found: flag it and ask.
4. For each θ candidate:
   - 4a. Fill X's dictionary (the pmf) with that θ.
   - 4b. Look up each data value and multiply. The product is the likelihood (score).
5. Multiply each likelihood by that candidate's prior.
6. Normalize: add, then divide each by the total. That is the posterior.

- [ ] Decide: is this the "rules 1-5" list, or did you mean a different list? (It has 6 steps.)
- [x] (done 2026-10-04: [[Bayes Update Algorithm]]) Make it a permanent note (e.g. "Bayes Update - Discrete Candidates") with each step written as given / what changes / what the next step receives.
- [ ] Test the sample-data template on a Poisson and an Exponential problem from the practice set. Does every line still fill?

## Ideas settled in the chat (not yet carded)

Already carded (Ladder 07 Likelihood, commit 8c12809): the bar in L(θ | x), L(θ; x), input of L, f vs L, sums to 1 or not, wording sentence, no prior in likelihood.

- [ ] Card: `~` means "follows the distribution" (X ~ Bernoulli(θ)). Elsewhere it can mean "approximately" or "not".
- [ ] Card: X (capital) = the slot before the result; x (lowercase) = the value it took; the pmf = the dictionary {1: θ, 0: 1 − θ}.
- [ ] Card: the model lives in X (the line X ~ Bernoulli(θ)); P is generic and reads X's dictionary.
- [ ] Card: multiplying comes from independence, not from the model. Messy formulas (Poisson, Exponential) change the lookup, not the multiply.
- [ ] Card: θ is the outcome's true chance, not a belief. The belief about θ is the prior; prior and likelihood combine only in step 5.
- [ ] Card: definition of a probability: outcomes cover everything and cannot happen together; each number is 0 or more; they add to 1.
- [ ] Card: a likelihood list fails condition 2 (0.082 + 0.031 = 0.113; one-shot column 0.8 + 0.5 = 1.3). Step 6 is what makes it pass.
- [ ] Card: in code, Likelihood(θ, data) == Probability(data, θ); Probability(θ, data) is the posterior and needs the prior.
- [ ] Card: MLE uses the likelihood with no prior (picks θ with the highest likelihood); Bayes adds the prior.
- [ ] Card: the sample space of 5 shots is 2^5 = 32 sequences (sequences, not permutations).
- [ ] Check the 6 Ladder 07 cards show up in Decks (the helper did not run `deck_import.py apply`).

## Audit: where Claude failed in this chat

1. Dropped your first instruction (problem + steps at the top of every reply) after one message, until you called it out.
2. Cut your "possible outcomes per trial" line when simplifying, then wrote a template that was hard to read.
3. Used undefined, loose words: "let the data pick what to multiply", "X is the shot", "attaches to", "held fixed". Each cost a round trip.
4. Claimed your slides use L(θ) without checking. Lecture 3 only writes f(x | θ).
5. Flagged L(θ; x) (the bar does not mean "given") late, after you had already built on L(θ | x).
6. Said f and L give "the same number" without first saying they are different functions. You had to push for the function vs value split.
7. Answered your code-framed questions in prose first; the code view (dictionaries, constants, function signatures) landed best and should come first.

- [ ] Fix for next time: define every term in code or in one plain line before using it; check the course PDF before naming notation; keep the pinned problem + steps until you say the problem is done.

## Do tomorrow

- [ ] STAT 132 Quiz 1 on Canvas, due Fri 10-02 by 23:59 (24-hour grace period).
