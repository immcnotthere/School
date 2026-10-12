---
parent: "[[ECON 140]]"
aliases: [Econ140 Lecture 3, Ricardian Model Part II]
tags: [econ140, lecture, ricardian-model]
course: "ECON 140"
instructor: Gueyon Kim (UCSC)
date: 
type: lecture
domain: econ
status: draft
---

# Econ140 – Lecture 3: The Ricardian Model, Part II

**Today's plan:**
1. Review: Assumptions, [[Relative Supply|RS]]/[[Relative Demand|RD]], [[Autarky]] equilibrium, practice example
2. Trade Equilibrium: World RS, World RD, practice examples
3. [[Gains from Trade]]

**Previous lecture:** [[Econ140 - Lecture 2 - Ricardian Model Part I]]

---

## Slide: Review — Ricardian Model Assumptions

World with two goods (Wine, Clothing) and two countries (Home, Foreign):

| Assumption | Details |
|---|---|
| Single factor | Labor only |
| Fixed labor | $L$ per country, constant |
| Constant returns to scale | Linear [[Production Possibility Frontier\|PPF]] |
| Technology differences | [[Unit Labor Requirement\|unit labor requirements]] $a_{LC}, a_{LW}$ |
| Competitive markets | Price/wage takers; workers mobile across sectors |

> 📌 See [[Ricardian Model]] for full model overview.

### Notes
<!-- space for your notes -->

---

## Slide: Review — PPF Example

*Given:* 100 workers, $a_{LC} = 0.5$, $a_{LW} = 0.2$

- Max clothing ($Q_C^{max}$) = $100/0.5 = 200$
- Max wine ($Q_W^{max}$) = $100/0.2 = 500$
- Connect intercepts → linear PPF, slope = $-0.5/0.2 = -2.5$

### Notes
<!-- space for your notes -->

---

## Slide: Autarky Equilibrium — Review

The only relative price consistent with autarky equilibrium in the [[Ricardian Model]] is:
$$\left(\frac{P_C}{P_W}\right)^{autarky} = \frac{a_{LC}}{a_{LW}} = \text{slope of PPF}$$

The [[Relative Supply|RS]] curve is flat at this value. [[Relative Demand|Relative demand]] determines only the quantity mix (where on the RS curve the equilibrium sits).

### Notes
<!-- space for your notes -->

---

## Slide: Autarky Example (Full Solution)

*Given:* $a_{LC} = 2$, $a_{LW} = 4$, $L$ workers, relative demand $= \frac{1}{D_C/D_W}$

**Step 1 — Autarky price:**
$$\frac{P_C}{P_W} = \frac{a_{LC}}{a_{LW}} = \frac{2}{4} = 0.5$$

**Step 2 — Production quantities (RS = RD in equilibrium):**
$$0.5 = \frac{1}{D_C/D_W} = \frac{D_W}{D_C} \implies D_C = 2D_W$$

Substitute into PPF ($2Q_C + 4Q_W = L$), and use $Q_C = D_C$, $Q_W = D_W$ (autarky):
$$2(2D_W) + 4D_W = L \implies 8D_W = L \implies D_W = Q_W = \frac{L}{8}, \quad D_C = Q_C = \frac{L}{4}$$

**Graph:** RS is flat at 0.5; RD intersects at $Q_C/Q_W = 2$.

### Notes
<!-- space for your notes -->

---

## Slide: Introducing the Second Country (Foreign)

| | Labor | Clothing | Wine |
|---|---|---|---|
| Home | $L$ | $a_{LC}$ | $a_{LW}$ |
| Foreign | $L^*$ | $a_{LC}^*$ | $a_{LW}^*$ |

**Key assumption for the analysis:**
$$\frac{a_{LC}^*}{a_{LW}^*} > \frac{a_{LC}}{a_{LW}}$$

→ Foreign's autarky price of clothing is **higher** than Home's → **Home has [[Comparative Advantage]] in clothing, Foreign has CA in wine.**

Note: the level of productivity (absolute advantage) does not determine trade patterns.

### Notes
<!-- space for your notes -->

---

## Slide: What This Assumption Means

$$\frac{a_{LC}^*}{a_{LW}^*} > \frac{a_{LC}}{a_{LW}} \iff \frac{a_{LW}^*}{a_{LC}^*} < \frac{a_{LW}}{a_{LC}}$$

| Direction | Interpretation |
|---|---|
| $\frac{a_{LC}^*}{a_{LW}^*} > \frac{a_{LC}}{a_{LW}}$ | Relative cost of clothing *higher* in Foreign → relative price of clothing higher in Foreign → Home has CA in clothing |
| $\frac{a_{LW}^*}{a_{LC}^*} < \frac{a_{LW}}{a_{LC}}$ | Relative cost of wine *lower* in Foreign → Foreign has CA in wine |

