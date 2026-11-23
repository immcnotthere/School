# AM 20 S26 - Lecture 17

## Slide 1
Lecture 17
Spring-Mass systems, II
* Free, damped vibrations (continued).
* Forced, damped vibrations.
	* The steady-state motion.
* Algebra and optimization.

## Slide 2
Part III: Spring mass - dashpot
"Free, damped vibrations" (no external force)

## Slide 3
Equation for free, damped motion
$$my'' + cy' + ky = 0$$
($m$ = mass, $c$ = damping constant, $k$ = spring constant)
Characteristic equation: $mr^2 + cr + k = 0$
Case (i): $c > 2\sqrt{mk}$ ($c^2 - 4mk > 0$)

## Slide 4
Case (ii): $c < 2\sqrt{mk}$ ($c^2 - 4mk < 0$)
$r = -\frac{c}{2m} \pm i\omega_1$
$\omega_1 = \frac{\sqrt{|c^2 - 4mk|}}{2m}$
General Solution:
$$y = e^{-\frac{c}{2m}t}(c_1\cos(\omega_1t) + c_2\sin(\omega_1t))$$

## Slide 5
*(Graph of an exponentially decaying sine wave)*
$y = e^{-\frac{c}{2m}t}(c_1\cos(\omega_1t) + c_2\sin(\omega_1t))$
"underdamped"

## Slide 6
Example (from Lect. 16) contin.
A 1 kg mass stretches a spring 50 cm in equilibrium, and is suspended in a dashpot with damping constant $c = 2$.
The mass is displaced downward 40cm, and released... Find $y(t) =$ height of mass at time $t$.

## Slide 7
Equation of motion: $y'' + 2y' + 19.6y = 0$
Discriminant: $2^2 - 4 \cdot 1 \cdot 19.6 = -74.4$
$r = -\frac{2}{2} \pm i \cdot \frac{\sqrt{74.4}}{2} \approx -1 \pm 4.31i$
$$y = e^{-t}(c_1\cos(4.31t) + c_2\sin(4.31t))$$

## Slide 8
$y(0) = -0.4, y'(0) = 0 \rightarrow c_1 = -0.4$
$y' = e^{-t}(-4.31c_1\sin(4.31t) + 4.31c_2\cos(4.31t)) - e^{-t}(c_1\cos(4.31t) + c_2\sin(4.31t))$
$y'(0) = 0 \rightarrow 4.31c_2 - c_1 = 0 \rightarrow 4.31c_2 + 0.4 = 0$
$c_2 \approx -0.09$

## Slide 9
*(Graph comparing underdamped and overdamped motion)*
$y = -e^{-t}(0.4\cos(4.31t) + 0.09\sin(4.31t))$
Underdamped ($c=2$) vs Overdamped ($c=10$, from Lecture 16)

## Slide 10
Case (iii): $c = 2\sqrt{mk}$ ($c^2 - 4mk = 0$)
$r = -\frac{c}{2m}$
General solution:
$$y = e^{-\frac{c}{2m}t}(c_1 + c_2t)$$
"Critically damped"

## Slide 11
Example, continued some more
"A 1 kg mass stretches... $c = \sqrt{78.4} \approx 8.85$..."
$y'' + \sqrt{78.4}y' + 19.6y = 0$
$r = -\frac{c}{2m} = -\frac{\sqrt{78.4}}{2} \approx -4.427$
$$y \approx e^{-4.427t}(c_1 + c_2t)$$

## Slide 12
$y \approx e^{-4.427t}(c_1 + c_2t)$
$y(0) = -0.4 \rightarrow c_1 = -0.4$
$y' = -4.427e^{-4.427t}(c_1 + c_2t) + c_2e^{-4.427t}$
$y'(0) = 0 \rightarrow c_2 = -0.4 \cdot \frac{\sqrt{78.4}}{2} \approx -1.77$
Solution:
$$y \approx -e^{-4.427t}(0.4 + 1.77t)$$

