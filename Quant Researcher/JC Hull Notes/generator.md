# 📝 Chapter 3: Hedging Strategies Using Futures (Part 2)

## 1. Arguments For and Against Hedging (Section 3.2)

### A. Arguments FOR Hedging (The Obvious Case)

1.  **Focus on Core Business:** Most non-financial companies specialize in manufacturing, retailing, or services, **not** predicting market variables (like interest rates or commodity prices). Hedging allows management to focus on their main area of expertise.
2.  **Avoid Unpleasant Surprises:** Hedging prevents sudden, sharp losses due to adverse price movements (e.g., a massive spike in the price of a raw material).

### B. Arguments AGAINST Hedging (The Skeptical Case)

| Argument | Detailed Explanation and Counterpoints |
| :--- | :--- |
| **Shareholders Can Hedge** | Shareholders can, theoretically, hedge the risk themselves. However: 1. **Information Asymmetry:** Shareholders often lack the real-time, detailed information about the company's risks that management possesses. 2. **Transaction Costs:** Hedging is cheaper when done in large transactions by the company than by many individual shareholders. |
| **Shareholders are Diversified** | A well-diversified shareholder may own shares in both the buyer and seller of a commodity (e.g., a copper user and a copper producer). Thus, the shareholder's portfolio risk is already mitigated, making corporate hedging redundant. |
| **Competitive Pressures (The Gold Jewelry Example)** | If competitors *don't* hedge, a company that *does* hedge may see its profit margins fluctuate wildly. 1. **Unhedged Competitor (TakeaChance Co.):** If gold prices rise, they pay more for gold, but the wholesale jewelry price also rises. **Profit margin is stable.** 2. **Hedged Company (SafeandSure Co.):** If gold prices rise, they are forced to sell futures at a loss (**Loss on Hedge**). Even though the jewelry selling price rises, the loss on the hedge reduces their profit margin, which may even become negative. |
| **Hedging Can Lead to a Worse Outcome** | When prices move favorably, the hedge causes a loss that offsets a real-world gain, leading to lower-than-possible profits. |
| **The "Rogue Treasurer" Problem** | Hedging reduces **company risk**, but it can increase **treasurer risk**. If the price moves favorably, the treasurer has to justify the "loss" on the futures market to executives who may not fully understand the concept. |

**Key Takeaway (The "Big Picture"):** If a company decides to hedge, it must first ensure **all senior executives fully understand** the strategy, and that the strategy accounts for **competitive dynamics** within the industry.

---

## 2. Basis Risk (Section 3.3)

### A. The Definition of Basis

Basis risk arises because the hedged asset price and the futures price do not move perfectly together.

$$
\text{Basis} (b) = \text{Spot price of asset to be hedged} (S) - \text{Futures price of contract used} (F)
$$
* **Strengthening of the Basis:** An increase in the basis ($b_2 > b_1$). $S$ rises relative to $F$.
* **Weakening of the Basis:** A decrease in the basis ($b_2 < b_1$). $F$ rises relative to $S$.
* **At Expiration:** If the asset being hedged is the same as the asset underlying the futures contract, the basis should be **zero** at the contract's expiration.

### B. Causes of Basis Risk (Why Hedges are Not Perfect)

1.  **Cross Hedging:** The asset being hedged is **different** from the asset underlying the futures contract (e.g., hedging jet fuel price with crude oil futures).
2.  **Date Uncertainty:** The hedger is **uncertain** of the exact date the asset will be bought or sold.
3.  **Early Closure:** The hedge requires the futures contract to be **closed out before its delivery month**.

### C. Calculating the Effective Price (Short Hedge Example)

Assume a short hedge is placed at $t_1$ and closed out at $t_2$.

* **Final Cash Flow:** The hedger sells the asset spot at $S_2$ and makes a profit/loss on the futures: $(F_1 - F_2)$.
* **Effective Price Received:**
    $$
    \text{Effective Price} = S_2 + (F_1 - F_2)
    $$
* **Basis Formula Simplification:** We know $S_2 = F_2 + b_2$. Substituting this into the equation:
    $$
    \text{Effective Price} = (F_2 + b_2) + (F_1 - F_2) = F_1 + b_2
    $$
* **The Risk:** The final effective price is known to be $F_1 + b_2$. Since $F_1$ is known today, the only uncertainty is the final basis ($b_2$). **Basis risk is the uncertainty associated with $b_2$.**

**Example Calculation (Short Hedge):**

