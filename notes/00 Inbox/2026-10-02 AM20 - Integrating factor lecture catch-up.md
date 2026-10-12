---
type: reference
domain: math
course: "AM20"
status: draft
---
# AM20: integrating factor lecture catch-up (2026-10-02)

Topic: [[AM20]]. Parked for review because I got lost in lecture.

## Form
y' + p(t)y = g(t).

- p(t) = what multiplies y.
- g(t) = what sits alone on the right.
- They are different slots, not equal to each other.
- Each may be a constant or a function of t, but never contain y. If y², sin y etc. appear, it is not linear and this method does not apply.
- If both are constants, separation also works.

| Equation | p | g |
|---|---|---|
| y' + ½y = ½e^(t/3) | ½ | ½e^(t/3) |
| y' + 2y = 3 | 2 | 3 |
| y' + ty = sin t | t | sin t |
| y' + (1/t)y = 0 | 1/t | 0 |
| y' + y² = t | not this form | |

## The 5 steps
1. Match the form: read off p and g.
2. μ = e^(∫p dt). The integral goes IN the exponent; μ = ∫p dt is wrong.
3. (μy)' = μg
4. μy = ∫μg dt + C
5. Divide by μ: y = (∫μg dt + C)/μ

## Worked: y' + ½y = ½e^(t/3)
- μ = e^(t/2).
- μg = ½e^(t/2 + t/3) = ½e^(5t/6).
- ∫μg dt = ½·(6/5)e^(5t/6) = (3/5)e^(5t/6).
- So e^(t/2)y = (3/5)e^(5t/6) + C, and y = (3/5)e^(t/3) + Ce^(-t/2).
- Check: substitute back and the result is ½e^(t/3).

## Two skills that blocked me
- Exponent rules: e^a·e^b = e^(a+b), e^a/e^b = e^(a-b).
- ∫e^(kt) dt = (1/k)e^(kt) + C (why: the derivative of e^(kt) is k·e^(kt)).

Drill task: Todoist "AM 20: drill the two skills that blocked the integrating-factor problem", due 2026-10-03.

No flashcards yet.

## In-class activity: xy' + 2y = 4x², y(1) = 2
Goal: find the function y(x) that satisfies the equation AND passes through (1, 2). The variable is x here instead of t.

0. Get y' alone: divide everything by x, so y' + (2/x)y = 4x. Then p = 2/x and g = 4x.
1. μ = e^(∫2/x dx) = e^(2 ln x) = e^(ln x²) = x². (Rule: e^(ln A) = A.)
2. (x²y)' = x²·4x = 4x³
3. x²y = ∫4x³ dx = x⁴ + C
4. y = x² + C/x²
5. Initial condition y(1) = 2: 2 = 1 + C, so C = 1.

Answer: y = x² + 1/x².
Check: xy' = 2x² - 2/x², 2y = 2x² + 2/x², sum = 4x². ✓

New skills from this one:
- Step 0: the coefficient on y' must be 1 first.
- e^(ln A) = A.
- Using the initial condition to find C.