## Slide 13
*(Graph showing all three damping cases)*
critical ($c \approx 8.85$), under ($c=2$), over ($c=10$)
$y_c \approx -e^{-4.427t}(0.4 + 1.77t)$

## Slide 14
Observations:
Underdamped: moves quickly to equilibrium, but then oscillates around it (MAMA Bear).
Overdamped: moves more slowly to equilibrium (PAPA Bear).
Critically damped: moves as quickly as possible to equilibrium, without oscillation (BABY Bear).

## Slide 15
Part IV: Forced, damped vibrations
$my'' + cy' + ky = F_0\cos(\omega t)$
Observation: $F_0\cos(\omega t)$ is not a typical solution of $my'' + cy' + ky = 0$, because $m, c,$ and $k$ are all $> 0$.
So...

## Slide 16
...a particular solution of ODE is: $y_p = A\cos(\omega t) + B\sin(\omega t) = R\cos(\omega t - \phi)$
Where $R^2 = A^2 + B^2$, $R\cos\phi = A$, $R\sin\phi = B$
and $A, B$ depend on $F_0, \omega, m, c, k$

## Slide 17
This means that the general solution of ODE is...
forced response $\rightarrow y = R\cos(\omega t - \phi) + y_h$
where $y_h$ is the corresponding homogeneous solution (the three unforced cases).

## Slide 18
in all three cases $\lim_{t \rightarrow \infty} y_h = 0$
"in the long run" $y \approx R\cos(\omega t - \phi)$
Terminology:
$y_p = R\cos(\omega t - \phi)$ is steady state component
$y_h$ is the transient component

## Slide 19
Next: How does $R$ depend on $F_0, \omega, m, c, k$?
First: $A$ and $B$...
$y_p = A\cos(\omega t) + B\sin(\omega t)$
$y_p' = -A\omega\sin(\omega t) + \omega B\cos(\omega t)$
$y_p'' = -A\omega^2\cos(\omega t) - \omega^2B\sin(\omega t)$

## Slide 20
$my_p'' + cy_p' + ky_p$
$= m(-A\omega^2\cos(\omega t) - \omega^2B\sin(\omega t)) + c(-A\omega\sin(\omega t) + \omega B\cos(\omega t)) + k(A\cos(\omega t) + B\sin(\omega t))$
$= \cos(\omega t)(kA - m\omega^2A + c\omega B) + \sin(\omega t)(-c\omega A + kB - m\omega^2B) = F_0\cos(\omega t)$

## Slide 21
*(Image of Gabriel Cramer)*
$\begin{cases}(k - m\omega^2)A + c\omega B = F_0 \\ -c\omega A + (k - m\omega^2)B = 0 \end{cases}$
$$A = \frac{F_0(k - m\omega^2)}{(k - m\omega^2)^2 + c^2\omega^2}$$
$$B = \frac{F_0c\omega}{(k - m\omega^2)^2 + c^2\omega^2}$$

## Slide 22
$$y_p = \frac{F_0(k - m\omega^2)}{(k - m\omega^2)^2 + c^2\omega^2}\cos(\omega t) + \frac{F_0c\omega}{(k - m\omega^2)^2 + c^2\omega^2}\sin(\omega t)$$
$R^2 = A^2 + B^2 = \left(\frac{F_0(k - m\omega^2)}{(k - m\omega^2)^2 + c^2\omega^2}\right)^2 + \left(\frac{F_0c\omega}{(k - m\omega^2)^2 + c^2\omega^2}\right)^2$
$$R^2 = \frac{F_0^2 \cdot ((k - m\omega^2)^2 + c^2\omega^2)}{((k - m\omega^2)^2 + c^2\omega^2)^2}$$

## Slide 23
and
$$R = \frac{F_0}{\sqrt{(k - m\omega^2)^2 + c^2\omega^2}}$$
$\cos\phi = \frac{k - m\omega^2}{\sqrt{(k - m\omega^2)^2 + c^2\omega^2}}$, $\sin\phi = \frac{c\omega}{\sqrt{(k - m\omega^2)^2 + c^2\omega^2}}$

