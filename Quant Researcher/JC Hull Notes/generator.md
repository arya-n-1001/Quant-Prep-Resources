# 📝 Chapter 3: Hedging Strategies Using Futures - Comprehensive Summary

This chapter explored the core purpose of futures markets: to provide mechanisms for companies and investors to **reduce or offset specific price risks** (exposures) they face in their primary business activities.

## I. Basic Hedging Principles

The goal of hedging is to take a position in the futures market whose gains/losses offset the losses/gains in the real world (spot market), locking in a desired price or cost.

### A. Types of Hedges

| Hedge Type | Futures Position | When Appropriate (Your Exposure) |
| :--- | :--- | :--- |
| **Short Hedge** | **Sell** futures contracts (Short Position) | When the company **gains if the asset price increases** and **loses if the asset price decreases** (e.g., you own the asset and plan to sell it later). |
| **Long Hedge** | **Buy** futures contracts (Long Position) | When the company **loses if the asset price increases** and **gains if the asset price decreases** (e.g., you need to buy the asset later). |

## II. Arguments for and Against Hedging

While risk reduction should be universally welcomed, companies often face practical and theoretical resistance to hedging.

### A. Reasons Why Companies Hedge (Pro)

* **Focus on Core Competency:** Allows management to concentrate on their primary business (manufacturing, service delivery) rather than speculating on financial or commodity price variables (e.g., interest rates, exchange rates).
* **Avoid Surprises:** Stabilizes cash flow and profit margins by eliminating exposure to sharp, adverse price movements.

### B. Reasons Why Companies May Not Hedge (Con)

* **Shareholder Diversification (Theoretical):** Shareholders holding well-diversified portfolios have already eliminated much of the company's systematic risk. They may not require the company to hedge the same risk.
* **Competitive Risk (Practical):** If a company hedges but its competitors do not, the hedged company's profit margin may actually **fluctuate more** than its competitors' margins, making it appear risky in the short term.
* **Executive Criticism (Internal Risk):** If the price of the underlying asset moves favorably (i.e., the company makes a gain on the asset), the corresponding loss on the futures hedge may draw criticism from management or shareholders who do not understand the strategy's purpose.

## III. Managing Basis Risk

An important reality is that perfect hedges are rare, primarily due to **Basis Risk**.

### A. Definition of Basis

The basis is the difference between the asset's price in the real world and the price of the hedging contract:

$$\text{Basis} (b) = \text{Spot Price of Asset to be Hedged} (S) - \text{Futures Price of Contract Used} (F)$$

### B. Basis Risk

**Basis Risk** is the uncertainty surrounding the **value of the basis** at the time the hedge is closed out.

* **Impact:** The final effective price received or paid is **$F_{initial} + b_{final}$**. Since $F_{initial}$ is known, the final basis ($b_{final}$) is the source of residual risk.
* **Causes:** The two prices (Spot and Futures) may not move perfectly together due to:
    1.  The hedging asset being different from the underlying asset (**Cross Hedging**).
    2.  The futures contract being closed out before its delivery month.

## IV. Optimal Hedging and Quantification

### A. The Hedge Ratio

The **Hedge Ratio ($h$ or $h^*$ )** is the ratio of the size of the futures position to the size of the exposure ($\frac{\text{Size of Futures Position}}{\text{Size of Exposure}}$).

* If the assets are identical, the hedge ratio is often $1.0$.
* **Minimum Variance Hedge Ratio ($h^*$):** When assets are different (**Cross Hedging**), the optimal $h^*$ minimizes the variance (risk) of the final hedged position.
    * $h^*$ is calculated as the **slope of the best-fit line** obtained by regressing daily changes in the spot price ($\Delta S$) against daily changes in the futures price ($\Delta F$).
    $$
    h^* = \rho \frac{\sigma_S}{\sigma_F}
    $$
* **Optimal Number of Contracts ($N$):** Once $h^*$ is found, the number of contracts is:
    $$
    N = \frac{h^* \times \text{Exposure Quantity} (Q_A)}{\text{Futures Contract Size} (Q_F)}
    $$

## V. Stock Index Futures for Equity Hedging

Stock index futures are essential for managing **systematic risk** (market risk) in stock portfolios.

### A. Hedging with Beta ($\beta$)

The appropriate hedge size for an equity portfolio is determined by the portfolio's **Beta ($\beta$)**, which measures its sensitivity to the index.

* **Formula for Number of Contracts ($N$):**
    $$
    N = \beta \frac{V_A}{V_F}
    $$
    Where $V_A$ is the portfolio value and $V_F$ is the value of one futures contract (Futures Price $\times$ Multiplier).

### B. Changing Portfolio Beta

Futures allow fund managers to adjust their market exposure **without buying or selling the underlying stocks** (which saves transaction costs):

| Strategy Goal | Target Beta ($\beta_T$) | Action | Purpose |
| :--- | :--- | :--- | :--- |
| **Complete Hedge** | $\beta_T = 0$ | **Short** $N = \beta \frac{V_A}{V_F}$ contracts | Removes all market risk; locks in return near the risk-free rate; isolates stock-specific performance (alpha). |
| **Increase Risk** | $\beta_T > \beta$ | **Long** $N = (\beta_T - \beta) \frac{V_A}{V_F}$ contracts | Leverages the portfolio; provides immediate market exposure for a very bullish view. |
| **Decrease Risk** | $\beta_T < \beta$ | **Short** $N = (\beta - \beta_T) \frac{V_A}{V_F}$ contracts | Reduces volatility for a moderate bearish or highly cautious outlook. |

## VI. Stack and Roll Strategy

When the required hedge period is longer than any liquid futures contract available, the hedge must be rolled forward.

* **Procedure:** Enter a sequence of short-dated futures contracts. As the near contract approaches expiration, **close it out** and **immediately enter a new contract** with a later delivery month.
* **Result:** This effectively creates a long-dated futures position by stacking a series of short ones.
* **Primary Risk:** **Liquidity Risk** (Cash Flow Mismatch). If prices move adversely (e.g., falling in a long hedge), the daily margin calls create immediate cash outflows that may be difficult to meet, even if the long-term hedge proves profitable (as illustrated by the **Metallgesellschaft disaster**).