Here is the table for **Discrete Distributions**.

| Distribution | PMF $P(X=k)$ | Mean $E[X]$ | Variance $\text{Var}(X)$ | MGF $\phi(t) = E[e^{tX}]$ |
| :--- | :--- | :--- | :--- | :--- |
| **Bernoulli($p$)** | $p^k (1-p)^{1-k}$ | $p$ | $p(1-p)$ | $1-p + pe^t$ |
| **Binomial($n, p$)** | $\binom{n}{k} p^k (1-p)^{n-k}$ | $np$ | $np(1-p)$ | $(1-p + pe^t)^n$ |
| **Poisson($\lambda$)** | $\frac{e^{-\lambda} \lambda^k}{k!}$ | $\lambda$ | $\lambda$ | $e^{\lambda(e^t - 1)}$ |
| **Geometric($p$)** | $(1-p)^{k-1} p$ | $\frac{1}{p}$ | $\frac{1-p}{p^2}$ | $\frac{pe^t}{1 - (1-p)e^t}$ |
| **Negative Binomial($r, p$)** | $\binom{k-1}{r-1} p^r (1-p)^{k-r}$ | $\frac{r}{p}$ | $\frac{r(1-p)}{p^2}$ | $\left(\frac{pe^t}{1 - (1-p)e^t}\right)^r$ |
| **Hypergeometric($N, K, n$)** | $\frac{\binom{K}{k}\binom{N-K}{n-k}}{\binom{N}{n}}$ | $n\frac{K}{N}$ | $n \frac{K}{N} \frac{N-K}{N} \frac{N-n}{N-1}$ | *(No simple closed form)* |

**Notation:**
* **$k$**: The random variable value (e.g., number of successes).
* **$n$**: Number of trials (or sample size for Hypergeometric).
* **$p$**: Probability of success.
* **$r$**: Number of successes needed (for Negative Binomial).
* **$N$**: Total population size (Hypergeometric).
* **$K$**: Total successes in the population (Hypergeometric).


Here is the table for **Continuous Distributions**.

| Distribution | PDF $f(x)$ | Mean $E[X]$ | Variance $\text{Var}(X)$ | MGF $\phi(t) = E[e^{tX}]$ |
| :--- | :--- | :--- | :--- | :--- |
| **Uniform($a, b$)** | $\frac{1}{b-a}$ | $\frac{a+b}{2}$ | $\frac{(b-a)^2}{12}$ | $\frac{e^{tb} - e^{ta}}{t(b-a)}$ |
| **Exponential($\lambda$)** | $\lambda e^{-\lambda x}$ | $\frac{1}{\lambda}$ | $\frac{1}{\lambda^2}$ | $\frac{\lambda}{\lambda - t}$ |
| **Normal($\mu, \sigma^2$)** | $\frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$ | $\mu$ | $\sigma^2$ | $e^{\mu t + \frac{1}{2}\sigma^2 t^2}$ |
| **Gamma($\alpha, \lambda$)** | $\frac{\lambda^\alpha}{\Gamma(\alpha)} x^{\alpha-1} e^{-\lambda x}$ | $\frac{\alpha}{\lambda}$ | $\frac{\alpha}{\lambda^2}$ | $\left(\frac{\lambda}{\lambda - t}\right)^\alpha$ |
| **Chi-Squared($n$)** | $\frac{1}{2^{n/2}\Gamma(n/2)} x^{\frac{n}{2}-1} e^{-\frac{x}{2}}$ | $n$ | $2n$ | $(1-2t)^{-n/2}$ |
| **Beta($\alpha, \beta$)** | $\frac{1}{B(\alpha, \beta)} x^{\alpha-1} (1-x)^{\beta-1}$ | $\frac{\alpha}{\alpha+\beta}$ | $\frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}$ | *(No simple closed form)* |
| **Cauchy($x_0, \gamma$)** | $\frac{1}{\pi\gamma [1 + (\frac{x-x_0}{\gamma})^2]}$ | **Undefined** | **Undefined** | **Does not exist** |

**Notation:**
* **$\Gamma(\alpha)$**: The Gamma function, $\Gamma(n) = (n-1)!$.
* **$B(\alpha, \beta)$**: The Beta function, a normalizing constant.
* **$t$**: MGF parameter (valid only where the integral converges, e.g., $t < \lambda$ for Exponential).