---
type: lecture
parent: "[[ECON 131]]"
domain: econ
course: "ECON 131"
lecture: 4
week: 3
date: 2026-10-06
lecturer: "Chenyue Hu"
chapter: "Bekaert & Hodrick ch 8 (purchasing power parity and real exchange rates)"
source: "70 Files/Courses/econ131/econ131-lecture04-purchasing-power-parity.pdf"
status: draft
mastery: 0
aliases:
  - "ECON 131 L4"
  - "ECON 131 Lecture 4"
prereqs:
  - "[[ECON 131 Lecture 3 - Interest Rate Parity]]"
  - "[[Appreciation and Depreciation]]"
  - "[[Direct vs Indirect Quote]]"
---
# ECON 131 Lecture 4: Purchasing Power Parity

Handout: [[econ131-lecture04-purchasing-power-parity.pdf]] (2 pages). Reading: [[ECON 131 W2 Reading - Textbook Ch 8 - Purchasing Power Parity and Real Exchange Rates]]. Midterm 1, Tue 10-20.

How to use this: text in quote blocks (>) is copied from the handout as closely as I can read it from the page. Anything under **Claude's explanation**, the folded answers, the tables I added and the **Fill in** lines are not in the handout. Your own class notes are left exactly as you typed them. After every folded answer and every explanation of mine there is a **My correction** box for you to overwrite me. Open the folded answers only after you've written your own.

**The question the lecture answers:** if the same stuff costs different amounts in different countries, what should the exchange rate be?

---

## 1. Law of one price (LOOP)
> 1. Law of one price (LOOP): The price of a good, when denominated in a particular currency, is the same wherever in the world the good is being sold.

Why violations of the law of one price occur (handout):
- Tariffs and quotas
- Transaction costs
	- literal and figurative
- Noncompetitive markets
- Sticky prices

**Fill in, in my words:** what LOOP says
- LOOP says the price in a currency 

**Fill in:** one real example of each break (one line each)
- Tariffs/quotas: 
- Transaction costs: 
- Noncompetitive markets: 
- Sticky prices: 

**Fill in:** what would someone do to make money if LOOP failed and none of the four breaks were there? (Hint: same move as Lecture 2 arbitrage.)

---

## 2. Price level, price index, inflation
> 2. A country's price level: the weighted average of the nominal prices of the goods and services consumed in the economy.
> $$P(t,\$) = \sum_{i=1}^{N} w_i \, P(t,i,\$)$$
> Price index: the ratio of a price level at one point in time to the price level in a designated base year.
> $$PI(t+k,\$) = \frac{P(t+k,\$)}{P(t,\$)}$$
> Inflation: change in price levels
> $$\pi = \frac{P(t+k,\$) - P(t,\$)}{P(t,\$)} * 100\%$$

> **Exhibit 8.1** Price Indexes for the G7 Countries, 1960-2010 (the handout shows it as a table from the textbook)

| Year | United States | Canada | France | Germany | Italy | Japan | United Kingdom |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1960 | 27.6 | 24.6 | 17.2 | 39.4 | 9.8 | 21.2 | 13.2 |
| 1970 | 36.1 | 32.3 | 25.2 | 50.9 | 14.0 | 36.9 | 19.6 |
| 1980 | 76.5 | 69.7 | 63.3 | 82.6 | 51.0 | 87.2 | 70.7 |
| 1985 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| 1990 | 121.4 | 124.1 | 116.3 | 107.7 | 131.2 | 107.0 | 133.4 |
| 1995 | 141.7 | 139.2 | 129.9 | 126.2 | 168.6 | 113.5 | 158.4 |
| 2000 | 159.0 | 150.0 | 138.0 | 133.9 | 188.3 | 115.2 | 179.9 |
| 2005 | 179.4 | 167.8 | 151.8 | 144.9 | 212.0 | 112.4 | 202.1 |
| 2008 | 197.8 | 179.0 | 161.1 | 154.5 | 227.8 | 114.3 | 219.3 |
| 2009 | 197.1 | 179.5 | 161.2 | 155.0 | 229.5 | 112.7 | 224.0 |
| 2010 | 199.3 | 181.1 | 162.6 | 155.8 | 231.3 | 111.7 | 228.2 |