## Slide 24
Question: What value of $\omega$ (the forcing frequency) maximizes the forced amplitude $R$?
maximize $\frac{F_0}{\sqrt{(k - m\omega^2)^2 + c^2\omega^2}}$ as a function of $\omega$.
$\rightarrow$ minimize $f(\omega) = (k - m\omega^2)^2 + c^2\omega^2$ as a function of $\omega$.

## Slide 25
First:
$(k - m\omega^2) = m\left(\frac{k}{m} - \omega^2\right) = m(\omega_0^2 - \omega^2)$ (natural frequency)
so $f(\omega) = m^2(\omega_0^2 - \omega^2)^2 + c^2\omega^2$
$f'(\omega) = 2m^2(\omega_0^2 - \omega^2) \cdot (-2\omega) + 2c^2\omega$
$= 2\omega(c^2 - 2m^2(\omega_0^2 - \omega^2))$
$= 2\omega(2m^2\omega^2 + (c^2 - 2m^2\omega_0^2))$

## Slide 26
$f'(\omega) = 0 \rightarrow \omega = 0$ and...
(i) if $c^2 \ge 2m^2\omega_0^2$, then $\omega = 0$ is the only c.p., and $f'(\omega) > 0$ for $\omega > 0$
$f(0) = m^2 \cdot \omega_0^4 = m^2 \cdot \frac{k^2}{m^2} = k^2$ is the min. value.

## Slide 27
In this case ($c^2 \ge 2m^2\omega_0^2$), max amplitude is $R_{max} = \frac{F_0}{k}$ ($\omega = 0$)
Moreover: $\cos\phi = 1$, $\sin\phi = 0 \rightarrow \phi = 0$
$\Rightarrow y_p = \frac{F_0}{k}$ (constant)

## Slide 28
*(Graph plotting $y_p$ for different $\omega$ values)*
Example $y'' + 3y' + y = 2\cos(\omega t)$
$y(0)=0$, $y'(0)=0$
Curves shown for $\omega = 0, 0.5, 2, 4$

## Slide 29
$f'(\omega) = 2\omega(2m^2\omega^2 + (c^2 - 2m^2\omega_0^2))$
(ii) If $c^2 < 2m^2\omega_0^2$ ( $= 2km$), then $f' = 0$ at $\omega = 0$ (still)
AND: when $2m^2\omega^2 = 2m^2\omega_0^2 - c^2$
$$\omega_1 = \sqrt{\omega_0^2 - \frac{c^2}{2m^2}}$$

## Slide 30
Also $0 < \omega < \sqrt{\omega_0^2 - \frac{c^2}{2m^2}} \rightarrow f'(\omega) < 0$
$\sqrt{\omega_0^2 - \frac{c^2}{2m^2}} < \omega \rightarrow f'(\omega) > 0$
$f\left(\sqrt{\omega_0^2 - \frac{c^2}{2m^2}}\right)$ is the abs. min
SO: $\omega_1 = \sqrt{\omega_0^2 - \frac{c^2}{2m^2}}$ is the amplitude maximizing frequency.

## Slide 31
Finally: $f(\omega_1) = m^2(\omega_0^2 - \omega_1^2)^2 + c^2\omega_1^2$
$= m^2\left(\omega_0^2 - \left(\omega_0^2 - \frac{c^2}{2m^2}\right)\right)^2 + c^2\left(\omega_0^2 - \frac{c^2}{2m^2}\right) = \dots = \frac{c^2}{4m^2}(4mk - c^2)$
The max amplitude is
$$R_{max} = \frac{F_0}{\sqrt{f(\omega_{max})}} = \frac{2mF_0}{c\sqrt{4mk - c^2}}$$

## Slide 32
*(Graph illustrating resonance amplitude peak)*
Example: $y'' + y' + y = 2\cos(\omega t)$
$\omega_1 = \sqrt{1 - \frac{1}{2}} = \frac{1}{\sqrt{2}} \approx 0.707$
$R_{max} = \frac{4}{\sqrt{3}} \approx 2.31$
Curves shown for $\omega = 0.25, 0.707, 2$