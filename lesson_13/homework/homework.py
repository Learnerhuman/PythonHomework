import numpy as np

# 1. Vector with values from 10 to 49
v1 = np.arange(10, 50)
print("1.", v1)

# 2. 3x3 matrix with values from 0 to 8
m2 = np.arange(9).reshape(3, 3)
print("\n2.\n", m2)

# 3. 3x3 identity matrix
m3 = np.eye(3)
print("\n3.\n", m3)

# 4. 3x3x3 array with random values
a4 = np.random.rand(3, 3, 3)
print("\n4.\n", a4)

# 5. 10x10 random array, min and max
a5 = np.random.rand(10, 10)
print("\n5. Min:", a5.min(), "Max:", a5.max())

# 6. Random vector of size 30, mean value
v6 = np.random.rand(30)
print("\n6. Mean:", v6.mean())

# 7. Normalize a 5x5 random matrix
m7 = np.random.rand(5, 5)
m7_norm = (m7 - m7.min()) / (m7.max() - m7.min())
print("\n7.\n", m7_norm)

# 8. Multiply a 5x3 matrix by a 3x2 matrix
A8 = np.random.rand(5, 3)
B8 = np.random.rand(3, 2)
m8 = A8 @ B8
print("\n8.\n", m8)

# 9. Dot product of two 3x3 matrices
A9 = np.random.rand(3, 3)
B9 = np.random.rand(3, 3)
m9 = np.dot(A9, B9)
print("\n9.\n", m9)

# 10. Transpose of a 4x4 matrix
m10 = np.random.rand(4, 4)
print("\n10.\n", m10.T)

# 11. Determinant of a 3x3 matrix
m11 = np.random.rand(3, 3)
det11 = np.linalg.det(m11)
print("\n11. Determinant:", det11)

# 12. Matrix product A (3x4) and B (4x3)
A12 = np.random.rand(3, 4)
B12 = np.random.rand(4, 3)
m12 = A12 @ B12
print("\n12.\n", m12)

# 13. Matrix-vector product
A13 = np.random.rand(3, 3)
v13 = np.random.rand(3, 1)
mv13 = A13 @ v13
print("\n13.\n", mv13)

# 14. Solve Ax = b
A14 = np.random.rand(3, 3)
b14 = np.random.rand(3, 1)
x14 = np.linalg.solve(A14, b14)
print("\n14.\n", x14)

# 15. Row-wise and column-wise sums of a 5x5 matrix
m15 = np.random.rand(5, 5)
row_sum = m15.sum(axis=1)
col_sum = m15.sum(axis=0)
print("\n15. Row sums:", row_sum)
print("    Column sums:", col_sum)