**Claude's explanation (not in the handout):**
- $w_i$ is the share of good $i$ in the consumption bundle, and the weights add to 1.
- $P(t,i,\$)$ is the dollar price of good $i$ at time $t$.
- Price index of 100 in the base year (1985 in Exhibit 8.1) means every later number reads as a percent of that year's price level.
- To get inflation between two years from the table, divide the later index by the earlier and subtract 1: $\pi = \dfrac{PI_{\text{later}}}{PI_{\text{earlier}}} - 1$.

> [!note]- My correction
> 


**Fill in, in my words:** what goes in, what comes out, for each formula
- Price level: in = ___ , out = ___
- Price index: in = ___ , out = ___
- Inflation: in = ___ , out = ___

Story = 112.7/114.3 - 1 = -1.4%
	The minus 1 comes from trying to find the rate of change
US 1985 - 2010/ 

$\pi$ = 199.3/100 = 2.79%

> [!info] Claude's check of your two lines above (not from the handout)
> - Japan, 2008 to 2009: $\dfrac{112.7}{114.3} - 1 = -0.0140$, so $\pi \approx -1.4\%$. ✓ Prices fell, so that is deflation.
> - US, 1985 to 2010: $\dfrac{199.3}{100} = 1.993$ is the price **index** (a 99.3% rise in total over 25 years), not a rate. The 2.79% you wrote is the **yearly** rate: $1.993^{1/25} - 1 \approx 0.0280$, about 2.80% per year.

> [!note]- My correction
> 


**Fill in:** why weights? Why not just average the prices?
- 

---

## 3. Purchasing power
> 3. Purchasing power: the amount of goods and services that can be purchased per unit of currency.
>
> Internal purchasing power of a dollar: the amount of goods and services that can be purchased with a dollar in the United States.
>
> External purchasing power of a dollar: the the amount of goods and services that can be purchased with a dollar outside the United States.
>
> e.g. Suppose the price level for the average consumption bundle is \$100 in the US, and €160 in Germany. The exchange rate is \$1.25/€. What is the internal and external purchasing power of \$1000?

**Claude's formulas (not in the handout):**
- Internal purchasing power of one dollar $= \dfrac{1}{P(t,\$)}$ bundles per dollar.
- External purchasing power of one dollar (convert to euros first, then buy) $= \dfrac{1}{S(t,\$/€)\,P(t,€)}$ bundles per dollar.

> [!note]- My correction
> 



**Fill in, step by step:**
- Given: 
- Internal: \$1000 buys 10 bundles in the US as $1000/\$100 per bundle = 10 bundles
- External: \$1000 converts to € ___ , which buys ___ bundles in Germany
	- 1k / 1.25/eur = 800 
	- then 800/160 = 5 bundles
- So the dollar buys more at home / abroad (circle one): 

> [!check]- Answer
> Internal: 1000 / 100 = **10 bundles**. External: 1000 / 1.25 = €800, and 800 / 160 = **5 bundles**. The dollar buys twice as much at home, so at this exchange rate Germany is expensive for an American.

> [!note]- My correction
> 




IF you buy goods in the US with 1k you get 10 bundles...

IF sell 10 bundles in EUR@PL there 160EUR per bundle

RECIEVE 10\* 160 = E 1600 EUR = $2000

This is goods markets arbitrage,  selling foreign converting back to domestic

The data demonstrates that there is strong volaitlity in real data but strong trend focus using PPP


---

## 4. Absolute PPP
> 4. Absolute purchasing power parity (PPP): the exchange rate will adjust to equalize the internal and external purchasing powers of a currency.
> $$\frac{1}{P(t,\$)} = \frac{1}{S^{PPP}(t,\$/€)}\,\frac{1}{P(t,€)}$$
> $$\Rightarrow S^{PPP}(t,\$/€) = \frac{P(t,\$)}{P(t,€)}$$

