---
type: lecture
parent: "[[ECON 131]]"
domain: econ
course: "ECON 131"
lecture: 3
week: 2
date: 2026-10-01
created: 2026-10-01
lecturer: "Chenyue Hu"
chapter: "Bekaert & Hodrick ch 3 (forwards, transaction risk) and ch 6 (interest rate parity)"
source: "School/ECON 131/Lectures/econ131-lec03.pdf"
status: draft
mastery: 0
aliases:
  - "Econ 130 L3"
  - "ECON 131 L3"
  - "ECON 131 Lecture 3"
  - "Interest Rate Parity (lecture)"
tags:
  - econ131
  - lecture
  - forex
  - interest-rate-parity
  - hedging
  - midterm1
prereqs:
  - "[[Spot vs Forward Contract]]"
  - "[[Direct vs Indirect Quote]]"
  - "[[Appreciation and Depreciation]]"
  - "[[Interest Rate Differential]]"
  - "[[Triangular Arbitrage]]"
related:
  - "[[Forward Premium and Discount]]"
  - "[[Covered Interest Rate Parity (CIP)]]"
  - "[[Covered Interest Arbitrage]]"
  - "[[Carry Trade]]"
  - "[[Uncovered Interest Rate Parity (UIP)]]"
  - "[[Transaction Exchange Risk]]"
  - "[[Forward Hedge vs Money Market Hedge]]"
---
# ECON 131 Lecture 3: Interest Rate Parity

> [!info] Lecture card
> | | |
> | --- | --- |
> | **Course** | [[ECON 131]] International Financial Markets |
> | **When** | Week 2, Lecture 3, Thu 2026-10-01 |
> | **Lecturer** | Chenyue Hu (office hours Thu 15:00-16:30, E2 469) |
> | **Handout** | [[econ131-lec03.pdf]] (2 pages) |
> | **Textbook** | Bekaert & Hodrick ch 3 and ch 6 |
> | **On the exam** | Midterm 1, Tue 2026-10-20 17:20 (weeks 1-3) |
> | **Comes after** | [[ECON 131 Lecture 2 - Exchange Rates]] (spot, forward, quotes, arbitrage) |
> | **Bitcoin aside** | Moved to the end of [[ECON 131 Lecture 2 - Exchange Rates]] (Kimchi premium, crypto vs FX, my argument) |

> [!abstract] The lecture in five lines
> 1. A **forward rate** $F$ is the rate locked in today for a trade on a future date. $F > S$ is a **forward premium** on the denominator currency; $F < S$ is a **forward discount**.
> 2. **Covered interest parity (CIP):** investing at home and investing abroad with the currency risk covered by a forward must pay the same: $1 + i = \frac{F}{S}(1 + i^*)$.
> 3. **Uncovered interest parity (UIP):** the same thing with the *expected* future spot rate in place of $F$ (no cover, so it holds only in expectation).
> 4. **Carry trade:** borrow the low-interest currency, invest in the high-interest one, and leave it uncovered (a bet that UIP fails).
> 5. **Hedging transaction risk:** a forward hedge or a money market hedge. When CIP holds, the two cost the same.

## Lecture map

| # | Section | The one idea | Concept note |
| --- | --- | --- | --- |
| 1 | Forward contracts | $F$ vs $S$ tells you premium or discount on the denominator currency | [[Forward Premium and Discount]] |
| 2 | Interest rates | Money today grows by $(1 + i)$; scale annual rates to the period | [[Interest Rate Differential]] |
| 3 | CIP | Covered foreign return = home return, or there is free money | [[Covered Interest Rate Parity (CIP)]], [[Covered Interest Arbitrage]] |
| 4 | Carry trade | Borrow low-yield, invest high-yield, uncovered | [[Carry Trade]] |
| 5 | UIP | Same parity, with the *expected* future spot | [[Uncovered Interest Rate Parity (UIP)]] |
| 6 | Transaction risk | Hedge with a forward or with the money markets | [[Transaction Exchange Risk]], [[Forward Hedge vs Money Market Hedge]] |
| P | Problems | Yen premium, Zachy's Wine, CIP arbitrage | below |

## Key terms

