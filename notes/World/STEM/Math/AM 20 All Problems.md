---
title: "AM 20 — Practice Problems (with text)"

tags: [MATH, AM20, differential-equations, practice]
type: study
parent: "[[AM20]]"
domain: math
status: draft
---
---

title: "AM 20 — Practice Problems (with text)"

tags: [MATH, AM20, differential-equations, practice]

---

  

# AM 20 Practice Problems

  

## Week 1

  

### Mon 3/30 — Introduction

  

*Reading: 1.1, 1.2*

  

#### Section 1.2

  

**1.2.1**

  

Find the order of the equation.

  

  - (a) $$\frac{d^2y}{dx^2} + 2\frac{dy}{dx}\frac{d^3y}{dx^3} + x = 0$$

  - (b) $y'' - 3y' + 2y = x^7$

  - (c) $y' - y^7 = 0$

  - (d) $y''y - (y')^2 = 2$

  

**1.2.4**

  

Solve the initial value problem.

  

  - (a) $y' = -xe^x$, $y(0) = 1$

  - (b) $y' = x\sin x^2$, $y\!\left(\sqrt{\frac{\pi}{2}}\right) = 1$

  - (c) $y' = \tan x$, $y(\pi/4) = 3$

  - (d) $y'' = x^4$, $y(2) = -1$, $y'(2) = -1$

  - (e) $y'' = xe^{2x}$, $y(0) = 7$, $y'(0) = 1$

  - (f) $y'' = -x\sin x$, $y(0) = 1$, $y'(0) = -3$

  - (g) $y''' = x^2 e^x$, $y(0) = 1$, $y'(0) = -2$, $y''(0) = 3$

  - (h) $y''' = 2 + \sin 2x$, $y(0) = 1$, $y'(0) = -6$, $y''(0) = 3$

  - (i) $y''' = 2x + 1$, $y(2) = 1$, $y'(2) = -4$, $y''(2) = 7$

  

**1.2.5**

  

Verify that the function is a solution of the initial value problem.

  

  - (a) $y = x\cos x$; $\quad y' = \cos x - y\tan x$, $y(\pi/4) = \dfrac{\pi}{4\sqrt{2}}$

  - (b) $y = \dfrac{1 + 2\ln x}{x^2} + \dfrac{1}{2}$; $\quad y' = \dfrac{x^2 - 2x^2 y + 2}{x^3}$, $y(1) = \dfrac{3}{2}$

  - (c) $y = \tan\!\left(\dfrac{x^2}{2}\right)$; $\quad y' = x(1 + y^2)$, $y(0) = 0$

  - (d) $y = \dfrac{2}{x - 2}$; $\quad y' = -y(y+1)$, $y(1) = -2$

  

**1.2.6**

  

Verify that the function is a solution of the initial value problem.

  

  - (a) $y = x^2(1 + \ln x)$; $\quad y'' = \dfrac{3xy' - 4y}{x^2}$, $y(e) = 2e^2$, $y'(e) = 5e$

  - (b) $y = \dfrac{x^2}{3} + x - 1$; $\quad y'' = \dfrac{x^2 - xy' + y + 1}{x^2}$, $y(1) = \dfrac{1}{3}$, $y'(1) = \dfrac{5}{3}$

  - (c) $y = (1 + x^2)^{-1/2}$; $\quad y'' = \dfrac{(x^2-1)y - x(x^2+1)y'}{(x^2+1)^2}$, $y(0) = 1$, $y'(0) = 0$

  - (d) $y = \dfrac{x^2}{1 - x}$; $\quad y'' = \dfrac{2(x+y)(xy'-y)}{x^3}$, $y(1/2) = 1/2$, $y'(1/2) = 3$

  

**1.2.7**

  

Suppose an object is launched from a point 320 feet above the earth with an initial velocity of 128 ft/sec upward, and the only force acting on it thereafter is gravity. Take $g = 32\ \text{ft/sec}^2$.

  

  - (a) Find the highest altitude attained by the object.

  - (b) Determine how long it takes for the object to fall to the ground.

  

**1.2.9**

  

Verify that

  

$$y = \begin{cases} e^x - 1, & x \ge 0 \\ 1 - e^{-x}, & x < 0 \end{cases}$$

  

is a solution of $y' = |y| + 1$ on $(-\infty, \infty)$. HINT: Use the definition of derivative at $x = 0$.

  

**1.2.10**

  

- (a) Verify that if $c$ is any real number then $y = c^2 + cx + 2c + 1$ satisfies $y' = \dfrac{-(x+2) + \sqrt{x^2 + 4x + 4y}}{2}$ on some open interval. Identify the open interval.

- (b) Verify that $y_1 = \dfrac{-x(x+4)}{4}$ also satisfies (B) on some open interval, and identify the open interval. (Note that $y_1$ can't be obtained by selecting a value of $c$ in (A).)

  

---

  

### Wed 4/1 — Direction Fields; First Order Linear ODEs I

  

*Reading: 1.3, 2.1*

  

#### Section 1.3

  

In Exercises 1–5 find the general solution.

  

**1.3.1**

  

$y' + ay = 0$ ($a$ = constant)

  

**1.3.3**

  

$xy' + (\ln x)y = 0$

  

**1.3.5**

  

$x^2 y' + y = 0$

  

**1.3.6**

  

$y' + \left(\dfrac{1+x}{x}\right)y = 0$, $y(1) = 1$

  

**1.3.9**

  

$y' - \left(\dfrac{2x}{1+x^2}\right)y = 0$, $y(0) = 2$

  

**1.3.10**

  

$y' + \dfrac{k}{y} = 0$, $y(1) = 3$ ($k$ = constant)

  

In Exercises 12–15 find the general solution. Also, plot a direction field and some integral curves on $\{-2 \le x \le 2,\ -2 \le y \le 2\}$.

  

**1.3.12**

  

$y' + 3y = 1$

  

**1.3.13**

  

$y' + \left(\dfrac{1}{x} - 1\right)y = -\dfrac{2}{x}$

  

**1.3.17**

  

$y' + \dfrac{4}{x-1}y = \dfrac{1}{(x-1)^5} + \dfrac{\sin x}{(x-1)^4}$

  

**1.3.22**

  

$(x-2)(x-1)y' - (4x-3)y = (x-2)^3$

  

**1.3.31**

  

$xy' + 2y = 8x^2$, $y(1) = 3$

  

**1.3.33**

  

$y' + 2xy = x$, $y(0) = 3$

  

In Exercises 38–42 solve the initial value problem and leave the answer in a form involving a definite integral.

  

**1.3.38**

  

$y' + 2xy = x^2$, $y(0) = 3$

  

**1.3.39**

  

$y' + \dfrac{1}{x}y = \dfrac{\sin x}{x^2}$, $y(1) = 2$

  

**1.3.43**

  

Experiments indicate that glucose is absorbed by the body at a rate proportional to the amount of glucose present in the bloodstream. Let $\lambda$ denote the (positive) constant of proportionality. Now suppose glucose is injected into a patient's bloodstream at a constant rate of $r$ units per unit of time. Let $G = G(t)$ be the number of units in the patient's bloodstream at time $t > 0$. Then

  

$$G' = -\lambda G + r,$$

  

where the first term on the right is due to the absorption of the glucose by the patient's body and the second term is due to the injection. Determine $G$ for $t > 0$, given that $G(0) = G_0$. Also, find $\lim_{t \to \infty} G(t)$.

  

**1.3.45**

  

Suppose $f$ is continuous on an open interval $(a, b)$ and $\alpha$ is a constant.

  

- (a) Derive a formula for the solution of the initial value problem $y' + \alpha y = f(x)$, $y(x_0) = y_0$, where $x_0$ is in $(a,b)$ and $y_0$ is an arbitrary real number.

- (b) Suppose $(a,b) = (a, \infty)$, $\alpha > 0$ and $\lim_{x \to \infty} f(x) = L$. Show that if $y$ is the solution of (A), then $\lim_{x \to \infty} y(x) = L/\alpha$.

  

**1.3.47**

  

Some nonlinear equations can be transformed into linear equations by changing the dependent variable. Show that if $g'(y)y' + p(x)g(y) = f(x)$, where $y$ is a function of $x$ and $g$ is a function of $y$, then the new dependent variable $z = g(y)$ satisfies the linear equation $z' + p(x)z = f(x)$.

  

---

### Fri 4/3 — First Order Linear ODEs II

  

*Reading: 2.1*

  

#### Section 2.1

  

In Exercises 1–5 find the general solution.

  

**2.1.3**

  

$xy' + (\ln x)y = 0$

  

**2.1.5**

  

$x^2 y' + y = 0$

  

In Exercises 6–11 solve the initial value problem.

  

**2.1.6**

  

$y' + \left(\dfrac{1+x}{x}\right)y = 0$, $y(1) = 1$

  

**2.1.9**

  

$y' - \dfrac{2x}{1+x^2}y = 0$, $y(0) = 2$

  

**2.1.10**

  

$y' + \dfrac{k}{x}y = 0$, $y(1) = 3$ ($k$ = constant)

  

In Exercises 12–15 find the general solution. Also, plot a direction field and some integral curves on $\{-2 \le x \le 2,\ -2 \le y \le 2\}$.

  

**2.1.13**

  

$y' + \left(\dfrac{1}{x} - 1\right)y = -\dfrac{2}{x}$

  

**2.1.17**

  

$y' + \dfrac{4}{x-1}y = \dfrac{1}{(x-1)^5} + \dfrac{\sin x}{(x-1)^4}$

  

**2.1.22**

  

$(x-2)(x-1)y' - (4x-3)y = (x-2)^3$

  

**2.1.31**

  

$xy' + 2y = 8x^2$, $y(1) = 3$

  

**2.1.33**

  

$y' + 2xy = x$, $y(0) = 3$

  

In Exercises 38–42 solve the IVP and leave the answer in a form involving a definite integral.

  

**2.1.39**

  

$y' + \dfrac{1}{x}y = \dfrac{\sin x}{x^2}$, $y(1) = 2$

  

**2.1.43**

  

Experiments indicate that glucose is absorbed by the body at a rate proportional to the amount of glucose present in the bloodstream. Let $\lambda$ denote the (positive) constant of proportionality. Now suppose glucose is injected into a patient's bloodstream at a constant rate of $r$ units per unit of time. Let $G = G(t)$ be the number of units in the patient's bloodstream at time $t > 0$. Then

  

$$G' = -\lambda G + r,$$

  

where the first term is due to absorption and the second is due to injection. Determine $G$ for $t > 0$, given that $G(0) = G_0$. Also, find $\lim_{t \to \infty} G(t)$.

  

**2.1.45**

  

Suppose $f$ is continuous on an open interval $(a, b)$ and $\alpha$ is a constant.

  

- (a) Derive a formula for the solution of the initial value problem $y' + \alpha y = f(x)$, $y(x_0) = y_0$, where $x_0 \in (a, b)$ and $y_0$ is an arbitrary real number.

- (b) Suppose $(a, b) = (a, \infty)$, $\alpha > 0$, and $\lim_{x \to \infty} f(x) = L$. Show that if $y$ is the solution of (A), then $\lim_{x \to \infty} y(x) = L/\alpha$.

  

**2.1.47**

  

Some nonlinear equations can be transformed into linear equations by changing the dependent variable. Show that if $g'(y)y' + p(x)g(y) = f(x)$, where $y$ is a function of $x$ and $g$ is a function of $y$, then the new dependent variable $z = g(y)$ satisfies the linear equation $z' + p(x)z = f(x)$.

  

---

  

---

  

## Week 2

  

### Mon 4/6 — Separable First Order Equations

  

*Reading: 2.2*

  

#### Section 2.2

  

In Exercises 1–6 find all solutions.

  

**2.2.1**

  

$y' = \dfrac{3x^2 + 2x + 1}{y - 2}$

  

**2.2.3**

  

$xy' + y^2 + y = 0$

  

**2.2.6**

  

$x^2 yy' = (y^2 - 1)^{3/2}$

  

**2.2.11**

  

$y' = \dfrac{x^2 + 3x + 2}{v - 2}$, $y(1) = 4$

  

**2.2.13**

  

$(3y^2 + 4y)y' + 2x + \cos x = 0$, $y(0) = 1$

  

**2.2.17**

  

$y'(x^2 + 2) + 4x(y^2 + 2y + 1) = 0$, $y(1) = -1$

  

**2.2.19**

  

$y' = \dfrac{2x}{1 + 2y}$, $y(2) = 0$

  

**2.2.25**

  

Solve $y'\sqrt{1 - x^2} + \sqrt{1 - y^2} = 0$ explicitly. HINT: Use the identity $\sin(A - B) = \sin A \cos B - \cos A \sin B$.

  

**2.2.27**

  

Solve the initial value problem $y' = ay - by^2$, $y(0) = y_0$. Discuss the behavior of the solution if **(a)** $y_0 \ge 0$; **(b)** $y_0 < 0$.

  

**2.2.28**

  

The population $P = P(t)$ of a species satisfies the logistic equation $P' = aP(1 - \alpha P)$ and $P(0) = P_0 > 0$. Find $P$ for $t > 0$, and find $\lim_{t \to \infty} P(t)$.

  

**2.2.29**

  

An epidemic spreads through a population at a rate proportional to the product of the number of people already infected and the number susceptible but not yet infected. If $S$ denotes the total susceptible population and $I = I(t)$ denotes the number infected at time $t$, then $I' = rI(S - I)$, where $r$ is a positive constant. Assuming that $I(0) = I_0$, find $I(t)$ for $t > 0$, and show that $\lim_{t \to \infty} I(t) = S$.

  

**2.2.31**

  

Consider the differential equation $y' = ay - by^2 - q$, where $a$, $b$ are positive constants and $q$ is an arbitrary constant. Suppose $y$ denotes a solution satisfying $y(0) = y_0$.

  

- (a) Choose $a$, $b$ positive and $q < a^2/4b$. By plotting direction fields and solutions on suitable rectangular grids, discover that there are numbers $y_1 < y_2$ such that if $y_0 > y_1$ then $\lim_{t\to\infty} y(t) = y_2$, and if $y_0 < y_1$ then $y(t) = -\infty$ for some finite $t$.

- (b) Choose $q = a^2/4b$. Discover that there's a number $y_1$ such that if $y_0 \ge y_1$ then $\lim_{t\to\infty} y(t) = y_1$, while if $y_0 < y_1$ then $y(t) = -\infty$ for some finite $t$.

- (c) Choose $q > a^2/4b$. Discover that no matter what $y_0$ is, $y(t) = -\infty$ for some finite $t$.

- (d) Verify your results analytically. Note that $q_0 = a^2/4b$ is a **bifurcation value** of $q$.

  

**2.2.33**

  

Suppose a disease spreads according to the model of Exercise 29, but there's a medication that cures the infected population at a constant rate of $q$ individuals per unit time, $q > 0$. Then $I' = rI(S - I) - q$. Assuming that $I(0) = I_0 > 0$, use the results of Exercise 31 to describe what happens as $t \to \infty$.

  

---

  

### Wed 4/8 — Existence and Uniqueness of Solutions

  

*Reading: 2.3*

  

#### Section 2.3

  

In Exercises 1–13 find all $(x_0, y_0)$ for which Theorem 2.3.1 implies that the initial value problem $y' = f(x, y)$, $y(x_0) = y_0$ has **(a)** a solution **(b)** a unique solution on some open interval containing $x_0$.

  

**2.3.1**

  

$y' = \dfrac{x^2 + y^2}{\sin x}$

  

**2.3.3**

  

$y' = \tan xy$

  

**2.3.7**

  

$y' = \ln(1 + x^2 + y^2)$

  

**2.3.14**

  

Apply Theorem 2.3.1 to the initial value problem $y' + p(x)y = q(x)$, $y(x_0) = y_0$ for a linear equation, and compare the conclusions that can be drawn from it to those that follow from Theorem 2.1.2.

  

**2.3.17**

  

Consider the initial value problem $y' = 3x(y - 1)^{1/3}$, $y(x_0) = y_0$.

  

- (a) For what points $(x_0, y_0)$ does Theorem 2.3.1 imply that the IVP has a solution?

- (b) For what points $(x_0, y_0)$ does Theorem 2.3.1 imply that the IVP has a unique solution on some open interval containing $x_0$?

  

**2.3.19**

  

From Theorem 2.3.1, the initial value problem $y' = 3x(y - 1)^{1/3}$, $y(0) = 9$ has a unique solution on an open interval containing $x_0 = 0$. Find the solution and determine the largest open interval on which it's unique.

  

---

  

### Fri 4/10 — Numerical Methods I: Euler's Method

  

*Reading: 3.1*

  

> [!tip] Try writing a MATLAB script that does the work on these problems for you.

  

#### Section 3.1

  

**3.1.1**

  

$y' = 2x^2 + 3y^2 - 2$, $y(2) = 1$; $h = 0.05$

  

**3.1.3**

  

$y' + 3y = x^2 - 3xy + y^2$, $y(0) = 2$; $h = 0.05$

  

**3.1.7**

  

Use Euler's method with step sizes $h = 0.1$, $h = 0.05$, and $h = 0.025$ to find approximate values of the solution of

  

$y' + \dfrac{2}{x}y = \dfrac{3}{x^3} + 1$, $y(1) = 1$

  

at $x = 1.0, 1.1, 1.2, \ldots, 2.0$. Compare with the exact solution $y = \dfrac{1}{3x^2}(9\ln x + x^3 + 2)$.

  

**3.1.11**

  

Use Euler's method with step sizes $h = 0.1$, $h = 0.05$, and $h = 0.025$ to find approximate values of the solution of

  

$(3y^2 + 4y)y' + 2x + \cos x = 0$, $y(0) = 1$ (Exercise 2.2.13)

  

at $x = 0, 0.1, 0.2, \ldots, 1.0$.

  

**3.1.15**

  

$y' + 2xy = x^2$, $y(0) = 3$ (Exercise 2.1.38); $h = 0.2, 0.1, 0.05$ on $[0, 2]$

  

---

  

## Week 3

  

### Mon 4/13 — Numerical Methods II: Improved Euler and Runge-Kutta

  

*Reading: 3.2, 3.3*

  

> [!tip] Use `ode45` in MATLAB for Section 3.3 problems.

  

#### Section 3.2

  

In Exercises 1–5 use the improved Euler method to find approximate values of the solution at $x_i = x_0 + ih$, $i = 1, 2, 3$.

  

**3.2.6**

  

Use the improved Euler method with step sizes $h = 0.1$, $h = 0.05$, and $h = 0.025$ to find approximate values of the solution of

  

$y' + 3y = 7e^{4x}$, $y(0) = 2$

  

at $x = 0, 0.1, 0.2, \ldots, 1.0$. Compare with the exact solution $y = e^{4x} + e^{-3x}$.

  

**3.2.7**

  

Use the improved Euler method with step sizes $h = 0.1$, $h = 0.05$, and $h = 0.025$ to find approximate values of the solution of

  

$y' + \dfrac{2}{x}y = \dfrac{3}{x^3} + 1$, $y(1) = 1$

  

at $x = 1.0, 1.1, \ldots, 2.0$. Compare with the exact solution $y = \dfrac{1}{3x^2}(9\ln x + x^3 + 2)$.

  

**3.2.11**

  

Use the improved Euler method with step sizes $h = 0.1$, $h = 0.05$, and $h = 0.025$ to find approximate values of the solution of

  

$(3y^2 + 4y)y' + 2x + \cos x = 0$, $y(0) = 1$ (Exercise 2.2.13)

  

at $x = 0, 0.1, 0.2, \ldots, 1.0$.

  

#### Section 3.3

  

In Exercises 1–5 use the Runge-Kutta method to find approximate values of the solution at $x_i = x_0 + ih$, $i = 1, 2$.

  

**3.3.1**

  

$y' = 2x^2 + 3y^2 - 2$, $y(2) = 1$; $h = 0.05$

  

**3.3.3**

  

$y' + 3y = x^2 - 3xy + y^2$, $y(0) = 2$; $h = 0.05$

  

**3.3.7**

  

Use the Runge-Kutta method with step sizes $h = 0.1$, $h = 0.05$, and $h = 0.025$ to find approximate values of the solution of

  

$y' + \dfrac{2}{x}y = \dfrac{3}{x^3} + 1$, $y(1) = 1$

  

at $x = 1.0, 1.1, \ldots, 2.0$. Compare with the exact solution $y = \dfrac{1}{3x^2}(9\ln x + x^3 + 2)$.

  

---

  

### Wed 4/15 — Applications I

  

*Reading: 4.1, 4.2*

  

#### Section 4.1

  

**4.1.1**

  

The half-life of a radioactive substance is 3200 years. Find the quantity $Q(t)$ of the substance left at time $t > 0$ if $Q(0) = 20$ g.

  

**4.1.3**

  

A radioactive material loses 25% of its mass in 10 minutes. What is its half-life?

  

**4.1.11**

  

A candymaker makes 500 pounds of candy per week, while his large family eats the candy at a rate equal to $Q(t)/10$ pounds per week, where $Q(t)$ is the amount of candy present at time $t$.

  

- (a) Find $Q(t)$ for $t > 0$ if the candymaker has 250 pounds of candy at $t = 0$.

- (b) Find $\lim_{t \to \infty} Q(t)$.

  

**4.1.15**

  

A wizard creates gold continuously at the rate of 1 ounce per hour, but an assistant steals it continuously at the rate of 5% of however much is there per hour. Let $W(t)$ be the number of ounces that the wizard has at time $t$. Find $W(t)$ and $\lim_{t \to \infty} W(t)$ if $W(0) = 1$.

  

**4.1.17**

  

A tank is empty at $t = 0$. Water is added to the tank at the rate of 10 gal/min, but it leaks out at a rate (in gallons per minute) equal to the number of gallons in the tank. What is the smallest capacity the tank can have if this process is to continue forever?

  

**4.1.22**

  

A homebuyer borrows $P_0$ dollars at an annual interest rate $r$, agreeing to repay the loan with equal monthly payments of $M$ dollars per month over $N$ years.

  

- (a) Derive a differential equation for the loan principal $P(t)$ at time $t > 0$, assuming the homebuyer repays continuously.

- (b) Solve the equation derived in (a).

- (c) Use the result of (b) to determine an approximate value for $M$ assuming each year has exactly 12 months of equal length.

- (d) The exact value of $M$ is $M = \dfrac{rP_0}{12}\!\left(1 - (1 + r/12)^{-12N}\right)^{-1}$. Compare with (c) for (i) $P_0 = \$50{,}000$, $r = 7\tfrac{1}{2}\%$, $N = 20$ and (ii) $P_0 = \$150{,}000$, $r = 9.0\%$, $N = 30$.

  

**4.1.23**

  

Assume that the homebuyer of Exercise 22 elects to repay the loan continuously at the rate of $\alpha M$ dollars per month, where $\alpha$ is a constant greater than 1 (accelerated payment).

  

- (a) Determine the time $T(\alpha)$ when the loan will be paid off and the amount $S(\alpha)$ that the homebuyer will save.

- (b) Suppose $P_0 = \$50{,}000$, $r = 8\%$, and $N = 15$. Compute the savings realized by accelerated payments with $\alpha = 1.05$, $1.10$, and $1.15$.

  

#### Section 4.2

  

**4.2.1**

  

A thermometer is moved from a room where the temperature is $70°$F to a freezer where the temperature is $12°$F. After 30 seconds the thermometer reads $40°$F. What does it read after 2 minutes?

  

**4.2.4**

  

A thermometer initially reading $212°$F is placed in a room where the temperature is $70°$F. After 2 minutes the thermometer reads $125°$F.

  

- (a) What does the thermometer read after 4 minutes?

- (b) When will the thermometer read $72°$F?

- (c) When will the thermometer read $69°$F?

  

**4.2.6**

  

An object is placed in a room where the temperature is $20°$C. The temperature of the object drops by $5°$C in 4 minutes and by $7°$C in 8 minutes. What was the temperature of the object when it was initially placed in the room?

  

**4.2.9**

  

A tank initially contains a solution of 10 pounds of salt in 60 gallons of water. Water with $\tfrac{1}{2}$ pound of salt per gallon is added to the tank at 6 gal/min, and the resulting solution leaves at the same rate. Find the quantity $Q(t)$ of salt in the tank at time $t > 0$.

  

---

  

### Fri 4/17 — Applications II

  

*Reading: 4.2, 4.3*

  

#### Section 4.2 (continued)

  

**4.2.13**

  

A chemical reaction in a laboratory with volume $V$ (in ft³) produces $q_1$ ft³/min of a noxious gas as a byproduct. The gas is dangerous at concentrations greater than $\bar{c}$, but harmless at concentrations $\le \bar{c}$. Intake fans pull in fresh air at rate $q_2$ ft³/min and exhaust fans exhaust the mixture at the same rate. Assuming the gas is always uniformly distributed and its initial concentration $c_0$ is at a safe level, find the smallest value of $q_2$ required to maintain safe conditions for all time.

  

**4.2.17**

  

Let $T = T(t)$ and $T_m = T_m(t)$ be the temperatures of an object and a medium respectively, with initial values $T_0$ and $T_{m0}$. Assume $T' = -k(T - T_m)$, $a(T - T_0) + a_m(T_m - T_{m0}) = 0$.

  

- (a) Use (A) and (B) to derive a differential equation involving only $T$.

- (b) Find $T(t)$ and $T_m(t)$ for $t > 0$.

- (c) Find $\lim_{t \to \infty} T(t)$ and $\lim_{t \to \infty} T_m(t)$.

  

**4.2.19**

  

Identical tanks $T_1$ and $T_2$ initially contain $W$ gallons each of pure water. Starting at $t_0 = 0$, a salt solution with constant concentration $c$ is pumped into $T_1$ at $r$ gal/min and drained from $T_1$ into $T_2$ at the same rate. The resulting mixture in $T_2$ is also drained at the same rate. Find the concentrations $c_1(t)$ and $c_2(t)$ in tanks $T_1$ and $T_2$ for $t > 0$.

  

#### Section 4.3

  

*Assume the magnitude of the gravitational force on an object with mass $m$ is constant and equal to $mg$. In exercises involving vertical motion take the upward direction to be positive.*

  

**4.3.1**

  

A firefighter who weighs 192 lb slides down an infinitely long fire pole that exerts a frictional resistive force with magnitude proportional to his speed, with $k = 2.5$ lb-s/ft. Assuming that he starts from rest, find his velocity as a function of time and find his terminal velocity.

  

**4.3.5**

  

A stone weighing $\tfrac{1}{2}$ lb is thrown upward from an initial height of 5 ft with an initial speed of 32 ft/s. Air resistance is proportional to speed, with $k = 1/128$ lb-s/ft. Find the maximum height attained by the stone.

  

**4.3.8**

  

An object with mass $m$ moves vertically through a medium that exerts a resistive force with magnitude proportional to the speed. Let $y = y(t)$ be the altitude of the object at time $t$, with $y(0) = y_0$. Use the results of Example 4.3.1 to show that

  

$$y(t) = y_0 + \frac{m}{k}(v_0 - v - gt).$$

  

**4.3.14**

  

An object of mass $m$ falls in a medium that exerts a resistive force $f = f(s)$, where $s = |v|$ is the speed of the object. Assume that $f(0) = 0$ and $f$ is strictly increasing and differentiable on $(0, \infty)$.

  

- (a) Write a differential equation for the speed $s = s(t)$ of the object.

- (b) Show that if $\lim_{s \to \infty} f(s) \le mg$ then $\lim_{t \to \infty} s(t) = \infty$.

- (c) Show that if $\lim_{s \to \infty} f(s) > mg$ then $\lim_{t \to \infty} s(t) = s_T$ (terminal speed), where $f(s_T) = mg$.

  

**4.3.17**

  

A space probe is to be launched from a space station 200 miles above Earth. Determine its escape velocity in miles/s. Take Earth's radius to be 3960 miles.

  

---

  

## Week 4

  

### Mon 4/20 — Midterm 1

  

*No practice problems — exam day.*

  

---

  

### Wed 4/22 — Second Order Linear ODEs I

  

*Reading: 5.1*

  

#### Section 5.1

  

**5.1.1**

  

- (a) Verify that $y_1 = e^{2x}$ and $y_2 = e^{5x}$ are solutions of $y'' - 7y' + 10y = 0$ on $(-\infty, \infty)$.

- (b) Verify that if $c_1$ and $c_2$ are arbitrary constants then $y = c_1 e^{2x} + c_2 e^{5x}$ is a solution on $(-\infty, \infty)$.

- (c) Solve the IVP: $y'' - 7y' + 10y = 0$, $y(0) = -1$, $y'(0) = 1$.

- (d) Solve the IVP: $y'' - 7y' + 10y = 0$, $y(0) = k_0$, $y'(0) = k_1$.

  

**5.1.2**

  

- (a) Verify that $y_1 = e^x \cos x$ and $y_2 = e^x \sin x$ are solutions of $y'' - 2y' + 2y = 0$ on $(-\infty, \infty)$.

- (b) Verify that if $c_1$ and $c_2$ are arbitrary constants then $y = c_1 e^x \cos x + c_2 e^x \sin x$ is a solution on $(-\infty, \infty)$.

- (c) Solve the IVP: $y'' - 2y' + 2y = 0$, $y(0) = 3$, $y'(0) = -2$.

- (d) Solve the IVP: $y'' - 2y' + 2y = 0$, $y(0) = k_0$, $y'(0) = k_1$.

  

**5.1.3**

  

- (a) Verify that $y_1 = e^x$ and $y_2 = xe^x$ are solutions of $y'' - 2y' + y = 0$ on $(-\infty, \infty)$.

- (b) Verify that $y = e^x(c_1 + c_2 x)$ is a solution on $(-\infty, \infty)$.

- (c) Solve the IVP: $y'' - 2y' + y = 0$, $y(0) = 7$, $y'(0) = 4$.

- (d) Solve the IVP: $y'' - 2y' + y = 0$, $y(0) = k_0$, $y'(0) = k_1$.

  

**5.1.4**

  

- (a) Verify that $y_1 = 1/(x-1)$ and $y_2 = 1/(x+1)$ are solutions of $(x^2-1)y'' + 4xy' + 2y = 0$ on $(-\infty,-1)$, $(-1,1)$, and $(1,\infty)$. What is the general solution on each interval?

- (b) Solve the IVP: $(x^2-1)y'' + 4xy' + 2y = 0$, $y(0) = -5$, $y'(0) = 1$. What is the interval of validity?

- (c) Graph the solution of the IVP.

- (d) Verify Abel's formula for $y_1$ and $y_2$, with $x_0 = 0$.

  

**5.1.6**

  

Find the Wronskian of a given set $\{y_1, y_2\}$ of solutions of $y'' + 3(x^2+1)y' - 2y = 0$, given that $W(\pi) = 0$.

  

**5.1.8**

  

Find the Wronskian of a given set $\{y_1, y_2\}$ of solutions of $x^2 y'' + xy' + (x^2 - \nu^2)y = 0$ (Bessel's equation), given that $W(1) = 1$.

  

**5.1.9**

  

Suppose $p$ and $q$ are continuous on $(a,b)$ and $y_1$ is a solution of $y'' + p(x)y' + q(x)y = 0$ that has no zeros on $(a,b)$. Let $P(x) = \int p(x)\,dx$.

  

- (a) Show that if $K \ne 0$ and $y_2$ satisfies $y_1 y_2' - y_1' y_2 = Ke^{-P(x)}$ on $(a,b)$, then $y_2$ also satisfies (A) and $\{y_1, y_2\}$ is a fundamental set of solutions.

- (b) Conclude that if $y_2 = uy_1$ where $u' = K\dfrac{e^{-P(x)}}{y_1^2(x)}$, then $\{y_1, y_2\}$ is a fundamental set.

  

---

  

### Fri 4/24 — Second Order Linear ODEs II

  

*Reading: 5.1, 5.2*

  

#### Section 5.1 (continued)

  

**5.1.11**

  

$y'' - 6y' + 9y = 0$; $y_1 = e^{3x}$

  

**5.1.15**

  

$x^2 y'' - (2a-1)xy' + a^2 y = 0$ ($a$ = nonzero constant); $x > 0$; $y_1 = x^a$

  

**5.1.27**

  

Suppose $p$ and $q$ are continuous on $(a,b)$ and $\{y_1, y_2\}$ is a fundamental set of solutions of $y'' + p(x)y' + q(x)y = 0$ on $(a,b)$. Let $z_1 = \alpha y_1 + \beta y_2$ and $z_2 = \gamma y_1 + \delta y_2$, where $\alpha, \beta, \gamma, \delta$ are constants. Show that $\{z_1, z_2\}$ is a fundamental set of solutions if and only if $\alpha\delta - \beta\gamma \ne 0$.

  

**5.1.37**

  

Suppose $p$ and $q$ are continuous on $(a,b)$ and $x_0 \in (a,b)$. Let $y_1$ and $y_2$ be the solutions of $y'' + p(x)y' + q(x)y = 0$ such that $y_1(x_0) = 1$, $y_1'(x_0) = 0$ and $y_2(x_0) = 0$, $y_2'(x_0) = 1$.

  

- (a) Show that $\{y_1, y_2\}$ is linearly independent on $(a,b)$.

- (b) Show that any solution $y$ of (A) on $(a,b)$ can be written as $y = y(x_0)y_1 + y'(x_0)y_2$.

- (c) Express the solution of $y'' + p(x)y' + q(x)y = 0$, $y(x_0) = k_0$, $y'(x_0) = k_1$ as a linear combination of $y_1$ and $y_2$.

  

**5.1.41**

  

Recall from Exercise 4 that $1/(x-1)$ and $1/(x+1)$ are solutions of $(x^2-1)y'' + 4xy' + 2y = 0$ on $(-1,1)$. Find solutions $y_1$ and $y_2$ such that $y_1(0)=1$, $y_1'(0)=0$ and $y_2(0)=0$, $y_2'(0)=1$. Then use Exercise 37(c) to write the solution of the IVP $(x^2-1)y'' + 4xy' + 2y = 0$, $y(0) = k_0$, $y'(0) = k_1$ as a linear combination of $y_1$ and $y_2$.

  

#### Section 5.2

  

In Exercises 1–12 find the general solution.

  

**5.2.1**

  

$y'' + 5y' - 6y = 0$

  

**5.2.2** (not assigned — see grid image for context)

  

$y'' - 4y' + 5y = 0$

  

**5.2.3**

  

$y'' + 8y' + 7y = 0$

  

**5.2.4**

  

$y'' - 4y' + 4y = 0$

  

**5.2.5**

  

$y'' + 2y' + 10y = 0$

  

**5.2.11**

  

$4y'' + 4y' + 10y = 0$

  

---

  

## Week 5

  

### Mon 4/27 — Second Order Linear ODEs III

  

*Reading: 5.2, 5.3*

  

#### Section 5.2 (continued)

  

**5.2.15**

  

$6y'' + y' - y = 0$, $y(0) = -1$, $y'(0) = 3$

  

**5.2.22**

  

- (a) Suppose $y$ is a solution of the constant coefficient equation $ay'' + by' + cy = 0$. Let $z(x) = y(x - x_0)$ where $x_0$ is an arbitrary real number. Show that $az'' + bz' + cz = 0$.

- (b) Let $z_1(x) = y_1(x - x_0)$ and $z_2(x) = y_2(x - x_0)$ where $\{y_1, y_2\}$ is a fundamental set of solutions of (A). Show that $\{z_1, z_2\}$ is also a fundamental set.

- (c) Use (b) to restate Theorem 5.2.1 conveniently for solving $ay'' + by' + cy = 0$, $y(x_0) = k_0$, $y'(x_0) = k_1$ where $x_0 \ne 0$.

  

**5.2.23**

  

$y'' + 3y' + 2y = 0$, $y(1) = -1$, $y'(1) = 4$

  

**5.2.25**

  

$y'' - 14y' + 49y = 0$, $y(1) = 2$, $y'(1) = 11$

  

#### Section 5.3

  

In Exercises 1–6 find a particular solution by the method of undetermined coefficients. Then find the general solution and, where indicated, solve the IVP and graph the solution.

  

**5.3.1**

  

$y'' + 5y' - 6y = 22 + 18x - 18x^2$

  

**5.3.2**

  

$y'' - 4y' + 5y = 1 + 5x$

  

**5.3.3**

  

$y'' + 8y' + 7y = -8 - x + 24x^2 + 7x^3$

  

**5.3.6**

  

$y'' + 6y' + 10y = 22 + 20x$, $y(0) = 2$, $y'(0) = -2$

  

**5.3.9**

  

$x^2 y'' - 7xy' + 7y = 13x^{1/2}$

  

**5.3.13**

  

$x^2 y'' - 3xy' + 13y = 2x^4$

  

---

  

### Wed 4/29 — Second Order Linear ODEs IV

  

*Reading: 5.3, 5.4*

  

#### Section 5.3 (continued)

  

In Exercises 16–21 use $a(e^{\alpha x})'' + b(e^{\alpha x})' + ce^{\alpha x} = (a\alpha^2 + b\alpha + c)e^{\alpha x}$ to find a particular solution. Then find the general solution and, where indicated, solve the IVP and graph the solution.

  

**5.3.17**

  

$y'' - 4y' + 5y = e^{2x}$

  

**5.3.21**

  

$y'' + 6y' + 10y = e^{-3x}$

  

In Exercises 24–29 use the fact that differentiating $\cos\omega x$ and $\sin\omega x$ yields linear combinations of $\cos\omega x$ and $\sin\omega x$ to find a particular solution. Then find the general solution and, where indicated, solve the IVP and graph the solution.

  

**5.3.24**

  

$y'' - 8y' + 16y = 23\cos x - 7\sin x$

  

**5.3.27**

  

$y'' + 6y' + 13y = 18\cos x + 6\sin x$

  

#### Section 5.4

  

In Exercises 1–14 find a particular solution.

  

**5.4.1**

  

$y'' - 3y' + 2y = e^{3x}(1 + x)$

  

**5.4.5**

  

$y'' + 4y = e^{-x}(7 - 4x + 5x^2)$

  

**5.4.7**

  

$y'' - 4y' - 5y = -6xe^{-x}$

  

In Exercises 15–19 find the general solution.

  

**5.4.15**

  

$y'' - 3y' + 2y = e^{3x}(1 + x)$

  

**5.4.18**

  

$y'' + 2y' - 3y = -16xe^x$

  

In Exercises 20–23 solve the IVP and plot the solution.

  

**5.4.21**

  

$y'' + 3y' - 4y = e^{2x}(7 + 6x)$, $y(0) = 2$, $y'(0) = 8$

  

---

  

### Fri 5/1 — Second Order Linear ODEs V

  

*Reading: 5.4, 5.5*

  

#### Section 5.4 (continued)

  

In Exercises 24–29 use the principle of superposition to find a particular solution.

  

**5.4.26**

  

$y'' - 8y' + 16y = 6xe^{4x} + 2 + 16x + 16x^2$

  

In Exercises 31–33 compare with the given example.

  

**5.4.31**

  

Compare with Example 5.4.1: $y'' - 7y' + 12y = 4e^{2x}$; $y_p = Ae^{2x}$

  

**5.4.32**

  

Compare with Example 5.4.2: $y'' - 7y' + 12y = 5e^{4x}$; $y_p = Axe^{4x}$

  

**5.4.33**

  

Compare with Example 5.4.3: $y'' - 8y' + 16y = 2e^{4x}$; $y_p = Ax^2 e^{4x}$

  

#### Section 5.5

  

In Exercises 1–17 find a particular solution.

  

**5.5.1**

  

$y'' + 3y' + 2y = 7\cos x - \sin x$

  

**5.5.3**

  

$y'' + 2y' + y = e^x(6\cos x + 17\sin x)$

  

**5.5.5**

  

$y'' - y' + y = e^x(2 + x)\sin x$

  

**5.5.10**

  

$y'' + 2y' + 2y = e^{-x}(8\cos x - 6\sin x)$

  

**5.5.19**

  

$y'' + 9y = -6\cos 3x - 12\sin 3x$

  

In Exercises 20–26 solve the IVP and plot the solution.

  

**5.5.23**

  

$y'' - 2y' + 2y = -e^{-x}(6\cos x + 4\sin x)$, $y(0) = 1$, $y'(0) = 4$

  

**5.5.25**

  

$y'' - 6y' + 10y = -e^{3x}(6\cos x + 4\sin x)$, $y(0) = 2$, $y'(0) = 7$

  

In Exercises 27–32 use the principle of superposition to find a particular solution. Where indicated, solve the IVP.

  

**5.5.29**

  

$y'' - 3y' + 2y = xe^x + 2e^{2x} + \sin x$

  

**5.5.32**

  

$y'' - 4y' + 4y = 6e^{2x} + 25\sin x$, $y(0) = 5$, $y'(0) = 3$

  

---

  

## Week 6

  

### Mon 5/4 — Second Order Linear ODEs VI

  

*Reading: 5.7*

  

#### Section 5.7

  

In Exercises 1–6 use variation of parameters to find a particular solution.

  

**5.7.1**

  

$y'' + 9y = \tan 3x$

  

**5.7.3**

  

$y'' - 3y' + 2y = \dfrac{4}{1 + e^{-x}}$

  

**5.7.5**

  

$y'' - 2y' + y = 14x^{3/2}e^x$

  

**5.7.7**

  

$x^2 y'' + xy' - y = 2x^2 + 2$; $y_1 = x$, $y_2 = \dfrac{1}{x}$

  

**5.7.9**

  

$4x^2 y'' + (4x - 8x^2)y' + (4x^2 - 4x - 1)y = 4x^{1/2}e^x$, $x > 0$; $y_1 = x^{1/2}e^x$, $y_2 = x^{-1/2}e^x$

  

**5.7.24**

  

$x^2 y'' - xy' - 3y = x^{3/2}$; $y_1 = 1/x$, $y_2 = x^3$

  

In Exercises 30–32 use variation of parameters to solve the IVP, given $y_1$, $y_2$ are solutions of the complementary equation.

  

**5.7.31**

  

$(x-1)^2 y'' - 2(x-1)y' + 2y = (x-1)^2$, $y(0) = 3$, $y'(0) = -6$; $y_1 = x-1$, $y_2 = x^2 - 1$

  

---

  

### Wed 5/6 — Spring-Mass Systems I

  

*Reading: 6.1*

  

#### Section 6.1

  

*In the following exercises assume there's no damping.*

  

**6.1.1**

  

A 64 lb object stretches a spring 4 ft in equilibrium. It is attached to a dashpot with damping constant $c = 8$ lb-sec/ft. The object is initially displaced 18 inches above equilibrium and given a downward velocity of 4 ft/sec. Find its displacement and time-varying amplitude for $t > 0$.

  

**6.1.3**

  

An 8 lb weight stretches a spring 1.5 inches. It is attached to a dashpot with damping constant $c = 8$ lb-sec/ft. The weight is initially displaced 3 inches above equilibrium and given an upward velocity of 6 ft/sec. Find and graph its displacement for $t > 0$.

  

**6.1.6**

  

An 8 lb weight stretches a spring 32 ft. The weight is initially displaced 6 inches above equilibrium and given an upward velocity of 4 ft/sec. Find its displacement for $t > 0$ if the medium exerts a damping force of 1.5 lb for each ft/sec of velocity.

  

**6.1.9**

  

A 64 lb weight is suspended from a spring with constant $k = 25$ lb/ft. It is initially displaced 18 inches above equilibrium and released from rest. Find its displacement for $t > 0$ if the medium resists the motion with 6 lb of force for each ft/sec of velocity.

  

**6.1.14**

  

A 32 lb weight stretches a spring 1 ft in equilibrium. It is attached to a dashpot with constant $c = 12$ lb-sec/ft. The weight is initially displaced 8 inches above equilibrium and released from rest. Find its displacement for $t > 0$.

  

**6.1.15**

  

A mass of one kg stretches a spring 49 cm in equilibrium. A dashpot attached to the spring supplies a damping force of 4 N for each m/sec of speed. The mass is initially displaced 10 cm above equilibrium and given a downward velocity of 1 m/sec. Find its displacement for $t > 0$.

  

---

  

### Fri 5/8 — Spring-Mass Systems II

  

*Reading: 6.2*

  

#### Section 6.2

  

**6.2.1**

  

A 64 lb object stretches a spring 4 ft in equilibrium. It is attached to a dashpot with damping constant $c = 8$ lb-sec/ft and subjected to an external force $F(t) = 4\cos 2t$ lb. Determine the steady state component of the displacement for $t > 0$.

  

**6.2.9**

  

An 8 lb weight stretches a spring 8 inches in equilibrium. It is attached to a dashpot with damping constant $c = 0.5$ lb-sec/ft and subjected to an external force $F(t) = 4\cos 2t$ lb. Determine the steady state component of the displacement for $t > 0$.

  

**6.2.13**

  

An 8 lb weight stretches a spring 8 inches in equilibrium. It is attached to a dashpot with damping constant $c = 0.5$ lb-sec/ft and subjected to an external force $F(t) = 4\cos 2t$ lb. Determine the steady state component of the displacement for $t > 0$.

  

**6.2.15**

  

A mass of 20 gm stretches a spring 5 cm. The spring is attached to a dashpot with damping constant 400 dyne sec/cm. Determine the displacement for $t > 0$ if the mass is initially displaced 9 cm above equilibrium and released from rest.

  

**6.2.24**

  

Find the solution of the IVP $my'' + cy' + ky = 0$, $y(0) = y_0$, $y'(0) = v_0$, given that the motion is underdamped, so the general solution is $y = e^{-ct/2m}(c_1\cos\omega_1 t + c_2\sin\omega_1 t)$.

  

**6.2.25**

  

Find the solution of the IVP $my'' + cy' + ky = 0$, $y(0) = y_0$, $y'(0) = v_0$, given that the motion is overdamped, so the general solution is $y = c_1 e^{r_1 t} + c_2 e^{r_2 t}$ ($r_1, r_2 < 0$).

  

**6.2.26**

  

Find the solution of the IVP $my'' + cy' + ky = 0$, $y(0) = y_0$, $y'(0) = v_0$, given that the motion is critically damped, so the general solution is $y = e^{r_1 t}(c_1 + c_2 t)$ ($r_1 < 0$).

  

---

  
