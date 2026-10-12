---
type: reference
parent: "[[AM20]]"
domain: math
course: "AM 20"
status: draft
---
# AM 20 Modeling Practice: Build Your Own ODE

Each problem describes a situation in words. **You write the equation**, then classify it: order, linear or nonlinear, time-invariant or time-varying, scalar or system. Answers are folded; open one only after you've written yours down on paper.

## The recipe (use it on every problem)
1. **Name the unknown(s)** and what they measure. Example: $P(t)$ = fish in the lake.
2. **Rate of change = what comes in minus what goes out.** Write $\frac{dP}{dt} = (\text{in}) - (\text{out})$.
3. For each in/out, ask which kind it is:
   - **constant**, the same every moment: a number, like $-1000$
   - **proportional to the amount**: more stuff, more change, like $kP$
   - **proportional to encounters between two things**: a product, like $bxy$, which makes it nonlinear
   - **depends on the clock**: a function of $t$ like $\sin t$, which makes it time-varying
4. **Check the signs**: does this term add or remove?
5. **Classify** with the y-count test (every term has 1 unknown, or 0) and look for a bare $t$.

---

## Level 1: one unknown, one idea

**1. Savings.** Your account earns 5% a year (continuously) and you withdraw \$1000 a year.
> [!success]- Answer
> $\frac{dM}{dt} = 0.05M - 1000$. First order, linear, time-invariant, scalar. In: proportional to the amount. Out: constant.

**2. Coffee cooling.** Coffee cools at a rate proportional to how much hotter it is than the 20°C room.
> [!success]- Answer
> $\frac{dT}{dt} = -k(T - 20)$, with $k > 0$. First order, linear, time-invariant, scalar. (This is Newton's Law of Cooling.)

**3. IV drip.** A drip adds a drug at a constant 5 mg/hour, and the body clears it at a rate proportional to the amount present.
> [!success]- Answer
> $\frac{dA}{dt} = 5 - kA$. First order, linear, time-invariant, scalar. Same shape as the falling ball: $m v' = mg - \gamma v$.

## Level 2: spot the nonlinear or time-varying piece

**4. A rumor.** In a school of $N$ students, a rumor spreads at a rate proportional to (students who know) times (students who don't).
> [!success]- Answer
> $\frac{dR}{dt} = kR(N - R) = kNR - kR^2$. First order, **nonlinear** (the $R^2$ term has 2 unknowns), time-invariant, scalar. Encounters mean a product, and a product means nonlinear.

**5. Pills on a schedule.** Same as problem 3, but the drug now comes in waves: the input rate is $5(1 + \cos t)$.
> [!success]- Answer
> $\frac{dA}{dt} = 5(1 + \cos t) - kA$. First order, linear, **time-varying** ($t$ appears on its own). Still linear: $\cos t$ never touches $A$.

**6. Fast falling ball.** At high speed, air drag is proportional to the **square** of the velocity.
> [!success]- Answer
> $m\frac{dv}{dt} = mg - \gamma v^2$: first order, **nonlinear** ($v^2$), time-invariant, scalar. In position form, $m x'' = mg - \gamma (x')^2$: second order, still nonlinear.

**7. Fishing a lake.** Fish grow logistically (growth $rP$, slowed by crowding: $rP(1 - P/K)$), and fishers remove a constant $h$ fish per year.
> [!success]- Answer
> $\frac{dP}{dt} = rP\left(1 - \frac{P}{K}\right) - h$. First order, nonlinear ($P^2$ hides inside the crowding term), time-invariant, scalar.

## Level 3: second order

**8. Spring.** A mass $m$ on a spring (force $-kx$) with friction proportional to velocity.
> [!success]- Answer
> $m\frac{d^2x}{dt^2} = -kx - \gamma\frac{dx}{dt}$. **Second order**, linear, time-invariant, scalar. Unlike the falling ball, you can't drop to first order with $v = x'$, because $-kx$ needs $x$ itself.

**9. Pushed spring.** Same spring, plus someone pushes it with force $F\cos(\omega t)$.
> [!success]- Answer
> $m x'' + \gamma x' + kx = F\cos(\omega t)$. Second order, linear, **time-varying**, scalar.

## Level 4: systems (more than one unknown)

**10. Two tanks.** Salt water flows out of tank 1 into tank 2, and out of tank 2 to the drain, both at rate $r$; each tank holds volume $V$. Let $Q_1$, $Q_2$ be the salt in each tank.
> [!success]- Answer
> $Q_1' = -\frac{r}{V}Q_1$ and $Q_2' = \frac{r}{V}Q_1 - \frac{r}{V}Q_2$. First order, linear, time-invariant, **system** (2 unknowns). Every term has exactly 1 unknown.

**11. Competitors, not predators.** Two species eat the same food. Each grows on its own, and each is hurt by meeting the other.
> [!success]- Answer
> $x' = ax - bxy$ and $y' = cy - dxy$. A nonlinear system. Compare with Lotka-Volterra: there the $xy$ term **helps** the predator ($+dxy$); here it hurts **both** ($-bxy$, $-dxy$).

**12. An epidemic (SIR).** Susceptible people $S$ get infected by meeting infected people $I$; infected people recover at a rate proportional to $I$; recovered people are $R$.
> [!success]- Answer
> $S' = -\beta SI$, $I' = \beta SI - \gamma I$, $R' = \gamma I$. A 3-unknown, first-order, nonlinear system ($SI$), time-invariant.

## Level 5: your own
**13.** Pick something from your own life that changes over time: your focus during a study block, caffeine in your blood, your savings, the flashcards you have due. Name the unknown, list what adds to it and what drains it, write the equation, and classify it. Then ask Claude to check your work.
