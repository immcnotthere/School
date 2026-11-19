# Lecture 18 — Supplemental Problems: exact-workflow map and answer checks

**Compiled 2026-11-19 from the user's verbatim pasted Lecture 18 Problems 1–10, including instructor solutions.** Original: [practice problems PDF](../files/lectures/AM20%20Lecture%2018%20-%20practice%20problems.pdf).

**Important:** This page is a *checking key*, not evidence of having independently finished these problems. Start at [Resume Here](LECTURE18_RESUME.md) (Problem 3 isolation step still awaiting answer). Do not show the checking key before a cold attempt.

| # | Prompt / task | Instructor answer-check |
|---|---|---|
| 1 | Convert \(y''+3y'+2y=0\) to first-order system | \(A=\begin{bmatrix}0&1\\-2&-3\end{bmatrix}\) |
| 2 | Convert \(y'''-2y''+y'-5y=0\) | \(A=\begin{bmatrix}0&1&0\\0&0&1\\5&-1&2\end{bmatrix}\) |
| 3 | Eliminate \(x_2\) in \(x_1'=2x_1+x_2,\ x_2'=3x_1+4x_2\) | \(x_1''-6x_1'+5x_1=0\); characteristic roots \(1,5\) |
| 4 | \(A=\begin{bmatrix}3&-2\\2&-2\end{bmatrix}\): general solution and origin | Eigenvalues \(2,-1\), vectors \((2,1)^T,(1,2)^T\); saddle |
| 5 | \(A=\begin{bmatrix}1&1\\4&-2\end{bmatrix}\): general solution and origin | Eigenvalues \(2,-3\), vectors \((1,1)^T,(1,-4)^T\); saddle |
| 6 | Verify #5 solution vectors and Wronskian | Both satisfy \(\mathbf x'=A\mathbf x\); \(W=-5e^{-t}\ne0\) |
| 7a | \(A=\operatorname{diag}(-2,-5)\): classify | Asymptotically stable node |
| 7b | \(A=\begin{bmatrix}0&1\\-1&0\end{bmatrix}\): classify | Center, stable but not asymptotically |
| 7c | \(A=\begin{bmatrix}1&2\\2&1\end{bmatrix}\): classify | Saddle (roots \(-1,3\)) |
| 7d | \(A=\begin{bmatrix}-1&2\\-2&-1\end{bmatrix}\): classify | Asymptotically stable spiral (roots \(-1\pm2i\)) |
| 8 | \(A=\begin{bmatrix}1&1\\4&1\end{bmatrix}, \mathbf x(0)=(2,3)^T\): IVP | Eigenvalues \(3,-1\); \(c_1=7/4,\ c_2=1/4\) |
| 9 | \(u''+5u'+6u=0\): convert, solve, compare scalar equation | \(A=\begin{bmatrix}0&1\\-6&-5\end{bmatrix}\); eigenvalues \(-2,-3\); \(u=c_1e^{-2t}+c_2e^{-3t}\) |
| 10 | \(A=\begin{bmatrix}1&2&0\\0&3&0\\2&-4&2\end{bmatrix}\) | Eigenvalues \(1,2,3\); vectors \((1,0,-2)^T,(0,0,1)^T,(1,1,-2)^T\) |

## Condensed general-solution checking key

**Problem 4:**
\[
\mathbf x(t)=c_1\begin{bmatrix}2\\1\end{bmatrix}e^{2t}+
c_2\begin{bmatrix}1\\2\end{bmatrix}e^{-t}.
\]

**Problem 5:**
\[
\mathbf x(t)=c_1\begin{bmatrix}1\\1\end{bmatrix}e^{2t}+
c_2\begin{bmatrix}1\\-4\end{bmatrix}e^{-3t}.
\]

**Problem 8:**
\[
\mathbf x(t)=\frac74\begin{bmatrix}1\\2\end{bmatrix}e^{3t}+
\frac14\begin{bmatrix}1\\-2\end{bmatrix}e^{-t}.
\]

**Problem 9:**
\[
\mathbf x(t)=c_1\begin{bmatrix}1\\-2\end{bmatrix}e^{-2t}+
c_2\begin{bmatrix}1\\-3\end{bmatrix}e^{-3t}.
\]

**Problem 10:**
\[
\mathbf x(t)=c_1\begin{bmatrix}1\\0\\-2\end{bmatrix}e^t+
c_2\begin{bmatrix}0\\0\\1\end{bmatrix}e^{2t}+
c_3\begin{bmatrix}1\\1\\-2\end{bmatrix}e^{3t}.
\]

## Future attempt tracking protocol

After each *actual* student response, record real local PST/PDT timestamp, problem number and substep, student's verbatim answer, hint level, correctness, targeted skill ID, and next cold-review date. Do **not** infer that obtaining the answer-key text is solving the problems.

Next immediate prompt at [resume guide](LECTURE18_RESUME.md): isolate \(x_2\) in \(x_1'=2x_1+x_2\).

Related: [full session concept map](session-2026-11-18-lecture18-audit.md) · [reusable heuristics](LECTURE18_HEURISTICS.md) · [atomic skill tracker](final-atomic-checkpoints.csv).
