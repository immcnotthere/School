---
type: reference
parent: "[[AM20]]"
domain: math
course: "AM 20"
status: draft
source: "AM20 Review1 Complex Numbers"
tags:
  - decks
---
# AM 20 Cards - AM20 Review1 Complex Numbers Complex Numbers

## Complex numbers
| Front | Back | Notes |
| --- | --- | --- |
| What is the standard (rectangular) form of a complex number $z$? | $z = a + bi$, with $a, b$ real and $i^2 = -1$. | p.1; definition |
| For $z = a+bi$, what is $\text{Re}(z)$? | $a$ | p.1; definition |
| For $z=a+bi$, what is $\text{Im}(z)$, exactly? | The real number $b$, not $bi$. | p.1; discrimination |

## Complex Number Arithmetic
| Front | Back | Notes |
| --- | --- | --- |
| How do you add two complex numbers, $(a+bi)+(c+di)$? | Add the real and imaginary parts separately: $(a+c) + (b+d)i$ | p.1; formula |
| How do you multiply $(a+bi)(c+di)$? | Expand like polynomials, then replace $i^2$ with $-1$: $(ac - bd) + (ad+bc)i$ | p.1; formula |

## Complex Conjugate and Modulus
| Front | Back | Notes |
| --- | --- | --- |
| What is the conjugate $\bar z$ of $z=a+bi$? | $\bar z = a - bi$, flip the sign of the imaginary part | p.1; definition |
| What is the modulus $\lvert z \rvert$ of $z=a+bi$? | $\lvert z \rvert = \sqrt{a^2+b^2}$ | p.1; formula |
| What does $z\bar z$ equal, in terms of $\lvert z \rvert$? | $z \bar z = a^2+b^2 = \lvert z \rvert^2$, always a nonnegative real number | p.1; formula |
| Why does it matter that $z\bar z$ is always a nonnegative real number? | It is what makes division by a complex number possible, since it clears the imaginary part from the denominator | p.1; concept |

## Division of Complex Numbers
| Front | Back | Notes |
| --- | --- | --- |
| How do you divide $z/w$ for complex $w$? | Multiply top and bottom by $\bar w$: $\dfrac{z}{w} = \dfrac{z\bar w}{w \bar w} = \dfrac{z \bar w}{\lvert w \rvert^2}$ | p.1; procedure |

## Square Root of a Negative Number
| Front | Back | Notes |
| --- | --- | --- |
| For $k>0$, what is $\sqrt{-k}$? | $\sqrt{-k} = i\sqrt{k}$ | p.1; formula |
| Where does the rule $\sqrt{-k}=i\sqrt{k}$ arise when using the quadratic formula? | When the discriminant is negative and you take its square root | p.1; procedure |

## Conjugate Root Pairs Theorem
| Front | Back | Notes |
| --- | --- | --- |
| For a polynomial with real coefficients, if $\alpha+i\beta$ is a root, what other number must also be a root? | $\alpha - i\beta$, its conjugate | p.1; theorem |
| Why do complex roots of a real coefficient polynomial always come in conjugate pairs? | Applying complex conjugation to the root equation shows the conjugate must satisfy it too, since all the coefficients are real | p.1; concept |

## Euler's Formula
| Front | Back | Notes |
| --- | --- | --- |
| State Euler's formula. | $e^{i\theta} = \cos\theta + i\sin\theta$ | p.1; formula |
| What is $e^{i\pi}$? | $-1$ | p.1; formula |
| What is $e^{-i\theta}$ in terms of cosine and sine? | $\cos\theta - i \sin\theta$, the conjugate of $e^{i\theta}$ | p.1; formula |

## Real and Imaginary Parts of a Complex Exponential
| Front | Back | Notes |
| --- | --- | --- |
| How do you split $e^{(\alpha+i\beta)t}$ into real and imaginary parts? | $e^{(\alpha+i\beta)t} = e^{\alpha t}(\cos\beta t + i \sin\beta t) = e^{\alpha t}\cos\beta t + i\, e^{\alpha t}\sin\beta t$ | p.1; formula |
| A complex root $\alpha \pm i\beta$ of a characteristic equation produces which two real solutions? | $e^{\alpha t}\cos\beta t$ and $e^{\alpha t}\sin\beta t$ | p.1; concept |

## Complex Number Arithmetic Practice
| Front | Back | Notes |
| --- | --- | --- |
| With $z=3+2i$, $w=1-5i$, what is $zw$? | $zw = 3-15i+2i-10i^2 = 13-13i$ | p.2; procedure |

## Complex Conjugate and Modulus Practice
| Front | Back | Notes |
| --- | --- | --- |
| For $z=-3+4i$, what are $\bar z$ and $\lvert z \rvert$? | $\bar z = -3-4i$, $\lvert z \rvert = \sqrt{9+16}=5$ | p.2; procedure |

