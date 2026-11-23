---
type: problem
parent: "[[ECON 131]]"
domain: econ
course: "ECON 131"
status: draft
date: 2026-10-13
due: 2026-10-13
source: "problem set pasted by Jacob 2026-10-13; method from the Lecture 3 and Lecture 4 handouts"
aliases:
  - "ECON 131 PS2"
  - "ECON 131 homework hedging and PPP"
tags:
  - econ131
  - homework
  - hedging
  - ppp
  - handwritten
uses:
  - "[[Forward Hedge vs Money Market Hedge]]"
  - "[[Transaction Exchange Risk]]"
  - "[[Covered Interest Rate Parity (CIP)]]"
  - "[[Spot vs Forward Contract]]"
  - "[[Appreciation and Depreciation]]"
related:
  - "[[ECON 131 Lecture 3 - Interest Rate Parity (fill-in)]]"
  - "[[ECON 131 Lecture 4 - Purchasing Power Parity]]"
  - "[[ECON 131 W2 Reading - Textbook Ch 3 - Forward Markets and Transaction Exchange Risk]]"
  - "[[ECON 131 W2 Reading - Textbook Ch 8 - Purchasing Power Parity and Real Exchange Rates]]"
---
# ECON 131 Problem Set 2: hedging (Lecture 3) and PPP (Lecture 4)

> (Please bring your handwritten work to class on Tue. No late or email submission is accepted.)

> [!warning] Handwritten, in class today
> Handed in on paper in class (Tue 10-13, 17:20), no email. Each problem has a **Copy by hand** box at its end: that is the short version to write out. Everything above it is the justification from class material.
>
> Numbered "2" because it is the second handwritten set (the first was the covered interest arbitrage and triangular set due Tue 10-06). Rename if Canvas numbers it differently.

**How to read this note.** Quote blocks (>) are copied from the handouts or from the problem. Everything under **Claude's work** is mine, not in the handouts, and each has a **My correction** box for you to overwrite me. Numbers were recomputed in Python, not by hand.

**Which lecture covers what.** Problem 1 is Lecture 3 section 6 (hedging). Problem 2 is Lecture 4 sections 3 and 4 (purchasing power, absolute PPP). Lectures 1 and 5 do not cover either: Lecture 1 is globalization and multinationals ([[ECON 131 Lecture 1 - Globalization and Multinationals]]), Lecture 5 is the balance of payments ([[ECON 131 Lecture 5 - Balance of Payments]]).

---

## Problem 1: the grain importer

> 1. As an importer of grain into Japan from the United States, you have agreed to pay \$326,434 in 120 days after you receive your grain. You face the following exchange rates and interest rates: spot rate, ¥103.89/\$, 120-day forward rate ¥105.33/\$, 120-day USD interest rate, 3.56% p.a., 120-day JPY interest rate, 2.27% p.a.
> (a). Explain two ways to hedge the transaction foreign exchange risk.
> (b). Calculate the costs of the two alternatives in part a and decide which one is superior with a lower cost.

### What the class material says (verbatim)

From the Lecture 3 handout, section 6:

> 6. Transaction exchange risk: possibility of taking a loss in foreign exchange transactions
>
> How to avoid transaction exchange risk? Hedging – protect against losses
>
> Method 1 forward hedge: using a forward contract and lock in a rate. No uncertainty.
>
> Method 2 money market hedge: making a transaction in the spot market to avoid currency mismatch in the future.

The handout's worked example (Zachy's Wine) is the template: the payable is in a foreign currency, and the costs are compared in the home currency. Your own class notes ([[ECON 131 Lecture 3 - Interest Rate Parity (fill-in)]], section 6) give the general case: forward hedge cost is the foreign liability times $\dfrac{F}{1+i}$, and the money market hedge cost is the foreign liability times $\dfrac{S}{1+i^*}$, where $i$ is the **domestic** rate and $i^*$ the **foreign** rate. Setting them equal gives the covered interest parity line from the handout:

$$1 + i = \frac{F}{S}\,(1 + i^*)$$

### Claude's work (not in the handout)

