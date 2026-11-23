---
parent: "[[STATS 131]]"
type: study
status: draft
---
## 1. Probability Foundations & Information Updating

- **Partitioning the Sample Space**
    - Recognizing that voters are either in set $A$ (voted for A) or $A^c$ (voted for B)
    - **Worked Example:** Since $Pr(A) = 0.3$, the partition for B must be $Pr(A^c) = 0.7$
- **Bayesian Inference**
    - Calculating the posterior probability $Pr(A|W)$ using $Pr(A|W) = \frac{Pr(W|A)Pr(A)}{Pr(W)}$
    - **Worked Example:** $Pr(A|W) = (0.7 \times 0.3) / 0.35 = 0.6$
- **Marginalization of Evidence**
    - Calculating $Pr(W)$ using the Law of Total Probability: $Pr(W) = Pr(W|A)Pr(A) + Pr(W|A^c)Pr(A^c)$
    - **Worked Example:** $(0.7 \times 0.3) + (0.2 \times 0.7) = 0.21 + 0.14 = 0.35$
- **Translation of Contextual Assumptions**
    - Converting the statement "people are honest" into the mathematical assumption that the survey response directly reflects the vote
    - **Worked Example:** If a person says they voted for A, event $W$ is defined as perfectly linked to the true event $A$

## 2. Continuous Bivariate Distributions (Multivariate Calculus)

- **Boundary Analysis**
    - Interpreting inequalities like $0 < x \leq y < 2$ to define the region of integration (a triangle in the $xy$-plane)
    - **Worked Example:** The region is bounded by the vertical $y$-axis ($x=0$), the diagonal line $y=x$, and the horizontal line $y=2$
- **Normalization of Joint P.D.F.s**
    - Solving for the constant $c$ by setting the double integral $\int \int f(x,y) , dA = 1$
    - **Worked Example:** $\int_{0}^{2} \int_{x}^{2} cx , dy, dx = 1$ yields $c = 3/4$
- **Deriving Marginal Distributions**
    - Integrating out the "unwanted" variable; finding $f(x)$ by integrating $f(x,y)$ with respect to $dy$ over the range $[x, 2]$
    - **Worked Example:** $f(x) = \int_{x}^{2} \frac{3}{4}x , dy = \frac{3}{4}x(2-x)$
- **Testing for Independence via Support**
    - Recognizing that if the limits of $x$ depend on $y$, the variables are inherently dependent regardless of the functional form
    - **Worked Example:** Because $x \leq y$, you cannot separate $f(x,y)$ into $f(x)g(y)$ — the support is not a rectangle
- **Conditional Probability Density Functions**
    - Constructing $f(y|x) = \frac{f(x,y)}{f(x)}$ to find probabilities over a specific interval of $Y$ given $X=1$
    - **Worked Example:** Integrating $f(y|1)$ over $4/3 < Y < 2$ gives the result $2/3$

## 3. Univariate Normal Distribution & Expected Values

- **Z-Score Transformation**
    - Standardizing a normal variable $X \sim N(150, 15^2)$ using $Z = \frac{X - \mu}{\sigma}$ to find probabilities for values like $X > 180$
    - **Worked Example:** $Z = (180 - 150) / 15 = 2.0$
- **Complementary Probability**
    - Using the standard normal table to find $Pr(Z > z)$ by calculating $1 - \Phi(z)$
    - **Worked Example:** $1 - \Phi(2) = 1 - 0.9772 = 0.0228$
- **Expected Value of a Binomial Count**
    - Identifying that "overflows" in 1000 trials follow a Binomial distribution, where the expected number is $n \cdot p$
    - **Worked Example:** Expected overflows $= 1000 \times p$

## 4. Asymptotic Theory (Central Limit Theorem)

- **Distribution of the Sample Mean**
    - Understanding that $\bar{X}$ is approximately normal $N!\left(\mu, \frac{\sigma^2}{n}\right)$ for large $n$
    - **Worked Example:** Even if individual scores are skewed, the average of 100 students forms a bell curve centered at the true mean
- **Margin of Error Calculations**
    - Setting up the inequality $Pr(|\bar{X} - 75| \leq 5) \geq 0.95$
    - **Worked Example:** Set the standard error to match the $Z = 1.96$ threshold
- **Solving for Sample Size ($n$)**
    - Using the Z-value for a 95% confidence interval ($z = 1.96$) to solve for $n$ in the standard error formula $\frac{\sigma}{\sqrt{n}}$
    - **Worked Example:** If desired margin of error is 5, solve $\frac{\sigma}{\sqrt{n}} = \frac{5}{1.96}$ for $n$

## 5. Transformations & Sums of Random Variables

- **The Transformation Method**
    - Finding the P.D.F. of $Y = e^{X_1}$ using $f_Y(y) = f_{X_1}(g^{-1}(y)) \cdot \left|\frac{d}{dy} g^{-1}(y)\right|$
    - **Worked Example:** If $X$ is bulb life and $Y = e^X$, use the derivative of the inverse function to transform the original density
- **Recognizing Exponential & Gamma Relationships**
    - Identifying that the sum of two i.i.d. $\text{Exponential}(\lambda)$ variables results in a $\text{Gamma}(2, \lambda)$ distribution, also known as an Erlang distribution
    - **Worked Example:** Total time $X_1 + X_2$ for two bulbs follows a Gamma distribution with two "stages"
- **Convolution Integrals**
    - Formally deriving the P.D.F. of $Y = X_1 + X_2$ by integrating the joint density $f(x_1, y - x_1)$
    - **Worked Example:** Integrate $f(x) \cdot f(y-x)$ over all lifetimes that could sum to $Y$

## 6. Discrete-Time Markov Chains (Extra Credit)

- **Transition Matrix Construction**
    - Organizing "On Time" and "Late" probabilities into a $2 \times 2$ stochastic matrix where rows sum to 1
    - **Worked Example:** Rows represent "today," columns represent "tomorrow"; e.g. $0.7$ for staying late, $0.4$ for becoming late
- **Path Probabilities**
    - Calculating the probability of a specific sequence ($\text{Late} \to \text{Late} \to \text{Late}$) given an initial state (On Time) using the multiplication rule for Markov chains
    - **Worked Example:** $0.7 \times 0.7 \times 0.7 = 0.343$