> 📌 CA is determined by **relative** costs, not absolute costs.

### Notes
<!-- space for your notes -->

---

## Slide: Production Patterns at Different World Prices

Let $\left(\frac{P_C}{P_W}\right)^W$ = world relative price of clothing.

| Condition | What happens |
|---|---|
| $\frac{a_{LC}^*}{a_{LW}^*} > \frac{a_{LC}}{a_{LW}} > \left(\frac{P_C}{P_W}\right)^W$ | Both countries produce only wine |
| $= \frac{a_{LC}}{a_{LW}}$ | Foreign produces wine; Home is indifferent |
| $\frac{a_{LC}^*}{a_{LW}^*} > \left(\frac{P_C}{P_W}\right)^W > \frac{a_{LC}}{a_{LW}}$ | **Home specializes in clothing; Foreign in wine** ← typical trade case |
| $= \frac{a_{LC}^*}{a_{LW}^*}$ | Home produces clothing; Foreign is indifferent |
| $\left(\frac{P_C}{P_W}\right)^W > \frac{a_{LC}^*}{a_{LW}^*} > \frac{a_{LC}}{a_{LW}}$ | Both countries produce only clothing |

### Notes
<!-- space for your notes -->

---

## Slide: World Relative Supply — Construction

The World RS is a **two-step staircase**. Three numbers to compute:

| Number | Formula | Meaning |
|---|---|---|
| Lower step height | $\frac{a_{LC}}{a_{LW}}$ | Home's autarky price |
| Vertical segment x-value | $\frac{L/a_{LC}}{L^*/a_{LW}^*}$ | Complete specialization point |
| Upper step height | $\frac{a_{LC}^*}{a_{LW}^*}$ | Foreign's autarky price |

**Complete specialization** ($\frac{Q_C + Q_C^*}{Q_W + Q_W^*} = \frac{L/a_{LC}}{L^*/a_{LW}^*}$): all Home workers in clothing, all Foreign workers in wine.

