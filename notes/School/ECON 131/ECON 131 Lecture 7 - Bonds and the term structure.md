---
type: lecture
parent: "[[ECON 131]]"
domain: econ
course: "ECON 131"
status: draft
---
Source: `ECON131 Lecture 07 - Bonds and the term structure.pdf` (Chenyue Hu), 2 pages. Your live class notes are in [[Econ 131 Lecture 7]] (currency crises, three pillars). This note is the handout.

## The map

Money today and money later are different goods. Everything here is one move: **discount each future cash flow back to today, then add**. A bond is a stack of future cash flows, so its price is that sum. The rate that makes the sum equal the market price is the yield. The rates for each maturity, read off bonds of different lengths, are the term structure.

## 1. Compound interest

> Compound interest rates – used when interest is calculated but not paid.

$$1 + r = (1+r_1)(1+r_2)\cdots(1+r_n)$$

(The handout prints this as $r=(1+r_1)\cdots(1+r_n)-1$.) Growth factors multiply. Rates do not add.

## 2. Nominal versus effective rate

> Nominal/stated rate versus effective rate. Nominal annual rate and six-month rate; effective annual rate and six-month rate.

$$r_{1yr} = \left(1+\frac{i_{1yr}}{n}\right)^{n}-1$$

- $i_{1yr}$ is the stated annual rate, $n$ is compounding periods per year.
- Going the other way, the per-period rate that compounds to an effective annual rate $r$ is $(1+r)^{1/n}-1$. Example: $r=1\%$ gives a six-month rate of $1.01^{1/2}-1\approx 0.4988\%$, not $0.5\%$.

My correction:

## 3. Present value and future value

> With $n$ periods and interest rate $r$ in each period,

$$FV = PV(1+r)^n, \qquad PV = \frac{FV}{(1+r)^n}$$

**Handout example.** Michael wants an asset worth \$120,000 in two years. How much to deposit at 7% per year compounded annually? What if compounded quarterly?

- Annually: $PV = \dfrac{120{,}000}{1.07^2} = \$104{,}812.65$
- Quarterly: 8 periods at $0.07/4 = 1.75\%$, so $PV = \dfrac{120{,}000}{1.0175^{8}} = \$104{,}449.39$
- Quarterly compounding earns more per year, so you need to deposit less.

My correction:

## 4. Bond

> Bond: a financial asset that promises its owner periodic interest payment, in addition to the face value of the bond.
> - Face value: the nominal value of the bond, or the bond's principal. This is the amount that the issuer of the bond promises to pay the investor when the bond matures.
> - Coupon: the periodic amount that the owners of the bond receive as interest payment.

> Discount factor: present value of \$1 at time $t$.

$$PV = \frac{c}{1+r}+\frac{c}{(1+r)^2}+\cdots+\frac{c}{(1+r)^n}+\frac{F}{(1+r)^n} = c\times\frac{(1+r)^n-1}{r(1+r)^n}+\frac{F}{(1+r)^n}$$

Here $c$ is the coupon and $F$ is the face value. The fraction multiplying $c$ is the closed form for the sum of $n$ discount factors (an annuity).

**Handout example.** Face \$1,000, matures in 10 years, pays 7% per year, discount rate 5%. Coupon $c = 70$.

$$PV = 70\times\frac{1.05^{10}-1}{0.05\times 1.05^{10}}+\frac{1000}{1.05^{10}} = 540.52+613.91 = \$1{,}154.43$$

It sells above face because the coupon (7%) beats the discount rate (5%).

My correction:

### Yield to maturity

> Yield to maturity (ytm): rate of return earned by an investor who buys the bond today, assuming the bond will be held until maturity.

$$PV = \frac{c}{1+ytm}+\frac{c}{(1+ytm)^2}+\cdots+\frac{c+F}{(1+ytm)^n}$$

Same equation, but now the price is known and you solve for the rate. Price and ytm move in opposite directions.

My correction:

## 5. Term structure

