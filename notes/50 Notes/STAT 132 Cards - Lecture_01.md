---
type: reference
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "Lecture_01"
tags:
  - decks
---
 # STAT 132 Cards - Lecture_01 Probability Review & Intro to Inference

## Random Experiment
| Front | Back | Notes |
| --- | --- | --- |
| What is a random experiment? %%dk:t:6l6azi%% | **An action or process that leads to one of several possible outcomes.** *Side note, not tested: You know the possible outcomes, but not which one will happen.* | p.2; definition |
| Give one example of a random experiment. | Rolling a die; tossing a coin 10 times. | p.2; worked example |

## Sample Space and Events
| Front | Back | Notes |
| --- | --- | --- |
| What is the sample space $\Omega$? %%dk:t:sphyhp%% | **The set of all possible outcomes** *Side note, not tested: of the experiment.* | p.2; definition |
| You toss a coin twice. Write the sample space $\Omega$. | $\{HH, HT, TH, TT\}$ | p.2; worked example |
| What is an event? %%dk:t:s4d952%% | **A subset of $\Omega$** (a set of outcomes). | p.2; definition |
| Two coin tosses: write the event "at least one head". | $\{HH, HT, TH\}$ | p.2; worked example |

## Probability Measure
| Front | Back | Notes |
| --- | --- | --- |
| What is a probability measure $\mathbb{P}$? | **A function that assigns a probability to each event**, obeying three rules. *Read aloud: "blackboard P."* | p.2; definition |
| Probability measure, rule 1: what range must $\mathbb{P}(A)$ fall in? | $0 \le \mathbb{P}(A) \le 1$ for any event A. *Read aloud: "P of A is between zero and one."* | p.2; formula |
| Probability measure, rule 2: what is $\mathbb{P}(\Omega)$? | **1.** *Side note, not tested: Some outcome in the sample space always happens.* | p.2; formula |

## Axioms of Probability
| Front | Back | Notes |
| --- | --- | --- |
| What are the three axioms a probability measure $\mathbb{P}$ must satisfy? %%dk:t:p2pwu9%% | 1) $0 \le \mathbb{P}(A) \le 1$ for any event $A$; 2) $\mathbb{P}(\Omega) = 1$; 3) for disjoint $A, B$, $\mathbb{P}(A \cup B) = \mathbb{P}(A) + \mathbb{P}(B)$. | p.2; definition |
| For disjoint events $A$ and $B$, what is $\mathbb{P}(A \cup B)$? %%dk:t:p1n5zr%% | $\mathbb{P}(A) + \mathbb{P}(B)$. | p.2; formula |

## Conditional Probability
| Front | Back | Notes |
| --- | --- | --- |
| What is the formula for $\mathbb{P}(A \mid B)$ when $\mathbb{P}(B) > 0$? %%dk:t:m2kd5k%% | $\mathbb{P}(A \mid B) = \dfrac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)}$. | p.2; formula |
| What condition is required for $\mathbb{P}(A \mid B)$ to be defined? %%dk:t:950g71%% | $\mathbb{P}(B) > 0$. | p.2; definition |
| In words, what does $\mathbb{P}(A \mid B)$ mean? | **The probability that A happens, given that B has already happened.** *Read aloud: "P of A given B."* | p.2; definition |
| You see $\dfrac{\mathbb{P}(A \cap B)}{\mathbb{P}(B)}$. What is this quantity called? | **The conditional probability of A given B**, $\mathbb{P}(A \mid B)$. | p.2; recognition |
| Why does conditional probability divide by $\mathbb{P}(B)$? | **Knowing B happened shrinks the world to B.** *Side note, not tested: Dividing by $\mathbb{P}(B)$ rescales so the chances inside B add to 1.* | p.2; motivation |

## Bayes' Rule
| Front | Back | Notes |
| --- | --- | --- |
| What is Bayes' rule for $\mathbb{P}(A \mid B)$? %%dk:t:hgslb1%% | $\mathbb{P}(A \mid B) = \dfrac{\mathbb{P}(B \mid A)\mathbb{P}(A)}{\mathbb{P}(B)}$. | p.2; formula |
| How is the denominator $\mathbb{P}(B)$ expanded in Bayes' rule using $A$ and $A^c$? %%dk:t:634mbg%% | $\mathbb{P}(B) = \mathbb{P}(B \mid A)\mathbb{P}(A) + \mathbb{P}(B \mid A^c)\mathbb{P}(A^c)$. | p.2; formula |

## Random variable
| Front | Back | Notes |
| --- | --- | --- |
| A random variable is a function. From what, to what? %%dk:t:klpldt%% | **From outcomes ($\Omega$) to real numbers.** *Read aloud: "X maps Omega to the real numbers."* | p.2; definition |
| Two coin tosses, $X$ = number of heads: what are $X(HT)$ and $X(HH)$? | $X(HT) = 1$, $X(HH) = 2$ | p.2; definition |
| Why is a random variable called a function? | **It is a rule: each outcome goes in, exactly one number comes out.** *Side note, not tested: it is not random and not a variable; the randomness is in which outcome happens.* | p.2; motivation |

## Discrete Random Variable
| Front | Back | Notes |
| --- | --- | --- |
| What kind of values does a discrete random variable take? | **Countable values: you can list them, like 0, 1, 2, ...** | p.2; definition |

## Continuous Random Variable
| Front | Back | Notes |
| --- | --- | --- |
| What kind of values does a continuous random variable take? | **Any value in an interval of $\mathbb{R}$**, e.g. any time between 0 and 10 minutes. | p.2; definition |

## Discrete vs Continuous Random Variable
| Front | Back | Notes |
| --- | --- | --- |
| How do you decide whether a random variable is discrete or continuous? %%dk:t:44q1cb%% | **Ask whether you can list its values one by one.** Yes: discrete. *Side note, not tested: No, it fills an interval: continuous.* | p.2; discrimination |
| Your bus wait in minutes: discrete or continuous? | Continuous: it can be any value in an interval. | p.2; discrimination |
| Calls to a help desk in one hour: discrete or continuous random variable? | **Discrete:** whole-number counts 0, 1, 2, ... (no hour has 2.5 calls). | p.2; discrimination |

