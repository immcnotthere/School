---
type: concept
parent: "[[AM 10]]"
domain: math
status: draft
---
[[Reduced Row Echelon Form (RREF)]], [[Column space]], & [[Null space]]


Let

$$  
A =  
\begin{bmatrix}  
1 & 2 & 4 & 4 & 5 \\  
2 & 0 & 3 & 7 & 5 \\  
4 & 1 & 0 & 7 & 4 \\ 
4 & 5 & 5 & 8 & 9  
\end{bmatrix}.  
$$

### 1. [[Row-reduce]]

$$  
\operatorname{rref}(A) =  
\begin{bmatrix}  
1 & 0 & 0 & 2 & 1 \\  
0 & 1 & 0 & -1 & 0 \\  
0 & 0 & 1 & 1 & 1 \\  
0 & 0 & 0 & 0 & 0  
\end{bmatrix}.  
$$

[[Pivot columns]] are columns 1, 2, 3. Columns 4 and 5 are [[Free columns|free]].

---

### 2. [[Basis]] for the [[Column space]]

Take the pivot columns of the original matrix (A):

$$  
\mathcal{C}(A) = \left\{\begin{bmatrix} 1\\2\\4\\4\\ \end{bmatrix}, \begin{bmatrix} 2\\0\\1\\5\\ \end{bmatrix},\begin{bmatrix} 4\\3\\0\\5\\ \end{bmatrix} \right\}   $$


So a [[Basis]] for $(\operatorname{col}(A))$ is


$$   \left\{\begin{bmatrix} 1\\2\\4\\4\\ \end{bmatrix}, \begin{bmatrix} 2\\0\\1\\5\\ \end{bmatrix},\begin{bmatrix} 4\\3\\0\\5\\ \end{bmatrix} \right\}   $$


---

### 3. Basis for the null space

Let the variables corresponding to columns 4 and 5 be [[Free columns|free]]:  
 
$$x_4 = s,\quad x_5 = t.  
$$

Read the equations from $(\operatorname{rref}(A))$:

$$  
\begin{aligned}  
x_1 + 2x_4 + x_5 &= 0 \quad\Rightarrow\quad x_1 = -2s - t,\\  
x_2 - x_4 &= 0 \quad\Rightarrow\quad x_2 = s,\\  
x_3 + x_4 + x_5 &= 0 \quad\Rightarrow\quad x_3 = -s - t.  
\end{aligned}  
$$

So any solution of (A\mathbf{x} = \mathbf{0}) has the form

# $$  
\mathbf{x} =  
\begin{bmatrix}x_1\\x_2\\x_3\\x_4\\x_5\end{bmatrix}
=
s\begin{bmatrix}-2\\1\\-1\\1\\0\\ \end{bmatrix} +  
t\begin{bmatrix}-1\\0\\-1\\0\\1\\ \end{bmatrix}.  
$$

Therefore a basis for $\operatorname{null}(A)$ is
$$  
\left\{\begin{bmatrix}-2\\1\\-1\\1\\0\\ \end{bmatrix},  
\begin{bmatrix}-1\\0\\-1\\0\\1\\ \end{bmatrix} \right\}  
$$