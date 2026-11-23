---
type: study
parent: "[[Econ 104]]"
domain: econ
status: draft
---
Here is the formula in clean general form:

---

**Omitted Variable Bias — the substitution method**

You have the true model:

$$y = \beta_0 + \beta_1 \cdot VOI + \beta_2 \cdot Omitted + \varepsilon$$

You know the relationship between the omitted variable and the VOI:

$$Omitted = \delta_0 + \delta_1 \cdot VOI$$

Substitute the second into the first:

$$y = \beta_0 + \beta_1 \cdot VOI + \beta_2(\delta_0 + \delta_1 \cdot VOI) + \varepsilon$$

Expand:

$$y = (\beta_0 + \beta_2\delta_0) + (\beta_1 + \beta_2\delta_1) \cdot VOI + \varepsilon$$

So the researcher running the univariate model gets:

$$\beta_0^* = \beta_0 + \beta_2\delta_0$$

$$\beta_1^* = \beta_1 + \beta_2\delta_1$$

And the bias on the VOI coefficient is:

$$\text{Bias} = \beta_1^* - \beta_1 = \beta_2\delta_1$$

---

The bias is always the product of two things — how much the omitted variable affects y (β₂) and how much the omitted variable moves with the VOI (δ₁). If either is zero there is no bias. If both are nonzero and the same sign the bias is positive. Opposite signs and the bias is negative — which is what happened in the smoking example.