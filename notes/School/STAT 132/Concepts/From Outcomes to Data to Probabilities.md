---
type: reference
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
---
# From Outcomes to Data to Probabilities

One example the whole way down: **flip a fair coin twice. $X$ = the number of heads.**
Cards for this page: STAT 132 Cards - Ladder 03b Outcomes to Data (deck removed 2026-10-05).

## 0. Check yourself first (paper, 5 minutes, no peeking)
1. What goes **into** $X$, and what comes **out**?
2. What goes into $f$, and what comes out?
3. $X$ sends both HT and TH to 1. Is $X$ still a function?
4. What is $f(1)$, and how do you build it from the outcomes?
5. Ten readings of $X$ give counts 2, 6, 2 for the values 0, 1, 2. How do you turn the counts into numbers that add to 1?
6. In $f(x \mid p)$, which is fixed once you have data: the $x$'s or $p$?

Answers are at the bottom. Whichever station you missed, read that one twice.

## Station 1: $X$ is a machine from outcomes to numbers
The outcomes $\omega$ are the things that can physically happen. $X$ reads one number off each:

| outcome $\omega$ | $X(\omega)$ |
| --- | --- |
| HH | 2 |
| HT | 1 |
| TH | 1 |
| TT | 0 |

A **function** has one rule: **each input gets exactly one output.** It does not have to be **one-to-one** (different inputs giving different outputs). $X$ is not one-to-one: HT and TH share the output 1. That is allowed, and it is the whole trick of Station 3.

$X$ never outputs a probability. $X(\omega)$ is always a reading: a face, a count, a number of minutes.

## Station 2: $P$ puts weight on outcomes
A fair coin makes all four outcomes equally likely, so each gets $\frac{1}{4}$.
They add to 1 because $\Omega = \{HH, HT, TH, TT\}$ is everything that can happen: something in it is certain.

$P$'s input is an **event** (a set of outcomes), and its output is a probability.

## Station 3: $f$ collects the weight onto the numbers
Now ask about numbers instead of outcomes. $f(x)$ = add up $P$ of **every outcome that $X$ sends to $x$**:

| $x$ | outcomes sent to $x$ | $f(x)$ |
| --- | --- | --- |
| 0 | TT | $\frac{1}{4}$ |
| 1 | HT, TH | $\frac{1}{4} + \frac{1}{4} = \frac{1}{2}$ |
| 2 | HH | $\frac{1}{4}$ |

That is all $f(x) = P(X = x)$ means: "$X = 1$" is the set {HT, TH}, and $P$ weighs that set.

**Why the total is still 1:** every outcome goes to exactly one bucket (a function gives one output per input). So when you move the weight from outcomes to numbers, none is lost and none is counted twice: $\frac{1}{4} + \frac{1}{2} + \frac{1}{4} = 1$.

## Station 4: data are readings of $X$; counts add to $n$, not 1
Do the two-flip experiment 10 times and write down each reading. These are your **data**, lowercase because they are now fixed numbers: $x_1, \dots, x_{10}$ = 1, 2, 1, 0, 1, 1, 2, 1, 0, 1.

Tally them:

| value | count | count ÷ 10 |
| --- | --- | --- |
| 0 | 2 | 0.2 |
| 1 | 6 | 0.6 |
| 2 | 2 | 0.2 |
| total | **10** | **1** |

The counts add to $n = 10$, not to 1. **Dividing every count by $n$** gives the **relative frequencies**, which add to 1. This is the same normalizing move as in Ladder 04: divide by the total.

The relative frequency table is the data's own estimate of $f$. Compare: the data say 0.2, 0.6, 0.2; the fair-coin $f$ says 0.25, 0.5, 0.25. Close, not equal: 10 runs is a small sample. With more runs the two tables get closer (the Law of Large Numbers).

## Station 5: data vs the model $f(x \mid p)$
Suppose the coin might not be fair. The model is now a whole family of tables, one for each $p$: $f(x \mid p)$ is Binomial(2, $p$). Read the bar as "given": the table you get once $p$ is chosen.

- The **data are fixed**: you already saw 1, 2, 1, 0, ...
- **$p$ is unknown**: it is the input you are trying to learn.
- The **likelihood** scores each possible $p$ by how well its table explains the data you saw.
- A first estimate: total heads ÷ total flips. Heads = $6 \times 1 + 2 \times 2 = 10$ out of $10 \times 2 = 20$ flips, so $p \approx \frac{10}{20} = 0.5$.

## Station 6: numbers that aren't counts
Scores, weights, or a formula like $g(x) = x$: if every value is at least 0 and the total is finite, **divide each by the total** and you have a valid pmf. For a curve, divide by the area. If any value is negative, no rescaling can make it a probability table.

## The picture to keep
- outcome $\omega$ → **X** → a number
- event (set of outcomes) → **P** → a probability
- number $x$ → **f** → a probability; $f$ asks $P$ about the event "$X = x$"
- data → tally → divide by $n$ → relative frequencies, an estimate of $f$

## Answers to section 0
1. In: an outcome. Out: a number.
2. In: a number $x$. Out: the probability $P(X = x)$.
3. Yes. A function only needs one output per input; sharing outputs is allowed.
4. $\frac{1}{2}$: add $P(HT) + P(TH) = \frac{1}{4} + \frac{1}{4}$.
5. Divide each by the total, 10: 0.2, 0.6, 0.2.
6. The $x$'s are fixed; $p$ is the unknown.
