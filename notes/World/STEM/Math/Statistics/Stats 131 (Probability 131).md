---
parent: "[[STATS 131]]"
type: concept
domain: stats
status: draft
---
Experiment
- A process whose outcome is known/is uncertain

| Symbol | LaTeX                        | Meaning                | Example           |
| ------ | ---------------------------- | ---------------------- | ----------------- |
| ∅      | `\varnothing` or `\emptyset` | empty set              | $$A=\varnothing$$ |
| { }    | `\{\,\}`                     | set builder braces     | $$\{1,2,3\}$$     |
| ∈      | `\in`                        | is an element of       | $$x\in A$$        |
| ∉      | `\notin`                     | is not an element of   | $$x\notin A$$     |
| ⊆      | `\subseteq`                  | subset (allow equal)   | $$A\subseteq B$$  |
| ⊂      | `\subset`                    | proper subset (strict) | $$A\subset B$$    |
| ⊇      | `\supseteq`                  | superset (allow equal) | $$B\supseteq A$$  |
| ⊃      | `\supset`                    | proper superset        | $$B\supset A$$    |
# 1.1
There is uncertainty. In uncertainty, experiments are any process performed with uncertainty. [[Sets]] are containers with items. Some sets have rules built into them making them spaces. A sample [[Space (mathematics)|space]] is the set of the sample in the *experiment* consisting of everything that could happen. Each entry is an event. Events, as entries, are not like integers, but instead have interesting new possibilities and some of the classic ones we know and love from the reals. The ones that deserves the most focus are also inherent to set theory - unions, intersections, complements, inclusivity, and exclusivity. 

We begin with a finite probability space $(\mathcal{S},\Pr)$ where $\mathcal{S}$ is a finite set and events are subsets $A \subseteq \mathcal{S}$. In a simple (uniform) space, probability is [[normalization]] [[cardinality]],

$$
\Pr(A)=\frac{|A|}{|\mathcal{S}|}.
$$

==Thus every probability problem reduces to computing the size of sets.== The first quarter is dedicated to finite sets and the second half is to continuous ones. Put differently, the first half is set logic and the second is integrating curves; the last section unifies these together. 

All probability questions reduce to:

$$P(E) = \frac{|\{\omega \in \mathcal S : \text{condition holds}\}|}{|\mathcal S|}$$

Functions exist only to define the condition cleanly.
Our process is not to fill out a function but do math which queries this data on it's probability. 