## Probability Mass Function
| Front | Back | Notes |
| --- | --- | --- |
| A PMF is used for which kind of random variable? | **Discrete.** | p.2; definition |

## Probability density function
| Front | Back | Notes |
| --- | --- | --- |
| A PDF is used for which kind of random variable? | **Continuous.** | p.2; definition |
| Why does a continuous random variable need an integral to give a probability? | **Any single exact value has probability 0**, so chance only exists over a range: the area under f. | p.2; motivation |
| In $\mathbb{P}(a \le X \le b) = \int_a^b f(x)\,dx$, where do a and b come from? | **The question's range**, e.g. "between 2 and 5 minutes" gives a = 2, b = 5. A one-sided question uses the support's edge or $\pm\infty$. | p.2; definition |
| What does the height $f(x)$ of a PDF measure? | **Density: chance per unit of x, not a chance itself.** *Side note, not tested: It can be above 1.* | p.2; definition |

## Cumulative Distribution Function
| Front | Back | Notes |
| --- | --- | --- |
| CDF vs PMF or PDF: what does the CDF give that they do not? | **A running total: the chance X is at most x.** The PMF and PDF describe one point (a chance or a height). | p.2; discrimination |

## PMF, PDF and CDF
| Front | Back | Notes |
| --- | --- | --- |
| What does the PMF $f(x)$ give for a discrete random variable? %%dk:t:95nzg6%% | $f(x) = \mathbb{P}(X = x)$. *Read aloud: "f of x equals the probability that X equals x."* | p.2; definition |
| How does a continuous random variable's PDF $f(x)$ relate to $\mathbb{P}(a \le X \le b)$? %%dk:t:c0f78%% | $\mathbb{P}(a \le X \le b) = \int_a^b f(x)\,dx$: the area under f from a to b. *Read aloud: "the integral from a to b of f of x d x."* | p.2; formula |
| What is the CDF $F(x)$ of a random variable? %%dk:t:p02mzl%% | $F(x) = \mathbb{P}(X \le x)$. *Read aloud: "capital F of x equals the probability that X is at most x."* | p.2; definition |

## Expectation
| Front | Back | Notes |
| --- | --- | --- |
| In words, what is the expectation $E[X]$? | **The long-run average of X.** | p.3; definition |
| What other name and symbol does $E[X]$ go by? | **The mean of X, often written $\mu$.** | p.3; notation |
| Fair six-sided die: what is $E[X]$? | $(1+2+3+4+5+6) \cdot \frac{1}{6} = \frac{21}{6} = 3.5$. | p.3; worked example |
| Why is $E[X] = 3.5$ for a die fine, though no roll shows 3.5? | **$E[X]$ is a long-run average, not a value X has to take.** | p.3; motivation |
| A game pays \$10 with chance 0.2 and \$0 otherwise. What is the expected payout? | $10(0.2) + 0(0.8) = \$2$. | p.3; worked example |
| Why does continuous $E[X]$ use an integral instead of a sum? | **There are endlessly many values, so you add up value times height times a tiny width.** *Side note, not tested: The integral is that sum.* | p.3; motivation |
| In $E[X] = \int x f(x)\,dx$, what plays the role that $\mathbb{P}(X = x)$ plays in the discrete sum? | **$f(x)\,dx$**: height times a tiny width, the chance of a tiny slice. | p.3; assembly |

## Variance (Math)
| Front | Back | Notes |
| --- | --- | --- |
| In words, what does $Var(X)$ measure? | **How spread out X is: the average squared distance from its mean.** | p.3; definition |
| Write the definition of $Var(X)$ in symbols. | $Var(X) = E[(X - E[X])^2]$. *Read aloud: "the expected squared distance of X from its mean."* | p.3; formula |
| Why is $Var(X)$, three letters and an X, legal notation? | **Var is a function whose input is a whole random variable**, not a number. *Side note, not tested: It returns one number.* | p.3; notation |
| $E[X^2]$ vs $(E[X])^2$: what is the difference? | **$E[X^2]$: square each value, then average. $(E[X])^2$: average first, then square.** | p.3; discrimination |
| Why use the shortcut $E[X^2] - (E[X])^2$ instead of the definition? | **No need to subtract the mean from every value first**; you need only two averages. | p.3; motivation |
| Why are the distances squared in the variance? | **So negative and positive distances do not cancel**; squares are never negative. | p.3; motivation |
| X is 0 or 2, each with chance 1/2. What is $Var(X)$? | $E[X] = 1$, $E[X^2] = 2$, so $Var(X) = 2 - 1^2 = 1$. | p.3; worked example |

## Standard Deviation
| Front | Back | Notes |
| --- | --- | --- |
| How is the standard deviation related to the variance? | $SD = \sqrt{Var(X)}$. | extra (not in lecture text); formula |
| Why take the square root of the variance? | **It puts spread back into X's own units** (minutes, not minutes squared). | extra; motivation |
| What does "deviation" mean in standard deviation? | **The distance of a value from the mean.** | extra; definition |
| What does "standard" mean in standard deviation? | **A typical, representative size** *Side note, not tested: of those deviations.* *Side note, not tested: Karl Pearson coined the term in the 1890s.* | extra; definition |
| Where else do the words "standard" and "deviation" show up in this course? | **z-scores (deviations counted in SDs), the standard normal, and the standard error.** | extra; recognition |

## Expectation and Variance
| Front | Back | Notes |
| --- | --- | --- |
| What is $E[X]$ for a discrete random variable? %%dk:t:hekq6u%% | $E[X] = \sum_x x\, \mathbb{P}(X=x)$. *Read aloud: "the sum over every value x of x times the probability X equals x."* | p.3; formula |
| What is $E[X]$ for a continuous random variable? %%dk:t:d971fk%% | $E[X] = \int_{-\infty}^{\infty} x f(x)\,dx$. | p.3; formula |
| What is the shortcut formula for $Var(X)$? %%dk:t:s44wup%% | $Var(X) = E[X^2] - (E[X])^2$. | p.3; formula |