| Term | Meaning |
| --- | --- |
| Forward contract | Delivery of a set amount of one currency for another at a fixed future date |
| Forward rate $F$ | The exchange rate written into the forward contract |
| Forward premium | $F > S$: the denominator currency is worth more forward than spot |
| Forward discount | $F < S$: the denominator currency is worth less forward than spot |
| $i$, $i^*$ | Domestic and foreign interest rate for one period |
| CIP | $1 + i = \frac{F}{S}(1 + i^*)$, riskless, enforced by arbitrage |
| Covered interest arbitrage | Borrow cheap, convert, invest, sell forward: riskless profit when CIP fails |
| Carry trade | Borrow low-yield, invest high-yield, **no** forward cover |
| UIP | $1 + i = E_t\left[\frac{S(t+1)}{S(t)}\right](1 + i^*)$, holds in expectation only |
| Unbiasedness hypothesis | $F_t = E_t[S(t+1)]$: no systematic gap between forward and expected spot |
| Transaction exchange risk | Possible loss on a foreign currency payment or receipt due later |
| Forward hedge | Lock in the rate with a forward |
| Money market hedge | Spot transaction now plus borrowing/lending so nothing is mismatched later |

## Formula sheet

| Formula | Use it when | Watch out |
| --- | --- | --- |
| $\dfrac{F - S}{S} \times \dfrac{360}{N_{\text{days}}}$ | Asked for a premium or discount "per annum" | Sign: + premium, minus discount, on the **denominator** currency |
| $1 + i = \dfrac{1}{S}(1 + i^*)F$ | Asked "does CIP hold?" | $S$, $F$ in home per foreign; $i$, $i^*$ for the **period**, not per annum |
| $F_{\text{parity}} = S \times \dfrac{1 + i}{1 + i^*}$ | Asked what the forward "should" be | Same units as above |
| $1 + i = E_t\left[\dfrac{S(t+1)}{S(t)}\right](1 + i^*)$ | UIP, carry trade questions | Expected spot, not $F$ |
| Period rate $= \text{annual} \times \dfrac{N_{\text{days}}}{360}$ | Any 90-day or 3-month problem | 3 months = divide by 4 |

> [!tip] Your move: any CIP problem in four steps
> 1. **Write the quote as home per foreign** ($S$ and $F$). Pick the U.S. as home if dollars are in the numerator.
> 2. **Scale the rates to the period:** 3 months, divide by 4.
> 3. **Compare** $1 + i$ (left) with $\frac{F}{S}(1 + i^*)$ (right).
> 4. **Arbitrage, if they differ:** borrow on the smaller side, invest on the bigger side, sell forward today. Profit = what the bigger side returns minus what you owe.

---

## 1 Forward contracts, forward premium and discount
Concept: [[Forward Premium and Discount]]

A **forward contract** calls for delivery, at a fixed future date, of a specified amount of one currency against payment in another currency. The exchange rate specified in the contract is called the **forward rate**.

- **Forward premium:** occurs when the price of the currency contract is higher than the spot rate: $F_{\$/£} > S_{\$/£}$
- **Forward discount:** occurs when the price of the currency contract is lower than the spot rate: $F_{\$/£} < S_{\$/£}$

> [!important] Note
> 1. As with the terms appreciation and depreciation, the terms forward premium and forward discount refer to the currency that is in the **denominator** of the exchange rate. (In $F_{\$/£}$, a premium or discount is on the pound.)
> 2. Premiums and discounts are often expressed as annualized percentages:
> $$\text{Annualized percent} = \frac{\text{forward} - \text{spot}}{\text{spot}} \times \frac{360}{N_{\text{days}}}$$

> [!note] My notes
> 

---

## 2 Interest rate: the time value of money
Concept: [[Interest Rate Differential]]

A unit of currency today is worth $(1 + i)$ units one period from now if invested at interest rate $i$. Rates in this lecture are quoted **per annum**, so for a shorter period scale them: a 3-month (90-day) rate is the annual rate $\times \frac{90}{360}$, i.e. divide by 4.

> [!note] My notes
> 

---

## 3 Covered Interest Rate Parity (CIP)
Concepts: [[Covered Interest Rate Parity (CIP)]], [[Covered Interest Arbitrage]]

Consider an investor with one unit of domestic currency and two alternative investments.
- **Alternative 1:** Invest in the domestic market.
- **Alternative 2:** Invest in the foreign market: convert the domestic currency into foreign currency, invest in the foreign market, and then sell the foreign currency in the forward market.

| Symbol | Meaning |
| --- | --- |
| $i$ | the domestic currency interest rate appropriate for one period |
| $i^*$ | the foreign currency interest rate appropriate for one period |
| $S$ | the spot exchange rate (domestic currency per foreign currency) |
| $F$ | the one-period forward exchange rate (domestic currency per foreign currency) |

$$1 + i = \frac{1}{S} \times (1 + i^*) \times F$$

