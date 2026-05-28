import numpy as np

N, M = map(int, input().split())

A = []
B = []
for _ in range(N):
    x = input().split()
    A.append(x)

for _ in range(N):
    x = input().split()
    B.append(x)

A_rr = np.array(A, dtype=int)
B_rr = np.array(B, dtype=int)

print(np.add(A_rr, B_rr))
print(np.subtract(A_rr, B_rr))
print(np.multiply(A_rr, B_rr))
print(A_rr // B_rr)
print(np.mod(A_rr, B_rr))
print(np.power(A_rr, B_rr))
