import numpy as np


N, M = map(int, input().split())

A = []
for _ in range(N):
    x = input().split()
    A.append(x)

A_arr = np.array(A, dtype=int)
print(np.max(np.min(A_arr, axis=1)))