## Solving a Quadratic With Complex Roots
| Front | Back | Notes |
| --- | --- | --- |
| Solve $r^2+4r+13=0$. | Discriminant is $16-52=-36$, so $\sqrt{-36}=6i$ and $r = \dfrac{-4\pm 6i}{2} = -2 \pm 3i$ | p.2; procedure |

## Real Solutions From a Complex Exponential
| Front | Back | Notes |
| --- | --- | --- |
| Write $e^{(-1+2i)t}$ in terms of real functions. | $e^{-t}\cos 2t + i\, e^{-t}\sin 2t$, so $\text{Re}=e^{-t}\cos 2t$ and $\text{Im}=e^{-t}\sin 2t$ | p.3; procedure |

## Expanding a Complex Number Times a Complex Exponential
| Front | Back | Notes |
| --- | --- | --- |
| Expand $(2+i)(\cos t + i\sin t)$ and give its real and imaginary parts. | $(2\cos t - \sin t) + i(2\sin t + \cos t)$, so $\text{Re}=2\cos t-\sin t$ and $\text{Im}=2\sin t+\cos t$ | p.3; procedure |

## Finding Roots of a Quartic With Complex Numbers
| Front | Back | Notes |
| --- | --- | --- |
| Find all four roots of $r^4+4=0$. | Factor as $(r^2-2r+2)(r^2+2r+2)$; the roots are $1\pm i$ and $-1\pm i$ | p.3; procedure |

# Node map
```json
[
 {
  "name": "Complex numbers",
  "type": "concept",
  "existing": false,
  "parent": "Complex Numbers",
  "prereqs": [],
  "uses": [],
  "page": 1,
  "summary": "A complex number is $z=a+bi$ with $a,b$ real and $i^2=-1$; $\\text{Re}(z)=a$ and $\\text{Im}(z)=b$ (the real number $b$, not $bi$)."
 },
 {
  "name": "Complex Number Arithmetic",
  "type": "concept",
  "existing": false,
  "parent": "Complex Numbers",
  "prereqs": [
   "Complex numbers"
  ],
  "uses": [],
  "page": 1,
  "summary": "Add and multiply complex numbers like polynomials, replacing $i^2$ by $-1$ wherever it appears."
 },
 {
  "name": "Complex Conjugate and Modulus",
  "type": "concept",
  "existing": false,
  "parent": "Complex Numbers",
  "prereqs": [
   "Complex numbers"
  ],
  "uses": [],
  "page": 1,
  "summary": "The conjugate $\\bar z = a-bi$ flips the imaginary part's sign; the modulus $|z|=\\sqrt{a^2+b^2}$ and $z\\bar z=|z|^2$ is always a nonnegative real number."
 },
 {
  "name": "Division of Complex Numbers",
  "type": "concept",
  "existing": false,
  "parent": "Complex Numbers",
  "prereqs": [
   "Complex Conjugate and Modulus"
  ],
  "uses": [],
  "page": 1,
  "summary": "Divide complex numbers by multiplying top and bottom by the conjugate of the denominator, turning the denominator into the real number $|w|^2$."
 },
 {
  "name": "Square Root of a Negative Number",
  "type": "concept",
  "existing": false,
  "parent": "Complex Numbers",
  "prereqs": [
   "Complex numbers"
  ],
  "uses": [],
  "page": 1,
  "summary": "For $k>0$, $\\sqrt{-k}=i\\sqrt{k}$; this is what the quadratic formula produces when the discriminant is negative."
 },
 {
  "name": "Conjugate Root Pairs Theorem",
  "type": "concept",
  "existing": false,
  "parent": "Complex Numbers",
  "prereqs": [
   "Complex Conjugate and Modulus",
   "Quadratic Equation"
  ],
  "uses": [],
  "page": 1,
  "summary": "A polynomial with real coefficients has complex roots only in conjugate pairs: if $\\alpha+i\\beta$ is a root, so is $\\alpha-i\\beta$."
 },
 {
  "name": "Euler's Formula",
  "type": "concept",
  "existing": false,
  "parent": "Complex Numbers",
  "prereqs": [
   "Complex numbers",
   "Trigonometric functions"
  ],
  "uses": [],
  "page": 1,
  "summary": "$e^{i\\theta}=\\cos\\theta+i\\sin\\theta$, with special case $e^{i\\pi}=-1$; $e^{-i\\theta}$ is the conjugate of $e^{i\\theta}$."
 },
 {
  "name": "Real and Imaginary Parts of a Complex Exponential",
  "type": "concept",
  "existing": false,
  "parent": "Complex Numbers",
  "prereqs": [
   "Euler's Formula"
  ],
  "uses": [],
  "page": 1,
  "summary": "Splitting $e^{(\\alpha+i\\beta)t}=e^{\\alpha t}\\cos\\beta t + i\\,e^{\\alpha t}\\sin\\beta t$ gives the two real solutions produced by a complex characteristic root $\\alpha\\pm i\\beta$."
 },
 {
  "name": "Complex Number Arithmetic Practice",
  "type": "problem",
  "existing": false,
  "parent": "Complex Numbers",
  "prereqs": [],
  "uses": [
   "Complex Number Arithmetic",
   "Division of Complex Numbers"
  ],
  "page": 2,
  "summary": "Computes $z+w$, $zw$, and $z/w$ for $z=3+2i$, $w=1-5i$."
 },
 {
  "name": "Complex Conjugate and Modulus Practice",
  "type": "problem",
  "existing": false,
  "parent": "Complex Numbers",
  "prereqs": [],
  "uses": [
   "Complex Conjugate and Modulus"
  ],
  "page": 2,
  "summary": "Finds $\\bar z$, $|z|$, and $z\\bar z$ for $z=-3+4i$."
 },
 {
  "name": "Solving a Quadratic With Complex Roots",
  "type": "problem",
  "existing": false,
  "parent": "Complex Numbers",
  "prereqs": [],
  "uses": [
   "Square Root of a Negative Number",
   "Conjugate Root Pairs Theorem"
  ],
  "page": 2,
  "summary": "Solves $r^2+4r+13=0$, getting the conjugate pair $r=-2\\pm 3i$."
 },
 {
  "name": "Real Solutions From a Complex Exponential",
  "type": "problem",
  "existing": false,
  "parent": "Complex Numbers",
  "prereqs": [],
  "uses": [
   "Real and Imaginary Parts of a Complex Exponential"
  ],
  "page": 3,
  "summary": "Writes $e^{(-1+2i)t}$ in terms of real functions and identifies its real and imaginary parts."
 },
 {
  "name": "Expanding a Complex Number Times a Complex Exponential",
  "type": "problem",
  "existing": false,
  "parent": "Complex Numbers",
  "prereqs": [],
  "uses": [
   "Complex Number Arithmetic",
   "Euler's Formula"
  ],
  "page": 3,
  "summary": "Expands $(2+i)(\\cos t+i\\sin t)$ into real and imaginary parts, the computation behind multiplying a complex eigenvector by $e^{i\\beta t}$."
 },
 {
  "name": "Finding Roots of a Quartic With Complex Numbers",
  "type": "problem",
  "existing": false,
  "parent": "Complex Numbers",
  "prereqs": [],
  "uses": [
   "Square Root of a Negative Number",
   "Conjugate Root Pairs Theorem",
   "Difference of Squares"
  ],
  "page": 3,
  "summary": "Finds all four roots of $r^4+4=0$ by factoring into two quadratics using a difference of squares."
 }
]
```