## Common Distributions
| Front | Back | Notes |
| --- | --- | --- |
| Binomial$(n,p)$: what is the mean? %%dk:t:b0dq73%% | $np$ | p.3; formula |
| Binomial$(n,p)$: what is the variance? | $np(1-p)$ | p.3; formula |
| Poisson$(\lambda)$: what is the mean? %%dk:t:h4e18q%% | $\lambda$ | p.3; formula |
| Poisson$(\lambda)$: what is the variance? | $\lambda$ (the same as the mean) | p.3; formula |
| Exponential$(\lambda)$: what is the mean? %%dk:t:2n0n0m%% | $\frac{1}{\lambda}$ | p.3; formula |
| Exponential$(\lambda)$: what is the variance? | $\frac{1}{\lambda^2}$ | p.3; formula |
| Uniform$(a,b)$: what is the mean? %%dk:t:54i9q7%% | $\frac{a+b}{2}$ | p.3; formula |
| Uniform$(a,b)$: what is the variance? | $\frac{(b-a)^2}{12}$ | p.3; formula |

## Gamma and Beta Functions
| Front | Back | Notes |
| --- | --- | --- |
| How is the Gamma function $\Gamma(x)$ defined as an integral? %%dk:t:l9pa7d%% | $\Gamma(x) = \int_0^\infty t^{x-1} e^{-t}\,dt$, for $x>0$. | p.3; formula |
| How does $\Gamma(n)$ relate to the factorial for a positive integer $n$? %%dk:t:tw4jmx%% | $\Gamma(n) = (n-1)!$. | p.4; formula |
| How is the Beta function $B(x,y)$ expressed in terms of Gamma functions? %%dk:t:v00qe8%% | $B(x,y) = \dfrac{\Gamma(x)\Gamma(y)}{\Gamma(x+y)}$. | p.4; formula |

## Law of Large Numbers
| Front | Back | Notes |
| --- | --- | --- |
| Law of Large Numbers: as $n$ grows, $\bar X$ gets close to what? %%dk:t:qls0ff%% | **$E[X]$, the true mean.** | p.4; theorem |
| Give a coin example of the Law of Large Numbers. | Keep flipping a fair coin and the share of heads settles at 0.5. | p.4; theorem |
| In the Law of Large Numbers, what has to happen for $\bar X$ to approach $E[X]$? | **The sample size n grows toward infinity.** *Side note, not tested: the law says "if n grows, then $\bar X \to E[X]$"; it is not a two-way rule.* | p.4; recognition |
| State the Law of Large Numbers in full. | **As $n \to \infty$, the sample mean $\bar X$ converges to $E[X]$.** *Read aloud: "as n goes to infinity, X bar converges to E of X."* | p.4; assembly |

## Central Limit Theorem
| Front | Back | Notes |
| --- | --- | --- |
| CLT: for large $n$, what shape does the distribution of $\bar X$ have? %%dk:t:cw3qoy%% | **Approximately normal.** | p.4; theorem |
| CLT: which distributions of $X$ does it work for? | **Any distribution** (skewed, discrete, anything) with a finite variance. | p.4; theorem |
| LLN vs CLT: does each describe a single value or a distribution's shape? %%dk:t:3ui3pf%% | LLN describes convergence of $\bar X$ to a single value, $E[X]$. CLT describes the shape of $\bar X$'s distribution, which becomes approximately normal. | p.4; discrimination |
| State the Central Limit Theorem in full. | **For large n, the distribution of $\bar X$ is approximately normal, whatever the distribution of X** (as long as X has a finite variance). | p.4; assembly |

## What Is Statistical Inference
| Front | Back | Notes |
| --- | --- | --- |
| Statistical inference in one line: from what, to what? %%dk:t:bfk47t%% | **From a sample (data) to conclusions about the population.** | p.4; definition |
| Give an example of statistical inference. | Survey 1,000 Californians to estimate the share of all Californians with a degree. | p.4; definition |
| What stops probability theory alone from answering real-world questions? %%dk:t:n9bnex%% | **It needs the parameters to be known, but the real world only hands you data.** | p.4; definition |
| What is statistics? | **The science of collecting, summarizing and drawing conclusions from data.** | p.4; definition; if stuck: Lecture_01 Prep deck |
| What is an inference? | **A conclusion reached from evidence and reasoning**, about something you did not observe directly. | p.4; definition |
| What gap does statistical inference bridge? | **Between probability theory** (known parameters, computed chances) **and real-world observations** (data, unknown parameters). | p.4; motivation |
| For statistical inference, the sample must be drawn from what? | **The population you want conclusions about.** *Side note, not tested: draw from a different group and your conclusions only apply to that group.* | p.4; definition; if stuck: Lecture_01 Prep deck |

## Probability vs Inference
| Front | Back | Notes |
| --- | --- | --- |
| Probability theory: what do you start with? %%dk:t:fokfq7%% | **Known parameters** (e.g. $p = 0.5$). | p.4; discrimination |
| Probability theory: what do you compute? | **The probability of data** (e.g. P(6 heads in 10)). | p.4; discrimination |
| Inferential statistics: what do you start with? %%dk:t:bz2tn2%% | **Observed data** (e.g. 8 heads in 10). | p.4; discrimination |
| Inferential statistics: what are you after? | **The unknown parameters** (e.g. what is $p$?). | p.4; discrimination |
| What do you need before you can compute the probability of an event? | **A distribution with known parameters** (the model) and the event written as a set of outcomes. | p.4; definition |
| Observed event vs possible event: which one counts as data? | **The observed one:** an outcome that actually happened and was recorded. *Side note, not tested: A possible event only lives in the sample space.* | p.4; discrimination |
| When is a parameter known rather than unknown? | **When the problem or theory fixes its value**, e.g. a fair coin has $p = 0.5$. | p.4; discrimination; if stuck: Lecture_01 Prep deck |
| What gives a population its distribution? | **How the values are spread across all its members** (what share has each value). | p.4; definition |

