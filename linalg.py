import numpy as np

A = np.array([2.966, 0.895], [-1.072, -2.521])
B = np.array([-1.072, -2.521])
result = np.linalg.solve(A, B)

print(result)
