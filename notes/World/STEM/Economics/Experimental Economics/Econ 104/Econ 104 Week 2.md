---
type: lecture
parent: "[[Econ 104]]"
domain: econ
status: draft
---
- Be able to articulate the difference between a study which is causal because of good experimental design but fails to demonstrate statistical difference 
- If the inverse exists find that

- **Rule of 72 (doubling-time approximation)**  
    Approximation:$$ doubling time (years) \approx \dfrac{72}{\text{growth rate in %}} 
    
	**Exponential growth setup for doubling** $$ 
    If a variable $X$ grows at rate $g$ per year, then $X_0(1+g)^t$; doubling solves $(1+g)^t=2$.
    
- **Solow growth model (baseline idea)**  
    Long-run living standards depend on capital accumulation, saving, depreciation, population growth, and productivity.
    
- **Production function (per worker)**  
    Output per worker $y$ as a function of capital per worker $k$: commonly $y=A k^\alpha$.
    
- **Savings rate $s$**  
    Fraction of output saved and invested: $i = s y$ in per-worker terms.
    
- **Investment (per worker) $i$**  
    In the basic Solow setup: $i = s y$.
    
- **Depreciation rate $\delta$**  
    Capital wears out at rate $\delta$; “break-even investment” term includes $\delta k$.
    
- **Capital accumulation equation (no population growth)**  
    Change in capital per worker: $\Delta k = s y - \delta k$.
    
- **Steady state (no population growth)**  
    $\Delta k=0$, so **steady-state condition**: $s y^* = \delta k^*$.
    
- **Steady-state levels $k^_, y^_, i^_, c^_$**  
    Long-run per-worker values implied by the steady-state condition and the production function.
    
- **Consumption (per worker) $c$**  
    Resource split: $y = c + i$, so $c = (1-s)y$ (in the closed-economy version used in the notes).
    
- **National income accounting identity (open economy)**  
    $Y = C + I + G + NX$.
    
- **Closed economy simplification**  
    With $G=0$ and $NX=0$: $Y = C + I$; per worker: $y=c+i$.
    
- **Savings identity and current account**  
    Notes connect savings to investment and external balance: $S = I + CA$ (with $CA$ labeled “current account”).
    
- **Cobb-Douglas production with labor and capital**  
    $Y = A K^\alpha L^{1-\alpha}$ (constant-returns-to-scale form).
    
- **Marginal product of capital (MPK)**  
    $MPK=\frac{\partial Y}{\partial K}$; linked to the rental rate of capital in competitive equilibrium.
    
- **Marginal product of labor (MPL)**  
    $MPL=\frac{\partial Y}{\partial L}$; linked to the wage in competitive equilibrium.
    
- **Factor prices in competitive equilibrium**  
    “Capital rent = MPK” and “wage = MPL” used to back out parameters/levels.
    
- **Income shares and $\alpha$ (capital share)**  
    In Cobb-Douglas under competition: capital income share $\approx \alpha$, labor income share $\approx 1-\alpha$.
    
- **Cross-country comparisons in Solow (role of $s$)**  
    How differences in saving rates map into differences in $k^_$ and $y^_$ (and ratios like $y_1^_/y_2^_$).
    
- **Model fit / convergence intuition (qualitative)**  
    Checking whether Solow’s predicted output differences match observed differences when “all else equal.”
    
- **Population growth rate $n$ (and doubling-time link)**  
    Using Rule of 72 logic to infer $n$ from “years to double.”
    
- **Malthusian model (core mechanism)**  
    Land per person affects income; higher income raises population growth, which pushes land per person down, limiting long-run income per person.
    
- **Malthusian steady state (population)**  
    Long-run population level $N^*$ where population growth is zero; income per person returns to a subsistence-like level after shocks.
    
- **Technology/productivity shock in Malthus (example: potatoes in Ireland)**  
    Productivity increase raises income temporarily, increases population growth, and leads to a higher long-run population level (with income per person reverting).
    
- **Health/mortality shock in Malthus (example: better medicine)**  
    Lower mortality increases population growth; long-run effect is higher population, with income per person pressured downward.
    
- **Pandemic/mass mortality shock prompt (example: COVID)**  
    Considered as a negative population shock; short-run vs long-run adjustment back toward the Malthusian steady state.
    
- **Solow model with population growth**  
    Per-worker capital shrinks mechanically when labor grows; introduces an additional “dilution” term.
    
- **Capital per worker definition**  
    $k=\dfrac{K}{L}$; when $L$ grows, holding $K$ fixed lowers $k$.
    
- **Break-even investment with population growth**  
    Becomes $(\delta+n)k$ (depreciation plus capital dilution).
    
- **Capital accumulation with population growth**  
    $\Delta k = s y - (\delta+n)k$.
    
- **Steady state with population growth**  
    $s y^* = (\delta+n)k^*$.
    
- **Steady-state formulas under Cobb-Douglas (with $n$)**  
    Deriving $k^_$ and $y^_$ as functions of $s, A, \delta, n, \alpha$ (comparative statics: higher $s$ or $A$ raises $k^_,y^_$; higher $\delta$ or $n$ lowers them).
    
- **Worked computational practice**  
    Solving for $k^_$, then $y^_$, then $c^*$ using the steady-state condition and $c=(1-s)y$ (or $c=y-i$ with $i=s y$).