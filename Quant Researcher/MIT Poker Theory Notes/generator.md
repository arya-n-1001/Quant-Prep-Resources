# Chapter 6: Jointly Distributed Random Variables (Part 3)
# Sections Covered:
# 6.6 Order Statistics
# 6.7 Joint Probability Distribution of Functions of Random Variables
# 6.8 Exchangeable Random Variables

---

# Big Picture

In Parts 1 and 2, we studied:

- Joint distributions
- Marginal distributions
- Independence
- Conditional distributions
- Sums of random variables

In this final conceptual part of the chapter, we study three advanced ideas:

1. How random variables behave after being sorted
2. How to find distributions of transformed random variables
3. How symmetry can replace independence

These concepts form the foundation of modern statistics, Bayesian inference, machine learning, reliability theory, and stochastic processes.

---

# 6.6 Order Statistics

---

# Motivation

Suppose we observe

\[
X_1,X_2,\ldots,X_n
\]

and arrange them from smallest to largest.

For example,

Original sample:

\[
7,\;3,\;9,\;1,\;5
\]

Sorted sample:

\[
1,\;3,\;5,\;7,\;9
\]

These ordered values are called **order statistics**.

---

# Definition

For a sample

\[
X_1,\ldots,X_n
\]

the ordered values are denoted by

\[
X_{(1)}
\le
X_{(2)}
\le
\cdots
\le
X_{(n)}
\]

where

\[
X_{(1)}
\]

is the smallest observation and

\[
X_{(n)}
\]

is the largest observation.

---

# Example

Sample:

\[
4,\;10,\;2,\;8
\]

After ordering:

\[
2,\;4,\;8,\;10
\]

Therefore

\[
X_{(1)}=2
\]

\[
X_{(2)}=4
\]

\[
X_{(3)}=8
\]

\[
X_{(4)}=10
\]

---

# Why Order Statistics Matter

Many important quantities are order statistics.

---

## Minimum

\[
X_{(1)}
\]

Represents:

- First failure time
- Smallest observation
- Worst performance

---

## Maximum

\[
X_{(n)}
\]

Represents:

- Largest observation
- Maximum stress
- Highest score

---

## Median

Middle observation.

---

## Percentiles

Examples:

- 25th percentile
- 50th percentile
- 95th percentile

All are order statistics.

---

# Joint Density of Order Statistics

Suppose

\[
X_1,\ldots,X_n
\]

are i.i.d. continuous random variables with density

\[
f(x)
\]

Then

\[
f_{X_{(1)},\ldots,X_{(n)}}
(x_1,\ldots,x_n)
=
n!
f(x_1)f(x_2)\cdots f(x_n)
\]

for

\[
x_1<x_2<\cdots<x_n
\]

and zero otherwise. :contentReference[oaicite:0]{index=0}

---

# Why Does the Factor \(n!\) Appear?

Suppose the ordered values are

\[
x_1<x_2<\cdots<x_n
\]

Before sorting, these values could have appeared in

\[
n!
\]

different orders.

Each ordering contributes equally.

Therefore the density is multiplied by

\[
n!
\]

---

# Distribution of the j-th Order Statistic

One of the most important formulas in this section.

The density of

\[
X_{(j)}
\]

is

\[
f_{X_{(j)}}(x)
=
\frac{n!}
{(j-1)!(n-j)!}
[F(x)]^{j-1}
[1-F(x)]^{n-j}
f(x)
\]

:contentReference[oaicite:1]{index=1}

---

# Understanding the Formula

For

\[
X_{(j)}=x
\]

we require:

- \(j-1\) observations below \(x\)
- One observation at \(x\)
- \(n-j\) observations above \(x\)

Each term corresponds exactly to this requirement.

---

# Minimum Distribution

The minimum is

\[
X_{(1)}
\]

To have

\[
X_{(1)}>x
\]

all observations must exceed \(x\).

Thus

\[
P(X_{(1)}>x)
=
[1-F(x)]^n
\]

Therefore

\[
F_{X_{(1)}}(x)
=
1-[1-F(x)]^n
\]