## Coin Tossing, Probability vs Inference
| Front | Back | Notes |
| --- | --- | --- |
| Coin example, inference problem: after seeing 8 heads in 10 tosses, what is still unknown? %%dk:t:nhqjg8%% | **The chance of heads, p.** | p.4-5; key move |
| Coin example, probability problem: for a fair coin, what is $\mathbb{P}(6 \text{ heads in } 10)$? | $\binom{10}{6}(0.5)^{10} = \dfrac{210}{1024} \approx 0.205$. | p.4; worked example |
| Coin example, inference problem: 8 heads in 10 tosses. What is a natural guess for $p$? | **8/10 = 0.8**, the sample proportion of heads. *Side note, not tested: this is also the MLE.* | p.5; worked example |

## Parametric vs Nonparametric
| Front | Back | Notes |
| --- | --- | --- |
| Parametric inference: what do you assume about the data's distribution? %%dk:t:uvxfxz%% | **It comes from a known family with a few unknown numbers.** *Side note, not tested: Ex: heights are Normal; only $\mu$ and $\sigma^2$ are unknown.* | p.5; definition |
| Non-parametric inference: what do you assume about the data's distribution? %%dk:t:yc0e15%% | **Almost nothing about its shape.** *Side note, not tested: Ex: estimate the median without assuming it's Normal.* | p.5; definition |
| Estimating a median without assuming any distribution family: parametric or non-parametric? %%dk:t:fvaliq%% | **Non-parametric.** | p.5; discrimination |
| What does "minimal assumptions" mean in non-parametric inference? | **You do not assume a family** (Normal, Poisson, ...). You may still assume basics like independence. | p.5; definition |
| Why would you make minimal assumptions about a distribution? | **Assume the wrong family and your conclusions can be badly wrong.** *Side note, not tested: Fewer assumptions are safer.* | p.5; motivation |
| When is parametric inference the better choice? | **When you have good reason (theory or past data) to trust the family.** It then gets more out of less data. | p.5; discrimination |
| When is non-parametric inference the better choice? | **When the family is unknown or doubtful** (odd or skewed shapes) and you have enough data. | p.5; discrimination |
| Besides the distribution's family, what other assumptions can an inference make about the data? | **Independence, one shared parameter for every observation (identically distributed), and random sampling.** | p.5; definition; dep: [[Bayes Update Algorithm]] |

## Population parameter
| Front | Back | Notes |
| --- | --- | --- |
| What is a parameter? %%dk:t:e9wd1j%% | **A number that picks out one distribution from a family.** | p.5; definition |
| Name the parameters of $N(\mu,\sigma^2)$. | $\mu$ and $\sigma^2$ | p.5; definition |
| What is the parameter space? %%dk:t:px4duh%% | **Every value the parameter is allowed to take.** | p.5; definition |
| Parameter space of $p$ in Binomial$(n,p)$? | $[0, 1]$ | p.5; definition |
| What is the parameter space for $N(\mu,\sigma^2)$? %%dk:t:jisgmm%% | $\mu \in \mathbb{R}$, $\sigma^2 > 0$. | p.5; procedure |
| Which letter is the usual placeholder for a generic parameter? | **$\theta$ (theta).** | p.5; notation; if stuck: Lecture_01 Prep deck |
| Where does the word "parameter" come from? | **Greek para (beside) + metron (measure):** a measuring quantity that sits beside the variable and sets the model. | p.5; motivation |

## Parameter Space
| Front | Back | Notes |
| --- | --- | --- |
| What is the parameter space of a Poisson rate $\lambda$? | **All numbers above 0**: $(0, \infty)$. | p.5; worked example |
| Why does knowing the parameter space matter? | **It rules out impossible answers and tells you which prior curve fits** (0 to 1 gives Beta; above 0 gives Gamma). | p.5; motivation; dep: [[Bayes Update Algorithm]] |
| A coin's estimated chance of heads comes out as 1.2. What does the parameter space tell you? | **It is impossible: p must lie in [0, 1]**, so the calculation went wrong. | p.5; worked example |
| What makes a set a "space" in mathematics? | **A set plus structure**, such as distance or order. *Side note, not tested: here it just means the set of allowed values.* | p.5; definition; if stuck: Lecture_01 Prep deck |

## Statistic (inference)
| Front | Back | Notes |
| --- | --- | --- |
| What is the rule for something to count as a statistic? %%dk:t:9p82ko%% | **You can compute it from the data alone, with no unknown parameters.** | p.5; definition |
| Which of $\bar X$, $S^2$, $\bar X - \mu$, $\max X_i$ is not a statistic? | $\bar X - \mu$: it contains the unknown $\mu$. | p.5; definition |
| Why can't a statistic contain an unknown parameter? %%dk:t:9sx3uw%% | **Because you have to be able to calculate it.** *Side note, not tested: If it contains the unknown $\mu$, you can't get a number out of your data.* | p.5; definition |
| When may a statistic contain a parameter? | **Only when that parameter's value is known**, a fixed number like $\mu_0 = 100$ in a test. *Side note, not tested: Unknown parameters are never allowed.* | p.5; discrimination |
| In $T = t(X_1, \dots, X_n)$, what is the difference between t and T? | **t is the rule (the function). T is its output**, a random quantity until the data are seen. | p.5; notation |