Theory
	Interpretations of Probability
		Classical
			All is equally likely
		Subjective
			Based off of interpreting the unknowable like human behavior
				See voting
		Frequency
			Bayesian Inference (If I can obsv. I can prove it.)
	Experiment
		is a process whose outcome is not known in advanced (uncertainty
	Events
		Set of outcomes; each outcome is $s$
	Sample space
		Collection of all possible outcomes; denoted as $𝒮$ ($S$)or $\Omega$, then $s ∈ 𝒮$
- **Set**: A collection of objects or outcomes.
	- Properties
		- **Finite**: Has a specific integer number of elements (like the sides of a die).
		- Infinite
			- **Infinite Countable**: You can count them $1, 2, 3...$ forever (like all positive integers).
			-  **Infinite Uncountable**: There are so many elements you can't even start a list (like all the decimal numbers between 0 and 1). 

	- Interiors
		- **Element ($s$):** An individual outcome within a set. We write $s \in S$ to say "$s$ is an element of set $S$".
		- **Subset ($A \subset B$):** $A$ is a subset of $B$ if **every** element in $A$ is also in $B$.
		- **Empty Set ($\emptyset$):** A set containing no elements at all. Think of it as the probability of me actually sticking to a diet—zero chance!
	- Relations
		- **Equality ($A = B$):** This only happens if $A \subset B$ AND $B \subset A$.
- **Union ($A \cup B$)** 
	- Definition
		- Think of this as the "OR" operation. The union includes any outcome that is in $A$, or in $B$, or in both. A key property is that if $A$ is already inside $B$, then their union is just $B$.
		Properties
			Commutativity
				A ∪ B ∪ C = (A ∪ B) ∪ C = A ∪ (B ∪ C)
			Associativity
				$A ∪ B = B ∪ A$
			Idempotent
				- $A ∪ 𝒮 = 𝒮$
			Property of inclusion
				if A ⊂ B, A ∪ B = B
			Property of Null
				 A ∪ ∅ = A; 
			Sequences
				$\bigcup_{i=1}^{\infty} A_i \quad \text{(countable union)}$
				$\bigcup_{i \in I} A_i \quad \text{(uncountable union)}$
- **The Intersection ($A \cap B$)
		Think of this as the "AND" operation. The intersection includes only outcomes that are in $A$ and in $B$ (the overlap).
	- **Definition**
		- $A \cap B = \{\, s \in \mathcal{S} \text{ such that } s \in A \text{ and } s \in B \,\}$
	- **Properties**
		- **Commutativity**
			- $A \cap B = B \cap A$
		- **Associativity**
			- $A \cap B \cap C = (A \cap B) \cap C = A \cap (B \cap C)$
		- **Idempotent**
			- $A \cap A = A$
		- **Identity (Universal set)**
			- $A \cap \mathcal{S} = A$
		- **Property of Null**
			- $A \cap \emptyset = \emptyset$
		- **Property of inclusion**
			- if $A \subset B$, then $A \cap B = A$
	- **Sequences**
		- For $A_1, A_2, \dots, A_n$:
			- $A_1 \cap A_2 \cap \cdots \cap A_n = \bigcap_{i=1}^{n} A_i$
		- $\bigcap_{i=1}^{\infty} A_i \quad \text{(countable intersection)}$
		- $\bigcap_{i \in I} A_i \quad \text{(uncountable intersection)}$
- Complement ($Ac = {s ∈ 𝒮; s ∉ A}$)
	- Think of this as **"NOT"**. The complement of $A$ is everything in the sample space $\mathcal{S}$ that is **not** in $A$.
	- **Definition**
		- $A^c = \{\, s \in \mathcal{S} \; ; \; s \notin A \,\}$
	- **Basic Properties**
		- **Double complement**
			- $(A^c)^c = A$
		- **Union with complement**
			- $A \cup A^c = \mathcal{S}$
		- **Intersection with complement**
			- $A \cap A^c = \emptyset$
		- **Complement of empty set**
			- $\emptyset^c = \mathcal{S}$
		- **Complement of sample space**
			- $\mathcal{S}^c = \emptyset$
- Distributive properties
	- These rules explain how $\cap$ and $\cup$ “distribute” over each other, and how complements interact with unions/intersections (De Morgan’s Laws).
	- **Distributive Laws**
		- **Intersection distributes over union**
			- $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$
		- **Union distributes over intersection**
			- $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$
	- **De Morgan’s Laws (finite)**
		- $(A \cup B)^c = A^c \cap B^c$
		- $(A \cap B)^c = A^c \cup B^c$
	- **De Morgan’s Laws (families of sets)**
		- $\left(\bigcup_{i \in I} A_i\right)^c = \bigcap_{i \in I} A_i^{\,c}$
		- $\left(\bigcap_{i \in I} A_i\right)^c = \bigcup_{i \in I} A_i^{\,c}$
- **Disjoint (Mutually Exclusive) Events**
	- Two events are **disjoint** if they have **no outcomes in common**.

	- **Two events**
		- $A$ and $B$ are disjoint if
			- $A \cap B = \emptyset$

	- **Finite collection**
		- A collection $A_1, A_2, \dots, A_n$ is disjoint (mutually exclusive) if for all $i \ne j$,
			- $A_i \cap A_j = \emptyset$

	- **Infinite collection**
		- An infinite collection $A_1, A_2, \dots$ is disjoint if for all $i \ne j$,
			- $A_i \cap A_j = \emptyset$
- **Axioms of Probability Itself** 
	- Probabilities are functions over a sample space $\mathcal{S}$ that measure the likelihood of events.
	- A probability is a specification of numbers on the sample space that satisfies the axioms below.
	- **Axioms**
		1. **Nonnegativity**
			- For every event $A \subset \mathcal{S}$,
				- $\Pr(A) \ge 0$
		2. **Normalization**
			- $\Pr(\mathcal{S}) = 1$
		3. **Countable Additivity (for disjoint events)**
			- For every infinite sequence of disjoint events $A_1, A_2, \dots$ such that $A_i \subset \mathcal{S}$,
				- $\Pr\!\left(\bigcup_{i=1}^{\infty} A_i\right) = \Pr(A_1) + \Pr(A_2) + \cdots$
				- $\Pr\!\left(\bigcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} \Pr(A_i)$

Lecture 1: 69 
# 1.2
It's important to be able to justify properties of the relations of events using the axioms and properties of them. Additionally, most basic set relations can be easily graphically represented as areas (This will be critical later on).

- **Additivity + Decomposition**
	- **Disjoint Additivity (finite)**
		- If $A_1,\dots,A_n$ are disjoint, then
			- $\Pr\!\left(\bigcup_{i=1}^{n}A_i\right)=\sum_{i=1}^{n}\Pr(A_i)$

	- **Union Decomposition (Inclusion–Exclusion, 2 sets)**
		- $\Pr(A\cup B)=\Pr(A)+\Pr(B)-\Pr(A\cap B)$
		- **Interpretation**
			- Add both, subtract the overlap you counted twice.

	- **Partition / Split Identity**
		- $B = (B\cap A)\cup(B\cap A^c)$  (disjoint union)

	- **Difference Identity**
		- $\Pr(B\cap A^c)=\Pr(B)-\Pr(A\cap B)$

	- **Nested-Set Simplification**
		- If $A\subset B$, then $A\cap B=A$, so
			- $\Pr(B\cap A^c)=\Pr(B)-\Pr(A)$

	- **Constraint Solving (from totals)**
		- If $\Pr(A\cup B)=1$, then
			- $\Pr(A\cap B)=\Pr(A)+\Pr(B)-1$
- **Probability as Measure**
	- **Measure Model**
		- When probability is proportional to “size” in $\mathcal{S}$:
			- $\Pr(E)=\dfrac{\text{Measure}(E)}{\text{Measure}(\mathcal{S})}$
	- **Common measures**
		- Area (2D), length (1D), volume (3D), etc.
	- **Use case**
		- Events correspond to regions; probability comes from relative size.
Lecture 2: 12 
# 2.1
In a simple finite sample space $S$, where all outcomes are equally likely, the probability of an event $A$ is formally defined by the ratio of the size of the event set to the total size of the sample space. This relationship is expressed mathematically as $Pr(A) = \frac{|A|}{|S|}$. Because this model relies entirely on the cardinality of sets, the crux of the theory involves using combinatorial operations to determine these values when the sample space is too large for manual enumeration.

The most fundamental operation is the **Multiplication Principle**, which states that if an experiment consists of $k$ independent parts where each part $i$ has $n_i$ outcomes, the total number of outcomes in the sample space is the product $n_1 \times n_2 \times \dots \times n_k$. This serves as the [[basis]] for **Permutations**, denoted as $P_{n,k}$, which count the number of ways to select $k$ items from a set of $n$ unique items without replacement when the order of selection matters. Formally, this is calculated using factorials as $P_{n,k} = \frac{n!}{(n-k)!}$. These principles allow for the calculation of probabilities in complex scenarios, such as the **Birthday Problem**, by using the law of complements ($Pr(A) = 1 - Pr(A^c)$) to find the likelihood that at least two individuals in a group share a birthday.

Example: The Birthday Problem for a Group of 3

To find the probability that at least two people in a group of $k=3$ share a birthday, we first calculate the probability of the complement ($A^c$), which is the event that all three have different birthdays.

- The total number of possible birthday combinations for 3 people is $|S|= 365 \times 365 \times 365 = 365^3$.
- The number of ways they can all have unique birthdays is the permutation $P_{365,3} = 365 \times 364 \times 363$.
- The probability that nobody shares a birthday is $Pr(A^c) = \frac{P_{365,3}}{365^3}$.
- Finally, the probability that at least two people share a birthday is $Pr(A) = 1 - \frac{P_{365,3}}{365^3}$
- **Finite Sample Space Framework**
	- Finite sample space notation:
		- Finding probabilities in a finite sample space is about finding the probability of each element in the sample space.
		- $\mathcal{S}=\{s_1,\dots,s_n\}$
	- Probability assignment to outcomes:
		- $\Pr(s_i)=p_i$
	- Probability bounds:
		- $p_i\in[0,1]$
	- Total probability condition:
		- $\sum_{i=1}^n p_i=1$
- **Simple (Equally Likely) Sample Spaces**
	- Equal likelihood condition:
		- $p_i=\frac{1}{n}$
	- Event probability by counting:
		- $\Pr(A)=\frac{m}{n}$
- **Multiplication Principle**
	- Multi-stage outcome structure:
		- $(u_1,\dots,u_k)$
	- Product rule for total outcomes:
		- $n_1 \times n_2 \times \cdots \times n_k$
- **Permutations (Without Replacement)**
	- Ordered selection formula:
		- $n(n-1)\cdots(n-k+1)$
	- Permutation notation:
		- $P_{n,k}=\frac{n!}{(n-k)!}$
	- Factorial definition:
		- $n!=n(n-1)\cdots1$
	- Special case:
		- $P_{n,n}=n!$
- **Counting-Based Probability Structures**
	- Total outcomes for repeated independent assignment:
		- $n^k$
	- Favorable outcomes via permutations:
		- $P_{n,k}$
	- Probability ratio structure:
		- $\Pr(A)=\frac{\text{favorable outcomes}}{\text{total outcomes}}$
- **Symmetry / Arrangement Probabilities**
	- Total orderings of $n$ distinct objects:
		- $n!$
	- Favorable grouped arrangements:
		- $k_1! \cdot k_2! \cdots$
	- Ratio structure:
		- $\Pr(E)=\frac{\text{favorable arrangements}}{\text{total arrangements}}$
Lecture 3: 23 
# 2.2

Lecture 2.2 centers on the transition from ordered sequences to unordered collections and the formal introduction of restricted probability environments. The primary new operation is the Binomial Coefficient, expressed as $\binom{n}{k}$, serves as a pure counting operator used to determine the number of distinct, unordered subsets of size $k$ that can be formed from a total population of $n$ unique elements. You use this operation in isolation when the objective is to count arrangements where the order of selection is irrelevant and there are no associated probabilities or "weights" attached to the items. For example, determining the number of ways to select a committee of 3 people from a group of 30, where every member has the same role, is calculated strictly as $\binom{30}{3} = \frac{30!}{3!(30-3)!}$ because the identity of the group is the only factor of interest. This operation also functions as the foundational building block for the Hypergeometric distribution, which calculates the probability of selecting a specific number of successes from a finite population without replacement by comparing ratios of these coefficients.

In contrast, the Binomial Theorem is the formal algebraic framework $(x+y)^n = \sum_{k=0}^n \binom{n}{k} x^k y^{n-k}$ that describes the expansion of a sum raised to a power. You transition from using the coefficient alone to using the full theorem when the problem involves independent trials where each outcome has a specific probability or "weight". In probability theory, this theorem defines the Binomial Distribution, where the variables $x$ and $y$ are replaced by the probability of success $p$ and failure $1-p$. For instance, to find the probability of obtaining exactly 3 heads in 10 coin tosses, the coefficient $\binom{10}{3}$ is used to count the number of possible sequences that result in three heads, but it must be integrated into the theorem's structure to account for the probability of those specific events occurring, resulting in $\mathbb{P}(X=3) = \binom{10}{3} p^3 (1-p)^7$. Thus, you use the coefficient to count the "how many" and the theorem to calculate the "how likely" across a full distribution.

The second core concept is **Conditional Probability**, which formalizes how the probability of an event $A$ changes when we have prior knowledge that another event $B$ has already occurred. This is understood as a **reduction of the sample space** from the original set $S$ to the restricted set $B$. The formal operation for this is $Pr(A|B) = \frac{Pr(A \cap B)}{Pr(B)}$, provided that $Pr(B) > 0$. By redefining the denominator to reflect only the outcomes where $B$ is true, we calculate the proportion of that "new world" in which $A$ also happens. For example, if we roll two dice and know the sum is odd, we discard all even-sum outcomes from our calculations and only count the relevant odd-sum outcomes to find the new probability of the total being less than 8.

- Combinations (unordered, without replacement):
	- $C_{n,k}=\dfrac{P_{n,k}}{k!}$
	- $\binom{n}{k}=\dfrac{n!}{k!(n-k)!}$
- Binomial theorem:
	- $(x+y)^n=\displaystyle\sum_{k=0}^{n}\binom{n}{k}x^k y^{\,n-k}$
- Multinomial coefficients:
	- Partition condition: $n_1+\dots+n_k=n$
	- $\displaystyle \binom{n}{n_1,\dots,n_k}=\frac{n!}{n_1!\cdots n_k!}$
	- Binomial as special case ($k=2$):
		- $\displaystyle \binom{n}{n_1,n_2}=\binom{n}{n_1}=\binom{n}{n_2}$
- Probability of unions:
	- Disjoint $A_1,\dots,A_n$:
		- $\Pr\!\left(\bigcup_{i=1}^{n}A_i\right)=\sum_{i=1}^{n}\Pr(A_i)$
	- Two events:
		- $\Pr(A\cup B)=\Pr(A)+\Pr(B)-\Pr(A\cap B)$
	- Three events:
		- $\Pr(A\cup B\cup C)=\Pr(A)+\Pr(B)+\Pr(C)$
		- $-\Pr(A\cap B)-\Pr(A\cap C)-\Pr(B\cap C)$
		- $+\Pr(A\cap B\cap C)$
	- General inclusion–exclusion:
		- $\Pr\!\left(\bigcup_{i=1}^{n}A_i\right)
		=\sum_i\Pr(A_i)
		-\sum_{i<j}\Pr(A_i\cap A_j)
		+\sum_{i<j<k}\Pr(A_i\cap A_j\cap A_k)
		-\dots
		+(-1)^{n+1}\Pr(A_1\cap\dots\cap A_n)$
- Conditional probability:
	- $\Pr(A\mid B)=\dfrac{\Pr(A\cap B)}{\Pr(B)}$
	- $\Pr(B\mid A)=\dfrac{\Pr(A\cap B)}{\Pr(A)}$
	- Product rule:
		- $\Pr(A\cap B)=\Pr(A)\Pr(B\mid A)$

# 3.1 
The study of independent events and the Law of Total Probability provides the mathematical framework for analyzing complex systems by breaking them down into simpler, isolated parts. Two events $A$ and $B$ are formally defined as independent if the occurrence of one provides no information about the likelihood of the other, which is expressed by the multiplication rule $Pr(A \cap B) = Pr(A) \cdot Pr(B)$. This relationship is functionally equivalent to stating that the conditional probability of an event is identical to its marginal probability, such as $Pr(A|B) = Pr(A)$. Mastery of this concept is necessary for multi-stage experiments, as it allows for the calculation of joint probabilities across different trials by simply finding the product of their individual likelihoods.

A critical distinction must be maintained between independent events and mutually exclusive (disjoint) events. While mutually exclusive events are physically separated in the sample space such that $A \cap B = \emptyset$ and $Pr(A \cap B) = 0$, they are inherently dependent because the occurrence of one guarantees that the other did not happen ($Pr(A|B) = 0$). In contrast, independent events are separated by information; knowing that $B$ occurred does not change the probability of $A$. If two events both have a probability greater than zero, they cannot be both independent and mutually exclusive. This distinction is vital for selecting the correct operation: use addition for mutually exclusive events to find the union, and use multiplication for independent events to find the intersection.

The Law of Total Probability serves as a "divide and conquer" operation for calculating the probability of a complex event $A$ by evaluating it across a partition of the sample space. A partition is a set of disjoint events $B_1, B_2, \dots, B_n$ that perfectly cover the entire space $S$ without any overlap. Instead of attempting to calculate $Pr(A)$ directly, the total probability is reconstructed by summing the conditional probabilities of $A$ given each piece of the partition, weighted by the probability of that piece occurring: $Pr(A) = \sum_{i=1}^{n} Pr(A|B_i)Pr(B_i)$. This operation is the fundamental precursor to Bayesian updating, as it provides the total "base rate" needed to understand how new evidence changes the probability of an initial hypothesis.

# 3.2

Lecture 3.2 formalizes the process of updating probability based on new evidence through Bayes' Theorem and introduces the mathematical framework for random variables. Bayes' Theorem allows for the calculation of a posterior probability, Pr(B∣A), by combining the prior probability of an event, Pr(B), with the likelihood of the evidence, Pr(A∣B), and the total probability of that evidence, Pr(A). The theorem is mathematically expressed as Pr(B∣A)=Pr(A)Pr(A∣B)×Pr(B)​, where the denominator is typically expanded using the Law of Total Probability as Pr(A∣B)Pr(B)+Pr(A∣Bc)Pr(Bc). This framework is the mathematical "crux" for diagnostic testing and any scenario where an initial belief must be adjusted in light of observed data.

The lecture then transitions from specific events to the broader concept of random variables, which are numerical descriptions of the outcomes of an experiment. A random variable X is defined as discrete if its range of possible values is finite or countably infinite. The behavior of a discrete random variable is characterized by its probability mass function (PMF), fX​(x)=Pr(X=x), which must satisfy the fundamental properties that 0≤fX​(x)≤1 for all x and the sum of all probabilities across its support must equal exactly 1, written as $∑_{x∈D}​f_X​(x)=1$. This abstraction allows for the calculation of probabilities for subsets of outcomes, Pr(X∈A), by summing the PMF values for all x belonging to that subset.

# 4.1


Lecture 4.1focuses on the classification of common discrete distributions and the foundational transition into continuous random variables. The first half of the lecture formalizes three discrete models: the **Discrete Uniform** distribution, where every value in a finite set $\{1, \dots, k\}$ is equally likely ($f_X(x) = 1/k$); the **Bernoulli** distribution ($X \sim \text{Bern}(p)$), which models a single trial with two outcomes (success with probability $p$ and failure with $1-p$); and the **Binomial** distribution ($X \sim \text{Binom}(n, p)$), which counts the number of successes in $n$ independent Bernoulli trials. The probability mass function for the Binomial case is defined as $f_X(x) = \binom{n}{x} p^x (1-p)^{n-x}$ for $x \in \{0, 1, \dots, n\}$.

The lecture then introduces **Continuous Random Variables**, which, unlike discrete variables, can take any value within an interval or union of intervals. These variables are described by a **Probability Density Function (PDF)**, denoted as $f_X(x)$, which must satisfy two critical properties: the function must be non-negative ($f_X(x) \ge 0$) for all $x$, and the total area under the curve must equal 1, expressed as $\int_{-\infty}^{\infty} f_X(x) dx = 1$. A key distinction highlighted is that for any continuous random variable, the probability of the variable taking an exact single value is zero ($Pr(X=c) = 0$), meaning probabilities are only meaningful over intervals.

The final "crux" of the lecture is the operational use of integration to find probabilities for continuous variables. To calculate the probability that $X$ falls between two values $a$ and $b$, one must compute the definite integral of the PDF over that range: $Pr(a < X < b) = \int_a^b f_X(x) dx$. This corresponds graphically to finding the area under the density curve between those two points. The lecture demonstrates this by solving for an unknown normalizing constant $c$ in a PDF (e.g., $f(x) = c(x+1)$) by setting the total integral to 1 and then using that verified density to compute specific interval probabilities.

# 4.2 
Lecture 4.2 introduces the Cumulative Distribution Function (CDF) as a universal tool that describes the behavior of any random variable, whether discrete, continuous, or mixed. The CDF, denoted as $F_X(x)$, is formally defined as the probability that the random variable $X$ takes a value less than or equal to $x$, expressed mathematically as $F(x) = Pr(X \le x)$. This function is fundamentally non-decreasing and bounded between $0$ and $1$, with the specific limits $\lim_{x \to -\infty} F(x) = 0$ and $\lim_{x \to \infty} F(x) = 1$. While a discrete random variable results in a "step function" CDF that is constant between values and jumps at specific points of the support, a continuous random variable yields a smooth, continuous CDF.

For continuous random variables, the CDF acts as the mathematical bridge to the Probability Density Function (PDF) through the fundamental theorem of calculus. The CDF is calculated by integrating the PDF from negative infinity up to the point $x$, such that $F(x) = \int_{-\infty}^x f(t) dt$. Conversely, if the CDF is known, the PDF can be recovered by taking the derivative: $F'(x) = f(x)$. This relationship allows for the calculation of probabilities over any interval $(a, b]$ by simply finding the difference in the CDF values at the endpoints, $Pr(a < X \le b) = F(b) - F(a)$, which eliminates the need for repeated integration once the CDF is derived.

The final major concept is the **Quantile Function**, which effectively serves as the inverse of the CDF. While the CDF takes a value $x$ and returns a probability $p$, the quantile function takes a probability $p \in (0,1)$ and returns the corresponding value $x$ such that $F(x) \ge p$. For continuous variables with one-to-one CDFs, this is simply $x = F^{-1}(p)$. A prominent example is the **median**, or 0.5-quantile, which is the value $x$ where $F(x) = 0.5$. In the case of a $X \sim \text{Uniform}[a, b]$ distribution, the $p$-quantile is derived by solving $p = \frac{x-a}{b-a}$, leading to the linear transformation $x = pb + (1-p)a$.

# 5.1
Lecture 5.1 introduces **Bivariate Distributions**, which formally describe the simultaneous behavior of two random variables, $X$ and $Y$, by assigning probabilities to pairs of real numbers. For discrete variables, this relationship is defined by a **Joint Probability Mass Function (PMF)**, $f(x,y) = Pr(X=x, Y=y)$, which must be non-negative for all pairs and sum to exactly 1 over the entire support. To find the probability that a pair $(X,Y)$ falls within a specific set $C$, you perform the operation of summing the joint PMF values for all coordinate pairs $(x,y)$ belonging to that set: $Pr[(X,Y) \in C] = \sum \sum_{(x,y) \in C} f(x,y)$.

In the continuous case, the variables are described by a **Joint Probability Density Function (PDF)**, $f(x,y)$, where probabilities are represented as volumes under a surface rather than sums of points. A valid joint PDF must satisfy two conditions: it must be non-negative everywhere ($f(x,y) \ge 0$), and its total integral over the entire $xy$-plane must equal 1, expressed as $\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f(x,y) dx dy = 1$. To calculate the probability that $(X,Y)$ lies within a region $C$, you compute the double integral of the PDF over that region: $Pr((X,Y) \in C) = \int \int_C f(x,y) dx dy$.

The **Joint Cumulative Distribution Function (CDF)**, $F(x,y) = Pr(X \le x, Y \le y)$, serves as a universal tool that calculates the probability that $X$ and $Y$ fall within a semi-infinite rectangle. For continuous distributions, the joint PDF can be recovered by taking the second-order partial derivative of the CDF: $f(x,y) = \frac{\partial^2}{\partial x \partial y} F(x,y)$. A primary operation using the CDF is calculating the probability of a rectangular region $[a,b] \times [c,d]$. This is done using an inclusion-exclusion formula that subtracts the overlapping areas and adds back the doubly-subtracted corner: $Pr(a < X \le b, c < Y \le d) = F(b,d) - F(a,d) - F(b,c) + F(a,c)$.

Example: Finding Probability Over a Rectangle

Given a joint CDF specified as $F(x,y) = \frac{1}{156}xy(x^2 + y)$ for $0 \le x \le 3$ and $0 \le y \le 4$, we can find $Pr(1 \le X \le 2, 1 \le Y \le 2)$ by evaluating the function at the corners of the rectangle:

- Evaluate the four corners: $F(2,2) = \frac{24}{156}$, $F(1,2) = \frac{6}{156}$, $F(2,1) = \frac{10}{156}$, and $F(1,1) = \frac{2}{156}$.
    
- Apply the rectangle formula: $Pr(1 \le X \le 2, 1 \le Y \le 2) = \frac{1}{156}[24 - 6 - 10 + 2]$.
    
- The final result is $\frac{10}{156}$, which simplifies to $\frac{5}{78}$.

# 5.2
Lecture 5.2 focuses on the practical application of discrete distributions to system reliability and the extension of joint continuous probability to non-rectangular regions. A primary application is modeling the failure of independent components using the Binomial distribution, where $X$ represents the number of failed units in a system of $n$ components with failure probability $p$. The mathematical operation for finding the probability of at least one failure often utilizes the law of complements, $Pr(X \ge 1) = 1 - Pr(X=0)$, while more complex queries like "at least two failed given at least one failed" require the conditional probability formula $Pr(X \ge 2 | X \ge 1) = \frac{Pr(X \ge 2)}{Pr(X \ge 1)}$.

The lecture also explores joint continuous distributions where the region of interest is not a simple rectangle, requiring the careful setup of double integrals with variable bounds. To calculate the probability of an event such as $X \ge Y$, the inner integral must be defined by the boundary line $y=x$ rather than a constant value. This is formally expressed as $Pr(X \ge Y) = \int_{x=a}^{b} \int_{y=c}^{x} f(x,y) dy dx$ or similarly by swapping the order of integration. This shift from fixed to functional bounds is the essential advancement for evaluating relationships between two continuous variables across a shared domain.

### Example: System Reliability and Conditional Failure

In an electronic system with 4 independent components, each having a failure probability of $p=0.1$, the probability that at least one component fails is calculated using $X \sim \text{Binom}(4, 0.1)$. By applying the complement rule, $1 - Pr(X=0) = 1 - \binom{4}{0}(0.1)^0(0.9)^4$, the probability is found to be $0.3439$. If we then want to find the probability that at least two components have failed given that at least one has already failed, we use the conditional formula:

$$Pr(X \ge 2 | X \ge 1) = \frac{Pr(X \ge 2 \cap X \ge 1)}{Pr(X \ge 1)} = \frac{Pr(X \ge 2)}{0.3439}$$

This illustrates how foundational discrete models are integrated with conditional logic to solve multi-stage reliability problems.
# 6.1
Marginal distributions provide the mathematical framework for isolating the individual behavior of a single random variable from a joint distribution that describes multiple variables simultaneously. In the discrete case, the marginal probability mass function (PMF) of X is derived by "summing out" the other variable Y, which involves totaling the joint probabilities across all possible outcomes of y for each fixed value of x: fX​(x)=∑y​f(x,y). This operation effectively collapses a two-dimensional probability table into a one-dimensional distribution, focusing purely on the marginal likelihoods associated with the variable of interest.

For continuous random variables, the marginal probability density function (PDF) is obtained by integrating the joint PDF f(x,y) over the entire range of the variable that is being excluded. To find the marginal density fX​(x), the joint density is integrated with respect to y, expressed as fX​(x)=∫−∞∞​f(x,y)dy. This process is graphically understood as projecting the volume under the joint density surface onto the axis of the variable being retained, resulting in a density curve whose total area remains equal to 1.

The principles of marginalization also extend to "mixed" scenarios where a discrete variable is dependent on a continuous parameter. In this case, the marginal PMF of the discrete variable is found by integrating the product of its conditional PMF and the marginal PDF of the continuous parameter. For example, if the number of defective items X follows a binomial distribution X∣P=p∼Bin(n,p) and the defective rate P is uniformly distributed over (0,1), the marginal PMF of X is calculated as fX​(x)=∫01​(xn​)px(1−p)n−xdp. Completing this integration yields fX​(x)=n+11​ for x∈{0,1,…,n}, demonstrating how the marginal distribution of a discrete variable becomes a discrete uniform distribution when the underlying success probability is completely unknown.
# 7.1
Lecture 7.1 introduces the mathematical framework for finding the distribution of a new random variable Y that is defined as a function of an existing variable X, expressed as Y=r(X). The crux of this knowledge lies in understanding that the probability of Y is determined by the "pre-image" or the set of all values of X that map to a specific value of y. In the discrete case, the probability mass function (PMF) g(y) is calculated by summing the probabilities of all x such that r(x)=y, written as g(y)=∑x:r(x)=y​fX​(x). This operation is essentially a grouping process where the original probabilities are reallocated to their new numerical targets based on the function r.

For continuous random variables, the transformation process requires accounting for the "stretching" or "shrinking" of the probability density as the variable's units change. The first approach, the CDF Method, finds the cumulative distribution function G(y)=Pr(r(X)≤y) by integrating the original density fX​(x) over the region where r(x)≤y, and then differentiating the result to obtain the density g(y)=G′(y). Alternatively, the Transformation Theorem (or Method of Transformations) provides a direct formula for one-to-one, differentiable functions: g(y)=fX​(r−1(y))![](data:image/svg+xml;utf8,<svg%20xmlns="http://www.w3.org/2000/svg"%20width="0.333em"%20height="1.800em"%20viewBox="0%200%20333%201800"><path%20d="M145%2015%20v585%20v600%20v585%20c2.667,10,9.667,15,21,15%0Ac10,0,16.667,-5,20,-15%20v-585%20v-600%20v-585%20c-2.667,-10,-9.667,-15,-21,-15%0Ac-10,0,-16.667,5,-20,15z%20M188%2015%20H145%20v585%20v600%20v585%20h43z"></path></svg>)​dyd​r−1(y)![](data:image/svg+xml;utf8,<svg%20xmlns="http://www.w3.org/2000/svg"%20width="0.333em"%20height="1.800em"%20viewBox="0%200%20333%201800"><path%20d="M145%2015%20v585%20v600%20v585%20c2.667,10,9.667,15,21,15%0Ac10,0,16.667,-5,20,-15%20v-585%20v-600%20v-585%20c-2.667,-10,-9.667,-15,-21,-15%0Ac-10,0,-16.667,5,-20,15z%20M188%2015%20H145%20v585%20v600%20v585%20h43z"></path></svg>)​. In this equation, the term ![](data:image/svg+xml;utf8,<svg%20xmlns="http://www.w3.org/2000/svg"%20width="0.333em"%20height="1.800em"%20viewBox="0%200%20333%201800"><path%20d="M145%2015%20v585%20v600%20v585%20c2.667,10,9.667,15,21,15%0Ac10,0,16.667,-5,20,-15%20v-585%20v-600%20v-585%20c-2.667,-10,-9.667,-15,-21,-15%0Ac-10,0,-16.667,5,-20,15z%20M188%2015%20H145%20v585%20v600%20v585%20h43z"></path></svg>)​dyd​r−1(y)![](data:image/svg+xml;utf8,<svg%20xmlns="http://www.w3.org/2000/svg"%20width="0.333em"%20height="1.800em"%20viewBox="0%200%20333%201800"><path%20d="M145%2015%20v585%20v600%20v585%20c2.667,10,9.667,15,21,15%0Ac10,0,16.667,-5,20,-15%20v-585%20v-600%20v-585%20c-2.667,-10,-9.667,-15,-21,-15%0Ac-10,0,-16.667,5,-20,15z%20M188%2015%20H145%20v585%20v600%20v585%20h43z"></path></svg>)​, often called the Jacobian in higher dimensions, acts as a scaling factor that preserves the total probability of 1 under the change of variables.

The lecture concludes by extending these principles to functions of multiple random variables, specifically the sum Y=X1​+X2​. When X1​ and X2​ are independent, the density of their sum is found through an operation called **convolution**. For continuous variables, this is calculated using the integral g(y)=∫−∞∞​f1​(y−x2​)f2​(x2​)dx2​. This operation is necessary because it accounts for every possible way the two variables can add up to the value y. By fixing X2​ at a value x2​, the other variable must be exactly y−x2​, and the convolution integrates across all such valid pairs in the joint support.
# 7.2
Lecture 7.2 focuses on the distributional properties of extreme values in a set of random variables and the formalization of expected value as a measure of central tendency. The first core concept involves finding the distributions of the maximum, $Y_n = \max\{X_1, \dots, X_n\}$, and the minimum, $Y_1 = \min\{X_1, \dots, X_n\}$, of $n$ independent and identically distributed (i.i.d.) random variables with cumulative distribution function $F(y)$. The cumulative distribution function for the maximum is derived as $G_n(y) = [F(y)]^n$, based on the logic that for the maximum to be less than or equal to $y$, every individual variable must be less than or equal to $y$. Conversely, the CDF for the minimum is $G_1(y) = 1 - [1 - F(y)]^n$, derived from the complement event that all variables must be strictly greater than $y$. These "order statistics" are vital for assessing system reliability, where a system might fail if its weakest component fails (minimum) or if all redundant components fail (maximum).

The second major "crux" is the formal definition and operational properties of the expected value, $E(X)$, which represents the long-run average of a random variable. For a discrete variable, the expectation is the weighted sum $E(X) = \sum_{x \in D} x f(x)$, while for a continuous variable, it is the integral $E(X) = \int_{-\infty}^{\infty} x f(x) dx$. The utility of expectation is greatly enhanced by its linear properties, specifically $E(aX + b) = aE(X) + b$, which allows for the calculation of averages for transformed variables without deriving their new distributions. Furthermore, the linearity of expectation extends to sums of multiple variables, $E(\sum_{i=1}^n a_i X_i) = \sum_{i=1}^n a_i E(X_i)$, a powerful result that holds regardless of whether the variables are independent. However, for independent variables specifically, the expectation of a product simplifies to the product of individual expectations, $E(\prod_{i=1}^n X_i) = \prod_{i=1}^n E(X_i)$. These operations provide the foundational tools for characterizing the mean behavior of common distributions, such as the Poisson distribution where $E(X) = \lambda$ and the Geometric distribution where $E(X) = \frac{1-p}{p}$.
# 8.1
Lecture 8.1 formalizes the measurement of "spread" and "co-movement" in random variables through the concepts of Variance and Covariance. The **Variance** of a random variable $X$, denoted as $Var(X)$ or $\sigma^2$, is defined as the expected value of the squared deviation from its mean $\mu$, expressed as $Var(X) = E[(X-\mu)^2]$. This operation serves as the "crux" for quantifying uncertainty; while the expectation $E(X)$ provides the center of the distribution, the variance measures how much the values typically fluctuate around that center. For practical calculations, the definition is often expanded into the more efficient computational formula $Var(X) = E(X^2) - [E(X)]^2$, which allows you to find the variance using the first two moments of the distribution. A key property to master is that variance is always non-negative ($Var(X) \ge 0$) and scales quadratically with constants, meaning $Var(aX + b) = a^2 Var(X)$.

The lecture extends this logic to the relationship between two variables through **Covariance**, which measures the linear association between $X$ and $Y$. Formally, $Cov(X,Y) = E[(X-\mu_X)(Y-\mu_Y)]$, which simplifies to the operational form $Cov(X,Y) = E(XY) - E(X)E(Y)$. This value indicates the direction of the relationship: a positive covariance suggests the variables tend to increase together, while a negative covariance suggests one increases as the other decreases.

A critical nuance is the relationship between independence and covariance: if two variables are independent, their covariance is mathematically guaranteed to be zero because $E(XY) = E(X)E(Y)$. However, the converse is not necessarily true; a covariance of zero only implies a lack of _linear_ association, meaning the variables could still be dependent through a non-linear relationship. This distinction is vital when assessing the total variance of a sum of variables, which is calculated as $Var(X+Y) = Var(X) + Var(Y) + 2Cov(X,Y)$. If the variables are independent, this "totaling" operation simplifies to the sum of individual variances, but in all other cases, the co-movement must be accounted for.
# 8.2
Lecture 8.2 formalizes the concept of **Correlation**, a dimensionless measure of linear association that standardizes covariance by the product of the variables' standard deviations. The correlation coefficient, denoted by $\rho(X,Y)$, is defined as $Corr(X,Y) = \frac{Cov(X,Y)}{\sigma_X \sigma_Y}$. A fundamental result derived from the **Cauchy-Schwarz Inequality**—which states that $[Cov(X,Y)]^2 \le \sigma_X^2 \sigma_Y^2$—ensures that correlation is always bounded between $-1$ and $1$. While independent variables must have a correlation of zero, a zero correlation does not necessarily imply independence, as it only detects the absence of a linear relationship.

The lecture then introduces the **Normal Distribution**, focusing specifically on the **Standard Normal Distribution** ($Z \sim N(0,1)$). The behavior of $Z$ is described by its cumulative distribution function $\Phi(x) = \int_{-\infty}^{x} \frac{1}{(2\pi)^{1/2}} \exp(-\frac{1}{2}u^2) du$. Because this integral has no closed-form algebraic solution, probabilities are determined using the Standard Normal Table, which provides values for $\Phi(x)$ for various $x \ge 0$. Due to the symmetry of the bell curve around zero, the probability for negative values is calculated using the identity $\Phi(-x) = 1 - \Phi(x)$. Any normal random variable $X$ with mean $\mu$ and variance $\sigma^2$ can be analyzed by transforming it into the standard normal variable through the "z-score" operation $Z = \frac{X-\mu}{\sigma}$.
