# Chapter 7 — Swaps (Part 1)

## J.C. Hull — *Options, Futures and Other Derivatives*

---

# Structure of Chapter 7

This chapter introduces one of the most important derivative instruments in modern finance:

# Swaps

Swaps are widely used by:

* Commercial banks
* Investment banks
* Corporations
* Hedge funds
* Governments
* Pension funds
* Insurance companies

The chapter is divided into three major areas:

| Part   | Topics                                                                                  |
| ------ | --------------------------------------------------------------------------------------- |
| Part 1 | Introduction to swaps, mechanics of interest rate swaps, comparative advantage argument |
| Part 2 | Valuation of swaps, currency swaps, market conventions                                  |
| Part 3 | Risks, applications, credit risk, advanced swap structures                              |

This document covers:

# Part 1 — Foundations of Swaps

---

# 7.1 Introduction to Swaps

A swap is:

> An agreement between two parties to exchange future cash flows according to predetermined rules.

The cash flows depend on:

* Interest rates
* Currency exchange rates
* Commodity prices
* Equity returns
* Credit events

The two most common types are:

1. Interest Rate Swaps
2. Currency Swaps

---

# Why Swaps Exist

Different market participants have different:

* Financing needs
* Credit quality
* Currency exposures
* Interest rate preferences

Swaps allow these participants to:

* Reduce borrowing costs
* Hedge risks
* Obtain desired cash flow structures
* Access markets indirectly
* Transform assets and liabilities

---

# Historical Background

The swap market developed rapidly during the 1980s.

Reasons for growth:

* Increased volatility in interest rates
* Globalization of capital markets
* Deregulation of banking systems
* Demand for flexible financing tools

Today, swaps represent one of the largest OTC derivatives markets in the world.

---

# Key Characteristics of Swaps

Swaps are generally:

* OTC (Over-the-Counter) contracts
* Customized agreements
* Long-term contracts
* Exposed to counterparty credit risk

Unlike exchange-traded futures:

* Swaps are privately negotiated
* Terms can be tailored
* There is no daily settlement through an exchange

---

# Basic Structure of a Swap

In a swap:

* One party agrees to make one set of payments
* Another party agrees to make another set of payments

The payments are exchanged periodically.

Typically:

* One stream is fixed
* One stream is floating

---

# Swap Terminology

| Term               | Meaning                                               |
| ------------------ | ----------------------------------------------------- |
| Notional Principal | Hypothetical principal used for interest calculations |
| Fixed Rate         | Predetermined interest rate                           |
| Floating Rate      | Variable interest rate linked to benchmark            |
| Swap Dealer        | Financial institution arranging swaps                 |
| Counterparty       | One of the two parties in the swap                    |
| Tenor              | Length of the swap agreement                          |

---

# Notional Principal

One of the most important concepts in swaps is:

# Notional Principal

The notional principal:

* Is NOT usually exchanged
* Is only used to calculate interest payments

Example:

Suppose:

* Notional principal = $100 million
* Fixed interest rate = 5%

Annual fixed payment:

$$
100,000,000 \times 0.05
=======================

5,000,000
$$

The $100 million itself is normally never exchanged.

---

# 7.2 Interest Rate Swaps

The most common swap is:

# Interest Rate Swap

An interest rate swap is:

> An agreement to exchange interest payments on the same notional principal for a specified period.

Usually:

* One party pays fixed
* One party pays floating

---

# Typical Floating Rate Benchmark

The floating rate is commonly based on:

* LIBOR (historically)
* SOFR (modern markets)
* EURIBOR
* Treasury bill rates

In Hull’s examples:

# LIBOR is primarily used.

---

# Plain Vanilla Interest Rate Swap

The simplest and most common swap is:

# Plain Vanilla Interest Rate Swap

Structure:

| Party   | Pays          | Receives      |
| ------- | ------------- | ------------- |
| Party A | Fixed Rate    | Floating Rate |
| Party B | Floating Rate | Fixed Rate    |

---

# Example — Basic Interest Rate Swap

Suppose:

* Notional principal = $100 million
* Fixed rate = 5%
* Floating rate = 6-month LIBOR
* Payments every 6 months
* Swap maturity = 3 years

Party A:

* Pays fixed 5%
* Receives LIBOR

Party B:

* Pays LIBOR
* Receives fixed 5%

---

# Calculating Swap Cash Flows

Suppose 6-month LIBOR for first payment period is:

$$
4.2%
$$

Floating payment:

$$
100,000,000
\times
0.042
\times
0.5
===

2,100,000
$$

Fixed payment:

$$
100,000,000
\times
0.05
\times
0.5
===

2,500,000
$$

Net payment from fixed-rate payer:

$$
2,500,000 - 2,100,000
=====================

400,000
$$

Thus:

# Party paying fixed pays net $400,000

---

# Important Practical Feature

In practice:

# Only net cash flows are exchanged

This reduces:

* Transaction costs
* Operational complexity
* Credit exposure

---

# Financial Interpretation of Interest Rate Swaps

An interest rate swap can transform:

| Original Exposure       | After Swap              |
| ----------------------- | ----------------------- |
| Floating-rate liability | Fixed-rate liability    |
| Fixed-rate liability    | Floating-rate liability |
| Floating-rate asset     | Fixed-rate asset        |
| Fixed-rate asset        | Floating-rate asset     |

---

# Why Companies Use Interest Rate Swaps

A company may:

* Prefer fixed borrowing costs
* Prefer floating borrowing costs
* Expect interest rates to change
* Hedge future financing needs
* Match asset and liability cash flows

