Linear Algebra: Fundamental Operators, Decompositions, and the Geometry of Data

1. Introduction: Matrices as Data Collections and Linear Operators

In the study of linear algebra, we frequently encounter a conceptual divide. The "simple" view—often the starting point of our undergraduate journey—is that a matrix is merely a structured repository for data, a rectangular arrangement of numbers used for storage and basic arithmetic. However, the more "sophisticated" view, and the one that powers modern engineering and science, treats a matrix as a linear operator. In this capacity, a matrix does not just "sit" there; it acts upon a vector space, transforming it into another.

Defining the Data Perspective

To ground this in reality, consider a dataset representing stock prices. We can index rows by companies and columns by specific dates. The resulting matrix provides a snapshot of market behavior over time.

Stock	July 1st	October 1st	September 1st
Apple	400	500	420
Morgan Stanley	500	520	510
Google	5000	5200	5100

Defining the Operator Perspective

From a theoretical standpoint, an m \times n matrix A defines a linear transformation T: \mathbb{R}^n \to \mathbb{R}^m. When we multiply a matrix by a vector, we are performing a mapping. Why does a collection of stock prices define a transformation? This is the central mystery we must unravel. By treating a dataset as an operator, we can apply geometric theories—rotation, scaling, and orientation—to raw numbers.

The "So What?" Layer

The power of this perspective lies in its ability to reveal structural stability. When we view data as an operator, we can identify which "directions" in the data are most resilient to change. To uncover these structural properties, we must identify the "anchors" of these transformations: the eigenvalues and eigenvectors.


--------------------------------------------------------------------------------


2. The Core Mechanism: Eigenvalues and Eigenvectors

Eigenvalues and eigenvectors represent the "hidden DNA" of a matrix. They provide the most simplified view of its action by identifying the directions in which the transformation is most predictable.

Formal Definition & Derivation

For a square n \times n matrix A, a scalar \lambda and a non-zero vector v are an eigenvalue and its corresponding eigenvector if they satisfy: Av = \lambda v

To solve for these, we rearrange the equation: (A - \lambda I)v = 0

For a non-trivial solution (where v \neq 0), the matrix (A - \lambda I) must not have full rank. This leads us to the characteristic equation: \det(A - \lambda I) = 0

The Characteristic Polynomial

The determinant \det(A - \lambda I) results in a polynomial of degree n in terms of \lambda. According to the fundamental theorem of algebra, this polynomial must have n roots. It is vital to note that even for matrices containing only real numbers, these roots—the eigenvalues—may be complex.

The "So What?" Layer

Geometrically, an eigenvector is a special direction that remains unchanged by the transformation A, except for a scale factor. While A might rotate or skew other vectors, it only stretches or shrinks the eigenvector by the factor \lambda. This reduces a complex n-dimensional operation into simple scalar multiplication, providing a "clear view" of the matrix's behavior.


--------------------------------------------------------------------------------


3. Matrix Diagonalization and the Importance of Symmetry

Diagonalization is a strategic method for simplifying matrix operations. By choosing a coordinate system defined by eigenvectors, the matrix acts as a simple list of scaling factors.

The Diagonalization Formula

A matrix A is diagonalizable if there exists an invertible matrix U such that: A = UDU^{-1}

* U: A matrix whose columns are the eigenvectors of A.
* D: A diagonal matrix where D_{ii} = \lambda_i.

In the "ideal" case where U is orthonormal (UU^T = I), the formula becomes A = UDU^T.

Symmetric Matrices (Theorem 2)

A symmetric matrix, where A = A^T, is the gold standard in linear algebra. It possesses a beautiful theoretical property: its eigenvalues are always real.

Proof of Real Eigenvalues:

1. Let Av = \lambda v.
2. Multiply by the complex conjugate transpose (v^H) on the left: v^H Av = v^H \lambda v = \lambda \|v\|^2.
3. Take the complex conjugate of the entire equation. Since A is real and symmetric (A = \bar{A} = A^T), we find that the left side v^H Av is equal to its own conjugate.
4. This implies \lambda \|v\|^2 = \bar{\lambda} \|v\|^2. Since v \neq 0, we must have \lambda = \bar{\lambda}, proving \lambda is real.

The "So What?" Layer

Symmetric matrices are "ideal" because they are always orthonormally diagonalizable. In real-world engineering, symmetry ensures stability; we are guaranteed real-numbered "DNA" that we can interpret physically. When you see a symmetric matrix, you should feel a sense of control over it.


--------------------------------------------------------------------------------


4. Singular Value Decomposition (SVD): The Universal Tool

While diagonalization is powerful, it is restricted to square matrices. Singular Value Decomposition (SVD) is our universal engine, capable of deconstructing any m \times n matrix.

The SVD Theorem

For any m \times n matrix A, there exists a decomposition: A = U \Sigma V^T Where U (m \times m) and V (n \times n) are orthonormal, and \Sigma (m \times n) is diagonal.

Geometric Interpretation: The Two-Frame Concept

Unlike Eigenvalue Decomposition (EVD), which works within a single frame, SVD uses two different orthonormal bases: one for the input space (V) and one for the target space (U).