**Claude's explanation (not in the handout):**
Read it: the PPP exchange rate is just **home price level over foreign price level**, in the same units as the quote (\$ on top, € on the bottom). The first line sets internal purchasing power (left) equal to external purchasing power (right), and the second line solves for $S$.

> [!note]- My correction
> 


**Fill in, in my words:** what PPP predicts, and why (what would people do if it failed?)
- The LHS is the internal and the EXTERNAL is RHS
	- S^PPP (t,\$/EUR) = p(t,\$)/p(t,EUR)
The ratio of price levels gives leverage statement over the exchange rate
**Fill in:** using the section 3 numbers, the PPP rate is \$___/€. The market rate is \$1.25/€. So the euro is over / undervalued:
- 

> [!check]- Answer
> $S^{PPP}$ = 100 / 160 = **\$0.625/€**. The market charges \$1.25, double that, so the **euro is overvalued** (the dollar undervalued) relative to PPP. That matches section 3: \$1000 bought only half as much in Germany.

> [!note]- My correction
> 


Why PPP fails bc sometimes LOOP violation
Secondarily diferent weights per good, leading to strong PL variation  


---

## 5. The Big Mac Index
> 5. The BigMac Index
>
> Suppose the price of a Big Mac sandwich is \$5 in the US and ¥550 in Japan. The exchange rate quoted in the forex market is ¥100/\$. Is the Japanese yen overvalued or undervalued according to absolute purchasing power parity based on Big Mac's prices?

**Fill in:**
- PPP rate (¥ per \$) = ___ / ___ = ___
- Market rate = ¥100/\$
- At the market rate, \$5 buys ¥___ . Is that enough for a ¥550 Big Mac?
- So the yen is: 
- By how much (%): 

> [!check]- Answer
> PPP: 550 / 5 = **¥110/\$**. At the market rate, \$5 only gets ¥500, not enough for the ¥550 burger, so Japan is expensive in dollars. The yen buys more dollars than PPP says it should (¥100 per \$ instead of ¥110), so the **yen is overvalued**, by about **10%** ($\frac{110 - 100}{100}$).

> [!note]- My correction
> 


**Fill in:** why is the Big Mac a good test good? Which of the LOOP breaks in section 1 still hit it?
- 

---

## 6. Relative PPP
> 6. Relative PPP: the percentage change in the exchange rate just offsets the differential rates of inflation.
> $$1 + s(t,\$/€) = \frac{1 + \pi(t,\$)}{1 + \pi(t,€)}$$
> $$\Rightarrow s(t,\$/€) = \frac{\pi(t,\$) - \pi(t,€)}{1 + \pi(t,€)} \approx \pi(t,\$) - \pi(t,€)$$

**Claude's explanation (not in the handout):**
- $s$ is the percent change in the exchange rate (\$ per €).
- Watch the units: the **top** currency's inflation goes on **top**.

> [!note]- My correction
> 


**Fill in, in my words:** absolute PPP is about ___ ; relative PPP is about ___ .
- relative ppp is a function of the rate of change of inflation across economies

**Fill in:** US inflation 5%, euro area 2%. By relative PPP, does the dollar appreciate or depreciate against the euro, and by about how much?
- 

> [!check]- Answer
> $s \approx 5\% - 2\% = 3\%$: \$/€ rises 3%, so the **dollar depreciates about 3%** (exactly 1.05/1.02 − 1 = 2.94%). The country with higher inflation sees its currency fall.

> [!note]- My correction
> 

It's the relationship between absol. and rel. PPP 

---

## 7. Real exchange rate
> 7. Real exchange rate: the nominal exchange rate multiplied by the ratio of the price levels
> $$RS(t,\$/€) = \frac{S(t,\$/€) \times P(t,€)}{P(t,\$)}$$

**Claude's explanation (not in the handout):**
Read it: how many **US bundles** it takes to buy one **German bundle**. If absolute PPP holds, $RS = 1$.