# Frankenstein problems

**Problem A.** Solve $r^2 - 2r + 5 = 0$. Then, for the root with positive imaginary part, write $e^{rt}$ in terms of real functions, and confirm the two roots form a conjugate pair.

*Concepts tested: Square Root of a Negative Number, Conjugate Root Pairs Theorem, Real and Imaginary Parts of a Complex Exponential.*

Solution. Discriminant: $b^2-4ac = 4 - 20 = -16$. By the square root rule, $\sqrt{-16}=4i$. Quadratic formula: $r = \dfrac{2\pm 4i}{2} = 1\pm 2i$. These two roots, $1+2i$ and $1-2i$, are conjugates of each other, as required for a real coefficient polynomial. Taking the root with positive imaginary part, $\alpha=1$, $\beta=2$, so $e^{(1+2i)t} = e^{t}(\cos 2t + i\sin 2t) = e^t\cos 2t + i\,e^t \sin 2t$. Thus $\text{Re}=e^t\cos 2t$ and $\text{Im}=e^t\sin 2t$.

**Problem B.** Let $z = 2-3i$ and $w=-1+i$. Compute $\bar z$, $\lvert z \rvert$, $zw$, and $z/w$, then verify that $\lvert z/w \rvert = \lvert z \rvert / \lvert w \rvert$.

*Concepts tested: Complex Number Arithmetic, Complex Conjugate and Modulus, Division of Complex Numbers.*

Solution. $\bar z = 2+3i$. $\lvert z \rvert = \sqrt{2^2+3^2} = \sqrt{13}$. Product: $zw = (2-3i)(-1+i) = -2+2i+3i-3i^2 = -2+5i+3 = 1+5i$. Quotient: multiply by $\bar w = -1-i$; $\lvert w \rvert^2 = 1+1=2$, and the numerator is $z\bar w = (2-3i)(-1-i) = -2-2i+3i+3i^2 = -2+i-3 = -5+i$, so $z/w = \dfrac{-5+i}{2} = -\dfrac{5}{2}+\dfrac{1}{2}i$. Check: $\lvert z/w \rvert = \sqrt{(25/4)+(1/4)} = \sqrt{26}/2$, and $\lvert z \rvert / \lvert w \rvert = \sqrt{13}/\sqrt{2} = \sqrt{13/2} = \sqrt{26}/2$. They match, confirming the modulus of a quotient is the quotient of moduli.
