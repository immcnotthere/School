---
parent: "[[ECON 140]]"
tags:
  - econ140
  - international-trade
  - new-trade-theory
  - monopolistic-competition
  - krugman
  - ucsc
  - lecture-notes
course: "Econ 140"
topic: "New Trade Theory"
lectures: [5, 6]
instructor: "Gueyon Kim"
aliases:
  - "NTT"
  - "Krugman Model"
  - "Monopolistic Competition Trade Model"
cssclasses:
  - wide-page
type: concept
domain: econ
status: draft
---

# New Trade Theory — Lectures 5 & 6

> [!abstract] What this note covers
> Paul Krugman's **monopolistic competition model** of trade, developed to explain patterns that [[Ricardian Model|Ricardian]] and [[Hecksher-Ohlin Model|H–O]] theory can't: extensive trade between *similar* industrial countries, and two-way trade in *differentiated* products within the same industry.
>
> - **Lecture 5** — builds the model from scratch: assumptions → demand → supply → PP curve → CC curve → autarky equilibrium → trade equilibrium → worked example.
> - **Lecture 6** — reviews the model, presents empirical evidence (Broda–Weinstein, Goldberg et al.), and analyzes redistribution effects of trade.
> - **Techniques section** — a reverse-engineered toolkit view: for each analytical move in the model, what problem it solves, what inputs it takes, what operation it performs, what output it yields.

> [!info] Core model ingredients at a glance
> - **Market structure:** Monopolistic competition (many firms, differentiated products, price setters, free entry/exit)
> - **Demand (residual):** $Q = S\!\left[\dfrac{1}{N} - b(P - P_{\text{avg}})\right]$
> - **Cost:** $TC = F + cQ$ (fixed + constant marginal)
> - **PP curve (pricing):** $P = c + \dfrac{1}{Nb}$
> - **CC curve (zero profit):** $P = \dfrac{FN}{S} + c$
> - **Equilibrium:** $N^* = \sqrt{\dfrac{S}{bF}}$, $P^* = \sqrt{\dfrac{F}{Sb}} + c$

---

## Quick Navigation

