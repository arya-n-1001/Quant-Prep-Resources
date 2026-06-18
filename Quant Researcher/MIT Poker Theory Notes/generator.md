## Monty Hall Problem Using Conditional Probability

Assume you initially choose **Door 1**.

Define:

- \(C_i\): the event that the car is behind Door \(i\)
- \(M_3\): the event that Monty opens Door 3 and reveals a goat

After Monty opens Door 3, switching means choosing Door 2. Therefore, we want to compute

\[
P(C_2 \mid M_3).
\]

### Step 1: Prior Probabilities

Since the car is equally likely to be behind any door,

\[
P(C_1)=P(C_2)=P(C_3)=\frac{1}{3}.
\]

### Step 2: Monty's Behavior

Assume Monty:

1. Knows where the car is.
2. Always opens a door containing a goat.
3. If he has two goat doors available, chooses randomly.

Then:

#### Case 1: Car behind Door 1

You have initially chosen the car.

Both Door 2 and Door 3 contain goats, so Monty chooses randomly between them.

\[
P(M_3 \mid C_1)=\frac{1}{2}.
\]

#### Case 2: Car behind Door 2

Door 3 is the only door Monty can open.

\[
P(M_3 \mid C_2)=1.
\]

#### Case 3: Car behind Door 3

Monty cannot open Door 3 because it contains the car.

\[
P(M_3 \mid C_3)=0.
\]

### Step 3: Compute \(P(M_3)\)

Using the Law of Total Probability,

\[
P(M_3)
=
P(M_3 \mid C_1)P(C_1)
+
P(M_3 \mid C_2)P(C_2)
+
P(M_3 \mid C_3)P(C_3).
\]

Substituting the values,

\[
P(M_3)
=
\frac{1}{2}\cdot\frac{1}{3}
+
1\cdot\frac{1}{3}
+
0\cdot\frac{1}{3}
=
\frac{1}{6}
+
\frac{1}{3}
=
\frac{1}{2}.
\]

### Step 4: Apply Bayes' Theorem

\[
P(C_2 \mid M_3)
=
\frac{P(M_3 \mid C_2)P(C_2)}
     {P(M_3)}.
\]

Substituting the values,

\[
P(C_2 \mid M_3)
=
\frac{1\cdot\frac{1}{3}}
     {\frac{1}{2}}
=
\frac{2}{3}.
\]

Therefore,

\[
\boxed{P(\text{win by switching})=\frac{2}{3}}.
\]

Similarly,

\[
P(C_1 \mid M_3)
=
\frac{\frac{1}{2}\cdot\frac{1}{3}}
     {\frac{1}{2}}
=
\frac{1}{3}.
\]

Hence, after Monty opens Door 3:

\[
P(\text{car behind your original door})=\frac{1}{3},
\]

\[
P(\text{car behind the other unopened door})=\frac{2}{3}.
\]

So switching increases your probability of winning from \(1/3\) to \(2/3\).