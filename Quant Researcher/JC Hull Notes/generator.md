### 5.5 Forward Price with Known Income
Many investment assets generate predictable cash income, such as stocks paying dividends or bonds paying coupons. The pricing formula must be adjusted to account for this income.

#### The Argument
If you buy the asset today, you receive the income. If you buy a forward contract, you *do not* receive the income paid during the life of the contract. Therefore, the forward price must be lower to reflect this missed income.
*   We define \( I \) as the **present value** of all income payments expected during the life of the forward contract.
*   We subtract \( I \) from the spot price \( S_0 \) to get the "net" cost of the asset.

#### The Formula
For an investment asset providing a known cash income with present value \( I \):
\[ F_0 = (S_0 - I)e^{rT} \]

#### Arbitrage Example
*   **Asset Price (\(S_0\)):** $900
*   **Income:** $40 coupon in 4 months.
*   **Interest Rates:** 3% (4-month) and 4% (9-month).
*   **Maturity:** 9 months.

1.  **Calculate PV of Income (\(I\)):**
    \[ I = 40e^{-0.03 \times (4/12)} = \$39.60 \]
2.  **Calculate No-Arbitrage Price:**
    \[ F_0 = (900 - 39.60)e^{0.04 \times 0.75} = 860.40e^{0.03} = \$886.60 \]

If \(F_0 > \$886.60\), arbitrageurs profit by **buying the asset** and **shorting the forward**. (They receive the coupon to help pay borrowing costs).
If \(F_0 < \$886.60\), arbitrageurs profit by **shorting the asset** and **buying the forward**. (They invest the short proceeds to cover the coupon payment they owe).

***

This is a very common point of confusion! The intuition is actually the opposite of what you might expect.


Here is the step-by-step breakdown of why the formula is \( F_0 = (S_0 - I)e^{rT} \).

### 1. The "Stock Price Drop" Mechanism
When a stock pays a dividend, the stock price generally **drops** by the amount of that dividend.

*   Imagine a stock is $100.
*   It pays a $5 dividend tomorrow.
*   Tomorrow, the stock will trade at roughly \$95. (Because the company just gave away $5 of value per share).

The **Forward Price** is a prediction of what the stock price will be in the future. Since the stock price is going to drop by $5 when the dividend is paid, the Forward price must account for that drop.

### 2. The Arbitrage Argument (The "Net Cost" View)
Let's look at the cost of acquiring the stock at time \(T\) using two different methods. To prevent arbitrage, these two costs must be equal.

**Method A: Buy the Forward**
*   You enter a contract to buy the stock at time \(T\).
*   **Cost at time T:** \( F_0 \)

**Method B: Buy the Stock Now (and borrow money to do it)**
*   You borrow money to buy the stock today at price \( S_0 \).
*   However, you know you will receive a dividend (Income) during this time.
*   You can use that dividend to pay back part of your loan.
*   Therefore, you don't need to borrow the full \( S_0 \). You only need to borrow the **Net Cost**: \( S_0 - I \).
*   The bank charges you interest on this borrowed amount.
*   **Cost at time T:** \( (S_0 - I)e^{rT} \)

**Conclusion:**
Since Method A and Method B both result in you owning the stock at time \(T\), their costs must be equal:
\[ F_0 = (S_0 - I)e^{rT} \]

### 3. A Numerical Example
Let's look at why your intuition ("S + I") would lead to free money (arbitrage) for someone else.

*   **Stock Price (\(S_0\)):** $100
*   **Dividend (PV):** $5 (Paid just before maturity)
*   **Interest Rate:** 0% (to keep it simple).

**Scenario 1 (Correct Formula):**
The Forward Price should be \( 100 - 5 = \$95 \).
*   Why? Because at maturity, the stock will likely be $95 (after the dividend drop).

**Scenario 2 (If we added, like you suggested):**
Suppose the Forward Price was **\$105** ($100 + $5).
*   **My Strategy:**
    1.  I buy the stock now for $100.
    2.  I short the forward (agree to sell it to you for $105).
    3.  I wait. I receive the \$5 dividend. (Now I have $5 cash + Stock).
    4.  At maturity, I sell you the stock for \$105 (per the contract).
