# **Chapter 4: Random Variables (Sections 4.8 – 4.10)**

## **4.8 Other Discrete Probability Distributions**

### **4.8.1 The Geometric Random Variable**
Represents the number of independent trials required to get the **first success**.
*   **Definition:** Independent trials, each with success probability $p$. $X$ is the trial number of the first success.
*   **PMF:**
    $$ P(X=n) = (1-p)^{n-1}p, \quad n=1, 2, \dots $$
*   **Properties:**
    *   $\sum P(X=n) = 1$ (Success eventually occurs with probability 1).
    *   **Expected Value:** $E[X] = \frac{1}{p}$
        *   *Example:* Expected rolls of a fair die to get a 1 is $1/(1/6) = 6$.
    *   **Variance:** $\text{Var}(X) = \frac{1-p}{p^2}$
    *   **Tail Probability:** $P(X > k) = (1-p)^k$ (Prob that first $k$ trials are failures).

### **4.8.2 The Negative Binomial Random Variable**
Represents the number of trials required to accumulate a total of **$r$ successes**.
*   **Definition:** Generalization of Geometric ($r=1$). $X$ is the trial number of the $r$-th success.
*   **PMF:**
    $$ P(X=n) = \binom{n-1}{r-1} p^r (1-p)^{n-r}, \quad n=r, r+1, \dots $$
    *   *Logic:* For the $r$-th success to happen on trial $n$, the first $n-1$ trials must contain exactly $r-1$ successes, and the $n$-th trial must be a success.
*   **Relationship:** $X$ can be written as the sum of $r$ independent geometric random variables $X_1 + \dots + X_r$.
*   **Properties:**
    *   **Expected Value:** $E[X] = \frac{r}{p}$
    *   **Variance:** $\text{Var}(X) = \frac{r(1-p)}{p^2}$
*   **Banach Match Problem:** A classic example involving two matchboxes, solved using negative binomial concepts to find the prob that the other box has $k$ matches when one becomes empty.

### **4.8.3 The Hypergeometric Random Variable**
Models sampling **without replacement** from a finite population.
*   **Scenario:** Urn with $N$ balls, $m$ are white, $N-m$ are black. Select $n$ balls. $X$ is the number of white balls selected.
*   **PMF:**
    $$ P(X=i) = \frac{\binom{m}{i}\binom{N-m}{n-i}}{\binom{N}{n}}, \quad i=0, \dots, n $$
*   **Properties:**
    *   **Expected Value:** $E[X] = \frac{nm}{N} = np$ (where $p=m/N$).
        *   *Note:* Same mean as Binomial, even though trials are dependent.
    *   **Variance:** $\text{Var}(X) = np(1-p) \left( \frac{N-n}{N-1} \right)$
        *   The term $\frac{N-n}{N-1}$ is the **finite population correction factor**. As $N \to \infty$, this approaches 1, and the variance approaches the Binomial variance.

### **4.8.4 The Zeta (Zipf) Distribution**
Used to model size/frequency data (e.g., word frequency, city populations).
*   **PMF:**
    $$ P(X=k) = \frac{C}{k^{\alpha+1}}, \quad k=1, 2, \dots $$
    *   Where $\alpha > 0$ and $C = \left[ \sum_{k=1}^\infty (1/k)^{\alpha+1} \right]^{-1}$ (related to the Riemann Zeta function).

***

## **4.9 Expected Value of Sums of Random Variables**
One of the most useful properties in probability theory.

### **Linearity of Expectation**
For any random variables $X_1, X_2, \dots, X_n$ (dependent or independent):
$$ E\left[ \sum_{i=1}^n X_i \right] = \sum_{i=1}^n E[X_i] $$
*   *Proof:* Based on the fact that $E[X] = \sum_{s \in S} X(s)p(s)$. By reordering the summation over outcomes $s$, the sum of expectations emerges naturally.

### **Applications**
1.  **Sum of Dice:** Rolling $n$ dice. $E[\text{Sum}] = n \times 3.5 = 3.5n$.
2.  **Binomial Mean:** $X = \sum X_i$ (indicator variables). $E[X] = \sum p = np$.
3.  **Hypergeometric Mean:** Even though trials are dependent (sampling without replacement), the probability of success on the $i$-th draw is still $m/N$. Thus $E[X] = n(m/N)$.
4.  **Coupon Collector's Problem:** (From previous sections, usually solved using sums of Geometric variables).

### **Variance of Sums**
Unlike expectation, variance is **not** generally linear.
$$ E\left[ \left( \sum X_i \right)^2 \right] = \sum E[X_i^2] + \sum_{i \ne j} E[X_i X_j] $$
*   If $X_i$ are independent (or uncorrelated), cross terms simplify, and $\text{Var}(\sum X_i) = \sum \text{Var}(X_i)$.
*   For Hypergeometric (dependent trials), the covariance terms lead to the finite population correction factor derived in section 4.8.3.

***

## **4.10 Properties of the Cumulative Distribution Function (CDF)**
The CDF $F(b) = P(X \le b)$ characterizes the random variable.

### **Properties**
1.  **Non-decreasing:** If $a < b$, then $F(a) \le F(b)$.
2.  **Limits:** $\lim_{b \to \infty} F(b) = 1$ and $\lim_{b \to -\infty} F(b) = 0$.
3.  **Right Continuous:** $\lim_{n \to \infty} F(b_n) = F(b)$ for decreasing sequence $b_n \to b$.

### **Computing Probabilities from F**
*   $P(a < X \le b) = F(b) - F(a)$
*   $P(X < b) = \lim_{h \to 0^+} F(b-h)$ (Left limit)
*   $P(X = b) = F(b) - \lim_{h \to 0^+} F(b-h)$ (Jump size at $b$)

### **Example**
Given a step function $F(x)$:
*   $P(X < 3)$ is the value of $F$ just before 3.
*   $P(X = 1)$ is the size of the jump at 1: $F(1) - F(1^-)$.
*   $P(X > 1/2) = 1 - F(1/2)$.

***

## **Chapter Summary (Key Formulas)**

| Distribution | PMF $P(X=k)$ | Mean $E[X]$ | Variance $\text{Var}(X)$ |
| :--- | :--- | :--- | :--- |
| **Binomial** | $\binom{n}{k} p^k (1-p)^{n-k}$ | $np$ | $np(1-p)$ |
| **Poisson** | $e^{-\lambda} \lambda^k / k!$ | $\lambda$ | $\lambda$ |
| **Geometric** | $(1-p)^{k-1}p$ | $1/p$ | $(1-p)/p^2$ |
| **Neg. Binomial** | $\binom{k-1}{r-1} p^r (1-p)^{k-r}$ | $r/p$ | $r(1-p)/p^2$ |
| **Hypergeometric** | $\frac{\binom{m}{k}\binom{N-m}{n-k}}{\binom{N}{n}}$ | $\frac{nm}{N}$ | $np(1-p) \frac{N-n}{N-1}$ |