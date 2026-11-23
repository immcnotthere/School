---
type: concept
parent: "[[Statistics]]"
domain: stats
status: draft
---
The bayse theorem is just the application of the multiplication rule and the next step is to apply 

the law of total probability is telling go case by case so sigma of the numerator 

## STAT 131 — Discussion (Week 4) Winter 2026

### Notation and formulas

#### Conditional probability

If $\Pr(B)>0$, then  
$$  
\Pr(A\mid B)=\frac{\Pr(A\cap B)}{\Pr(B)}.  
$$

Equivalently,  
$$  
\Pr(A\cap B)=\Pr(B)\Pr(A\mid B)=\Pr(A)\Pr(B\mid A).  
$$

#### Law of total probability (partitions)

If ${B_1,\dots,B_k}$ is a partition of $S$ with $\Pr(B_i)>0$, then  
$$  
\Pr(A)=\sum_{i=1}^k \Pr(A\mid B_i)\Pr(B_i).  
$$

#### Bayes’ theorem (invert conditionals)

If $\Pr(B)>0$, then  
$$  
\Pr(A\mid B)=\frac{\Pr(B\mid A)\Pr(A)}{\Pr(B)}.  
$$

With a partition ${B_1,\dots,B_k}$,  
$$  
\Pr(B_j\mid A)=\frac{\Pr(A\mid B_j)\Pr(B_j)}{\sum_{i=1}^k \Pr(A\mid B_i)\Pr(B_i)}.  
$$

#### Independence vs. disjointness

- $A$ and $B$ independent $\iff \Pr(A\cap B)=\Pr(A)\Pr(B)$ (equivalently $\Pr(A\mid B)=\Pr(A)$ when $\Pr(B)>0$).
    
- Disjoint means $A\cap B=\varnothing$ so $\Pr(A\cap B)=0$. If $\Pr(A)>0$ and $\Pr(B)>0$, disjoint events cannot be independent.
    

#### Discrete random variables (pmf or pf)

A discrete random variable $X$ takes values in a countable set. Its pmf (or pf) is  
$$  
f_X(x)=\Pr(X=x),  
$$  
and  
$$  
\sum_x f_X(x)=1.  
$$

To compute probabilities, add pmf (pf) values:  
$$  
\Pr(X\in S)=\sum_{x\in S} f_X(x).  
$$

#### What to write first (workflow)

- Define events and what is given (prior probabilities, conditional probabilities, partition).
    
- Compute the denominator using total probability, then apply Bayes.
    
- For independence: compute $\Pr(A\cap B)$ and compare with $\Pr(A)\Pr(B)$.
    
- For a pmf (pf): list all possible values of $X$, then compute $\Pr(X=x)$ for each.
    

---

## STAT 131 — Discussion (Week 4) Winter 2026

### Monday Version

### Problem 1: Bayes’ theorem (test accuracy)

A screening test is used to detect a disease in individuals from a given population. Suppose that if an individual from this population is chosen randomly, the probability that this individual has the disease is $0.01$. In addition, assume that if an individual from this population has the disease the probability that the individual tests positive is $0.95$. Finally, assume that if an individual does not have the disease the probability that this person tests positive is $0.08$.

(a) If an individual is randomly sampled from the population, what is the probability that the individual tests positive?

(b) If an individual tests positive, what is the probability that this individual actually has the disease?

(c) Interpret your result in (b). Is it higher or lower than $0.01$?

---

### Problem 2: Partitions + Bayes + independence + pmf (or pf)

(a) **Machines (partition + Bayes).**  
Three machines $M_1,M_2,M_3$ produce items with  
$$  
\Pr(M_1)=0.20,\quad \Pr(M_2)=0.30,\quad \Pr(M_3)=0.50,  
$$  
and defect probabilities  
$$  
\Pr(D\mid M_1)=0.01,\quad \Pr(D\mid M_2)=0.02,\quad \Pr(D\mid M_3)=0.03,  
$$  
where $D=$ “item is defective.” Compute $\Pr(M_2\mid D)$.

(b) **Independence vs. disjointness.**  
Let $A$ and $B$ be events with $\Pr(A)=\tfrac13$ and $\Pr(B)=\tfrac14$, and assume $A$ and $B$ are independent. Compute $\Pr(A\cap B)$ and $\Pr(A\cup B)$. Then answer true/false with a one-line justification:

> If $A\cap B=\varnothing$ and $\Pr(A)>0$, $\Pr(B)>0$, then $A$ and $B$ are independent.

(c) **Discrete random variable (pmf).**  
A fair coin is tossed twice. You earn $2 for each head and lose $1 for each tail. Let $X=$ total earnings (in dollars). List the possible values of $X$ and compute the pmf  
$$  
f_X(x)=\Pr(X=x)  
$$  
for each value. Then compute $\Pr(X\ge1)$ using your pmf.

---

**Source:** STAT 131 — Discussion (Week 4), Winter 2026

P1 Workflow

Pr(C)=COVID=.01
Pr(H)=Healthy=.99
Pr(+)=Positive=?
Pr(+|H)=.08
Pr(+|C)=.95