*   **My Total Profit:** \$105 (from you) + \$5 (dividend) - \$100 (cost) = **$10 Profit**.
*   This is "free money" (arbitrage). The market would never allow this. The price would be forced down.

### Summary
You subtract \(I\) because the **Forward price predicts the future stock price**, and the future stock price decreases every time a dividend is paid out.

### 5.6 Forward Price with Known Yield
Instead of fixed cash amounts (like $40), some assets pay income as a percentage of the asset's price (yield). This is common for currencies or stock indices.
*   **Notation:** \( q \) is the average annual yield (continuously compounded).

#### The Formula
Since the income scales with the asset price, we adjust the growth rate in the exponent:
\[ F_0 = S_0 e^{(r-q)T} \]

*   **Logic:** The asset yields \(q\), which offsets the cost of carry \(r\). The net cost of holding the asset is \(r - q\).

#### Example
*   **Asset Price:** $25
*   **Risk-Free Rate (\(r\)):** 10%
*   **Dividend Yield:** 4% semiannually \(\rightarrow\) 3.96% continuous (\(q = 0.0396\)).
*   **Maturity:** 6 months (0.5 years).
    \[ F_0 = 25 e^{(0.10 - 0.0396) \times 0.5} = 25 e^{0.0302} = \$25.77 \]

***

### 5.7 Valuing Forward Contracts
It is crucial to distinguish between the **Forward Price (\(F_0\))** and the **Value of the Contract (\(f\))**.
*   **At Inception:** The delivery price \(K\) is set equal to the current forward price \(F_0\). Therefore, the value \(f\) is **zero**.
*   **Later:** As time passes, the market forward price \(F_0\) changes, but your contracted delivery price \(K\) stays fixed. The contract now has positive or negative value.

#### General Valuation Formula
The value of a **long** forward contract (agreement to buy at \(K\)) is the present value of the difference between the current forward price and the delivery price:
\[ f = (F_0 - K)e^{-rT} \]

**Alternative Forms (Substituting \(F_0\)):**
*   **No Income:** \( f = S_0 - Ke^{-rT} \)
*   **Known Cash Income:** \( f = S_0 - I - Ke^{-rT} \)
*   **Known Yield:** \( f = S_0 e^{-qT} - Ke^{-rT} \)

#### Mark-to-Market: Forwards vs. Futures
*   **Futures:** Gains/losses are settled daily. If the price moves by \$1, you get $1 immediately.
*   **Forwards:** Gains/losses are realized only at maturity. If the price moves by \$1, your profit is the **present value** of $1 discounted from maturity to today.

***

### 5.8 Forward vs. Futures Prices
Are forward prices and futures prices theoretically identical?
*   **Constant Interest Rates:** Yes. If \(r\) is constant, \(F_{forward} = F_{futures}\).
*   **Stochastic Interest Rates:** No, they diverge slightly due to daily settlement (marking to market).

#### Correlation Argument
The difference depends on the correlation between the **Asset Price (\(S\))** and **Interest Rates (\(r\))**.
1.  **Positive Correlation:**
    *   When \(S\) rises, you make a profit on futures. Since \(r\) likely rose too, you reinvest that profit at a *higher* rate.
    *   When \(S\) falls, you lose money. Since \(r\) likely fell, you finance that loss at a *lower* rate.
    *   *Result:* Futures are more attractive \(\rightarrow\) **Futures Price > Forward Price**.
2.  **Negative Correlation:**
    *   The opposite happens. You lose money when rates are high and make money when rates are low.
    *   *Result:* Forward contracts are more attractive \(\rightarrow\) **Forward Price > Futures Price**.

*Practical Note:* For most short-term contracts (months), the difference is negligible, and we assume \(F_{forward} = F_{futures}\). The major exception is **Eurodollar Futures** (discussed in Chapter 6), where the difference is significant.