**Who is who.** You are the Japanese importer, so the **domestic** currency is the yen and the **foreign** currency is the dollar. The liability is in dollars, so $L = \$326{,}434$. Quotes are yen per dollar, so $S = 103.89$ and $F = 105.33$ are in the form domestic per foreign, the same as the handout's $S$ and $F$. So $i = i_{\yen} = 2.27\%$ and $i^* = i_{\$} = 3.56\%$.

**The risk.** In 120 days you must hand over dollars. If the dollar gets stronger (the quote rises above ¥103.89/\$), the same \$326,434 costs more yen. That is the transaction exchange risk.

**Period rates** (120 days of a 360-day year, the handout's convention):

| Rate | Per year | × 120/360 | Growth factor |
| --- | --- | --- | --- |
| USD $i^*$ | 3.56% | 1.18667% | 1.0118667 |
| JPY $i$ | 2.27% | 0.75667% | 1.0075667 |

#### (a) Two ways to hedge

**Method 1, forward hedge.** Sign a 120-day forward today to buy \$326,434 at ¥105.33/\$. The yen cost is fixed now, whatever the spot is in 120 days.

**Method 2, money market hedge.** Get the dollars today instead of in 120 days, so nothing is mismatched later:

| Step | When | What | Math | Result |
| --- | --- | --- | --- | --- |
| 1 | Today | Work out the dollars to deposit so they grow to \$326,434 | $\dfrac{326{,}434}{1.0118667}$ | **\$322,605.75** |
| 2 | Today | Borrow the yen to buy them at spot | $322{,}605.75 \times 103.89$ | **¥33,515,510.86** |
| 3 | Today | Buy the dollars and deposit them at 3.56% | | grows to \$326,434 at day 120 |
| 4 | Day 120 | Pay the grain bill from the deposit | | \$326,434 paid |
| 5 | Day 120 | Repay the yen loan with interest | $33{,}515{,}510.86 \times 1.0075667$ | **¥33,769,111.56** |

#### (b) Costs, compared the way class compares them (in today's yen)

|                    | Math                                                                    | Cost today (¥)       | Cost at day 120 (¥) |
| ------------------ | ----------------------------------------------------------------------- | -------------------- | ------------------- |
| Forward hedge      | $L \cdot \dfrac{F}{1+i} = 326{,}434 \times \dfrac{105.33}{1.0075667}$   | **34,125,080.11**    | 34,383,293.22       |
| Money market hedge | $L \cdot \dfrac{S}{1+i^*} = 326{,}434 \times \dfrac{103.89}{1.0118667}$ | **33,515,510.86**    | 33,769,111.56       |
| **Difference**     | forward minus money market                                              | **¥609,569** (1.79%) | ¥614,182            |

**The money market hedge is superior** (lower cost by about ¥609,569 in today's yen). The two columns agree on the winner: today's cost is the day-120 cost discounted at the yen rate, which is how your Lecture 3 notes did it for Zachy's.

**Why they differ (the CIP check).** If covered interest parity held, the forward would be $F^{\text{parity}} = S\,\dfrac{1+i}{1+i^*} = 103.89 \times \dfrac{1.0075667}{1.0118667} = 103.4485$, that is **¥103.4485/\$**. The market forward is ¥105.33/\$, about ¥1.88 higher. The money market hedge effectively buys dollars at ¥103.4485 (¥33,769,111.56 divided by 326,434 dollars), so it is cheaper by exactly the gap between the market forward and the parity forward. For Zachy's the two matched because CIP held; here it does not.

> [!note] My correction
> 

> [!abstract] Copy by hand: Problem 1
> **Given.** $L = \$326{,}434$, $S = ¥103.89/\$$, $F = ¥105.33/\$$, $i_{\$} = 3.56\%$, $i_{\yen} = 2.27\%$, 120 days = $\tfrac13$ year.
>
> **(a)** Risk: the dollar rises, so the payable costs more yen.
> 1. Forward hedge: buy \$326,434 forward at ¥105.33/\$ and lock the yen cost.
> 2. Money market hedge: borrow yen, buy dollars at spot, deposit them at $i_{\$}$ until they grow to \$326,434, repay the yen loan.
>
> **(b)**
> - Forward: $326{,}434 \times 105.33 = ¥34{,}383{,}293$ at day 120; today $\dfrac{34{,}383{,}293}{1.0075667} = ¥34{,}125{,}080$.
> - Money market: deposit $\dfrac{326{,}434}{1.0118667} = \$322{,}605.75$; borrow $322{,}605.75 \times 103.89 = ¥33{,}515{,}511$; repay $33{,}515{,}511 \times 1.0075667 = ¥33{,}769{,}112$ at day 120.
> - **Money market hedge is cheaper** by ¥609,569 today (¥614,182 at day 120).
> - Reason: the market forward ¥105.33 is above the parity forward ¥103.45, so CIP fails.

---

## Problem 2: purchasing power

> 2. Suppose that the price level in Canada is CAD13,800, the price level in France is EUR12,500, and the spot exchange rate is CAD1.20/EUR.
>
> What is the internal purchasing power of 10,000 Canadian dollar?
> What is the internal purchasing power of 10,000 euro in France?
> What is the implied exchange rate of CAD/EUR that satisfies absolute PPP?
> Is the euro overvalued or undervalued relative to the Canadian dollar?
> What amount of appreciation or depreciation of the euro would be required to return the actual exchange rate to its PPP value?

### What the class material says (verbatim)

From the Lecture 4 handout:

> 3. Purchasing power: the amount of goods and services that can be purchased per unit of currency.
>
> Internal purchasing power of a dollar: the amount of goods and services that can be purchased with a dollar in the United States.
>
> External purchasing power of a dollar: the the amount of goods and services that can be purchased with a dollar outside the United States.

> 4. Absolute purchasing power parity (PPP): the exchange rate will adjust to equalize the internal and external purchasing powers of a currency.
> $$\frac{1}{P(t,\$)} = \frac{1}{S^{PPP}(t,\$/€)}\,\frac{1}{P(t,€)}$$
> $$\Rightarrow S^{PPP}(t,\$/€) = \frac{P(t,\$)}{P(t,€)}$$

Handout example in section 3, worked in your class notes: price level \$100 in the US and €160 in Germany, \$1.25/€. Internal: \$1000 ÷ \$100 = 10 bundles. External: \$1000 ÷ 1.25 = €800, then 800 ÷ 160 = 5 bundles. PPP rate: 100 ÷ 160 = \$0.625/€; the market's \$1.25 is higher, so the **euro is overvalued**. Problem 2 is the same method with CAD in place of the dollar.

### Claude's work (not in the handout)

**Swap of symbols.** Home currency CAD (price level $P_{\text{CAD}} = 13{,}800$), foreign currency EUR ($P_{\text{EUR}} = 12{,}500$), quote CAD per EUR ($S = 1.20$). The handout's $\$$ becomes CAD and its € stays €.

| Part | What it asks                                        | Math                                                                            | Answer                           |
| ---- | --------------------------------------------------- | ------------------------------------------------------------------------------- | -------------------------------- |
| (1)  | Internal purchasing power of CAD 10,000 (in Canada) | $\dfrac{10{,}000}{13{,}800}$                                                    | **0.7246 bundles**               |
| (2)  | Internal purchasing power of EUR 10,000 (in France) | $\dfrac{10{,}000}{12{,}500}$                                                    | **0.8 bundles**                  |
| (3)  | PPP rate, CAD per EUR                               | $S^{PPP} = \dfrac{P_{\text{CAD}}}{P_{\text{EUR}}} = \dfrac{13{,}800}{12{,}500}$ | **CAD 1.104/EUR**                |
| (4)  | Euro over or undervalued?                           | actual 1.20 vs PPP 1.104                                                        | **Overvalued** (CAD undervalued) |
| (5)  | Change in the euro to reach PPP                     | $\dfrac{1.104 - 1.20}{1.20}$                                                    | **−8.0%: depreciate 8%**         |

**(3), how the formula comes from the definition.** Set internal equal to external for CAD: $\dfrac{1}{P_{\text{CAD}}} = \dfrac{1}{S^{PPP}}\cdot\dfrac{1}{P_{\text{EUR}}}$. Solve for $S^{PPP}$: $S^{PPP} = P_{\text{CAD}} / P_{\text{EUR}}$. Units: CAD per bundle over EUR per bundle gives CAD per EUR, which matches the quote.

**(4), the reason in two ways.**
- **Compare the rates.** The market charges CAD 1.20 for a euro. PPP says a euro should cost only CAD 1.104. A euro costs more than it should, so it is overvalued (same logic as the handout's Big Mac answer: the yen at ¥100/\$ instead of ¥110/\$ is overvalued).
- **Compare purchasing power at the market rate.**

| | Buys at home | Buys abroad at CAD 1.20/EUR | Reading |
| --- | --- | --- | --- |
| CAD 10,000 | 0.7246 bundles in Canada | $\dfrac{10{,}000}{1.20} = €8{,}333.33$, then $\dfrac{8{,}333.33}{12{,}500} = 0.6667$ bundles in France | the Canadian dollar buys less abroad |
| EUR 10,000 | 0.8 bundles in France | $10{,}000 \times 1.20 = \text{CAD } 12{,}000$, then $\dfrac{12{,}000}{13{,}800} = 0.8696$ bundles in Canada | the euro buys more abroad |

Under absolute PPP, internal and external purchasing power are equal. The euro's external (0.8696) beats its internal (0.8), so the euro is overvalued, as the rate comparison said. The overvaluation is $\dfrac{1.20}{1.104} - 1 = 8.70\%$ (the market price is 8.70% above its PPP value).

**(5), which currency the percent belongs to.** In CAD/EUR the euro is the **denominator**, so the percent change of the quote is the euro's. To return from 1.20 to 1.104 the quote falls 8.0%, so the **euro depreciates 8.0%** against the Canadian dollar. Seen from the other side, the CAD must appreciate $\dfrac{1.20}{1.104} - 1 = 8.70\%$. The two percents differ because the base changes, the same pair as −20% and +25% earlier.

> [!note] My correction
> 

> [!abstract] Copy by hand: Problem 2
> **Given.** $P_{\text{CAD}} = 13{,}800$, $P_{\text{EUR}} = 12{,}500$, $S = \text{CAD } 1.20/\text{EUR}$.
> 1. Internal purchasing power of CAD 10,000: $\dfrac{10{,}000}{13{,}800} = 0.7246$ bundles.
> 2. Internal purchasing power of EUR 10,000: $\dfrac{10{,}000}{12{,}500} = 0.8$ bundles.
> 3. $S^{PPP}(\text{CAD/EUR}) = \dfrac{P_{\text{CAD}}}{P_{\text{EUR}}} = \dfrac{13{,}800}{12{,}500} = \text{CAD } 1.104/\text{EUR}$.
> 4. Market 1.20 > PPP 1.104, so the **euro is overvalued** (CAD undervalued). Check: EUR 10,000 buys 0.8696 bundles abroad but 0.8 at home.
> 5. $\dfrac{1.104 - 1.20}{1.20} = -8.0\%$: the euro must **depreciate 8.0%** (the CAD appreciates 8.70%).

---

## Where each step comes from
| Step | Source |
| --- | --- |
| Forward hedge and money market hedge as the two methods | Lecture 3 handout, section 6 |
| Compare costs in the home currency; $L\,F/(1+i)$ vs $L\,S/(1+i^*)$ | Zachy's Wine example and your class notes, [[ECON 131 Lecture 3 - Interest Rate Parity (fill-in)]] |
| 360-day year, period rate = annual rate × days/360 | Lecture 3 handout, annualized percent formula |
| Why costs differ: covered interest parity | Lecture 3 handout, section 3 |
| Internal and external purchasing power; section 3 example (10 bundles, 5 bundles) | Lecture 4 handout, section 3 |
| $S^{PPP} = P/P$ and over/undervalued | Lecture 4 handout, sections 4 and 5 (Big Mac) |
| Percent change belongs to the denominator currency | Lecture 2 class notes |
| Lectures 1 and 5 | not used: they cover globalization and the balance of payments |

> [!note] My notes
> 