> Term structure: the relationship between short- and long-term spot interest rates.
> Spot interest rate $r_t$: discount rate for the cash flows that take place at time $t$.

**Handout example.** Face value 100. Find the 1-, 2-, 3-year spot rates from this table (an image on page 2):

| Maturity | Coupon | Price |
|---|---|---|
| 1 | 0 | 95.22 |
| 2 | 4.5 | 99.40 |
| 3 | 5 | 99.16 |
| 4 | 6 | 99.91 |
| 5 | 5.5 | 98.38 |

Peel off one maturity at a time. Each new bond's earlier cash flows are priced with the spot rates you already have, and its last cash flow gives the next spot rate.

1. 1-year, no coupon: $95.22 = \dfrac{100}{1+r_1} \Rightarrow r_1 = 5.02\%$
2. 2-year: $99.40 = \dfrac{4.5}{1+r_1}+\dfrac{104.5}{(1+r_2)^2}$. The first term is $4.29$, so $\dfrac{104.5}{(1+r_2)^2}=95.11 \Rightarrow r_2 = 4.82\%$
3. 3-year: $99.16 = \dfrac{5}{1+r_1}+\dfrac{5}{(1+r_2)^2}+\dfrac{105}{(1+r_3)^3}$. The first two terms are $4.76+4.55$, so $\dfrac{105}{(1+r_3)^3}=89.85 \Rightarrow r_3 = 5.33\%$

The curve is 5.02, 4.82, 5.33. It dips at year 2, then rises at year 3. The handout says the term structure "generally" rises, and this data only mostly does.

My correction:

### Why the term structure usually rises (three reasons)

> 1) Belief that short term interest rate will be higher in the future.

> Suppose there are two investment options. You can do a long-run investment at two-year annual rate of $r_2$, or you can do a short-term investment with current one-year rate of $r_1$. Which investment you choose will depend on your forecast of future one-year rate $r_{fut}$.

> The expectations hypothesis: long-term interest rates are a weighted average of the current short-term rate and expected future short-term rates.

For two years, the two routes should end up equal:

$$(1+r_2)^2 = (1+r_1)(1+r_{fut}), \qquad 1+r_2=\sqrt{(1+r_1)(1+r_{fut})}$$

If you expect $r_{fut}>r_1$, then $r_2>r_1$.

> 2) Risk of higher future inflation.

> Fisher Equation: $1 + r_{nominal} = (1+r_{real})\times(1+\pi)$

Lenders on long bonds want compensation for expected inflation, which raises the nominal rate on longer maturities.

> 3) Greater exposure of long-term bonds to changes in interest rates.

A long bond's price moves more when rates change, so holders demand extra yield for that risk.

My correction:

## Exercises

> Calculate the price of bonds in the following cases when the effective annual discount rate is 1%. Assume the face value is \$100.

1. **A 6-month Treasury with no coupon.** One cash flow of 100 at half a year. $PV = \dfrac{100}{1.01^{0.5}} = \$99.50$
2. **A 2-year U.S. corporate bond that pays 5% in the first year and 2% in the second year.** Cash flows 5 and $2+100$. $PV=\dfrac{5}{1.01}+\dfrac{102}{1.01^2}=4.95+99.99=\$104.94$
3. **A Consol that pays 2% per year indefinitely.** No face value is repaid, so it is a perpetuity. $PV=\dfrac{c}{r}=\dfrac{2}{0.01}=\$200$
4. **A 1-year Treasury with an annual coupon of 1.5% paid semi-annually.** Coupon is $0.75$ at 6 months and $0.75+100$ at 12 months. The six-month rate is $1.01^{0.5}-1$, so $PV=\dfrac{0.75}{1.01^{0.5}}+\dfrac{100.75}{1.01}=0.75+99.75=\$100.50$

My correction:

## Connections

- Discounting across time is the same comparison as [[ECON 131 Lecture 3 - Interest Rate Parity (fill-in)]].
- The Fisher equation ties to inflation differences in [[ECON 131 Lecture 4 - Purchasing Power Parity]].