Read the right side left to right as the steps of Alternative 2: $\frac{1}{S}$ turns 1 unit of home currency into foreign currency, $(1 + i^*)$ grows it abroad, $\times F$ sells it forward back into home currency.

Forward premiums and discounts in the foreign exchange market offset interest differentials to eliminate possible arbitrage that would arise from borrowing the low-interest-rate currency, lending the high-interest-rate currency, and covering the foreign exchange risk.

> [!tip] Same equation, rearranged
> $$\frac{F}{S} = \frac{1 + i}{1 + i^*}$$
> The currency with the **higher** interest rate trades at a forward **discount**, by about the interest differential.

> [!note] My notes
> 

---

## 4 Carry trade
Concept: [[Carry Trade]]

**Carry trade:** a strategy in which an investor borrows in low-yield currencies and invests in high-yield currencies.

Unlike covered arbitrage, it is not covered with a forward, so it carries exchange rate risk. It pays off when the high-yield currency does not depreciate enough to wipe out the interest gap.

> [!note] My notes
> 

---

## 5 Uncovered Interest Rate Parity (UIP)
Concept: [[Uncovered Interest Rate Parity (UIP)]]

The foreign money market investment has the same ***expected*** return as the domestic investment.

$$1 + i = E_t\left[\frac{S(t+1)}{S(t)}\right] \times (1 + i^*)$$

**Unbiasedness hypothesis:** there is no systematic difference between the forward rate and the expected future spot rate: $F_t = E_t[S(t+1)]$. (If both CIP and UIP hold, this follows.)

> [!note] My notes
> 

---

## 6 Transaction exchange risk and hedging
Concepts: [[Transaction Exchange Risk]], [[Forward Hedge vs Money Market Hedge]]

**Transaction exchange risk:** the possibility of taking a loss in foreign exchange transactions.

How to avoid transaction exchange risk? **Hedging**: protect against losses.
- **Method 1, forward hedge:** use a forward contract and lock in a rate. No uncertainty.
- **Method 2, money market hedge:** make a transaction in the spot market to avoid a currency mismatch in the future.

> [!note] My notes
> 

---

## Problems
The handout leaves these for class. Worked answers are **folded**: try on paper first, then click to open. They were worked by Claude, not the professor, so check them against class.

### P1 Yen forward discount (section 1)
If the spot exchange rate of the yen relative to the dollar is ¥100/\$, and the 90-day forward rate is ¥90/\$, is the dollar at a forward premium or discount? Express the premium or discount as a percentage per annum for a 360-day year.

> [!example]- Worked answer
> The dollar is in the denominator (¥ per \$), so the question is about the dollar.
> Forward ¥90 < spot ¥100: a dollar buys fewer yen forward than now, so the **dollar is at a forward discount**.
> $$\frac{90 - 100}{100} \times \frac{360}{90} = -0.10 \times 4 = -40\% \text{ per annum}$$
> The dollar is at a 40% per annum forward discount. (Flip the quote to \$/¥ and the yen is at a forward premium.)

### P2 Zachy's Wine hedge (section 6)
Zachy's Wine is importing wine from France for €4 million. It is payable in 90 days.
- Spot exchange rate: \$1.10/€
- 90-day forward: \$1.08/€
- 90-day dollar interest rate: 6% p.a.
- 90-day euro interest rate: 13.519% p.a.

> [!example]- Worked answer
> Zachy's owes euros in 90 days, so the risk is the euro getting more expensive. 90-day rates: dollar $6\%/4 = 1.5\%$, euro $13.519\%/4 = 3.37975\%$.
>
> **Forward hedge:** buy €4M forward at \$1.08/€. Cost in 90 days: $4{,}000{,}000 \times 1.08 = \$4{,}320{,}000$, known today.
>
> **Money market hedge:** get the euros now and park them so they grow to exactly €4M.
> 1. Euros needed today: $\frac{4{,}000{,}000}{1.0337975} \approx 3{,}869{,}230$ euros
> 2. Buy them at spot: $3{,}869{,}230 \times 1.10 \approx \$4{,}256{,}153$ (borrow these dollars at 1.5%).
> 3. Invest the euros at 3.37975%; in 90 days they are worth €4M, which pays the bill.
> 4. Repay the dollar loan: $4{,}256{,}153 \times 1.015 \approx \$4{,}319{,}995$
>
> Both hedges cost about **\$4.32M**. The numbers were chosen so CIP holds ($\frac{1.08}{1.10} = \frac{1.015}{1.0337975}$), and when CIP holds the two hedges are the same deal.