Swaps provide flexibility without refinancing existing debt.

---

# Fixed vs Floating Preference

## Fixed Rate Preference

Companies preferring certainty:

* Prefer fixed-rate liabilities
* Want predictable interest payments

Examples:

* Pension funds
* Insurance firms
* Conservative corporations

---

## Floating Rate Preference

Companies expecting falling interest rates may prefer:

* Floating-rate liabilities

Advantages:

* Benefit when rates decline
* Potentially lower financing costs

---

# Swap Dealer

Most swaps are arranged through:

# Financial Intermediaries

called:

# Swap Dealers

Examples:

* JPMorgan
* Goldman Sachs
* Citibank
* Barclays

Swap dealers:

* Match counterparties
* Quote swap rates
* Manage risk
* Earn bid-ask spreads

---

# Role of Financial Institutions

Financial institutions often:

* Enter offsetting swaps
* Hedge exposures dynamically
* Act as market makers

Thus swap markets are highly dealer-driven.

---

# 7.3 Comparative Advantage Argument

Hull next explains the classical explanation for why swaps exist:

# Comparative Advantage

This is one of the most famous ideas in swap markets.

---

# Basic Idea

Different firms have:

* Different credit ratings
* Different borrowing costs

A company may have:

* Better access to fixed-rate markets
* Worse access to floating-rate markets

Another company may have the opposite advantage.

A swap allows both companies to benefit.

---

# Example Setup

Suppose:

## Company X

Can borrow at:

| Market   | Borrowing Rate |
| -------- | -------------- |
| Fixed    | 5.0%           |
| Floating | LIBOR + 0.2%   |

---

## Company Y

Can borrow at:

| Market   | Borrowing Rate |
| -------- | -------------- |
| Fixed    | 6.5%           |
| Floating | LIBOR + 1.0%   |

---

# Observing Comparative Advantage

Difference in fixed-rate borrowing:

$$
6.5 - 5.0 = 1.5%
$$

Difference in floating-rate borrowing:

$$
1.0 - 0.2 = 0.8%
$$

Thus:

# Company X has stronger comparative advantage in fixed-rate borrowing.

---

# Desired Preferences

Suppose:

| Company | Wants                   |
| ------- | ----------------------- |
| X       | Floating-rate borrowing |
| Y       | Fixed-rate borrowing    |

Then:

* X borrows fixed
* Y borrows floating
* They enter swap agreement

---

# Total Potential Gain

Potential gain:

$$
1.5% - 0.8%
===========

0.7%
$$

This gain can be shared between:

* Company X
* Company Y
* Swap dealer

---

# Intuition Behind Comparative Advantage

Even though:

# Company X is better in both markets

its advantage is:

* Larger in fixed-rate market
* Smaller in floating-rate market

Therefore:

* X should borrow where it is relatively strongest
* Y should borrow where it is relatively weakest

Then swap cash flows create desired exposure.

---

# Important Insight from Hull

Hull emphasizes:

# Comparative advantage is not the whole story.

Modern explanations include:

* Market segmentation
* Regulatory differences
* Tax effects
* Credit considerations
* Balance-sheet management
* Hedging needs

Nevertheless, comparative advantage remains the classical explanation.

---

# Mechanics of the Swap Arrangement

Typical process:

## Step 1

Each company borrows where it has advantage.

## Step 2

Swap dealer arranges swap.

## Step 3

Cash flows exchanged periodically.

## Step 4

Both companies achieve preferred financing structure.

---

# Visual Interpretation of Swap

The swap transforms:

$$
\text{Original Borrowing}
\rightarrow
\text{Desired Borrowing Exposure}
$$

without refinancing debt directly.

---

# Important Advantages of Swaps

## 1. Flexibility

Customized agreements.

---

## 2. Cost Reduction

Can reduce effective borrowing costs.

---

## 3. Risk Management

Helps hedge interest-rate risk.

---

## 4. Market Access

Allows indirect access to markets.

---

## 5. Asset-Liability Matching

Useful for banks and financial institutions.

---

# Risks of Swaps

Although swaps are useful, they involve important risks.

## Counterparty Risk

One party may default.

---

## Market Risk

Interest rates may move adversely.

---

## Liquidity Risk

Some swaps may be difficult to unwind.

---

## Operational Risk

Documentation and settlement errors may occur.

---

# Key Formulas from Part 1

## Fixed Payment

$$
\text{Notional Principal}
\times
\text{Fixed Rate}
\times
\text{Time Fraction}
$$

---

## Floating Payment

$$
\text{Notional Principal}
\times
\text{Floating Rate}
\times
\text{Time Fraction}
$$

---

## Net Swap Payment

$$
\text{Fixed Payment}
--------------------

\text{Floating Payment}
$$

---

## Comparative Advantage Gain

$$
\text{Difference in Fixed Spreads}
----------------------------------

\text{Difference in Floating Spreads}
$$

---

# Key Exam Concepts

You must understand:

* Definition of swaps
* OTC nature of swaps
* Interest rate swaps
* Notional principal
* Fixed vs floating payments
* Net settlement
* Comparative advantage argument
* Swap dealer role
* Risks of swaps

---

# Final Intuition of Part 1

Core intuition:

1. Swaps are agreements to exchange future cash flows.
2. Interest rate swaps transform fixed exposure into floating exposure or vice versa.
3. The notional principal is usually not exchanged.
4. Only net cash flows are typically settled.
5. Comparative advantage explains how two firms can both benefit from a swap.
6. Swaps are powerful tools for financing and risk management.
7. Swap markets are primarily dealer-driven OTC markets.