## Sample Mean and Sample Variance
| Front | Back | Notes |
| --- | --- | --- |
| What is the formula for the sample mean $\bar X$? %%dk:t:jnld0g%% | $\bar X = \dfrac{1}{n}\sum_{i=1}^n X_i$. | p.6; formula |
| What is the formula for the sample variance $S^2$? %%dk:t:ytw0xs%% | $S^2 = \dfrac{1}{n-1}\sum_{i=1}^n (X_i - \bar X)^2$. | p.6; formula |
| $\bar X$ vs $\mu$: which one changes from sample to sample? %%dk:t:v74ev3%% | **$\bar X$**, because it is computed from the data. *Side note, not tested: $\mu$ is a fixed feature of the population.* | p.6; discrimination |
| Why is the sample mean a sensible estimate of $\mu$? | **It is the average of what you saw, and by the Law of Large Numbers it closes in on $\mu$ as n grows.** | p.6; motivation |
| Sample variance $S^2$ vs $Var(X)$: which is which? | **$Var(X)$ is the population's spread (a parameter); $S^2$ is computed from the sample to estimate it.** | p.6; discrimination |
| Why does $S^2$ divide by $n - 1$ instead of n? | **Using $\bar X$ in place of $\mu$ makes the squared distances a bit too small; dividing by $n - 1$ fixes that on average** (unbiased). | p.6; motivation |

## Estimation and Prediction
| Front | Back | Notes |
| --- | --- | --- |
| Estimation targets what? %%dk:t:y2knpt%% | **A parameter** (e.g. $\mu$). | p.6; definition |
| Prediction targets what? | **A future observation**, e.g. next year's STAT 132 enrollment. | p.6; definition |

## Point Estimate vs Interval Estimate
| Front | Back | Notes |
| --- | --- | --- |
| What does a point estimate give you? %%dk:t:lsebx8%% | **One best guess**, e.g. $\bar X = 52$. | p.6; discrimination |
| What does an interval estimate give you? | **A range with a confidence level**, e.g. 48 to 56 at 95%. | p.6; discrimination |
| How do you judge whether a point estimator is good? | **By its errors over many samples: small bias and small spread.** *Side note, not tested: later this becomes mean squared error and loss functions (DeGroot 7.4).* | p.6; definition |
| Name three common methods of point estimation. | **Maximum likelihood (MLE), Bayes estimators (e.g. the posterior mean), and the method of moments.** | p.6; recognition |
| In the Bayes update algorithm, where does a point estimate come from? | **After step 6: summarize the posterior with one number**, e.g. its mean (help desk: $20/6 \approx 3.33$). | p.6; assembly; dep: [[Bayes Update Algorithm]] |
| In the Bayes update algorithm, where does an interval estimate come from? | **After step 6: take a range holding most of the posterior**, e.g. its middle 95%. | p.6; assembly; dep: [[Bayes Update Algorithm]] |

## Hypothesis Testing
| Front | Back | Notes |
| --- | --- | --- |
| Hypothesis testing: what do you decide? %%dk:t:gjjgu1%% | **Whether a claim about a parameter holds up**, using sample data. *Side note, not tested: Ex: is the mean fruit weight 100 g?* | p.6; definition |
| Hypothesis testing is a type of what? | **Decision theory:** choosing an action (reject or keep a claim) under uncertainty. | p.6; definition; if stuck: Lecture_01 Prep deck |
| What is a claim, in statistics? | **A statement about a parameter's value**, e.g. $\mu = 100$. | p.6; definition |
| Which parameters can a hypothesis be about? | **Any parameter**: $\mu$, $p$, $\lambda$, $\sigma^2$, and so on. | p.6; definition |

## Null and Alternative Hypotheses
| Front | Back | Notes |
| --- | --- | --- |
| What does $H_0$ stand for? %%dk:t:g9gyzv%% | **The null hypothesis: the default claim, kept unless the data argue against it.** | p.6; definition |
| What does $H_1$ stand for? | **The alternative hypothesis**: what you conclude if the data argue against $H_0$. | p.6; definition |
| Which hypothesis usually contains the "=" sign? | $H_0$, e.g. $\mu = 100$ (against $H_1$: $\mu \ne 100$). | p.6; definition |
| Read $H_0: \mu = 100$ aloud and say what it means. | **The null hypothesis: the mean is 100.** *Read aloud: "H naught: mu equals 100."* | p.6; notation |
| What other symbols are used for $H_1$? | **$H_A$ or $H_a$** (the alternative). | p.6; notation |
| Which signs can the alternative hypothesis $H_1$ use? | **$\ne$ (two-sided), or $<$ or $>$ (one-sided).** | p.6; definition |

## Testing a Mean, Fruit Weight
| Front | Back | Notes |
| --- | --- | --- |
| For testing whether a fruit's average weight equals 100 grams, what are $H_0$ and $H_1$? %%dk:t:qzm0xt%% | $H_0: \mu = 100$; $H_1: \mu \neq 100$. | p.6; key move |

## Defective Items, Two Machines
| Front | Back | Notes |
| --- | --- | --- |
| Factory: machine A makes 60% of items (5% defective), machine B makes 40% (2% defective). What is $\mathbb{P}(\text{defective})$? | $0.05(0.6) + 0.02(0.4) = 0.038$. *Side note, not tested: law of total probability, splitting on which machine made it.* | problem; worked example |
| Same factory: an item is defective. What is $\mathbb{P}(\text{machine A} \mid \text{defective})$? | $\dfrac{0.03}{0.038} = \dfrac{15}{19} \approx 0.789$, by Bayes' rule. | problem; worked example |
| Same factory: X = defective items in an independent sample of 10. Which distribution does X follow? | **Binomial(10, 0.038).** | problem; recognition |
| X is Binomial(10, 0.038). What is $E[X]$? | $10(0.038) = 0.38$. | problem; worked example |
| X is Binomial(10, 0.038). What is $Var(X)$? | $10(0.038)(0.962) \approx 0.366$. | problem; worked example |

