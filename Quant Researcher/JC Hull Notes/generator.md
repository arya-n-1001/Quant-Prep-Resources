# 📝 Chapter 2: Mechanics of Futures Markets (Continued)

## 3. Convergence of Futures Price to Spot Price (Section 2.3)

### a. The Convergence Principle

* **General Rule:** As the delivery period for a futures contract approaches, the futures price converges to the spot price of the underlying asset.
* **At Delivery:** When the delivery period is reached, the futures price either **equals** or is **very close to** the spot price.

### b. Arbitrage Forces Driving Convergence

The convergence is enforced by arbitrage opportunities:

| Scenario | Arbitrage Action | Market Impact |
| :--- | :--- | :--- |
| **Futures Price ($F$) > Spot Price ($S$)** | 1. Sell (short) a futures contract. 2. Buy the asset. 3. Make delivery. | This risk-free profit causes the **futures price ($F$) to fall**. |
| **Futures Price ($F$) < Spot Price ($S$)** | Companies acquire the asset by entering into a long futures contract and waiting for delivery. | This demand for long positions causes the **futures price ($F$) to rise**. |

* **Result:** Arbitrage ensures that the futures price tracks the spot price closely up to the final day.

![](/assets/ch2_fig2.1.png)

---

## 4. The Operation of Margin Accounts (Section 2.4)

### a. Purpose of Margin Accounts

* **Risk Mitigation:** Margin accounts are the key mechanism used by the exchange to **avoid contract defaults** by ensuring traders have the financial resources to honor their agreements.

### b. Daily Settlement (Marking to Market)

* **Initial Margin:** The amount of funds that must be deposited by the investor when the contract is entered into.
* **Daily Settlement:** At the end of each trading day, the margin account is adjusted to reflect the investor's gain or loss. This is also known as **marking to market**.
* **Flow of Funds:** Gains and losses are settled daily between brokers and the exchange clearing house, and money flows from the losing side's broker to the winning side's broker via the clearing house.
* **Effective Contract Rewriting:** A futures contract is, in effect, **closed out and rewritten at a new price each day** (the new settlement price).

### c. Maintenance Margin and Margin Calls

* **Maintenance Margin:** A minimum account balance level, set lower than the initial margin, that must be maintained.
* **Margin Call:** If the margin account balance falls **below the maintenance margin**, the investor receives a margin call.
* **Variation Margin:** The extra funds deposited to bring the account balance back up to the **initial margin** level.
* **Default:** If the variation margin is not provided by the end of the next day, the broker **closes out the position** (neutralizes the contract).

### d. Further Details on Margin

* **Interest:** Most brokers pay interest on the balance in the margin account.
* **Alternative Collateral (Initial Margin Only):** Securities can be deposited instead of cash to satisfy initial margin:
    * Treasury bills are accepted at about $90\%$ of their face value.
    * Shares are sometimes accepted at about $50\%$ of market value.
* **Setting Minimums:** Minimum margin levels are set by the exchange clearing house and are based on the **variability** of the underlying asset's price. The maintenance margin is usually about $75\%$ of the initial margin.
* **Lower Requirements:**
    * **Bona Fide Hedgers** may face lower margin requirements due to less risk of default.
    * **Day trades** and **spread transactions** also often have lower requirements.
* **Symmetry:** Margin requirements are the **same for short futures positions as they are for long futures positions**.

### e. The Clearing House and Credit Risk

* **Clearing House Role:** Acts as an **intermediary** in all transactions, guaranteeing the performance of the parties.
* **Clearing Margin:** Clearing house members (brokers) provide initial margin to the clearing house, often calculated on a **net basis** (short positions offset against long positions).
* **Guaranty Fund:** Members contribute to a fund used if a member fails to provide variation margin, ensuring traders' contracts are honored.
* **Success:** The margining system has been highly successful; contracts at major exchanges have always been honored.