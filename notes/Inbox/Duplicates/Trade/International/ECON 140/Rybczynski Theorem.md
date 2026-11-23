---
title: "Rybczynski Theorem"
aliases:
  - Rybczynski
  - Rybczynski effect
  - factor endowment output effect
topic: "Heckscher-Ohlin Model"
course: "Economics 140"
tags:
  - econ140
  - international-trade
  - heckscher-ohlin
  - rybczynski
  - factor-endowments
  - production
type: theorem
related:
  - "[[Heckscher-Ohlin Model]]"
  - "[[Heckscher-Ohlin Theorem]]"
  - "[[Stolper-Samuelson Theorem]]"
  - "[[Relative Factor Intensity]]"
  - "[[Relative Factor Abundance]]"
  - "[[Production Possibility Frontier]]"
  - "[[Rybczynski (1955)]]"
status: "in-progress"
---

# Rybczynski Theorem

---

## Statement

> **An increase in a factor endowment will increase output in the sector that uses that factor intensively, and will decrease output in the other sector** — holding goods prices constant.

Formally, if factor $i$'s endowment increases:

$$\uparrow \bar{F}_i \implies \uparrow Q_{\text{intensive in } i}, \quad \downarrow Q_{\text{other}}$$

This is one of the three core predictions of the [[Heckscher-Ohlin Model]].

---

## Intuition

In the [[Heckscher-Ohlin Model]], both factors ([[Land]] and [[Labor]]) are **fully mobile** across sectors. When one factor's endowment grows:

1. The expanding factor is relatively cheaper → the sector that uses it intensively wants to expand
2. To expand, that sector pulls **both** factors in (because both are needed, via [[Factor Complementarity]])
3. The other sector must shrink to release those factors
4. At the original goods prices, the factor markets re-clear with output shifting toward the intensive sector

The key insight is that the output effect is **more than proportional** — a small increase in a factor endowment leads to a magnified shift in output composition. This is sometimes called the **magnification effect**.

---

## Application in the [[Heckscher-Ohlin Model]]

### Setup

| Sector | Intensive Factor |
|--------|----------------|
| Food (F) | [[Land]] (T) |
| Clothing (C) | [[Labor]] (L) |

### Case 1: Increase in Land (T)

$$\bar{T} \uparrow \implies Q_F \uparrow, \quad Q_C \downarrow$$

- PPF shifts outward but **biased toward Food** (the land-intensive good)
- For a given relative price $\frac{P_C}{P_F}$, the economy produces more Food and less Clothing

### Case 2: Increase in Labor (L)

$$\bar{L} \uparrow \implies Q_C \uparrow, \quad Q_F \downarrow$$

- PPF shifts outward but **biased toward Clothing** (the labor-intensive good)
- For a given relative price $\frac{P_C}{P_F}$, the economy produces more Clothing and less Food

---

## Graphical Intuition

The [[Production Possibility Frontier]] shifts outward **asymmetrically**:

```
Q_F
 |
 |       New PPF (T increases)
 |      /
 |     / ← biased outward along Q_F axis
 |    /    Original PPF
 |   /    /
 |  /    /
 | /    /
 |/____/_________ Q_C
```

- Point 1 (original equilibrium) → Point 2 (new equilibrium at same price ratio)
- $Q_F^2 > Q_F^1$ and $Q_C^2 < Q_C^1$
- The slope $-P_C/P_F$ is the same at both points (prices held fixed)

---

## Why Output of the Other Sector *Falls*

This is the non-obvious part. Why does Clothing output fall when Land increases?

- To expand Food production, the Food sector draws in **more Labor** (via [[Factor Complementarity]])
- This pulls Labor **away from Clothing**
- Even though total Labor is unchanged, the Clothing sector has less of it
- Since Clothing is labor-intensive, $Q_C$ falls

$$\Delta T \uparrow \implies L_F \uparrow \implies L_C \downarrow \implies Q_C \downarrow$$

This is a **general equilibrium** effect — partial equilibrium intuition (more land → just more food) misses the reallocation of Labor.

---

## Connection to Trade and the [[Heckscher-Ohlin Theorem]]

The Rybczynski Theorem explains why countries with different factor endowments have differently shaped PPFs:

- A **land-abundant** country (Foreign: $T^*/L^* > T/L$) has a PPF biased toward Food
- A **labor-abundant** country (Home: $T/L < T^*/L^*$) has a PPF biased toward Clothing
- These differently biased PPFs generate different autarky prices → [[Comparative Advantage]] → trade

$$\frac{T^*}{L^*} > \frac{T}{L} \implies \text{Foreign PPF biased toward Food} \implies \text{Foreign exports Food}$$

---

## Connection to [[Stolper-Samuelson Theorem]]

Rybczynski and [[Stolper-Samuelson Theorem]] are **mathematical duals**:

| Theorem | Exogenous change | Effect on |
|---------|-----------------|-----------|
| [[Stolper-Samuelson Theorem]] | Goods prices ($P_i$) | Factor returns ($w$, $r$) |
| **Rybczynski Theorem** | Factor endowments ($\bar{L}$, $\bar{T}$) | Goods output ($Q_F$, $Q_C$) |

Both operate through the same mechanism: full factor mobility and factor intensity differences. They are dual theorems in the sense that one describes the price side of the model, the other the quantity side.

---

## Real-World Evidence: The [[Asian Tigers]]

From [[Econ 140 – Lecture 10: The Heckscher-Ohlin Model|Lecture 10]]:

Over 40 years, **Taiwan, Singapore, Hong Kong, and South Korea** dramatically increased their endowments of **skilled [[Labor]]** through education and development.

**Rybczynski prediction:**

$$\uparrow \text{Skilled Labor} \implies \uparrow \text{Skill-intensive exports}, \quad \downarrow \text{Low-skill exports}$$

**Observed pattern:**
- 1960: exports concentrated in low-skill-intensive industries
- 1998: exports shifted significantly toward high-skill-intensive industries
- As skill intensity rose, their export share to the US shifted up the skill ladder

This is exactly what the Rybczynski Theorem predicts — and it is one of the cleaner real-world confirmations of the [[Heckscher-Ohlin Model]].

---

## Rybczynski in the Context of Immigration

The theorem also applies to **immigration** — an inflow of workers is equivalent to an increase in the labor endowment:

$$\text{Immigration} \implies \bar{L} \uparrow \implies Q_C \uparrow, \quad Q_F \downarrow$$

At constant goods prices, the labor-abundant sector expands and the land-intensive sector contracts. This helps explain why immigration may affect the output *composition* of an economy without necessarily causing unemployment (factors just reallocate across sectors).

---

## Who Was Rybczynski?

**Tadeusz Rybczynski** (1923–1998) was a Polish-British economist who derived the theorem in his 1955 paper *"Factor Endowment and Relative Commodity Prices"* published in *Economica*. It was originally framed as a theoretical curiosity in a two-sector, two-factor model, but became one of the foundational results of modern trade theory.

---

## Key Equations

$$\frac{T_F}{L_F} > \frac{T_C}{L_C} \quad \text{(Food is land-intensive — required condition)}$$

$$\bar{T} \uparrow \implies Q_F \uparrow, \; Q_C \downarrow \quad \text{(at constant } P_C/P_F\text{)}$$

$$\bar{L} \uparrow \implies Q_C \uparrow, \; Q_F \downarrow \quad \text{(at constant } P_C/P_F\text{)}$$

$$T_F + T_C = \bar{T}, \quad L_F + L_C = \bar{L} \quad \text{(factor market clearing)}$$

---

## 📝 Notes
>

---

## Linked Concepts

- [[Heckscher-Ohlin Model]]
- [[Heckscher-Ohlin Theorem]]
- [[Stolper-Samuelson Theorem]]
- [[Relative Factor Intensity]]
- [[Relative Factor Abundance]]
- [[Production Possibility Frontier]]
- [[Factor Complementarity]]
- [[Comparative Advantage]]
- [[Land]]
- [[Labor]]
- [[Capital]]
- [[Mobile Factor]]
- [[Asian Tigers]]
- [[Magnification Effect]]

---

## See Also

- [[Econ 140 – Lecture 10: The Heckscher-Ohlin Model]]
- [[Stolper-Samuelson Theorem]] — the dual theorem (prices → factor returns)
- [[Heckscher-Ohlin Theorem]] — the trade prediction built on top of Rybczynski logic