# 6.3 Eurodollar Futures

The most popular interest rate futures contract in the United States is the **three-month Eurodollar futures contract** traded on the CME Group.

A **Eurodollar** is:

- A US dollar deposit
- Held in a bank outside the United States

The Eurodollar interest rate is essentially the same as:

# LIBOR (London Interbank Offered Rate)

It represents the interest rate at which banks lend US dollars to one another.

---

# Nature of the Eurodollar Futures Contract

A three-month Eurodollar futures contract is:

> A futures contract on the interest rate that will apply to a \$1 million deposit for a future three-month period.

The contract allows traders to:

- Speculate on future short-term interest rates
- Hedge future borrowing/lending costs
- Construct the LIBOR zero curve
- Manage money-market exposure

---

# Contract Characteristics

## Underlying

- Interest on \$1 million for 3 months

## Contract Months

Available maturities:

- March
- June
- September
- December

Contracts may extend:

- Up to 10 years into the future

Thus traders can take positions on future interest rates many years ahead.

---

# Final Settlement

The final settlement occurs:

- Two business days before the third Wednesday of the delivery month

At settlement:

$$
\text{Final Settlement Price} = 100 - R
$$

Where:

- \(R\) = 3-month LIBOR fixing
- Expressed with:
  - Quarterly compounding
  - Actual/360 day count convention

---

# Example — Final Settlement

Suppose:

- Final LIBOR fixing = 0.75%

Then:

$$
100 - 0.75 = 99.250
$$

Thus:

# Final settlement price = 99.250

After final settlement:

- All contracts are closed

---

# Price Quotation Convention

Eurodollar futures are quoted as:

$$
100 - \text{Interest Rate}
$$

This means:

| Futures Quote | Implied Interest Rate |
|---|---|
| 99.725 | 0.275% |
| 97.400 | 2.600% |
| 96.500 | 3.500% |

---

# Important Intuition

Because the quote is:

$$
100 - R
$$

there is an inverse relationship between:

- Interest rates
- Futures prices

---

# Relationship Between Futures Price and Interest Rates

## If Interest Rates Rise

- Futures prices fall

## If Interest Rates Fall

- Futures prices rise

Therefore:

| Position | Profits When |
|---|---|
| Long Futures | Rates fall |
| Short Futures | Rates rise |

---

# One Basis Point Rule

A very important feature of Eurodollar futures:

# A one-basis-point move equals \$25 per contract

---

# Why?

A basis point:

$$
0.01\% = 0.0001
$$

Contract principal:

$$
\$1,000,000
$$

Three-month period:

$$
0.25 \text{ years}
$$

Interest change:

$$
1,000,000 \times 0.0001 \times 0.25
=
25
$$

Thus:

# 1 basis point = \$25

---

# Trading Profit and Loss

## If Quote Increases by 1 Basis Point

- Long gains \$25
- Short loses \$25

## If Quote Decreases by 1 Basis Point

- Long loses \$25
- Short gains \$25

---

# Example — Daily Gain/Loss

Suppose settlement price changes:

$$
99.725 \rightarrow 99.685
$$

Difference:

$$
0.040
=
4 \text{ basis points}
$$

Loss to long position:

$$
4 \times 25
=
\$100
$$

Gain to short position:

$$
\$100
$$

---

# Contract Price Formula

Hull defines the contract price as:

$$
10,000
\left[
100 - 0.25(100-Q)
\right]
$$

Where:

- \(Q\) = futures quote

---

# Example — Contract Price

Suppose:

$$
Q = 99.725
$$

Then:

$$
10,000
\left[
100 - 0.25(100-99.725)
\right]
$$

$$
=
10,000
\left[
100 - 0.25(0.275)
\right]
$$

$$
=
10,000(99.93125)
$$

$$
=
999,312.5
$$

Thus:

# Contract Price = \$999,312.50

---

# Example — Final Contract Value

Suppose final quote becomes:

$$
99.615
$$

Then:

$$
10,000
\left[
100 - 0.25(100-99.615)
\right]
$$

$$
=
999,037.5
$$

Difference:

$$
999,312.5 - 999,037.5
=
275
$$

Thus:

# Long position loses \$275

---

# Hedging with Eurodollar Futures

Eurodollar futures are widely used for:

- Hedging future investments
- Locking future borrowing rates
- Locking future lending rates

---

# Example 6.3 — Locking in an Interest Rate

Suppose an investor wants to lock in the interest rate for:

- A future 3-month investment
- Principal = \$100 million

Current September Eurodollar futures quote:

$$
96.50
$$

Implied interest rate:

$$
100 - 96.50
=
3.5\%
$$

The investor buys:

# 100 contracts

---

# Suppose Actual Future Rate Becomes 2.6%

Final settlement price:

$$
100 - 2.6
=
97.40
$$

Price movement:

$$
97.40 - 96.50
=
0.90
=
90 \text{ basis points}
$$

---

# Profit on Futures Position

Each basis point:

$$
\$25
$$

Therefore:

$$
100 \times 25 \times 90
$$

$$
=
225,000
$$

Thus:

# Futures profit = \$225,000

---

# Interest Earned on Investment

Actual investment return:

$$
100,000,000
\times
0.25
\times
0.026
$$

$$
=
650,000
$$

---

# Total Effective Return

$$
650,000 + 225,000
=
875,000
$$

Equivalent interest rate:

$$
100,000,000
\times
0.25
\times
0.035
=
875,000
$$

Thus:

# Effective locked-in rate = 3.5%

---

# Important Reality — Hedge Is Not Perfect

Hull explains that the hedge is not exactly perfect because:

## 1. Futures Are Settled Daily

Cash flows occur every day via marking to market.

## 2. Timing Mismatch Exists

- Futures settle in September
- Actual investment interest received in December

This creates reinvestment risk.

---

# Hedge Adjustment

Hull suggests an approximate adjustment:

$$
\frac{1}{1 + 0.035 \times 0.25}
=
0.9913
$$

Adjusted contracts:

$$
100 \times 0.9913
=
99
$$

Thus:

# Use 99 contracts instead of 100

---

# Eurodollar Futures and the Yield Curve

Eurodollar futures provide information about:

- Future LIBOR expectations
- Interest rate term structure

Example from Hull:

| Future Date | Futures Rate |
|---|---|
| June 2013 | 0.275% |
| September 2013 | 0.295% |
| December 2013 | 0.325% |
| December 2015 | 0.900% |
| December 2017 | 2.270% |
| December 2019 | 3.324% |

This indicates:

# An upward-sloping yield curve

Meaning:

- Long-term interest rates are higher than short-term rates.

---

# Forward Rates vs Futures Rates

Eurodollar futures resemble:

# Forward Rate Agreements (FRAs)

because both lock in future interest rates.

---

# Important Difference Between FRAs and Futures

## Eurodollar Futures

- Settled daily
- Final settlement at time \(T_1\)

## FRA

- No daily settlement
- Settlement occurs at time \(T_2\)

---

# Two Major Differences

## 1. Daily Settlement Effect

Daily settlement creates cash flows during the contract life.

This changes contract value because:

- Gains occur when rates move favorably
- Margin cash can earn interest

This creates:

# Convexity Bias

---

## 2. Timing of Settlement

Futures:

- Settled earlier

FRAs:

- Payoff occurs later

Because of time value of money:

- Futures rates tend to exceed forward rates.

---

# Convexity Adjustment

Hull gives the convexity adjustment formula:

$$
\text{Forward Rate}
=
\text{Futures Rate}
-
\frac{1}{2}\sigma^2 T_1 T_2
$$

Where:

- \(\sigma\) = volatility of short-term rates
- \(T_1\) = maturity of futures contract
- \(T_2\) = maturity of underlying rate

---

# Key Insight

Convexity adjustment:

- Reduces futures rate
- Produces estimated forward rate

---

# Example 6.4 — Convexity Adjustment

