---
type: study
parent: "[[ECON 131 Lecture 3 - Interest Rate Parity]]"
domain: econ
course: "ECON 131"
lecture: 3
source: "70 Files/Courses/econ131/econ131-lecture03-interest-rate-parity.pdf"
status: draft
prereqs:
  - "[[Spot vs Forward Contract]]"
  - "[[Direct vs Indirect Quote]]"
  - "[[Appreciation and Depreciation]]"
---
# ECON 131 Lecture 3: Interest Rate Parity (fill-in)

Handout: [[econ131-lecture03-interest-rate-parity.pdf]] (2 pages). Full worked notes: [[ECON 131 Lecture 3 - Interest Rate Parity]]. Midterm 1, Tue 10-20.

How to use this: text in quote blocks (>) is copied from the handout as closely as I can read it from the page. Anything under **Claude's explanation**, the folded answers, the tables I added and the **Fill in** lines are not in the handout. Your own class notes are left exactly as you typed them. After every folded answer and every explanation of mine there is a **My correction** box for you to overwrite me. Open the folded answers only after you've written your own.

**The question the lecture answers:** if I can earn interest at home or abroad, what has to be true about exchange rates so nobody gets free money?

---

## 1. Forward contracts
> 1. A forward contract calls for delivery, at a fixed future date, of a specified amount of one currency against payment in another currency. The exchange rate specified in the contract is called the forward rate.
>
> Forward premium: occurs when the price of the currency contract is higher than the spot rate
> $$F_{\$/£} > S_{\$/£}$$
> Forward discount: occurs when the price of the currency contract is lower than the spot rate
> $$F_{\$/£} < S_{\$/£}$$
>
> Note: 1) As with the terms appreciation and depreciation, the terms forward premium and forward discount refer to the currency that is in the denominator of the exchange rate. 2) Premiums and discounts are often expressed as annualized percentages.
> $$\text{Annualized Percent} = \frac{\text{forward} - \text{spot}}{\text{spot}} * \frac{360}{N_{\text{days}}}$$




**Claude's explanation (not in the handout):**
- A forward premium means $F > S$ (the contract price is above spot). A forward discount means $F < S$.
- Both words describe the currency in the **denominator** of the quote, so in $F_{\$/£}$ it is the pound.
- The annualized formula multiplies the percent gap by $\frac{360}{N_{\text{days}}}$ to scale it to a full 360-day year.

> [!note]- My correction
> 


**Fill in, in my words:** what a forward is, and why a company would want one
- 

**Fill in:** in $F_{\$/£}$, which currency is "at a premium" when $F > S$, and why that one?
- 

> Example. If the spot exchange rate of the yen relative to the dollar is ¥100/\$, and the 90-day forward rate is ¥90/\$, is the dollar at a forward premium or discount? Express the premium or discount as a percentage per annum for a 360-day year.
- Given: 
- Denominator currency: 
- F vs S: 
- Annualized: ( ___ − ___ ) / ___ × 360 / ___ = ___

> [!check]- Answer
> The dollar is in the denominator. F = 90 < S = 100, so the **dollar is at a forward discount**: (90 − 100)/100 × 360/90 = **−40% per annum**.

> [!note]- My correction
> 


---

## 2. Interest rates: the time value of money
> 2. Interest rate — the time value of money

**Claude's explanation (the handout only gives the heading above):**
- \$1 today at rate $i$ becomes $1 + i$ after one period.
- Rates are quoted **per annum**. For a shorter period, scale them: 3 months = annual ÷ 4, 90 days = annual × 90/360.

> [!note]- My correction
> 



What determines interest rates, and their change
Primarily, risk
Risk here is long term outcomes

**Fill in:** 6% per annum for 90 days becomes ___ , so \$1 grows to ___
- 

---

## 3. Covered interest rate parity (CIP)
> 3. Covered Interest Rate Parity (CIP)
>
> Consider an investor with one unit of domestic currency and two alternative investments.
>
> Alternative 1: Invest in the domestic market.
>
> Alternative 2: Invest in the foreign market — convert the domestic currency into foreign currency, invest in the foreign market, and then sell the foreign currency in the forward market.
>
> $i$ the domestic currency interest rate appropriate for one period
>
> $i^*$ the foreign currency interest rate appropriate for one period
>
> $S$ the spot exchange rate (domestic currency per foreign currency)
>
> $F$ the one-period forward exchange rate (domestic currency per foreign currency)
> $$1 + i = 1/S \times (1 + i^*) \times F$$
> Forward premiums and discounts in the foreign exchange market offset interest differentials to eliminate possible arbitrage that would arise from borrowing the low-interest rate currency, lending the high-interest-rate currency, and covering the foreign exchange risk.

