import numpy as np

N, M = map(int, input().split())

A = []

for _ in range(N):
    x = input().split()
    A.append(x)

arr_A = np.array(A, dtype=int)

print(np.prod(np.sum(arr_A, axis=0)))