Suppose:

$$
\sigma = 0.012
$$

8-year Eurodollar futures quote:

$$
94
$$

Implied futures rate:

$$
6\%
$$

Given:

$$
T_1 = 8
$$

$$
T_2 = 8.25
$$

---

# Calculate Adjustment

$$
\frac{1}{2}(0.012)^2(8)(8.25)
$$

$$
=
0.00475
$$

Thus:

$$
0.475\%
=
47.5 \text{ basis points}
$$

---

# Forward Rate Estimate

Continuous-compounding futures rate:

$$
6.038\%
$$

Adjusted forward rate:

$$
6.038 - 0.475
$$

$$
=
5.563\%
$$

Thus:

# Forward rate = 5.563%

---

# Important Observation

Hull notes:

# Convexity adjustment grows rapidly with maturity

| Maturity | Adjustment |
|---|---|
| 2 years | 3.2 bps |
| 4 years | 12.2 bps |
| 6 years | 27.0 bps |
| 8 years | 47.5 bps |
| 10 years | 73.8 bps |

Observation:

- Adjustment approximately grows with:
  
$$
T^2
$$

---

# Using Eurodollar Futures to Build the LIBOR Zero Curve

Eurodollar futures are frequently used to extend:

# The LIBOR zero curve

---

# Basic Idea

Known:

- Short-term LIBOR rates

Need:

- Longer-term zero rates

Eurodollar futures provide:

- Forward rates

These forward rates are bootstrapped into zero rates.

---

# Relationship Between Forward and Zero Rates

Hull derives:

$$
F_i
=
\frac{R_{i+1}T_{i+1} - R_iT_i}
{T_{i+1}-T_i}
$$

Rearranging:

$$
R_{i+1}
=
\frac{
F_i(T_{i+1}-T_i)
+
R_iT_i
}
{T_{i+1}}
$$

---

# Example 6.5 — Bootstrapping Zero Rates

Suppose:

400-day zero rate:

$$
4.80\%
$$

Forward rate for next 91 days:

$$
5.30\%
$$

---

# Compute 491-Day Zero Rate

$$
\frac{
0.053 \times 91
+
0.048 \times 400
}
{491}
$$

$$
=
0.04893
$$

Thus:

# 491-day zero rate = 4.893%

---

# Compute 589-Day Zero Rate

Next forward rate:

$$
5.50\%
$$

Then:

$$
\frac{
0.055 \times 98
+
0.04893 \times 491
}
{589}
$$

$$
=
0.04994
$$

Thus:

# 589-day zero rate = 4.994%

---

# 6.4 Duration-Based Hedging Strategies Using Futures

Duration is extremely important in interest rate risk management.

Suppose:

- A bond portfolio is being hedged
- Using interest rate futures

Define:

| Symbol | Meaning |
|---|---|
| \(V_F\) | Futures contract value |
| \(D_F\) | Duration of underlying futures asset |
| \(P\) | Portfolio value |
| \(D_P\) | Portfolio duration |

---

# Duration Approximation

For small yield changes:

$$
\Delta P
=
- P D_P \Delta y
$$

Similarly:

$$
\Delta V_F
=
- V_F D_F \Delta y
$$

---

# Duration-Based Hedge Ratio

Equating sensitivities gives:

$$
N
=
\frac{P D_P}
{V_F D_F}
$$

Where:

- \(N\) = number of futures contracts

This is called:

# Duration-Based Hedge Ratio

or

# Price Sensitivity Hedge Ratio

---

# Important Assumption

This approach assumes:

# Parallel shifts in the yield curve

Meaning:

- All interest rates move equally

This is a major limitation.

---

# Choosing the Correct Futures Contract

The hedger tries to choose futures contracts where:

$$
D_F \approx D_P
$$

---

# Typical Usage

| Futures Type | Usage |
|---|---|
| Eurodollar Futures | Short-term rates |
| Treasury Bond Futures | Long-term rates |
| Treasury Note Futures | Medium-term rates |

---