**Claude's explanation (not in the handout):**
The same formula as a fraction: $1 + i = \dfrac{F}{S}\,(1 + i^*)$. Solving for the forward-to-spot ratio gives $\dfrac{F}{S} = \dfrac{1 + i}{1 + i^*}$.

> [!note]- My correction
> 


**Fill in:** read the right side left to right as a path for your 1 unit of home money
- $\frac{1}{S}$: 
- $\times (1 + i^*)$: 
- $\times F$: 

**Fill in, in my words:** why are the two sides equal? What happens if they aren't?
- 

**Fill in:** under CIP, does the high-interest currency trade at a forward premium or discount? Why?
- 

> [!check]- Answer
> At a discount. Rearranged, $\frac{F}{S} = \frac{1+i}{1+i^*}$, so a bigger foreign rate $i^*$ means a smaller $F$. You earn more interest abroad but lose it back on the forward.

> [!note]- My correction
> 


---

## 4. Carry trade
> 4. Carry trade: a strategy in which an investor borrows in low-yield currencies and invest in high-yield currencies.

**Fill in:** how is this different from Alternative 2 in CIP? What's missing, and what is the risk?

The two sources of gain in a carry trade
	Interest differential
	Suppose AUD & JPY are
		If you can borrow in the JPY at 0%
		and lend in AUD in 4% 
		The interest diff. is the first source of gain in the carry trade
	Potential movements S (JPY/AUD) If goes up in value
		This currency movement provides the second source of income.
	If both sources are compared, the second source is guarenteed as FEX delta is unknown and of unknown parity
		AUD is a strong currency due to investment and stability
		IF the second source of growth goes in such a way that invaldiates the currency posiitves it can kill any profitability
	This happened during the unwinding of 98' where wallstreet lost some big players due to the uncanny movement where the JPY and AUD performed uncanny movements
Hedging
	Why do firms not then hedge with the forward contract
	If everyone is using the forward contract, then the CIP condition kicks in and the investment payout equalizes.
	SO there will be no arbitrage opprotunity
	ergo there is no way to hedge risk
	---
	What would be our pick for strong itnerest rates to lend in and low interest rates to borrow in

Takes advantage of long currency and short currency,

Long term currency
Short term currency

terms of profit are called the difference in % between the interest rate between both currencies held

Positive Carry

> [!info] Claude's check of your carry trade notes (not from the handout)
> - You wrote that the second source "is guarenteed". The exchange-rate move is the part that is **not** guaranteed, which is exactly the carry trade's risk. The first source (the interest differential) is the known part.
> - Why a forward would not help: if everyone hedges with a forward, CIP holds and the hedged gain is zero, so the profit that attracted the carry trade is gone. That is your "no arbitrage opportunity" line.

> [!note]- My correction
> 



---

## 5. Uncovered interest rate parity (UIP)
> 5. Uncovered interest rate parity (UIP)
>
> The foreign money market investment has the same *expected* return as the domestic investment.
> $$1 + i = E_t\left[\frac{S(t+1)}{S(t)}\right] \times (1 + i^*)$$
> Unbiasedness hypothesis
>
> There is no systematic difference between the forward rate and the expected future spot rate.

**Fill in:** the one difference between CIP and UIP (look at what replaced $F$)
- 

**Fill in:** if the carry trade makes money on average, which parity fails, CIP or UIP?
- 

---

## 6. Transaction exchange risk and hedging
> 6. Transaction exchange risk: possibility of taking a loss in foreign exchange transactions
>
> How to avoid transaction exchange risk? Hedging – protect against losses
>
> Method 1 forward hedge: using a forward contract and lock in a rate. No uncertainty.
>
> Method 2 money market hedge: making a transaction in the spot market to avoid currency mismatch in the future.

The two methods, in place for your notes (from the handout):
- Method 1 forward hedge: using a forward contract and lock in a rate. No uncertainty.
		
- Method 2 money market hedge: making a transaction in the spot market to avoid currency mismatch in the future.
		Trade currencies today to avoid currency mismatch today 

> Example: Zachy's Wine is importing wine from France for €4 million. It is payable in 90 days. Spot exchange rate: \$1.10/€, 90-day forward: \$1.08/€, 90-day dollar interest rate: 6% p.a. 90-day euro interest rate: 13.519% p.a.

The example's numbers, in place for your notes (from the handout):
		p.a. - per annum
Forward hedge
- Spot exchange rate: \$1.10/€, 90-day forward: \$1.08/€,
	- 1.08 dollar per euro:
		- EUR 4M * USD1.08/EUR = USD4,320,000
			- This is not the full amount you set aside as you will be taking the interest rates gain to your funds
			- So we do:
			- $4,320,000
			- 1+6% * 90/360 = 4,256,157.64 so that is the cost of doing the forward hedge