- [[#Lecture 5 — New Trade Theory Part I]]
- [[#Lecture 6 — New Trade Theory Part II]]
- [[#Techniques — Problem ▸ Inputs ▸ Operation ▸ Output]]
- [[#Master Formula Sheet]]
- [[#Glossary of Symbols]]

---

# Lecture 5 — New Trade Theory Part I

> [!quote] The motivating puzzle
> *"For some time now there has been considerable skepticism about the ability of comparative cost theory to explain the actual pattern of international trade. Neither the extensive trade among the industrial countries, nor the prevalence in this trade of two-way exchanges of differentiated products, make much sense in terms of standard theory."*
> — Paul Krugman (1980)

---

### Slide 1 — Title

**Topic:** New Trade Theory: Part I. Introduces the framework that won Krugman the 2008 Nobel.

#### Notes
> [!note]- Your notes
> *

---

### Slide 2 — Plan for Today

Roadmap: two types of trade (inter- vs intra-industry) → assumptions of NTT → demand/supply → equilibrium (PP and CC curves) → trade equilibrium → worked example.

#### Notes
> [!note]- Your notes
> *

---

### Slide 3 — Two Types of Trade (Inter-Industry)

**Inter-industry trade** = trade *between* industries (e.g. food for automobiles).
- Based on **comparative advantage**.
- Arises when countries differ in **opportunity costs** because of:
  - Differences in relative **productivities** ([[Ricardian Model]])
  - Differences in relative **resource endowments** ([[Hecksher-Ohlin Model|Heckscher-Ohlin Model]])

#### Notes
> [!note]- Your notes
> *

---

### Slide 4 — Inter-Industry Trade Example

In the Ricardian and Heckscher–Ohlin models, countries **specialize** and trade is inter-industry.

> [!example] Textbook case
> If Clothing is capital-intensive and Food is labor-intensive, then a capital-abundant Home exports Clothing while a labor-abundant Foreign exports Food. There is **no two-way trade in the same good**.

#### Notes
> [!note]- Your notes
> *

---

### Slide 5 — Intra-Industry Trade

**Intra-industry trade** = trade *within* industries (e.g. Fords for Mercedes/Toyotas/Volvos).
- Based on **economies of scale** (not comparative advantage).
- Can arise between **similar** economies.
- **Empirically big:** 1/4 to 1/3 of all international trade is intra-industry.

#### Notes
> [!note]- Your notes
> *

---

### Slide 6 — Intra-Industry Trade: US Golf Club Imports

The U.S. imports golf clubs from a wide array of countries — China dominates by quantity (14.5M clubs) and value ($385M).

> [!info] What to notice
> Average prices vary enormously by source (from $6/club from the UK to $197/club from Japan), suggesting **quality/variety differentiation** within the "golf club" category.

#### Notes
> [!note]- Your notes
> *

---

### Slide 7 — Intra-Industry Trade: US Golf Club Exports

The U.S. *also exports* golf clubs to many of the **same countries** (Japan, Canada, Korea, Hong Kong, UK…). This is the two-way trade in differentiated products that motivates NTT.

#### Notes
> [!note]- Your notes
> *

---

### Slide 8 — Intra-Industry Trade Goes Beyond Golf Clubs

Intra-industry trade indices (higher = more two-way trade in that category):

| Product | IIT Index |
|---|---|
| Vaccines | 82% |
| Whiskey | 82% |
| Frozen orange juice | 81% |
| Natural gas | 69% |
| Mattresses | 46% |
| Golf clubs | 41% |
| Small cars | 40% |
| Apples | 34% |
| Sunglasses | 32% |
| Large passenger aircraft | 10% |
| Men's shorts | 2% |

#### Notes
> [!note]- Your notes
> *

---

### Slide 9 — "New" Trade Theory (Krugman 1980)

Krugman articulates the puzzle: standard theory cannot explain (a) extensive trade among industrial countries and (b) two-way trade in differentiated products. A new framework is needed.

#### Notes
> [!note]- Your notes
> *

---

### Slide 10 — Paul Krugman

One of the authors of the course textbook; won the **Nobel Prize in 2008** largely for the model developed in this lecture.

#### Notes
> [!note]- Your notes
> *

---

### Slide 11 — Three Pillars of "New" Trade Theory

> [!important] Three new ingredients
> 1. **Product differentiation** — "consumers love variety." Firms produce *different* products; utility rises with variety.
> 2. **Imperfect competition** — differentiated producers are **price setters** facing downward-sloping demand (unlike perfect competition's price takers).
> 3. **Economies of scale** — average cost falls as output rises. Opening to trade **expands the market**, letting firms capitalize on scale.

#### Notes
> [!note]- Your notes
> *

---

### Slide 12 — Plan Recap

Section transition: now moving into assumptions and model mechanics.

#### Notes
> [!note]- Your notes
> *

---

### Slide 13 — Assumptions

Two identical countries: **Home** and **Foreign** (*).

> [!info] Market structure: Monopolistic competition
> - Many ($N$) small firms in each country
> - Firms produce **differentiated** products (one variety per firm — "monopolist of its own variety")
> - **Free entry and exit**

> [!info] Economies of scale
> 1. Cost per unit **falls** as firm output rises
> 2. This translates into **lower prices**

> [!info] Symmetry
> Firms are identical except for the label of their variety. Each faces identical demand, has identical production technology and cost structure.

#### Notes
> [!note]- Your notes
> *

---

### Slide 14 — Market Structure: Monopolistic Competition vs Perfect Competition

| Feature | Perfect Competition | Imperfect Competition (Monopolistic) |
|---|---|---|
| Firm behavior | Price **taker** | Price **setter** |
| Products | Identical (perfect substitutes) | Differentiated |
| Firm's demand curve | Perfectly **elastic** (horizontal) | Downward-sloping |
| Market power | None | Some, but eroded by competitors |

> [!tip] Key distinction
> **Monopolistic competition = many firms, each with some market power over its own variety, but competing with close substitutes.**

#### Notes
> [!note]- Your notes
> *

---

### Slide 15 — Demand (Residual Demand Curve)

Each differentiated-good producer faces:

$$Q = S\!\left[\frac{1}{N} - b(P - P_{\text{avg}})\right]$$

| Symbol | Meaning |
|---|---|
| $Q$ | Quantity sold by **the firm** |
| $S$ | Total quantity sold in the firm's industry ("market size") |
| $N$ | Number of firms in the industry |
| $P$ | Price **this** firm charges |
| $P_{\text{avg}}$ | Average price charged by **all** firms in the industry |
| $b$ | Substitutability of products |

> [!tip] Intuition for each term
> - $S/N$ is the firm's "fair share" of the market if all firms charged the same price.
> - The $-b(P - P_{\text{avg}})$ term **penalizes** firms whose price is above the industry average. Higher $b$ → more substitutable → bigger penalty.
>
> Each firm takes $S$, $N$, $b$, and $P_{\text{avg}}$ **as given**.

#### Notes
> [!note]- Your notes
> *

---

### Slide 16 — Demand (Rearranged) and Symmetry

Inverting the residual demand:

$$P = P_{\text{avg}} + \frac{1}{Nb} - \frac{Q}{Sb}$$

- **Slope** of the firm's demand is $-\dfrac{1}{Sb}$.
- Higher $b$ (more substitutable) → **flatter** demand → less market power.
- In the symmetric equilibrium $P = P_{\text{avg}}$, which implies $Q = \dfrac{S}{N}$ — each firm gets an equal market share.

#### Notes
> [!note]- Your notes
> *

---

### Slide 17 — Demand and Marginal Revenue

Marginal revenue for a firm with downward-sloping demand:

$$MR(Q) = \frac{d(TR)}{dQ} = P(Q) + P'(Q)\cdot Q$$

For our linear inverse demand $P = P_{\text{avg}} + \dfrac{1}{Nb} - \dfrac{Q}{Sb}$:

$$MR(Q) = P - \frac{Q}{Sb}$$

> [!important] Geometric fact
> For a linear demand $P = a - bQ$, MR is also linear but with **double the slope**: $MR = a - 2bQ$. MR lies strictly *below* demand.

> [!tip] Intuition
> Selling one more unit earns $P(Q)$ **but** also forces the price down on every unit sold ($P'(Q)\cdot Q < 0$). Net marginal revenue is therefore less than price.

#### Notes
> [!note]- Your notes
> *

---

### Slide 18 — Supply: Production and Cost

$$TC(Q) = F + cQ$$

| Term | Meaning |
|---|---|
| $F$ | Fixed cost |
| $c$ | Constant marginal cost |
| $AC(Q) = \dfrac{TC}{Q} = \dfrac{F}{Q} + c$ | Average cost (declining in $Q$) |
| $MC(Q) = c$ | Marginal cost (constant) |

> [!important] Internal economies of scale
> $AC(Q) \downarrow$ as $Q \uparrow$ because the fixed cost $F$ is spread over more units. This is what makes market size matter.

#### Notes
> [!note]- Your notes
> *

---

### Slide 19 — The Monopolist's Problem

Each firm acts like a monopolist over its own variety. Profit is maximized where:

$$MR(Q) = MC(Q) = c$$

This pins down the firm's optimal quantity $Q^*$ and, via the demand curve, its optimal price $P^*$.

#### Notes
> [!note]- Your notes
> *

---

### Slide 20 — Solving MR = MC → The PP Curve

Setting MR = MC and imposing symmetry $Q = S/N$:

$$MR = P - \frac{Q}{Sb} = P - \frac{S/N}{Sb} = P - \frac{1}{Nb}$$

Setting this equal to $c$:

$$P - \frac{1}{Nb} = c \;\Longrightarrow\; \boxed{\,P = c + \frac{1}{Nb}\quad \text{(PP Curve)}\,}$$

> [!warning] Key result
> Under monopolistic competition $P \neq MC$. There's a wedge.

#### Notes
> [!note]- Your notes
> *

---

### Slide 21 — Markup

The **markup** is the gap between price and marginal cost:

$$\text{markup} = P - c = \frac{1}{Nb}$$

> [!tip] Comparative statics
> - **Higher $b$** (more substitutable products) → lower markup.
> - **Higher $N$** (more competitors) → lower markup.
> - As $N \to \infty$, markup $\to 0$ (approaches perfect competition).
> - When $N = 1$ (monopoly), markup $= \dfrac{1}{b}$.

#### Notes
> [!note]- Your notes
> *

---

### Slide 22 — Supply: Free Entry and Average Cost

Since $Q = S/N$ in symmetric equilibrium:

$$AC(Q) = \frac{TC(Q)}{Q} = \frac{F + Qc}{Q} = \frac{F}{Q} + c = \frac{FN}{S} + c$$

> [!info] Reading the formula
> - Bigger $N$ → higher AC for each firm (each produces less, so fixed cost is spread more thinly).
> - Bigger $S$ (market size) → lower AC (each firm produces more and exploits scale).

#### Notes
> [!note]- Your notes
> *

---

### Slide 23 — Free Entry → The CC Curve

Profit: $\pi(Q) = P\cdot Q - AC \cdot Q = (P - AC)\cdot Q$

With **free entry**, firms enter until profits are driven to zero:

$$\pi = 0 \iff P = AC$$

Combining with $AC = \dfrac{FN}{S} + c$:

$$\boxed{\,P = \frac{FN}{S} + c\quad \text{(CC Curve)}\,}$$

#### Notes
> [!note]- Your notes
> *

---

### Slide 24 — Free Entry (Graph, Positive Profits Case)

> [!example] When profits > 0
> At $P^* > AC$, the shaded rectangle $(P^* - AC)\cdot Q^*$ represents per-firm profit. New firms are attracted into the industry.

Entry shifts the **incumbent firm's demand curve left** (shrinking market share), which:
1. Reduces the price markup
2. Reduces efficiency (increases $AC(Q^*)$)
3. Reduces profit

#### Notes
> [!note]- Your notes
> *

---

### Slide 25 — Monopolistic Competition Long-Run Equilibrium

Firms enter until **economic profit = 0**.

> [!important] Long-run properties
> - Firms earn **zero profit**
> - Firms still set $P > MC$ (positive markup, but fully absorbed by average fixed-cost coverage)
> - Demand is tangent to AC at the equilibrium quantity

#### Notes
> [!note]- Your notes
> *

---

### Slide 26 — Plan Recap

Section transition: moving into equilibrium analysis (intersection of PP and CC).

#### Notes
> [!note]- Your notes
> *

---

### Slide 27 — Autarky Equilibrium

Intersection of PP and CC determines $(N^*, P^*)$:

$$P^* = c + \frac{1}{N^* b} = \frac{FN^*}{S} + c$$

Solving:

$$(N^*)^2 = \frac{S}{bF} \;\Longrightarrow\; \boxed{\,N^* = \sqrt{\frac{S}{bF}},\quad P^* = \sqrt{\frac{F}{Sb}} + c\,}$$

> [!tip] Reading the PP–CC diagram
> - **PP** slopes **down** in $(N, P)$ space: more firms → tougher competition → lower markup → lower price.
> - **CC** slopes **up**: more firms → each produces less → higher AC → higher break-even price.
> - Intersection is the unique zero-profit monopolistically competitive equilibrium.

#### Notes
> [!note]- Your notes
> * What we're trying to say in the graph is "hey", what if we're in a situ where insufficent of firms : $x<n^*$
> * Well the average cost will be equal to $AC^*=P^*$, here arrives a gap where there's a price that exceeds average cost
> * So people are enjoying positive profits, but this leaves room for people to join the market
> * The inverse also applies when there are too many firms and the price now agrees with costs exceeding profits 

---

### Slide 28 — Autarky Equilibrium: Stability

- At $N_1 < N^*$: $P > AC$, positive profits → firms **enter**.
- Entry increases competition, lowers $P$, raises $AC$ per firm.
- Entry erodes profits until $N = N^*$.
- Symmetric logic for $N_3 > N^*$: losses → exit.

#### Notes
> [!note]- Your notes
> * Now we're ready to talk about trade. 
> * Both curves would be effected due to change in marginal cost 
> * Suppose we made that move and then another move will be made to zero profits, this model is then limited for the intermediate dynamics of this
> * 

---

### Slide 29 — Key Results Recap

> [!important] Cheat sheet (autarky)
> - Demand: $Q_D = S\!\left[\dfrac{1}{N} - b(P - \bar{P})\right]$
> - Cost: $TC = F + cQ$
> - Symmetric quantity: $Q = S/N$
> - PP: $P = c + \dfrac{1}{Nb}$
> - CC: $AC = \dfrac{NF}{S} + c$
> - Equilibrium: $N^* = (S/bF)^{1/2}$

#### Notes
> [!note]- Your notes
> *

---

### Slide 30 — Trade Equilibrium: CC Shifts Down

When Home opens to Foreign, the **relevant market size grows** to $S^W = S + S^*$.

- **PP unchanged**: $P = c + 1/(Nb)$ doesn't depend on $S$.
- **CC shifts down**: $AC = \dfrac{NF}{S}\! +\! c$ falls for every $N$ because $S$ grew.

Graphically the new CC₂ lies below CC₁, intersecting PP at a lower $P$ and higher $N$.

#### Notes
> [!note]- Your notes
> *

---

### Slide 31 — Two Effects of Opening to Trade

> [!important] The two welfare-raising effects
> 1. **Variety-enhancing effect** — equilibrium $N$ **rises**. Consumers get access to more varieties.
> 2. **Pro-competitive effect** — equilibrium $P$ **falls**. Larger market → more firms can cover fixed costs → more competition → thinner markups. Some firms exit (those who had negative profits after integration).
>
> Because consumers **value variety**, trade increases welfare unambiguously in this model.

#### Notes
> [!note]- Your notes
> *

---

### Slide 32 — More Trade Equilibrium Implications

2. Total world firms **> either country's autarky count** *but* **< the sum of the two autarkies**. Some firms shut down.
3. Each surviving firm **produces more**: $Q = S/N = (SbF)^{1/2}$ ⇒ rises with $S$.
4. Each firm has **lower AC** — they're exploiting economies of scale they couldn't access in the smaller autarky market.

#### Notes
> [!note]- Your notes
> *

---

### Slide 33 — Plan Recap

Section transition: worked numerical example.

#### Notes
> [!note]- Your notes
> *

---

### Slide 34 — Example: Setup

Automobile industry, two countries:

| Parameter | Home | Foreign |
|---|---|---|
| Market size $S$ | 900,000 | 1,600,000 |
| Substitutability $b$ | 1/30,000 | 1/30,000 |
| Fixed cost $F$ | \$750,000,000 | \$750,000,000 |
| Marginal cost $c$ | \$5,000 | \$5,000 |

**Questions:** (1) autarky $N$ and $P$ in each country; (2) integrated-market $N^W$ and $P^W$ under free trade.

#### Notes
> [!note]- Your notes
> *

---

### Slide 35 — Example: Demand and Cost Structure

Residual demand at each producer:

$$Q = 900{,}000\!\left[\frac{1}{N} - \frac{P - P_{\text{avg}}}{30{,}000}\right],\qquad Q^* = 1{,}600{,}000\!\left[\frac{1}{N^*} - \frac{P^* - P^*_{\text{avg}}}{30{,}000}\right]$$

Average cost (same both countries):

$$AC(Q) = \frac{F + Qc}{Q} = \frac{750{,}000{,}000}{Q} + 5{,}000$$

#### Notes
> [!note]- Your notes
> *

---

### Slide 36 — Example: Autarky Numbers

**Home:**
$$N = \sqrt{\frac{S}{bF}} = \sqrt{\frac{900{,}000}{750{,}000{,}000 \cdot 1/30{,}000}} = 6$$
$$P = c + \frac{1}{Nb} = 5{,}000 + \frac{1}{6\cdot 1/30{,}000} = \$10{,}000$$

**Foreign:**
$$N^* = \sqrt{\frac{1{,}600{,}000}{750{,}000{,}000\cdot 1/30{,}000}} = 8$$
$$P^* = 5{,}000 + \frac{1}{8\cdot 1/30{,}000} = \$8{,}750$$

#### Notes
> [!note]- Your notes
> *

---

### Slide 37 — Example: Autarky Comparison

| | **Home** (before trade) | **Foreign** (before trade) |
|---|---|---|
| Total sales of autos | 900,000 | 1,600,000 |
| Number of firms | 6 | 8 |
| Sales per firm | 150,000 | 200,000 |
| Average cost | \$10,000 | \$8,750 |
| Price | \$10,000 | \$8,750 |

> [!tip] Pattern
> **Larger market → lower price, more variety, higher output per firm.** This is already a preview of why trade helps.

#### Notes
> [!note]- Your notes
> *

---

### Slide 38 — Example: Free Trade

Integrated market: $S^W = 900{,}000 + 1{,}600{,}000 = 2{,}500{,}000$.

$$N^W = \sqrt{\frac{2{,}500{,}000}{750{,}000{,}000\cdot 1/30{,}000}} = 10$$
$$P^W = 5{,}000 + \frac{1}{10\cdot 1/30{,}000} = \$8{,}000$$

> [!info] Observations
> - World firm count: **10**, down from 6 + 8 = **14**. Four firms exit.
> - But both countries now access **10 varieties** (versus 6 or 8 before). Everyone gets more variety.
> - Price falls to **\$8,000** for consumers in **both** countries.

#### Notes
> [!note]- Your notes
> *

---

### Slide 39 — Example: Summary

| | Home (autarky) | Foreign (autarky) | Integrated (trade) |
|---|---|---|---|
| Total sales | 900,000 | 1,600,000 | 2,500,000 |
| Number of firms | 6 | 8 | **10** |
| Sales per firm | 150,000 | 200,000 | **250,000** |
| Average cost | \$10,000 | \$8,750 | **\$8,000** |
| Price | \$10,000 | \$8,750 | **\$8,000** |

> [!important] Takeaways
> - Free trade **raises welfare in both countries** (lower prices + more variety).
> - Some firms shut down as a result of trade (4 in this example).

#### Notes
> [!note]- Your notes
> *

---


# Lecture 6 — New Trade Theory Part II

> [!abstract] Focus of this lecture
> Review the Lecture 5 model, then pivot to (a) **empirical evidence** on gains from variety and intra-industry trade, and (b) **redistribution effects** — who wins and who loses from trade under monopolistic competition.

---

### Slide 1 — Title

**Topic:** New Trade Theory: Part II.

#### Notes
> [!note]- Your notes
> *

---

### Slide 2 — Plan for Today

Review → Empirical Evidence → Redistribution Effects.

#### Notes
> [!note]- Your notes
> *

---

### Slide 3 — Review of the New Trade Theory

In a market of size $S$ with $N$ monopolistically competitive firms:

| Building block | Formula |
|---|---|
| Demand (typical firm) | $Q_D = S\!\left[\dfrac{1}{N} - b(P - \bar{P})\right]$ |
| Cost (typical firm) | $TC = F + cQ$ |
| Symmetric output | $Q = S/N$ |
| **PP Curve** | $P = c + \dfrac{1}{Nb}$ |
| **CC Curve** | $AC = \dfrac{NF}{S} + c$ |
| **Equilibrium $N$** | $N = (S/bF)^{1/2}$ |

#### Notes
> [!note]- Your notes
> *

---

### Slide 4 — Autarky Equilibrium

Intersection of PP and CC yields:

$$P^* = c + \frac{1}{N^* b} = \frac{F N^*}{S} + c \;\Longrightarrow\; (N^*)^2 = \frac{S}{bF}$$

> [!tip] Geometric intuition
> - PP: downward-sloping (more firms → more competition → lower price)
> - CC: upward-sloping (more firms → each produces less → higher AC → higher break-even price)

#### Notes
> [!note]- Your notes
> *

---

### Slide 5 — Trade Equilibrium

Opening to trade effectively **enlarges $S$** (from domestic to integrated market size).

> [!important] Two effects of opening to trade
> 1. **Variety-enhancing:** equilibrium $N$ rises.
> 2. **Pro-competitive:** equilibrium $P$ falls (some firms exit because they now earn negative profits at the new, lower equilibrium price).
>
> Because consumers value variety, **trade increases welfare**.

#### Notes
> [!note]- Your notes
> *

---

### Slide 6 — Example Summary (Gains from Market Integration)

| | Home (before) | Foreign (before) | Integrated (after) |
|---|---|---|---|
| Total sales of autos | 900,000 | 1,600,000 | 2,500,000 |
| Number of firms | 6 | 8 | 10 |
| Sales per firm | 150,000 | 200,000 | 250,000 |
| Average cost | \$10,000 | \$8,750 | \$8,000 |
| Price | \$10,000 | \$8,750 | \$8,000 |

> [!important] Two core takeaways
> - Free trade **raises welfare in both countries**: consumers get greater variety at lower prices.
> - Some firms **shut down** as a result of trade (14 → 10 in this example).

#### Notes
> [!note]- Your notes
> *

---

### Slide 7 — Plan Recap

Moving into empirical evidence.

#### Notes
> [!note]- Your notes
> *

---

### Slide 8 — Empirical Evidence: Variety Gains

> [!example] Broda and Weinstein (2006)
> The welfare gain to U.S. consumers from increased **import variety** between 1972 and 2001 is equivalent to **2.6% higher GDP in 2001**. Core finding: more varieties available = higher consumer welfare, and NTT's variety channel is quantitatively important.

> [!example] Goldberg et al. (2010)
> India's **trade liberalization** (1990s reforms) led to a big rise in the variety of goods produced by Indian firms. **31% of the increase** came from access to new **imported intermediate input varieties** — showing that NTT's variety mechanism operates in production inputs too, not just final consumer goods.

#### Notes
> [!note]- Your notes
> *

---

### Slide 9 — Empirical Evidence: Intra-Industry Trade Indices (U.S., 1993)

Higher index ⇒ more two-way (intra-industry) trade in that category.

| Industry | IIT Index |
|---|---|
| Inorganic chemicals | 0.99 |
| Power-generating machinery | 0.97 |
| Electrical machinery | 0.96 |
| Organic chemicals | 0.91 |
| Medical and pharmaceutical | 0.86 |
| Office machinery | 0.81 |
| Telecommunications equipment | 0.69 |
| Road vehicles | 0.65 |
| Iron and steel | 0.43 |
| Clothing and apparel | 0.27 |
| Footwear | 0.00 |

#### Notes
> [!note]- Your notes
> *

---

### Slide 10 — Variation Across Sectors

> [!tip] Where does intra-industry trade dominate?
> - **High IIT:** sophisticated manufactured goods — pharmaceuticals, autos, chemicals, specialized machinery, precision instruments, telecom equipment. These are exactly the industries where product differentiation + economies of scale are strong, as predicted by NTT.
> - **Low IIT:** labor-intensive goods (clothing, footwear, food) and industries tied to local raw materials (oil, diamonds, iron ore). These look more like the Heckscher–Ohlin world of comparative advantage.

> [!info] Interpretation
> NTT and [[Hecksher-Ohlin Model|H–O]] are **complements, not substitutes**. Different industries fit different models.

#### Notes
> [!note]- Your notes
> *

---

### Slide 11 — Redistributive Effects

> [!question] Who gains and who loses from trade?
> - In the [[Hecksher-Ohlin Model|Heckscher-Ohlin Model]], **inter-industry** trade created clear winners and losers (the scarce factor lost; Stolper–Samuelson).
> - In the monopolistic competition model, **all consumers benefit** from trade (perhaps some more than others depending on love of variety).
> - **Firms** bear the adjustment: some will shut down because they can no longer cover fixed costs in the tougher integrated market.

> [!warning] Policy relevance
> NTT says the **average** consumer gains from trade, but real-world adjustment is costly for laid-off workers at exiting firms. Welfare gains ≠ Pareto improvements without compensating transfers.

#### Notes
> [!note]- Your notes
> *

---


# Techniques — Problem ▸ Inputs ▸ Operation ▸ Output

> [!abstract] How to read this section
> Each technique below is an analytical move that shows up in NTT. Each entry follows the same four-part template:
>
> - **Problem** — the question the tool is designed to answer.
> - **Inputs** — what you need in hand *before* you can apply it.
> - **Operation** — the transformation or derivation you perform.
> - **Output** — the information or object you walk away with.
>
> Use this section as a **reverse lookup**: when you're handed a problem, match it to a technique and check that you have the required inputs.

---

## Technique 1 — Deriving Marginal Revenue from a Demand Curve

> [!info] Problem
> The firm's total revenue depends nonlinearly on quantity because **price depends on quantity** (downward-sloping demand). To maximize profit we need the *marginal* return from one more unit sold.

**Inputs**
- An inverse demand function $P = P(Q)$ (price as a function of the firm's own quantity).
- Calculus: product rule.

**Operation**
Differentiate total revenue $TR = P(Q)\cdot Q$ with respect to $Q$:

$$MR(Q) = \frac{d(TR)}{dQ} = \frac{d[P(Q)\cdot Q]}{dQ} = P'(Q)\cdot Q + P(Q)$$

Since $P'(Q) < 0$ for downward-sloping demand, the first term is negative, so $MR(Q) < P(Q)$ — marginal revenue lies *below* demand.

**Output**
A function $MR(Q)$ that tells you, at each quantity level, the *net* revenue gained by selling one more unit. **Used as input for Technique 4 (MR = MC).**

> [!tip] Shortcut for linear demand
> If $P = a - bQ$, then $MR = a - 2bQ$ — same intercept, *double the slope*.

---

## Technique 2 — Inverting Residual Demand into Price Form

> [!info] Problem
> Demand is given as $Q$ as a function of $P$, but monopoly/monopolistic-competition analysis needs $P$ as a function of $Q$ to take the derivative for MR.

**Inputs**
- Residual demand $Q = S\!\left[\dfrac{1}{N} - b(P - P_{\text{avg}})\right]$.
- Treated as given: $S$, $N$, $b$, $P_{\text{avg}}$.

**Operation**
Algebraic rearrangement — solve for $P$:

$$
\begin{aligned}
Q &= \frac{S}{N} - Sb\,P + Sb\,P_{\text{avg}}\\
Sb\,P &= \frac{S}{N} - Q + Sb\,P_{\text{avg}}\\
P &= \frac{1}{Nb} - \frac{Q}{Sb} + P_{\text{avg}}\\[2pt]
P &= P_{\text{avg}} + \frac{1}{Nb} - \frac{Q}{Sb}
\end{aligned}
$$

**Output**
Inverse demand curve $P(Q) = P_{\text{avg}} + \dfrac{1}{Nb} - \dfrac{Q}{Sb}$. The slope $-\dfrac{1}{Sb}$ is the key object — it governs how steeply price falls as the firm expands.

---

## Technique 3 — Symmetry Reduction

> [!info] Problem
> The model has lots of variables per firm ($P$, $Q$, $P_{\text{avg}}$). Tracking them individually is hopeless. We want industry-level equations.

**Inputs**
- The assumption that all firms are **identical** (same cost, same technology, same demand).
- Residual demand equation.

**Operation**
In any symmetric equilibrium, every firm chooses the same price, so $P = P_{\text{avg}}$. Substitute this into the demand equation:

$$Q = S\!\left[\frac{1}{N} - b\underbrace{(P - P_{\text{avg}})}_{=\,0}\right] = \frac{S}{N}$$

**Output**
- Each firm's equilibrium quantity: $Q = S/N$.
- A massive simplification: the entire model can now be described by just two variables, $N$ and $P$.

> [!tip] Why this works
> Symmetry is an equilibrium *selection* assumption. With identical firms, any asymmetric outcome is unstable — a firm charging more loses share, a firm charging less gets crushed on margins. The symmetric fixed point is the only stable one.

---

## Technique 4 — MR = MC: Deriving the PP Curve

> [!info] Problem
> Each firm chooses its price (equivalently, its output) to maximize profit. What relationship must hold between **price $P$** and **number of firms $N$** at the optimum?

**Inputs**
- Marginal revenue: $MR(Q) = P - \dfrac{Q}{Sb}$ (from Technique 1 applied to our inverse demand).
- Marginal cost: $MC = c$ (from $TC = F + cQ$).
- Symmetric quantity: $Q = S/N$ (from Technique 3).

**Operation**
Set $MR = MC$ and substitute $Q = S/N$:

$$P - \frac{Q}{Sb} = c \;\Longrightarrow\; P - \frac{S/N}{Sb} = c \;\Longrightarrow\; P - \frac{1}{Nb} = c$$

**Output**

$$\boxed{\,P = c + \frac{1}{Nb}\quad \text{(PP Curve)}\,}$$

A downward-sloping curve in $(N, P)$ space. **Interpretation:** the more firms in the industry, the lower the price each firm can profitably charge, because competition shrinks each firm's market power and markup.

---

## Technique 5 — Zero-Profit Free Entry: Deriving the CC Curve

> [!info] Problem
> Under free entry, firms enter whenever profits are positive and exit when they're negative. In long-run equilibrium, **profits must be zero**. What relationship does this impose between $P$ and $N$?

**Inputs**
- Average cost: $AC(Q) = \dfrac{F}{Q} + c$ (from dividing $TC = F + cQ$ by $Q$).
- Symmetric quantity: $Q = S/N$.
- Profit: $\pi = (P - AC)\cdot Q$.
- Zero-profit condition: $\pi = 0 \iff P = AC$.

**Operation**
Substitute $Q = S/N$ into $AC$, then impose $P = AC$:

$$AC = \frac{F}{Q} + c = \frac{F}{S/N} + c = \frac{FN}{S} + c$$

Zero-profit condition:

$$P = AC = \frac{FN}{S} + c$$

**Output**

$$\boxed{\,P = \frac{FN}{S} + c\quad \text{(CC Curve)}\,}$$

An upward-sloping curve in $(N, P)$ space. **Interpretation:** the more firms, the smaller each firm's output, the higher its average cost, and therefore the higher the price needed just to break even.

---

## Technique 6 — Solving the PP–CC System: Finding Equilibrium $(N^*, P^*)$

> [!info] Problem
> The PP curve says what firms *want* to charge given entry; the CC curve says what they *must* charge to survive. Equilibrium is where both hold.

**Inputs**
- PP: $P = c + \dfrac{1}{Nb}$
- CC: $P = \dfrac{FN}{S} + c$

**Operation**
Set PP = CC, cancel $c$ from both sides, cross-multiply:

$$\frac{1}{Nb} = \frac{FN}{S} \;\Longrightarrow\; S = FbN^2 \;\Longrightarrow\; N^2 = \frac{S}{bF}$$

**Output**

$$\boxed{\,N^* = \sqrt{\frac{S}{bF}},\qquad P^* = c + \sqrt{\frac{F}{Sb}}\,}$$

**Comparative statics embedded in this formula:**
- $S \uparrow \Rightarrow N^* \uparrow$ and $P^* \downarrow$ — **bigger markets have more variety and lower prices**.
- $b \uparrow$ (more substitutable) $\Rightarrow N^* \downarrow$ and $P^* \downarrow$.
- $F \uparrow$ (higher fixed cost) $\Rightarrow N^* \downarrow$ (fewer firms can cover fixed costs) and $P^* \uparrow$.

---

## Technique 7 — Comparative Statics in $S$: Trade as Market Enlargement

> [!info] Problem
> How does opening up to international trade change the equilibrium? In this model, trade = enlargement of the relevant market size $S$.

**Inputs**
- Autarky equilibrium: $N^* = \sqrt{S/bF}$, $P^* = c + \sqrt{F/(Sb)}$.
- Trade shock: $S \to S^W = S_{\text{Home}} + S_{\text{Foreign}}$.
- Same $b$, $F$, $c$ in both countries (by assumption).

**Operation**
Substitute new $S^W$ into the equilibrium formulas:

$$N^{W} = \sqrt{\frac{S^W}{bF}} > N^*_{\text{each country}},\qquad P^{W} = c + \sqrt{\frac{F}{S^W b}} < P^*_{\text{each country}}$$

**Output**
Two simultaneous effects of trade:

| Effect | Direction | Why |
|---|---|---|
| **Variety-enhancing** | $N \uparrow$ | Larger market supports more firms at zero profits |
| **Pro-competitive** | $P \downarrow$ | CC shifts down → each firm on a flatter AC → lower equilibrium price |

Plus a secondary result: per-firm output $Q = S/N = \sqrt{SbF}$ **rises** — each surviving firm exploits scale economies more fully.

> [!tip] Key graphical move
> Only **CC shifts** (down) when $S$ rises; **PP is unchanged** because the pricing formula $P = c + 1/(Nb)$ doesn't depend on $S$ directly.

---

## Technique 8 — Markup Analysis

> [!info] Problem
> How much market power do firms have, and what determines it?

**Inputs**
- PP curve: $P = c + 1/(Nb)$.
- Definition: markup = $P - MC = P - c$.

**Operation**
Substitute PP into the markup definition:

$$\text{markup} = P - c = \frac{1}{Nb}$$

**Output**
- Markup is $\dfrac{1}{Nb}$, decreasing in both $N$ (more competitors) and $b$ (more substitutability).
- **Limits:**
  - $N \to \infty \Rightarrow \text{markup} \to 0$ (perfect competition).
  - $N = 1 \Rightarrow \text{markup} = 1/b$ (pure monopoly).
- **Policy reading:** trade integration lowers markups via the pro-competitive channel.

---

## Technique 9 — Welfare Analysis under Monopolistic Competition

> [!info] Problem
> Does opening to trade make people better off? Can we characterize winners and losers?

**Inputs**
- Trade equilibrium results from Technique 7.
- Assumption: consumers have **love of variety** (CES-style preferences implicit in the demand structure).

**Operation**
Decompose the welfare change into two channels:

1. **Variety channel:** $N$ rises → more products available → direct utility gain from variety.
2. **Price channel:** $P$ falls → lower cost of consumption → real income rises.

Then identify who bears adjustment costs: firms that exit (and their workers).

**Output**
- **All consumers gain** (some more than others depending on how strongly they value variety).
- **Some firms lose** (they shut down; 14 → 10 firms in the worked example).
- Unlike [[Hecksher-Ohlin Model|Heckscher-Ohlin Model]]'s Stolper–Samuelson result, **there is no systematic factor-of-production loser** in this model — the distributional story runs on the firm/worker rather than factor-ownership axis.

> [!warning] What the model leaves out
> Adjustment costs, unemployment, imperfect labor mobility between exiting and surviving firms. These are where real-world politics lives.

---

## Technique 10 — Intra-Industry Trade Index (Empirical Tool)

> [!info] Problem
> We want to quantify, for a given industry, **how much** trade is intra-industry (two-way trade in similar differentiated products) versus inter-industry (one-way exchange of fundamentally different goods).

**Inputs**
- Bilateral industry-level trade data: value of **imports** $M$ and **exports** $X$ in a given industry.

**Operation**
Compute the Grubel–Lloyd-style index:

$$\text{IIT} = 1 - \frac{|X - M|}{X + M}$$

- If $X = M$: IIT = 1 (pure intra-industry trade).
- If $X = 0$ or $M = 0$: IIT = 0 (pure inter-industry trade).

**Output**
A number in $[0, 1]$ per industry:
- **High IIT** (>0.8 for pharmaceuticals, inorganic chemicals, power-generating machinery) → industry fits **NTT's monopolistic competition** story.
- **Low IIT** (footwear ≈ 0, men's shorts ≈ 0.02, iron and steel ≈ 0.43) → industry fits **H–O comparative advantage** story better.

> [!tip] Practical use
> IIT indices let you sort industries into the appropriate theoretical framework empirically, rather than having to pick one model to govern all trade.

---


# Master Formula Sheet

> [!important] Everything you need for the exam on one page

| # | Object | Formula |
|---|---|---|
| 1 | Residual demand | $Q = S\!\left[\dfrac{1}{N} - b(P - P_{\text{avg}})\right]$ |
| 2 | Inverse demand | $P = P_{\text{avg}} + \dfrac{1}{Nb} - \dfrac{Q}{Sb}$ |
| 3 | Demand slope | $\dfrac{dP}{dQ} = -\dfrac{1}{Sb}$ |
| 4 | Marginal revenue | $MR = P - \dfrac{Q}{Sb}$ |
| 5 | Symmetric output | $Q = S/N$ |
| 6 | Total cost | $TC = F + cQ$ |
| 7 | Average cost | $AC = \dfrac{F}{Q} + c = \dfrac{FN}{S} + c$ |
| 8 | Marginal cost | $MC = c$ |
| 9 | **PP curve** | $P = c + \dfrac{1}{Nb}$ |
| 10 | **CC curve** | $P = \dfrac{FN}{S} + c$ |
| 11 | Markup | $P - c = \dfrac{1}{Nb}$ |
| 12 | **Equilibrium $N$** | $N^* = \sqrt{\dfrac{S}{bF}}$ |
| 13 | **Equilibrium $P$** | $P^* = c + \sqrt{\dfrac{F}{Sb}}$ |
| 14 | Equilibrium $Q$ (per firm) | $Q^* = \sqrt{SbF}$ |
| 15 | Trade market size | $S^W = S_{\text{Home}} + S_{\text{Foreign}}$ |
| 16 | IIT index (empirical) | $\text{IIT} = 1 - \dfrac{|X - M|}{X + M}$ |

---

# Glossary of Symbols

| Symbol | Meaning | Unit / Range |
|---|---|---|
| $S$ | Total industry sales (market size) | units |
| $N$ | Number of firms in the industry | positive integer |
| $Q$ | Output of the representative firm | units |
| $P$ | Price charged by the representative firm | \$ / unit |
| $P_{\text{avg}}$ (or $\bar{P}$) | Average industry price | \$ / unit |
| $b$ | Substitutability parameter | > 0 |
| $F$ | Fixed cost per firm | \$ |
| $c$ | Constant marginal cost | \$ / unit |
| $AC$ | Average cost | \$ / unit |
| $MC$ | Marginal cost | \$ / unit |
| $MR$ | Marginal revenue | \$ / unit |
| $TC$ | Total cost | \$ |
| $TR$ | Total revenue | \$ |
| $\pi$ | Profit | \$ |
| $^*$ superscript | Equilibrium value (e.g. $N^*$) | — |
| $^W$ superscript | World / integrated market (e.g. $S^W$) | — |
| Foreign $^*$ | Foreign-country version of a variable (e.g. $S^*$) | — |

---

# Related Notes

- [[Ricardian Model]]
- [[Hecksher-Ohlin Model|Heckscher-Ohlin Model]]
- [[Stolper-Samuelson Theorem]]
- [[Economies of Scale]]
- [[Monopolistic Competition]]
- [[Intra-Industry Trade]]

---

# Key Papers / Further Reading

- **Krugman, P. (1980)** — "Scale economies, product differentiation, and the pattern of trade." *American Economic Review*. The paper that started it all.
- **Broda, C. and D. Weinstein (2006)** — "Globalization and the gains from variety." *Quarterly Journal of Economics*. Quantifies variety gains for U.S. consumers.
- **Goldberg, P., A. Khandelwal, N. Pavcnik, and P. Topalova (2010)** — "Imported intermediate inputs and domestic product growth: evidence from India." *Quarterly Journal of Economics*. Shows NTT's variety mechanism operates through imported inputs.

---

> [!tip] How to use this note in Obsidian
> - Fold any slide's **Notes** callout to keep the page scannable.
> - Add your own observations under each `#### Notes` heading — the `> [!note]-` callout starts collapsed, so extra text won't clutter the page.
> - The `tags:` in the frontmatter will populate Obsidian's tag pane; click any of them to see all related notes in your vault.
> - Backlinks (`[[...]]`) will surface this note whenever you reference New Trade Theory, Krugman, or monopolistic competition elsewhere.