# Important Direction Rule

## If Rates Rise

- Bond prices fall
- Futures prices fall

## If Rates Fall

- Bond prices rise
- Futures prices rise

---

# Hedging Rule

| Exposure | Hedge |
|---|---|
| Lose when rates rise | Short futures |
| Lose when rates fall | Long futures |

---

# Example 6.6 — Duration Hedge

Suppose:

Portfolio value:

$$
\$10,000,000
$$

Portfolio duration:

$$
6.80
\text{ years}
$$

Current futures price:

$$
93-02 = 93.0625
$$

Contract value:

$$
93,062.50
$$

CTD bond duration:

$$
9.20
\text{ years}
$$

---

# Calculate Contracts

$$
N
=
\frac{
10,000,000
\times
6.80
}
{
93,062.50
\times
9.20
}
$$

$$
=
79.42
$$

Thus:

# Short 79 futures contracts

---

# Why Short Futures?

If rates rise:

- Bond portfolio loses value
- Short futures gains value

If rates fall:

- Bond portfolio gains value
- Short futures loses value

Thus hedge offsets interest-rate risk.

---

# Cheapest-to-Deliver Risk

In Treasury bond futures:

- Multiple deliverable bonds exist

The hedger assumes one bond will be CTD.

If market conditions change:

- Another bond may become CTD

This weakens hedge effectiveness.

---

# Business Snapshot — Asset Liability Management (ALM)

Banks carefully manage interest-rate exposure using:

# Asset Liability Management (ALM)

---

# GAP Management

Banks divide the yield curve into:

# Buckets

Examples:

- 0–1 month
- 1–3 months
- 3–6 months

Banks analyze:

- How portfolio value changes when one bucket shifts.

---

# Tools Used by Banks

Banks use:

- Swaps
- FRAs
- Bond futures
- Eurodollar futures
- Other interest-rate derivatives

---

# 6.5 Hedging Portfolios of Assets and Liabilities

Financial institutions often hedge by matching:

- Duration of assets
- Duration of liabilities

This is called:

# Duration Matching

or

# Portfolio Immunization

---

# Objective of Immunization

Protect against:

# Small parallel shifts in interest rates

---

# How It Works

If:

$$
\text{Asset Duration}
=
\text{Liability Duration}
$$

then:

- Gain on assets offsets loss on liabilities
- Portfolio becomes less sensitive to rates

---

# Limitation of Duration Matching

Duration matching only protects against:

# Parallel yield curve shifts

In reality:

- Short-term rates are more volatile
- Long-term rates move differently

Sometimes:

- Short rates rise
- Long rates fall

Therefore:

# Duration matching is only a first approximation

---

# Summary of Chapter Concepts

## Treasury Bond Futures

Important delivery options:

1. Delivery timing option
2. Choice of deliverable bond
3. Wild card option

These options:

# Reduce futures price

---

# Eurodollar Futures

- Based on future 3-month LIBOR
- Quoted as:
  
$$
100 - R
$$

- Used for:
  - Hedging
  - Speculation
  - Yield curve construction

---

# Convexity Adjustment

Necessary because:

- Futures ≠ forward contracts

Adjustment:

$$
\text{Forward Rate}
=
\text{Futures Rate}
-
\frac{1}{2}\sigma^2T_1T_2
$$

---

# Duration Hedging

Hedge ratio:

$$
N
=
\frac{PD_P}{V_FD_F}
$$

Purpose:

- Protect against interest-rate changes

---

# Core Intuition of Entire Chapter

This chapter connects:

- Futures pricing
- Bond sensitivity
- LIBOR markets
- Hedging
- Yield curves
- Duration management

Key ideas:

1. Interest rates and bond prices move inversely.
2. Eurodollar futures dominate short-term interest-rate trading.
3. Treasury futures contain embedded delivery options.
4. Duration measures interest-rate sensitivity.
5. Hedging works best under parallel yield-curve shifts.
6. Convexity adjustment is necessary when using futures to estimate forward rates.