## Exam Scores CLT Test
| Front | Back | Notes |
| --- | --- | --- |
| 25 exam scores, $\bar x = 78$, $s^2 = 25$, testing whether the true mean is 80. Why does $\bar x$ count as a statistic? | **It is computed from the data alone, with no unknown parameters.** | problem; definition |
| 25 exam scores, $\bar x = 78$, $s^2 = 25$, testing whether the true mean is 80. Write $H_0$ and $H_1$. | $H_0: \mu = 80$; $H_1: \mu \ne 80$. | problem; worked example |
| 25 exam scores, $\bar x = 78$, $s^2 = 25$, testing whether the true mean is 80. By the CLT, what is the approximate distribution of $\bar X$ under $H_0$? | $N(80, 25/25) = N(80, 1)$. | problem; worked example |
| 25 exam scores, $\bar x = 78$, $s^2 = 25$, testing whether the true mean is 80. Compute $z = \dfrac{\bar x - \mu_0}{s/\sqrt n}$. | $\dfrac{78 - 80}{5/5} = -2$. | problem; worked example |

# Node map
```json
[
 {
  "name": "Sample Space and Events",
  "type": "concept",
  "existing": false,
  "parent": "Probability theory",
  "prereqs": [],
  "uses": [],
  "page": 2,
  "summary": "A random experiment produces one of several outcomes; the sample space $\\Omega$ is the set of all outcomes, and an event is any subset of $\\Omega$."
 },
 {
  "name": "Axioms of Probability",
  "type": "concept",
  "existing": false,
  "parent": "Probability theory",
  "prereqs": [
   "Sample Space and Events"
  ],
  "uses": [],
  "page": 2,
  "summary": "A probability measure $\\mathbb{P}$ satisfies $0 \\le \\mathbb{P}(A) \\le 1$, $\\mathbb{P}(\\Omega)=1$, and additivity over disjoint events."
 },
 {
  "name": "Conditional Probability",
  "type": "concept",
  "existing": true,
  "parent": "Probability theory",
  "prereqs": [
   "Axioms of Probability"
  ],
  "uses": [],
  "page": 2,
  "summary": "$\\mathbb{P}(A \\mid B) = \\mathbb{P}(A \\cap B)/\\mathbb{P}(B)$ when $\\mathbb{P}(B)>0$: the probability of $A$ given that $B$ occurred."
 },
 {
  "name": "Bayes' Rule",
  "type": "concept",
  "existing": true,
  "parent": "Probability theory",
  "prereqs": [
   "Conditional Probability"
  ],
  "uses": [],
  "page": 2,
  "summary": "$\\mathbb{P}(A \\mid B) = \\mathbb{P}(B \\mid A)\\mathbb{P}(A)/\\mathbb{P}(B)$, reversing the direction of conditioning, with $\\mathbb{P}(B)$ expanded via $A$ and $A^c$."
 },
 {
  "name": "Random variable",
  "type": "concept",
  "existing": false,
  "parent": "Probability theory",
  "prereqs": [
   "Sample Space and Events"
  ],
  "uses": [],
  "page": 2,
  "summary": "A random variable is a function $X:\\Omega \\to \\mathbb{R}$; it is discrete if it takes countable values, continuous if it takes values in an interval of $\\mathbb{R}$."
 },
 {
  "name": "PMF, PDF and CDF",
  "type": "concept",
  "existing": true,
  "parent": "Probability theory",
  "prereqs": [
   "Random variable"
  ],
  "uses": [],
  "page": 2,
  "summary": "The PMF gives $\\mathbb{P}(X=x)$ for discrete variables, the PDF integrates to give interval probabilities for continuous variables, and the CDF gives $\\mathbb{P}(X \\le x)$."
 },
 {
  "name": "Expectation and Variance",
  "type": "concept",
  "existing": true,
  "parent": "Probability theory",
  "prereqs": [
   "PMF, PDF and CDF"
  ],
  "uses": [],
  "page": 3,
  "summary": "$E[X]$ is the probability-weighted average of $X$ (sum or integral); $Var(X)=E[X^2]-(E[X])^2$ measures spread."
 },
 {
  "name": "Common Distributions",
  "type": "concept",
  "existing": true,
  "parent": "Probability theory",
  "prereqs": [
   "PMF, PDF and CDF",
   "Expectation and Variance"
  ],
  "uses": [],
  "page": 3,
  "summary": "A table of standard distributions (Binomial, Poisson, Normal, Gamma, Beta, Exponential, Uniform) with their density/mass functions, means, and variances."
 },
 {
  "name": "Gamma and Beta Functions",
  "type": "concept",
  "existing": true,
  "parent": "Probability theory",
  "prereqs": [
   "Common Distributions"
  ],
  "uses": [],
  "page": 3,
  "summary": "$\\Gamma(x)=\\int_0^\\infty t^{x-1}e^{-t}dt$ extends the factorial ($\\Gamma(n)=(n-1)!$); the Beta function $B(x,y)=\\Gamma(x)\\Gamma(y)/\\Gamma(x+y)$ appears in the Beta distribution's PDF."
 },
 {
  "name": "Law of Large Numbers",
  "type": "concept",
  "existing": true,
  "parent": "Probability theory",
  "prereqs": [
   "Expectation and Variance",
   "Sample Mean and Sample Variance"
  ],
  "uses": [],
  "page": 4,
  "summary": "As $n \\to \\infty$, the sample mean $\\bar X$ converges to $E[X]$."
 },
 {
  "name": "Central Limit Theorem",
  "type": "concept",
  "existing": true,
  "parent": "Probability theory",
  "prereqs": [
   "Law of Large Numbers",
   "Common Distributions"
  ],
  "uses": [],
  "page": 4,
  "summary": "For large $n$, the distribution of $\\bar X$ approaches a normal distribution regardless of the distribution of $X$."
 },
 {
  "name": "What Is Statistical Inference",
  "type": "concept",
  "existing": false,
  "parent": "Statistical Inference",
  "prereqs": [],
  "uses": [],
  "page": 4,
  "summary": "Statistical inference makes conclusions about a population from sample data, bridging probability theory and real-world observations."
 },
 {
  "name": "Probability vs Inference",
  "type": "concept",
  "existing": true,
  "parent": "Statistical Inference",
  "prereqs": [
   "What Is Statistical Inference"
  ],
  "uses": [],
  "page": 4,
  "summary": "Probability theory starts with known parameters and computes probabilities of data; inferential statistics starts with observed data and infers unknown parameters."
 },
 {
  "name": "Coin Tossing, Probability vs Inference",
  "type": "problem",
  "existing": false,
  "parent": "Statistical Inference",
  "prereqs": [],
  "uses": [
   "Probability vs Inference",
   "Common Distributions"
  ],
  "page": 4,
  "summary": "Contrasts computing $\\mathbb{P}(X=6)$ for a known fair coin (probability) with estimating $p$ from 8 heads in 10 tosses (inference)."
 },
 {
  "name": "Parametric vs Nonparametric",
  "type": "concept",
  "existing": true,
  "parent": "Parametric vs Non-Parametric Inference",
  "prereqs": [
   "Population parameter"
  ],
  "uses": [],
  "page": 5,
  "summary": "Parametric inference assumes a distribution indexed by finitely many parameters (e.g. $N(\\mu,\\sigma^2)$); non-parametric inference assumes minimal distributional form (e.g. estimating a median)."
 },
 {
  "name": "Population parameter",
  "type": "concept",
  "existing": true,
  "parent": "Parameters and Parameter Space",
  "prereqs": [],
  "uses": [],
  "page": 5,
  "summary": "A parameter indexes a family of distributions (e.g. $\\mu,\\sigma^2$ for $N(\\mu,\\sigma^2)$); the parameter space is the set of all values it can take (e.g. $\\mu\\in\\mathbb{R}, \\sigma^2>0$)."
 },
 {
  "name": "Statistic (inference)",
  "type": "concept",
  "existing": true,
  "parent": "Statistics",
  "prereqs": [
   "Random variable"
  ],
  "uses": [],
  "page": 5,
  "summary": "A statistic $T=t(X_1,\\ldots,X_n)$ is a function of the data alone, containing no unknown parameters."
 },
 {
  "name": "Sample Mean and Sample Variance",
  "type": "concept",
  "existing": false,
  "parent": "Statistics",
  "prereqs": [
   "Statistic (inference)",
   "Expectation and Variance"
  ],
  "uses": [],
  "page": 6,
  "summary": "$\\bar X = \\frac{1}{n}\\sum X_i$ and $S^2=\\frac{1}{n-1}\\sum(X_i-\\bar X)^2$ are the standard statistics estimating a population's mean and variance."
 },
 {
  "name": "Estimation and Prediction",
  "type": "concept",
  "existing": false,
  "parent": "Estimation and Prediction",
  "prereqs": [
   "Population parameter",
   "Sample Mean and Sample Variance"
  ],
  "uses": [],
  "page": 6,
  "summary": "Point estimation gives a single best guess of a parameter; interval estimation gives a range at a confidence level; prediction instead forecasts future observations."
 },
 {
  "name": "Hypothesis Testing",
  "type": "concept",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [
   "Population parameter",
   "Estimation and Prediction"
  ],
  "uses": [],
  "page": 6,
  "summary": "A decision-theory procedure for testing a claim about a parameter using sample data, framed as a null hypothesis $H_0$ versus alternative $H_1$."
 },
 {
  "name": "Testing a Mean, Fruit Weight",
  "type": "problem",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [],
  "uses": [
   "Hypothesis Testing"
  ],
  "page": 6,
  "summary": "Sets up $H_0: \\mu=100$ vs $H_1: \\mu \\neq 100$ to test whether a fruit's average weight is 100 grams."
 },
 {
  "name": "Discrete vs Continuous Random Variable",
  "type": "concept",
  "existing": true,
  "parent": "",
  "prereqs": [],
  "summary": ""
 },
 {
  "name": "Point Estimate vs Interval Estimate",
  "type": "concept",
  "existing": true,
  "parent": "",
  "prereqs": [],
  "summary": ""
 },
 {
  "name": "Null and Alternative Hypotheses",
  "type": "concept",
  "existing": true,
  "parent": "",
  "prereqs": [],
  "summary": ""
 },
 {
  "name": "Random Experiment",
  "uses": [],
  "type": "concept",
  "existing": false,
  "parent": "Probability theory",
  "prereqs": [],
  "page": 2,
  "summary": "An action or process that leads to one of several possible outcomes; you know the possible outcomes but not which one will happen."
 },
 {
  "name": "Probability Measure",
  "uses": [],
  "type": "concept",
  "existing": false,
  "parent": "Probability theory",
  "prereqs": [
   "Sample Space and Events"
  ],
  "page": 2,
  "summary": "A function $\\mathbb{P}$ assigning a probability to each event, with $0 \\le \\mathbb{P}(A) \\le 1$, $\\mathbb{P}(\\Omega)=1$, and additivity over disjoint events."
 },
 {
  "name": "Discrete Random Variable",
  "uses": [],
  "type": "concept",
  "existing": false,
  "parent": "Random variable",
  "prereqs": [
   "Random variable"
  ],
  "page": 2,
  "summary": "A random variable that takes countable values (values you can list, like 0, 1, 2, ...)."
 },
 {
  "name": "Continuous Random Variable",
  "uses": [],
  "type": "concept",
  "existing": false,
  "parent": "Random variable",
  "prereqs": [
   "Random variable"
  ],
  "page": 2,
  "summary": "A random variable that takes any value in an interval of the real numbers."
 },
 {
  "name": "Probability Mass Function",
  "uses": [],
  "type": "concept",
  "existing": false,
  "parent": "Random variable",
  "prereqs": [
   "Discrete Random Variable"
  ],
  "page": 2,
  "summary": "For a discrete random variable, $f(x) = \\mathbb{P}(X = x)$: the chance X lands exactly on x."
 },
 {
  "name": "Probability density function",
  "uses": [],
  "type": "concept",
  "existing": true,
  "parent": "Random variable",
  "prereqs": [
   "Continuous Random Variable"
  ],
  "page": 2,
  "summary": "For a continuous random variable, $\\mathbb{P}(a \\le X \\le b) = \\int_a^b f(x)\\,dx$."
 },
 {
  "name": "Cumulative Distribution Function",
  "uses": [],
  "type": "concept",
  "existing": false,
  "parent": "Random variable",
  "prereqs": [
   "Probability Mass Function",
   "Probability density function"
  ],
  "page": 2,
  "summary": "$F(x) = \\mathbb{P}(X \\le x)$: the running total of probability up to x, for discrete and continuous variables."
 },
 {
  "name": "Expectation",
  "uses": [],
  "type": "concept",
  "existing": true,
  "parent": "Expectation and Variance",
  "prereqs": [
   "Probability Mass Function",
   "Probability density function"
  ],
  "page": 3,
  "summary": "The long-run average of X: each value weighted by its chance; $\\sum_x x\\,\\mathbb{P}(X=x)$ or $\\int x f(x)\\,dx$."
 },
 {
  "name": "Variance (Math)",
  "uses": [],
  "type": "concept",
  "existing": true,
  "parent": "Expectation and Variance",
  "prereqs": [
   "Expectation"
  ],
  "page": 3,
  "summary": "$Var(X) = E[(X - E[X])^2] = E[X^2] - (E[X])^2$: the average squared distance of X from its mean."
 },
 {
  "name": "Standard Deviation",
  "uses": [],
  "type": "concept",
  "existing": true,
  "parent": "Expectation and Variance",
  "prereqs": [
   "Variance (Math)"
  ],
  "page": 3,
  "summary": "$SD = \\sqrt{Var(X)}$: the typical size of a deviation from the mean, in X's own units."
 },
 {
  "name": "Parameter Space",
  "uses": [],
  "type": "concept",
  "existing": true,
  "parent": "Statistical Model",
  "prereqs": [
   "Parameters"
  ],
  "page": 5,
  "summary": "The set of all values the parameter can take."
 },
 {
  "name": "Defective Items, Two Machines",
  "type": "problem",
  "existing": false,
  "parent": "Conditional Probability",
  "prereqs": [],
  "uses": [
   "Law of Total Probability",
   "Bayes' Rule",
   "Binomial Distribution"
  ],
  "page": "",
  "summary": "Two machines with different defect rates: total probability, Bayes' rule, then a Binomial count."
 },
 {
  "name": "Exam Scores CLT Test",
  "type": "problem",
  "existing": false,
  "parent": "Hypothesis Testing",
  "prereqs": [],
  "uses": [
   "Statistic (inference)",
   "Central Limit Theorem",
   "Null and Alternative Hypotheses"
  ],
  "page": "",
  "summary": "Sample of 25 scores, mean 78, variance 25: statistic, hypotheses, CLT distribution, z = -2."
 }
]
```