Money market hedge
- 90-day dollar interest rate: 6% p.a. 90-day euro interest rate: 13.519% p.a.
	Hedge by buying now and letting the exchange rate be a non-sequitor as its already in the right currency
	1+13.51% * 90/360 = 3,869,229.71
	The question is how much will we need to fund this amount and we find that by 
	EUR 3,869,229.71 \* 1.1/EUR = 4256152.68
Let's make the comparison to see which one is better
	Here our metric is more affordable, here that difference is 5 dollars
	5 dollars in 4 million, they cost almost the same and this is not a coincidence

If we think about the dollar cost in the general case, foreign liabilty \* F/ 1 + i
That is how we charge in the general case

If we want to summarize the general case:
Foreign liability \* S / 1+i\*

If we cross out the common foreign liability 

We get F/1+i = S/1+i

**This is the CIP condition**
Under the condition 1+i=F/S(1+i\*)

> [!info] Claude's check of your Zachy's notes (not from the handout)
> - Forward hedge, present value: $\dfrac{4{,}000{,}000 \times 1.08}{1.015} = \dfrac{4{,}320{,}000}{1.015} = 4{,}256{,}157.64$ ✓
> - Euros needed today: $\dfrac{4{,}000{,}000}{1.0337975} = 3{,}869{,}229.7$, and $3{,}869{,}229.7 \times 1.10 = 4{,}256{,}152.7$ ✓
> - The gap is about \$5, as you wrote ✓. Your general case also checks out: forward hedge costs $L\,\dfrac{F}{1+i}$, money market hedge costs $L\,\dfrac{S}{1+i^*}$; setting them equal gives $1 + i = \dfrac{F}{S}(1 + i^*)$, the CIP line.

> [!note]- My correction
> 


**Fill in:**
- What is Zachy's afraid of? 
	- Uncertainty in the exchange rate
- 90-day rates: dollar ___ %, euro ___ %
- Forward hedge cost in 90 days: 4,000,000 × ___ = \$___
- Money market hedge:
  - Euros needed today so they grow to €4M: 4,000,000 / ___ = €___
  - Dollars to buy them at spot: ___ × 1.10 = \$___
  - Repay that dollar loan in 90 days: ___ × ___ = \$___
- Which hedge is cheaper, and why?

> [!check]- Answer
> The risk is the euro getting more expensive. Rates: 1.5% and 3.37975%. Forward: 4,000,000 × 1.08 = **\$4,320,000**. Money market: €3,869,230 today, costing \$4,256,153, which you repay as about **\$4,319,995**. **Same cost**, because CIP holds with these numbers.

> [!note]- My correction
> 


---

## Exercise (handout): interest rate parity
> Exercise on interest rate parity. Currently, the spot exchange rate is \$1.50/£ and the three-month forward exchange rate is \$1.52/£. The three-month interest rate is 8.0% per annum in the U.S. and 5.8% per annum in the U.K. Assume that you can borrow as much as \$1,500,000 or £1,000,000.

> a. Determine whether the covered interest rate parity is currently holding.
- Period rates: $i$ = ___ , $i^*$ = ___
- Left side: $1 + i$ = ___
- Right side: $\frac{1}{1.50} \times$ ___ $\times 1.52$ = ___
- Equal? 

> [!check]- Answer a
> $i$ = 2.0%, $i^*$ = 1.45%. Left 1.0200, right ≈ 1.0280. **CIP does not hold**; the covered UK investment pays more.

> [!note]- My correction
> 


> b. If the CIP is not holding, how would you carry out covered interest arbitrage? Show all the steps and determine the arbitrage profit.
- Borrow where: ___ . Invest where: ___
- Step 1, borrow: 
- Step 2, convert at spot: 
- Step 3, invest: 
- Step 4, sell forward today: 
- Step 5, repay: 
- Profit: 

> [!check]- Answer b
> Borrow \$1.5M at 2% (owe \$1,530,000) → £1,000,000 → invest at 1.45% → £1,014,500 → sold forward at 1.52 = \$1,542,040. **Profit \$12,040**, riskless.

> [!note]- My correction
> 


> c. Explain how the CIP will be restored as a result of covered arbitrage activities.

**Fill in:** one line for each of S, F, i, i*
- S: 
- F: 
- i: 
- i*: 

> [!check]- Answer c
> Buying £ spot pushes S up. Selling £ forward pushes F down. Borrowing dollars pushes i up. Lending pounds pushes i* down. That continues until the two sides are equal again.

> [!note]- My correction
> 


---

## My questions for lecture or office hours
- 

## Related
Full notes: [[ECON 131 Lecture 3 - Interest Rate Parity]] · Next: [[ECON 131 Lecture 4 - Purchasing Power Parity]] · Course hub: [[ECON 131]]
