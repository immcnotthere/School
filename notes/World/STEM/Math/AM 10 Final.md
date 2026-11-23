---
parent: "[[AM 10]]"
type: study
domain: math
status: draft
---
Phase 1: The Matrix Spaces Masterclass (Problem 1)

This phase uses the given $4 \times 5$ matrix $A$.

- [x] **Skill 1.1: Extracting Standard Bases.** Row reduce matrix $A$ to RREF. Grab the original pivot columns for your $col(A)$ [[basis]]. Solve $A\overline{x} = \overline{0}$ to find the free variables and extract the $null(A)$ [[basis]].
	- - **Skill 1.1 — Column Space & Null Space Bases**
    - **Part 1: Column Space [[Basis]] — The "Go Back" Rule**
        - **Step 1 — RREF:** Row-reduce your matrix $A$ to find $\text{RREF}(A)$
        - **Step 2 — Find Pivots:** Identify which columns contain leading 1s — these are your **pivot columns**
        - **Step 3 — Go Back:** Return to the **original matrix** $A$ and copy those same pivot columns exactly as written — those vectors are your [[basis]]
            - $\text{Basis}_{\text{col}(A)} = \{\text{pivot col 1 of } A,\ \text{pivot col 2 of } A,\ \ldots\}$
        - **Worked Example:**
            - $M \xrightarrow{\text{RREF}} \begin{bmatrix} 1 & 2 & 0 & -2 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0 \end{bmatrix}$
            - Pivot columns: **1 and 3** → go back to $M$ and grab columns 1 and 3
            - $\text{Basis}_{\text{col}(M)} = \left\{ \begin{bmatrix} 1 \\ 2 \\ 1 \end{bmatrix},\ \begin{bmatrix} 3 \\ 7 \\ 1 \end{bmatrix} \right\}$
    - **Part 2: Null Space [[Basis]] — The "Split the Vector" Rule**
        - **Step 1 — RREF Only:** Forget the original matrix — work entirely from $\text{RREF}(A)$
        - **Step 2 — Identify Variables:**
            - Pivot columns → **Basic variables**
            - Non-pivot columns → **Free variables**
            - Zero rows → **Ignore**
        - **Step 3 — Write Equations:** Turn each non-zero row into an equation set equal to $0$
        - **Step 4 — Isolate:** Rearrange so each **basic variable** is alone on the left, free variables on the right
        - **Step 5 — Split & Factor:** Write the full solution vector, plug in your isolated expressions, split so each free variable gets its own vector, then factor it out front — the resulting numerical vectors are your [[basis]]
            - $\mathbf{x} = x_{f_1}\begin{bmatrix} \vdots \end{bmatrix} + x_{f_2}\begin{bmatrix} \vdots \end{bmatrix} + \cdots \implies \text{Basis}_{\text{null}(A)} = \{\mathbf{v}_1,\ \mathbf{v}_2,\ \ldots\}$
        - **Worked Example:**
            - $\text{RREF}(M) = \begin{bmatrix} 1 & 2 & 0 & -2 \\ 0 & 0 & 1 & 2 \\ 0 & 0 & 0 & 0 \end{bmatrix}$
            - Basic: $x_1, x_3$ — Free: $x_2, x_4$ — Row 3: ignore
            - Equations: $x_1 + 2x_2 - 2x_4 = 0$ and $x_3 + 2x_4 = 0$
            - Isolate: $x_1 = -2x_2 + 2x_4$ and $x_3 = -2x_4$
            - Split & Factor:
                - $\begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{bmatrix} = \begin{bmatrix} -2x_2 + 2x_4 \\ x_2 \\ -2x_4 \\ x_4 \end{bmatrix} = x_2\begin{bmatrix} -2 \\ 1 \\ 0 \\ 0 \end{bmatrix} + x_4\begin{bmatrix} 2 \\ 0 \\ -2 \\ 1 \end{bmatrix}$
                - $\text{Basis}_{\text{null}(M)} = \left\{ \begin{bmatrix} -2 \\ 1 \\ 0 \\ 0 \end{bmatrix},\ \begin{bmatrix} 2 \\ 0 \\ -2 \\ 1 \end{bmatrix} \right\}$
    