# Frankenstein problems

**Problem 1: Defective Items and a Random Sample**
A factory has two machines. Machine A produces 60% of items, and 5% of Machine A's items are defective. Machine B produces 40% of items, and 2% of Machine B's items are defective. An item is picked at random.

**(a)** What is $\mathbb{P}(\text{defective})$?
**(b)** Given the item is defective, what is $\mathbb{P}(\text{Machine A} \mid \text{defective})$?
**(c)** Let $X$ be the number of defective items in an independent sample of 10 items from the overall output. Find $E[X]$ and $Var(X)$.

**Solution:**

(a) By the law of total probability (from the axioms of probability, splitting on disjoint events A, A^c):
$$\mathbb{P}(\text{defective}) = \mathbb{P}(\text{def} \mid A)\mathbb{P}(A) + \mathbb{P}(\text{def} \mid B)\mathbb{P}(B) = (0.05)(0.6) + (0.02)(0.4) = 0.03 + 0.008 = 0.038.$$

(b) By Bayes' rule:
$$\mathbb{P}(A \mid \text{def}) = \frac{\mathbb{P}(\text{def} \mid A)\mathbb{P}(A)}{\mathbb{P}(\text{def})} = \frac{0.03}{0.038} = \frac{15}{19} \approx 0.789.$$

