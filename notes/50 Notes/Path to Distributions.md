---
type: reference
parent: "[[Common Distributions]]"
domain: stats
course: "STAT 132"
status: draft
---
# Path to Distributions

The build-up from "what is a probability" to every distribution STAT 132 uses. Study top to bottom; each stage needs the ones above it. Every name links to its note and cards. For the live picture of how well you hold each one: Super+Alt+K (Knowledge Map).

## Stage 0: the ground rules
[[Experiment]] → [[Sample Space]] → [[Event]] → [[Axioms of Probability]] → [[Conditional Probability]] → [[Independent Events]]

## Stage 1: turning outcomes into numbers
[[Random variable]] → [[PMF, PDF and CDF]] → [[Expectation and Variance]]
A distribution is just "which values can X take, and how likely is each". Everything below is one specific answer to that.

## Stage 2: discrete (countable values)
[[Bernoulli Distribution]] → [[Binomial Distribution]] → [[Poisson Distribution]]; separately [[Discrete Uniform Distribution]]

## Stage 3: continuous (any value in a range)
[[Uniform distribution]] → [[Exponential distribution]] → [[Gamma Distribution]] (needs [[Gamma and Beta Functions]]); [[Beta Distribution]]; [[Normal distribution]] → [[Standard Normal Distribution]] (via [[Standardization (math)]])

## Stage 4: built from the Normal (STAT 132, weeks 4 to 6)
[[Chi-Square Distribution]] → [[t Distribution]]

## The data for each distribution
DeGroot's conventions (Exponential and Gamma use the rate β).

| Distribution     | Values     | Parameters             | P(X=k) or density f(x)                 | Mean    | Variance           | Models                                            | Built from / related                 |
| ---------------- | ---------- | ---------------------- | -------------------------------------- | ------- | ------------------ | ------------------------------------------------- | ------------------------------------ |
| Bernoulli        | 0, 1       | p                      | P(X=1)=p                               | p       | p(1−p)             | one yes/no trial                                  | Binomial with n=1                    |
| Binomial         | 0..n       | n, p                   | C(n,k) pᵏ(1−p)ⁿ⁻ᵏ                      | np      | np(1−p)            | successes in n independent trials                 | sum of n Bernoullis                  |
| Discrete uniform | a..b       | a, b                   | 1/(b−a+1)                              | (a+b)/2 | ((b−a+1)²−1)/12    | a fair die                                        |                                      |
| Poisson          | 0, 1, 2, … | λ                      | e^(−λ) λᵏ/k!                           | λ       | λ                  | counts in a fixed time or space                   | Binomial with n large, p small, np=λ |
| Uniform          | [a, b]     | a, b                   | 1/(b−a)                                | (a+b)/2 | (b−a)²/12          | "any value equally likely"                        |                                      |
| Exponential      | x > 0      | rate β                 | β e^(−βx)                              | 1/β     | 1/β²               | waiting time; memoryless                          | Gamma with α=1                       |
| Gamma            | x > 0      | α, β                   | βᵅ/Γ(α) · x^(α−1) e^(−βx)              | α/β     | α/β²               | total wait for α events; prior for a Poisson rate | sum of α Exponentials                |
| Beta             | 0 < x < 1  | α, β                   | Γ(α+β)/(Γ(α)Γ(β)) · x^(α−1)(1−x)^(β−1) | α/(α+β) | αβ/((α+β)²(α+β+1)) | an unknown proportion; prior for p                | Uniform(0,1) is Beta(1,1)            |
| Normal           | all reals  | μ, σ²                  | 1/(σ√(2π)) · e^(−(x−μ)²/(2σ²))         | μ       | σ²                 | sums and averages (CLT), measurement error        |                                      |
| Standard normal  | all reals  | none                   | same with μ=0, σ=1                     | 0       | 1                  | Z-scores                                          | Z = (X−μ)/σ                          |
| Chi-square       | x > 0      | m (degrees of freedom) | Gamma(m/2, 1/2)                        | m       | 2m                 | sample variance of normal data                    | sum of m squared standard normals    |
| t                | all reals  | m                      | (see [[t Distribution PDF]])           | 0 (m>1) | m/(m−2) (m>2)      | standardized mean when σ is unknown               | Z / √(χ²ₘ/m)                         |

## How to use this page
1. Pick the first stage where anything feels shaky in the Knowledge Map (red or grey).
2. For each concept there: read its note, then do its cards.
3. For the table: cover the right-hand columns and say them from the left-hand name. That is the exam skill ("X is Poisson(3): mean? variance?").