- [x] **Skill 1.2: Finding Coordinates (The Hard Way).** Set up an augmented matrix where the columns are your $col(A)$ [[basis]] from Skill 1.1, and the final column is the target vector $\overline{u}$. Row reduce to solve for the coordinate weights.
    - **Skill 1.2 — Coordinate Vectors**
    - **The Object:** The Coordinate Vector, written as $[\vec{u}]_B$
    - **The Geometry — The "Wonky Grid" Rule:** The physical point in space never moves — what changes is the grid you use to get there
        - **Standard Vector** $(\vec{u})$: Directions using the default rigid square axes
        - **Coordinate Vector** $([\vec{u}]_B)$: Directions to that same location using a custom map built from your own [[basis]] vectors
    - **The Verb:** Solve — set it up as a linear system and row-reduce
    - **The 3-Step Process**
        - **Step 1 — Build the Augmented Matrix:** Pack your [[basis]] vectors as columns on the left, target vector on the far right
            - $[\, \vec{b}_1 \mid \vec{b}_2 \mid \dots \mid \vec{u} \,]$
        - **Step 2 — RREF:** Row-reduce the entire augmented matrix until the left side becomes the Identity matrix
        - **Step 3 — Extract:** The numbers in the far-right column are your scalar weights — stack them into a vector and you're done
            - $[\vec{u}]_B = \begin{bmatrix} c_1 \\ c_2 \\ \vdots \end{bmatrix}$
    - **Worked Example — Problem 1(b)**
        - Given: $\vec{u} = \begin{bmatrix} 5 \\ 8 \\ 2 \\ 4 \end{bmatrix}$, and [[basis]] $B = \left\{ \begin{bmatrix} 1 \\ 2 \\ 4 \\ 4 \end{bmatrix},\ \begin{bmatrix} 2 \\ 0 \\ 1 \\ 5 \end{bmatrix},\ \begin{bmatrix} 4 \\ 3 \\ 0 \\ 5 \end{bmatrix} \right\}$
        - Build it:
            - $\begin{bmatrix} 1 & 2 & 4 & \mid & 5 \\ 2 & 0 & 3 & \mid & 8 \\ 4 & 1 & 0 & \mid & 2 \\ 4 & 5 & 5 & \mid & 4 \end{bmatrix}$
        - Row-reduce it:
            - $\xrightarrow{\text{RREF}} \begin{bmatrix} 1 & 0 & 0 & \mid & 1 \\ 0 & 1 & 0 & \mid & -2 \\ 0 & 0 & 1 & \mid & 2 \\ 0 & 0 & 0 & \mid & 0 \end{bmatrix}$
        - Extract it:
            - $[\vec{u}]_B = \begin{bmatrix} 1 \\ -2 \\ 2 \end{bmatrix}$
            - Translation: 1 step along $\vec{b}_1$, backwards 2 steps along $\vec{b}_2$, forward 2 steps along $\vec{b}_3$
- [ ] **Skill 1.3: Gram-Schmidt Orthogonalization.** Take the standard bases you found in 1.1 and apply the shadow/subtract method to force them into 90-degree angles.
    
- [ ] **Skill 1.4: Normalization.** Take your orthogonal vectors from 1.3 and divide each by its own magnitude to create **orthonormal** bases for both $col(A)$ and $null(A)$.
    
- [ ] **Skill 1.5: Finding Coordinates (The Fast Way).** Take the dot product of target vector $\overline{u}$ with each of the orthonormal $col(A)$ [[basis]] vectors you just built in 1.4. These dot products are your new coordinates.
    
- [ ] **Skill 1.6: Subspace Projection.** Take target vector $\overline{v}$ and project it onto $null(A)$ by taking its dot product with each of the orthonormal $null(A)$ [[basis]] vectors, multiplying each result by the respective vector, and adding them up.
    

---

### Phase 2: The Projection Machine (Problem 2)

- [ ] **Skill 2.1: Building a Projection Matrix.** Take the two given vectors for subspace $W$ and put them into the columns of a new matrix $A$. Compute the factory formula: $P_W = A(A^TA)^{-1}A^T$ to build the projection matrix.
    

---

### Phase 3: Least Squares & Best Fit (Problems 3 & 4)

- [ ] **Skill 3.1: Translating Systems to Matrices.** Convert the 5 given equations (starting with $x-y+z=2$) into the matrix format $A\overline{x} = \overline{b}$.
    
- [ ] **Skill 3.2: Solving the Normal Equation.** Multiply your matrices to find $A^TA$ and $A^T\overline{b}$. Set up the augmented matrix for $A^TA\overline{x} = A^T\overline{b}$ and row reduce to find the closest possible solution.
    
- [ ] **Skill 3.3: Designing a Quadratic Model.** Take the 5 given $(x,y)$ coordinate points and plug them into the quadratic template $y = c_0 + c_1x + c_2x^2$ to build a brand new design matrix $A$ and vector $\overline{b}$.
    
- [ ] **Skill 3.4: Fitting the Curve.** Run the exact same Normal Equation process from Skill 3.2 on your new quadratic matrices to find the coefficients $c_0, c_1, c_2$.
    

---

### Phase 4: Orthogonal Diagonalization (Problem 5)

This phase uses the symmetric $3 \times 3$ matrix $B$.

- [ ] **Skill 4.1: Finding Eigenvalues.** Solve the characteristic equation $det(B - \lambda I) = 0$ to find your scalar eigenvalues ($\lambda$).
    
- [ ] **Skill 4.2: Finding Eigenvectors.** Plug each $\lambda$ back into the matrix $(B - \lambda I)$ and find the null space to get your eigenvectors.
    
- [ ] **Skill 4.3: Assembling the Deconstruction.** Normalize those eigenvectors (divide by magnitude) to build your orthogonal matrix $P$. Put the eigenvalues into a diagonal matrix $D$. Write your final answer in the format $B = PDP^T$