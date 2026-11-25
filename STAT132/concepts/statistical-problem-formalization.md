# Statistical Problem Formalization
## Semantic-to-Mathematical Translation

Recorded: 2026-11-25. Origin: Discussion 01 study conversation.
Status: developing; independent recall not yet verified.

### Learning objective
Translate a verbal statistical problem into mathematical notation before computing. Identify observations, unknown parameters, distribution roles, and requested output.

### Recognition cues
| Verbal cue | Mathematical notation | Role |
|---|---|---|
| The unknown parameter follows a Beta distribution | $\theta\sim\mathrm{Beta}(\alpha,\beta)$ | Prior, if specified before data |
| The observations follow an exponential distribution with rate lambda | $X_i\mid\lambda\sim\mathrm{Exp}(\lambda)$ | Sampling model |
| Observed values are 2, 2.5, 3 | $x=(2,2.5,3)$ | Realized data |
| Write the likelihood | $L(\lambda;x)=\prod_i f(x_i\mid\lambda)$ | Function of parameter, assuming conditional independence |
| Find the posterior | $\pi(\theta\mid x)\propto L(\theta;x)\pi(\theta)$ | Updated parameter density |

### Notation
- $\sim$: is distributed as, not conditioning.
- $\mid$: given; the quantity to the right is held fixed in the conditional model, even if its actual value is unknown.
- $X_i$: random observation; $x_i$: realized observation.
- $\pi$: conventional function name for prior or posterior density, not the numerical constant pi.
- Distribution: probability law; PDF: explicit density representing a continuous law. Discrete laws use PMFs.

Example: $\theta\sim\mathrm{Beta}(2,3)$ is equivalent to $\pi(\theta)=12\theta(1-\theta)^2$ for $0<\theta<1$, zero elsewhere.

### Procedure
1. Identify what is observed and what is unknown.
2. Identify which variable each named distribution describes.
3. Write the distribution statement and its PDF or PMF.
4. Identify the requested object; do not invent a prior if only likelihood is requested.
5. For conditionally independent observations, multiply sampling densities to obtain the likelihood.
6. If posterior is requested, multiply by the prior and normalize.

### Common misconceptions to review
- A named distribution is not inherently a prior or likelihood.
- The prior does not carry observed data; the likelihood supplies evidence.
- Every valid prior can be updated when the posterior is well-defined. Conjugacy means the posterior remains in the same distribution family, not that other priors cannot update.
- A likelihood is a function of the parameter with data fixed, not generally a normalized parameter density.

### Recall checks
1. Translate: the unknown success probability has a Beta(2,3) prior.
2. Translate: study times are exponential with unknown rate lambda.
3. Explain the difference between tilde and vertical bar.
4. Distinguish prior distribution from prior PDF and explain pi.
5. For independent exponential observations 2, 2.5, 3, construct the likelihood without a prior.

Answers: 1. $\theta\sim\mathrm{Beta}(2,3)$. 2. $X_i\mid\lambda\sim\mathrm{Exp}(\lambda)$. 3–4. See notation above. 5. $L(\lambda;x)=\lambda^3e^{-7.5\lambda}$ for $\lambda>0$.

Source note: This module records the study conversation and general mathematical notation; the exact Discussion 01 worksheet text was not independently verified.
