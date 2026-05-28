import numpy as np


N, M = map(int, input().split())

A = []
for _ in range(N):
    x = input().split()
    A.append(x)

A_arr = np.array(A, int)

print(np.mean(A_arr, axis=1))
print(np.var(A_arr, axis=0))
print(round(np.std(A_arr), 11))


