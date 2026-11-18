---
type: concept
parent: "[[STAT 132]]"
domain: stats
course: "STAT 132"
status: draft
source: "Reading 2 §2.5; DS 7.2"
week: 1
prereqs:
  - "[[PMF, PDF and CDF]]"
  - "[[Parameters]]"
  - "[[Joint probability distribution]]"
retention_band: cold
---
# Likelihood function

For an iid sample, $L(\theta)=\prod_{i=1}^n f(x_i\mid\theta)$.
It is the same formula as the joint PMF/PDF, but the **data are fixed and $\theta$ varies**.

Example: 12 of 20 buses were on time, so $L(p)\propto p^{12}(1-p)^8\,I(0\le p\le1)$, maximized at $p=0.6$.

- It is **not** a distribution for $\theta$ (it doesn't integrate to 1) and it is **not** $P(\theta\mid x)$.
- Only **ratios** matter: $L(\theta_1)/L(\theta_2)$ is the relative support. Constant factors can be dropped (∝).
- Put parameter constraints in with indicators.

## Notation: L(θ; x)

- In $L(\theta \mid x)$ the bar means "with the data $x$ held fixed." It is not conditional probability. Many books write $L(\theta; x)$ to avoid that confusion.
- The input of $L(\theta; x)$ is $\theta$. The data $x$ is loaded first and stays fixed.
- $f(x \mid \theta)$ (Lecture 3 notation) and $L(\theta; x)$ are not the same function: $f$ varies the data with $\theta$ fixed, $L$ varies $\theta$ with the data fixed. At any single pair $(x, \theta)$ they give the same number. $f$ adds to 1 over all possible data; $L$ does not add to 1 over $\theta$ (for example $0.082 + 0.031$).

See [[Log-Likelihood]]. The maximizer is the MLE (wk 3, DS 7.5).
