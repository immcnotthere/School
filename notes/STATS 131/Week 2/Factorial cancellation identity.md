---
title: Factorial cancellation identity
aliases:
  - Factorial ratio identity
  - Falling factorial identity
  - Truncated factorial identity
tags:
  - math
  - counting
  - factorials
  - permutations
  - probability
---
# Factorial cancellation identity

## Core definition

### [[Factorial]]
For a positive integer $n$,
$$n!=n(n-1)(n-2)\cdots 2\cdot 1.$$

### Factorial cancellation identity
For integers $n\ge k\ge 1$,
$$n(n-1)(n-2)\cdots k=\frac{n!}{(k-1)!}.$$

Equivalently, for integers $n\ge r\ge 0$,
$$n(n-1)\cdots(n-r+1)=\frac{n!}{(n-r)!}.$$

Interpretation: dividing by the smaller factorial cancels the “tail” of $n!$.

---

## Why it works

Start with
$$n!=\big(n(n-1)\cdots k\big)\big((k-1)(k-2)\cdots 1\big).$$

But
$$(k-1)!=(k-1)(k-2)\cdots 1.$$

So
$$\frac{n!}{(k-1)!}=n(n-1)\cdots k.$$

---

## Domain-specific senses

### [[Counting]] without replacement
Use this when the number of choices decreases after each selection because repeats are not allowed.

### [[Permutations]]
An ordered selection of $r$ distinct items from $n$:
$$P(n,r)=n(n-1)\cdots(n-r+1)=\frac{n!}{(n-r)!}.$$

---

## Positive and negative signals

### Positive signals (use a factorial ratio)
- “$n$ choices, then $n-1$, then $n-2$, …”
- “No repeats,” “distinct,” “without replacement,” “at most one per box.”
- You see a product like $20\cdot 19\cdots 9$.

### Negative signals (don’t do this)
- Subtractions like $n!-k!$ usually do not match a counting story.
- If order does not matter, you likely need [[Combinations]] instead.

---

## Examples

### Ends at $9$
$$20\cdot 19\cdot 18\cdots 9=\frac{20!}{8!}.$$

### Ends at $4$
$$10\cdot 9\cdot 8\cdot 7\cdot 6\cdot 5\cdot 4=\frac{10!}{3!}.$$

### Quick sanity check against subtraction
For “2 balls into 3 boxes, no sharing”:
- Correct: $3\cdot 2=\frac{3!}{1!}=6$
- Wrong form: $3!-2!=4$

---

## Related links
- [[Factorial]]
- [[Falling factorial]]
- [[Permutations]]
- [[Combinations]]
- [[Binomial coefficient]]
- [[Sample space]]
- [[Injective function]]