---

# Maximum Distribution

The maximum is

\[
X_{(n)}
\]

To have

\[
X_{(n)}\le x
\]

all observations must be less than \(x\).

Hence

\[
F_{X_{(n)}}(x)
=
[F(x)]^n
\]

---

# Important Insight

As sample size increases:

- The minimum moves left
- The maximum moves right

The sample becomes more spread out.

---

# Sample Median

For a sample size

\[
2m+1
\]

the median is

\[
X_{(m+1)}
\]

the middle observation.

---

# Range

The range is defined as

\[
R
=
X_{(n)}
-
X_{(1)}
\]

---

# Interpretation

Largest value minus smallest value.

Measures overall spread.

---

# Example

Data:

\[
3,\;7,\;11,\;20
\]

Range:

\[
20-3
=
17
\]

---

# Applications of Order Statistics

Used heavily in:

- Reliability theory
- Quality control
- Survival analysis
- Statistical estimation
- Risk management

---

# 6.7 Joint Probability Distribution of Functions of Random Variables

---

# Motivation

Frequently we are not interested in the original variables.

Instead we care about functions of them.

Examples:

\[
Y=X_1+X_2
\]

Total profit.

---

\[
Y=X_1-X_2
\]

Difference in scores.

---

\[
Y_1=X_1+X_2
\]

\[
Y_2=X_1-X_2
\]

Sum and difference.

---

Question:

> How do we find the distribution of the transformed variables?

---

# Change of Variables

Suppose

\[
Y_1=g_1(X_1,X_2)
\]

\[
Y_2=g_2(X_1,X_2)
\]

and we know the joint density of

\[
X_1,X_2
\]

We want the joint density of

\[
Y_1,Y_2
\]

---

# The Jacobian

The key tool is the Jacobian determinant.

\[
J
=
\begin{vmatrix}
\dfrac{\partial y_1}{\partial x_1}
&
\dfrac{\partial y_1}{\partial x_2}
\\[1ex]
\dfrac{\partial y_2}{\partial x_1}
&
\dfrac{\partial y_2}{\partial x_2}
\end{vmatrix}
\]

---

# Transformation Formula

If the transformation is one-to-one,

\[
f_{Y_1,Y_2}(y_1,y_2)
=
f_{X_1,X_2}(x_1,x_2)
|J|^{-1}
\]

where \(x_1,x_2\) are expressed in terms of \(y_1,y_2\). :contentReference[oaicite:2]{index=2}

---

# Interpretation

The Jacobian measures how much area is stretched or compressed.

Probability mass stays constant.

Density changes to compensate.

---

# Classic Example

Define

\[
Y_1=X_1+X_2
\]

\[
Y_2=X_1-X_2
\]

Then

\[
J
=
\begin{vmatrix}
1 & 1\\
1 & -1
\end{vmatrix}
=
-2
\]

Thus

\[
|J|=2
\]

and

\[
f_{Y_1,Y_2}(y_1,y_2)
=
\frac12
f_{X_1,X_2}
\left(
\frac{y_1+y_2}{2},
\frac{y_1-y_2}{2}
\right)
\]

:contentReference[oaicite:3]{index=3}

---

# Why This Example Matters

Many advanced transformations reduce to this same pattern.

Examples:

- Sample mean and deviations
- Sum and difference
- Principal components
- Linear transformations

---

# Polar Coordinate Transformation

Suppose

\[
X=R\cos\Theta
\]

\[
Y=R\sin\Theta
\]

Then

\[
|J|=R
\]

This explains why polar-coordinate integrals contain an extra factor \(R\).

---

# Multivariable Version

For

\[
X_1,\ldots,X_n
\]

and

\[
Y_1,\ldots,Y_n
\]

the Jacobian becomes

\[
J
=
\det
\left[
\frac{\partial y_i}
{\partial x_j}
\right]
\]

and

\[
f_Y(y)
=
f_X(x)|J|^{-1}
\]

:contentReference[oaicite:4]{index=4}

---

# Important Applications

Transformation methods are used to derive:

- Gamma distribution
- Chi-square distribution
- Beta distribution
- Sampling distributions
- Multivariate normal results

---

# Example: Sum of Exponential Variables

Let

\[
Y_n=X_1+\cdots+X_n
\]

where the \(X_i\) are i.i.d. exponential.

Using transformations one obtains

\[
f_{Y_n}(y)
=
\frac{\lambda^n y^{n-1}}
{(n-1)!}
e^{-\lambda y}
\]

which is the Gamma distribution. :contentReference[oaicite:5]{index=5}

---

# 6.8 Exchangeable Random Variables

---

# Motivation

So far we have heavily used independence.

But many real systems are not independent.

Still, they may possess symmetry.

This leads to the concept of exchangeability.

---

# Definition

Random variables

\[
X_1,X_2,\ldots,X_n
\]

are said to be **exchangeable** if their joint distribution remains unchanged under every permutation.

In other words,

\[
(X_1,X_2,\ldots,X_n)
\]

has the same joint distribution as

\[
(X_{i_1},X_{i_2},\ldots,X_{i_n})
\]

for every permutation

\[
(i_1,i_2,\ldots,i_n)
\]

of

\[
(1,2,\ldots,n)
\]

:contentReference[oaicite:6]{index=6}

---

# Intuition

Exchangeability means:

> The labels do not matter.

Only the collection of values matters.

---

# Example: Fair Coin Tosses

Let

\[
X_i=
\begin{cases}
1,&\text{Head}\\
0,&\text{Tail}
\end{cases}
\]

for independent fair tosses.

Then

\[
(X_1,X_2,X_3)
\]

and

\[
(X_3,X_1,X_2)
\]

have exactly the same distribution.

Thus they are exchangeable.

---

# Relationship with Independence

Every i.i.d. collection is exchangeable.

Therefore

\[
\text{i.i.d.}
\implies
\text{Exchangeable}
\]

---

# Very Important

The converse is FALSE.

\[
\text{Exchangeable}
\nRightarrow
\text{Independent}
\]

---

# Counterexample

Suppose:

With probability

\[
\frac12
\]

all variables equal 0.

With probability

\[
\frac12
\]

all variables equal 1.

Then

\[
(X_1,\ldots,X_n)
\]

is exchangeable because order does not matter.

However,

\[
X_1,\ldots,X_n
\]

are clearly not independent.

Knowing one variable immediately reveals all others.

---

# Why Exchangeability Is Important

Exchangeability appears naturally when:

- Individuals are sampled from the same population
- Labels carry no meaning
- Symmetry assumptions are reasonable

---

# Applications

Exchangeability plays a major role in:

- Bayesian statistics
- de Finetti's theorem
- Machine learning
- Reliability theory
- Random graph models

---

# Exchangeability vs Independence

| Property | Independent | Exchangeable |
|-----------|------------|-------------|
| Labels irrelevant | Yes | Yes |
| Variables affect each other | No | Possibly |
| Joint distribution factors | Yes | Not necessarily |
| Stronger condition | Yes | No |

---

# Chapter 6 Final Conceptual Summary

The chapter can be viewed as answering four major questions:

---

## Question 1

How do multiple random variables behave together?

Answer:

- Joint distributions
- Marginal distributions
- Independence

---

## Question 2

How does information about one variable affect another?

Answer:

- Conditional distributions
- Conditional probabilities

---

## Question 3

How do we create new random variables from old ones?

Answer:

- Sums
- Transformations
- Jacobians

---

## Question 4

What special structures arise among many variables?

Answer:

- Order statistics
- Exchangeability

---

# Key Takeaway

Part 3 introduces two of the deepest ideas in probability:

1. **Order statistics**, which allow us to study minima, maxima, medians, ranges, and percentiles.

2. **Transformations and Jacobians**, which allow us to derive distributions of complicated random variables from simpler ones.

3. **Exchangeability**, which captures symmetry among random variables and serves as a bridge between independence and modern Bayesian probability.

Together, these ideas form the mathematical foundation for statistical inference, machine learning, reliability analysis, and advanced probability theory.