### P3 Exercise on interest rate parity (section 3)
Currently, the spot exchange rate is \$1.50/£ and the three-month forward exchange rate is \$1.52/£. The three-month interest rate is 8.0% per annum in the U.S. and 5.8% per annum in the U.K. Assume that you can borrow as much as \$1,500,000 or £1,000,000.

a. Determine whether the covered interest rate parity is currently holding.

b. If the CIP is not holding, how would you carry out covered interest arbitrage? Show all the steps and determine the arbitrage profit.

c. Explain how the CIP will be restored as a result of covered arbitrage activities.

> [!example]- Worked answer (a)
> Three-month rates: $i = 8.0\%/4 = 2.0\%$ (U.S., domestic), $i^* = 5.8\%/4 = 1.45\%$ (U.K.).
> - Left side: $1 + i = 1.0200$
> - Right side: $\frac{1}{1.50} \times 1.0145 \times 1.52 \approx 1.0280$
>
> $1.0200 \ne 1.0280$, so **CIP does not hold**. The covered U.K. investment pays more than the U.S. one. (The parity forward rate would be $1.50 \times \frac{1.02}{1.0145} \approx 1.5081$ dollars per pound, but the market forward is \$1.52.)

> [!example]- Worked answer (b)
> Borrow where the return is low (U.S.), invest where the covered return is high (U.K.).
> 1. Borrow \$1,500,000 in the U.S. at 2%; you will owe $1{,}500{,}000 \times 1.02 = 1{,}530{,}000$ dollars.
> 2. Convert at spot: $1{,}500{,}000 / 1.50 = 1{,}000{,}000$ pounds.
> 3. Invest in the U.K. at 1.45%: grows to $1{,}000{,}000 \times 1.0145 = 1{,}014{,}500$ pounds.
> 4. Today, sell £1,014,500 forward at \$1.52: locks in $1{,}014{,}500 \times 1.52 = 1{,}542{,}040$ dollars.
> 5. In three months, repay \$1,530,000.
>
> **Arbitrage profit: \$1,542,040 minus \$1,530,000 = \$12,040**, riskless.

> [!example]- Worked answer (c)
> Everyone doing step (b) pushes each price toward parity:
> - Buying £ spot raises the spot rate $S$.
> - Selling £ forward lowers the forward rate $F$.
> - Borrowing dollars raises the U.S. rate $i$.
> - Lending pounds lowers the U.K. rate $i^*$.
>
> $F/S$ falls and $(1+i)/(1+i^*)$ rises until $1 + i = \frac{F}{S}(1 + i^*)$ and the profit is gone.

> [!note] My notes
> 

---

## Self-test (answer cold, then open)

> [!question]- 1. In $F_{¥/\$} < S_{¥/\$}$, which currency is at a forward discount?
> The dollar (the denominator currency).

> [!question]- 2. A 3-month rate is quoted as 6% per annum. What goes into the CIP equation?
> $1.015$ (6% / 4 = 1.5% for the period).

> [!question]- 3. Under CIP, does the high-interest currency trade at a forward premium or discount?
> Discount. $\frac{F}{S} = \frac{1+i}{1+i^*}$, so a bigger $i^*$ means a smaller $F$.

> [!question]- 4. What is the one difference between CIP and UIP?
> CIP uses the forward rate $F$ (covered, riskless). UIP uses the expected future spot $E_t[S(t+1)]$ (uncovered, holds on average).

> [!question]- 5. Why is a carry trade risky but covered interest arbitrage not?
> The carry trade has no forward, so a depreciation of the high-yield currency can wipe out the interest gap. Covered arbitrage locks the conversion rate with a forward.

> [!question]- 6. CIP holds. Which is cheaper, the forward hedge or the money market hedge?
> Neither: they cost the same.

> [!question] Ask Claude
> 

---

## Related
- Previous: [[ECON 131 Lecture 2 - Exchange Rates]] and its cards [[ECON 131 Cards - ECON131 Lecture 2]]
- Prereqs: [[Spot vs Forward Contract]], [[Direct vs Indirect Quote]], [[Appreciation and Depreciation]], [[Interest Rate Differential]], [[Triangular Arbitrage]]
- New concepts: [[Forward Premium and Discount]], [[Covered Interest Rate Parity (CIP)]], [[Covered Interest Arbitrage]], [[Carry Trade]], [[Uncovered Interest Rate Parity (UIP)]], [[Transaction Exchange Risk]], [[Forward Hedge vs Money Market Hedge]]
- Course hub: [[ECON 131]] · Topic hub: [[Exchange Rates]]
