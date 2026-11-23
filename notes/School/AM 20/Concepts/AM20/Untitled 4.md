---
parent: "[[AM20]]"
type: concept
status: draft
---
# Differential Equations Review Notes

  

> Formatted from the pasted source text. Math notation and answers are preserved as written.

  

## Table of Contents

  

1. [LAPLACE TRANSFORMS — FULL TABLE](#laplace-transforms-full-table)

2. [1                  1/s](#1-1s)

3. [IVP ALGORITHM](#ivp-algorithm)

4. [Q7-Q1  k=mw^2 RESONANCE](#q7-q1-kmw2-resonance)

5. [Q7-Q2  FORWARD: L{3t*cos4t - e^(2t)*sint}](#q7-q2-forward-l3tcos4t-e2tsint)

6. [Q7-Q3  INVERSE: L^-1{6/(s^2+9)+(2s-3)/((s-1)^2+4)}](#q7-q3-inverse-l-16s292s-3s-124)

7. [Q7-Q4  L^-1{(6+0.4s*e^(-3s))/(s^2+4)}](#q7-q4-l-1604se-3ss24)

8. [Q7-Q5  L^-1  PFD over (s^2+4)(s+1)(s+2)](#q7-q5-l-1-pfd-over-s24s1s2)

9. [Q7-Q6  y''+4y'+5y=3-3u(t-6); y0=0,y0'=2](#q7-q6-y4y5y3-3ut-6-y00y02)

10. [Q7-Q7  y''-4y'+3y=u(t-2)(t-2)^3; y0=2,y0'=0](#q7-q7-y-4y3yut-2t-23-y02y00)

11. [HW5-2  TRIPLE DELTA IMPULSE](#hw5-2-triple-delta-impulse)

12. [HW5-3b  CONVOLUTION  F=(s+2)/[(s+1)^2*(s^2+4s+5)]](#hw5-3b-convolution-fs2s12s24s5)

13. [HW6-1  LAPLACE IVP  y''+4y'+13y=6e^(-2t)sin3t+2cos3t](#hw6-1-laplace-ivp-y4y13y6e-2tsin3t2cos3t)

14. [Q10-Q6  L{t*f(t)}=-F'(s); convolution thm](#q10-q6-ltft-fs-convolution-thm)

15. [KEY FORMULA BANK](#key-formula-bank)

16. [M2B-Q2  SPRING UNDERDAMPED IVP](#m2b-q2-spring-underdamped-ivp)

17. [M2W-Q2  SPRING UNDERDAMPED](#m2w-q2-spring-underdamped)

18. [3RD ORDER ODE — CHAR POLY](#3rd-order-ode-char-poly)

19. [Q8-Q2  3RD ORDER UC](#q8-q2-3rd-order-uc)

20. [UC GUESS TABLE](#uc-guess-table)

21. [M2B-Q1  UC IVP  y''+5y'+4y=t*e^(-3t)](#m2b-q1-uc-ivp-y5y4yte-3t)

22. [VARIATION OF PARAMETERS — ALGORITHM](#variation-of-parameters-algorithm)

23. [ABEL'S FORMULA FOR W](#abels-formula-for-w)

24. [M2B-Q3  VoP+Abel  y''+(3/t)y'+4y=cos3t](#m2b-q3-vopabel-y3ty4ycos3t)

25. [M2W-Q3  VoP+Abel  y''+(4/t)y'+5y=sin2t](#m2w-q3-vopabel-y4ty5ysin2t)

26. [INTEGRATING FACTOR](#integrating-factor)

27. [M1B-Q1a  y'-4y=sin2x; y(0)=0](#m1b-q1a-y-4ysin2x-y00)

28. [M1B-Q1b  x*y'+3y=sqrt(x^3+8); y(1)=1](#m1b-q1b-xy3ysqrtx38-y11)

29. [EXISTENCE & UNIQUENESS](#existence-uniqueness)

30. [Q8-Q3/C1  A=[[1,2],[2,1]]](#q8-q3c1-a1221)

31. [Q8-Q4/C2  A=[[2,3],[-3,2]]](#q8-q4c2-a23-32)

32. [Q8-Q5/C3  A=[[1,3],[3,1]]](#q8-q5c3-a1331)

33. [Q8-Q6/C4  det([[3-u,2,1],[-1,1-u,2],[1,1,2-u]])](#q8-q6c4-det3-u21-11-u2112-u)

34. [Q8-Q7/C6  UPPER-TRIANGULAR BLOCK](#q8-q7c6-upper-triangular-block)

35. [Q8-Q8/C7  A=[[4,2,1],[0,2,5],[0,5,2]]](#q8-q8c7-a421025052)

36. [Q9-Q1/C5  A=[[2,-2],[2,2]] COMPLEX EIGENVEC](#q9-q1c5-a2-222-complex-eigenvec)

37. [Q9-Q2  GEOMETRIC MULTIPLICITY CHECK](#q9-q2-geometric-multiplicity-check)

38. [3x3 COFACTOR SIGNS](#3x3-cofactor-signs)

39. [SYSTEMS x'=Ax — CASE 1: REAL DISTINCT](#systems-xax-case-1-real-distinct)

40. [CASE 2: COMPLEX EIGENVALUES  Q9-Q5](#case-2-complex-eigenvalues-q9-q5)

41. [CASE 4: CONST NONHOM  Q9-Q4](#case-4-const-nonhom-q9-q4)

42. [CASE 4: LINEAR-t NONHOM  Q9-Q6](#case-4-linear-t-nonhom-q9-q6)

43. [HW6-3  COMPLEX SYSTEM  B=[[2,-1],[1,2]]](#hw6-3-complex-system-b2-112)

44. [HW6-4  NONHOM SYSTEM  A=[[2,1],[6,-3]], b=[5;4]](#hw6-4-nonhom-system-a216-3-b54)

45. [HW7-1a  NONHOM LIN-t  A=[[1,2],[3,-4]]](#hw7-1a-nonhom-lin-t-a123-4)

46. [HW7-2  4-TANK EQUILIBRIUM](#hw7-2-4-tank-equilibrium)

47. [HW7-3  LOTKA-VOLTERRA](#hw7-3-lotka-volterra)

48. [Q10-Q8 = Q4-Q5  REPEATED ROOT IVP](#q10-q8-q4-q5-repeated-root-ivp)

49. [Q10-Q5 = Q3-Q4  SEPARABLE ODE](#q10-q5-q3-q4-separable-ode)

50. [ode45 CONFIRMED ANSWERS](#ode45-confirmed-answers)

51. [EQUILIBRIA ANALYSIS](#equilibria-analysis)

52. [M1B-Q3  y'=y(y-1)(y-5)](#m1b-q3-yyy-1y-5)

53. [M1W-Q3  y'=y(y-2)(y-5)](#m1w-q3-yyy-2y-5)

54. [M1B-Q2  500gal cap, V0=300gal](#m1b-q2-500gal-cap-v0300gal)

55. [M1W-Q2  400gal cap, V0=300gal](#m1w-q2-400gal-cap-v0300gal)

56. [BERNOULLI  y'+P*y=Q*y^n](#bernoulli-ypyqyn)

57. [Q2-Q3  y'+y=3x*y^2; y(0)=1/2](#q2-q3-yy3xy2-y012)

58. [NEWTON'S COOLING](#newtons-cooling)

59. [TECHNIQUE DECISION TREE](#technique-decision-tree)

60. [EXAM PRIORITY TABLE](#exam-priority-table)

61. [EXAM FORMAT PREDICTION](#exam-format-prediction)

62. [FORMULA REFERENCE](#formula-reference)

63. [SPRING UNITS: SI: k=mg/DL g=9.8 DL in meters](#spring-units-si-kmgdl-g98-dl-in-meters)

64. [UC MULTIPLICITY: s=0 if alpha NOT char root](#uc-multiplicity-s0-if-alpha-not-char-root)

65. [VoP/ABEL STANDARD FORM:](#vopabel-standard-form)

66. [2ND SHIFT: e^(-as)*F(s) => u(t-a)*f(t-a)](#2nd-shift-e-asfs-ut-aft-a)

67. [PFD QUADRATIC:](#pfd-quadratic)

68. [EIGENVEC DEFECT:](#eigenvec-defect)

69. [IC FULL SOLUTION:](#ic-full-solution)

70. [NONHOM SYSTEM IC:](#nonhom-system-ic)

71. [3x3 BLOCK EIGENVALUE:](#3x3-block-eigenvalue)

72. [MIXING VARIABLE VOLUME:](#mixing-variable-volume)

73. [PIECEWISE LAPLACE:](#piecewise-laplace)

74. [DELTA IMPULSE:](#delta-impulse)

75. [COMPLEX EIGENVECTOR:](#complex-eigenvector)

76. [EQUILIBRIUM DIRECTION:](#equilibrium-direction)

77. [REPEATED ROOT ODE:](#repeated-root-ode)

78. [UPPER TRIANGULAR det:](#upper-triangular-det)

79. [RESONANCE:](#resonance)

80. [VoP u1 SIGN:](#vop-u1-sign)

81. [ABEL STANDARD FORM:](#abel-standard-form)

82. [M1B MIDTERM 1 BLUE](#m1b-midterm-1-blue)

83. [M1W MIDTERM 1 WHITE](#m1w-midterm-1-white)

84. [M2B MIDTERM 2 BLUE](#m2b-midterm-2-blue)

85. [M2W MIDTERM 2 WHITE](#m2w-midterm-2-white)

86. [QUICK IDENTITIES](#quick-identities)

87. [PFD RULES](#pfd-rules)

88. [CHAR EQ DISCRIMINANT TABLE](#char-eq-discriminant-table)

89. [WRONSKIAN VERIFICATION](#wronskian-verification)

90. [HOW TO COMPLETE THE SQUARE](#how-to-complete-the-square)

91. [SYSTEMS FORMULA REFERENCE](#systems-formula-reference)

92. [SPRING-MASS SUMMARY TABLE](#spring-mass-summary-table)

93. [HIGHER ORDER — GENERAL RULES](#higher-order-general-rules)

94. [WRONSKIAN & LINEAR INDEPENDENCE](#wronskian-linear-independence)

95. [LOTKA-VOLTERRA PATTERN](#lotka-volterra-pattern)

96. [KEY NUMBERS TO KNOW](#key-numbers-to-know)

97. [EXAM CHECKLIST](#exam-checklist)

98. [ALL PROBLEM ANSWERS QUICK-REF](#all-problem-answers-quick-ref)

  

---

  

## LAPLACE TRANSFORMS — FULL TABLE

  

| f(t) | F(s) |

|---|---|

  

---

  

## 1                  1/s

  

```text

t^n                n!/s^(n+1)

e^(at)             1/(s-a)

sin(bt)            b/(s^2+b^2)

cos(bt)            s/(s^2+b^2)

e^(at)sin(bt)      b/((s-a)^2+b^2)

e^(at)cos(bt)      (s-a)/((s-a)^2+b^2)

t*sin(bt)          2bs/(s^2+b^2)^2

t*cos(bt)          (s^2-b^2)/(s^2+b^2)^2

t^n*e^(at)         n!/(s-a)^(n+1)

u(t-a)             e^(-as)/s

u(t-a)f(t-a)       e^(-as)*F(s)

delta(t-a)         e^(-as)

(f*g)(t)           F(s)*G(s)

```

  

---

  

## IVP ALGORITHM

  

```text

1. L{y''}=s^2*Y-s*y0-y0'   L{y'}=sY-y0

2. Collect Y(s), solve algebraically

3. PFD: A/(s-r) | A/(s-r)+B/(s-r)^2 | (As+B)/quad

4. Complete square for quad: s^2+bs+c=(s+b/2)^2+(c-b^2/4)

5. e^(-as) factor => 2nd shift: u(t-a)f(t-a)

6. (s-a) shift in denominator => 1st shift: multiply by e^(at)

```

  

---

  

## Q7-Q1  k=mw^2 RESONANCE

  

```text

m=6kg, DL=5cm, F=8cos(14t), dashpot 1N@7m/s

k = 6*9.8/0.05 = 1176 N/m

c = 1/7 N*s/m    w=14 rad/s

k - m*w^2 = 1176 - 6*196 = 1176-1176 = 0  RESONANCE

c^2*w^2 = (1/7)^2*196 = 4

R = F0/sqrt((k-mw^2)^2+c^2*w^2) = 8/sqrt(0+4) = 8/2

ANS: R = 4 m   [only damping limits amp at resonance]

```

  

---

  

## Q7-Q2  FORWARD: L{3t*cos4t - e^(2t)*sint}

  

```text

L{t*cosbt}=(s^2-b^2)/(s^2+b^2)^2  b=4:

  Term1 = 3(s^2-16)/(s^2+16)^2

1st shift: L{e^(at)f}=F(s-a); L{sint}=1/(s^2+1)

  Term2 = 1/((s-2)^2+1)

ANS: 3(s^2-16)/(s^2+16)^2 - 1/((s-2)^2+1)

```

  

---

  

## Q7-Q3  INVERSE: L^-1{6/(s^2+9)+(2s-3)/((s-1)^2+4)}

  

```text

6/(s^2+9) = 2*[3/(s^2+9)]  =>  2*sin(3t)

(2s-3)/((s-1)^2+4): write num=2(s-1)-1

= 2*(s-1)/((s-1)^2+4) - (1/2)*2/((s-1)^2+4)

1st shift (multiply by e^t, replace s-1->s):

ANS: 2sin(3t) + e^t*(2cos(2t) - (1/2)sin(2t))

```

  

---

  

## Q7-Q4  L^-1{(6+0.4s*e^(-3s))/(s^2+4)}

  

```text

Split: 6/(s^2+4) + 0.4s*e^(-3s)/(s^2+4)

6/(s^2+4) = 3*[2/(s^2+4)] => 3sin(2t)

0.4*[s/(s^2+4)] => 0.4cos(2t); e^(-3s)=>2nd shift a=3

ANS: 3sin(2t) + 0.4*u(t-3)*cos(2(t-3))

```

  

---

  

## Q7-Q5  L^-1  PFD over (s^2+4)(s+1)(s+2)

  

```text

Combine fractions; cover-up at s=-1,-2; match s^3

ANS: (2/5)sin2t+(3/10)cos2t-(11/2)e^(-2t)+(12/5)e^(-t)

```

  

---

  

## Q7-Q6  y''+4y'+5y=3-3u(t-6); y0=0,y0'=2

  

```text

L: (s^2+4s+5)Y - 2 = 3/s - 3e^(-6s)/s

ANS: Y = 2/(s^2+4s+5) + 3(1-e^(-6s))/[s(s^2+4s+5)]

Invert: s^2+4s+5=(s+2)^2+1

PFD 1/[s((s+2)^2+1)]: A=1/5, B=-1/5, C=-2/5

g(t)=(1/5)[1-e^(-2t)(cost+2sint)]

y=2e^(-2t)sint+3g(t)-3u(t-6)g(t-6)

```

  

---

  

## Q7-Q7  y''-4y'+3y=u(t-2)(t-2)^3; y0=2,y0'=0

  

```text

u(t-2)(t-2)^3: 2nd shift a=2, f(t)=t^3 => F=6/s^4

L{rhs}=e^(-2s)*6/s^4

L of ODE: (s^2-4s+3)Y-2s+8 = 6e^(-2s)/s^4

ANS: Y = 6e^(-2s)/[s^4(s^2-4s+3)] + (2s-8)/(s^2-4s+3) HW5-1  5-PIECE PIECEWISE FORCING

y''+4y'+13y=f(t); y(0)=y'(0)=0

f alternates 1,0,1,0,0 on [0,1),[1,2),[2,3),[3,4),[4,inf)

Cumulative steps: +1@0, -2@1, +2@2, -2@3, +1@4

f(t)=1-2u(t-1)+2u(t-2)-2u(t-3)+u(t-4)

F(s)=(1-2e^(-s)+2e^(-2s)-2e^(-3s)+e^(-4s))/s

Char: s^2+4s+13=(s+2)^2+9

H(s)=1/[s((s+2)^2+9)]  PFD: A=1/13,B=-1/13,C=-4/13... wait:

1=[A*((s+2)^2+9)+(Bs+C)*s]; A=1/13; B=-1/13; C=-4/13

g(t)=(1/13)[1-e^(-2t)(cos3t+(2/3)sin3t)]

ANS: y=g(t)-2g(t-1)u(1)+2g(t-2)u(2)-2g(t-3)u(3)+g(t-4)u(4)

  where u(k) means u(t-k)

```

  

---

  

## HW5-2  TRIPLE DELTA IMPULSE

  

```text

y''+4y'+13y=3d(t)+2d(t-1)+d(t-2); y0=y0'=0

L: (s^2+4s+13)Y = 3+2e^(-s)+e^(-2s)

Base: 1/((s+2)^2+9) => (1/3)e^(-2t)sin3t

ANS: y=e^(-2t)sin3t+(2/3)u(t-1)e^(-2(t-1))sin3(t-1)

       +(1/3)u(t-2)e^(-2(t-2))sin3(t-2)

```

  

---

  

## HW5-3b  CONVOLUTION  F=(s+2)/[(s+1)^2*(s^2+4s+5)]

  

```text

s^2+4s+5=(s+2)^2+1

WAY 1: F=[1/(s+1)^2]*[(s+2)/(s^2+4s+5)]

  g1=t*e^(-t),  g2=e^(-2t)*cost

  y=INTEGRAL_0^t tau*e^(-tau)*e^(-2(t-tau))*cos(t-tau)dtau

WAY 2: F=[(s+2)/(s+1)^2]*[1/(s^2+4s+5)]

  h1=(1+t)e^(-t),  h2=e^(-2t)*sint

  y=INTEGRAL_0^t (1+tau)e^(-tau)*e^(-2(t-tau))*sin(t-tau)dtau

```

  

---

  

## HW6-1  LAPLACE IVP  y''+4y'+13y=6e^(-2t)sin3t+2cos3t

  

```text

y0=y0'=0. Char: s^2+4s+13=(s+2)^2+9

L: Y=6*[3/((s+2)^2+9)]/[(s+2)^2+9] + 2*[s/(s^2+9)]/[(s+2)^2+9]

Y = 18/[(s+2)^2+9]^2 + 2s/[(s^2+9)((s+2)^2+9)]

Second term: PFD (As+B)/(s^2+9)+(Cs+D)/((s+2)^2+9)

```

  

---

  

## Q10-Q6  L{t*f(t)}=-F'(s); convolution thm

  

```text

L{t^n*f} = (-1)^n * F^(n)(s)  [n-th deriv of transform]

Convolution: L{(f*g)(t)}=F(s)G(s)

L^-1{F(s)G(s)} = integral_0^t f(tau)g(t-tau)dtau

ANS for Q10-Q6: 23/5

```

  

---

  

## KEY FORMULA BANK

  

```text

SPRING: k=mg/DL | R=F0/sqrt[(k-mw^2)^2+c^2*w^2]

        c_crit=2*sqrt(mk) | resonance when k=m*w^2

SHIFTS: 1st: e^(at)f(t)<->F(s-a)

        2nd: u(t-a)f(t-a)<->e^(-as)*F(s)

t-TRIG: t*cosbt<->(s^2-b^2)/(s^2+b^2)^2

        t*sinbt<->2bs/(s^2+b^2)^2

SYSTEM: Real: SUM ci*e^(li*t)*vi

        Complex a+bi: e^(at)[c1(p*cosbt-q*sinbt)+c2(p*sinbt+q*cosbt)]

        Defect: c1*e^(lt)*v+c2*e^(lt)*(t*v+w) where (A-lI)w=v

NONHOM: const b: xp=-A^(-1)*b | lin-t: Aa=-f_t, Ab=a-f_const

VoP:    u1'=-y2*g/W  u2'=y1*g/W  yp=u1*y1+u2*y2

ABEL:   W=c0*e^(-INT p dt)  [standard form: lead coeff=1]

UC:     s=mult of alpha as char root; guess t^s*e^(at)*P_n*(A*cos+B*sin)

EQUIL:  f'(y*)<0 stable | f'(y*)>0 unstable | sign chart

IF:     mu=e^(INT P dx) | (mu*y)'=mu*Q | y=(1/mu)(INT mu*Q+C)

BERN:   v=y^(1-n) | v'+(1-n)Pv=(1-n)Q | solve for v

ABEL2:  W=y1y2'-y2y1' (direct) or Abel formula

MIX:    V(t)=V0+(rin-rout)t | p=rout/V(t) | mu=e^(INT p)

SPRING-MASS SYSTEM — FULL SETUP

1. k=mg/DL  (SI: g=9.8, DL in m)

   English: m=W/32 (slug), k=W/DL (lb/ft)

2. c = F_damp/velocity

3. ODE: m*y''+c*y'+k*y=F0*cos(wt)

4. Discriminant D=c^2-4mk:

   D>0: overdamped  | D=0: critically  | D<0: underdamped

5. r=(-c+-sqrt(D))/(2m)

6. R=F0/sqrt[(k-mw^2)^2+c^2*w^2]

7. c_crit=2*sqrt(mk)

```

  

---

  

## M2B-Q2  SPRING UNDERDAMPED IVP

  

```text

m=2kg, DL=196cm=1.96m, c=8

pulled 90cm down, v0=3m/s down (positive=down)

k=2*9.8/1.96=10  char: 2r^2+8r+10=0 => r^2+4r+5=0

r=(-4+-sqrt(16-20))/2 = -2+-i  underdamped

y=e^(-2t)(c1*cost+c2*sint)

y(0)=0.9=>c1=0.9; y'(0)=-2c1+c2=3=>c2=4.8

ANS: y=e^(-2t)(0.9cost+4.8sint)

c_crit=2*sqrt(2*10)=4*sqrt(5)~8.944

```

  

---

  

## M2W-Q2  SPRING UNDERDAMPED

  

```text

m=2kg, DL=98cm=0.98m, c=4

pulled 70cm, v0=2m/s down

k=2*9.8/0.98=20  2r^2+4r+20=0 => r^2+2r+10=0

r=-1+-3i  y=e^(-t)(c1*cos3t+c2*sin3t)

y(0)=0.7=>c1=0.7; y'(0)=-c1+3c2=2=>c2=0.9

ANS: y=e^(-t)(0.7cos3t+0.9sin3t)

c_crit=2*sqrt(2*20)=4*sqrt(10)~12.65

```

  

---

  

## 3RD ORDER ODE — CHAR POLY

  

```text

Rational root test: try +-1,+-2,+-3,...

Q8-Q1:  y'''-2y''-5y'+6y=0

r^3-2r^2-5r+6=0; r=1: 1-2-5+6=0 chk

(r-1)(r^2-r-6)=(r-1)(r-3)(r+2)=0

ANS: y=c1*e^t+c2*e^(3t)+c3*e^(-2t)

```

  

---

  

## Q8-Q2  3RD ORDER UC

  

```text

y'''+ 2y''-5y'-6y=6t^2

Char: r=-1: (-1)+2+5-6=0 chk

(r+1)(r^2+r-6)=(r+1)(r+3)(r-2)=0

yh=c1*e^(-t)+c2*e^(-3t)+c3*e^(2t)

r=0 not a root => s=0, guess yp=At^2+Bt+C

yp'=2At+B  yp''=2A  yp'''=0

Sub: 0+4A-10At-5B-6At^2-6Bt-6C=6t^2

t^2: -6A=6  => A=-1

t^1: -10A-6B=0 => 10=6B => B=5/3

t^0: 4A-5B-6C=0 => -4-25/3=6C => C=-37/18

ANS: y=yh - t^2+(5/3)t-37/18

```

  

---

  

## UC GUESS TABLE

  

```text

RHS poly P_n(t)          => t^s*(An*t^n+...+A0)

RHS e^(at)               => t^s*A*e^(at)

RHS cos(bt)/sin(bt)      => t^s*(A*cosbt+B*sinbt)

RHS e^(at)*cos/sin(bt)   => t^s*e^(at)*(A*cos+B*sin)

RHS P_n*e^(at)*cos/sin   => t^s*e^(at)*P_n*(Acos+Bsin)

  s=0 if alpha not a char root

  s=1 if alpha is a simple char root

  s=2 if alpha is a double char root

```

  

---

  

## M2B-Q1  UC IVP  y''+5y'+4y=t*e^(-3t)

  

```text

Char: (r+1)(r+4)=0  yh=c1*e^(-t)+c2*e^(-4t)

a=-3 not a root => s=0, guess yp=(At+B)e^(-3t)

yp'=(-3At+A-3B)e^(-3t)

yp''=(9At-6A+9B)e^(-3t)

Sub into ODE, e^(-3t) factors out:

(9A-15A+4A)t = -2At => coeff t: -2A=1 => A=-1/2

coeff 1: -6A+9B+5A-15B+4B=-A-2B=0 => B=1/4

ANS: yp=(-t/2+1/4)e^(-3t)

ICs y0=y0'=0: c1+c2=-1/4; -c1-4c2+3/4... solve:

c1=1/12, c2=-1/3  M2W-Q1  UC IVP  y''-4y'+3y=2x*e^(-x)

Char: (r-1)(r-3)=0  yh=c1*e^x+c2*e^(3x)

a=-1 not a root => s=0, guess yp=(Ax+B)e^(-x)

yp'=(A-Ax-B)e^(-x)

yp''=(-2A+Ax+B)e^(-x)

Sub: e^(-x)[(-2A+Ax+B)-4(A-Ax-B)+3(Ax+B)]=2x

x coeff: (A+4A+3A)=8A=2 => A=1/4

const: -6A+8B=0 => B=3/16

ANS: yp=(x/4+3/16)e^(-x)

ICs: c1=-1/4, c2=1/16

```

  

---

  

## VARIATION OF PARAMETERS — ALGORITHM

  

```text

CRITICAL: standard form y''+(p)y'+(q)y=g FIRST

W=y1*y2'-y2*y1'  [Wronskian]

u1'=-y2*g/W   u2'=y1*g/W

yp=u1*y1+u2*y2

(leave as integrals on midterm if not evaluable)

```

  

---

  

## ABEL'S FORMULA FOR W

  

```text

If p(t) known but y1,y2 not explicit:

W(t)=c0*e^(-INT p(t) dt)

Example p=3/t: W=c0*e^(-3*ln|t|)=c0*t^(-3)

Example p=4/t: W=c0*t^(-4)

Then use u1'=-y2*g/W, u2'=y1*g/W as usual

```

  

---

  

## M2B-Q3  VoP+Abel  y''+(3/t)y'+4y=cos3t

  

```text

p=3/t => W=c0*t^(-3)

u1'=-y2*cos3t*(t^3/c0)

u2'=y1*cos3t*(t^3/c0)

ANS: y=c1*y1+c2*y2-(t^3/c0)*y1*INT(y2*cos3t)+(t^3/c0)*y2*INT(y1*cos3t)

```

  

---

  

## M2W-Q3  VoP+Abel  y''+(4/t)y'+5y=sin2t

  

```text

p=4/t => W=c0*t^(-4)

ANS: y=c1*y1+c2*y2-(1/c0)*y1*INT(y2*t^4*sin2t)+(1/c0)*y2*INT(y1*t^4*sin2t)

```

  

---

  

## INTEGRATING FACTOR

  

```text

Standard: y'+P*y=Q  mu=e^(INT P dx)

(mu*y)'=mu*Q  =>  y=(1/mu)(INT mu*Q dx + C)

TRAP: divide by leading coeff FIRST

TRAP: mu=e^(3*lnx)=x^3, NOT 3x

```

  

---

  

## M1B-Q1a  y'-4y=sin2x; y(0)=0

  

```text

mu=e^(-4x)   (e^(-4x)*y)'=e^(-4x)*sin2x

INT e^(ax)*sinbx = e^(ax)*(a*sinbx-b*cosbx)/(a^2+b^2)

Here a=-4,b=2: INT = e^(-4x)*(-4sin2x-2cos2x)/20

Apply IC: C=1/10

ANS: y=-(1/5)sin2x-(1/10)cos2x+(1/10)e^(4x)

```

  

---

  

## M1B-Q1b  x*y'+3y=sqrt(x^3+8); y(1)=1

  

```text

Divide by x: y'+(3/x)y=(1/x)sqrt(x^3+8)

mu=e^(INT 3/x dx)=e^(3*lnx)=x^3

(x^3*y)'=x^2*sqrt(x^3+8)

Sub u=x^3+8, du=3x^2 dx:

INT x^2*sqrt(x^3+8)dx=(2/9)(x^3+8)^(3/2)+C

x^3*y=(2/9)(x^3+8)^(3/2)+C

IC y(1)=1: (2/9)*27+C=1 => 6+C=1 => C=-5

ANS: y=[2(x^3+8)^(3/2)-45]/(9x^3)

check x=1: (54-45)/9=1 YES

```

  

---

  

## EXISTENCE & UNIQUENESS

  

```text

1st-order y'=f(t,y): f,df/dy cts on R => unique on SOME ivl

1st-order linear: p,g cts on (a,b) => unique on ALL of (a,b)

2nd-order linear: P,Q,R cts, P!=0 => unique on ALL of (a,b)

Q4-Q1: sqrt(t^2+2)*y''+ cos(pi*t)*y'+2y=0

  leading never zero => unique on (-inf,inf)

Q2-Q5: y'=x*(y^2-4)^(2/3): df/dy fails at y=+-2 => not unique

EIGENVALUES — 2x2 FORMULA

det(A-lI)=0 => l^2-(trA)*l+detA=0

l=[(a+d)+-sqrt((a+d)^2-4(ad-bc))]/2

D=(a+d)^2-4(ad-bc):

  D>0 real distinct | D=0 repeated | D<0 complex

Eigenvector: (A-lI)v=0; set v1=1, solve for v2

VERIFY: A*v=l*v after computing

```

  

---

  

## Q8-Q3/C1  A=[[1,2],[2,1]]

  

```text

tr=2, det=1-4=-3 => l=(2+-4)/2 => l=3,-1

l=3: (A-3I)=[[-2,2],[2,-2]] => v1=v2 => v=[1;1]

l=-1: (A+I)=[[2,2],[2,2]] => v1=-v2 => v=[1;-1]

ANS: l=3 v=[1;1],  l=-1 v=[1;-1]

```

  

---

  

## Q8-Q4/C2  A=[[2,3],[-3,2]]

  

```text

tr=4, det=4+9=13 => D=16-52=-36

l=(4+-6i)/2 = 2+-3i

ANS: l=2+-3i  (alpha=2, beta=3)

```

  

---

  

## Q8-Q5/C3  A=[[1,3],[3,1]]

  

```text

tr=2, det=1-9=-8 => D=4+32=36

l=(2+-6)/2 => l=4,-2

l=4: v=[1;1]   l=-2: v=[1;-1]

```

  

---

  

## Q8-Q6/C4  det([[3-u,2,1],[-1,1-u,2],[1,1,2-u]])

  

```text

Cofactor expand Row 1:

(3-u)*[(1-u)(2-u)-2] - 2*[(-1)(2-u)-2] + 1*[(-1)-(1-u)]

M11=(1-u)(2-u)-2=u^2-3u+2-2=u^2-3u

M12=(-1)(2-u)-2=u-4

M13=(-1)-(1-u)=u-2

=(3-u)(u^2-3u)-2(u-4)+(u-2)

=3u^2-9u-u^3+3u^2-2u+8+u-2

ANS: -u^3+6u^2-10u+6

```

  

---

  

## Q8-Q7/C6  UPPER-TRIANGULAR BLOCK

  

```text

A=[[1,7,1],[0,3,5],[0,5,3]]

Top-left 1x1: l1=1 (rows 2,3 col1 both zero)

Bottom-right 2x2: B=[[3,5],[5,3]]

trB=6, detB=9-25=-16

l=(6+-sqrt(36+64))/2=(6+-10)/2

ANS: l=1, 8, -2

```

  

---

  

## Q8-Q8/C7  A=[[4,2,1],[0,2,5],[0,5,2]]

  

```text

l1=4 (rows 2,3 col1=0)

Block [[2,5],[5,2]]: tr=4, det=4-25=-21

l=(4+-sqrt(16+84))/2=(4+-10)/2

ANS: l=4, 7, -3

```

  

---

  

## Q9-Q1/C5  A=[[2,-2],[2,2]] COMPLEX EIGENVEC

  

```text

A-(2+2i)I=[[-2i,-2],[2,-2i]]

Row1: -2i*v1-2*v2=0 => v2=-i*v1; v1=1: v=[1;-i]

Split: v=p+i*q where p=[1;0], q=[0;-1]

Real solutions:

x1=e^(2t)*(p*cos2t-q*sin2t)=e^(2t)*[cos2t;sin2t]

x2=e^(2t)*(p*sin2t+q*cos2t)=e^(2t)*[sin2t;-cos2t]

ANS: x=e^(2t)*[c1*cos2t+c2*sin2t; c1*sin2t-c2*cos2t]

```

  

---

  

## Q9-Q2  GEOMETRIC MULTIPLICITY CHECK

  

```text

A=[[10,8,-8],[-7,-5,7],[2,2,0]], claimed l=2

A-2I=[[8,8,-8],[-7,-7,7],[2,2,-2]]

Row reduce: R1/8=[1,1,-1]; R2+7R1->0; R3-2R1->0

rank=1 => null space dim=3-1=2

ANS: alg mult=2, geom mult=2 (NOT defective)

```

  

---

  

## 3x3 COFACTOR SIGNS

  

```text

  [+  -  +]

  [-  +  -]

  [+  -  +]

det=a11*M11-a12*M12+a13*M13

SHORTCUT upper/lower triangular: det=product of diag  REPEATED DEFECTIVE EIGENVALUE — CASE 3

Scenario: l with alg mult=2, geom mult=1

=> only ONE eigenvector v exists

Find generalized eigenvector w: (A-lI)*w=v

Solution: x=c1*e^(lt)*v + c2*e^(lt)*(t*v+w)

IC: x(0)=c1*v+c2*w=x0 => solve [v|w][c1;c2]=x0

Example A=[[3,1],[0,3]]: l=3 double

  v=[1;0]; (A-3I)*w=v => [[0,1],[0,0]]*w=[1;0]

  w2=1 from row1; w1=0 free => w=[0;1]

  x=c1*e^(3t)*[1;0]+c2*e^(3t)*(t*[1;0]+[0;1])

  =e^(3t)*[c1+c2*t; c2]

```

  

---

  

## SYSTEMS x'=Ax — CASE 1: REAL DISTINCT

  

```text

Q9-Q3: x'=[[-2,1],[1,-2]]*x; x(0)=[1;2]

det(A-lI)=(l+2)^2-1=l^2+4l+3=(l+1)(l+3)=0

l=-1: (A+I)=[[-1,1],[1,-1]] => v1=v2 => v=[1;1]

l=-3: (A+3I)=[[1,1],[1,1]] => v1=-v2 => v=[1;-1]

x=c1*e^(-t)*[1;1]+c2*e^(-3t)*[1;-1]

IC: c1+c2=1 and c1-c2=2 => c1=3/2, c2=-1/2

ANS: x=(3/2)e^(-t)*[1;1]-(1/2)e^(-3t)*[1;-1]

```

  

---

  

## CASE 2: COMPLEX EIGENVALUES  Q9-Q5

  

```text

y1'=-y1+2y2, y2'=-2y1-y2; IC y1=1,y2=2

A=[[-1,2],[-2,-1]]  (l+1)^2+4=0 => l=-1+-2i

alpha=-1, beta=2

Eigvec l=-1+2i: [[-2i,2],[-2,-2i]]*v=0

Row1: -2i*v1+2*v2=0 => v2=i*v1 => v=[1;i]

p=[1;0], q=[0;1]

x=e^(-t)[c1*(p*cos2t-q*sin2t)+c2*(p*sin2t+q*cos2t)]

y1=e^(-t)(c1*cos2t+c2*sin2t)

y2=e^(-t)(-c1*sin2t+c2*cos2t)

IC: c1=1, c2=2

ANS: y1=e^(-t)(cos2t+2sin2t)

     y2=e^(-t)(2cos2t-sin2t)

```

  

---

  

## CASE 4: CONST NONHOM  Q9-Q4

  

```text

x'=[[1,1],[-2,4]]*x+[-1;3]

Particular: set x'=0 => A*xp=-b=[1;-3]

A*xp=[1;-3]: p1+p2=1 and -2p1+4p2=-3

p2=1-p1; -2p1+4-4p1=-3 => p1=7/6, p2=-1/6

Eigenvalues: l^2-5l+6=(l-2)(l-3)=0

l=2: v=[1;1]  l=3: v=[1;2]

ANS: x=c1*e^(2t)*[1;1]+c2*e^(3t)*[1;2]+[7/6;-1/6]

```

  

---

  

## CASE 4: LINEAR-t NONHOM  Q9-Q6

  

```text

x'=4x-y+2, y'=5x-2y+t  A=[[4,-1],[5,-2]]

f=[2;t]=[2;0]+[0;1]*t. Guess xp=a*t+b

Match t^1: xp'=a=A*(a*t+b)+f => Aa=[0;-1]

Wait: Aa=[0;-1] means 4a1-a2=0 and 5a1-2a2=-1

=> a2=4a1; 5a1-8a1=-1 => a1=1/3, a2=4/3

Match t^0: a=Ab+[2;0] => Ab=a-[2;0]=[1/3-2;4/3]

Ab=[-5/3;4/3]: 4b1-b2=-5/3, 5b1-2b2=4/3

b2=4b1+5/3; 5b1-8b1-10/3=4/3 => b1=-14/9

b2=4(-14/9)+5/3=-41/9

Eigenvals: l=3,l=-1; l=3: v=[1;1]; l=-1: v=[1;5]

ANS: x=c1*e^(3t)*[1;1]+c2*e^(-t)*[1;5]+[(1/3)t-14/9;(4/3)t-41/9]

  

HW6-2  SYSTEM IVP  x'=3x+2y, y'=x+2y

IC: x(0)=1, y(0)=-1

A=[[3,2],[1,2]]: l^2-5l+4=(l-1)(l-4)=0

l=1: (A-I)=[[2,2],[1,1]] => v1=-v2 => v=[1;-1]

  verify: A*[1;-1]=[1;-1]=1*[1;-1] YES

l=4: (A-4I)=[[-1,2],[1,-2]] => v1=2v2 => v=[2;1]

IC: c1*[1;-1]+c2*[2;1]=[1;-1]

c1+2c2=1 and -c1+c2=-1 => 3c2=0=>c2=0, c1=1

ANS: x=e^t,  y=-e^t

```

  

---

  

## HW6-3  COMPLEX SYSTEM  B=[[2,-1],[1,2]]

  

```text

IC: u(0)=1, v(0)=2

(2-l)^2+1=0 => l=2+-i; alpha=2, beta=1

l=2+i: [[-i,-1],[1,-i]]*v=0

Row1: -iv1-v2=0 => v2=-iv1; v=[1;-i]

p=[1;0], q=[0;-1]

x=e^(2t)[c1*(p*cost-q*sint)+c2*(p*sint+q*cost)]

u=e^(2t)(c1*cost+c2*sint)

v=e^(2t)(c1*sint-c2*cost)

IC t=0: u(0)=c1=1; v(0)=-c2=2 => c2=-2

ANS: u=e^(2t)(cost-2sint)

     v=e^(2t)(sint+2cost)

verify v(0)=0+2=2 YES

```

  

---

  

## HW6-4  NONHOM SYSTEM  A=[[2,1],[6,-3]], b=[5;4]

  

```text

IC: x(0)=y(0)=0

l^2+l-12=(l+4)(l-3)=0

l=-4: (A+4I)=[[6,1],[6,1]] => 6v1+v2=0 => v=[1;-6]

l=3: (A-3I)=[[-1,1],[6,-6]] => v1=v2 => v=[1;1]

A*xp=-b: 2p+q=-5, 6p-3q=-4

q=-5-2p; 6p+15+6p=-4 => 12p=-19 => p=-19/12

q=-5+19/6=-11/6

x=c1*e^(-4t)*[1;-6]+c2*e^(3t)*[1;1]+[-19/12;-11/6]

IC x(0)=0: c1+c2=19/12; -6c1+c2=22/12

subtract: 7c1=-3/12 => c1=-1/28

c2=19/12+1/28=136/84=34/21

ANS: c1=-1/28,  c2=34/21

```

  

---

  

## HW7-1a  NONHOM LIN-t  A=[[1,2],[3,-4]]

  

```text

y1'=y1+2y2+2, y2'=3y1-4y2-t; IC=[0;0]

l^2+3l-10=(l+5)(l-2)=0

l=-5: v=[1;-3]   l=2: v=[2;1]

f=[2;-t]=[2;0]-[0;1]*t

Guess xp=a*t+b. xp'=a=A*(at+b)+[2;0]+[0;-1]*t

Match t^1: 0=Aa+[0;-1] => Aa=[0;1]

[[1,2],[3,-4]]*[a1;a2]=[0;1]

a1+2a2=0 and 3a1-4a2=1

a1=-2a2; -6a2-4a2=1 => a2=-0.1, a1=0.2

Match t^0: a=Ab+[2;0] => Ab=[0.2-2;-0.1]=[-1.8;-0.1]

b1+2b2=-1.8, 3b1-4b2=-0.1

b2=(-1.8-b1)/2; 3b1-4*(-1.8-b1)/2=-0.1

3b1+2*(1.8+b1)=-0.1 => 5b1=-3.7 => b1=-0.74

b2=(-1.8+0.74)/2=-0.53

ANS: xp=[0.2t-0.74; -0.1t-0.53]

IC: c1*[1;-3]+c2*[2;1]=[0.74;0.53]

c1+2c2=0.74; -3c1+c2=0.53

7c2=0.74+3*0.53=2.33 => c2~0.333

EXACT: c1~-0.046, c2~0.393  HW7-1b  COMPLEX SYSTEM IVP  A=[[2,-1],[1,2]]

IC: y1(0)=0, y2(0)=1

(2-l)^2+1=0 => l=2+-i; alpha=2, beta=1

l=2+i: [[-i,-1],[1,-i]]*v=0

v2=-i*v1; v=[1;-i]; p=[1;0], q=[0;-1]

y1=e^(2t)(c1*cost+c2*sint)

y2=e^(2t)(c1*sint-c2*cost)

IC: y1(0)=c1=0; y2(0)=-c2=1 => c2=-1

ANS: y1=-e^(2t)*sint,  y2=e^(2t)*cost

```

  

---

  

## HW7-2  4-TANK EQUILIBRIUM

  

```text

Q'=M*Q+p  (4x4 system, all neg eigenvalues)

As t->inf: e^(Mt)->0 if all eig(M)<0

Equilibrium = xp: M*Qeq=-p => Qeq=-M^(-1)*p

ANS: Q(inf)~[3203;4822;2392;1843] oz

PATTERN: any lin sys with all neg eig => equilib=-A^(-1)*b

```

  

---

  

## HW7-3  LOTKA-VOLTERRA

  

```text

dx/dt=0.4x-0.2xy, dy/dt=0.1xy-0.3y

Set=0: x(0.4-0.2y)=0 and y(0.1x-0.3)=0

=> (x,y)=(0,0) and (x,y)=(3,2)

Jacobian: J=[[0.4-0.2y, -0.2x],[0.1y, 0.1x-0.3]]

J(0,0)=[[0.4,0],[0,-0.3]]: l=0.4,-0.3 => SADDLE

J(3,2)=[[0,-0.6],[0.2,0]]: tr=0,det=0.12>0

l^2+0.12=0 => l=+-i*sqrt(0.12) => CENTER

ANS: (0,0) saddle | (3,2) center (closed orbits)

ode45: all 4 ICs give closed ovals around (3,2)

```

  

---

  

## Q10-Q8 = Q4-Q5  REPEATED ROOT IVP

  

```text

4y''-4y'+y=0; y(0)=-1, y'(0)=2

4r^2-4r+1=(2r-1)^2=0 => r=1/2 double

y=(c1+c2*t)*e^(t/2)

y(0)=c1=-1

y'=(c2+(c1+c2*t)/2)*e^(t/2); y'(0)=c2+c1/2=2

c2=2-(-1)/2=2+1/2=5/2

ANS: y=(-1+(5/2)t)*e^(t/2)

y(1)=(3/2)*e^(1/2)~2.473  ode45 confirms

```

  

---

  

## Q10-Q5 = Q3-Q4  SEPARABLE ODE

  

```text

y'=cos^2(y)*cos^2(x); y(pi)=pi/4

Separate: sec^2(y)dy=cos^2(x)dx

tan(y)=(x+sin(x)cos(x))/2+C=(x/2)+(sin2x)/4+C

IC x=pi, y=pi/4: tan(pi/4)=1=pi/2+0+C => C=1-pi/2

y(2pi): tan(y)=pi+0+(1-pi/2)=1+pi/2

ANS: y(2pi)=arctan(1+pi/2)~1.2

```

  

---

  

## ode45 CONFIRMED ANSWERS

  

```text

Q2-Q1: y'=-ty+3t, y(0)=2 => y(1)~2.3935

Q3-Q4=Q10-Q5: y'=cos^2y*cos^2x,y(pi)=pi/4 => y(2pi)=1.2

Q3-Q5: y'+y/(t^2+y^2+1)=1,y(0)=1 => y(2)=2.281

Q4-Q4: 3y''+y'-2y=0,y(0)=0,y'(0)=2 => y(2)=4.390

Q4-Q5=Q10-Q8: 4y''-4y'+y=0,y(0)=-1,y'(0)=2 => y(1)=2.473

Q10-Q6: Laplace conceptual => 23/5

MATLAB SYNTAX:

  [t,y]=ode45(@(t,y)f(t,y),[t0,T],y0);

  val=y(end);

  2nd order: x=[y;y']; f=@(t,x)[x(2);rhs];

```

  

---

  

## EQUILIBRIA ANALYSIS

  

```text

1. Solve f(y)=0; factor to get all y*

2. Test sign of f between each pair

3. -=>+ unstable | +=>- stable | same semi-stable

4. y(0)=y0: follow sign arrow to find limit

```

  

---

  

## M1B-Q3  y'=y(y-1)(y-5)

  

```text

y*=0,1,5

f(-0.5)=(-)(-)(-)<0 down

f(0.5)=(+)(-)(-)>0 up   => y=0 unstable

f(3)=(+)(+)(-)<0 down   => y=1 stable

f(6)=(+)(+)(+)>0 up     => y=5 unstable

y(0)=4: f(4)=4(3)(-1)<0 => heads to y=1

ANS: lim y(t)=1 as t->inf

```

  

---

  

## M1W-Q3  y'=y(y-2)(y-5)

  

```text

y*=0,2,5

f(1)>0 up | f(3)<0 down | f(6)>0 up

y=0 unstable | y=2 stable | y=5 unstable

y(0)=3: f(3)<0 => heads to y=2

ANS: lim y(t)=2

MIXING TANK — VARIABLE VOLUME

V(t)=V0+(rin-rout)*t

overflow time: t*=(Vmax-V0)/(rin-rout)

Q'=Cin*rin - (Q/V(t))*rout

=> Q' + (rout/V(t))*Q = Cin*rin

mu = e^(INT rout/V(t) dt)

```

  

---

  

## M1B-Q2  500gal cap, V0=300gal

  

```text

rin=9gal/min @ 8oz/gal, rout=4gal/min

V(t)=300+5t; overflow: (500-300)/5=40 min

Q'=72-4Q/(300+5t)

p=4/(300+5t)=4/(5(60+t))=(4/5)/(60+t)

mu=e^((4/5)*ln(60+t))=(60+t)^(4/5)

[(60+t)^(4/5)*Q]'=72*(60+t)^(4/5)

(60+t)^(4/5)*Q=72*(5/9)*(60+t)^(9/5)+C

                =40*(60+t)^(9/5)+C

Q=40*(60+t)+C*(60+t)^(-4/5)

IC Q(0)=0: 0=40*60+C*60^(-4/5)

C=-2400*60^(4/5)

Q(40)=40*100+C*100^(-4/5)

60^(4/5)~27.60, 100^(-4/5)=1/100^(4/5)~1/39.81

Q(40)=4000-2400*27.60/39.81~4000-1663~2337

ANS: C=Q(40)/500~4.67 oz/gal

```

  

---

  

## M1W-Q2  400gal cap, V0=300gal

  

```text

rin=8gal/min @ 7oz/gal, rout=4gal/min

V(t)=300+4t; overflow: (400-300)/4=25 min

Q'=56-Q/(75+t)

p=1/(75+t) => mu=75+t

[(75+t)*Q]'=56*(75+t)

(75+t)*Q=28*(75+t)^2+C

Q=28*(75+t)+C/(75+t)

IC Q(0)=0: 28*75+C/75=0 => C=-28*75^2=-157500

Q(25)=28*100-157500/100=2800-1575=1225

ANS: C(25)=1225/400=3.0625 oz/gal

```

  

---

  

## BERNOULLI  y'+P*y=Q*y^n

  

```text

Divide by y^n: y^(-n)*y'+(P)y^(1-n)=Q

Let v=y^(1-n): v'=(1-n)*y^(-n)*y'

=> v'+(1-n)*P*v=(1-n)*Q  [linear in v]

y=v^(1/(1-n))

```

  

---

  

## Q2-Q3  y'+y=3x*y^2; y(0)=1/2

  

```text

n=2, v=y^(-1), v'=-y^(-2)*y'

Divide by y^2: y^(-2)*y'+y^(-1)=3x

-v'+v=3x... wait: v'=-y^(-2)*y' so y^(-2)*y'=-v'

-v'+v=3x => v'-v=-3x

mu=e^(-x); (e^(-x)*v)'=-3x*e^(-x)

INT -3x*e^(-x)dx = 3e^(-x)*(x+1)+C

v*e^(-x)=3e^(-x)*(x+1)+C => v=3(x+1)+C*e^x

IC v(0)=1/y(0)=2: 2=3+C => C=-1

v=3x+3-e^x => y=1/(3x+3-e^x)

ANS: y=1/(3x+3-e^x)

```

  

---

  

## NEWTON'S COOLING

  

```text

T'=-k(T-Ta) => T=Ta+(T0-Ta)*e^(-kt)

Q2-Q4: T(0)=200, Ta=10, T(1)=170

170=10+190*e^(-k) => e^(-k)=160/190=16/19

k=ln(19/16)

T(10)=10+190*(16/19)^10

(16/19)^10~0.178; 190*0.178~33.8

ANS: T(10)~44 deg C COMPANION MATRIX  T16

2nd order y''+b*y'+c*y=f(t):

let x1=y, x2=y'

x'=[[0,1],[-c,-b]]*x+[0;f(t)]

3rd order y'''+ a*y''+b*y'+c*y=0:

A=[[0,1,0],[0,0,1],[-c,-b,-a]]

eigenvalues of A = roots of char poly

```

  

---

  

## TECHNIQUE DECISION TREE

  

```text

y'=f(y) autonomous       => Equilibria

y'+Py=Q                  => Integrating Factor

y'+Py=Q*y^n Bernoulli    => v=y^(1-n)

Newton cooling/radioactive => T=Ta+(T0-Ta)e^(-kt)

ay''+by'+cy=0            => char eq ar^2+br+c=0

  RHS poly/exp/trig        => UC (check s=mult)

  general g or var coeff   => VoP (standard form!)

  var coeff W unknown      => Abel's formula

spring-mass physical       => k=mg/DL; classify

mixing tank                => Q'=in-out; V(t)

3rd/4th order              => rational root theorem

piecewise / delta forcing  => Laplace

system x'=Ax              => eigenvalues

  +const forcing           => xp=-A^(-1)*b

  +linear t                => guess at+b

ODE to system              => companion matrix

nonlinear equilibria       => Jacobian, classify

```

  

---

  

## EXAM PRIORITY TABLE

  

```text

T1 MUST: Eigenvalues 2x2/3x3 (15pts)

T1 MUST: Systems of ODEs (12pts)

T1 MUST: Spring-Mass (12pts)

T1 MUST: Laplace+Unit Step (9pts)

T1 MUST: Equilibria (8pts)

T1 MUST: Mixing Tank (8pts)

T1 MUST: UC (7pts)

T2 HIGH: Nonhom Systems (6pts)

T2 HIGH: Inv Laplace PFD (6pts)

T2 HIGH: Complex Eigenvalues (6pts)

T2 HIGH: 3rd-Order ODE (4pts)

T2 HIGH: Delta/Convolution (4pts)

T2 HIGH: VoP (5pts)

T3 BG:   Abel's Formula (2pts)

T3 BG:   1st-Order IF (4pts)

T3 BG:   ode45 numerical (8pts)

```

  

---

  

## EXAM FORMAT PREDICTION

  

```text

P1 ~6pts: Systems IVP (real/complex/nonhom)

P2 ~6pts: Laplace IVP (piecewise/delta)

P3 ~4pts: Spring-Mass or UC/VoP full IVP

P4 ~4pts: Eigenvalue 3x3 or 3rd-order

Bonus: equilibria, mixing tank, ode45

TIME: eigenvals/systems first; Laplace second

SHOW: Av=lv check; root sub check; sign chart

```

  

---

  

## FORMULA REFERENCE

  

```text

k=mg/DL | R=F0/sqrt[(k-mw^2)^2+c^2w^2]

c_crit=2*sqrt(mk) | resonance: k=mw^2

L{y''}=s^2*Y-s*y0-y0' | L{y'}=sY-y0

L{d(t-a)}=e^(-as) | L{u(t-a)*f(t-a)}=e^(-as)*F(s)

L{e^(at)*f(t)}=F(s-a)  [1st shift]

L{t*cosbt}=(s^2-b^2)/(s^2+b^2)^2

L{t*sinbt}=2bs/(s^2+b^2)^2

W=c0*e^(-INT p dt)  [Abel, standard form]

u1'=-y2g/W  u2'=y1g/W  yp=u1y1+u2y2

V(t)=V0+(rin-rout)t | mu=e^(INT rout/V dt)

T=Ta+(T0-Ta)*e^(-kt)  [Newton cooling]

Complex l=a+bi: e^(at)[c1(pcos-qsin)+c2(psin+qcos)]

Defect: c1*e^(lt)*v+c2*e^(lt)*(tv+w)

J(x*,y*)=[[df/dx,df/dy],[dg/dx,dg/dy]] at equil

TRAP LIST — MEMORIZE ALL

```

  

---

  

## SPRING UNITS: SI: k=mg/DL g=9.8 DL in meters

  

```text

  English: m=W(lb)/32 k=W(lb)/DL(ft)

```

  

---

  

## UC MULTIPLICITY: s=0 if alpha NOT char root

  

```text

  s=1 if simple char root

  s=2 if double char root

  CHECK EVERY PROBLEM before guessing

```

  

---

  

## VoP/ABEL STANDARD FORM:

  

```text

  DIVIDE by leading coeff FIRST

  t*y''+p*y'=g => y''+(p/t)y'=g/t

  p(t) must come from standard form

```

  

---

  

## 2ND SHIFT: e^(-as)*F(s) => u(t-a)*f(t-a)

  

```text

  MUST replace t with (t-a) in f, not just multiply by u

  Example: e^(-3s)/(s^2+4) => u(t-3)*sin(2(t-3))/2

```

  

---

  

## PFD QUADRATIC:

  

```text

  (As+B)/(s^2+bs+c): complete square

  Write as A*(s+b/2)/q^2 + (B-Ab/2)/q^2

  where q^2=(s+b/2)^2+(c-b^2/4)

```

  

---

  

## EIGENVEC DEFECT:

  

```text

  (A-lI)*w=v is the GENERALIZED eigenvector eq

  w is NOT another eigenvector; it satisfies Aw=lw+v

```

  

---

  

## IC FULL SOLUTION:

  

```text

  ICs apply to y=yh+yp (full soln)

  y'(0) must use derivative of yh+yp

```

  

---

  

## NONHOM SYSTEM IC:

  

```text

  x(0)=xh(0)+xp => c1v1+c2v2=x0-xp

  SUBTRACT particular first, then solve for c1,c2

```

  

---

  

## 3x3 BLOCK EIGENVALUE:

  

```text

  Can only read eigenvalue from diagonal IF

  all entries in that row/col (off block) are zero

  Verify before assuming block structure

```

  

---

  

## MIXING VARIABLE VOLUME:

  

```text

  p=rout/V(t) NOT rout/V0

  V(t) changes over time

```

  

---

  

## PIECEWISE LAPLACE:

  

```text

  Track CUMULATIVE jumps at each t=a

  Sum of all coefficients = final steady value

  Verify: what is f(inf)?

```

  

---

  

## DELTA IMPULSE:

  

```text

  L{f(t)*d(t-a)}=f(a)*e^(-as)

  Standard: L{d(t-a)}=e^(-as)

  Adds e^(-as)/[char poly] to Y(s) for each impulse

```

  

---

  

## COMPLEX EIGENVECTOR:

  

```text

  One complex eigenvector (for l=a+bi)

  Gives TWO real solutions (real/imag parts)

  Do NOT try to find eigenvector for l=a-bi separately

```

  

---

  

## EQUILIBRIUM DIRECTION:

  

```text

  y0 between two equilibria

  Evaluate f(y0): sign tells direction arrow

  Limit = stable equilibrium in that direction

```

  

---

  

## REPEATED ROOT ODE:

  

```text

  y=(c1+c2*t)*e^(rt), NOT c1*e^rt+c2*te^rt

  (same thing, but write as one expression)

```

  

---

  

## UPPER TRIANGULAR det:

  

```text

  det=product of diag ONLY for triangular matrices

  Otherwise MUST cofactor expand

```

  

---

  

## RESONANCE:

  

```text

  At k=mw^2: R=F0/(c*w) denominator=c*w NOT zero

  Amplitude still finite if c>0

```

  

---

  

## VoP u1 SIGN:

  

```text

  u1'=-y2*g/W  (MINUS y2)

  u2'=+y1*g/W  (PLUS y1)

  Both divided by W

```

  

---

  

## ABEL STANDARD FORM:

  

```text

  p comes from y''+(p)y'+(q)y=g

  Example: t^2*y''+3t*y'+y=f

  => y''+(3/t)y'+(1/t^2)y=f/t^2

  => p=3/t => W=c0*t^(-3) MIDTERM PROBLEMS — COMPLETE REFERENCE

```

  

---

  

## M1B MIDTERM 1 BLUE

  

```text

Q1a: y'-4y=sin2x, y(0)=0

  ANS: y=-(1/5)sin2x-(1/10)cos2x+(1/10)e^(4x)

Q1b: xy'+3y=sqrt(x^3+8), y(1)=1

  ANS: y=[2(x^3+8)^(3/2)-45]/(9x^3)

Q2: 500gal, V0=300, in:9@8, out:4

  ANS: C(overflow)~4.67 oz/gal

Q3: y'=y(y-1)(y-5)

  y=0 unstable | y=1 stable | y=5 unstable

  y(0)=4 => lim=1

```

  

---

  

## M1W MIDTERM 1 WHITE

  

```text

Q1a: different coefficients (same structure as M1B)

Q2: 400gal, V0=300, in:8@7, out:4

  ANS: C(25min)=3.0625 oz/gal

Q3: y'=y(y-2)(y-5)

  y=0 unstable | y=2 stable | y=5 unstable

  y(0)=3 => lim=2

```

  

---

  

## M2B MIDTERM 2 BLUE

  

```text

Q1: y''+5y'+4y=t*e^(-3t), y0=y0'=0

  yp=(-t/2+1/4)e^(-3t); c1=1/12, c2=-1/3

Q2: spring m=2, DL=196cm, c=8

  ANS: y=e^(-2t)(0.9cost+4.8sint)

  c_crit=4sqrt(5)~8.94

Q3: y''+(3/t)y'+4y=cos3t  [VoP+Abel]

  W=c0*t^(-3); leave integrals unevaluated

```

  

---

  

## M2W MIDTERM 2 WHITE

  

```text

Q1: y''-4y'+3y=2x*e^(-x), y0=y0'=0

  yp=(x/4+3/16)e^(-x); c1=-1/4, c2=1/16

Q2: spring m=2, DL=98cm, c=4

  ANS: y=e^(-t)(0.7cos3t+0.9sin3t)

  c_crit=4sqrt(10)~12.65

Q3: y''+(4/t)y'+5y=sin2t  [VoP+Abel]

  W=c0*t^(-4); leave integrals unevaluated

```

  

---

  

## QUICK IDENTITIES

  

```text

INT e^(ax)*cosb*x dx = e^(ax)*(a*cosbx+b*sinbx)/(a^2+b^2)

INT e^(ax)*sinb*x dx = e^(ax)*(a*sinbx-b*cosbx)/(a^2+b^2)

INT x*e^(ax)dx = e^(ax)*(ax-1)/a^2

INT x*e^(-ax)dx = -e^(-ax)*(ax+1)/a^2

INT sqrt(u)du = (2/3)*u^(3/2)

INT 1/(a^2+u^2)du = (1/a)*arctan(u/a)

INT 1/sqrt(a^2-u^2)du = arcsin(u/a)

```

  

---

  

## PFD RULES

  

```text

Distinct linear: A/(s-a)+B/(s-b)+...

Repeated linear: A/(s-a)+B/(s-a)^2+...

Irreducible quad: (As+B)/(s^2+bs+c)

  complete square: s^2+bs+c=(s+b/2)^2+(c-b^2/4)

  write As+B = A*(s+b/2)+(B-Ab/2)

  => A*(s+b/2)/q^2 + (B-Ab/2)/q^2

  first term => e^(at)*cos(bt) after first shift

  second term => e^(at)*sin(bt) after first shift

Cover-up method for simple poles:

  A/(s-a)+... multiply both sides by (s-a), set s=a

```

  

---

  

## CHAR EQ DISCRIMINANT TABLE

  

```text

D>0 real: y=c1*e^(r1t)+c2*e^(r2t)

D=0 rep:  y=(c1+c2*t)*e^(rt)  r=-b/(2a)

D<0 cpx:  y=e^(at)(c1*cosbt+c2*sinbt)

  a=-b/(2m), b=sqrt|D|/(2m)

3rd order: use rational roots then factor

```

  

---

  

## WRONSKIAN VERIFICATION

  

```text

For y1=e^(r1t), y2=e^(r2t):

W=|e^(r1t)   e^(r2t)  |

  |r1e^(r1t) r2e^(r2t)|

=(r2-r1)*e^((r1+r2)t) != 0 if r1!=r2

For y1=e^(at)cosbt, y2=e^(at)sinbt:

W=b*e^(2at) != 0 if b!=0

COMPLETE LAPLACE INVERSE SHORTCUTS

1/s              => 1

1/s^n            => t^(n-1)/(n-1)!

1/(s-a)          => e^(at)

1/(s-a)^n        => t^(n-1)*e^(at)/(n-1)!

b/(s^2+b^2)      => sinbt

s/(s^2+b^2)      => cosbt

b/((s-a)^2+b^2)  => e^(at)*sinbt  [1st shift]

(s-a)/((s-a)^2+b^2)=>e^(at)*cosbt [1st shift]

2bs/(s^2+b^2)^2  => t*sinbt

(s^2-b^2)/(s^2+b^2)^2 => t*cosbt

e^(-as)/s        => u(t-a)

e^(-as)*F(s)     => u(t-a)*f(t-a)

e^(-as)          => delta(t-a)

F(s)*G(s)        => (f*g)(t)=INT_0^t f(tau)g(t-tau)dtau

```

  

---

  

## HOW TO COMPLETE THE SQUARE

  

```text

s^2+4s+5=(s+2)^2+1   [add/subtract (b/2)^2]

s^2+2s+2=(s+1)^2+1

s^2-4s+3=(s-2)^2-1   [may not need if factors]

s^2-4s+5=(s-2)^2+1

THEN: match to (s-a)^2+b^2 form

numerator (s+2)/(s+2)^2+1 = (s-(-2))/((s-(-2))^2+1)

=> cosine term with 1st shift a=-2

numerator const/((s+a)^2+b^2): rewrite as (const/b)*b/...

=> sine term with 1st shift

```

  

---

  

## SYSTEMS FORMULA REFERENCE

  

```text

General solution structure:

Case 1 (real distinct): SUM ci*e^(li*t)*vi

Case 2 (complex a+-bi):

  e^(at)[c1*(p*cosbt-q*sinbt)+c2*(p*sinbt+q*cosbt)]

  where v=p+iq is eigenvec for a+bi

Case 3 (repeated defective):

  c1*e^(lt)*v + c2*e^(lt)*(t*v+w)

  (A-lI)*w=v   find w by row reduction

Particular (const): Ax_p=-b

Particular (lin-t): Aa=-f_t, Ab=a-f_const

Equilibrium (neg eig): x_eq=-A^(-1)*b

```

  

---

  

## SPRING-MASS SUMMARY TABLE

  

```text

overdamped (D>0): y=c1*e^(r1t)+c2*e^(r2t) no osc

critical (D=0): y=(c1+c2t)*e^(rt) r=-c/(2m)

underdamped (D<0): y=e^(at)(c1coswt+c2sinwt)

  a=-c/(2m), w=sqrt(4mk-c^2)/(2m)

forced: y=yh+yp where yp=(1/D)*(A*coswt+B*sinwt)

  A=k-mw^2, B=cw, D=A^2+B^2=[(k-mw^2)^2+c^2w^2]

  amplitude R=F0/sqrt(D)

pure resonance (c=0,k=mw^2): amplitude UNBOUNDED

practical resonance: amplitude bounded by c

```

  

---

  

## HIGHER ORDER — GENERAL RULES

  

```text

n-th order linear => n linearly independent solutions

Char poly degree n => n roots (with multiplicity)

Real root r (simple): e^(rt)

Real root r (mult m): e^(rt), t*e^(rt),...,t^(m-1)*e^(rt)

Complex pair a+-bi (simple): e^(at)cosbت, e^(at)sinbt

Complex pair (mult m): t^k*e^(at)cos/sinbt, k=0..m-1

```

  

---

  

## WRONSKIAN & LINEAR INDEPENDENCE

  

```text

W(y1,..,yn)(t) = det of [yi^(j-1)(t)] matrix

W!=0 for some t0 => linearly independent

Abel: W(t)=W(t0)*e^(-INT_t0^t p(s)ds)

For solutions of y''+ py'+ qy=0:

  W(t)=c0*e^(-INT p dt)

W=0 for all t => linearly dependent

EXAM: if given y1, check W(y1,y2) to verify y2 indep  NONLINEAR SYSTEMS — EQUILIBRIA & JACOBIAN

dx/dt=f(x,y), dy/dt=g(x,y)

Step1: solve f=0 and g=0 simultaneously

Step2: Jacobian J=[[df/dx,df/dy],[dg/dx,dg/dy]]

Step3: evaluate J at each equilibrium (x*,y*)

Step4: eigenvalues of J classify the equilibrium:

  both neg real: stable node (spiral in)

  both pos real: unstable node (spiral out)

  one pos one neg: saddle point

  pure imaginary: center (closed orbits)

  complex a+-bi, a<0: stable spiral

  complex a+-bi, a>0: unstable spiral

  a=0 (pure imaginary): center (nonlinear!)

CAVEAT: for nonlinear, a=0 => center OR spiral

  (linearization inconclusive for nonlinear)

```

  

---

  

## LOTKA-VOLTERRA PATTERN

  

```text

x'=ax-bxy, y'=-cy+dxy

Equilibria: (0,0) and (c/d, a/b)

J(0,0): [[a,0],[0,-c]] => saddle if a,c>0

J(c/d,a/b): [[0,-bc/d],[da/b,0]]

tr=0, det=ac>0 => pure imaginary eigenvalues

=> center in linearization

=> actual behavior: center (closed orbits) for L-V

```

  

---

  

## KEY NUMBERS TO KNOW

  

```text

sqrt(2)~1.414 | sqrt(3)~1.732 | sqrt(5)~2.236

sqrt(10)~3.162 | e~2.718 | pi~3.14159

ln(2)~0.693 | ln(10)~2.303 | e^(0.5)~1.649

60^(4/5)~27.60 | 100^(4/5)~39.81

(16/19)^10~0.178  [Newton cooling Q2-Q4]

```

  

---

  

## EXAM CHECKLIST

  

```text

[ ] eigenvalues: compute det(A-lI)=0

[ ] eigenvectors: row-reduce (A-lI)v=0

[ ] verify: Av=l*v

[ ] complex: extract p=Re(v), q=Im(v)

[ ] IVP: apply ALL initial conditions

[ ] subtract xp before applying ICs to system

[ ] Laplace: check for e^(-as) factors (2nd shift)

[ ] spring: compute k=mg/DL first

[ ] UC: check multiplicity s before guessing

[ ] VoP: divide by leading coefficient first

[ ] equilibria: sign chart between every pair

[ ] mixing: V(t) changes! use p=rout/V(t)

```

  

---

  

## ALL PROBLEM ANSWERS QUICK-REF

  

```text

Q7-Q1: R=4m

Q7-Q2: 3(s^2-16)/(s^2+16)^2 - 1/((s-2)^2+1)

Q7-Q3: 2sin3t+e^t(2cos2t-(1/2)sin2t)

Q7-Q4: 3sin2t+0.4*u(t-3)*cos(2(t-3))

Q7-Q5: (2/5)sin2t+(3/10)cos2t-(11/2)e^(-2t)+(12/5)e^(-t)

Q7-Q6: Y=2/(s^2+4s+5)+3(1-e^(-6s))/[s(s^2+4s+5)]

Q7-Q7: Y=6e^(-2s)/[s^4(s^2-4s+3)]+(2s-8)/(s^2-4s+3)

Q8-Q1: y=c1*e^t+c2*e^(3t)+c3*e^(-2t)

Q8-Q2: y=yh-t^2+(5/3)t-37/18

Q8-Q3: l=3,-1

Q8-Q4: l=2+-3i

Q8-Q5: l=4,-2

Q8-Q6: -u^3+6u^2-10u+6

Q8-Q7: l=1,8,-2

Q8-Q8: l=4,7,-3

Q9-Q1: x=e^(2t)*[c1cos2t+c2sin2t; c1sin2t-c2cos2t]

Q9-Q2: alg=2 geom=2 (not defective)

Q9-Q3: (3/2)e^(-t)*[1;1]-(1/2)e^(-3t)*[1;-1]

Q9-Q4: xp=[7/6;-1/6]

Q9-Q5: y1=e^(-t)(cos2t+2sin2t)

Q9-Q6: x=c1*e^(3t)*[1;1]+c2*e^(-t)*[1;5]+xp

Q10-Q5=Q3-Q4: 1.2

Q10-Q8=Q4-Q5: 2.473

HW5-2: triple delta solution as above

HW6-2: x=e^t, y=-e^t

HW6-3: u=e^(2t)(cost-2sint), v=e^(2t)(sint+2cost)

HW6-4: c1=-1/28, c2=34/21

HW7-1a: xp=[0.2t-0.74;-0.1t-0.53]; c1~-0.046,c2~0.393

HW7-1b: y1=-e^(2t)sint, y2=e^(2t)cost

HW7-2: equil~[3203;4822;2392;1843] oz

HW7-3: (0,0)saddle (3,2)center

M2B-Q1: yp=(-t/2+1/4)e^(-3t)

M2B-Q2: y=e^(-2t)(0.9cost+4.8sint)

M2W-Q1: yp=(x/4+3/16)e^(-x)

M2W-Q2: y=e^(-t)(0.7cos3t+0.9sin3t)

```

  

---