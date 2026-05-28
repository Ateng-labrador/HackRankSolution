import numpy as np

N = input()

A = np.array([input().split() for _ in range(int(N))], dtype=int)
B = np.array([input().split() for _ in range(int(N))], dtype=int)


print(np.dot(A, B))
# res = []
# for i in range(int(N)):
#     row = []
#     for j in range(int(N)):
#         total = 0
#         for k in range(int(N)):
#             total += A[i][k] * B[k][j]
#         row.append(row)
#     res.append(row)