* Orthonormal matrices (like U and V) represent rotations. As our guest speaker noted, these matrices give you the "cosines of the new coordinate system" relative to the old one.
* The transformation is thus: Rotate (via V^T), Scale (via \Sigma), and Rotate again (via U).

The "So What?" Layer

Why is SVD more applicable but "restricted"? It is applicable because it works for non-square data (like our stock matrix). It is "restricted" in the sense that U and V are generally different; we lose the elegance of a single coordinate frame where the matrix just "scales." However, it remains the universal tool for identifying correlations in high-dimensional data.


--------------------------------------------------------------------------------


5. Computational Methodology: SVD Step-by-Step

The SVD algorithm relies on the symmetric matrix A^T A, which allows us to use our EVD tools to solve the SVD problem.

The SVD Algorithm

1. Compute the symmetric matrix A^T A.
2. Find the eigenvalues (\lambda_i) and orthonormal eigenvectors (v_i) of A^T A. These v_i form the columns of V.
3. Calculate singular values \sigma_i = \sqrt{\lambda_i}.
4. Define u_i = Av_i / \sigma_i. These form the columns of U.

Worked Example: 2 \times 3 Matrix

Given A = \begin{bmatrix} 3 & 2 & 2 \\ 2 & 3 & -2 \end{bmatrix}:

1. A^T A: \begin{bmatrix} 13 & 12 & 2 \\ 12 & 13 & -2 \\ 2 & -2 & 8 \end{bmatrix}. Eigenvalues are \lambda_1=25, \lambda_2=9, \lambda_3=0.
2. Singular Values: \sigma_1 = 5, \sigma_2 = 3, \sigma_3 = 0.
3. Matrix V: Solving (A^T A - \lambda I)v=0 gives: v_1 = \begin{bmatrix} 1/\sqrt{2} \\ 1/\sqrt{2} \\ 0 \end{bmatrix}, v_2 = \begin{bmatrix} 1/\sqrt{18} \\ -1/\sqrt{18} \\ 4/\sqrt{18} \end{bmatrix}, v_3 = \begin{bmatrix} 2/3 \\ -2/3 \\ -1/3 \end{bmatrix}.
4. Matrix U: Using u_i = Av_i / \sigma_i: u_1 = \frac{1}{5} \begin{bmatrix} 5/\sqrt{2} \\ 5/\sqrt{2} \end{bmatrix} = \begin{bmatrix} 1/\sqrt{2} \\ 1/\sqrt{2} \end{bmatrix}, u_2 = \frac{1}{3} \begin{bmatrix} 9/\sqrt{18} \\ -9/\sqrt{18} \end{bmatrix} = \begin{bmatrix} 1/\sqrt{2} \\ -1/\sqrt{2} \end{bmatrix}.

Reduced SVD

Note that \sigma_3 = 0. The third column of V and the zero components of \Sigma contribute nothing to the product. In the Reduced SVD, we drop these irrelevant dimensions. In massive datasets (e.g., 5 companies over 365 days), the computational savings from dropping low-rank information are enormous.


--------------------------------------------------------------------------------


6. Advanced Property: The Perron-Frobenius Theorem

When a matrix consists entirely of positive entries, it exhibits a unique, deep behavior governed by the Perron-Frobenius theorem.

The Weak Form Theorem

For an n \times n matrix A (here assumed symmetric for simplicity) with strictly positive entries:

1. There exists a unique, largest real eigenvalue \lambda_0 that dominates all others (|\lambda| < \lambda_0).
2. The corresponding eigenvector has strictly positive entries.
3. The multiplicity of \lambda_0 is 1.

The "So What?" Layer

This theorem is the bridge to the Steve Ross Recovery Theorem in finance and the study of Markov Chains in probability. It guarantees that in positive systems, there is a single "dominant" state or direction that the system will inevitably favor. It is a profound result: the mere fact that all entries are positive dictates the existence of a unique, stable primary direction.


--------------------------------------------------------------------------------


7. Synthesis and Key Takeaways

We have moved from raw numbers to structural understanding. By decomposing a matrix, you aren't just doing arithmetic; you are performing a "dissection" of the data's geometry.

Essential Concepts & Formulas

* EVD: A = UDU^{-1} (Requires square, diagonalizable).
* SVD: A = U\Sigma V^T (The universal engineer's tool).
* Orthonormal Properties: UU^T = I; preserves lengths, represents pure rotation.

Common Pitfalls

* Normalizing: Forgetting to normalize eigenvectors to unit length (norm = 1) when constructing U and V.
* Complex Values: Expecting real eigenvalues for non-symmetric matrices.
* Rank: Ignoring that many real-world matrices have a "low rank," meaning most of the singular values are zero or negligible.

Exam-Level Mastery Checklist

* [ ] Can you derive (A - \lambda I)v = 0?
* [ ] Can you prove that symmetric matrices have real eigenvalues using complex conjugates?
* [ ] Can you manually execute the SVD algorithm for a small matrix?
* [ ] Can you explain the geometric role of U and V as "cosines of the new coordinate system"?

Linear algebra is no longer a classroom abstraction; it is the universal tool for deconstructing the complexity of the modern world. Use your imagination to see the geometry behind the data.
 