IF RS=1.2 consumer price in EUR is 20% higher than US, and ergo euro in 20% overeval.
presuming PPP holds
When absol. PPP breaks


**Fill in, in my words:** the difference between the nominal rate and the real rate
- 

**Fill in:** using section 3's numbers, $RS$ = ___ . What does that number mean?
- 

> [!check]- Answer
> $RS$ = 1.25 × 160 / 100 = **2**. One German bundle costs as much as two US bundles. PPP would make it 1.

> [!note]- My correction
> 
The relative price of two consumption bundles, the RS val is =

---

## Exercise (handout): hamburgers and sushi
> Exercise:
> Suppose the US and Japan only consume two types of goods: hamburgers and sushi. In the US, hamburgers account for 60% of the consumption bundle and sushi accounts for 40%. In Japan, hamburgers account for 40% of the consumption bundle and sushi accounts for 60%. Both hamburgers and sushi satisfy the law of one price. In 2020, a hamburger is as expensive as a box of sushi. In 2021, the price of hamburgers increases by 10%, and the price of sushi falls by 20%.

> 1). Assume the price of a hamburger and the price of a box of sushi are both 100 in 2020. What is the rate of inflation in each country in 2021?
- Given: 
- 2021 prices: hamburger ___ , sushi ___
- US price level 2020 = ___ ; 2021 = 0.6 × ___ + 0.4 × ___ = ___
- Japan price level 2020 = ___ ; 2021 = 0.4 × ___ + 0.6 × ___ = ___
- $\pi_\$$ = ___ , $\pi_¥$ = ___

> [!check]- Answer 1
> Hamburger 110, sushi 80. US: 0.6(110) + 0.4(80) = 98, so **π\$ = −2%**. Japan: 0.4(110) + 0.6(80) = 92, so **π¥ = −8%**. Both deflate; Japan more, because it eats more of the good that got cheaper.

> [!note]- My correction
> 


> 2). Suppose the exchange rate in 2020 is ¥100/\$. What is the exchange rate in 2021 if relative purchasing power parity holds?
- Which currency is on top of the quote? ___ So its inflation goes on top.
- $1 + s$ = ___ / ___ = ___
- 2021 rate = 100 × ___ = ___
- Did the yen get stronger or weaker? Does that make sense given part 1?

> [!check]- Answer 2
> Quote is ¥/\$, so yen inflation on top: $1 + s = \frac{0.92}{0.98} = 0.9388$. 2021 rate = **¥93.88/\$**. The yen strengthens, which fits: Japan's prices fell more, so each yen buys more.

> [!note]- My correction
> 


> 3). Suppose that in 2021, the dollar weakens relative to the yen by 10% during 2021. What would be the magnitude of the real depreciation of the dollar relative to the yen?
- Relative PPP said the dollar should weaken ___ % (from part 2)
- It actually weakened 10%
- So the part not explained by inflation (the real depreciation) is about ___ %
- Exact: real change = (1 − 0.10) × ___ / ___ = ___

> [!check]- Answer 3
> PPP alone predicted the dollar falling about 6.1%. It fell 10%, so the real depreciation is roughly 10% − 6% = **about 4%**. Exact, with ¥/\$ falling 10%: $0.90 \times \frac{0.98}{0.92} = 0.9587$, a **real depreciation of about 4.1%**. (If you read "weakens 10%" as \$/¥ rising 10%, you get about 3.3%. Ask which reading she wants.)

> [!note]- My correction
> 


---

## Tie it to Lecture 3 (fill in)
- CIP and UIP said interest rates and exchange rates have to line up. PPP says ___ and exchange rates have to line up.
- If relative PPP holds and UIP holds, then high inflation countries should have high / low interest rates, because: 
- 

## My questions for lecture or office hours
- 

## Related
Previous: [[ECON 131 Lecture 3 - Interest Rate Parity]] · Course hub: [[ECON 131]] · Topic hub: [[Exchange Rates]]