> 📌 See [[Relative Supply#World Relative Supply (Two Countries)]] for full derivation.

### Notes
<!-- space for your notes -->

---

## Slide: World Relative Demand

Assume consumers in both countries have identical **homothetic preferences**:
- Relative demand doesn't depend on income
- Same RD schedule in both countries
- Under free trade (same world price), both face a **common world relative demand**

The world RD curve slopes **downward** as usual.

> 📌 See [[Relative Demand]] for the income/substitution effects behind the downward slope.

### Notes
<!-- space for your notes -->

---

## Slide: World Equilibrium Conditions

In the free trade equilibrium:
1. Firms maximize profits (production on PPF)
2. Consumers maximize utility (on budget constraint)
3. **World** demand = world supply for each good (key difference from autarky)
4. Each country's labor market clears

> *Main difference from autarky:* in autarky, condition (3) applies country-by-country. Under trade, it applies globally.

### Notes
<!-- space for your notes -->

---

## Slide: Three Types of Trade Equilibria

Combining World RS (staircase) and World RD (downward sloping):

| RD location | Equilibrium price | Specialization |
|---|---|---|
| $RD_1$ (far right / low clothing demand) | At lower step: $P_C/P_W = a_{LC}/a_{LW}$ | Home incompletely specializes |
| $RD_2$ (moderate) | On vertical segment: $a_{LC}/a_{LW} < P < a_{LC}^*/a_{LW}^*$ | **Complete specialization** — Home in clothing, Foreign in wine |
| $RD_3$ (far left / high clothing demand) | At upper step: $P_C/P_W = a_{LC}^*/a_{LW}^*$ | Foreign incompletely specializes |

### Notes
<!-- space for your notes -->

---

## Slide: Example 1 Setup — England and France

| | Labor | $a_{LC}$ | $a_{LW}$ |
|---|---|---|---|
| England (Home) | $L = 100$ | 0.5 | 0.2 |
| France (Foreign) | $L^* = 20$ | 1 | 0.1 |

### Notes
<!-- space for your notes -->

---

## Slide: Example 1, Q1 — Absolute Advantage

- England: $a_{LC} = 0.5 < a_{LC}^* = 1$ → AA in clothing
- France: $a_{LW}^* = 0.1 < a_{LW} = 0.2$ → AA in wine

**England has [[Absolute Advantage]] in clothing; France has AA in wine.**

### Notes
<!-- space for your notes -->

---

## Slide: Example 1, Q2 & Q3 — Autarky Prices & Comparative Advantage

**Autarky prices:**
- England: $\frac{P_C}{P_W} = \frac{0.5}{0.2} = \frac{5}{2} = 2.5$
- France: $\frac{P_C^*}{P_W^*} = \frac{1}{0.1} = 10$

**Comparative advantage:**
- Clothing is relatively cheaper in England ($2.5 < 10$) → **England has CA in clothing**
- Wine is relatively cheaper in France → **France has CA in wine**

Note: France has AA in wine but England has AA in clothing — a case where AA and CA align, but that's coincidental.

### Notes
<!-- space for your notes -->

---

## Slide: Example 1, Q4 — World RS Curve

Three numbers:

| Value | Calculation | Result |
|---|---|---|
| $\frac{L/a_{LC}}{L^*/a_{LW}^*}$ | $\frac{100/0.5}{20/0.1} = \frac{200}{200}$ | **1** |
| $\frac{a_{LC}}{a_{LW}}$ (England autarky price) | $\frac{0.5}{0.2}$ | **2.5** |
| $\frac{a_{LC}^*}{a_{LW}^*}$ (France autarky price) | $\frac{1}{0.1}$ | **10** |

**World RS:** flat at 2.5, vertical at $Q_C/Q_W = 1$, flat at 10.

### Notes
<!-- space for your notes -->

---

## Slide: Example 1, Q5 — Trade Equilibrium

World RD: $\frac{D_C}{D_W} = \frac{5}{P_C/P_W}$

**Step 1:** Find price when $Q_C/Q_W = 1$ (complete specialization point):
$$1 = \frac{5}{P_C/P_W} \implies \frac{P_C}{P_W} = 5$$

**Step 2:** Check: $2.5 < 5 < 10$ ✓ → equilibrium falls on the vertical segment (complete specialization)

**Trade equilibrium:**
$$\left(\frac{P_C}{P_W}\right)^W = 5 \qquad \left(\frac{Q_C}{Q_W}\right)^W = 1$$

> England fully specializes in clothing; France fully specializes in wine.

### Notes
<!-- space for your notes -->

---

## Slide: Example 2 — England AA in Everything

| | Labor | $a_{LC}$ | $a_{LW}$ |
|---|---|---|---|
| England | $L = 100$ | 0.5 | 0.2 |
| France | $L^* = 20$ | **4** | **0.4** |

England now has AA in both goods. Does France still trade? **Yes** — compare CAs:
- England OC of clothing: $0.5/0.2 = 2.5$
- France OC of clothing: $4/0.4 = 10$
- England still has CA in clothing; France still has CA in wine

The pattern of trade is unchanged — absolute advantage is irrelevant to CA.

*Note:* world RS numbers will differ from Example 1.

### Notes
<!-- space for your notes -->

---

## Slide: Gains from Trade — PPF Analysis

With complete specialization ($\frac{a_{LC}^*}{a_{LW}^*} > \left(\frac{P_C}{P_W}\right)^W > \frac{a_{LC}}{a_{LW}}$):

**Home (England):**
- Produces at clothing corner of PPF: $(Q_C, Q_W) = (L/a_{LC}, 0)$
- Trades clothing for wine at world price
- Consumption point lies **outside** Home's autarky PPF → welfare gain

**Foreign (France):**
- Produces at wine corner: $(Q_C^*, Q_W^*) = (0, L^*/a_{LW}^*)$
- Trades wine for clothing at world price
- Consumption point lies **outside** Foreign's autarky PPF → welfare gain

**Both countries reach higher indifference curves than in autarky.**

> 📌 See [[Gains from Trade]] for full analysis.

### Notes
<!-- space for your notes -->

---

## Slide: Gains from Trade — Summary

| | Autarky | Free Trade |
|---|---|---|
| Home produces | Mix of C and W | Only Clothing |
| Home consumes | = Production | More W (via imports), same or more C |
| Foreign produces | Mix of C and W | Only Wine |
| Foreign consumes | = Production | More C (via imports), same or more W |
| World welfare | Lower | **Higher — both countries gain** |

> Key insight: trade allows countries to *consume* beyond their own PPF by specializing and exchanging.

### Notes
<!-- space for your notes -->

---

## Summary

| Concept | Key Result |
|---|---|
| Autarky price | $= a_{LC}/a_{LW}$ (supply-determined) |
| CA condition | $a_{LC}/a_{LW} < a_{LC}^*/a_{LW}^*$ → Home has CA in clothing |
| World RS | Step function with vertical segment at $\frac{L/a_{LC}}{L^*/a_{LW}^*}$ |
| Trade equilibrium | World price between two autarky prices → complete specialization |
| [[Gains from Trade]] | Both countries consume beyond their PPF |

**Next:** Lectures 4–5 continue the Ricardian Model (wages, empirical tests).
