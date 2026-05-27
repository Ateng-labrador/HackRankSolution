import numpy as np


N, M, P = map(int, input().split())


A = []
B = []

for _ in range(N):
    x = input().split()
    A.append(x)

for _ in range(M):
    y = input().split()
    B.append(y)

arr_A = np.array(A, int)
arr_B = np.array(B, int)

print(np.concatenate((arr_A, arr_B)))