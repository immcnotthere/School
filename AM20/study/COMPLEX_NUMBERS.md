# Complex numbers — AM 20 review

Primary reference: uploaded *Review 1. Complex Numbers*, pp. 1–3. This is an original instructional summary aligned with Lecture 9.

## 1. What is a complex number?

A complex number is **z = a + bi**, where **i² = −1**. The real part is **a** and the imaginary part is **b**, *not* bi.

Example: for z = −3 + 4i, Re(z) = −3 and Im(z) = 4.

## 2. Arithmetic

Add the real parts and imaginary parts separately.

- (3 + 2i) + (1 − 5i) = **4 − 3i**
- (3 + 2i)(1 − 5i) = 3 − 15i + 2i − 10i² = **13 − 13i**

Remember: i³ = −i, i⁴ = 1; powers repeat every four.

## 3. Conjugates, modulus, division

For z = a + bi:
- Conjugate: **z̄ = a − bi**
- Modulus: **|z| = √(a²+b²)**
- **z z̄ = |z|² = a²+b²**

To divide complex numbers, multiply numerator and denominator by the denominator's conjugate.

Example: (3 + 2i)/(1 − 5i) = [(3 + 2i)(1 + 5i)]/26 = **(−7 + 17i)/26**.

## 4. Roots of real polynomials

When the quadratic formula gives a negative discriminant, use **√(−k) = i√k**.

Example: r² + 4r + 13 = 0 gives r = (−4 ± √(−36))/2 = **−2 ± 3i**.

Real-coefficient polynomials have complex roots in conjugate pairs.

## 5. Euler's formula: the bridge into ODEs

**e^(iθ) = cos θ + i sin θ**.

Therefore:

**e^((α+iβ)t) = e^(αt)cos(βt) + i e^(αt)sin(βt)**.

For a real-coefficient homogeneous second-order ODE with characteristic roots **α ± iβ**, the two real solutions are

**e^(αt)cos(βt)** and **e^(αt)sin(βt)**,

and their combination is

**y(t) = e^(αt)[C₁ cos(βt) + C₂ sin(βt)]**.

The real part α determines growth/decay of the amplitude; |β| determines angular frequency.

## 6. Worked ODE example

Solve **y″ + 4y′ + 13y = 0**.

1. Characteristic equation: r² + 4r + 13 = 0.
2. Roots: r = −2 ± 3i.
3. Real general solution: **y = e^(−2t)[C₁ cos(3t) + C₂ sin(3t)]**.

For **y(0)=1** and **y′(0)=0**, we get C₁=1 and −2C₁+3C₂=0, so C₂=2/3.

Thus **y(t)=e^(−2t)[cos(3t)+(2/3)sin(3t)]**.

## 7. Quick self-test

1. Simplify i¹⁷.
2. Compute (2−3i)(4+i).
3. Find |−5+12i|.
4. Compute (1+i)/(2−i).
5. Solve r²+6r+25=0.
6. Write the real general solution for y″+6y′+25y=0.

### Answer key

1. i
2. 11−10i
3. 13
4. (1+3i)/5
5. −3±4i
6. e^(−3t)[C₁cos(4t)+C₂sin(4t)]

**Mastery condition:** You can do all six without viewing the key and justify the complex-root solution formula.

For tracking, use skill IDs **CN-01 through CN-15** in the [live AM 20 spreadsheet](https://docs.google.com/spreadsheets/d/1htZ0UlYkbGe2-3tFK22qC7-Cj028OZJjVbVNafLEa60/edit).
