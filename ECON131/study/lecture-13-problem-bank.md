# ECON 131 Lecture 13 — Active-recall problem bank

Companion to [lecture-13-options.md](lecture-13-options.md). Source-aligned items marked **Handout**; all other numbers are **New practice**, not professor-assigned questions. Work without scrolling to the key. Status: **unattempted** until user actually works each one.

## Stage A — Identify and interpret (no calculator)

**P1 — Vocabulary (New).** Explain in one sentence each: call, put, strike price, maturity, European option, American option. Which side has a right and which side has the obligation?

**P2 — Payoffs (New).** A stock ends at $45, $80, or $120. For strike $80, find the call and put payoff in each state. Do not confuse payoff with option profit.

**P3 — Writers (New).** The owner of a call with K=$70 receives $25 at expiry. What is the underlying stock price? What does the option writer pay at expiry?

**P4 — Combined diagram (Handout).** Sell a 6-month call on Y with K=$200 and buy a 6-month put with K=$50. Write the piecewise terminal payoff and compute it at S=$0,$30,$50,$100,$200,$220,$250. Sketch the graph, marking the kinks.

## Stage B — Apply a formula (calculator optional)

**P5 — Put-call parity (New).** A European non-dividend-paying call and put each have K=$100, T=1 year. S0=$105, annual effective risk-free rate 5%, and put price $8. Find the call price; identify two portfolios whose terminal payoffs coincide.

**P6 — Comparative statics (New).** Holding the other factors fixed, what is the usual direction of change in a call's value as (i) S rises, (ii) K rises, (iii) volatility rises, (iv) the risk-free rate rises? Explain one in words.

**P7 — Hedge (Handout example extended).** S0=$50; next year S=$60 or $40; strike=$50; risk-free return=5.25%. List option payoffs, calculate the replicating call's stock quantity delta, and cash/borrowing B such that delta*S_T + 1.0525 B equals the option payoff in both states.

**P8 — Risk-neutral (Handout example extended).** Using P7, find the risk-neutral up probability q. Calculate the call and put prices and verify put-call parity.

## Stage C — Transfer and explain

**P9 — New binomial (New).** S0=$100; next year S=$120 or $90; K=$100; annual risk-free return=5%. Find call/put payoff pairs, q, both prices, and call delta. Verify your result using put-call parity. What is the downside stock *return*?

**P10 — Conceptual synthesis (New).** In 3–5 sentences: (i) why doesn't the risk-neutral probability necessarily describe the true chance of a price rise? (ii) why do replication and risk-neutral pricing agree? (iii) why could a quoted market option price different from the replicating portfolio's price create a trade in this model?

## Solutions — reveal only after attempting

**A1.** Call: right to buy; put: right to sell; K: contractual buy/sell price; T: expiry; European: exercise only at maturity; American: exercise any time up to maturity. Owner has the exercise right; writer owes the corresponding transaction if exercised.

**A2.** At S=$45: call $0, put $35; at $80: both $0; at $120: call $40, put $0.

**A3.** S=$95, since 95−70=25; call writer's payoff is −$25 (excluding option premium).

**A4.** If S<50, 50−S; if 50≤S≤200, 0; if S>200, 200−S. Payoffs: $50,$20,$0,$0,$0,−$20,−$50. Kinks at 50 and 200.

**A5.** C=P+S−PV(K)=8+105−100/1.05=**$17.7619**. Portfolios: call + bond paying K, versus put + one share.

**A6.** (i) usually up, (ii) down, (iii) up, (iv) usually up. More volatility benefits an option owner because downside exercise losses are floored at zero whereas upside gains remain possible. Qualifications apply to precise option structure and market assumptions.

**A7.** Stock up/down $60/$40; call up/down $10/$0. delta=(10−0)/(60−40)=0.5. Solve 0.5×60+1.0525B=10 -> B=−20/1.0525=**−$19.0024**. Up-state portfolio: 30−20=10; down-state: 20−20=0. Initial call price 0.5×50−19.0024=**$5.9976**.

**A8.** Up and down returns +20%,−20%. q=(0.0525+0.20)/0.40=**0.63125**. C=(0.63125×10)/1.0525=**$5.9976**. P=(0.36875×10)/1.0525=**$3.5036**. C+50/1.0525=P+50≈**$53.5036**.

**A9.** Call payoffs $20/$0, put payoffs $0/$10. Downside return is (90−100)/100=**−10%**; upside +20%. q=(0.05−(−0.10))/(0.20−(−0.10))=**0.5**. C=(0.5×20)/1.05=**$9.5238**; P=(0.5×10)/1.05=**$4.7619**. delta_call=(20−0)/(120−90)=**2/3** share. Check: 9.5238+100/1.05≈4.7619+100≈**$104.7619**.

**A10.** q is the probability that makes the stock's expected return equal the risk-free rate *in a hypothetical pricing world*; it isn't necessarily the market's empirical probability. A replicating share/cash portfolio and the derivative have identical payoffs in each possible state, so no-arbitrage requires the same price today. A pricing difference creates an opportunity to buy the cheaper payoff and sell the more expensive one, subject to trading and model assumptions.

## Tutor scoring protocol

| Outcome | Label | Next action |
|---|---|---|
| Correct, full reasoning without hint | solved | Ask why/transfer; record in **source-of-truth** ledger if available |
| Correct arithmetic after prompting | assisted | Repeat analogous problem cold later |
| Incorrect or missing concept | missed | Explain the minimum missing prerequisite and retest |
| Only read the answer | not attempted | No rep; preserve unattempted status |

If a student makes an arithmetic mistake, distinguish computation error from conceptual error; invite a corrected attempt before supplying the full solution.

### Review prompts for next sessions

- **Immediate:** define K, maturity, payoff, and choose exercise.
- **Next day:** redo P7 and P8 unassisted from the 50/40/60 inputs.
- **Delayed:** do P9 and explain q versus actual probability.
- **Exam readiness:** one independent problem for diagram, parity, and each binomial method, all correct without hints.
