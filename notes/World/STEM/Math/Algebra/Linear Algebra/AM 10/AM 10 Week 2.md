---
type: lecture
parent: "[[AM 10]]"
domain: math
status: draft
---
- Find a more efficent way to do RREF using Euclid or smth

Example (showing the “only trivial solution” test):

Let
$$
\mathbf{u}_1=\begin{bmatrix}1\\0\end{bmatrix},\quad
\mathbf{u}_2=\begin{bmatrix}0\\1\end{bmatrix}\in\mathbb{R}^2.
$$

Check condition (ii): solve
$$
c_1\mathbf{u}_1+c_2\mathbf{u}_2=\mathbf{0}.
$$

Write it out:
$$
c_1\begin{bmatrix}1\\0\end{bmatrix}+c_2\begin{bmatrix}0\\1\end{bmatrix}
=
\begin{bmatrix}c_1\\c_2\end{bmatrix}
=
\begin{bmatrix}0\\0\end{bmatrix}.
$$

So
$$
\begin{aligned}
c_1&=0\\
c_2&=0
\end{aligned}
$$
is the only solution, which means $\mathbf{u}_1,\mathbf{u}_2$ are linearly independent.

And condition (i) matches: $\mathbf{u}_1\notin\operatorname{span}(\mathbf{u}_2)$ and $\mathbf{u}_2\notin\operatorname{span}(\mathbf{u}_1)$.