| Time | Spot Price (S) | Futures Price (F) | Basis ($b = S - F$) |
| :--- | :--- | :--- | :--- |
| **$t_1$ (Initial)** | $S_1 = \$2.50$ | $F_1 = \$2.20$ | $b_1 = \$0.30$ |
| **$t_2$ (Close Out)** | $S_2 = \$2.00$ | $F_2 = \$1.90$ | $b_2 = \$0.10$ |

1.  **Profit on Futures:** $F_1 - F_2 = \$2.20 - \$1.90 = \$0.30$
2.  **Effective Price Received:** $S_2 + (F_1 - F_2) = \$2.00 + \$0.30 = \mathbf{\$2.30}$
3.  **Check with Basis Formula:** $F_1 + b_2 = \$2.20 + \$0.10 = \mathbf{\$2.30}$

### D. Impact of Basis Changes

| Hedge Type | Basis Change | Effect on Hedger's Position |
| :--- | :--- | :--- |
| **Short Hedge (Selling)** | **Strengthens ($b \uparrow$)** | **Improves:** $S$ increases relative to $F$. The hedger sells their asset at a higher price relative to their futures loss. |
| **Short Hedge (Selling)** | **Weakens ($b \downarrow$)** | **Worsens:** $F$ increases relative to $S$. The hedger's futures gain is less than expected, or futures loss is more than expected. |
| **Long Hedge (Buying)** | **Strengthens ($b \uparrow$)** | **Worsens:** $S$ increases relative to $F$. The hedger buys their asset at a higher price relative to their futures gain. |
| **Long Hedge (Buying)** | **Weakens ($b \downarrow$)** | **Improves:** $F$ increases relative to $S$. The hedger pays a lower price for the asset relative to their futures loss. |

### E. Cross Hedging

* **Definition:** Using a futures contract on an asset **different** from the asset being hedged (e.g., hedging the price of heating oil with a crude oil futures contract).
* **Basis Components in Cross Hedging:**
    1.  **$S^* - F$:** The basis that would exist if the asset being hedged ($S$) were the same as the futures asset ($S^*$).
    2.  **$S - S^*$:** The basis arising from the price difference between the two different assets.

### F. Choice of Futures Contract

The goal is to minimize basis risk. This involves two choices:

1.  **Underlying Asset:** Choose the contract whose futures price is **most closely correlated** with the price of the asset being hedged.
2.  **Delivery Month:**
    * **Rule of Thumb:** Choose a delivery month that is as **close as possible to, but later than, the expiration of the hedge**.
    * **Example:** For a hedge expiring in December, January, or February, use the **March** contract.
    * **Why Later?** Futures prices are often **erratic during the delivery month**. Also, long hedgers risk being forced to take delivery if they hold the contract too long.
    * **Liquidity Caveat:** This rule must be balanced by the fact that **short-maturity contracts often have the greatest liquidity**.

**Example 3.1: Short Hedge (Yen Currency)**

* **Exposure:** Expect to **receive $\text{¥}50$ million** (Short Hedge) at the end of **July**.
* **Contract Used:** September Yen Futures (4 contracts).
* **$t_1$ (March 1):** $F_1 = 0.9800$ cents/yen.
* **$t_2$ (End of July, Close Out):** $S_2 = 0.9200$ cents/yen; $F_2 = 0.9250$ cents/yen.
* **Final Basis ($b_2$):** $S_2 - F_2 = 0.9200 - 0.9250 = \mathbf{-0.0050}$ cents/yen.
* **Effective Price Received:** $F_1 + b_2 = 0.9800 + (-0.0050) = \mathbf{0.9750 \text{ cents/yen}}$.
* **Total Amount Received:** $\text{¥}50 \text{ million} \times 0.00975 \text{ USD/yen} = \mathbf{\$487,500}$.
    *(If the spot rate had remained at 0.9800, the company would have received $\text{¥}50 \text{ million} \times 0.00980 = \$490,000$. The $\$2,500$ difference is the basis risk loss.)*

**Example 3.2: Long Hedge (Crude Oil)**

* **Exposure:** Need to **purchase 20,000 barrels** (Long Hedge) in **October/November**.
* **Contract Used:** December Crude Oil Futures (20 contracts).
* **$t_1$ (June 8):** $F_1 = \$88.00$/barrel.
* **$t_2$ (Nov 10, Close Out):** $S_2 = \$90.00$/barrel; $F_2 = \$89.10$/barrel.
* **Final Basis ($b_2$):** $S_2 - F_2 = \$90.00 - \$89.10 = \mathbf{\$0.90}$/barrel.
* **Effective Price Paid:** $F_1 + b_2 = \$88.00 + \$0.90 = \mathbf{\$88.90}$/barrel.
* **Total Price Paid:** $20,000 \text{ barrels} \times \$88.90/\text{barrel} = \mathbf{\$1,778,000}$.