(c) $X \sim \text{Binomial}(n=10, p=0.038)$, using the Binomial mean/variance from Common Distributions:
$$E[X] = np = 10(0.038) = 0.38, \qquad Var(X) = np(1-p) = 10(0.038)(0.962) = 0.36556.$$

Concepts tested: Axioms of Probability, Conditional Probability, Bayes' Rule, Common Distributions, Expectation and Variance.

**Problem 2: Testing a Sample Mean with the CLT**
A sample of $n=25$ exam scores has sample mean $\bar x = 78$ and sample variance $s^2 = 25$. A researcher wants to test whether the true population mean $\mu$ equals 80.

**(a)** Is $\bar x$ a statistic? Why?
**(b)** State $H_0$ and $H_1$.
**(c)** Using the CLT, what is the approximate sampling distribution of $\bar X$ under $H_0$ (using $s^2$ in place of $\sigma^2$)?
**(d)** Compute the standardized test statistic $z = \dfrac{\bar x - \mu_0}{s/\sqrt{n}}$.

**Solution:**

(a) Yes: $\bar X = \frac{1}{n}\sum X_i$ is a function of the data only, with no unknown parameters, so it is a statistic (and it is the sample mean).

(b) $H_0: \mu = 80$, $H_1: \mu \neq 80$.

(c) By the Central Limit Theorem, for large $n$, $\bar X$ is approximately normal with mean $\mu$ and variance $\sigma^2/n$; substituting $\mu_0=80$ and $s^2=25$ under $H_0$:
$$\bar X \approx N\left(80, \frac{25}{25}\right) = N(80, 1).$$

(d) Standard error $= \sqrt{s^2/n} = \sqrt{25/25} = \sqrt{1} = 1$.
$$z = \frac{78 - 80}{1} = -2.$$

Concepts tested: Statistic (inference), Sample Mean and Sample Variance, Population parameter, Central Limit Theorem, Hypothesis Testing.
